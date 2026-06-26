-- Hermes Content Pipeline — Phase 2 DDL
-- Spec: docs/06-supabase-schema.md · Ownership: docs/AGENT-OS.md §7
-- Apply before: supabase/policies/rls_agent_ownership.sql

BEGIN;

-- ---------------------------------------------------------------------------
-- pipeline_runs — one row per weekly/manual Kanban root task
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.pipeline_runs (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    trigger text NOT NULL
        CONSTRAINT pipeline_runs_trigger_check
        CHECK (trigger IN ('manual', 'cron')),
    status text NOT NULL DEFAULT 'pending'
        CONSTRAINT pipeline_runs_status_check
        CHECK (status IN ('pending', 'running', 'completed', 'partial', 'failed')),
    stage text,
    kanban_root_task_id text UNIQUE,
    topics_researched integer NOT NULL DEFAULT 0,
    topics_produced integer NOT NULL DEFAULT 0,
    packages_produced integer NOT NULL DEFAULT 0,
    error_summary text,
    started_at timestamptz,
    completed_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE public.pipeline_runs IS
    'Authoritative run record; StorageAgent owns INSERT/UPDATE.';

-- ---------------------------------------------------------------------------
-- topics — research output (TinyFish citations in source_urls)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.topics (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pipeline_run_id uuid NOT NULL
        REFERENCES public.pipeline_runs (id) ON DELETE CASCADE,
    title text NOT NULL,
    trending_score integer
        CONSTRAINT topics_trending_score_check
        CHECK (trending_score IS NULL OR (trending_score >= 1 AND trending_score <= 100)),
    audience text,
    source_urls jsonb NOT NULL DEFAULT '[]'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT topics_pipeline_run_title_unique UNIQUE (pipeline_run_id, title)
);

COMMENT ON TABLE public.topics IS
    'ResearchAgent INSERT/UPDATE; all agents may SELECT.';

-- ---------------------------------------------------------------------------
-- scripts — one draft/final script per topic
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.scripts (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    topic_id uuid NOT NULL
        REFERENCES public.topics (id) ON DELETE CASCADE,
    full_script text,
    structure jsonb,
    status text NOT NULL DEFAULT 'draft'
        CONSTRAINT scripts_status_check
        CHECK (status IN ('draft', 'final')),
    created_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT scripts_topic_id_unique UNIQUE (topic_id)
);

COMMENT ON TABLE public.scripts IS
    'ScriptAgent INSERT/UPDATE; Script/XOpt/Storage SELECT.';

-- ---------------------------------------------------------------------------
-- x_posts — optimized X thread package per script
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.x_posts (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    script_id uuid NOT NULL
        REFERENCES public.scripts (id) ON DELETE CASCADE,
    main_post text NOT NULL,
    thread jsonb NOT NULL,
    virality_score integer
        CONSTRAINT x_posts_virality_score_check
        CHECK (virality_score IS NULL OR (virality_score >= 1 AND virality_score <= 100)),
    signals_applied jsonb NOT NULL,
    suggested_post_time timestamptz,
    created_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT x_posts_script_id_unique UNIQUE (script_id)
);

COMMENT ON TABLE public.x_posts IS
    'XOptimizerAgent INSERT/UPDATE; signals_applied required (Phoenix rules).';

COMMENT ON COLUMN public.x_posts.signals_applied IS
    'Algorithm metadata — see docs/09-x-algorithm-rules.md';

-- ---------------------------------------------------------------------------
-- Indexes (query paths for agents + storage reconciliation)
-- ---------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_topics_run_score
    ON public.topics (pipeline_run_id, trending_score DESC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_scripts_topic
    ON public.scripts (topic_id);

CREATE INDEX IF NOT EXISTS idx_x_posts_script
    ON public.x_posts (script_id);

CREATE INDEX IF NOT EXISTS idx_pipeline_runs_status
    ON public.pipeline_runs (status);

CREATE INDEX IF NOT EXISTS idx_topics_pipeline_run_id
    ON public.topics (pipeline_run_id);

CREATE INDEX IF NOT EXISTS idx_scripts_topic_status
    ON public.scripts (topic_id, status);

COMMIT;
