# Cursor Prompt — Phase 6: Full Pipeline

## Context

Phase 6 · [SOP-06](../../sops/SOP-06-full-pipeline.md) · Kanban: [docs/08-kanban-conventions.md](../../../docs/08-kanban-conventions.md)

## Your task

1. Finalize `skills/storage-agent/SKILL.md` and `skills/pipeline-seeder/SKILL.md`
2. Finalize `skills/content-pipeline-kanban/SKILL.md`
3. `runbooks/07-full-pipeline.md` — includes fan-in storage dependency
4. Update `profiles/storage-agent.yaml` and default profile for pipeline-seeder
5. Ensure [full-pipeline-run prompt](../../prompts/full-pipeline-run.md) matches card graph in docs/08

## Kanban graph (must document in runbook)

```text
research → script (×N) → x-optimize (×N) → storage (fan-in)
```

## Acceptance

M7 · full chain in agent-testing · tutorial benchmark 5 research → 2 packages

## Do NOT

- Build custom orchestrator service
