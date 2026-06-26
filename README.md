# Hermes Kanban Multi-Agent Content Pipeline

Faithful reproduction of the [Derek Cheung Hermes Kanban content pipeline tutorial](https://www.youtube.com/watch?v=2oKmF--xJAI) — adapted for **forex/gold/XAUUSD signal content**: research trending gold topics, write trading scripts, optimize for X, persist to Supabase, weekly cron.

> **Status:** Runtime **M7–M8 (~90%)** — cron + forex/gold live. Chưa M9. [docs/PROJECT-STATUS.md](docs/PROJECT-STATUS.md)

## Triển khai

| Phase | Tài nguyên | Đường dẫn |
|-------|------------|-----------|
| 1 | Deploy Railway | [deploy/railway/README.md](deploy/railway/README.md) |
| 2 | Supabase SQL | [supabase/migrations/001_content_pipeline.sql](supabase/migrations/001_content_pipeline.sql) |
| 7 | **Verify Supabase** | `python scripts/verify_supabase.py` |
| 7 | Review + Phoenix | [runbooks/07-full-pipeline-review.md](runbooks/07-full-pipeline-review.md) |
| 8 | Weekly cron | [runbooks/08-weekly-cron.md](runbooks/08-weekly-cron.md) |
| publish | **Manual X (v1)** | [docs/12-manual-x-publish.md](docs/12-manual-x-publish.md) · `scripts/export_x_post.py` |
| domain | **Audience config** | [content.yaml](content.yaml) · `forex-gold-signals` |
| **clone** | **OPS Bundler** | [ops/OPS-BUNDLER.md](ops/OPS-BUNDLER.md) |
| **keys** | **API & Supabase setup** | [ops/CREDENTIALS-AND-KEYS.md](ops/CREDENTIALS-AND-KEYS.md) |
| **factory** | **Workflow video→3 skill→build** | [factory/WORKFLOW.md](factory/WORKFLOW.md) |
| ops | Gateway 24/7 | [runbooks/09-gateway-hardening.md](runbooks/09-gateway-hardening.md) |
| 1 | Profiles | [profiles/](profiles/) |

## Pipeline

```
Telegram
   ↓
Hermes Gateway (Kanban dispatcher)
   ↓
Kanban Board (shared scoreboard — SQLite)
   ↓
Research Agent → Script Agent → X Optimizer Agent → Storage Agent
   (TinyFish)        (draft)         (Phoenix signals)    (Supabase coord)
   ↓
Supabase (topics · scripts · x_posts · pipeline_runs)
   ↓
**Manual X publish (v1)** — operator copy-paste from export script
   ↓
Weekly Cron (Monday 07:00)
```

## Design philosophy

- **Kanban is the bus** — agents coordinate through cards, not shared in-process state
- **Skill-first** — Supabase and TinyFish capabilities installed as Hermes skills
- **Native Hermes only** — no custom workflow engine, queue, or orchestrator service
- **Supabase is the artifact store** — agents read upstream / write downstream via tables
- **One message kicks the pipeline** — full runs coordinated by Kanban dependencies
- **Manual X publish in v1** — agents stop at `x_posts`; human posts via [docs/12-manual-x-publish.md](docs/12-manual-x-publish.md)

## Documentation

| Document | Contents |
|----------|----------|
| [**docs/PROJECT-OS.md**](docs/PROJECT-OS.md) | **Project OS** — Step 1 (15 deliverables) |
| [**docs/AGENT-OS.md**](docs/AGENT-OS.md) | **Agent OS** — Step 2 (contracts, workflow, retry) |
| [**knowledge/ASSET-INDEX.md**](knowledge/ASSET-INDEX.md) | **Knowledge assets** — Step 3 (skills, SOPs, prompts) |
| [docs/01-architecture.md](docs/01-architecture.md) | Technical architecture deep-dive |
| [docs/02-repository-layout.md](docs/02-repository-layout.md) | Repository and folder structure |
| [docs/03-development-phases.md](docs/03-development-phases.md) | Implementation phases (video order) |
| [docs/04-technical-roadmap.md](docs/04-technical-roadmap.md) | Sequenced work items |
| [docs/05-milestones.md](docs/05-milestones.md) | Milestones and acceptance criteria |
| [AGENTS.md](AGENTS.md) | Rules for AI agents implementing this project |

## Primary references

- [Tutorial video](https://www.youtube.com/watch?v=2oKmF--xJAI) — primary architectural reference
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · [Kanban docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Railway template](https://railway.com/deploy/hermes-agent) · [Supabase plug](https://supabase.plug.dev/ykdVN09)
- [TinyFish](https://tinyfish.ai) · [X Algorithm (Phoenix)](https://github.com/xai-org/x-algorithm)
- [Prompt reference repo](https://github.com/derekcheungsa/ai-automation-resources) (guide PDF in repo)
