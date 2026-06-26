# 02 — Repository & Folder Structure

Canonical layout for reproducing the [tutorial pipeline](https://www.youtube.com/watch?v=2oKmF--xJAI). See [PROJECT-OS.md §3–4](PROJECT-OS.md) for deliverables context.

---

## Design principle

**The pipeline runs in Hermes, not in this repo.**

This repository holds:

- Specifications and runbooks
- Supabase schema as SQL
- Profile and skill install manifests
- Deploy documentation

It does **not** hold a custom Python workflow engine, agent prompts, or SKILL.md bodies (those install into Hermes at runtime).

---

## Repository tree

```
hermes-content-pipeline/
├── README.md
├── AGENTS.md
├── SECURITY.md
├── .env.example
├── .gitignore
│
├── docs/
│   ├── PROJECT-OS.md              # Master OS (15 deliverables)
│   ├── 01-architecture.md
│   ├── 02-repository-layout.md    # This file
│   ├── 03-development-phases.md
│   ├── 04-technical-roadmap.md
│   ├── 05-milestones.md
│   ├── 06-supabase-schema.md      # Phase 2 — full DDL spec
│   ├── 07-agent-specs.md          # Phase 3 — behavior, no prompts
│   ├── 08-kanban-conventions.md # Card naming, assignees
│   ├── 09-x-algorithm-rules.md    # Phoenix signal reference
│   ├── 10-runbook.md              # Consolidated go-live
│   └── 11-documentation-plan.md
│
├── supabase/
│   ├── migrations/
│   │   └── 001_content_pipeline.sql
│   ├── policies/
│   │   └── rls_agent_ownership.sql
│   └── README.md
│
├── deploy/
│   ├── railway/
│   │   ├── README.md
│   │   └── volume-notes.md
│   └── vps/
│       ├── hermes-gateway.service
│       └── README.md
│
├── skills/
│   ├── INSTALL.md
│   ├── supabase-agent.manifest.yaml
│   └── tinyfish.manifest.yaml
│
├── profiles/
│   ├── research-agent.yaml
│   ├── script-agent.yaml
│   ├── x-optimizer-agent.yaml
│   └── storage-agent.yaml
│
├── schemas/                       # JSON Schema for row validation
│   ├── topic.json
│   ├── script.json
│   ├── x_post.json
│   └── pipeline_run.json
│
├── runbooks/                      # 1:1 with video steps
│   ├── 01-railway-deploy.md
│   ├── 02-kanban-team.md
│   ├── 03-supabase-schema.md
│   ├── 04-research-agent.md
│   ├── 05-script-agent.md
│   ├── 06-x-optimizer.md
│   ├── 07-full-pipeline.md
│   └── 08-weekly-cron.md
│
└── tests/
    ├── test_schema_sql.py
    └── test_profile_yaml.py
```

---

## Folder responsibilities

| Folder | Edited when | Never contains |
|--------|-------------|----------------|
| `docs/` | Design changes | Prompts, secrets |
| `supabase/` | Schema evolution | Live data |
| `deploy/` | Host changes | API keys |
| `skills/` | Skill source URL changes | SKILL.md copies |
| `profiles/` | Agent toolset changes | Runtime config |
| `runbooks/` | Tutorial steps change | Implementation code |
| `schemas/` | Column changes | — |
| `tests/` | Schema/profile lint | LLM integration tests |

---

## Hermes runtime paths (not in git)

Railway volume `/data` or `~/.hermes/`:

```
config.yaml                 # LLM, Telegram, cron, MCP
kanban.db                   # Coordination (or boards/<slug>/)
skills/                     # Installed Supabase + TinyFish skills
state.db                    # Hermes session memory (≠ content)
```

---

## Profile YAML fragment (structure only)

```yaml
# profiles/research-agent.yaml — structural preview
name: research-agent
model: deepseek-chat          # tutorial default; override per deploy
toolsets:
  - terminal
  - web
skills:
  - use-tinyfish
memory:
  enabled: true
```

Full spec: `docs/07-agent-specs.md` (Phase 3).

---

## Kanban conventions preview

| Card title pattern | Assignee |
|--------------------|----------|
| `research:pipeline-{run_id}` | research-agent |
| `script:topic-{slug}` | script-agent |
| `x-optimize:topic-{slug}` | x-optimizer-agent |
| `storage:pipeline-{run_id}` | storage-agent |
| `weekly-run:YYYY-Www` | cron orchestrator |

Full spec: `docs/08-kanban-conventions.md` (Phase 2).
