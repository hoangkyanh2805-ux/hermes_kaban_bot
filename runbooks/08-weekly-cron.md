# Runbook 08 — Weekly cron (thứ Hai 07:00)

**Phase 7–8** · Milestone M8

Pipeline chạy tự động mỗi tuần — không cần gõ Telegram.

---

## Checklist M8

- [ ] `/sethome` đã gửi trong chat Telegram với bot
- [ ] Gateway running ổn định (xem [09-gateway-hardening.md](09-gateway-hardening.md))
- [ ] Cron test 1 lần (chạy sau 5 phút) thành công
- [ ] Cron production `0 7 * * 1` Asia/Ho_Chi_Minh
- [ ] `pipeline_runs.trigger = cron` trên run thứ Hai

---

## Bước 1 — Set home channel

Telegram → chat với @hermes_kaban_bot:

```text
/sethome
```

Bot xác nhận — cron và `kanban_complete` notify về chat này.

---

## Bước 2 — Test cron (5 phút)

```text
Tạo cronjob test chạy sau 5 phút.

Khi chạy:
1. Seed pipeline_runs trigger=manual title weekly-run:TEST
2. Research 5 topics forex/gold/XAUUSD (audience forex-gold-signals)
3. Produce top 2 packages (script + x_post)
4. Lưu Supabase, báo Telegram khi storage xong

Nếu có pipeline_runs status=running từ tuần trước → skip.
```

Đợi notify → verify:

```bash
python scripts/verify_supabase.py --relaxed-phoenix
```

---

## Bước 3 — Production cron

```text
Set weekly cron: thứ Hai 07:00 Asia/Ho_Chi_Minh (0 7 * * 1).

Mỗi tuần:
- Title Kanban root: weekly-run:{YYYY-Www}
- Research 5 topics, produce top 2
- Full pipeline → Supabase
- Notify Telegram start + complete

Overlap: skip nếu run trước vẫn running.
```

Prompt đầy đủ: [knowledge/prompts/weekly-cron-setup.md](../knowledge/prompts/weekly-cron-setup.md)

---

## Bước 4 — Verify thứ Hai sau

Supabase SQL:

```sql
SELECT id, trigger, status, topics_researched, packages_produced, created_at
FROM pipeline_runs
WHERE trigger = 'cron'
ORDER BY created_at DESC
LIMIT 3;
```

Local:

```bash
python scripts/verify_supabase.py --min-topics 5 --min-scripts 2 --min-x-posts 2
```

---

## Xử lý sự cố

| Triệu chứng | Cách xử lý |
|-------------|------------|
| Cron không chạy | `hermes gateway status` — gateway phải running |
| Không notify | `/sethome` lại |
| Run trùng | Bật overlap skip trong prompt |
| Data trống | Check `/data/.env` có đủ keys |

---

## Tiếp theo

→ [09-gateway-hardening.md](09-gateway-hardening.md) · Milestone M9 reproducible deploy
