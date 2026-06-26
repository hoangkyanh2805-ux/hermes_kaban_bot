# Runbook 02 — Tạo đội 4 Agent trên Kanban

**Phase 1** · Milestone M2 · ~30 phút

Sau khi M1 xong. Tạo profiles + 4 thẻ Kanban.

---

## Checklist

- [ ] 4 profile Hermes đã tạo
- [ ] Fragment YAML áp dụng (xem `profiles/`)
- [ ] 4 thẻ Kanban trong **To Do**
- [ ] Assignee đúng tên profile
- [ ] Smoke test: worker spawn được

---

## Bước 1 — Tạo profiles

Trên host Hermes (Railway shell hoặc VPS):

```bash
hermes profile create research-agent \
  --description "TinyFish research → Supabase topics"

hermes profile create script-agent \
  --description "Video scripts từ topics"

hermes profile create x-optimizer-agent \
  --description "Tối ưu post X theo algorithm"

hermes profile create storage-agent \
  --description "Đối soát pipeline_runs"
```

Cấu hình model (ví dụ DeepSeek):

```bash
for p in research-agent script-agent x-optimizer-agent storage-agent; do
  hermes -p "$p" config set model.default deepseek/deepseek-chat
done
```

### Orchestrator (profile default)

Bật toolset `kanban` cho profile default — dùng seed pipeline sau này:

```bash
# Qua Web UI: Tools → bật kanban cho default profile
# Hoặc xem fragment: profiles/default-orchestrator.yaml
```

Chạy script hỗ trợ (in hướng dẫn merge):

```bash
./scripts/install_profiles.sh
```

---

## Bước 2 — Tạo 4 thẻ Kanban qua Telegram

Gửi prompt từ [knowledge/prompts/kanban-team-setup.md](../knowledge/prompts/kanban-team-setup.md) tới bot Hermes.

**Tóm tắt nội dung prompt:**

- 4 task: Research, Script, X Optimizer, Storage
- Assignee: `research-agent`, `script-agent`, `x-optimizer-agent`, `storage-agent`
- Trạng thái: **todo**

---

## Bước 3 — Xác nhận trên dashboard

| Thẻ | Assignee |
|-----|----------|
| Research agent | research-agent |
| Script agent | script-agent |
| X optimizer agent | x-optimizer-agent |
| Storage agent | storage-agent |

Tất cả trong cột **To Do**.

---

## Bước 4 — Smoke test dispatcher

Tạo thẻ test (Telegram hoặc CLI):

```bash
hermes kanban create "test:research-smoke" --assignee research-agent
```

Quan sát:

1. Thẻ chuyển **ready** → **in progress**
2. Worker spawn (logs gateway)
3. Hoàn thành hoặc comment trên thẻ
4. Telegram nhận thông báo `completed` (nếu tạo từ Telegram)

```bash
hermes kanban watch
```

---

## Xác nhận M2

| Tiêu chí | OK? |
|----------|-----|
| 4 profiles tồn tại | ☐ |
| 4 thẻ + assignee đúng | ☐ |
| Dispatcher spawn worker | ☐ |
| Telegram notifier hoạt động | ☐ |

---

## Tiếp theo (Phase 2)

→ [SOP-02 Supabase](../knowledge/sops/SOP-02-supabase-schema.md)  
→ Prompt: [supabase-schema-setup.md](../knowledge/prompts/supabase-schema-setup.md)

**Lưu ý:** Phase 1 chưa cần Supabase/TinyFish — chỉ cần Kanban + profiles sống.
