# Railway Volume — Ghi chú kỹ thuật

## Tại sao cần volume

Hermes lưu trạng thái runtime trên disk:

- `kanban.db` — task graph, comments, events
- `config.yaml` — providers, Telegram, cron
- `skills/` — skill đã cài
- `state.db` — lịch sử session

**Không mount volume** → mỗi lần redeploy Railway tạo container mới → mất Kanban và cấu hình.

## Cấu hình Railway

1. Service → **Volumes** → Add Volume
2. Mount path: `/data`
3. Hermes Railway template map `~/.hermes` → `/data`

## Backup (khuyến nghị)

| Tần suất | Hành động |
|----------|-----------|
| Hàng tuần | Snapshot volume Railway hoặc copy `/data/kanban/` |
| Content | Supabase là nguồn sự thật cho artifacts — backup riêng ở Phase 2 |

## Dung lượng ước tính

| Thành phần | Kích thước |
|------------|------------|
| kanban.db | < 50 MB (hàng nghìn task) |
| state.db | Tăng theo session — prune định kỳ |
| skills/ | < 5 MB |

Free tier Railway volume thường đủ cho pipeline này.
