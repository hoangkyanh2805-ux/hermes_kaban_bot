# Cursor Prompt — Phase 5: X Optimizer

## Context

Phase 5 · [SOP-05](../../sops/SOP-05-x-optimizer.md) · [docs/09-x-algorithm-rules.md](../../../docs/09-x-algorithm-rules.md)

## Your task

1. Ensure `docs/09-x-algorithm-rules.md` is complete (all signals + validation gates)
2. Finalize `skills/x-optimizer-agent/SKILL.md`
3. `runbooks/06-x-optimizer.md`
4. Update `profiles/x-optimizer-agent.yaml`
5. Optional: `paths/specs/x-thread-pack.md` — thread JSON shape example

## Validation rules (must be in skill)

- No http(s) in main_post
- Link in thread index 1
- signals_applied JSONB keys complete

## Acceptance

M6 phase-gates · agent-testing § XOptimizerAgent
