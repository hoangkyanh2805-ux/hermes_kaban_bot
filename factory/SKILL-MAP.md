# Skill Map — Factory workflow

Ba skill dùng **tuần tự** khi bắt đầu dự án Hermes Kanban pipeline từ idea/video.

---

## Bảng chọn skill

| Skill | Dùng khi | Input | Output | Không làm |
|-------|----------|-------|--------|-----------|
| **`project-kickstart-os`** | Idea thô, video YouTube, case study, repo GitHub, bài Facebook, brainstorm | Brief, link video, business goal | PROJECT-OS: architecture, phases, milestones, folder layout | Code, agents, prompts |
| **`agent-os-designer`** | Đã có PROJECT-OS; cần agent loop, permission, stop condition | `docs/PROJECT-OS.md` | AGENT-OS: 4 agent, Kanban, scheduler, DB ownership | Code, SQL |
| **`knowledge-asset-factory`** | Đã có PROJECT-OS + AGENT-OS | Cả hai OS docs | skills/, SOP, prompts, checklists, implementation prompts | Runtime code |

---

## Skill bổ sung (ngoài 3 step — khi cần)

| Skill | Dùng khi |
|-------|----------|
| `knowledge-asset-factory` (lại) | Pivot niche — đổi prompts/skills (vd. AI → forex/gold) |
| OPS Bundler (repo nội bộ) | Clone instance sang dự án mới |
| Cursor Agent | Phase implementation: SQL, scripts, runbooks |

---

## Thứ tự bắt buộc

```text
idea / video
    ↓
project-kickstart-os     (Step 1)
    ↓
agent-os-designer        (Step 2)
    ↓
knowledge-asset-factory  (Step 3)
    ↓
OPS runtime + deploy     (Step 4 — không phải skill, là operator)
    ↓
OPS Bundler clone        (Step 5 — dự án tiếp theo)
```

**Không đảo Step 2 trước Step 1.**  
**Không implement Railway trước khi Step 3 prompts/skills có.**

---

## Prompt files trong repo (copy vào Cursor/Codex)

| Step | File |
|------|------|
| 0 Brief | [steps/00-idea-to-brief.md](steps/00-idea-to-brief.md) |
| 1 | [steps/01-project-kickstart-os.md](steps/01-project-kickstart-os.md) |
| 2 | [steps/02-agent-os-designer.md](steps/02-agent-os-designer.md) |
| 3 | [steps/03-knowledge-asset-factory.md](steps/03-knowledge-asset-factory.md) |

Implementation prompts (sau Step 3): `knowledge/implementation/cursor/PHASE-*.md`

---

## Ví dụ dự án này

| Step | Skill | Artifact chính |
|------|-------|----------------|
| 1 | project-kickstart-os | `docs/PROJECT-OS.md`, `docs/01–05` |
| 2 | agent-os-designer | `docs/AGENT-OS.md` |
| 3 | knowledge-asset-factory | `knowledge/`, `skills/` |
| 4 | OPS (operator) | Railway live, `content.yaml` forex/gold |
| 5 | OPS Bundler | `ops/OPS-BUNDLER.md` |
