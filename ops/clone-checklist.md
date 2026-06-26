# Clone Checklist — Hermes Kanban Pipeline (dự án mới)

Dùng sau khi fork [hermes_kaban_bot](https://github.com/hoangkyanh2805-ux/hermes_kaban_bot).

**Thời gian ước tính:** 1–2 ngày (docs) + 1 ngày (ops live) nếu đã quen Hermes.

---

## Phase 0 — Brief & rename

- [ ] Copy [templates/PROJECT-BRIEF.md](templates/PROJECT-BRIEF.md) → `ops/PROJECT-BRIEF-{slug}.md`
- [ ] **[CREDENTIALS-AND-KEYS.md](CREDENTIALS-AND-KEYS.md)** — đọc trước khi deploy
- [ ] Điền: tên project, niche, audience, nguồn research, timezone cron
- [ ] Copy [templates/content.yaml.template](templates/content.yaml.template) → `content.yaml`
- [ ] Cập nhật `README.md` (1 đoạn mô tả niche)
- [ ] Tạo repo GitHub mới (không push `.env`)

---

## Step 1 — Project OS (docs)

- [ ] Đọc `docs/PROJECT-OS.md` — sửa vision/audience nếu cần
- [ ] Xác nhận hard constraints: Hermes Kanban only, no custom queue
- [ ] `.env.example` — thêm biến mới nếu có integration khác
- [ ] `docs/PROJECT-STATUS.md` — reset cho instance mới
- [ ] Gate M0: [knowledge/checklists/phase-gates.md](../knowledge/checklists/phase-gates.md)

---

## Step 2 — Agent OS

- [ ] `docs/AGENT-OS.md` — giữ 4 agent trừ khi thêm stage (vd. LinkedIn)
- [ ] `profiles/*.yaml` — cập nhật `description` theo niche
- [ ] `docs/08-kanban-conventions.md` — card naming nếu đổi slug pattern
- [ ] Nếu thêm bảng Supabase → cập nhật AGENT-OS §7 + migration mới

---

## Step 3 — Knowledge assets

- [ ] `skills/research-agent/SKILL.md` — queries + audience
- [ ] `skills/script-agent/SKILL.md` — format script
- [ ] `skills/x-optimizer-agent/SKILL.md` — thread template
- [ ] `knowledge/prompts/research-agent-config.md`
- [ ] `knowledge/prompts/full-pipeline-run.md`
- [ ] `knowledge/prompts/weekly-cron-setup.md`
- [ ] (Tuỳ chọn) `knowledge/prompts/reconfigure-audience-*.md` cho pivot sau này
- [ ] Cập nhật [knowledge/ASSET-INDEX.md](../knowledge/ASSET-INDEX.md) nếu thêm file

---

## OPS Phase 1 — Railway + Telegram (M1–M2)

- [ ] Deploy [Railway Hermes template](https://railway.com/deploy/hermes-agent)
- [ ] Volume `/data` mounted
- [ ] Variables: `DEEPSEEK_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, `PORT`
- [ ] Web UI: Telegram connected
- [ ] `hermes kanban init` (nếu cần)
- [ ] Tạo 4 profiles: research, script, x-optimizer, storage
- [ ] Prompt Kanban team: [knowledge/prompts/kanban-team-setup.md](../knowledge/prompts/kanban-team-setup.md)
- [ ] Test `ping` Telegram

**Runbook:** [runbooks/01-railway-deploy.md](../runbooks/01-railway-deploy.md), [02](../runbooks/02-kanban-team.md)

---

## OPS Phase 2 — Supabase (M3)

- [ ] Tạo Supabase project mới (hoặc schema riêng)
- [ ] SQL Editor: `supabase/migrations/001_content_pipeline.sql`
- [ ] SQL Editor: `supabase/policies/rls_agent_ownership.sql`
- [ ] Railway: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
- [ ] Ghi keys vào `/data/.env` trên volume
- [ ] Verify 4 bảng + RLS

**Runbook:** [runbooks/03-supabase-schema.md](../runbooks/03-supabase-schema.md)

---

## OPS Phase 3–5 — Agents (M4–M6)

- [ ] `TINYFISH_API_KEY` → Railway + `/data/.env`
- [ ] Cài TinyFish + Supabase skills (Telegram hoặc CLI)
- [ ] Chạy research → ≥5 topics
- [ ] Chạy script → `full_script` + `structure`
- [ ] Chạy x-optimizer → Phoenix `signals_applied`
- [ ] `python scripts/verify_supabase.py`

---

## OPS Phase 6–7 — Full pipeline + cron (M7–M8)

- [ ] Full pipeline prompt: [full-pipeline-run.md](../knowledge/prompts/full-pipeline-run.md)
- [ ] `pipeline_runs.status = completed`
- [ ] `/sethome` Telegram
- [ ] Gateway: `sudo hermes gateway install --system`
- [ ] Cron test 5 phút → OK
- [ ] Cron production: thứ 2 07:00 (timezone trong brief)
- [ ] 1 run `trigger=cron` trên Supabase

**Runbook:** [runbooks/08-weekly-cron.md](../runbooks/08-weekly-cron.md), [09](../runbooks/09-gateway-hardening.md)

---

## Go-live (M9 partial)

- [ ] `python scripts/export_x_post.py` → đăng X thủ công
- [ ] Ghi [publish-log.md](publish-log.md)
- [ ] 2 tuần cron liên tiếp OK
- [ ] Không secrets trong git (`git ls-files | grep env`)

**Runbook:** [runbooks/10-go-live.md](../runbooks/10-go-live.md)  
**Policy:** [docs/12-manual-x-publish.md](../docs/12-manual-x-publish.md)

---

## Customization matrix (dự án khác niche)

| Thay đổi | File chính | Giữ nguyên |
|----------|------------|------------|
| Audience / queries | `content.yaml`, research skill | Kanban stages |
| Script format | script skill | 4-table schema |
| Output channel khác X | x-optimizer skill, bảng mới | Hermes dispatcher |
| Thêm agent thứ 5 | AGENT-OS, profiles, migration | Railway pattern |
| Cron khác T2 | prompts, content.yaml | verify scripts |

---

## Sign-off

| Role | Date | OK |
|------|------|-----|
| Operator | | |
| Docs (Step 1–3) | | |
| Live M7 | | |
| Live M8 | | |
