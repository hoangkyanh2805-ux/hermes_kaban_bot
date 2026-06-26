-- Hermes Content Pipeline — RLS agent ownership
-- Spec: docs/06-supabase-schema.md · docs/AGENT-OS.md §7
-- Apply AFTER: supabase/migrations/001_content_pipeline.sql
--
-- JWT claim: auth.jwt() ->> 'agent_role' ∈
--   research-agent | script-agent | x-optimizer-agent | storage-agent | pipeline-seeder
--
-- Note: Supabase service_role bypasses RLS (Hermes Supabase skill default).
-- These policies enforce ownership when using scoped JWT / anon + custom claims.

BEGIN;

-- ---------------------------------------------------------------------------
-- Helper — resolve agent role from JWT or request claim
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.current_agent_role()
RETURNS text
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
    SELECT COALESCE(
        NULLIF(auth.jwt() ->> 'agent_role', ''),
        NULLIF(current_setting('request.jwt.claim.agent_role', true), '')
    );
$$;

COMMENT ON FUNCTION public.current_agent_role() IS
    'Returns agent_role JWT claim for RLS policies.';

-- ---------------------------------------------------------------------------
-- Enable RLS on all pipeline tables
-- ---------------------------------------------------------------------------
ALTER TABLE public.pipeline_runs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.topics ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.scripts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.x_posts ENABLE ROW LEVEL SECURITY;

-- Force RLS for table owners (defense in depth when not using service_role)
ALTER TABLE public.pipeline_runs FORCE ROW LEVEL SECURITY;
ALTER TABLE public.topics FORCE ROW LEVEL SECURITY;
ALTER TABLE public.scripts FORCE ROW LEVEL SECURITY;
ALTER TABLE public.x_posts FORCE ROW LEVEL SECURITY;

-- ---------------------------------------------------------------------------
-- pipeline_runs
-- ---------------------------------------------------------------------------

-- All agents: read run metadata
CREATE POLICY pipeline_runs_select_all_agents
    ON public.pipeline_runs
    FOR SELECT
    TO authenticated
    USING (
        public.current_agent_role() IN (
            'research-agent',
            'script-agent',
            'x-optimizer-agent',
            'storage-agent',
            'pipeline-seeder'
        )
    );

-- Seeder + Storage: create runs
CREATE POLICY pipeline_runs_insert_seeder_storage
    ON public.pipeline_runs
    FOR INSERT
    TO authenticated
    WITH CHECK (
        public.current_agent_role() IN ('storage-agent', 'pipeline-seeder')
    );

-- Storage: full run reconciliation updates
CREATE POLICY pipeline_runs_update_storage
    ON public.pipeline_runs
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'storage-agent')
    WITH CHECK (public.current_agent_role() = 'storage-agent');

-- Research: patch started_at when first topic lands (agent contract only)
CREATE POLICY pipeline_runs_update_research_started_at
    ON public.pipeline_runs
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'research-agent')
    WITH CHECK (public.current_agent_role() = 'research-agent');

-- ---------------------------------------------------------------------------
-- topics — ResearchAgent writes; all agents read
-- ---------------------------------------------------------------------------
CREATE POLICY topics_select_all_agents
    ON public.topics
    FOR SELECT
    TO authenticated
    USING (
        public.current_agent_role() IN (
            'research-agent',
            'script-agent',
            'x-optimizer-agent',
            'storage-agent',
            'pipeline-seeder'
        )
    );

CREATE POLICY topics_insert_research
    ON public.topics
    FOR INSERT
    TO authenticated
    WITH CHECK (public.current_agent_role() = 'research-agent');

CREATE POLICY topics_update_research
    ON public.topics
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'research-agent')
    WITH CHECK (public.current_agent_role() = 'research-agent');

-- ---------------------------------------------------------------------------
-- scripts — ScriptAgent writes; Script/XOpt/Storage read
-- ---------------------------------------------------------------------------
CREATE POLICY scripts_select_downstream
    ON public.scripts
    FOR SELECT
    TO authenticated
    USING (
        public.current_agent_role() IN (
            'script-agent',
            'x-optimizer-agent',
            'storage-agent'
        )
    );

CREATE POLICY scripts_insert_script
    ON public.scripts
    FOR INSERT
    TO authenticated
    WITH CHECK (public.current_agent_role() = 'script-agent');

CREATE POLICY scripts_update_script
    ON public.scripts
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'script-agent')
    WITH CHECK (public.current_agent_role() = 'script-agent');

-- ---------------------------------------------------------------------------
-- x_posts — XOptimizerAgent writes; XOpt/Storage read
-- ---------------------------------------------------------------------------
CREATE POLICY x_posts_select_downstream
    ON public.x_posts
    FOR SELECT
    TO authenticated
    USING (
        public.current_agent_role() IN ('x-optimizer-agent', 'storage-agent')
    );

CREATE POLICY x_posts_insert_x_optimizer
    ON public.x_posts
    FOR INSERT
    TO authenticated
    WITH CHECK (public.current_agent_role() = 'x-optimizer-agent');

CREATE POLICY x_posts_update_x_optimizer
    ON public.x_posts
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'x-optimizer-agent')
    WITH CHECK (public.current_agent_role() = 'x-optimizer-agent');

-- ---------------------------------------------------------------------------
-- DELETE forbidden for all agents (no DELETE policies)
-- ---------------------------------------------------------------------------

COMMIT;
