# Hermes Skills — Content Pipeline

Install these into the Hermes runtime. Each skill includes Purpose, Inputs, Outputs, Dependencies, Examples, Failure cases, Testing checklist, and Documentation.

## Project skills (this repo)

| Skill | Directory | Profile |
|-------|-----------|---------|
| Research | [research-agent/](research-agent/SKILL.md) | `research-agent` |
| Script | [script-agent/](script-agent/SKILL.md) | `script-agent` |
| X Optimizer | [x-optimizer-agent/](x-optimizer-agent/SKILL.md) | `x-optimizer-agent` |
| Storage | [storage-agent/](storage-agent/SKILL.md) | `storage-agent` |
| Pipeline Seeder | [pipeline-seeder/](pipeline-seeder/SKILL.md) | default / cron profile |
| Kanban conventions | [content-pipeline-kanban/](content-pipeline-kanban/SKILL.md) | all profiles |

## Vendor skills (external)

| Skill | Source | Used by |
|-------|--------|---------|
| Supabase agent | Install via Hermes conversation | script, x-opt, storage, research |
| TinyFish `use-tinyfish` | [tinyfish-cookbook](https://github.com/tinyfish-io/tinyfish-cookbook) | research-agent |

See [INSTALL.md](INSTALL.md) for installation steps.

## Binding skills to profiles

```yaml
# profiles/research-agent.yaml (preview)
skills:
  - content-pipeline-research
  - content-pipeline-kanban
  - use-tinyfish          # vendor
```
