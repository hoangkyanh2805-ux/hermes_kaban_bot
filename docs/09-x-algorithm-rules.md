# 09 — X Algorithm Rules (Phoenix 2026)

Reference for XOptimizerAgent. Source: [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) + tutorial signals.

---

## Engagement weights (public)

| Signal | Weight / rule | Optimizer action |
|--------|---------------|------------------|
| Reply | 27× a like | Ask questions; controversy; "wrong answers only" |
| Author replies to commenter | 150× | Plan author follow-up reply in thread |
| External link in root | Suppressed since 2023 | **Never** put URL in main_post |
| Link placement | First reply | Put URL in thread index 1 |
| Early velocity | Strong in first 30–60 min | Target 5+ replies in first 15 min |
| Post timing | Peak windows | 07:00–09:00 or 18:00–20:00 operator TZ |

---

## Required `signals_applied` JSONB

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

## Thread structure template

| Index | Role | Content rules |
|-------|------|---------------|
| 0 | root | Hook, no links, ≤280 chars ideal |
| 1 | reply | Link + context |
| 2+ | thread | Steps, insights, CTA |

---

## Validation gates (XOptimizerAgent)

- [ ] Regex scan: no `https?://` in `main_post`
- [ ] `thread[1]` contains intended link
- [ ] All JSONB keys present
- [ ] virality_score justified in kanban_comment

---

## Out of scope (v1)

- Live X API posting
- Real-time engagement polling
- Paid promotion

Update this doc when x-algorithm repo changes materially.
