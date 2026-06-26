# 12 — Manual X Publish (v1)

**Decision record** · Accepted for v1 · Not a bug

---

## Policy

| Scope | v1 | v2 (future) |
|-------|-----|-------------|
| Research → script → optimize | Automated (Hermes agents) | Same |
| Persist to Supabase | Automated | Same |
| **Post to X** | **Manual — human operator** | Optional X API agent |

Pipeline **ends at `x_posts`**. Publishing is an **operator step** outside Hermes.

Rationale (from [AGENTS.md](../AGENTS.md)):

- Human review before public post
- No X API credentials in v1
- Avoid auto-post mistakes / hallucinated links
- Matches Derek Cheung tutorial scope

---

## Operator workflow

```text
Weekly cron / manual run
        ↓
Supabase x_posts (Phoenix-compliant)
        ↓
python scripts/export_x_post.py [--id PREFIX]
        ↓
Copy ROOT → X compose
Reply 1 → link (thread[1])
Reply 2 → insight
Reply 3 → CTA
        ↓
Log in ops/publish-log.md (optional)
```

---

## Export command

```bash
# Best Phoenix pass, highest virality
python scripts/export_x_post.py

# Specific package
python scripts/export_x_post.py --id 542c
python scripts/export_x_post.py --id 9ecc
```

Verify before export:

```bash
python scripts/verify_supabase.py
```

---

## Publish checklist (per post)

- [ ] `main_post` has **no** `https://`
- [ ] Link only in **first reply** (thread index 1)
- [ ] `signals_applied` includes `algorithm_version: phoenix-2026`
- [ ] Posted in 07:00–09:00 or 18:00–20:00 operator TZ (or `suggested_post_time`)
- [ ] First 15 min: reply to comments (author-reply signal)
- [ ] Recorded in [ops/publish-log.md](../ops/publish-log.md)

---

## What agents must NOT do (v1)

- Call X API to create tweets
- Auto-schedule via third-party without human copy-paste
- Mark `x_posts` as published in DB (no column in v1 schema)

---

## Related docs

| Doc | Purpose |
|-----|---------|
| [runbooks/10-go-live.md](../runbooks/10-go-live.md) | First trial publish |
| [docs/09-x-algorithm-rules.md](09-x-algorithm-rules.md) | Phoenix gates |
| [knowledge/sops/SOP-09-manual-x-publish.md](../knowledge/sops/SOP-09-manual-x-publish.md) | Short SOP |

---

## v2 extension (not implemented)

Add only with explicit request:

- `x-publisher-agent` profile
- X API OAuth env vars
- Human approval gate in Telegram before post
- Optional `x_posts.published_at` migration

See [PROJECT-OS.md §15](PROJECT-OS.md) — auto-post to X listed as post-v1 extension.
