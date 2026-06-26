# Publish log — manual X posts (v1)

Operator ghi nhận sau mỗi lần đăng thủ công. Pipeline **không** tự post.

Spec: [docs/12-manual-x-publish.md](../docs/12-manual-x-publish.md)

---

## Template (copy per post)

| Field | Value |
|-------|--------|
| Date (VN) | YYYY-MM-DD HH:mm |
| x_post id | uuid prefix |
| Topic / title | |
| Root URL on X | https://x.com/.../status/... |
| virality_score | |
| Notes | replies, timing, performance |

---

## Log

### 2026-06-26 — Gold breakout (READY — đăng ngay)

| Field | Value |
|-------|--------|
| x_post id | `cc072d31` |
| Topic | GOLD BREAKOUT ALERT — XAU/USD bullish flag weekly |
| Root URL on X | *(điền sau khi đăng)* |
| virality_score | 94 |
| pipeline | `trigger=cron` run mới nhất |
| Notes | `python scripts/export_x_post.py` · Phoenix pass · forex-gold-signals |

### 2026-06-26 — Post #2 (sau khi đăng #1)

| Field | Value |
|-------|--------|
| x_post id | *(mở Supabase x_posts, sort created_at DESC, row #2)* |
| Root URL on X | *(điền sau khi đăng)* |
| Notes | `export_x_post.py` lấy row virality thứ 2 |

### 2026-06-26 — Trial publish #1 (AI era — archive)

| Field | Value |
|-------|--------|
| x_post id | `542cfba7` |
| Topic | 10 Unmistakeable AI Trends (@acoustik) |
| Root URL on X | *(điền sau khi đăng)* |
| virality_score | 100 |
| Notes | v1 manual publish; export via `scripts/export_x_post.py --id 542c` |

### 2026-06-26 — Trial publish #2 (planned)

| Field | Value |
|-------|--------|
| x_post id | `9ecc74cd` |
| Topic | *(từ export `--id 9ecc`)* |
| Root URL on X | *(điền sau khi đăng)* |
| Notes | |

---

*Thêm dòng mới phía trên cho mỗi lần đăng.*
