# Project Status — Snapshot

**Cập nhật:** 2026-06-26 · Operator: Railway + Supabase live · Niche: `forex-gold-signals`  
**Handoff máy khác:** [ops/HANDOFF.md](../ops/HANDOFF.md)

---

## Mới (2026-06-26) — Creator discovery

| Mục | Trạng thái |
|-----|------------|
| Bảng `x_creators` + RLS | ✅ Supabase `hermes-growth` |
| Unique X creators | ✅ **108** handles (8 quốc gia) |
| Batch 1 ID | `88274469-fe50-44a7-a95e-3b2c85e02271` |
| Skill research-agent Mode 2 | ✅ Sync Railway `/data/.hermes/skills/` |
| ICP report trong repo | ❌ Chưa — chạy [x-creators-icp-analysis.md](../knowledge/prompts/x-creators-icp-analysis.md) |
| GitHub | `f49e63b` — x_creators migration + prompts |

---

## Tóm tắt một dòng

**Runtime tutorial (M1–M8): ~90% xong — vận hành được.**  
**Repo engineering (engine/cli, M9): chưa xong.**  
**Go-live operator: còn đăng X thủ công + 1–2 tuần cron ổn định.**

---

## Phase map (video order)

| Phase | Tên | Repo | Production (Railway) | Gate |
|-------|-----|------|----------------------|------|
| 0 | Project OS | ✅ | — | M0 ✅ |
| 1 | Railway + Kanban | ✅ runbooks, profiles | ✅ deploy, Telegram, gateway | M1 ✅ M2 ⚠️ |
| 2 | Supabase schema | ✅ SQL + RLS + tests | ✅ 4 bảng + data | M3 ✅ |
| 3 | Research + TinyFish | ✅ skills, content.yaml | ✅ topics ≥5 | M4 ✅ |
| 4 | Script agent | ✅ skills, profiles | ✅ scripts | M5 ✅ |
| 5 | X optimizer | ✅ skills, docs/09 | ✅ x_posts Phoenix (2/6 pass strict) | M6 ⚠️ |
| 6 | Full pipeline | ✅ prompts, verify script | ✅ 5→2 packages, completed | M7 ✅ |
| 7 | Weekly cron | ✅ runbook 08 | ✅ Mon 07:00 VN + cron test | M8 ⚠️ |
| 8 | Hardening / M9 | ⚠️ partial | ⚠️ gateway auto-restart claimed | M9 ❌ |

**⚠️ M2:** Dùng task pipeline tổng hợp — chưa luôn 4 thẻ Kanban tách riêng như tutorial.  
**⚠️ M6:** Không phải mọi `x_posts` row pass Phoenix — cần filter hoặc regenerate.  
**⚠️ M8:** Cron đã set + 1 run `trigger=cron` — chưa chứng minh 2 thứ Hai liên tiếp unattended.  
**❌ M9:** Chưa external operator test; `engine/` + `cli/` chưa build (ngoài scope tutorial runtime).

---

## Việc operator còn lại (go-live)

1. [ ] **ICP** từ 108 creators → lưu `ops/icp-forex-gold-signals.md`
2. [ ] Đăng ≥1 post X thủ công (`export_x_post.py`) → [ops/publish-log.md](../ops/publish-log.md)
2. [ ] Thứ Hai tới: xác nhận cron chạy (`pipeline_runs.trigger=cron`)
3. [ ] Tuần 2: cron lần 2 → M8 đóng hẳn
4. [ ] (Tuỳ chọn) Regenerate 4 x_posts cũ fail Phoenix

---

## Repo chưa làm (AGENTS.md Phase 2 engine — optional)

| Item | Ghi chú |
|------|---------|
| `engine/*.py` | Domain-agnostic engine — không bắt buộc nếu chỉ dùng Hermes |
| `cli/content.py` | CLI wrapper |
| `runbooks/04–06` | Có thể bổ sung; ops đã qua Telegram |
| `scripts/weekly_seed.py` | Cron Hermes thay thế |

---

## Lệnh verify nhanh

```bash
python scripts/verify_supabase.py --relaxed-phoenix
python scripts/export_x_post.py
```

---

## Kết luận

Dự án **đủ dùng production-lite** cho niche forex/gold: cron hàng tuần → Supabase → export → đăng X tay.

**Chưa** gọi là “phase 8 / M9 hoàn tất” cho đến khi: 2 cron tuần OK + publish-log có URL thật + (tuỳ chọn) runbook reproducibility sign-off.
