-- Hermes Content Pipeline — RLS for x_creators
-- Apply AFTER: supabase/migrations/002_x_creators.sql
-- Requires: current_agent_role() from rls_agent_ownership.sql

BEGIN;

ALTER TABLE public.x_creators ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.x_creators FORCE ROW LEVEL SECURITY;

-- Idempotent re-apply (safe if policies already exist from a prior run)
DROP POLICY IF EXISTS x_creators_select_all_agents ON public.x_creators;
DROP POLICY IF EXISTS x_creators_insert_research ON public.x_creators;
DROP POLICY IF EXISTS x_creators_update_research ON public.x_creators;

-- All pipeline agents: read creator rows
CREATE POLICY x_creators_select_all_agents
    ON public.x_creators
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

-- ResearchAgent: insert discovered creators
CREATE POLICY x_creators_insert_research
    ON public.x_creators
    FOR INSERT
    TO authenticated
    WITH CHECK (public.current_agent_role() = 'research-agent');

-- ResearchAgent: update rows in same batch (enrichment / corrections)
CREATE POLICY x_creators_update_research
    ON public.x_creators
    FOR UPDATE
    TO authenticated
    USING (public.current_agent_role() = 'research-agent')
    WITH CHECK (public.current_agent_role() = 'research-agent');

-- DELETE forbidden (no DELETE policies)

COMMIT;
