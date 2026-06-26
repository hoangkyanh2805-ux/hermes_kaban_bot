# OPS Bundler — Clone Hermes Kanban Pipeline cho dự án mới

**Gói vận hành** tổng hợp Step 1 → 2 → 3 + triển khai thực tế (Railway → Supabase → cron → đăng X thủ công).

Dùng repo này làm **template**. Dự án mới = fork + điền brief + đổi niche trong `content.yaml`.

---

## OPS Bundler là gì?

| Thành phần | Mô tả |
|------------|--------|
| **Step 1 — Project OS** | Kiến trúc, milestone, rủi ro, env vars (`docs/PROJECT-OS.md`) |
| **Step 2 — Agent OS** | 4 agent, Kanban, Supabase ownership (`docs/AGENT-OS.md`) |
| **Step 3 — Knowledge** | Skills, SOP, prompts, checklists (`knowledge/`) |
| **OPS Runtime** | Railway, Telegram, Supabase, cron, verify scripts |
| **Clone kit** | Checklist + template điền niche mới (`ops/clone-checklist.md`) |

**Không clone:** secrets (`.env`), data Supabase production, volume Railway `/data`.

---

## Khi nào dùng bundler này?

✅ Pipeline **research → script → optimize → storage** trên Hermes Kanban  
✅ Output lưu **Supabase** + notify **Telegram**  
✅ Human **đăng X thủ công** (v1)  
✅ Cron **hàng tuần**

❌ Custom Celery/Redis orchestrator  
❌ Auto-post X API (v2 — scope riêng)  
❌ Single monolithic agent prompt

---

## Quy trình clone (tóm tắt)

```text
1. Fork repo → đổi tên project
2. Điền ops/templates/PROJECT-BRIEF.md
3. Copy content.yaml.template → content.yaml (niche mới)
4. Step 1: rà soát / cập nhật PROJECT-OS (nếu đổi stack)
5. Step 2: rà soát AGENT-OS (giữ 4 agent trừ khi thêm stage)
6. Step 3: sửa skills + prompts theo niche
7. OPS Phase 1–2: Railway + Supabase SQL
8. OPS Phase 3–7: Telegram prompts → chạy pipeline
9. Go-live: gateway + cron + manual publish
10. Verify: scripts/verify_supabase.py
```

Chi tiết từng bước: [clone-checklist.md](clone-checklist.md)

---

## Map Step 1–2–3 → file trong repo

### Step 1 — Project OS (M0)

| Deliverable | File |
|-------------|------|
| Vision + constraints | `docs/PROJECT-OS.md` |
| Architecture | `docs/01-architecture.md` |
| Repo layout | `docs/02-repository-layout.md` |
| Phases | `docs/03-development-phases.md` |
| Milestones | `docs/05-milestones.md` |
| Env catalog | `.env.example` |
| Agent rules | `AGENTS.md` |

**Gate:** Stakeholder đọc PROJECT-OS + AGENTS.md trước khi deploy.

### Step 2 — Agent OS

| Deliverable | File |
|-------------|------|
| Agent contracts | `docs/AGENT-OS.md` |
| Kanban naming | `docs/08-kanban-conventions.md` |
| X algorithm | `docs/09-x-algorithm-rules.md` |
| Profiles | `profiles/*.yaml` |

**Gate:** 4 agent + bảng ownership Supabase không đổi trừ khi thêm bảng mới.

### Step 3 — Knowledge assets

| Loại | Thư mục |
|------|---------|
| Skills | `skills/*/SKILL.md` |
| SOP | `knowledge/sops/SOP-00` … `SOP-09` |
| Prompts Telegram | `knowledge/prompts/` |
| Checklists | `knowledge/checklists/` |
| Cursor prompts | `knowledge/implementation/cursor/` |

**Index:** [knowledge/ASSET-INDEX.md](../knowledge/ASSET-INDEX.md)

---

## OPS Runtime (sau Step 3)

| Phase | SOP | Runbook | Milestone |
|-------|-----|---------|-----------|
| 1 Railway + Kanban | SOP-01 | `runbooks/01`, `02` | M1–M2 |
| 2 Supabase | SOP-02 | `runbooks/03` | M3 |
| 3 Research | SOP-03 | prompts | M4 |
| 4 Script | SOP-04 | prompts | M5 |
| 5 X optimize | SOP-05 | `docs/09` | M6 |
| 6 Full pipeline | SOP-06 | `runbooks/07` | M7 |
| 7 Weekly cron | SOP-07 | `runbooks/08` | M8 |
| 8 Hardening | SOP-08 | `runbooks/09`, `10` | M9 |
| Publish | SOP-09 | `docs/12`, `ops/publish-log.md` | Go-live |

---

## File bắt buộc sửa khi clone niche mới

| File | Sửa gì |
|------|--------|
| `content.yaml` | audience, search_queries, script format, hashtags |
| `skills/research-agent/SKILL.md` | query themes, audience default |
| `skills/script-agent/SKILL.md` | output format |
| `knowledge/prompts/research-agent-config.md` | Telegram prompt |
| `knowledge/prompts/full-pipeline-run.md` | domain trong prompt |
| `knowledge/prompts/weekly-cron-setup.md` | timezone, schedule |
| `README.md` | mô tả project |
| `ops/publish-log.md` | reset log |

**Không sửa (thường):** `supabase/migrations/*`, `docs/AGENT-OS.md` workflow, Kanban stage names.

---

## Bài học từ deploy thật (hermes_kaban_bot)

| Vấn đề | Cách xử lý |
|--------|------------|
| Bot Telegram im | `hermes gateway status` → `gateway install --system` |
| Key Railway nhưng agent không thấy | Ghi vào **`/data/.env`** trên volume |
| Schema qua bot chậm/treo | Apply SQL trong **Supabase SQL Editor** |
| `signals_applied` sai format | `python scripts/verify_supabase.py` + regenerate prompt |
| Đổi niche giữa chừng | `content.yaml` + [reconfigure-audience prompt](../knowledge/prompts/reconfigure-audience-forex-gold.md) |
| Đăng X | **Thủ công v1** — `scripts/export_x_post.py` |
| Secrets trong chat | Rotate key; chỉ `.env.example` trên git |

---

## Lệnh operator (mọi dự án clone)

```bash
# Local verify (cần .env)
python scripts/verify_supabase.py
python scripts/export_x_post.py

# Railway Console
hermes gateway status
grep -E 'TINYFISH|SUPABASE|DEEPSEEK|TELEGRAM' /data/.env
sudo hermes gateway install --system
```

---

## Clone repo mới — 3 lệnh Git

```bash
git clone https://github.com/hoangkyanh2805-ux/hermes_kaban_bot.git my-new-pipeline
cd my-new-pipeline
rm -rf .git && git init
# Điền PROJECT-BRIEF → content.yaml → commit → push repo mới
```

---

## Tài liệu liên quan

| Doc | Mục đích |
|-----|----------|
| [clone-checklist.md](clone-checklist.md) | Checklist từng bước clone |
| [templates/PROJECT-BRIEF.md](templates/PROJECT-BRIEF.md) | Brief dự án mới |
| [templates/content.yaml.template](templates/content.yaml.template) | Template domain config |
| [../knowledge/sops/SOP-OPS-BUNDLER.md](../knowledge/sops/SOP-OPS-BUNDLER.md) | SOP chính thức |
| [../docs/PROJECT-STATUS.md](../docs/PROJECT-STATUS.md) | Ví dụ trạng thái instance này |

---

## Acceptance — bundler hoàn chỉnh

- [ ] Brief mới điền xong
- [ ] `content.yaml` niche mới
- [ ] M3 Supabase 4 bảng
- [ ] M7 một full run `completed`
- [ ] M8 cron set + 1 run `trigger=cron`
- [ ] 1 post đăng X + `publish-log.md`
- [ ] Repo push GitHub không có `.env`
