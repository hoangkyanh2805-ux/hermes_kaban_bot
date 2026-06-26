# Prompt: ICP từ x_creators (≥100 creators)

**Sau khi** `SELECT count(DISTINCT handle) FROM x_creators` ≥ 100.

Gửi qua **Telegram** (research-agent hoặc default profile có Supabase read).

---

## Prompt Telegram (copy-paste)

```text
ICP ANALYSIS — đọc Supabase x_creators (toàn bộ rows, dedupe handle).

KHÔNG insert topics. Không cào thêm creator trừ khi cần bổ sung followers_estimate.

Bước 1 — Load data:
SELECT DISTINCT ON (handle)
  handle, country, display_name, followers_estimate, bio_snippet,
  profile_url, why_relevant, niche, research_batch_id
FROM x_creators
ORDER BY handle, created_at DESC;

Bước 2 — Phân tích ICP cho niche forex-gold-signals (XAUUSD / gold trading signals):

A) SEGMENTATION (bảng markdown):
| Segment | Tiêu chí | % ước lượng | Ví dụ 3 handles |
(vd: Macro gold traders, Technical signal providers, Retail edu creators, Broker-affiliated, Arabic gold community, EU session traders...)

B) GEO ICP:
| Country | Count | Tier ưu tiên (1-3) | Lý do |
8 nước: Canada, Italy, Germany, UAE, France, Saudi Arabia, UK, Poland

C) FOLLOWER TIERS:
| Tier | Range | Count | Outreach fit (follow/collab/DM) |

D) BIO KEYWORDS (top 15 từ khoá trong bio_snippet + why_relevant):
frequency count + ý nghĩa cho content

E) IDEAL CUSTOMER PROFILE — 2-3 personas:
Mỗi persona:
- Tên persona (vd. "London Session Gold Scalper")
- Demographics (country, language, follower band)
- Pain points (3 bullet)
- Content họ consume (format, hook style)
- CTA hiệu quả (signal, levels, macro catalyst)
- 5 handles đại diện (profile_url)

F) ANTI-ICP — ai KHÔNG nên target (3-5 loại)

G) OUTREACH PRIORITY LIST — top 20 handles:
| Rank | handle | country | segment | score 1-100 | lý do | suggested_action |
score = relevance to forex-gold-signals + estimated reach + content fit

H) CONTENT IMPLICATIONS cho pipeline:
- 5 hook themes nên đăng X
- 3 hashtag clusters theo geo
- Best posting window gợi ý theo segment (session timezone)

Bước 3 — Lưu kết quả:
- Trả full report Telegram (markdown)
- INSERT 1 row vào pipeline_runs (trigger=manual, status=completed, kanban_root_task_id='icp-analysis-{date}') NẾU cần audit trail
- (Tuỳ chọn) Ghi file tóm tắt vào Kanban comment nếu có card

Bước 4 — Summary line:
ICP: personas={n} top20={handles} segments={list} unique_creators={count}
```

---

## Verify thủ công

- Report có ≥2 personas, top 20 handles có URL thật từ DB
- Segments khớp dữ liệu thật (không invent handle ngoài x_creators)
- Anti-ICP hợp lý (spam bots, crypto-only, no gold mention...)

---

## SQL hỗ trợ trước khi ICP

```sql
-- Unique count
SELECT count(DISTINCT handle) FROM x_creators;

-- Top countries
SELECT country, count(DISTINCT handle) n FROM x_creators GROUP BY 1 ORDER BY 2 DESC;

-- Missing followers (enrich trước ICP nếu >50% null)
SELECT count(*) FILTER (WHERE followers_estimate IS NULL) AS missing,
       count(*) AS total
FROM (SELECT DISTINCT ON (handle) * FROM x_creators ORDER BY handle, created_at DESC) t;
```

Nếu >50% thiếu `followers_estimate`, chạy prompt enrich trước:

```text
Enrich x_creators: với mỗi handle có followers_estimate IS NULL,
TinyFish search "site:x.com/{handle}" hoặc profile snippet → UPDATE followers_estimate + bio_snippet nếu có.
Không tạo row mới. Báo số row updated.
```

---

## Output lưu repo (thủ công)

Copy report từ Telegram → `ops/icp-forex-gold-signals.md` (tùy chọn, cho team).
