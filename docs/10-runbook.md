# 10 — Consolidated Runbook

Operator quick path. Detailed steps in [knowledge/sops/](../knowledge/sops/).

## Prerequisites

- Hermes ≥ v2026.5.7 on Railway or VPS
- API keys in `.env.example`
- [knowledge/checklists/go-live.md](../knowledge/checklists/go-live.md)

## Deploy sequence

| Step | SOP | Time |
|------|-----|------|
| 1 | [SOP-01 Railway + Kanban](../knowledge/sops/SOP-01-railway-kanban.md) | ~1h |
| 2 | [SOP-02 Supabase](../knowledge/sops/SOP-02-supabase-schema.md) | ~1h |
| 3 | [SOP-03 Research](../knowledge/sops/SOP-03-research-agent.md) | ~1h |
| 4 | [SOP-04 Script](../knowledge/sops/SOP-04-script-agent.md) | ~30m |
| 5 | [SOP-05 X Optimizer](../knowledge/sops/SOP-05-x-optimizer.md) | ~1h |
| 6 | [SOP-06 Full pipeline](../knowledge/sops/SOP-06-full-pipeline.md) | ~1h |
| 7 | [SOP-07 Weekly cron](../knowledge/sops/SOP-07-weekly-cron.md) | ~30m |
| 8 | [SOP-08 Hardening](../knowledge/sops/SOP-08-hardening.md) | ~2h |

## One-message full run

[knowledge/prompts/full-pipeline-run.md](../knowledge/prompts/full-pipeline-run.md)

## Health checks

```bash
hermes kanban list
hermes kanban stats
hermes kanban ready
```

Supabase:

```sql
SELECT status, trigger, completed_at FROM pipeline_runs ORDER BY created_at DESC LIMIT 5;
```

## Escalation

| Symptom | Check |
|---------|-------|
| Stalled pipeline | `hermes kanban ready` — blocked cards? |
| Empty topics | TinyFish key, research skill |
| RLS error | `docs/06-supabase-schema.md` policies |
| Cron missed | Hermes schedule TZ, overlap skip |

## Document map

- Architecture: [PROJECT-OS.md](PROJECT-OS.md)
- Agents: [AGENT-OS.md](AGENT-OS.md)
- Assets: [knowledge/ASSET-INDEX.md](../knowledge/ASSET-INDEX.md)
