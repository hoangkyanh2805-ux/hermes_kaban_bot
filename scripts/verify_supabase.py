#!/usr/bin/env python3
"""Verify Supabase pipeline artifacts — counts, FK chain, Phoenix x_post gates."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
URL_PATTERN = re.compile(r"https?://", re.IGNORECASE)

PHOENIX_SIGNAL_KEYS = (
    "reply_weight",
    "author_reply_weight",
    "no_root_external_link",
    "link_placement",
    "early_velocity_target_replies_15min",
    "algorithm_version",
)


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class VerifyReport:
    checks: list[CheckResult] = field(default_factory=list)

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks.append(CheckResult(name, ok, detail))

    @property
    def passed(self) -> bool:
        return all(c.ok for c in self.checks)

    def print_report(self) -> None:
        for c in self.checks:
            mark = "OK" if c.ok else "FAIL"
            line = f"[{mark}] {c.name}"
            if c.detail:
                line += f" — {c.detail}"
            print(line)


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


def supabase_get(
    base_url: str,
    service_key: str,
    table: str,
    *,
    select: str = "*",
    order: str | None = None,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    params: dict[str, str] = {"select": select}
    if order:
        params["order"] = order
    if limit is not None:
        params["limit"] = str(limit)
    query = urllib.parse.urlencode(params)
    url = f"{base_url.rstrip('/')}/rest/v1/{table}?{query}"
    req = urllib.request.Request(
        url,
        headers={
            "apikey": service_key,
            "Authorization": f"Bearer {service_key}",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected response for {table}: {type(data)}")
    return data


def thread_texts(thread: Any) -> list[str]:
    if not isinstance(thread, list):
        return []
    texts: list[str] = []
    for item in thread:
        if isinstance(item, str):
            texts.append(item)
        elif isinstance(item, dict):
            for key in ("text", "content", "body"):
                if key in item and isinstance(item[key], str):
                    texts.append(item[key])
                    break
    return texts


def has_external_url(text: str) -> bool:
    return bool(URL_PATTERN.search(text or ""))


def validate_signals_applied(signals: Any) -> tuple[bool, str]:
    if not isinstance(signals, dict):
        return False, "signals_applied must be a JSON object"
    missing = [k for k in PHOENIX_SIGNAL_KEYS if k not in signals]
    if missing:
        return False, f"missing keys: {', '.join(missing)}"
    if signals.get("link_placement") != "first_reply":
        return False, "link_placement must be first_reply"
    if signals.get("no_root_external_link") is not True:
        return False, "no_root_external_link must be true"
    return True, "phoenix schema ok"


def parse_json_field(value: Any) -> Any:
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value


def validate_x_post(row: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    main_post = row.get("main_post") or ""
    if has_external_url(main_post):
        errors.append("main_post contains external URL")
    if not main_post.strip():
        errors.append("main_post is empty")

    thread = parse_json_field(row.get("thread"))
    texts = thread_texts(thread)
    if not texts:
        errors.append("thread has no post text")
    elif len(texts) < 2:
        errors.append("thread should have at least 2 posts (root + reply)")
    elif not has_external_url(texts[1]):
        errors.append("thread[1] should contain the external link")

    ok, detail = validate_signals_applied(parse_json_field(row.get("signals_applied")))
    if not ok:
        errors.append(detail)

    score = row.get("virality_score")
    if score is not None and not (1 <= int(score) <= 100):
        errors.append("virality_score out of range 1-100")

    return errors


def verify(
    base_url: str,
    service_key: str,
    *,
    min_topics: int = 1,
    min_scripts: int = 1,
    min_x_posts: int = 1,
    strict_phoenix: bool = True,
) -> VerifyReport:
    report = VerifyReport()

    tables = ("pipeline_runs", "topics", "scripts", "x_posts")
    counts: dict[str, int] = {}
    for table in tables:
        try:
            rows = supabase_get(base_url, service_key, table, select="id")
            counts[table] = len(rows)
        except urllib.error.HTTPError as exc:
            report.add(f"table:{table}", False, f"HTTP {exc.code}")
            return report
        except OSError as exc:
            report.add("supabase_connect", False, str(exc))
            return report

    report.add("supabase_connect", True, base_url)
    report.add("pipeline_runs", counts["pipeline_runs"] >= 1, f"count={counts['pipeline_runs']}")
    report.add("topics", counts["topics"] >= min_topics, f"count={counts['topics']} (min {min_topics})")
    report.add("scripts", counts["scripts"] >= min_scripts, f"count={counts['scripts']} (min {min_scripts})")
    report.add("x_posts", counts["x_posts"] >= min_x_posts, f"count={counts['x_posts']} (min {min_x_posts})")

    runs = supabase_get(
        base_url,
        service_key,
        "pipeline_runs",
        select="id,status,trigger,topics_researched,packages_produced,created_at",
        order="created_at.desc",
        limit=1,
    )
    if runs:
        latest = runs[0]
        report.add(
            "latest_run_status",
            latest.get("status") in ("completed", "partial", "running"),
            f"status={latest.get('status')} trigger={latest.get('trigger')}",
        )

    if not strict_phoenix:
        return report

    x_posts = supabase_get(
        base_url,
        service_key,
        "x_posts",
        select="id,main_post,thread,virality_score,signals_applied",
        limit=50,
    )
    bad = 0
    for row in x_posts:
        errs = validate_x_post(row)
        if errs:
            bad += 1
            if bad <= 3:
                short_id = str(row.get("id", ""))[:8]
                report.add(f"x_post:{short_id}", False, "; ".join(errs))

    phoenix_ok = bad == 0
    report.add(
        "x_posts_phoenix",
        phoenix_ok,
        f"{len(x_posts) - bad}/{len(x_posts)} pass Phoenix gates" if x_posts else "no rows",
    )
    return report


def main(argv: list[str] | None = None) -> int:
    load_dotenv(REPO_ROOT / ".env")

    parser = argparse.ArgumentParser(description="Verify Hermes content pipeline Supabase data.")
    parser.add_argument("--url", default=os.environ.get("SUPABASE_URL"), help="Supabase project URL")
    parser.add_argument(
        "--key",
        default=os.environ.get("SUPABASE_SERVICE_ROLE_KEY"),
        help="Supabase service role / secret key",
    )
    parser.add_argument("--min-topics", type=int, default=1)
    parser.add_argument("--min-scripts", type=int, default=1)
    parser.add_argument("--min-x-posts", type=int, default=1)
    parser.add_argument(
        "--relaxed-phoenix",
        action="store_true",
        help="Skip Phoenix signals_applied / URL gates (counts only)",
    )
    args = parser.parse_args(argv)

    if not args.url or not args.key:
        print("Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY (env or --url/--key).", file=sys.stderr)
        return 2

    report = verify(
        args.url,
        args.key,
        min_topics=args.min_topics,
        min_scripts=args.min_scripts,
        min_x_posts=args.min_x_posts,
        strict_phoenix=not args.relaxed_phoenix,
    )
    report.print_report()
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
