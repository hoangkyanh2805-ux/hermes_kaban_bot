# SOP-09: Manual X Publish

**Post-M7** · Operator step · v1 scope lock

## Purpose

Document that **publishing to X is manual** after the pipeline writes `x_posts` to Supabase.

## Prerequisites

- At least one Phoenix-compliant `x_posts` row (`python scripts/verify_supabase.py`)
- [docs/12-manual-x-publish.md](../../docs/12-manual-x-publish.md)

## Procedure

1. Export: `python scripts/export_x_post.py` (or `--id PREFIX`).
2. Open X → compose **root** from export (no URLs).
3. Reply with thread posts in order (link in reply 1).
4. Engage first 15 minutes (target 5+ replies).
5. Log date + `x_post` id in [ops/publish-log.md](../../ops/publish-log.md).

## Out of scope (v1)

- X API auto-post
- Hermes agent posting on behalf of operator

## Next

[SOP-07 Weekly cron](SOP-07-weekly-cron.md) — pipeline keeps producing; operator publishes top packages.
