# Cursor Implementation Prompts

Copy each phase prompt into Cursor Agent when implementing that phase. **Do not implement code until the phase prompt is active.**

## Read first

1. [AGENTS.md](../../AGENTS.md)
2. [docs/PROJECT-OS.md](../../docs/PROJECT-OS.md)
3. [docs/AGENT-OS.md](../../docs/AGENT-OS.md)
4. [knowledge/tasks/PHASE-TASKS.md](../tasks/PHASE-TASKS.md)

## Phase prompts

| Phase | File |
|-------|------|
| 1 — Infra | [PHASE-01-infra.md](PHASE-01-infra.md) |
| 2 — Supabase | [PHASE-02-supabase.md](PHASE-02-supabase.md) |
| 3 — Research | [PHASE-03-research.md](PHASE-03-research.md) |
| 4 — Script | [PHASE-04-script.md](PHASE-04-script.md) |
| 5 — X Optimizer | [PHASE-05-x-optimizer.md](PHASE-05-x-optimizer.md) |
| 6 — Full pipeline | [PHASE-06-pipeline.md](PHASE-06-pipeline.md) |
| 7 — Cron | [PHASE-07-cron.md](PHASE-07-cron.md) |
| 8 — Hardening | [PHASE-08-hardening.md](PHASE-08-hardening.md) |

## Rules for Cursor

- Follow existing docs — do not invent a custom workflow engine
- Hermes Kanban only for orchestration
- Match naming in [docs/08-kanban-conventions.md](../../docs/08-kanban-conventions.md)
- No secrets in committed files
- Run phase gate checklist when done
