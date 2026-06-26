# 05 — Milestones & Acceptance Criteria

Maps to [PROJECT-OS.md §6 and §12](PROJECT-OS.md).

---

## Milestone summary

| ID | Name | Phase | Key proof |
|----|------|-------|-----------|
| M0 | Project OS | 0 | 15 deliverables complete |
| M1 | Hermes live | 1 | Railway + Kanban tab |
| M2 | Team on board | 1 | 4 cards, 4 profiles |
| M3 | Supabase wired | 2 | 4 tables + skill |
| M4 | Research works | 3 | TinyFish → topics |
| M5 | Script works | 4 | Top topic → script |
| M6 | X optimize works | 5 | signals_applied JSONB |
| M7 | Full pipeline | 6 | 2 packages, 1 prompt |
| M8 | Weekly cron | 7 | Unattended Monday run |
| M9 | Reproducible | 8 | External deploy <2h |

---

## M0 — Project OS ✅

- [x] Project Vision
- [x] Technical Architecture
- [x] Repository Structure
- [x] Folder Structure
- [x] Development Roadmap
- [x] Milestones
- [x] Technology Stack
- [x] Dependencies
- [x] Environment Variables
- [x] Risk Analysis
- [x] Implementation Phases
- [x] Acceptance Criteria
- [x] Documentation Plan
- [x] Testing Strategy
- [x] Future Extension Strategy

---

## M1 — Hermes live

| Criterion | Verification |
|-----------|--------------|
| Railway deploy succeeds | Service healthy in dashboard |
| Kanban tab accessible | Screenshot or live check |
| LLM responds | Test message in Telegram |
| Volume mounted | Redeploy preserves config |

---

## M2 — Team on board

| Criterion | Verification |
|-----------|--------------|
| 4 profiles exist | Hermes profiles list |
| 4 Kanban cards in `todo` | Dashboard or `hermes kanban list` |
| Correct assignees | research, script, x-optimizer, storage |
| Dispatcher spawns worker | Test card completes |

---

## M3 — Supabase wired

| Criterion | Verification |
|-----------|--------------|
| `topics` table exists | Supabase dashboard |
| `scripts` table exists | — |
| `x_posts` with `signals_applied` JSONB | — |
| `pipeline_runs` table exists | — |
| Foreign keys link stages | Schema inspector |
| RLS policies active | Policy tab |
| Supabase skill installed | Hermes confirms |

---

## M4 — Research works

| Criterion | Verification |
|-----------|--------------|
| TinyFish skill installed | Skills directory |
| ≥5 topics saved | `SELECT count(*) FROM topics` |
| Scores 1–100 present | `trending_score` column |
| Live sources cited | `source_urls` JSONB non-empty |
| Top score ≥90 possible | Tutorial: 95 for top topic |

---

## M5 — Script works

| Criterion | Verification |
|-----------|--------------|
| Picks highest `trending_score` | Compare topic ↔ script FK |
| `full_script` non-empty | Supabase row |
| Structure sections present | `structure` JSONB |
| Runs only after research | Kanban dependency log |

---

## M6 — X optimize works

| Criterion | Verification |
|-----------|--------------|
| `main_post` written | x_posts row |
| `thread` JSONB array | ≥2 posts |
| No URL in root post | Manual inspect |
| Link in reply 1 | Thread JSON |
| `signals_applied` populated | JSONB keys match docs/09 |
| `virality_score` 1–100 | Column value |

---

## M7 — Full pipeline

| Criterion | Verification |
|-----------|--------------|
| One Telegram prompt triggers all | Single user message |
| 5 researched, top 2 selected | topics count + script count |
| 2 x_posts packages | Row count |
| All 4 tables filled | SQL join query |
| Downstream waited for upstream | Kanban event timeline |
| `pipeline_runs.status = completed` | Final row |

**Tutorial benchmark:** "Four tables filled. Two research-to-X-optimize content packages."

---

## M8 — Weekly cron

| Criterion | Verification |
|-----------|--------------|
| Cron set Monday 07:00 | Hermes schedule config |
| No human message required | Run completes overnight |
| `pipeline_runs.trigger = cron` | DB row |
| Content ready Monday AM | Operator checklist |

---

## M9 — Reproducible

| Criterion | Verification |
|-----------|--------------|
| Runbooks 01–08 complete | All files exist |
| `.env.example` matches deploy | Diff check |
| Schema tests pass | CI green |
| External operator deploys | Timed runbook follow |
| No secrets in repo | Scan clean |

---

## Ongoing success metrics (post-M9)

| Metric | Target |
|--------|--------|
| Weekly run success rate | ≥ 90% |
| Topics per run | 5 researched, 2 produced |
| Research source quality | ≥ 3 URLs per topic |
| Script length | Sufficient for 8–12 min video |
| Cost per weekly run | Configurable budget |
| Cron reliability | 4/4 Mondays per month |

---

## Rollback / pause triggers

- M1 not achieved in 2 days → infra blocker review
- M7 fails 3 consecutive runs → Kanban dependency audit
- Supabase RLS blocks agent writes → policy matrix review
- Weekly cost > 3× budget → reduce topics per run
