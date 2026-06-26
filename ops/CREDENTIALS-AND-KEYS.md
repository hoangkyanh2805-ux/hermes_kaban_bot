# Hướng dẫn API Keys & Credentials

**Operator guide** — lấy key từng dịch vụ, điền vào Railway + `/data/.env`.

Dùng cho mọi dự án clone từ [factory/](../factory/WORKFLOW.md).

**Không bao giờ** commit file `.env` hoặc paste key vào chat công khai.

---

## Tổng quan — key cần có

| Biến | Dịch vụ | Bắt buộc | Dùng cho |
|------|---------|----------|----------|
| `DEEPSEEK_API_KEY` | DeepSeek | ✅ | LLM Hermes agents |
| `TELEGRAM_BOT_TOKEN` | Telegram | ✅ | Bot gateway |
| `TELEGRAM_ALLOWED_USERS` | Telegram | Khuyến nghị | Chỉ bạn dùng bot |
| `SUPABASE_URL` | Supabase | ✅ | Database artifacts |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase | ✅ | Agent ghi DB |
| `TINYFISH_API_KEY` | TinyFish | ✅ (research) | Live web search |
| `ADMIN_USERNAME` | Railway/Hermes | Khuyến nghị | Web UI login |
| `ADMIN_PASSWORD` | Railway/Hermes | Khuyến nghị | Web UI login |
| `PORT` | Railway | Tự động | `8080` |

Template local: [.env.example](../.env.example)

---

## Nơi điền key (2 chỗ — quan trọng)

Hermes trên Railway đọc **cả hai**:

```text
1. Railway → service hermes-agent → Variables   (dashboard)
2. Volume /data/.env                             (shell Railway)
```

| Chỉ có Railway Variables | Chỉ có /data/.env |
|--------------------------|-------------------|
| Đôi khi gateway thấy | Agent runtime thấy |
| Sau redeploy OK | Persist trên volume |

**Khuyến nghị:** điền **cả hai** cùng giá trị.

### Ghi `/data/.env` (Railway Console)

```bash
cat >> /data/.env << 'EOF'
DEEPSEEK_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_USERS=123456789
TINYFISH_API_KEY=sk-tinyfish-...
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=sb_secret_...
EOF

grep -v '^#' /data/.env | grep .
```

Sau khi sửa → restart gateway:

```bash
nohup hermes gateway run --replace > /tmp/gateway.log 2>&1 &
```

---

## 1. DeepSeek API Key

**Dùng cho:** LLM chính (research, script, x-optimizer, storage).

### Lấy key

1. Mở https://platform.deepseek.com (hoặc https://api.deepseek.com)
2. Đăng ký / đăng nhập
3. **API Keys** → **Create API Key**
4. Copy key (dạng `sk-...`)

### Điền

| Nơi | Giá trị |
|-----|---------|
| Railway Variables | `DEEPSEEK_API_KEY` |
| `/data/.env` | `DEEPSEEK_API_KEY=sk-...` |

### Kiểm tra

- Hermes Web UI → LLM provider = DeepSeek
- Telegram `ping` → bot trả lời
- Log không có `401` / credit error

---

## 2. Telegram Bot

**Dùng cho:** Giao tiếp operator, cron notify, chạy pipeline.

### 2a. Tạo bot — BotFather

1. Mở Telegram → tìm **@BotFather**
2. Gửi `/newbot`
3. Đặt tên hiển thị + username (phải kết thúc `bot`, vd. `hermes_kaban_bot`)
4. Copy **HTTP API token** → `TELEGRAM_BOT_TOKEN`

### 2b. Lấy User ID (allowlist)

1. Gửi `/start` cho bot vừa tạo
2. Mở https://t.me/userinfobot → gửi bất kỳ tin → copy **Id** (số)
3. Hoặc dùng @getidsbot

### Điền

| Nơi | Giá trị |
|-----|---------|
| Railway | `TELEGRAM_BOT_TOKEN` |
| Railway | `TELEGRAM_ALLOWED_USERS=672890533` (id của bạn, có thể nhiều id cách nhau dấu phẩy) |
| `/data/.env` | cả hai dòng trên |

### Cấu hình Hermes

1. Railway public URL → đăng nhập admin
2. **Channels** → Telegram → dán token
3. Gửi `/start` cho bot
4. Nếu pairing: `hermes pairing approve telegram {CODE}` trên shell
5. Gửi `/sethome` trong chat để nhận cron notify

### Kiểm tra

```text
ping
```
→ `Pong!`

---

## 3. Supabase

**Dùng cho:** Lưu `topics`, `scripts`, `x_posts`, `pipeline_runs`.

### 3a. Tạo project

1. https://supabase.com/dashboard → **New project**
2. Organization → đặt tên project
3. **Database password** → lưu password manager (không commit)
4. **Region** → gần Railway (vd. Singapore / US East)
5. **Enable automatic RLS** → **TẮT** (repo có RLS riêng)
6. Chờ **Active**

### 3b. Apply schema (SQL)

1. **SQL Editor** → New query
2. Chạy lần lượt từ repo:
   - `supabase/migrations/001_content_pipeline.sql`
   - `supabase/policies/rls_agent_ownership.sql`
3. **Table Editor** → thấy 4 bảng

Chi tiết: [runbooks/03-supabase-schema.md](../runbooks/03-supabase-schema.md)

### 3c. Lấy URL + Secret key

**Settings** → **API** (hoặc **API Keys**):

| Lấy gì | Ở đâu | Biến Railway |
|--------|-------|--------------|
| Project URL | General hoặc API → `https://xxxxx.supabase.co` | `SUPABASE_URL` |
| Secret key | API Keys → **Secret** (`sb_secret_...`) | `SUPABASE_SERVICE_ROLE_KEY` |

**Không dùng** Publishable (`sb_publishable_...`) cho agent writes.

Tab **Legacy** → `service_role` chỉ khi Secret key mới không tương thích Hermes skill.

### Điền

```bash
# Railway Variables
SUPABASE_URL=https://jilbbbsnpxymhmyrpugq.supabase.co
SUPABASE_SERVICE_ROLE_KEY=sb_secret_...
```

+ cùng nội dung trong `/data/.env`

### Kiểm tra

SQL Editor:

```sql
SELECT COUNT(*) FROM pipeline_runs;
```

Local (file `.env`):

```bash
python scripts/verify_supabase.py --relaxed-phoenix
```

---

## 4. TinyFish API Key

**Dùng cho:** Research agent — search web trending topics.

### Lấy key

1. Mở https://agent.tinyfish.ai/api-keys (hoặc https://tinyfish.ai)
2. Đăng ký / đăng nhập
3. **Create API Key**
4. Copy key (dạng `sk-tinyfish-...`)

### Điền

| Nơi | Giá trị |
|-----|---------|
| Railway | `TINYFISH_API_KEY` |
| `/data/.env` | `TINYFISH_API_KEY=sk-tinyfish-...` |

### Kiểm tra

Telegram:

```text
Cài TinyFish skill. API key đã có trong env. Test search "XAUUSD gold forecast".
```

Supabase `topics` có rows mới sau research run.

---

## 5. Railway / Hermes Admin

### Deploy

1. https://railway.com/deploy/hermes-agent
2. **Volume** mount tại `/data` (bắt buộc)
3. **Variables** — thêm tất cả key trên
4. **Deploy** → đợi Online

Chi tiết: [runbooks/01-railway-deploy.md](../runbooks/01-railway-deploy.md)

### Admin Web UI

| Biến | Mặc định |
|------|----------|
| `ADMIN_USERNAME` | `admin` |
| `ADMIN_PASSWORD` | Xem deploy logs lần đầu nếu chưa set |
| `PORT` | `8080` |

### Gateway

```bash
hermes gateway status
sudo hermes gateway install --system   # auto-start sau redeploy
```

---

## 6. File `.env` local (Cursor / verify scripts)

Trên máy dev (không push git):

```bash
cp .env.example .env
# Điền key thật vào .env
```

Dùng cho:

```bash
python scripts/verify_supabase.py
python scripts/export_x_post.py
```

`.env` đã có trong `.gitignore`.

---

## Checklist credentials (in một lần)

- [ ] `DEEPSEEK_API_KEY` — Railway + `/data/.env`
- [ ] `TELEGRAM_BOT_TOKEN` — Railway + `/data/.env`
- [ ] `TELEGRAM_ALLOWED_USERS` — Railway + `/data/.env`
- [ ] `SUPABASE_URL` — Railway + `/data/.env`
- [ ] `SUPABASE_SERVICE_ROLE_KEY` — Railway + `/data/.env`
- [ ] `TINYFISH_API_KEY` — Railway + `/data/.env`
- [ ] Supabase 4 bảng đã tạo (SQL)
- [ ] Volume `/data` mounted
- [ ] Gateway running
- [ ] Telegram `ping` OK
- [ ] Không có key trong git (`git ls-files` không có `.env`)

---

## Bảo mật

| Quy tắc | Lý do |
|---------|-------|
| Không commit `.env` | Public repo |
| Rotate key nếu lộ trong chat | Hermes/Telegram logs |
| `TELEGRAM_ALLOWED_USERS` bắt buộc nếu bot public | Tránh người lạ dùng |
| Service role chỉ trên server | Full DB access |
| Không share DeepSeek key | Billing risk |

Sau rotate → cập nhật Railway **và** `/data/.env` → redeploy/restart gateway.

---

## Xử lý sự cố

| Triệu chứng | Nguyên nhân | Sửa |
|-------------|-------------|-----|
| Bot im | Gateway off | `hermes gateway run --replace` |
| `TINYFISH_API_KEY` missing | Chỉ có Railway var | Ghi `/data/.env` |
| Supabase empty | SQL chưa chạy | Run migration SQL |
| `401` DeepSeek | Key sai/hết credit | Tạo key mới |
| OpenRouter error | Phụ — bỏ `OPENROUTER_API_KEY` | Chỉ DeepSeek |
| RLS error | Schema/policy thiếu | Chạy `rls_agent_ownership.sql` |

---

## Liên quan

| Doc | Nội dung |
|-----|----------|
| [runbooks/03-supabase-schema.md](../runbooks/03-supabase-schema.md) | Supabase chi tiết |
| [runbooks/01-railway-deploy.md](../runbooks/01-railway-deploy.md) | Railway deploy |
| [factory/steps/04-ops-runtime.md](../factory/steps/04-ops-runtime.md) | OPS sau factory |
| [SECURITY.md](../SECURITY.md) | Policy repo |
