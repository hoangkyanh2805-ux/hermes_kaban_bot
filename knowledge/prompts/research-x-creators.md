# Prompt: Research X Creators (lưu Supabase)

**One-off** · `research-agent` · bảng `x_creators`

Gửi nguyên khối dưới đây qua **Telegram** (hoặc gán Kanban card cho `research-agent`).

---

## Prompt (copy-paste)

```text
Research task — CREATOR DISCOVERY — lưu Supabase x_creators.

KHÔNG insert vào bảng topics. Chỉ dùng bảng x_creators.

Bước 1 — Chuẩn bị batch:
- Tạo research_batch_id = UUID mới (giữ nguyên cho mọi row trong task này).
- niche = forex-gold-signals

Bước 2 — TinyFish search (ít nhất 1 query / quốc gia):
Canada:
- "top forex twitter creators Canada site:x.com"
- "gold trading influencer Canada site:x.com"
Italy:
- "forex gold trader Italy site:x.com"
- "XAUUSD influencer Italy site:x.com"
Germany:
- "gold trading influencer Germany site:x.com"
- "forex trader Germany site:x.com"
United Arab Emirates:
- "forex gold trader Dubai UAE site:x.com"
France:
- "XAUUSD trader France site:x.com"
- "forex gold influencer France site:x.com"
Saudi Arabia:
- "gold forex trader Saudi Arabia site:x.com"
United Kingdom:
- "forex gold trader UK London site:x.com"
Poland:
- "forex gold trader Poland site:x.com"

Bước 3 — Với mỗi account hợp lệ (10–15 / quốc gia nếu có đủ kết quả thật):
- country (tên đầy đủ: Canada, Italy, Germany, United Arab Emirates, France, Saudi Arabia, United Kingdom, Poland)
- handle (không có @)
- display_name
- followers_estimate (số nguyên ước lượng từ snippet; null nếu không có)
- bio_snippet (≤200 ký tự)
- profile_url (https://x.com/{handle} — chỉ URL thật từ search)
- why_relevant (1 câu: forex/gold/XAUUSD)
- source_urls (JSON array các URL TinyFish đã dùng để tìm account này)
- research_batch_id, niche

Bước 4 — INSERT vào Supabase public.x_creators.
- Idempotent: nếu (research_batch_id, handle) đã tồn tại thì skip.
- Không bịa handle. Không URL giả.

Bước 5 — Báo cáo:
- research_batch_id
- Tổng rows inserted theo country
- 3 handle nổi bật nhất
- kanban_complete --result nếu có Kanban card, hoặc trả summary Telegram.

Verify: SELECT count(*), country FROM x_creators WHERE research_batch_id = '{batch}' GROUP BY country;
```

---

## Trước khi chạy (một lần)

1. Supabase SQL Editor → chạy `supabase/migrations/002_x_creators.sql`
2. Chạy `supabase/policies/rls_x_creators.sql`
3. Table Editor → thấy bảng `x_creators`
4. Hermes có Supabase skill + `SUPABASE_SERVICE_ROLE_KEY` trong `/data/.env`

---

## Verify sau khi chạy

**Supabase SQL Editor:**

```sql
SELECT country, count(*) AS n
FROM x_creators
WHERE research_batch_id = 'PASTE-BATCH-UUID-HERE'
GROUP BY country
ORDER BY country;
```

**Local (nếu có .env):**

```bash
python scripts/verify_supabase.py --creators --min-creators 10
```

---

## Placeholders

| Variable | Source |
|----------|--------|
| `research_batch_id` | Agent tạo UUID mới mỗi lần chạy prompt |
| `pipeline_run_id` | Tuỳ chọn — gắn vào weekly run nếu chạy trong pipeline |

---

## Lưu ý

- Task này **không** chặn script/x-optimize cards — chạy độc lập.
- Cùng `@handle` có thể xuất hiện ở batch khác; unique chỉ trong một `research_batch_id`.
- Nếu TinyFish trả ít kết quả cho một nước → ghi comment, không invent.
