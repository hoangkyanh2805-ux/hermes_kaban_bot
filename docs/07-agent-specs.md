# 07 — Agent Specifications (Summary)

Behavior summary for implementers. Full contracts: [AGENT-OS.md](AGENT-OS.md). Skills: [skills/](../skills/).

| Agent | Profile | Stage | Writes | Skill |
|-------|---------|-------|--------|-------|
| ResearchAgent | research-agent | RESEARCH | topics | content-pipeline-research |
| ScriptAgent | script-agent | SCRIPT | scripts | content-pipeline-script |
| XOptimizerAgent | x-optimizer-agent | OPTIMIZE | x_posts | content-pipeline-x-optimizer |
| StorageAgent | storage-agent | STORAGE | pipeline_runs | content-pipeline-storage |

**Seeder (not a worker):** pipeline-seeder skill on default/cron profile.

**Shared:** content-pipeline-kanban on all profiles.

## Worker loop

```text
kanban_show → work → validate → kanban_complete | kanban_block
```

## Prompt templates

[knowledge/prompts/PROMPT-INDEX.md](../knowledge/prompts/PROMPT-INDEX.md)

## Testing

[knowledge/checklists/agent-testing.md](../knowledge/checklists/agent-testing.md)
