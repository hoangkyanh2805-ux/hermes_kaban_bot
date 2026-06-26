---
name: content-pipeline-kanban
description: Shared Kanban conventions for the Hermes content pipeline. Card naming, stages, dependencies, and worker lifecycle for all pipeline agents.
---

# Content Pipeline Kanban Skill

Used by: **all pipeline profiles** + **pipeline seeder**

Reference: [docs/08-kanban-conventions.md](../../docs/08-kanban-conventions.md)

---

## Purpose

Provide a single reference for Kanban card naming, pipeline stages, dependency wiring, and worker lifecycle so every agent behaves consistently on the shared board.

---

## Inputs

| Input | Source |
|-------|--------|
| Assigned task | `kanban_show()` |
| Pipeline stage | Card metadata `stage` field |
| Parent / blocked_by | Kanban link relations |

---

## Outputs

| Output | When |
|--------|------|
| Correct `kanban_complete` / `kanban_block` | Worker terminal |
| Formatted `kanban_comment` | Progress per [docs/AGENT-OS.md §13](../../docs/AGENT-OS.md) |
| Stage-appropriate result line | See per-agent skills |

---

## Dependencies

| Dependency | Type |
|------------|------|
| Hermes Kanban ≥ v2026.5.7 | Runtime |
| Gateway dispatcher running | Infrastructure |
| Board initialized | `hermes kanban init` |

---

## Pipeline stages

```text
TODO → RESEARCH → SCRIPT → OPTIMIZE → STORAGE → DONE
```

| Stage | Assignee profile |
|-------|------------------|
| RESEARCH | research-agent |
| SCRIPT | script-agent |
| OPTIMIZE | x-optimizer-agent |
| STORAGE | storage-agent |

---

## Card title patterns

| Pattern | Example |
|---------|---------|
| `pipeline-run:{uuid}` | `pipeline-run:abc-123` |
| `research:{run_id}` | `research:abc-123` |
| `script:{topic_slug}` | `script:ai-agents-beginners` |
| `x-optimize:{topic_slug}` | `x-optimize:ai-agents-beginners` |
| `storage:{run_id}` | `storage:abc-123` |
| `weekly-run:{YYYY-Www}` | `weekly-run:2026-W26` |

---

## Worker lifecycle (every agent)

```text
1. kanban_show()           — first action always
2. kanban_comment("start: {STAGE} {task_id}")
3. [do work]
4. kanban_heartbeat()      — if run > 5 minutes
5. kanban_complete --result "{summary}"
   OR kanban_block --reason "{actionable}"
```

**Never:** shell out to `hermes kanban` CLI from worker — use `kanban_*` tools only.

---

## Examples

### Verify upstream done (implicit)

Kanban `blocked_by` ensures promotion. Worker should still confirm task body references valid `pipeline_run_id`.

### Multi-topic fan-in

```text
storage:abc-123 blocked_by:
  - x-optimize:topic-a
  - x-optimize:topic-b
```

Storage promotes to `ready` only when **both** are `done`.

---

## Failure cases

| Failure | Action |
|---------|--------|
| Wrong assignee on card | `kanban_block` — misconfigured graph |
| Missing metadata | `kanban_block` — seeder error |
| Complete another agent's card | **Forbidden** |
| Skip `kanban_show` | Violates contract — always call first |

---

## Testing checklist

- [ ] Card titles match patterns
- [ ] Stage metadata present on worker cards
- [ ] Downstream stays `todo` until upstream `done`
- [ ] `kanban_complete` triggers Telegram notifier
- [ ] `task_events` logged in Kanban DB
- [ ] Crash → reclaim → worker respawns

---

## Documentation

| Reference | Path |
|-----------|------|
| Agent OS workflow | [docs/AGENT-OS.md §2](../../docs/AGENT-OS.md) |
| Orchestration | [docs/AGENT-OS.md §3](../../docs/AGENT-OS.md) |
| Retry logic | [docs/AGENT-OS.md §6](../../docs/AGENT-OS.md) |
