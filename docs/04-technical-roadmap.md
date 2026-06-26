# 04 — Development Roadmap

Sequenced workstreams aligned with [PROJECT-OS.md §5](PROJECT-OS.md) and the tutorial build order.

---

## Roadmap Gantt

```
Week 1                    Week 2
│ Infra ────┤             │
│ Supabase ─────┤         │
│ Research ─────────┤     │
│ Script+X ─────────────┤ │
│ Pipeline+Cron ──────────┼──┤
│ Harden ─────────────────┼────┤
```

---

## WS-1: Infrastructure

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 1.1 | Railway deploy Hermes template | — | Kanban tab visible |
| 1.2 | Mount `/data` volume | 1.1 | Config survives redeploy |
| 1.3 | LLM provider key configured | 1.1 | `hermes chat` works |
| 1.4 | Telegram bot wired | 1.1 | Bot responds |
| 1.5 | Gateway service stable | 1.4 | 24h uptime |
| 1.6 | Scaffold repo per layout | — | Folders exist |

---

## WS-2: Kanban team

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 2.1 | Create 4 Hermes profiles | 1.5 | `profiles/*.yaml` applied |
| 2.2 | Create 4 Kanban cards | 2.1 | Board shows assignees |
| 2.3 | Verify dispatcher spawn | 2.2 | Worker completes test card |
| 2.4 | Document card conventions | 2.2 | `docs/08` drafted |

---

## WS-3: Supabase

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 3.1 | Provision Supabase project | — | URL + keys obtained |
| 3.2 | Write `001_content_pipeline.sql` | — | 4 tables + FK |
| 3.3 | Write RLS policies | 3.2 | Per-agent write scope |
| 3.4 | Install Supabase agent skill | 3.1 | Hermes confirms connection |
| 3.5 | JSON schemas for rows | 3.2 | `schemas/*.json` |
| 3.6 | Schema test in CI | 3.2 | `test_schema_sql.py` green |

---

## WS-4: TinyFish + research

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 4.1 | TinyFish API key | — | Key in env |
| 4.2 | Install use-tinyfish skill | 4.1 | Skill in `/data/skills` |
| 4.3 | Configure research-agent | 4.2, 3.4 | Profile + skill bound |
| 4.4 | Research integration test | 4.3 | 5+ `topics` rows |
| 4.5 | Runbook 04 complete | 4.4 | Reproducible steps |

---

## WS-5: Script + X optimize

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 5.1 | Configure script-agent | 3.4, 4.4 | Script from top topic |
| 5.2 | Document X algorithm rules | — | `docs/09` complete |
| 5.3 | Configure x-optimizer-agent | 5.1, 5.2 | x_posts row complete |
| 5.4 | Verify link-in-reply pattern | 5.3 | No root URL |
| 5.5 | Runbooks 05–06 complete | 5.4 | — |

---

## WS-6: Full pipeline + cron

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 6.1 | Kanban dependency wiring | 5.5 | blocked_by chain |
| 6.2 | Storage agent coordination | 3.4 | pipeline_runs written |
| 6.3 | Full pipeline test | 6.1, 6.2 | 2 topic packages |
| 6.4 | Weekly cron config | 6.3 | Monday 07:00 set |
| 6.5 | Cron validation run | 6.4 | Unattended success |
| 6.6 | Runbooks 07–08 complete | 6.5 | — |

---

## WS-7: Hardening

| # | Item | Depends | Done when |
|---|------|---------|-----------|
| 7.1 | VPS deploy path | 1.5 | systemd unit works |
| 7.2 | `.env.example` complete | all | Every var documented |
| 7.3 | `SECURITY.md` | 7.2 | Trust surface covered |
| 7.4 | Consolidated runbook | all | `docs/10-runbook.md` |
| 7.5 | M9 reproducibility test | 7.4 | External deploy OK |

---

## Technology decisions (locked)

| Decision | Choice |
|----------|--------|
| Orchestration | Hermes Kanban only |
| Workflow engine | None — Hermes dispatcher |
| Content DB | Supabase Postgres |
| Coordination DB | Hermes Kanban SQLite |
| Research | TinyFish (free search/fetch) |
| Interface | Telegram |
| Schedule | Hermes cron |
| Deploy default | Railway template |
| LLM default | DeepSeek (tutorial); swappable |

---

## Deferred (post-v1)

| Item | Rationale |
|------|-----------|
| n8n MCP integration | Referenced in Derek's series; not in core tutorial |
| Human approval gate | Tutorial runs without; add as extension |
| Custom Python engine | Violates Hermes philosophy |
| Auto-post to X | Out of tutorial scope |
