# SOP-03: Research Agent

**Phase 3** · Video step 4 · Milestone M4

## Purpose

Install TinyFish skill, bind research-agent profile, run research Kanban card → `topics` table.

## Prerequisites

- SOP-02 complete
- `TINYFISH_API_KEY`
- [skills/research-agent/SKILL.md](../../skills/research-agent/SKILL.md)
- [knowledge/prompts/research-agent-config.md](../prompts/research-agent-config.md)

## Procedure

1. Install TinyFish `use-tinyfish` per [skills/INSTALL.md](../../skills/INSTALL.md).
2. Copy `skills/research-agent/SKILL.md` to Hermes skills dir.
3. Bind skill to `research-agent` profile.
4. Send config prompt from `prompts/research-agent-config.md`.
5. Trigger research Kanban card (or Telegram command).
6. Monitor: TinyFish queries → Supabase `topics` filling.
7. Verify ≥5 topics with `trending_score` and `source_urls`.
8. Confirm card `done` + Telegram notification.

## Acceptance

- Top topic score documented (tutorial: 95)
- Live URLs in `source_urls` — not hallucinated

## Testing

Run [checklists/agent-testing.md](../checklists/agent-testing.md) § ResearchAgent

## Next

[SOP-04 Script Agent](SOP-04-script-agent.md)
