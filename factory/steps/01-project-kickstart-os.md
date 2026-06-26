# Step 1 — $project-kickstart-os

**Skill:** `project-kickstart-os`  
**Gate:** M0 · **Không** code · **Không** prompts agent

---

## Objective

Build the exact **Hermes Kanban Multi-Agent Content Pipeline** demonstrated in the tutorial — modular, self-hostable, documentation-first.

---

## Input (paste vào Cursor/Codex)

```text
Build the exact multi-agent Kanban workflow demonstrated in the Hermes tutorial.

Business Goal:
Create an AI-native content operating system powered by Hermes Kanban.
The system should orchestrate multiple specialized agents that automatically
research trending topics, generate long-form content, optimize for X, store
everything in Supabase, and execute on a weekly schedule.

Expected pipeline:
Telegram → Hermes → Kanban → Research Agent → Script Agent →
X Optimizer Agent → Storage Agent → Supabase → Weekly Cron

Requirements:
- Hermes native Kanban only
- Modular architecture
- Self-hostable
- Railway/VPS deployment
- Telegram gateway
- Supabase
- TinyFish
- Weekly scheduler
- Reusable skills
- Documentation-first

Primary Reference: https://www.youtube.com/watch?v=2oKmF--xJAI
Study the complete video before generating the project.

Supporting Resources:
- Supabase: https://supabase.plug.dev/ykdVN09
- Hermes: https://github.com/NousResearch/hermes-agent
- Kanban: https://hermes-agent.nousresearch.com
- Railway: https://railway.com/deploy/hermes-agent
- TinyFish: https://tinyfish.ai
- X Algorithm: https://github.com/xai-org/x-algorithm

Required Deliverables (15):
1. Project Vision
2. Technical Architecture
3. Repository Structure
4. Folder Structure
5. Development Roadmap
6. Milestones
7. Technology Stack
8. Dependencies
9. Environment Variables
10. Risk Analysis
11. Implementation Phases
12. Acceptance Criteria
13. Documentation Plan
14. Testing Strategy
15. Future Extension Strategy

Constraints:
- Use Hermes native Kanban. Do NOT build a custom workflow engine.
- Modular, skill-first, documentation-first, AI-native workflow.
- Avoid reinventing Hermes features.

Output:
Produce only the complete Project Operating System.
Do NOT generate implementation code.
Do NOT create agents.
Do NOT generate prompts.
```

---

## Output artifacts (repo)

| File | Mục |
|------|-----|
| `docs/PROJECT-OS.md` | 15 deliverables |
| `docs/01-architecture.md` | Deep-dive |
| `docs/02-repository-layout.md` | Folder map |
| `docs/03-development-phases.md` | Video order phases |
| `docs/04-technical-roadmap.md` | Sequenced work |
| `docs/05-milestones.md` | M0–M9 |
| `.env.example` | Env catalog |
| `AGENTS.md` | Hard constraints |
| `SECURITY.md` | Secrets policy |
| `README.md` | Entry point |

Map đầy đủ: [../ARTIFACT-MAP.md](../ARTIFACT-MAP.md)

---

## Acceptance

- [ ] 15 deliverables trong PROJECT-OS
- [ ] Constraint "Hermes Kanban only" documented
- [ ] No Python engine/ code in repo
- [ ] Stakeholder sign-off M0

---

## Next

→ [02-agent-os-designer.md](02-agent-os-designer.md)
