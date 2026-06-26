# Kanban Conventions

Companion to [AGENT-OS.md](AGENT-OS.md) §2. Card naming, dependencies, and stage tags.

---

## Stage pipeline

```text
TODO → RESEARCH → SCRIPT → OPTIMIZE → STORAGE → DONE
```

Every worker card carries metadata:

```yaml
pipeline_run_id: <uuid>
stage: RESEARCH | SCRIPT | OPTIMIZE | STORAGE
topic_slug: <optional>
```

---

## Card templates

| Title | Assignee | blocked_by | stage |
|-------|----------|------------|-------|
| `pipeline-run:{uuid}` | — | — | TODO |
| `research:{run_id}` | research-agent | — | RESEARCH |
| `script:{topic_slug}` | script-agent | research:{run_id} | SCRIPT |
| `x-optimize:{topic_slug}` | x-optimizer-agent | script:{topic_slug} | OPTIMIZE |
| `storage:{run_id}` | storage-agent | all x-optimize siblings | STORAGE |

---

## Fan-in rule (storage)

Storage card lists **all** `x-optimize:*` cards as `blocked_by`. Kanban auto-promotes storage to `ready` only when every sibling is `done`.

---

## Hermes CLI examples (human/seeder only)

Structural reference — not implementation:

```bash
# Research card
hermes kanban create "research:abc123" \
  --assignee research-agent \
  --parent pipeline-run:abc123

# Script card with dependency
hermes kanban create "script:ai-agents-beginners" \
  --assignee script-agent \
  --blocked-by research:abc123
```

Workers use `kanban_*` tools — not CLI.

---

## Status reference

| Status | Meaning |
|--------|---------|
| `todo` | Created; may wait on parents |
| `ready` | Parents done; dispatcher may claim |
| `in_progress` | Worker active |
| `done` | `kanban_complete` called |
| `blocked` | Needs human `kanban_unblock` |
| `crashed` | Worker died; reclaim pending |
| `gave_up` | Max retries exceeded |
