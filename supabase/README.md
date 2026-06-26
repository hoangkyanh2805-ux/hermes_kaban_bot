# Supabase — Content Pipeline Schema

DDL source of truth for the four pipeline tables. Spec: [docs/06-supabase-schema.md](../docs/06-supabase-schema.md).

## Files

| File | Purpose |
|------|---------|
| `migrations/001_content_pipeline.sql` | Tables, FKs, indexes, CHECK constraints |
| `policies/rls_agent_ownership.sql` | RLS per agent role ([AGENT-OS §7](../docs/AGENT-OS.md)) |
| `../schemas/*.json` | JSON Schema for row validation in agents/tests |

## Quick apply (Supabase Dashboard)

1. Create a project at [supabase.plug.dev/ykdVN09](https://supabase.plug.dev/ykdVN09) (or your own org).
2. Open **SQL Editor** → **New query**.
3. Paste and run **`migrations/001_content_pipeline.sql`** → Success.
4. Paste and run **`policies/rls_agent_ownership.sql`** → Success.
5. **Table Editor** → confirm: `pipeline_runs`, `topics`, `scripts`, `x_posts`.
6. Copy **Project URL** + **service role key** → Railway Variables:
   - `SUPABASE_URL`
   - `SUPABASE_SERVICE_ROLE_KEY`

Detailed runbook (Vietnamese): [runbooks/03-supabase-schema.md](../runbooks/03-supabase-schema.md).

## Apply via Supabase CLI (optional)

```bash
# From repo root, with linked project:
supabase db push
# Or run files manually:
psql "$DATABASE_URL" -f supabase/migrations/001_content_pipeline.sql
psql "$DATABASE_URL" -f supabase/policies/rls_agent_ownership.sql
```

## Verify schema

Run in SQL Editor:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN ('pipeline_runs', 'topics', 'scripts', 'x_posts')
ORDER BY table_name;

SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'x_posts'
  AND column_name = 'signals_applied';

SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public'
  AND tablename IN ('pipeline_runs', 'topics', 'scripts', 'x_posts');
```

Expected: 4 tables; `signals_applied` = `jsonb` NOT NULL; `rowsecurity` = `true` on all four.

## Smoke insert (manual)

```sql
INSERT INTO pipeline_runs (trigger, status, kanban_root_task_id)
VALUES ('manual', 'pending', 'test-root-001')
RETURNING id;
-- Use returned id as pipeline_run_id for topics, etc.
```

## RLS and Hermes Supabase skill

Hermes agents typically connect with the **service role** key (`SUPABASE_SERVICE_ROLE_KEY`). In Supabase, **service_role bypasses RLS**.

The policies in `policies/rls_agent_ownership.sql` still matter for:

- Future scoped JWT keys per agent (`agent_role` claim)
- Human dashboard access with `authenticated` role
- Defense in depth if you stop using service role for writes

Agent ownership matrix (who may write what):

| Agent | Tables (write) |
|-------|----------------|
| research-agent | `topics`; `pipeline_runs.started_at` only |
| script-agent | `scripts` |
| x-optimizer-agent | `x_posts` |
| storage-agent | `pipeline_runs` |
| pipeline-seeder | `pipeline_runs` INSERT |

## Telegram alternative

To let Hermes create schema via conversation instead of SQL Editor, use [knowledge/prompts/supabase-schema-setup.md](../knowledge/prompts/supabase-schema-setup.md). **Recommended:** apply SQL from this repo (reproducible, versioned).

## Next phase

- Install Supabase skill on Railway Hermes ([skills/INSTALL.md](../skills/INSTALL.md))
- Phase 3: TinyFish + research agent — [runbooks/04-research-agent.md](../runbooks/04-research-agent.md)
