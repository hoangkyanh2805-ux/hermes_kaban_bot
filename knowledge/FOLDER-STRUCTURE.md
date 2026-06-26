# Knowledge & Project Folder Structure

Complete layout after Step 3 (knowledge assets). Implementation folders are **documented**; code is added in later steps by implementers.

```text
hermes-content-pipeline/
│
├── README.md                          # Project entry
├── AGENTS.md                          # AI implementer rules
├── SECURITY.md
├── .env.example
│
├── docs/                              # Architecture & OS (Steps 1–2)
│   ├── PROJECT-OS.md
│   ├── AGENT-OS.md
│   ├── 01-architecture.md … 05-milestones.md
│   ├── 06-supabase-schema.md
│   ├── 07-agent-specs.md
│   ├── 08-kanban-conventions.md
│   ├── 09-x-algorithm-rules.md
│   └── 10-runbook.md
│
├── knowledge/                         # ★ Step 3 reusable assets
│   ├── README.md
│   ├── ASSET-INDEX.md
│   ├── FOLDER-STRUCTURE.md            # (this file)
│   ├── sops/                          # SOP-00 … SOP-08
│   ├── prompts/                       # Telegram / Hermes templates
│   ├── checklists/
│   ├── tasks/
│   └── implementation/
│       ├── cursor/                    # Cursor agent prompts
│       └── claude-code/               # Claude Code prompts
│
├── skills/                            # Hermes SKILL.md (install to ~/.hermes)
│   ├── README.md
│   ├── INSTALL.md
│   ├── research-agent/
│   ├── script-agent/
│   ├── x-optimizer-agent/
│   ├── storage-agent/
│   ├── pipeline-seeder/
│   └── content-pipeline-kanban/
│
├── profiles/                          # (Phase 1+) Hermes profile YAML
├── supabase/                          # (Phase 2+) migrations, policies
├── deploy/                            # (Phase 8+) railway, vps
├── runbooks/                          # Operator mirrors of SOPs (short form)
├── schemas/                           # (Phase 2+) JSON row schemas
└── tests/                             # (Phase 8+) schema lint only
```

## Asset placement rules

| Content type | Goes in | Never in |
|--------------|---------|----------|
| Agent behavior for Hermes | `skills/*/SKILL.md` | `engine/` |
| Operator procedures | `knowledge/sops/` | Prompt bodies in code |
| Copy-paste Hermes messages | `knowledge/prompts/` | Committed secrets |
| Phase acceptance | `knowledge/checklists/` | — |
| IDE implementation briefs | `knowledge/implementation/` | — |
| DDL source of truth | `supabase/migrations/` | Skills |
| Architecture decisions | `docs/` | `knowledge/` (link only) |

## Runtime (not in git)

```text
/data/  or  ~/.hermes/
├── config.yaml
├── kanban/kanban.db
├── skills/          ← copied from repo skills/
└── state.db
```
