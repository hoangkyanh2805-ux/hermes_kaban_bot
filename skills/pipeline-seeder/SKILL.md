---
name: content-pipeline-seeder
description: Seed Kanban card graph and pipeline_runs row for manual or cron-triggered content pipeline runs. Use when starting weekly or on-demand pipeline.
---

# Pipeline Seeder Skill

Used by: **default Hermes profile** or **cron orchestrator** (not a worker agent)

Contract: [docs/AGENT-OS.md §3–4](../../docs/AGENT-OS.md)

---

## Purpose

Create the Kanban task graph and `pipeline_runs` row for a new content pipeline execution — manual (Telegram) or scheduled (Monday 07:00 cron).

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Trigger type | `manual` \| `cron` | Yes |
| Run brief | User message or cron template | Yes |
| `topics_to_research` | Default: 5 | Yes |
| `topics_to_produce` | Default: 2 | Yes |
| Board slug | `content-os` or default | No |
| ISO week | Cron: `YYYY-Www` | Cron only |

---

## Outputs

| Output | Destination |
|--------|-------------|
| `pipeline-run:{uuid}` root card | Kanban |
| `research:{run_id}` card | Kanban → research-agent |
| `script:{slug}` × N cards | Kanban → script-agent |
| `x-optimize:{slug}` × N cards | Kanban → x-optimizer-agent |
| `storage:{run_id}` card | Kanban → storage-agent |
| `pipeline_runs` row | Supabase (`status=pending`, `trigger`) |
| `blocked_by` links | Kanban dependency chain + fan-in |

---

## Dependencies

| Dependency | Type |
|------------|------|
| `kanban` toolset enabled | Profile config |
| Supabase agent skill | Insert `pipeline_runs` |
| content-pipeline-kanban skill | Card naming conventions |
| Gateway + dispatcher running | Infrastructure |
| No overlapping `running` run | Scheduler policy |

---

## Card graph template

```text
pipeline-run:{uuid}
├── research:{uuid}           → research-agent
├── script:{slug_a}           → script-agent    blocked_by: research
├── script:{slug_b}           → script-agent    blocked_by: research
├── x-optimize:{slug_a}       → x-optimizer     blocked_by: script:{slug_a}
├── x-optimize:{slug_b}       → x-optimizer     blocked_by: script:{slug_b}
└── storage:{uuid}            → storage-agent   blocked_by: BOTH x-optimize cards
```

Slug placeholders filled after research for single-phase seed, OR pre-declared for full-run prompt (Step 7 uses dynamic slugs from research output — seeder creates script/x cards after research in advanced mode; tutorial creates all 4 agent cards upfront then chains via deps).

**Tutorial-simple mode:** Create 4 stage cards with sequential `blocked_by` for first integration; expand to multi-topic graph for Step 7.

---

## Examples

### Manual seed (Telegram)

User message pattern in [knowledge/prompts/full-pipeline-run.md](../../knowledge/prompts/full-pipeline-run.md)

### Cron seed

```text
weekly-run:2026-W26
trigger: cron
Creates same graph as manual with trigger=cron
```

### Overlap guard

```sql
SELECT id FROM pipeline_runs WHERE status = 'running' LIMIT 1;
-- If row exists: skip cron seed; comment on prior run
```

---

## Failure cases

| Failure | Action |
|---------|--------|
| Duplicate `weekly-run:{week}` | Skip; notify operator |
| Prior run still `running` | Skip cron per scheduler policy |
| Kanban create fails | Report error to Telegram; do not insert pipeline_runs |
| Missing kanban toolset | Instruct operator to enable on profile |

---

## Testing checklist

- [ ] Root + child cards visible in Kanban dashboard
- [ ] Correct assignees on each card
- [ ] `blocked_by` prevents script before research done
- [ ] Storage blocked until all x-optimize done
- [ ] `pipeline_runs` row with correct `trigger`
- [ ] Duplicate week seed rejected
- [ ] `hermes kanban watch` shows created events

---

## Documentation

| Reference | Path |
|-----------|------|
| Kanban conventions | [docs/08-kanban-conventions.md](../../docs/08-kanban-conventions.md) |
| Scheduler | [docs/AGENT-OS.md §4](../../docs/AGENT-OS.md) |
| SOP cron | [knowledge/sops/SOP-07-weekly-cron.md](../../knowledge/sops/SOP-07-weekly-cron.md) |
| Full pipeline prompt | [knowledge/prompts/full-pipeline-run.md](../../knowledge/prompts/full-pipeline-run.md) |
