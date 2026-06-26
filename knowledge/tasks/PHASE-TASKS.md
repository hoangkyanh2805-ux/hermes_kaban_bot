# Development Tasks by Phase

Implementation-ready task list. Pair with `knowledge/implementation/cursor/` or `claude-code/` prompts.

---

## Phase 0 — Foundation docs ✅

| ID | Task | Owner | Done |
|----|------|-------|------|
| P0-1 | PROJECT-OS.md | — | ✅ |
| P0-2 | AGENT-OS.md | — | ✅ |
| P0-3 | Knowledge assets (Step 3) | — | ✅ |

---

## Phase 1 — Railway + Kanban

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P1-1 | Write `deploy/railway/README.md` | deploy/ | ✅ |
| P1-2 | Create `profiles/research-agent.yaml` | profiles/ | ✅ |
| P1-3 | Create `profiles/script-agent.yaml` | profiles/ | ✅ |
| P1-4 | Create `profiles/x-optimizer-agent.yaml` | profiles/ | ✅ |
| P1-5 | Create `profiles/storage-agent.yaml` | profiles/ | ✅ |
| P1-6 | Create `runbooks/01-railway-deploy.md` | runbooks/ | ✅ |
| P1-7 | Create `runbooks/02-kanban-team.md` | runbooks/ | ✅ |
| P1-8 | Execute SOP-01 on live Railway | — | ☐ Operator |

---

## Phase 2 — Supabase

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P2-1 | Write `docs/06-supabase-schema.md` | docs/ | Full DDL spec |
| P2-2 | Write `supabase/migrations/001_content_pipeline.sql` | supabase/ | Applies cleanly |
| P2-3 | Write `supabase/policies/rls_agent_ownership.sql` | supabase/ | Per-agent matrix |
| P2-4 | Write `schemas/*.json` | schemas/ | Match columns |
| P2-5 | Write `runbooks/03-supabase-schema.md` | runbooks/ | Mirrors SOP-02 |
| P2-6 | Execute SOP-02 | — | M3 gate |

---

## Phase 3 — Research

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P3-1 | Finalize `skills/research-agent/SKILL.md` | skills/ | Testing checklist |
| P3-2 | Write `runbooks/04-research-agent.md` | runbooks/ | Mirrors SOP-03 |
| P3-3 | Install vendor + project skills on host | — | INSTALL.md |
| P3-4 | Execute SOP-03 | — | M4 gate |

---

## Phase 4 — Script

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P4-1 | Finalize `skills/script-agent/SKILL.md` | skills/ | — |
| P4-2 | Write `runbooks/05-script-agent.md` | runbooks/ | — |
| P4-3 | Execute SOP-04 | — | M5 gate |

---

## Phase 5 — X Optimizer

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P5-1 | Write `docs/09-x-algorithm-rules.md` | docs/ | All signals documented |
| P5-2 | Finalize `skills/x-optimizer-agent/SKILL.md` | skills/ | — |
| P5-3 | Write `runbooks/06-x-optimizer.md` | runbooks/ | — |
| P5-4 | Execute SOP-05 | — | M6 gate |

---

## Phase 6 — Full pipeline

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P6-1 | Finalize `skills/storage-agent/SKILL.md` | skills/ | — |
| P6-2 | Finalize `skills/pipeline-seeder/SKILL.md` | skills/ | — |
| P6-3 | Write `runbooks/07-full-pipeline.md` | runbooks/ | — |
| P6-4 | Wire Kanban fan-in for storage | — | docs/08 |
| P6-5 | Execute SOP-06 | — | M7 gate |

---

## Phase 7 — Cron

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P7-1 | Write `runbooks/08-weekly-cron.md` | runbooks/ | — |
| P7-2 | Configure Hermes cron | — | M8 gate |
| P7-3 | Revert test cron to Mon 07:00 | — | Production |

---

## Phase 8 — Hardening

| ID | Task | Artifact | Acceptance |
|----|------|----------|------------|
| P8-1 | Write `docs/10-runbook.md` | docs/ | Consolidated |
| P8-2 | Write `deploy/vps/` manifests | deploy/ | systemd unit |
| P8-3 | Write `tests/test_schema_sql.py` | tests/ | CI green |
| P8-4 | Write `tests/test_profile_yaml.py` | tests/ | — |
| P8-5 | Execute SOP-08 | — | M9 gate |

---

## Task dependencies

```text
P1-* → P2-* → P3-* → P4-* → P5-* → P6-* → P7-* → P8-*
```

Skills docs (Step 3) precede P3–P6 execution.
