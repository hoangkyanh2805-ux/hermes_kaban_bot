# Runbook 07 — Review pipeline run + sửa x_posts

**Phase 6–7** · Milestone M7 · Sau lần chạy đầu

Bạn đã có data trong 4 bảng. Bước này: **verify chất lượng** và regenerate nếu cần.

---

## 1. Verify từ máy local (Cursor)

Trong repo (đã có `.env` với Supabase keys):

```bash
python scripts/verify_supabase.py
```

Chỉ đếm rows (bỏ qua Phoenix):

```bash
python scripts/verify_supabase.py --relaxed-phoenix
```

**Kỳ vọng M7:**

```text
[OK] pipeline_runs — count>=1
[OK] topics — count>=5
[OK] scripts — count>=2
[OK] x_posts — count>=2
[OK] x_posts_phoenix — N/N pass Phoenix gates
```

Nếu `x_posts_phoenix` **FAIL** → `signals_applied` chưa đúng spec → Bước 3.

---

## 2. Chọn package để đăng X

Supabase → **Table Editor** → `x_posts`:

1. Sort `virality_score` DESC
2. Mở `main_post` + `thread`
3. Chọn **2 package** tốt nhất (tutorial target)

Checklist thủ công:

- [ ] Root post không có URL
- [ ] Link ở reply đầu tiên trong thread
- [ ] `suggested_post_time` hợp lý (07–09h hoặc 18–20h VN)

---

## 3. Regenerate x_posts đúng Phoenix (Telegram)

Gửi bot nếu verify FAIL:

```text
Regenerate 2 x_posts có virality_score cao nhất.

Bắt buộc signals_applied JSONB:
{
  "reply_weight": 27,
  "author_reply_weight": 150,
  "no_root_external_link": true,
  "link_placement": "first_reply",
  "early_velocity_target_replies_15min": 5,
  "algorithm_version": "phoenix-2026"
}

main_post: không có https://
thread[1]: chứa link nguồn
Cập nhật row Supabase, không tạo topic mới.
```

Spec: [docs/09-x-algorithm-rules.md](../docs/09-x-algorithm-rules.md)

---

## 4. Full pipeline lần 2 (4 thẻ Kanban)

Lần test đầu dùng 1 task tổng. Lần sau dùng prompt đầy đủ:

[knowledge/prompts/full-pipeline-run.md](../knowledge/prompts/full-pipeline-run.md)

```text
Run full content pipeline qua Kanban:
- 5 topics research
- Top 2 scripts
- 2 x_posts Phoenix-compliant
- storage reconciliation
Dependencies: script blocked_by research, x-optimize blocked_by script, storage fan-in all x-optimize.
```

---

## 5. Sau M7

→ [08-weekly-cron.md](08-weekly-cron.md)
