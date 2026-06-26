# Prompt: Weekly Cron Setup

**Phase 7** · SOP-07 · Tutorial bonus

Send via Telegram:

---

Set up a **weekly content pipeline run** every **Monday at 7:00 AM** in timezone `{TIMEZONE}` (e.g. America/New_York).

Use Hermes built-in cron scheduling. Each Monday:
1. Seed a new pipeline run with trigger `cron` and title `weekly-run:{YYYY-Www}`
2. Create the full Kanban card graph (research → script → optimize → storage)
3. Run the same pipeline: research 5 forex/gold/XAUUSD topics (audience forex-gold-signals), produce top 2, optimize for X, save to Supabase
4. Notify me in Telegram when the weekly run starts and when storage completes

**Overlap policy:** Skip the cron seed if a pipeline run is still `running` from the previous week.

For testing, create a one-time run in 5 minutes first, then apply the Monday schedule.

---

## Production cron

`0 7 * * 1` in operator timezone

## Verify

- [ ] `pipeline_runs.trigger = cron` on Monday run
- [ ] Supabase populated without manual message
- [ ] M8 gate in phase-gates checklist
