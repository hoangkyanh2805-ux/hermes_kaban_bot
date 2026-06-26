#!/usr/bin/env python3
"""Export a Phoenix-compliant x_post from Supabase for manual X publishing."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

# Reuse Supabase + validation from verify script
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_supabase import (  # noqa: E402
    REPO_ROOT,
    load_dotenv,
    parse_json_field,
    supabase_get,
    thread_texts,
    validate_x_post,
)


def pick_post(
    rows: list[dict[str, Any]],
    *,
    id_prefix: str | None = None,
) -> dict[str, Any] | None:
    if id_prefix:
        for row in rows:
            if str(row.get("id", "")).startswith(id_prefix):
                return row
        return None

    passing = [r for r in rows if not validate_x_post(r)]
    if passing:
        return passing[0]

    for row in rows:
        if not validate_x_post(row):
            return row
    return rows[0] if rows else None


def format_publish_pack(row: dict[str, Any]) -> str:
    thread = parse_json_field(row.get("thread"))
    texts = thread_texts(thread)
    signals = parse_json_field(row.get("signals_applied"))
    lines = [
        "=" * 60,
        f"x_post id: {row.get('id')}",
        f"virality_score: {row.get('virality_score')}",
        f"suggested_post_time: {row.get('suggested_post_time')}",
        "=" * 60,
        "",
        "── ROOT POST (copy → đăng tweet đầu) ──",
        "",
        (row.get("main_post") or "").strip(),
        "",
    ]
    for i, text in enumerate(texts):
        if i == 0:
            continue  # root often duplicates main_post
        lines.extend([f"── REPLY {i} ──", "", text.strip(), ""])
    lines.extend(
        [
            "── signals_applied ──",
            json.dumps(signals, indent=2, ensure_ascii=False),
            "",
            "── Publish checklist ──",
            "[ ] Root post không có https://",
            "[ ] Reply 1 có link nguồn",
            "[ ] Đăng trong khung 07–09h hoặc 18–20h (VN)",
            "[ ] Theo dõi 15 phút đầu — mục tiêu 5+ replies",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    load_dotenv(REPO_ROOT / ".env")

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="Export x_post ready to publish on X.")
    parser.add_argument("--url", default=os.environ.get("SUPABASE_URL"))
    parser.add_argument("--key", default=os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))
    parser.add_argument("--id", dest="id_prefix", help="x_post UUID prefix (e.g. 542c)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args(argv)

    if not args.url or not args.key:
        print("Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY.", file=sys.stderr)
        return 2

    rows = supabase_get(
        args.url,
        args.key,
        "x_posts",
        select="id,script_id,main_post,thread,virality_score,signals_applied,suggested_post_time",
        order="virality_score.desc.nullslast",
        limit=20,
    )

    row = pick_post(rows, id_prefix=args.id_prefix)
    if not row:
        print("No x_posts found.", file=sys.stderr)
        return 1

    errs = validate_x_post(row)
    if errs:
        print(f"Warning: post {str(row.get('id'))[:8]} fails Phoenix gates:", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        print(file=sys.stderr)

    if args.json:
        print(json.dumps(row, indent=2, ensure_ascii=False))
    else:
        print(format_publish_pack(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
