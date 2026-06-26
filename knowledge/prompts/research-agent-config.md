# Prompt: Research Agent Configuration

**Phase 3** · SOP-03

---

Configure the **research-agent** profile using the content-pipeline-research skill.

**TinyFish:** Ensure use-tinyfish skill is installed with API key.

**Task:** Find five trending forex/gold/XAUUSD topics for audience `forex-gold-signals`. Score each 1–100 for virality using TinyFish (FXStreet, Investing.com, Forex Factory, X). Exclude generic AI automation.

**Save to:** Supabase `topics` table with pipeline_run_id `{PIPELINE_RUN_ID}`.

**Include:** title, trending_score, audience, source_urls (JSONB with real URLs).

**Kanban:** Complete the research card when finished. Result line format: `top: {title} score={n} topics={count}`

Run the research agent now on the research Kanban card.

---

## Placeholders

| Variable | Source |
|----------|--------|
| `{PIPELINE_RUN_ID}` | From seeded pipeline_runs row or Kanban metadata |

## Verify

- [ ] ≥5 topics in Supabase
- [ ] source_urls contain live URLs
- [ ] Research card `done`
