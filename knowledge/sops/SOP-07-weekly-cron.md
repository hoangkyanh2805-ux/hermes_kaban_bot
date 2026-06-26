# SOP-07: Weekly Cron

**Phase 7** · Video bonus · Milestone M8

## Purpose

Schedule unattended Monday 07:00 pipeline runs via Hermes built-in cron.

## Prerequisites

- SOP-06 full pipeline success
- [knowledge/prompts/weekly-cron-setup.md](../prompts/weekly-cron-setup.md)

## Procedure

1. Send weekly cron setup prompt to Hermes (see prompts file).
2. Confirm cron entry: `0 7 * * 1` in operator timezone.
3. **Staging test:** temporarily use `*/5 * * * *`; verify one unattended run.
4. Revert to Monday 07:00 for production.
5. Verify `pipeline_runs.trigger = 'cron'`.
6. Confirm overlap policy: skip if prior run `running`.

## Acceptance

- Monday morning: Supabase populated without human message
- Telegram optional "weekly run started" notification

## Next

[SOP-08 Hardening](SOP-08-hardening.md)
