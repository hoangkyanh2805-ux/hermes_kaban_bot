# Prompt: Supabase Schema Setup

**Phase 2** · SOP-02

## Part A — Install skill

Send via Telegram:

---

Install the Supabase agent skill. My project URL is: `{SUPABASE_URL}` and my service role key is: `{SUPABASE_SERVICE_ROLE_KEY}`

Confirm the connection works.

---

## Part B — Create schema

Send via Telegram:

---

Create four tables for my content pipeline with foreign keys linking each stage:

1. **pipeline_runs** — id, trigger (manual/cron), status, kanban_root_task_id, topics_researched, topics_produced, packages_produced, error_summary, started_at, completed_at

2. **topics** — id, pipeline_run_id (FK), title, trending_score (1-100), audience, source_urls (JSONB), created_at

3. **scripts** — id, topic_id (FK), full_script, structure (JSONB), status (draft/final), created_at

4. **x_posts** — id, script_id (FK), main_post, thread (JSONB), virality_score, signals_applied (JSONB), suggested_post_time, created_at

Add RLS policies so:
- research-agent writes only to topics
- script-agent writes only to scripts
- x-optimizer-agent writes only to x_posts
- storage-agent updates pipeline_runs and can read all tables

Use the service role for agent writes with RLS enforcing ownership.

---

## Alternative (khuyến nghị)

Apply SQL từ repo trong Supabase SQL Editor — theo thứ tự:

1. `supabase/migrations/001_content_pipeline.sql`
2. `supabase/policies/rls_agent_ownership.sql`

Runbook: [runbooks/03-supabase-schema.md](../../runbooks/03-supabase-schema.md) · Spec: [docs/06-supabase-schema.md](../../docs/06-supabase-schema.md)

## Verify

- [ ] Four tables in dashboard
- [ ] `signals_applied` is JSONB on x_posts
- [ ] RLS enabled
