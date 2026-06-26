# Claude Code Prompt — Phase 2: Supabase

Implement Phase 2 per `docs/06-supabase-schema.md` and `knowledge/tasks/PHASE-TASKS.md` P2-*.

Create:
- `supabase/migrations/001_content_pipeline.sql`
- `supabase/policies/rls_agent_ownership.sql`
- `supabase/README.md`
- `schemas/*.json` (4 files)
- `runbooks/03-supabase-schema.md`
- `tests/test_schema_sql.py`

Tables: pipeline_runs, topics, scripts, x_posts. signals_applied JSONB required.

No API keys in SQL. Match AGENT-OS §7 ownership matrix.

Gate: M3 in `knowledge/checklists/phase-gates.md`.
