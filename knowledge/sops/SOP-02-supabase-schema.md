# SOP-02: Supabase Schema + Skill

**Phase 2** · Video step 3 · Milestone M3

## Purpose

Provision Supabase, install Supabase agent skill, create four tables with FK and RLS.

## Prerequisites

- SOP-01 complete
- Supabase account ([plug link](https://supabase.plug.dev/ykdVN09))
- [docs/06-supabase-schema.md](../../docs/06-supabase-schema.md)
- [knowledge/prompts/supabase-schema-setup.md](../prompts/supabase-schema-setup.md)

## Procedure

1. Create Supabase project; note URL + service role key.
2. Install Supabase agent skill via Hermes (see [skills/INSTALL.md](../../skills/INSTALL.md)).
3. Send schema prompt from `prompts/supabase-schema-setup.md` OR apply `supabase/migrations/001_content_pipeline.sql` in SQL editor.
4. Verify tables: `topics`, `scripts`, `x_posts`, `pipeline_runs`.
5. Verify `x_posts.signals_applied` is JSONB.
6. Apply RLS policies per [docs/06-supabase-schema.md](../../docs/06-supabase-schema.md).
7. Test insert as research profile (manual card).

## Outputs

- Four tables with foreign keys
- RLS active per agent role
- Supabase skill connected in Hermes

## Failure handling

| Issue | Action |
|-------|--------|
| RLS blocks insert | Review policy matrix in AGENT-OS §7 |
| Skill won't connect | Verify service role key, not anon key |

## Next

[SOP-03 Research Agent](SOP-03-research-agent.md)
