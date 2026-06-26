---
name: content-pipeline-storage
description: Reconcile Kanban pipeline completion with Supabase artifact counts. Finalize pipeline_runs status. Last stage before DONE.
---

# Storage Agent Skill

Hermes profile: `storage-agent` · Pipeline stage: **STORAGE**

Contract: [docs/AGENT-OS.md §11](../../docs/AGENT-OS.md)

---

## Purpose

Finalize the pipeline run by auditing Kanban card completion against Supabase row counts, setting authoritative `pipeline_runs.status`, and marking the run **DONE**.

Storage coordinates cross-stage consistency — it does **not** edit `topics`, `scripts`, or `x_posts` content.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Kanban task | `kanban_show()` | Yes |
| `pipeline_run_id` | Card metadata | Yes |
| All `x-optimize:*` siblings | Kanban fan-in | All `done` |
| Artifact tables | Supabase COUNT queries | Yes |
| Expected package count | Task body (default: 2) | Yes |

---

## Outputs

| Output | Destination |
|--------|-------------|
| `pipeline_runs.status` | `completed` \| `partial` \| `failed` |
| `pipeline_runs.completed_at` | timestamptz |
| `topics_researched`, `topics_produced`, `packages_produced` | counts |
| `error_summary` | on partial/failed |
| Reconciliation comment | Root `pipeline-run` card |
| Summary | `kanban_complete --result` |

**Result line format:** `run: {status} packages={n}/{expected}`

---

## Dependencies

| Dependency | Type |
|------------|------|
| Supabase agent skill | Hermes skill |
| ALL `x-optimize:{slug}` cards `done` | Kanban fan-in |
| `pipeline_runs` row | Supabase |

**Runs last** in the chain: TODO → RESEARCH → SCRIPT → OPTIMIZE → **STORAGE** → DONE

---

## Reconciliation procedure

```text
1. kanban_show → pipeline_run_id, expected counts
2. Verify all x-optimize siblings = done
3. COUNT topics WHERE pipeline_run_id = ?
4. COUNT scripts JOIN topics for run
5. COUNT x_posts JOIN scripts for run
6. Compare actual vs expected
7. UPDATE pipeline_runs SET status, counts, completed_at
8. kanban_comment reconciliation matrix on root card
9. kanban_complete
```

### Status decision

| Condition | status |
|-----------|--------|
| All counts match expected; no critical `gave_up` | `completed` |
| Some packages missing | `partial` |
| Research or critical card `gave_up` | `failed` |

---

## Examples

### Reconciliation comment

```text
audit: run abc-123
topics: 5 (expected ≥5) ✓
scripts: 2/2 ✓
x_posts: 2/2 ✓
status: completed
```

### Partial run example

```text
audit: scripts 2/2, x_posts 1/2
failed: x-optimize:topic-b gave_up
status: partial
```

---

## Failure cases

| Failure | Action |
|---------|--------|
| x-optimize sibling not done | Should not spawn (Kanban gate) |
| Count mismatch | `partial` or `kanban_block` if unresolvable |
| Supabase update conflict | Retry 3× (30s backoff) |
| Missing pipeline_runs row | INSERT then UPDATE (idempotent) |

---

## Testing checklist

- [ ] Storage card `todo` until ALL x-optimize siblings `done`
- [ ] `pipeline_runs.status = completed` on full success
- [ ] Counts match Supabase queries
- [ ] `error_summary` populated on partial
- [ ] Root card receives audit comment
- [ ] No writes to topics/scripts/x_posts body fields
- [ ] Telegram receives final run summary
- [ ] Re-run storage idempotent (no duplicate status flip)

---

## Documentation

| Reference | Path |
|-----------|------|
| Agent contract | [docs/AGENT-OS.md §11](../../docs/AGENT-OS.md) |
| SOP | [knowledge/sops/SOP-06-full-pipeline.md](../../knowledge/sops/SOP-06-full-pipeline.md) |
| DB ownership | [docs/AGENT-OS.md §7](../../docs/AGENT-OS.md) |
