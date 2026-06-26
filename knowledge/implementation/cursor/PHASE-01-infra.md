# Cursor Prompt — Phase 1: Railway + Kanban Infrastructure

## Context

Implement Phase 1 per [knowledge/tasks/PHASE-TASKS.md](../../tasks/PHASE-TASKS.md) P1-* and [knowledge/sops/SOP-01-railway-kanban.md](../../sops/SOP-01-railway-kanban.md).

**Constraints:** Hermes native Kanban only. No custom workflow engine. No Python orchestrator.

## Your task

Create implementation-ready **documentation and config fragments** for Phase 1:

1. `deploy/railway/README.md` — step-by-step Railway Hermes deploy using official template, volume at `/data`, env vars from `.env.example`
2. `profiles/research-agent.yaml` — model, toolsets (terminal, web, kanban read), skills list referencing repo skills
3. `profiles/script-agent.yaml`
4. `profiles/x-optimizer-agent.yaml`
5. `profiles/storage-agent.yaml`
6. `runbooks/01-railway-deploy.md` — operator short form of SOP-01
7. `runbooks/02-kanban-team.md` — links to [knowledge/prompts/kanban-team-setup.md](../../prompts/kanban-team-setup.md)

## Profile requirements

- Profile names MUST match [docs/AGENT-OS.md](../../../docs/AGENT-OS.md): research-agent, script-agent, x-optimizer-agent, storage-agent
- Default/cron profile: enable `kanban` toolset for seeding
- Reference skills from [skills/](../../../skills/) — do not duplicate SKILL bodies into profiles

## Do NOT

- Build Celery, Redis, or custom dispatcher
- Commit API keys
- Create agent prompt text outside `knowledge/prompts/`

## Acceptance

- [knowledge/checklists/phase-gates.md](../../checklists/phase-gates.md) M1–M2 document paths exist
- Profiles validate as YAML
- Runbooks reference correct SOP and prompts

## When done

Report files created and remind operator to execute SOP-01 on live Railway.
