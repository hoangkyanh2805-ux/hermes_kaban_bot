---
name: content-pipeline-research
description: Research trending forex/gold/XAUUSD topics via TinyFish, score virality 1-100, save to Supabase topics table. Use when assigned a Kanban research card in the Hermes content pipeline.
---

# Research Agent Skill

Hermes profile: `research-agent` · Pipeline stage: **RESEARCH**

Contract: [docs/AGENT-OS.md §8](../../docs/AGENT-OS.md)

---

## Purpose

Find trending **forex / gold (XAUUSD) / trading signal** topics for the `forex-gold-signals` audience using **live TinyFish search** (not LLM invention), score each 1–100 for content virality, and persist ranked rows to Supabase `topics`.

Domain config: [content.yaml](../../content.yaml)

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Kanban task id | `_KANBAN_TASK` env | Yes |
| Task body | `kanban_show()` | Yes |
| `pipeline_run_id` | Card metadata | Yes |
| Topic count | Task body (default: 5) | Yes |
| Audience | Task body (default: `forex-gold-signals`) | No |
| Search queries | Task body or [content.yaml](../../content.yaml) defaults | Yes |

**Default query themes:** `XAUUSD gold forecast`, `gold technical analysis breakout`, `forex gold macro catalyst`, `XAUUSD key levels support resistance`, `gold trading signal trending`

---

## Outputs

| Output | Destination |
|--------|-------------|
| `topics` rows (≥ target count) | Supabase |
| `pipeline_runs.started_at` | Supabase (first insert) |
| Progress comments | Kanban `kanban_comment` |
| Summary line | `kanban_complete --result` |

**Result line format:** `top: {title} score={n} topics={count}`

---

## Dependencies

| Dependency | Type |
|------------|------|
| TinyFish `use-tinyfish` skill | Hermes skill (vendor) |
| Supabase agent skill | Hermes skill (vendor) |
| `pipeline_runs` row | Seeded before research |
| Kanban card `research:{run_id}` | Assigned to this profile |

**Does not depend on:** script, x-optimize, or storage cards.

---

## Workflow

```text
kanban_show → confirm pipeline_run_id
→ TinyFish search (parallel queries)
→ score each result 1-100 with cited evidence
→ INSERT topics (idempotent on pipeline_run_id + title)
→ kanban_complete
```

### TinyFish decision tree

1. **search** — discover topics, trends, titles, URLs
2. **fetch_content** — deepen scoring for top 3 candidates only
3. Never use TinyFish `agent`/browser unless task body explicitly requests

---

## Examples

### Example task body

```text
Find 5 trending forex/gold/XAUUSD topics for audience forex-gold-signals.
Score each 1-100 for virality. Save to topics table for pipeline_run_id {uuid}.
Exclude generic AI automation topics.
Mark done when finished.
```

### Example `topics` row

```json
{
  "pipeline_run_id": "abc-123",
  "title": "Gold Forecast, News and Analysis (XAU/USD) - FXStreet",
  "trending_score": 95,
  "audience": "forex-gold-signals",
  "source_urls": ["https://...", "https://..."]
}
```

### Example kanban_comment sequence

```text
start: RESEARCH t_research_01
tinyfish: search 3 queries → 24 results
tinyfish: fetch top 3 → scoring complete
supabase: inserted 5 topics
```

---

## Failure cases

| Failure | Detection | Action |
|---------|-----------|--------|
| TinyFish timeout/429 | API error | Retry up to 3× (30s, 60s, 120s backoff); comment each retry |
| Empty search results | 0 usable hits | Widen query once; then `kanban_block` |
| < 3 topics after retries | Count check | `kanban_block` — insufficient research |
| RLS insert denied | Supabase error | `kanban_block` — no retry |
| Missing pipeline_run_id | Metadata check | `kanban_block` — config error |
| Duplicate title | Unique constraint | Skip row; continue |

---

## Testing checklist

- [ ] `kanban_show()` returns research card assigned to this profile
- [ ] TinyFish search returns real URLs in `source_urls`
- [ ] ≥ 5 `topics` rows for test run
- [ ] `trending_score` between 1 and 100
- [ ] Top topic score ≥ 70 on live run
- [ ] No invented URLs (spot-check 2 sources)
- [ ] `kanban_complete` result line matches format
- [ ] Research card `done` before script card promotes to `ready`
- [ ] Retry: kill worker mid-run → reclaim completes without duplicate topics

---

## Creator discovery mode (optional)

**Trigger:** Kanban card or Telegram one-off — see [knowledge/prompts/research-x-creators.md](../../knowledge/prompts/research-x-creators.md).

**Not** the weekly topic pipeline — do **not** insert `topics` rows.

### Inputs

| Input | Source | Required |
|-------|--------|----------|
| `research_batch_id` | Agent generates UUID once per task | Yes |
| Countries | Task body or [content.yaml](../../content.yaml) `creator_research.countries` | Yes |
| `niche` | Default `forex-gold-signals` | No |
| `pipeline_run_id` | Optional link to weekly run | No |

### Outputs

| Output | Destination |
|--------|-------------|
| `x_creators` rows | Supabase |
| Summary by country | `kanban_complete --result` or Telegram |

**Result line format:** `creators: batch={uuid} total={n} top_countries={ca,uk,...}`

### Workflow

```text
generate research_batch_id
→ TinyFish search (≥1 query per country)
→ validate profile_url is real x.com/twitter.com link from search
→ INSERT x_creators (skip duplicate handle in batch)
→ report counts per country
```

### Example `x_creators` row

```json
{
  "research_batch_id": "abc-123",
  "country": "Canada",
  "handle": "exampletrader",
  "display_name": "Example Trader",
  "followers_estimate": 12500,
  "bio_snippet": "XAUUSD / gold macro threads",
  "profile_url": "https://x.com/exampletrader",
  "why_relevant": "Posts daily gold levels and breakout setups",
  "niche": "forex-gold-signals",
  "source_urls": ["https://...", "https://..."]
}
```

### Failure cases (creator mode)

| Failure | Action |
|---------|--------|
| Table `x_creators` missing | `kanban_block` — run migration 002 first |
| 0 rows after all countries | `kanban_block` — widen queries once, then block |
| Invented handle (no search evidence) | Skip row; comment violation |
| Duplicate handle in batch | Skip (idempotent) |

---

## Testing checklist (creator mode)

- [ ] Migration `002_x_creators.sql` applied on Supabase
- [ ] ≥10 `x_creators` rows for smoke test
- [ ] Every `profile_url` resolves to x.com or twitter.com
- [ ] `source_urls` non-empty for spot-checked rows
- [ ] No rows in `topics` from creator-only task

---

## Documentation

| Reference | Path |
|-----------|------|
| Agent contract | [docs/AGENT-OS.md §8](../../docs/AGENT-OS.md) |
| SOP | [knowledge/sops/SOP-03-research-agent.md](../../knowledge/sops/SOP-03-research-agent.md) |
| Config prompt | [knowledge/prompts/research-agent-config.md](../../knowledge/prompts/research-agent-config.md) |
| DB ownership | [docs/AGENT-OS.md §7](../../docs/AGENT-OS.md) |
| TinyFish install | [skills/INSTALL.md](../INSTALL.md) |
