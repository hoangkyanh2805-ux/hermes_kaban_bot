# PROJECT BRIEF — {PROJECT_NAME}

**Slug:** `{project-slug}`  
**Repo GitHub:** `{org}/{repo}`  
**Ngày:** YYYY-MM-DD  
**Operator:**

---

## 1. Vision (1 đoạn)

_Mô tả pipeline làm gì, cho ai, output cuối là gì._

**Ví dụ (hermes_kaban_bot):** Research XAUUSD/gold trending → trading-signal script → X thread Phoenix → Supabase → operator đăng X thủ công mỗi tuần.

---

## 2. Niche & audience

| Field | Giá trị |
|-------|---------|
| `audience.primary` | e.g. `forex-gold-signals` |
| `audience.label` | Mô tả ngắn |
| Ngôn ngữ content | vi / en / mixed |
| Exclude topics | |

---

## 3. Research (TinyFish)

| Field | Giá trị |
|-------|---------|
| Topics per run | 5 |
| Packages produced | 2 |
| Search queries (5+) | |
| Preferred sources | |
| API keys | `TINYFISH_API_KEY` |

---

## 4. Script format

| Field | Giá trị |
|-------|---------|
| Type | video / trading-signal / newsletter |
| Sections | e.g. catalyst, levels, trade plan |
| Voice/tone | |

---

## 5. X optimizer (Phoenix v1)

| Field | Giá trị |
|-------|---------|
| Thread structure | hook → link reply 1 → body → CTA |
| Auto-post | **No** (manual v1) |
| Algorithm doc | `docs/09-x-algorithm-rules.md` |

---

## 6. Infrastructure

| Service | URL / ID |
|---------|----------|
| Railway project | |
| Hermes public URL | |
| Supabase project | |
| Telegram bot | @ |
| Telegram user ID allowlist | |
| Cron | e.g. Mon 07:00 Asia/Ho_Chi_Minh |

---

## 7. Secrets (KHÔNG commit)

→ Chi tiết từng bước: [CREDENTIALS-AND-KEYS.md](../CREDENTIALS-AND-KEYS.md)

| Variable | Nơi set |
|----------|---------|
| `DEEPSEEK_API_KEY` | Railway + `/data/.env` |
| `TELEGRAM_BOT_TOKEN` | Railway |
| `SUPABASE_*` | Railway + `/data/.env` |
| `TINYFISH_API_KEY` | Railway + `/data/.env` |

---

## 8. Milestone target

- [ ] M3 Supabase
- [ ] M7 full pipeline
- [ ] M8 weekly cron
- [ ] First manual X post logged

---

## 9. Clone từ template

- [ ] Fork: `hoangkyanh2805-ux/hermes_kaban_bot`
- [ ] `content.yaml` filled from [content.yaml.template](content.yaml.template)
- [ ] [clone-checklist.md](../clone-checklist.md) in progress
