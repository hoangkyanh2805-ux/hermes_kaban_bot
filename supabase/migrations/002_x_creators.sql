-- Hermes Content Pipeline — X creator discovery (ad-hoc + pipeline-linked)
-- Apply AFTER: 001_content_pipeline.sql
-- RLS: supabase/policies/rls_x_creators.sql

BEGIN;

-- ---------------------------------------------------------------------------
-- x_creators — ResearchAgent output for X/Twitter influencer discovery
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.x_creators (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    research_batch_id uuid NOT NULL DEFAULT gen_random_uuid(),
    pipeline_run_id uuid
        REFERENCES public.pipeline_runs (id) ON DELETE SET NULL,
    country text NOT NULL,
    handle text NOT NULL,
    display_name text,
    followers_estimate integer
        CONSTRAINT x_creators_followers_estimate_check
        CHECK (followers_estimate IS NULL OR followers_estimate >= 0),
    bio_snippet text,
    profile_url text NOT NULL,
    why_relevant text,
    niche text NOT NULL DEFAULT 'forex-gold-signals',
    source_urls jsonb NOT NULL DEFAULT '[]'::jsonb,
    discovered_at timestamptz NOT NULL DEFAULT now(),
    created_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT x_creators_batch_handle_unique UNIQUE (research_batch_id, handle),
    CONSTRAINT x_creators_profile_url_check
        CHECK (profile_url ~* '^https?://(www\.)?(x\.com|twitter\.com)/')
);

COMMENT ON TABLE public.x_creators IS
    'ResearchAgent INSERT/UPDATE — X creators discovered via TinyFish; all agents may SELECT.';

COMMENT ON COLUMN public.x_creators.research_batch_id IS
    'Groups rows from one creator-research prompt/run; generate once per task.';

COMMENT ON COLUMN public.x_creators.handle IS
    'X username without leading @.';

-- ---------------------------------------------------------------------------
-- Indexes
-- ---------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_x_creators_batch
    ON public.x_creators (research_batch_id);

CREATE INDEX IF NOT EXISTS idx_x_creators_country
    ON public.x_creators (country);

CREATE INDEX IF NOT EXISTS idx_x_creators_pipeline_run
    ON public.x_creators (pipeline_run_id)
    WHERE pipeline_run_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_x_creators_niche_country
    ON public.x_creators (niche, country);

COMMIT;
