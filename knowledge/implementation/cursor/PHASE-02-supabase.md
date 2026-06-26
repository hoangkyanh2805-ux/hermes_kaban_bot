# Cursor Prompt — Phase 2: Supabase Schema

## Context

Phase 2 per P2-* in [knowledge/tasks/PHASE-TASKS.md](../../tasks/PHASE-TASKS.md). Spec: [docs/06-supabase-schema.md](../../../docs/06-supabase-schema.md).

## Your task

1. `supabase/migrations/001_content_pipeline.sql` — full DDL for pipeline_runs, topics, scripts, x_posts, indexes, FKs
2. `supabase/policies/rls_agent_ownership.sql` — RLS per [docs/AGENT-OS.md §7](../../../docs/AGENT-OS.md)
3. `supabase/README.md` — apply instructions + link to [knowledge/prompts/supabase-schema-setup.md](../../prompts/supabase-schema-setup.md)
4. `schemas/topic.json`, `script.json`, `x_post.json`, `pipeline_run.json` — JSON Schema matching columns
5. `runbooks/03-supabase-schema.md`
6. `tests/test_schema_sql.py` — lint that migration file exists and contains required table names (no DB connection required for CI)

## Rules

- `x_posts.signals_applied` MUST be JSONB NOT NULL
- Unique: `(pipeline_run_id, title)` on topics
- Match [docs/06-supabase-schema.md](../../../docs/06-supabase-schema.md) exactly

## Do NOT

- Put service role keys in SQL files
- Create application Python beyond schema tests

## Acceptance

M3 checklist in [knowledge/checklists/phase-gates.md](../../checklists/phase-gates.md)
