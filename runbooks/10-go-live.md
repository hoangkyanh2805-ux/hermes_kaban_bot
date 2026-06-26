# Runbook 10 — Go-live: đăng thử → gateway → cron

**Sau M7** · 3 bước cuối để pipeline vận hành thật

Thứ tự: **đăng 1 post (thủ công)** → **gateway auto-start** → **weekly cron**

> **v1 scope lock:** Pipeline tự động đến Supabase `x_posts`. Đăng X = operator thủ công.  
> Ghi nhận chính thức: [docs/12-manual-x-publish.md](../docs/12-manual-x-publish.md) · Log: [ops/publish-log.md](../ops/publish-log.md)

---

## Bước A — Đăng thử 1 post trên X

### A1. Export post từ Supabase (Cursor terminal)

Post Phoenix-compliant (virality cao nhất pass gates):

```bash
python scripts/export_x_post.py
```

Hoặc chỉ định id (vd. `542c`):

```bash
python scripts/export_x_post.py --id 542c
```

Copy output → notepad.

### A2. Đăng trên X (thủ công — v1 không auto-post)

| Bước | Hành động |
|------|-----------|
| 1 | Paste **ROOT POST** → Post |
| 2 | Reply tweet đó → paste **REPLY 1** (có link nguồn) |
| 3 | Tiếp reply → **REPLY 2** (góc nhìn) |
| 4 | Reply → **REPLY 3** (CTA) |

**Thời điểm:** `suggested_post_time` hoặc 07:00–09:00 / 18:00–20:00 giờ VN.

### A3. 15 phút đầu (Phoenix)

- [ ] Trả lời mọi comment (author reply = 150× signal)
- [ ] Mục tiêu ≥5 replies trong 15 phút đầu
- [ ] Không edit root post để thêm link

### A4. Ghi nhận đã đăng

Điền URL tweet vào [ops/publish-log.md](../ops/publish-log.md) sau khi post live.

---

## Bước B — Gateway auto-start (Railway)

**Một lần** trên Railway Console:

```bash
grep -E 'TINYFISH|SUPABASE|DEEPSEEK|TELEGRAM' /data/.env

sudo hermes gateway install --system
sleep 2
hermes gateway status
```

Kỳ vọng: `Gateway is running`

**Test Telegram:**

```text
ping
```

→ `Pong!`

Chi tiết: [09-gateway-hardening.md](09-gateway-hardening.md)

---

## Bước C — Weekly cron

### C1. Set home channel

Telegram:

```text
/sethome
```

### C2. Cron test (5 phút)

```text
Tạo cronjob test chạy sau 5 phút.

Pipeline giống production:
- Research 5 topics **forex/gold/XAUUSD** (audience `forex-gold-signals`)
- Top 2 scripts + x_posts Phoenix-compliant
- Lưu Supabase, notify Telegram khi xong
- Skip nếu pipeline_runs đang running
```

Đợi notify → verify:

```bash
python scripts/verify_supabase.py --min-topics 5 --min-scripts 2 --min-x-posts 2 --relaxed-phoenix
```

### C3. Production — thứ Hai 07:00 VN

```text
Set weekly cron: thứ Hai 07:00 Asia/Ho_Chi_Minh (cron 0 7 * * 1).

Mỗi tuần:
- Kanban root title weekly-run:{YYYY-Www}
- Research 5, produce top 2
- x_posts phải pass Phoenix (main_post no URL, link thread[1], signals_applied đầy đủ)
- Notify Telegram start + complete
- Skip nếu run trước vẫn running
```

### C4. Verify thứ Hai sau

```sql
SELECT trigger, status, topics_researched, packages_produced, created_at
FROM pipeline_runs WHERE trigger = 'cron'
ORDER BY created_at DESC LIMIT 1;
```

---

## Checklist go-live

- [ ] A — 1 post đăng thử trên X
- [ ] B — `hermes gateway install --system` + ping OK
- [ ] C1 — `/sethome`
- [ ] C2 — cron test 5 phút OK
- [ ] C3 — cron thứ Hai 07:00 set
- [ ] `python scripts/verify_supabase.py` — ≥2 x_posts Phoenix pass

---

## Milestone

| Mục | Gate |
|-----|------|
| M7 | Full pipeline + 2 Phoenix posts ✅ |
| M8 | Cron Monday unattended |
| M9 | 2 consecutive successful runs + docs |

---

## Tiếp theo

- Đăng post thứ 2 từ `export_x_post.py --id 9ecc`
- Dọn 8 x_posts draft cũ (tuỳ chọn)
- Milestone M9: [docs/05-milestones.md](../docs/05-milestones.md)
