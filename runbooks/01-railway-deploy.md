# Runbook 01 — Deploy Railway + Khởi tạo Kanban

**Phase 1** · Milestone M1 · ~30–60 phút

Phiên bản ngắn của [SOP-01](../knowledge/sops/SOP-01-railway-kanban.md). Chi tiết deploy: [deploy/railway/README.md](../deploy/railway/README.md).

---

## Checklist nhanh

- [ ] Deploy [Railway Hermes template](https://railway.com/deploy/hermes-agent)
- [ ] Gắn volume `/data`
- [ ] Set `DEEPSEEK_API_KEY` (hoặc LLM khác)
- [ ] Cấu hình Telegram trong Web UI
- [ ] Thấy tab **Kanban** trên dashboard
- [ ] `hermes kanban init` (nếu cần)

---

## Các bước

### 1. Deploy

1. Vào link template → Deploy.
2. Variables → thêm API key LLM.
3. Volumes → mount `/data`.
4. Đợi Healthy.

### 2. Telegram

1. Mở URL service → đăng nhập admin.
2. Channels → Telegram → dán bot token.
3. Allowlist user ID của bạn.
4. Gửi `/start` cho bot — phải có phản hồi.

### 3. Kanban

1. Dashboard → **Kanban** (sidebar).
2. Nếu trống: shell Railway → `hermes kanban init`.
3. (Khuyến nghị) Tạo board `content-os`:

```bash
hermes kanban boards create content-os --name "Content Pipeline" --switch
```

### 4. Kiểm tra gateway

- Logs Railway: không lỗi gateway crash liên tục.
- Tab Kanban load được.

---

## Xác nhận M1

| Tiêu chí | OK? |
|----------|-----|
| Service healthy 24h | ☐ |
| Kanban tab hiển thị | ☐ |
| Telegram phản hồi | ☐ |
| Volume `/data` gắn | ☐ |

---

## Sự cố thường gặp

| Vấn đề | Giải pháp |
|--------|-----------|
| Không có tab Kanban | Hermes ≥ v2026.5.7 |
| Bot im lặng | Token sai / chưa allowlist |
| Mất cấu hình | Chưa mount volume |

---

## Tiếp theo

→ [02-kanban-team.md](02-kanban-team.md)
