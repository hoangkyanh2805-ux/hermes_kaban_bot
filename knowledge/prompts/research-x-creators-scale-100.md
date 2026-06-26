# Prompt: Cào tiếp X creators → 100 unique (Supabase)

**Round 2+** · `research-agent` · bảng `x_creators`

Batch đầu: `88274469-fe50-44a7-a95e-3b2c85e02271` (~50 creators). Mục tiêu: **≥100 handle unique** toàn DB (dedupe theo `handle`).

---

## Bước 0 — Đếm hiện tại (Supabase SQL)

```sql
SELECT count(DISTINCT handle) AS unique_creators FROM x_creators;
SELECT country, count(DISTINCT handle) AS n FROM x_creators GROUP BY country ORDER BY n DESC;
```

Ghi `unique_creators` — cần thêm `100 - unique_creators` người.

---

## Prompt Telegram (copy-paste)

```text
Research — CREATOR DISCOVERY ROUND 2 — lưu Supabase x_creators.

Mục tiêu: tổng UNIQUE handle trong bảng x_creators ≥ 100.
Hiện có ~50 — cần thêm ~50+ account MỚI.

KHÔNG insert topics.

Bước 1 — Dedupe:
- SELECT DISTINCT handle, country FROM x_creators
- Không INSERT handle đã tồn tại (bất kỳ batch nào)

Bước 2 — Batch mới:
- research_batch_id = UUID mới
- niche = forex-gold-signals

Bước 3 — TinyFish (≥3 query / quốc gia, query KHÁC round 1):

Canada:
- "XAUUSD analyst Canada twitter list site:x.com"
- "gold futures trader Toronto site:x.com"
- "forex signals Canada min_faves site:x.com"

Italy:
- "trader oro XAUUSD Italia site:x.com"
- "forex italiano influencer site:x.com"
- "analisi tecnica oro site:x.com"

Germany:
- "Goldhandel XAUUSD Deutschland site:x.com"
- "Forex Signale Deutschland twitter site:x.com"
- "DAX gold trader site:x.com"

United Arab Emirates:
- "Dubai gold trader forex site:x.com"
- "XAUUSD signals UAE site:x.com"
- "middle east forex influencer site:x.com"

France:
- "trader or XAUUSD France site:x.com"
- "signaux forex or France site:x.com"
- "analyse technique or site:x.com"

Saudi Arabia:
- "gold forex trader Riyadh site:x.com"
- "تداول ذهب فوركس site:x.com"
- "XAUUSD Saudi trader site:x.com"

United Kingdom:
- "London gold trader XAUUSD site:x.com"
- "UK forex signals twitter site:x.com"
- "FTSE gold macro trader site:x.com"

Poland:
- "forex złoto XAUUSD Polska site:x.com"
- "trader forex Polska twitter site:x.com"
- "sygnały forex gold site:x.com"

Bước 4 — Mỗi account mới:
country, handle (no @), display_name, followers_estimate, bio_snippet,
profile_url (https://x.com/... thật), why_relevant, source_urls,
research_batch_id, niche

Bước 5 — INSERT x_creators. Skip handle trùng DB.

Bước 6 — Báo cáo:
- research_batch_id mới
- inserted_this_run, total_unique_handles (SELECT count DISTINCT handle)
- count/country (toàn bảng)
- Nếu total_unique < 100: nói còn thiếu bao nhiêu, đề xuất query round 3

Chỉ URL/handle thật từ TinyFish. Không bịa.
```

---

## Round 3 (nếu vẫn < 100)

Gửi lại với query mở rộng:

```text
Round 3 — đạt 100 unique handles. Đọc handles hiện có, skip trùng.

Thêm query:
- "forex gold XAUUSD trader" + từng thành phố: Toronto, Vancouver, Milan, Frankfurt, Paris, London, Warsaw, Dubai, Riyadh
- "site:x.com" "gold analysis" "forex signals" lang:en|de|fr|it|pl|ar
- "best forex twitter accounts 2025 2026" + country name

Ưu tiên account có bio nhắc: XAUUSD, gold, signals, technical analysis, macro.
INSERT x_creators, báo total_unique_handles.
```

---

## Verify

```sql
SELECT count(DISTINCT handle) AS unique_creators FROM x_creators;

SELECT country, count(DISTINCT handle) AS n
FROM x_creators
GROUP BY country
ORDER BY n DESC;

SELECT handle, country, profile_url
FROM x_creators
ORDER BY created_at DESC
LIMIT 20;
```

Kỳ vọng: `unique_creators >= 100`.

---

## Sau khi đủ 100

→ [x-creators-icp-analysis.md](x-creators-icp-analysis.md)
