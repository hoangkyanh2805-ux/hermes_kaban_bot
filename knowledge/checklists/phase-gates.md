# Phase Gate Checklist (M0–M9)

## M0 — Project OS ✅

- [x] PROJECT-OS.md complete (15 deliverables)
- [x] AGENT-OS.md complete
- [x] Knowledge assets (Step 3) indexed

## M1 — Hermes live

- [ ] Railway deploy healthy
- [ ] Kanban tab visible in dashboard
- [ ] LLM provider responds
- [ ] Volume `/data` mounted

## M2 — Team on board

- [ ] Telegram bot connected
- [ ] 4 profiles created
- [ ] 4 Kanban cards with correct assignees
- [ ] Test worker spawns via dispatcher

## M3 — Supabase wired

- [ ] Supabase agent skill installed
- [ ] Tables: topics, scripts, x_posts, pipeline_runs
- [ ] Foreign keys link stages
- [ ] RLS policies active
- [ ] signals_applied JSONB on x_posts

## M4 — Research works

- [ ] TinyFish skill installed
- [ ] ≥5 topics from live search
- [ ] trending_score + source_urls populated
- [ ] Research card `done`

## M5 — Script works

- [ ] Script for top trending_score topic
- [ ] full_script + structure JSONB
- [ ] Script waited for research `done`

## M6 — X optimize works

- [ ] x_posts row with main_post + thread
- [ ] No URL in root post; link in reply 1
- [ ] signals_applied complete
- [ ] virality_score 1–100

## M7 — Full pipeline

- [ ] One Telegram prompt runs full chain
- [ ] 5 researched → 2 produced packages
- [ ] All 4 tables filled
- [ ] pipeline_runs.status = completed
- [ ] No downstream early start

## M8 — Weekly cron

- [ ] Cron Monday 07:00 configured
- [ ] Unattended run succeeds
- [ ] pipeline_runs.trigger = cron

## M9 — Reproducible

- [ ] External operator deploy < 2 hours
- [ ] 2 consecutive successful runs
- [ ] No secrets in git
- [ ] All SOPs + runbooks complete
