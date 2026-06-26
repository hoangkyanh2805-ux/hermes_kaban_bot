# AGENTS.md — Implementation Guide

For AI coding agents building this project.

**Read order:** [docs/PROJECT-OS.md](docs/PROJECT-OS.md) → [docs/AGENT-OS.md](docs/AGENT-OS.md) → [knowledge/ASSET-INDEX.md](knowledge/ASSET-INDEX.md)

Primary reference: [Derek Cheung tutorial](https://www.youtube.com/watch?v=2oKmF--xJAI)

---

## What this project is

A **faithful reproduction** of the Hermes Kanban content pipeline from the tutorial:

- 4 agents: research, script, x-optimizer, storage
- Kanban coordinates; Supabase stores
- TinyFish researches; Hermes cron schedules
- **No custom workflow engine**

---

## Hard constraints

| Rule | Reason |
|------|--------|
| Hermes native Kanban only | Tutorial architecture |
| No custom dispatcher/queue | Gateway provides this |
| No Python pipeline engine | Skills + Kanban + Supabase |
| No prompts in repo | External PDF guide; runbooks describe intent only |
| No SKILL.md bodies in repo | Install into Hermes at runtime |
| Skill-first development | Supabase + TinyFish via Hermes skills |
| Documentation-first | Spec before each phase |

---

## Build order (tutorial-faithful)

```
1. Railway deploy Hermes          → runbooks/01
2. Kanban + 4 profiles            → runbooks/02
3. Supabase skill + 4 tables      → runbooks/03, supabase/
4. TinyFish + research agent      → runbooks/04
5. Script agent                   → runbooks/05
6. X optimizer                    → runbooks/06
7. Full pipeline                  → runbooks/07
8. Weekly cron                    → runbooks/08
```

Do not skip phases. Do not build agents before Supabase schema exists.

---

## What to implement per phase

| Phase | Create | Do NOT create |
|-------|--------|---------------|
| 0 | Docs, `.env.example` | Code, prompts, agents |
| 1 | `profiles/`, `deploy/`, runbooks 01–02 | Custom orchestrator |
| 2 | `supabase/migrations/`, `schemas/`, runbook 03 | Application server |
| 3–6 | Runbooks, `docs/07–09` | Monolithic agent script |
| 7–8 | Cron docs, tests | Celery, n8n required path |

---

## Agent profile names (locked)

| Profile | Kanban assignee |
|---------|-----------------|
| `research-agent` | research cards |
| `script-agent` | script cards |
| `x-optimizer-agent` | x-optimize cards |
| `storage-agent` | storage cards |

---

## Supabase tables (locked)

`topics` · `scripts` · `x_posts` · `pipeline_runs`

Schema source: `supabase/migrations/001_content_pipeline.sql` (create in Phase 2).

---

## External prompt reference

Prompts live in [derekcheungsa/ai-automation-resources](https://github.com/derekcheungsa/ai-automation-resources) (PDF guide). This repo documents **what** each step achieves, not prompt text.

---

## When stuck

| Problem | Check |
|---------|-------|
| Kanban tab missing | Hermes version ≥ v2026.5.7 |
| Worker won't spawn | Gateway running? `hermes kanban ready` |
| Downstream runs early | `blocked_by` links on cards |
| Empty topics | TinyFish key? Skill installed? |
| Supabase write fails | RLS policy for agent role |
| Cron silent | Hermes schedule timezone |

Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban

---

## Do not

- Build a custom workflow engine
- Put `SUPABASE_SERVICE_ROLE_KEY` in git
- Generate agent prompts into the repo
- Replace Kanban with Supabase job queues
- Auto-post to X without explicit v2 scope
