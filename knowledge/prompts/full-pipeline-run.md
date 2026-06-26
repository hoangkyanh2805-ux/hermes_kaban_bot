# Prompt: Full Pipeline Run

**Phase 6** · SOP-06 · Tutorial Step 7

Send **one message** via Telegram:

---

Run the full content pipeline.

1. Research five trending **forex/gold/XAUUSD** topics using TinyFish for audience `forex-gold-signals`.
2. Pick the top **two** by virality potential (trending_score).
3. Write a full video script for each selected topic.
4. Optimize both for X using algorithm signals (no root external links; link in first reply).
5. Save all outputs to Supabase (topics, scripts, x_posts, pipeline_runs).

**Coordinate via Kanban.** Create the full card graph with dependencies:
- Script cards blocked by research completion
- X-optimize cards blocked by respective script cards
- Storage card blocked by ALL x-optimize cards (fan-in)

Agents must **not** start downstream work until upstream tasks complete.

Use pipeline-seeder and content-pipeline-kanban skills for card naming.

When storage agent finishes, set pipeline_runs.status to completed and send me a summary.

---

## Expected outcome

- 5 topics researched
- 2 scripts written
- 2 x_posts packages with signals_applied
- pipeline_runs completed
- All Kanban stage cards `done`

## Verify

- [checklists/phase-gates.md](../checklists/phase-gates.md) M7
