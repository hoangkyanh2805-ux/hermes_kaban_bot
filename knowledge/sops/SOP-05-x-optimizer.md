# SOP-05: X Optimizer Agent

**Phase 5** · Video step 6 · Milestone M6

## Purpose

Configure x-optimizer-agent to produce algorithm-optimized X post + thread in `x_posts`.

## Prerequisites

- SOP-04 complete (scripts exist)
- [docs/09-x-algorithm-rules.md](../../docs/09-x-algorithm-rules.md)
- [skills/x-optimizer-agent/SKILL.md](../../skills/x-optimizer-agent/SKILL.md)
- [knowledge/prompts/x-optimizer-config.md](../prompts/x-optimizer-config.md)

## Procedure

1. Install `skills/x-optimizer-agent/SKILL.md`.
2. Bind to `x-optimizer-agent` profile.
3. Send config prompt from `prompts/x-optimizer-config.md`.
4. Trigger x-optimize card after script `done`.
5. Verify `x_posts`: `main_post`, `thread`, `signals_applied`, `virality_score`.
6. Confirm **no URL in root post**; link in thread reply 1.
7. Mark card `done`.

## Acceptance

- All `signals_applied` keys present
- virality_score 1–100
- Thread format matches tutorial (link in first reply)

## Next

[SOP-06 Full Pipeline](SOP-06-full-pipeline.md)
