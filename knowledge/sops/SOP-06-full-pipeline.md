# SOP-06: Full Pipeline Run

**Phase 6** · Video step 7 · Milestone M7

## Purpose

Execute end-to-end pipeline from one Telegram prompt with Kanban dependency coordination.

## Prerequisites

- SOP-03 through SOP-05 validated individually
- [skills/pipeline-seeder/SKILL.md](../../skills/pipeline-seeder/SKILL.md)
- [skills/storage-agent/SKILL.md](../../skills/storage-agent/SKILL.md)
- [knowledge/prompts/full-pipeline-run.md](../prompts/full-pipeline-run.md)

## Procedure

1. Install storage + pipeline-seeder + kanban skills.
2. Wire full dependency graph per [docs/08-kanban-conventions.md](../../docs/08-kanban-conventions.md).
3. Send **full pipeline prompt** (see prompts file).
4. Watch Kanban: RESEARCH → SCRIPT → OPTIMIZE → STORAGE.
5. Verify no downstream card enters `in_progress` before upstream `done`.
6. Confirm Supabase: 5 topics researched, top 2 scripted, 2 x_posts packages.
7. Storage agent sets `pipeline_runs.status = completed`.
8. Receive Telegram final summary.

## Acceptance (tutorial benchmark)

> Four tables filled. Two research-to-X-optimize content packages.

## Testing

- [checklists/agent-testing.md](../checklists/agent-testing.md) — full chain
- [checklists/phase-gates.md](../checklists/phase-gates.md) M7

## Next

[SOP-07 Weekly Cron](SOP-07-weekly-cron.md)
