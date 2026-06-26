# Cursor Prompt — Phase 7: Weekly Cron

## Context

Phase 7 · [SOP-07](../../sops/SOP-07-weekly-cron.md) · [docs/AGENT-OS.md §4](../../../docs/AGENT-OS.md)

## Your task

1. `runbooks/08-weekly-cron.md` — staging test with */5 cron, revert to Mon 07:00
2. Document overlap skip policy in runbook (skip if pipeline_runs.status = running)
3. Update `docs/10-runbook.md` cron section if needed
4. Add cron verification queries to runbook (SQL + hermes schedule check)

## Acceptance

M8 phase-gates

## Operator action

Send [weekly-cron-setup prompt](../../prompts/weekly-cron-setup.md) via Telegram — not automated by this repo.
