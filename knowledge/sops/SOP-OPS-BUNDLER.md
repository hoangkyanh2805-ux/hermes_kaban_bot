# SOP-OPS: OPS Bundler — Clone pipeline cho dự án mới

**Meta-SOP** · Áp dụng sau khi hoàn thành 1 instance reference (hermes_kaban_bot)

## Purpose

Đóng gói Step 1 (Project OS) + Step 2 (Agent OS) + Step 3 (Knowledge) + OPS runtime thành quy trình tái sử dụng khi fork pipeline sang niche/domain khác.

## Prerequisites

- Reference repo: [github.com/hoangkyanh2805-ux/hermes_kaban_bot](https://github.com/hoangkyanh2805-ux/hermes_kaban_bot)
- Operator đã chạy thành công ≥1 full pipeline (M7) trên instance gốc
- [ops/OPS-BUNDLER.md](../../ops/OPS-BUNDLER.md) đã đọc

## Procedure

### A — Documentation bundle (Step 1–3)

1. Fork hoặc `git clone` reference repo.
2. Điền [ops/templates/PROJECT-BRIEF.md](../../ops/templates/PROJECT-BRIEF.md).
3. Copy [content.yaml.template](../../ops/templates/content.yaml.template) → `content.yaml`.
4. Rà soát `docs/PROJECT-OS.md` — cập nhật vision/audience (Step 1).
5. Rà soát `docs/AGENT-OS.md` — giữ workflow 4 agent trừ khi mở rộng (Step 2).
6. Cập nhật skills + prompts theo niche (Step 3) — xem file matrix trong OPS-BUNDLER.
7. Reset `ops/publish-log.md`, `docs/PROJECT-STATUS.md`.

### B — Infrastructure clone (OPS Phase 1–2)

8. Deploy Railway Hermes mới (hoặc service riêng) — [SOP-01](SOP-01-railway-kanban.md).
9. Supabase project mới + apply migrations — [SOP-02](SOP-02-supabase-schema.md).
10. Sync secrets: Railway Variables **và** `/data/.env` on volume.

### C — Runtime validation (OPS Phase 3–7)

11. TinyFish + research — [SOP-03](SOP-03-research-agent.md).
12. Script + X optimize — [SOP-04](SOP-04-script-agent.md), [SOP-05](SOP-05-x-optimizer.md).
13. Full pipeline — [SOP-06](SOP-06-full-pipeline.md).
14. Weekly cron — [SOP-07](SOP-07-weekly-cron.md).
15. Gateway hardening — [runbooks/09-gateway-hardening.md](../../runbooks/09-gateway-hardening.md).

### D — Go-live

16. Manual X publish — [SOP-09](SOP-09-manual-x-publish.md).
17. Verify: `python scripts/verify_supabase.py`.
18. Sign-off [ops/clone-checklist.md](../../ops/clone-checklist.md).

## Outputs

| Output | Location |
|--------|----------|
| New GitHub repo | Operator account |
| Live Hermes + Supabase | Railway + Supabase |
| Domain config | `content.yaml` |
| Operator checklist | `ops/clone-checklist.md` completed |

## What NOT to copy

- `.env` / API keys
- Supabase production rows
- Railway volume `/data` state
- Telegram bot token (tạo bot mới hoặc dùng riêng per project)

## Escalation

| Issue | Action |
|-------|--------|
| Schema change needed | New migration in `supabase/migrations/` — update AGENT-OS §7 |
| Fifth agent needed | New profile + table + Kanban stage — update PROJECT-OS extension |
| Auto-post required | Explicit v2 scope — not in bundler v1 |

## Reference checklist

[ops/clone-checklist.md](../../ops/clone-checklist.md)

## Related

- [ops/OPS-BUNDLER.md](../../ops/OPS-BUNDLER.md)
- [knowledge/ASSET-INDEX.md](../ASSET-INDEX.md)
- [docs/03-development-phases.md](../../docs/03-development-phases.md)
