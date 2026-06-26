---
name: content-pipeline-x-optimizer
description: Rewrite script drafts into X posts and threads optimized for Phoenix algorithm signals. No external links in root post. Save to x_posts with signals_applied JSONB.
---

# X Optimizer Agent Skill

Hermes profile: `x-optimizer-agent` · Pipeline stage: **OPTIMIZE**

Contract: [docs/AGENT-OS.md §10](../../docs/AGENT-OS.md)

---

## Purpose

Transform the latest `scripts` draft into an X-native **main post + thread** engineered for engagement using documented open-source algorithm weights (Phoenix 2026 / public X algorithm signals).

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Kanban task | `kanban_show()` | Yes |
| `topic_slug` / `script_id` | Card metadata | Yes |
| Script draft | Supabase `scripts` | Yes |
| Algorithm rules | [docs/09-x-algorithm-rules.md](../../docs/09-x-algorithm-rules.md) | Yes |
| Script card `done` | Kanban `blocked_by` | Yes |

---

## Outputs

| Output | Destination |
|--------|-------------|
| `x_posts` row | Supabase |
| `main_post` | No URLs in root |
| `thread` | JSONB array; **link in reply 1 only** |
| `signals_applied` | JSONB — weights used |
| `virality_score` | 1–100 |
| `suggested_post_time` | 07:00–09:00 or 18:00–20:00 operator TZ |
| Summary | `kanban_complete --result` |

**Result line format:** `x: {topic_slug} virality={n}`

---

## Dependencies

| Dependency | Type |
|------------|------|
| Supabase agent skill | Hermes skill |
| `scripts` row for topic | Supabase |
| Script Kanban card `done` | Kanban |
| x-algorithm reference | [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) |

---

## Algorithm rules (must apply)

| Signal | Rule |
|--------|------|
| Reply weight | 27× a like — engineer for replies |
| Author reply | 150× when author replies to commenter — plan follow-up reply |
| External links | **Forbidden in root post** — place in thread reply 1 |
| Early velocity | Target 5+ replies in first 15 minutes |
| Post timing | Morning 07:00–09:00 or evening 18:00–20:00 |

### Required `signals_applied` keys

```json
{
  "reply_weight": 27,
  "author_reply_weight": 150,
  "no_root_external_link": true,
  "link_placement": "first_reply",
  "early_velocity_target_replies_15min": 5,
  "algorithm_version": "phoenix-2026"
}
```

---

## Examples

### Thread shape

```json
{
  "posts": [
    {"index": 0, "role": "root", "text": "Hook question — no URLs"},
    {"index": 1, "role": "reply", "text": "Link + context here"},
    {"index": 2, "role": "thread", "text": "Step 1..."}
  ]
}
```

### Reply-bait patterns

- Open question in root post
- "Wrong answers only" framing
- Controversial-but-defensible take
- Numbered thread promise ("🧵 7 steps")

---

## Failure cases

| Failure | Action |
|---------|--------|
| URL detected in `main_post` | Regenerate; block after 2 failures |
| Missing `signals_applied` key | `kanban_block` |
| No script for topic | `kanban_block` |
| Thread exceeds char limits | Split into more thread posts — never silent truncate |
| Script card not done | Must not run (Kanban gate) |

---

## Testing checklist

- [ ] `main_post` has zero `http://` or `https://`
- [ ] Link present in thread index 1
- [ ] `signals_applied` contains all required keys
- [ ] `virality_score` 1–100
- [ ] `x_posts.script_id` FK correct
- [ ] Root post ≤ 280 chars (or thread format if longer content)
- [ ] `suggested_post_time` in allowed window
- [ ] Optimize card `done` only after script `done`
- [ ] Storage fan-in waits for all optimize siblings

---

## Documentation

| Reference | Path |
|-----------|------|
| Agent contract | [docs/AGENT-OS.md §10](../../docs/AGENT-OS.md) |
| Algorithm rules | [docs/09-x-algorithm-rules.md](../../docs/09-x-algorithm-rules.md) |
| SOP | [knowledge/sops/SOP-05-x-optimizer.md](../../knowledge/sops/SOP-05-x-optimizer.md) |
| Config prompt | [knowledge/prompts/x-optimizer-config.md](../../knowledge/prompts/x-optimizer-config.md) |
