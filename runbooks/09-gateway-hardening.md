# Runbook 09 — Gateway auto-start (Railway)

**Phase 5 hardening** · Tránh bot Telegram im sau redeploy

---

## Vấn đề

`nohup hermes gateway run --replace` **mất** khi Railway restart/redeploy container.

Triệu chứng: `hermes gateway status` → **not running**, Telegram không trả lời.

---

## Fix lâu dài — Railway Console

Sau mỗi deploy ổn định, chạy **một lần**:

```bash
sudo hermes gateway install --system
hermes gateway status
```

Hoặc qua **Hermes Web UI** → **Start Gateway** → cấu hình auto-start nếu có.

---

## Fix tạm — mỗi lần redeploy

```bash
nohup hermes gateway run --replace > /tmp/gateway.log 2>&1 &
sleep 3
hermes gateway status
tail -20 /tmp/gateway.log
```

---

## Đảm bảo env trên volume

Hermes đọc `/data/.env` — không chỉ Railway Variables:

```bash
grep -E 'TINYFISH|SUPABASE|DEEPSEEK|TELEGRAM' /data/.env
```

Thiếu key → append (xem [03-supabase-schema.md](03-supabase-schema.md)).

---

## Checklist sau redeploy

- [ ] `hermes gateway status` → running
- [ ] Telegram `ping` → Pong
- [ ] `hermes kanban list` → có task
- [ ] Volume `/data` mounted (Railway → Volumes)

---

## Volume warning (Railway sidebar)

Nếu volume có icon cảnh báo → kiểm tra mount path `/data` còn gắn service `hermes-agent`.

Xem: [deploy/railway/volume-notes.md](../deploy/railway/volume-notes.md)
