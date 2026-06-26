# SOP-04: Script Agent

**Phase 4** · Video step 5 · Milestone M5

## Purpose

Configure script-agent to read top `topics` row and write full video script to `scripts`.

## Prerequisites

- SOP-03 complete (topics exist)
- [skills/script-agent/SKILL.md](../../skills/script-agent/SKILL.md)
- [knowledge/prompts/script-agent-config.md](../prompts/script-agent-config.md)

## Procedure

1. Install `skills/script-agent/SKILL.md` to Hermes.
2. Bind to `script-agent` profile.
3. Send config prompt from `prompts/script-agent-config.md`.
4. Ensure script Kanban card `blocked_by` research card.
5. Trigger script card after research `done`.
6. Verify `scripts.full_script` populating in Supabase.
7. Confirm structure: cold open, 7 steps, payoff, friction, outro.
8. Mark card `done`.

## Acceptance

- Script for highest `trending_score` topic
- Word count ≥ 1200
- Script card never ran before research `done`

## Next

[SOP-05 X Optimizer](SOP-05-x-optimizer.md)
