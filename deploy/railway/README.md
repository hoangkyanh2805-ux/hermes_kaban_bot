# Triển khai Hermes trên Railway

Hướng dẫn deploy Phase 1 cho **Hermes Content Pipeline**.

**Tham chiếu:** [SOP-01](../../knowledge/sops/SOP-01-railway-kanban.md) · [runbooks/01-railway-deploy.md](../../runbooks/01-railway-deploy.md)

---

## Yêu cầu

| Hạng mục | Ghi chú |
|----------|---------|
| Tài khoản Railway | [railway.com](https://railway.com) |
| API key LLM | DeepSeek (tutorial) hoặc OpenRouter |
| Telegram bot | Tạo qua [@BotFather](https://t.me/BotFather) |
| Hermes version | ≥ v2026.5.7 (có Kanban) |

---

## Bước 1 — Deploy template

1. Mở [Railway Hermes template](https://railway.com/deploy/hermes-agent).
2. Chọn project → **Deploy**.
3. Thêm biến môi trường (Variables):

| Biến | Bắt buộc | Mô tả |
|------|----------|-------|
| `DEEPSEEK_API_KEY` | Có* | LLM chính (*hoặc provider khác) |
| `PORT` | Tự động | Mặc định `8080` |
| `ADMIN_USERNAME` | Khuyến nghị | Basic auth UI cấu hình |
| `ADMIN_PASSWORD` | Khuyến nghị | Xem deploy logs nếu chưa set |
| `SUPABASE_URL` | Phase 2 | Project URL từ Supabase → Settings → General |
| `SUPABASE_SERVICE_ROLE_KEY` | Phase 2 | Secret key (`sb_secret_...`) — **không** dùng publishable |

4. **Volume:** mount persistent volume tại `/data`.
   - Kanban DB, config, skills, memory nằm trên volume này.
   - Không có volume = mất state khi redeploy.

5. Đợi build xong (~2 phút). Service status **Healthy**.

---

## Bước 2 — Cấu hình qua Web UI

1. Mở URL public của service (từ Railway dashboard).
2. Đăng nhập basic auth (`ADMIN_USERNAME` / `ADMIN_PASSWORD`).
3. **LLM provider:** xác nhận DeepSeek (hoặc provider đã chọn) hoạt động.
4. **Telegram:**
   - Dán `TELEGRAM_BOT_TOKEN`.
   - Thêm **allowed user IDs** (khuyến nghị — tránh bot công khai).
5. Lưu cấu hình. Gateway khởi động tự động khi có API key.

---

## Bước 3 — Kiểm tra Kanban

1. Dashboard Hermes → tab **Kanban** (sidebar trái).
2. Nếu chưa có board, chạy (qua shell Railway hoặc CLI local trỏ vào volume):

```bash
hermes kanban init
```

3. (Tùy chọn) Tạo board riêng cho pipeline:

```bash
hermes kanban boards create content-os --name "Content Pipeline" --switch
```

4. Xác nhận tab Kanban hiển thị cột To Do / Ready / In Progress / Done.

---

## Bước 4 — Cài profiles

Trên máy có quyền truy cập volume `/data`, hoặc qua Railway shell:

```bash
# Tạo 4 profile worker + 1 profile orchestrator (default đã có kanban)
hermes profile create research-agent --description "TinyFish research, topics table"
hermes profile create script-agent --description "Video scripts from Supabase topics"
hermes profile create x-optimizer-agent --description "X algorithm post optimization"
hermes profile create storage-agent --description "Pipeline reconciliation and pipeline_runs"

# Áp dụng fragment từ repo (xem profiles/README.md)
./scripts/install_profiles.sh
```

Chi tiết từng profile: thư mục [`profiles/`](../../profiles/).

---

## Bước 5 — Bảo mật sau setup

Sau khi Telegram hoạt động:

1. **Tùy chọn:** Gỡ public endpoint trên Railway — Hermes chỉ cần Telegram.
2. Không commit API keys vào git.
3. Xoay `ADMIN_PASSWORD` nếu đã lộ trong logs.

---

## Đường dẫn dữ liệu (Railway)

| Path trên volume | Nội dung |
|------------------|----------|
| `/data/config.yaml` | Cấu hình Hermes |
| `/data/kanban/` hoặc `kanban.db` | Kanban SQLite |
| `/data/skills/` | Skills đã cài |
| `/data/state.db` | Session Hermes (≠ Supabase content) |

Xem thêm: [volume-notes.md](volume-notes.md)

---

## Xử lý sự cố

| Triệu chứng | Cách xử lý |
|-------------|------------|
| Không thấy tab Kanban | Nâng Hermes ≥ v2026.5.7 |
| Gateway không chạy | Kiểm tra API key trong Variables |
| Mất config sau redeploy | Gắn volume `/data` |
| Telegram không phản hồi | Kiểm tra token + allowlist user ID |

---

## Tiếp theo

→ [runbooks/02-kanban-team.md](../../runbooks/02-kanban-team.md) — tạo 4 thẻ Kanban và đội agent
