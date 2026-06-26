# 03 — Implementation Phases

Phases follow the [tutorial's demonstrated build order](https://www.youtube.com/watch?v=2oKmF--xJAI). See [PROJECT-OS.md §11](PROJECT-OS.md).

---

## Phase 0 — Project OS ✅

**Objective:** Complete project foundation before any deployment.

| Output | Location |
|--------|----------|
| 15 deliverables | `docs/PROJECT-OS.md` |
| Supporting specs | `docs/01–05`, `AGENTS.md` |
| Env catalog | `.env.example` |

**Gate:** No implementation code. Stakeholder sign-off.

---

## Phase 1 — Railway + Kanban (Video Steps 1–2)

**Objective:** Hermes running with Kanban visible; four-agent team on board.

| Task | Reference |
|------|-----------|
| Deploy Railway template | `runbooks/01-railway-deploy.md` |
| Set DeepSeek (or other) API key | deploy README |
| Connect Telegram | Hermes web UI |
| Open Kanban tab | Dashboard sidebar |
| Create 4 profiles | `profiles/*.yaml` |
| Create 4 Kanban cards in `todo` | `runbooks/02-kanban-team.md` |

**Gate (M1–M2):**

- [ ] Gateway survives restart
- [ ] Four cards visible with correct assignees
- [ ] Test task spawns worker via dispatcher

**Effort:** ~1 day

---

## Phase 2 — Supabase (Video Step 3)

**Objective:** Four-table schema + Supabase agent skill.

| Task | Reference |
|------|-----------|
| Create Supabase project | [supabase.plug.dev/ykdVN09](https://supabase.plug.dev/ykdVN09) |
| Install Supabase agent skill | `skills/INSTALL.md` |
| Apply migration SQL | `supabase/migrations/001_content_pipeline.sql` |
| Verify RLS | `supabase/policies/` |

**Tables:** `topics`, `scripts`, `x_posts`, `pipeline_runs`

**Gate (M3):**

- [ ] Skill connection confirmed in Hermes
- [ ] Four tables with FK + RLS in dashboard
- [ ] `signals_applied` column is JSONB on `x_posts`

**Effort:** ~1 day

---

## Phase 3 — Research agent (Video Step 4)

**Objective:** TinyFish-powered topic discovery → `topics` table.

| Task | Reference |
|------|-----------|
| Install TinyFish skill | `skills/INSTALL.md` |
| Configure research-agent | `runbooks/04-research-agent.md` |
| Run research Kanban card | 5 topics, score 1–10 |

**Gate (M4):**

- [ ] ≥5 rows in `topics` from live TinyFish search
- [ ] Top topic has `trending_score` and source metadata
- [ ] Research card marked `done`

**Effort:** ~1 day

---

## Phase 4 — Script agent (Video Step 5)

**Objective:** Top topic → full video script in `scripts`.

| Task | Reference |
|------|-----------|
| Configure script-agent | `runbooks/05-script-agent.md` |
| Run script Kanban card | Picks highest `trending_score` |

**Gate (M5):**

- [ ] `scripts.full_script` populated in real time
- [ ] Structure includes cold open → outro sections
- [ ] Script card `done` only after research `done`

**Effort:** ~0.5 day

---

## Phase 5 — X optimizer (Video Step 6)

**Objective:** Algorithm-aware X post + thread in `x_posts`.

| Task | Reference |
|------|-----------|
| Document algorithm rules | `docs/09-x-algorithm-rules.md` |
| Configure x-optimizer-agent | `runbooks/06-x-optimizer.md` |

**Gate (M6):**

- [ ] `x_posts.main_post` has no root external link
- [ ] Link in thread reply 1
- [ ] `signals_applied` JSONB populated
- [ ] `virality_score` 1–100

**Effort:** ~1 day

---

## Phase 6 — Full pipeline (Video Step 7)

**Objective:** One Telegram prompt; Kanban coordinates end-to-end.

| Task | Reference |
|------|-----------|
| Wire `blocked_by` dependencies | `docs/08-kanban-conventions.md` |
| Run full pipeline prompt pattern | `runbooks/07-full-pipeline.md` |

Tutorial target: 5 topics researched → top 2 scripted → both X-optimized → all in Supabase.

**Gate (M7):**

- [ ] 2 complete content packages across 4 tables
- [ ] No downstream agent started before upstream `done`
- [ ] `pipeline_runs` shows completed run

**Effort:** ~1 day

---

## Phase 7 — Weekly cron (Video bonus)

**Objective:** Unattended Monday 07:00 runs.

| Task | Reference |
|------|-----------|
| Configure Hermes cron | `runbooks/08-weekly-cron.md` |
| Test with near-term schedule | */5 cron for validation |

**Gate (M8):**

- [ ] Cron fires without human
- [ ] Supabase populated before operator checks
- [ ] `pipeline_runs.trigger = 'cron'`

**Effort:** ~0.5 day

---

## Phase 8 — Hardening

**Objective:** Reproducible deploy; schema tests; security doc.

| Task | Output |
|------|--------|
| Complete all runbooks | `runbooks/` |
| Schema + profile tests | `tests/` |
| VPS alternative | `deploy/vps/` |
| Security review | `SECURITY.md` |

**Gate (M9):** Third party deploys from docs in <2 hours.

**Effort:** ~2 days

---

## Phase timeline

```
P0 ──●
P1 ──────●
P2 ──────────●
P3 ──────────────●
P4 ──────────────────●
P5 ──────────────────────●
P6 ──────────────────────────●
P7 ──────────────────────────────●
P8 ──────────────────────────────────●
  D0  D1   D2   D3   D4   D5   D6   D7   D10
```

**Total:** ~8–10 working days part-time.
