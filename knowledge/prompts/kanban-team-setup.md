# Prompt: Kanban Team Setup

**Phase 1** · SOP-01

Send via Telegram to Hermes:

---

I'm building a content creation pipeline. Create four Kanban tasks for these agents:

1. **Research agent** — Find trending YouTube topics using TinyFish web search and save results to Supabase `topics` table.

2. **Script agent** — Turn a research topic into a complete video script and save to Supabase `scripts` table.

3. **X optimizer agent** — Apply X algorithm virality signals to generate an optimized post and thread. Save to Supabase `x_posts` table with `signals_applied` JSONB.

4. **Storage agent** — Coordinate Supabase writes across all stages and finalize `pipeline_runs`.

Assign each to its own profile:
- research-agent
- script-agent
- x-optimizer-agent
- storage-agent

Set all cards to **todo**. Use the content pipeline Kanban naming conventions from the project skills.

---

## Expected result

- Four cards visible in Kanban dashboard
- Correct assignees
- Cards in `todo` status

## Verify

- [ ] Kanban tab shows 4 cards
- [ ] Assignees match profile names
