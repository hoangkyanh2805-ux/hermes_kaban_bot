# Handoff — Làm tiếp trên máy khác

**Cập nhật:** 2026-06-26 · Đọc file này trước khi mở laptop mới.

---

## Chat / Telegram có tự lưu vào repo không?

**Không.** Tin nhắn Telegram, chat Cursor, và dữ liệu Supabase **không** tự sync vào Git.

| Nguồn | Lưu ở đâu | Cách đưa vào repo |
|-------|-----------|-------------------|
| Telegram ↔ Hermes bot | Railway volume `/data`, Supabase | Ghi tay vào file dưới đây |
| Cursor chat | Chỉ trên máy Cursor | Export / copy vào `ops/HANDOFF.md` |
| Supabase `topics`, `x_creators`, … | Supabase cloud | Query SQL; không commit DB vào git |
| Code, prompts, migration | GitHub repo | `git pull` trên laptop |

**File “tình hình” chính:**

| File | Mục đích |
|------|----------|
| **`ops/HANDOFF.md`** (file này) | Snapshot vận hành, ID, việc tiếp theo |
| **`docs/PROJECT-STATUS.md`** | Milestone M0–M9, % hoàn thành |
| **`ops/publish-log.md`** | URL tweet đã đăng X thủ công |
| **`ops/CREDENTIALS-AND-KEYS.md`** | Cách lấy API key (không chứa secret) |

---

## Infrastructure (đang live)

| Hạng mục | Giá trị |
|----------|---------|
| GitHub | https://github.com/hoangkyanh2805-ux/hermes_kaban_bot |
| Branch | `main` · commit gần nhất: `f49e63b` (x_creators + prompts) |
| Railway project | `trustworthy-emotion` |
| Railway service | `hermes-agent` (Online, volume `/data`) |
| Supabase project | `hermes-growth` (dashboard Supabase) |
| Telegram bot | `@hermes_kaban_bot` |
| Telegram user ID | `672890533` |
| Niche | `forex-gold-signals` |

**Lưu ý Railway:** Chưa bật Public URL → không có Web UI Kanban. Dùng **Telegram** + **Railway Console** (`hermes kanban list`).

---

## Supabase — bảng & dữ liệu

| Bảng | Trạng thái |
|------|------------|
| `pipeline_runs`, `topics`, `scripts`, `x_posts` | ✅ Có data pipeline weekly |
| `x_creators` | ✅ Migration 002 + RLS đã apply |

### Creator discovery (đã chạy)

| Mục | Giá trị |
|-----|---------|
| Batch 1 | `88274469-fe50-44a7-a95e-3b2c85e02271` (~50 creators) |
| Round 2 | Batch UUID mới (xem Supabase) |
| **Tổng unique handles** | **108** (mục tiêu ≥100 ✅) |
| 8 quốc gia | Canada, Italy, Germany, UAE, France, Saudi Arabia, UK, Poland |

Verify trên laptop (cần `.env` hoặc Supabase SQL Editor):

```sql
SELECT count(DISTINCT handle) FROM x_creators;
SELECT country, count(DISTINCT handle) n FROM x_creators GROUP BY 1 ORDER BY 2 DESC;
```

---

## Hermes / Railway — đã làm

- [x] Skill `research-agent` sync từ GitHub → `/data/.hermes/skills/research-agent/SKILL.md`
- [x] Mode 2 Creator Discovery → INSERT `x_creators`
- [x] `/data/.env` có `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `TINYFISH_API_KEY`
- [ ] ICP analysis report → **chưa lưu repo** (chạy prompt `knowledge/prompts/x-creators-icp-analysis.md`)
- [ ] Kanban board `content-os` → **trống task** (pipeline chạy qua Telegram one-off, không seed 4 thẻ)

### Lệnh Console hữu ích

```bash
hermes gateway status          # phải running
hermes gateway start           # nếu not running
hermes kanban boards list
hermes kanban list             # KHÔNG dùng "watch" (lỗi invalid choice)
grep x_creators /data/.hermes/skills/research-agent/SKILL.md
```

---

## Việc tiếp theo (laptop)

1. **Clone / pull repo**
   ```bash
   git clone https://github.com/hoangkyanh2805-ux/hermes_kaban_bot.git
   cd hermes_kaban_bot
   ```
2. **Copy `.env` local** (không có trên git) — lấy từ máy cũ hoặc Railway Variables + Supabase dashboard.
3. **ICP** — Telegram gửi prompt trong `knowledge/prompts/x-creators-icp-analysis.md` → paste report vào `ops/icp-forex-gold-signals.md` → commit.
4. **Round 3 creators** (tuỳ chọn) — `knowledge/prompts/research-x-creators-scale-100.md`
5. **Go-live X** — `docs/12-manual-x-publish.md` + `ops/publish-log.md`
6. **Cron M8** — 2 thứ Hai liên tiếp `pipeline_runs.trigger=cron`

---

## Prompt nhanh (Telegram)

**ICP:**
```
ICP ANALYSIS — đọc toàn bộ x_creators (dedupe handle). Report personas, top 20 outreach, geo tiers. KHÔNG insert topics.
```

**Cào thêm creator:**
```
Research ROUND 3 — skip handle đã có. Mục tiêu giữ ≥100 unique. INSERT x_creators only.
```

---

## Cập nhật file này khi nào?

Sau mỗi phiên làm việc lớn, sửa tay:

1. `ops/HANDOFF.md` — ID, số liệu, checkbox
2. `docs/PROJECT-STATUS.md` — milestone
3. `ops/publish-log.md` — sau khi đăng X
4. `ops/icp-forex-gold-signals.md` — sau ICP (tạo khi có report)

Rồi: `git add` → `git commit` → `git push`.
