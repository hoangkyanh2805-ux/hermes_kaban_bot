# Artifact Map — Step → file trong repo

Map output từng factory step sang đường dẫn thực tế trong [hermes_kaban_bot](https://github.com/hoangkyanh2805-ux/hermes_kaban_bot).

---

## Step 1 — project-kickstart-os → Project OS

| Deliverable (#) | File trong repo |
|-----------------|-----------------|
| 1 Project Vision | `docs/PROJECT-OS.md` §1 |
| 2 Technical Architecture | `docs/01-architecture.md` |
| 3 Repository Structure | `docs/02-repository-layout.md` |
| 4 Folder Structure | `docs/02-repository-layout.md` |
| 5 Development Roadmap | `docs/04-technical-roadmap.md` |
| 6 Milestones | `docs/05-milestones.md` |
| 7 Technology Stack | `docs/PROJECT-OS.md` §8 |
| 8 Dependencies | `docs/PROJECT-OS.md` §9 |
| 9 Environment Variables | `.env.example` |
| 10 Risk Analysis | `docs/PROJECT-OS.md` §10 |
| 11 Implementation Phases | `docs/03-development-phases.md` |
| 12 Acceptance Criteria | `docs/05-milestones.md` |
| 13 Documentation Plan | `docs/11-documentation-plan.md` (nếu có) / PROJECT-OS |
| 14 Testing Strategy | `docs/PROJECT-OS.md` §14 |
| 15 Future Extension | `docs/PROJECT-OS.md` §15 |
| Agent rules | `AGENTS.md` |
| Security | `SECURITY.md` |
| README | `README.md` |

**Gate:** M0 — [knowledge/checklists/phase-gates.md](../knowledge/checklists/phase-gates.md)

---

## Step 2 — agent-os-designer → Agent OS

| Deliverable | File |
|-------------|------|
| 4 agent contracts | `docs/AGENT-OS.md` §8–11 |
| Kanban workflow | `docs/AGENT-OS.md` §2, `docs/08-kanban-conventions.md` |
| Scheduler / cron model | `docs/AGENT-OS.md` §scheduler |
| Pipeline state | `docs/AGENT-OS.md` §state |
| Retry logic | `docs/AGENT-OS.md` per-agent |
| DB ownership | `docs/AGENT-OS.md` §7 |
| Supabase DDL spec | `docs/06-supabase-schema.md` |
| X algorithm ref | `docs/09-x-algorithm-rules.md` |
| Profile skeletons | `profiles/*.yaml` |

---

## Step 3 — knowledge-asset-factory → Knowledge

| Asset type | Location |
|------------|----------|
| Skills (6) | `skills/*/SKILL.md` |
| Skill install | `skills/INSTALL.md` |
| SOP 00–09 | `knowledge/sops/` |
| SOP OPS Bundler | `knowledge/sops/SOP-OPS-BUNDLER.md` |
| Prompt templates | `knowledge/prompts/` |
| Prompt index | `knowledge/prompts/PROMPT-INDEX.md` |
| Checklists | `knowledge/checklists/` |
| Phase tasks | `knowledge/tasks/PHASE-TASKS.md` |
| Asset index | `knowledge/ASSET-INDEX.md` |
| Cursor prompts | `knowledge/implementation/cursor/PHASE-*.md` |
| Claude prompts | `knowledge/implementation/claude-code/PHASE-*.md` |

---

## Step 4 — OPS runtime (implementation)

| Phase | Artifacts |
|-------|-----------|
| 1 Railway | `deploy/railway/`, `runbooks/01`, `02`, `profiles/` |
| 2 Supabase | `supabase/migrations/`, `policies/`, `schemas/`, `runbooks/03` |
| 3–7 Agents | Live Hermes + Telegram prompts |
| Verify | `scripts/verify_supabase.py`, `scripts/export_x_post.py` |
| Domain config | `content.yaml` |
| Go-live | `runbooks/07–10`, `docs/12-manual-x-publish.md` |
| Status | `docs/PROJECT-STATUS.md` |
| Publish log | `ops/publish-log.md` |

---

## Step 5 — Factory meta (folder này)

| File | Purpose |
|------|---------|
| `factory/WORKFLOW.md` | End-to-end diagram |
| `factory/steps/*.md` | Prompts từng step |
| `ops/OPS-BUNDLER.md` | Clone kit |

---

## Clone dự án mới — file phải sửa

Xem [ops/clone-checklist.md](../ops/clone-checklist.md) · Template [ops/templates/](../ops/templates/)
