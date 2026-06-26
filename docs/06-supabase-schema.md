# 06 — Supabase Schema Specification

DDL source of truth for Phase 2 implementation. Apply via `supabase/migrations/001_content_pipeline.sql`.

Reference: [PROJECT-OS.md Appendix A](PROJECT-OS.md) · [AGENT-OS.md §7](AGENT-OS.md)

---

## Tables

### pipeline_runs

| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK DEFAULT gen_random_uuid() | |
| trigger | text CHECK (manual, cron) | |
| status | text CHECK (pending, running, completed, partial, failed) | |
| stage | text | Latest pipeline stage |
| kanban_root_task_id | text UNIQUE | Hermes task id |
| topics_researched | int DEFAULT 0 | |
| topics_produced | int DEFAULT 0 | |
| packages_produced | int DEFAULT 0 | |
| error_summary | text | |
| started_at | timestamptz | |
| completed_at | timestamptz | |
| created_at | timestamptz DEFAULT now() | |

### topics

| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | |
| pipeline_run_id | uuid FK → pipeline_runs ON DELETE CASCADE | |
| title | text NOT NULL | |
| trending_score | int CHECK (1–100) | |
| audience | text | |
| source_urls | jsonb DEFAULT '[]' | TinyFish citations |
| created_at | timestamptz DEFAULT now() | |

**Unique:** `(pipeline_run_id, title)`

### scripts

| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | |
| topic_id | uuid FK → topics ON DELETE CASCADE | |
| full_script | text | |
| structure | jsonb | Section map |
| status | text CHECK (draft, final) DEFAULT draft | |
| created_at | timestamptz DEFAULT now() | |

**Unique:** `(topic_id)` per run

### x_posts

| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | |
| script_id | uuid FK → scripts ON DELETE CASCADE | |
| main_post | text NOT NULL | No root URLs |
| thread | jsonb NOT NULL | Array of posts |
| virality_score | int CHECK (1–100) | |
| signals_applied | jsonb NOT NULL | Algorithm metadata |
| suggested_post_time | timestamptz | |
| created_at | timestamptz DEFAULT now() | |

**Unique:** `(script_id)`

---

## RLS policies

| Role claim | topics | scripts | x_posts | pipeline_runs |
|------------|--------|---------|---------|---------------|
| research-agent | INSERT, UPDATE | — | — | UPDATE started_at only |
| script-agent | SELECT | INSERT, UPDATE | — | SELECT |
| x-optimizer-agent | SELECT | SELECT | INSERT, UPDATE | SELECT |
| storage-agent | SELECT | SELECT | SELECT | INSERT, UPDATE |

Implement via `auth.jwt() ->> 'agent_role'` or service-role + policy per agent API key pattern used by Supabase skill.

---

## Indexes

```sql
CREATE INDEX idx_topics_run_score ON topics (pipeline_run_id, trending_score DESC);
CREATE INDEX idx_scripts_topic ON scripts (topic_id);
CREATE INDEX idx_x_posts_script ON x_posts (script_id);
CREATE INDEX idx_pipeline_runs_status ON pipeline_runs (status);
```

---

## Migration file

Implementation phase creates: `supabase/migrations/001_content_pipeline.sql` matching this spec.
