# Step 4 — OPS Runtime (sau Factory Step 1–3)

**Không phải skill** — operator + Cursor implementation theo `knowledge/implementation/cursor/`.

Factory Step 1–3 = **docs only**. Step 4 = **chạy thật** trên Railway + Supabase.

---

## Master guide

→ **[ops/OPS-BUNDLER.md](../../ops/OPS-BUNDLER.md)**  
→ **[ops/clone-checklist.md](../../ops/clone-checklist.md)**

---

## Phase map

| Phase | Việc | Runbook | Milestone |
|-------|------|---------|-----------|
| 1 | Railway + Telegram + Kanban + profiles | `runbooks/01`, `02` | M1–M2 |
| 2 | Supabase SQL + RLS | `runbooks/03` | M3 |
| 3 | TinyFish + research-agent | prompts, Telegram | M4 |
| 4 | script-agent | prompts | M5 |
| 5 | x-optimizer-agent | `docs/09` | M6 |
| 6 | Full pipeline | `runbooks/07` | M7 |
| 7 | Weekly cron | `runbooks/08` | M8 |
| 8 | Gateway + go-live | `runbooks/09`, `10` | M9 partial |

---

## Implementation trong repo (Cursor)

| Phase | Cursor prompt file |
|-------|-------------------|
| 2 Supabase | `knowledge/implementation/cursor/PHASE-02-supabase.md` |
| 1 Infra | `PHASE-01-infra.md` |
| 3–8 | `PHASE-03` … `PHASE-08` |

Code đã tạo trong instance mẫu:

- `supabase/migrations/001_content_pipeline.sql`
- `scripts/verify_supabase.py`, `export_x_post.py`
- `content.yaml` (niche)
- `tests/test_*.py`

---

## Bài học deploy (bắt buộc đọc)

| Issue | Fix |
|-------|-----|
| Bot im | `hermes gateway status` → `install --system` |
| Key không vào agent | `/data/.env` on volume |
| Schema | Supabase SQL Editor, không bot |
| Phoenix fail | `verify_supabase.py` + regenerate |
| Đăng X | Manual v1 — `export_x_post.py` |

---

## Domain config (đổi niche)

1. `content.yaml` (hoặc template → fill)
2. `knowledge/prompts/reconfigure-audience-*.md`
3. Skills research/script

**Ví dụ instance này:** `forex-gold-signals`

---

## Verify go-live

```bash
python scripts/verify_supabase.py
python scripts/export_x_post.py
```

- [ ] `pipeline_runs.trigger=cron` (sau thứ 2)
- [ ] `ops/publish-log.md` có URL tweet

---

## Step 5 — Clone dự án mới

→ [ops/OPS-BUNDLER.md](../../ops/OPS-BUNDLER.md)

Fork repo → brief mới → `clone-checklist.md`

---

## Quay lại factory

Niche mới từ đầu (không fork): lặp Step 0 → 1 → 2 → 3 → 4.

Niche mới từ template: Step 0 brief + sửa `content.yaml` + Step 4 only.
