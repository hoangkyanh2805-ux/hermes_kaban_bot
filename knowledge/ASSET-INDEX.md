# Knowledge Asset Index

Complete catalog of Step 3 reusable assets.

---

## Skills (Hermes runtime)

| Skill | Path | Agent / role |
|-------|------|--------------|
| Research Agent | [skills/research-agent/SKILL.md](../skills/research-agent/SKILL.md) | ResearchAgent |
| Script Agent | [skills/script-agent/SKILL.md](../skills/script-agent/SKILL.md) | ScriptAgent |
| X Optimizer | [skills/x-optimizer-agent/SKILL.md](../skills/x-optimizer-agent/SKILL.md) | XOptimizerAgent |
| Storage Agent | [skills/storage-agent/SKILL.md](../skills/storage-agent/SKILL.md) | StorageAgent |
| Pipeline Seeder | [skills/pipeline-seeder/SKILL.md](../skills/pipeline-seeder/SKILL.md) | Cron / human seed |
| Kanban Conventions | [skills/content-pipeline-kanban/SKILL.md](../skills/content-pipeline-kanban/SKILL.md) | All workers |
| Install guide | [skills/INSTALL.md](../skills/INSTALL.md) | Operator |

**External (vendor):** TinyFish `use-tinyfish`, Supabase agent skill — see `skills/INSTALL.md`.

---

## SOPs (standard operating procedures)

| Phase | SOP | Video step |
|-------|-----|------------|
| 0 | [SOP-00-project-foundation.md](sops/SOP-00-project-foundation.md) | — |
| 1 | [SOP-01-railway-kanban.md](sops/SOP-01-railway-kanban.md) | 1–2 |
| 2 | [SOP-02-supabase-schema.md](sops/SOP-02-supabase-schema.md) | 3 |
| 3 | [SOP-03-research-agent.md](sops/SOP-03-research-agent.md) | 4 |
| 4 | [SOP-04-script-agent.md](sops/SOP-04-script-agent.md) | 5 |
| 5 | [SOP-05-x-optimizer.md](sops/SOP-05-x-optimizer.md) | 6 |
| 6 | [SOP-06-full-pipeline.md](sops/SOP-06-full-pipeline.md) | 7 |
| 7 | [SOP-07-weekly-cron.md](sops/SOP-07-weekly-cron.md) | Bonus |
| 8 | [SOP-08-hardening.md](sops/SOP-08-hardening.md) | — |
| 9 | [SOP-09-manual-x-publish.md](sops/SOP-09-manual-x-publish.md) | Go-live |
| **OPS** | **[SOP-OPS-BUNDLER.md](sops/SOP-OPS-BUNDLER.md)** | **Clone dự án mới** |

---

## OPS Bundler (clone template)

| Asset | Path |
|-------|------|
| **Master guide** | [ops/OPS-BUNDLER.md](../ops/OPS-BUNDLER.md) |
| Clone checklist | [ops/clone-checklist.md](../ops/clone-checklist.md) |
| Project brief template | [ops/templates/PROJECT-BRIEF.md](../ops/templates/PROJECT-BRIEF.md) |
| content.yaml template | [ops/templates/content.yaml.template](../ops/templates/content.yaml.template) |
| Publish log | [ops/publish-log.md](../ops/publish-log.md) |

---

## Factory workflow (idea → 3 skills → build)

| Asset | Path |
|-------|------|
| **End-to-end workflow** | [factory/WORKFLOW.md](../factory/WORKFLOW.md) |
| Skill map | [factory/SKILL-MAP.md](../factory/SKILL-MAP.md) |
| Artifact map | [factory/ARTIFACT-MAP.md](../factory/ARTIFACT-MAP.md) |
| Step prompts | [factory/steps/](../factory/steps/) |

---

## Prompt templates

| Template | Path | Use when |
|----------|------|----------|
| Index | [prompts/PROMPT-INDEX.md](prompts/PROMPT-INDEX.md) | Finding the right template |
| Supabase schema | [prompts/supabase-schema-setup.md](prompts/supabase-schema-setup.md) | Phase 2 |
| Kanban team | [prompts/kanban-team-setup.md](prompts/kanban-team-setup.md) | Phase 1 |
| Research config | [prompts/research-agent-config.md](prompts/research-agent-config.md) | Phase 3 |
| Script config | [prompts/script-agent-config.md](prompts/script-agent-config.md) | Phase 4 |
| X optimizer config | [prompts/x-optimizer-config.md](prompts/x-optimizer-config.md) | Phase 5 |
| Full pipeline | [prompts/full-pipeline-run.md](prompts/full-pipeline-run.md) | Phase 6 |
| Weekly cron | [prompts/weekly-cron-setup.md](prompts/weekly-cron-setup.md) | Phase 7 |

---

## Checklists

| Checklist | Path |
|-----------|------|
| Phase gates (M0–M9) | [checklists/phase-gates.md](checklists/phase-gates.md) |
| Per-agent testing | [checklists/agent-testing.md](checklists/agent-testing.md) |
| Go-live | [checklists/go-live.md](checklists/go-live.md) |
| Pre-deploy security | [checklists/pre-deploy-security.md](checklists/pre-deploy-security.md) |

---

## Development tasks

| Document | Path |
|----------|------|
| All phases | [tasks/PHASE-TASKS.md](tasks/PHASE-TASKS.md) |

---

## Implementation prompts (coding agents)

### Cursor

| Phase | Prompt |
|-------|--------|
| README | [implementation/cursor/README.md](implementation/cursor/README.md) |
| 0–8 | [implementation/cursor/](implementation/cursor/) |

### Claude Code

| Phase | Prompt |
|-------|--------|
| README | [implementation/claude-code/README.md](implementation/claude-code/README.md) |
| 0–8 | [implementation/claude-code/](implementation/claude-code/) |

---

## Supporting documentation (docs/)

| Doc | Status |
|-----|--------|
| [docs/06-supabase-schema.md](../docs/06-supabase-schema.md) | Schema spec |
| [docs/07-agent-specs.md](../docs/07-agent-specs.md) | Agent behavior summary |
| [docs/09-x-algorithm-rules.md](../docs/09-x-algorithm-rules.md) | X optimizer rules |
| [docs/10-runbook.md](../docs/10-runbook.md) | Consolidated runbook |
