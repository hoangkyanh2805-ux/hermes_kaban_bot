---
name: content-pipeline-script
description: Select top virality topic from Supabase and write a full video script with cold open, seven steps, payoff, friction, and outro. Use when assigned a Kanban script card.
---

# Script Agent Skill

Hermes profile: `script-agent` · Pipeline stage: **SCRIPT**

Contract: [docs/AGENT-OS.md §9](../../docs/AGENT-OS.md)

---

## Purpose

Read the highest `trending_score` topic(s) for the current pipeline run from Supabase and produce a **trading-signal script** (macro catalyst or technical setup) saved to `scripts` with structured sections in `structure` JSONB.

Audience: `forex-gold-signals` — XAUUSD / gold / forex traders. See [content.yaml](../../content.yaml).

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Kanban task | `kanban_show()` | Yes |
| `pipeline_run_id` | Card metadata | Yes |
| `topic_slug` | Card title `script:{topic_slug}` | Yes (multi-topic) |
| Ranked topics | `SELECT * FROM topics WHERE pipeline_run_id = ? ORDER BY trending_score DESC` | Yes |
| Research card `done` | Kanban `blocked_by` (implicit) | Yes |

---

## Outputs

| Output | Destination |
|--------|-------------|
| `scripts` row per assigned topic | Supabase |
| `full_script` text | `scripts.full_script` |
| Section map | `scripts.structure` JSONB |
| `status` | `draft` |
| Summary | `kanban_complete --result` |

**Result line format:** `script: {topic_slug} words={n}`

---

## Dependencies

| Dependency | Type |
|------------|------|
| Supabase agent skill | Hermes skill |
| Research card `done` | Kanban `blocked_by` |
| `topics` rows exist | Supabase |
| content-pipeline-kanban skill | Optional — conventions |

**Must not run if:** research card not `done` or zero topics for run.

---

## Script structure (required sections)

1. **Cold open** — hook in first 30 seconds
2. **Seven steps** — numbered main content
3. **Payoff** — what viewer gains
4. **Friction** — honest caveats / common mistakes
5. **Outro** — CTA and next step

Encode section boundaries in `structure` JSONB:

```json
{
  "cold_open": {"start": 0, "end": 1},
  "steps": [1, 2, 3, 4, 5, 6, 7],
  "payoff": {},
  "friction": {},
  "outro": {}
}
```

---

## Examples

### Topic selection

```sql
SELECT id, title, trending_score FROM topics
WHERE pipeline_run_id = '{uuid}'
ORDER BY trending_score DESC
LIMIT 1;
```

Tutorial reference: "AI agents for beginners — no-code build tutorials 2026" @ score 95.

### Example kanban_comment

```text
start: SCRIPT script:ai-agents-beginners
selected: topic_id={uuid} score=95
writing: full_script → supabase
words: 1847
```

---

## Failure cases

| Failure | Action |
|---------|--------|
| No topics for run | `kanban_block` — upstream research failed |
| topic_slug not in topics | `kanban_block` — card/config mismatch |
| Script < 1200 words | Regenerate once; then `kanban_block` |
| Supabase read timeout | Retry 2× (60s backoff) |
| Tie on trending_score | Pick higher score; tie-break `created_at` ASC |

---

## Testing checklist

- [ ] Script card stays `todo` until research card `done`
- [ ] Selected topic matches highest `trending_score`
- [ ] `full_script` contains all 5 section types
- [ ] `structure` JSONB valid
- [ ] `scripts.topic_id` FK correct
- [ ] `status = draft`
- [ ] Word count ≥ 1200
- [ ] `kanban_complete` result line correct
- [ ] Idempotent: re-run upserts same `topic_id` without duplicate

---

## Documentation

| Reference | Path |
|-----------|------|
| Agent contract | [docs/AGENT-OS.md §9](../../docs/AGENT-OS.md) |
| SOP | [knowledge/sops/SOP-04-script-agent.md](../../knowledge/sops/SOP-04-script-agent.md) |
| Config prompt | [knowledge/prompts/script-agent-config.md](../../knowledge/prompts/script-agent-config.md) |
