# Runbook 03 — Supabase Schema (Phase 2)

**Phase 2** · Milestone M3 · ~45 phút

Sau M2 (Kanban + profiles). Tạo 4 bảng Postgres + RLS trên Supabase, rồi gắn key vào Railway.

---

## Checklist M3

- [ ] Supabase project đã tạo
- [ ] Migration `001_content_pipeline.sql` chạy thành công
- [ ] RLS `rls_agent_ownership.sql` chạy thành công
- [ ] 4 bảng: `pipeline_runs`, `topics`, `scripts`, `x_posts`
- [ ] `x_posts.signals_applied` kiểu JSONB NOT NULL
- [ ] `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` trên Railway
- [ ] (Tuỳ chọn) Supabase skill cài trên Hermes

---

## Bước 1 — Tạo project Supabase

1. Mở [supabase.plug.dev/ykdVN09](https://supabase.plug.dev/ykdVN09) hoặc [supabase.com/dashboard](https://supabase.com/dashboard).
2. **New project** → chọn region gần Railway (vd. `us-east-1`).
3. Đặt mật khẩu DB → lưu an toàn (không commit).
4. Chờ project **Active**.

---

## Bước 2 — Apply migration SQL (khuyến nghị)

Trong Supabase Dashboard:

1. **SQL Editor** → **New query**.
2. Mở file repo: `supabase/migrations/001_content_pipeline.sql`
3. Copy toàn bộ → **Run**.
4. Mở file: `supabase/policies/rls_agent_ownership.sql`
5. Copy toàn bộ → **Run**.

Nếu lỗi "already exists" khi chạy lại — bảng đã có; chỉ cần verify Bước 3.

Chi tiết: [supabase/README.md](../supabase/README.md)

---

## Bước 3 — Verify

**Table Editor** → phải thấy 4 bảng.

Hoặc SQL Editor:

```sql
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN ('pipeline_runs', 'topics', 'scripts', 'x_posts');
```

Kiểm tra `signals_applied`:

```sql
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'x_posts' AND column_name = 'signals_applied';
-- Kỳ vọng: jsonb, NO
```

Kiểm tra RLS bật:

```sql
SELECT tablename, rowsecurity FROM pg_tables
WHERE schemaname = 'public'
  AND tablename IN ('pipeline_runs', 'topics', 'scripts', 'x_posts');
-- rowsecurity = true cả 4 bảng
```

---

## Bước 4 — Lấy credentials

**Project Settings** → **API**:

| Biến Railway | Lấy từ |
|--------------|--------|
| `SUPABASE_URL` | Project URL |
| `SUPABASE_SERVICE_ROLE_KEY` | `service_role` (secret) |

**Không** dùng `anon` key cho agent writes.

Trên Railway → service `hermes-agent` → **Variables** → thêm 2 biến trên → **Redeploy** (hoặc restart gateway).

---

## Bước 5 — Cài Supabase skill trên Hermes (tuỳ chọn)

Có 2 cách kết nối DB với agent:

| Cách | Khi nào dùng |
|------|----------------|
| **SQL từ repo** (Bước 2) | Khuyến nghị — reproducible, đã làm xong |
| **Bot Telegram** | Chỉ khi muốn Hermes tự tạo bảng bằng skill |

Nếu dùng skill, gửi Telegram (thay URL/key thật):

```text
Cài Supabase agent skill. Project URL: {SUPABASE_URL}
Service role key: {SUPABASE_SERVICE_ROLE_KEY}
Xác nhận kết nối OK.
```

Prompt đầy đủ: [knowledge/prompts/supabase-schema-setup.md](../knowledge/prompts/supabase-schema-setup.md)

Vì schema đã apply từ SQL, skill chỉ cần **test SELECT** — không cần nhờ bot tạo lại bảng.

---

## Bước 6 — Smoke test trên Supabase

SQL Editor (không cần bot):

```sql
WITH run AS (
  INSERT INTO pipeline_runs (trigger, status, kanban_root_task_id)
  VALUES ('manual', 'running', 'smoke-' || gen_random_uuid()::text)
  RETURNING id
),
topic AS (
  INSERT INTO topics (pipeline_run_id, title, trending_score, audience, source_urls)
  SELECT id, 'Smoke test topic', 75, 'non-technical', '[]'::jsonb FROM run
  RETURNING id, pipeline_run_id
)
SELECT topic.id AS topic_id, topic.pipeline_run_id FROM topic;
```

Xóa dữ liệu test sau nếu muốn:

```sql
DELETE FROM pipeline_runs WHERE kanban_root_task_id LIKE 'smoke-%';
```

---

## RLS — hiểu đúng với Hermes

- Agent trên Railway dùng **service role** → Supabase **bỏ qua RLS** (mặc định).
- File `rls_agent_ownership.sql` vẫn cần cho audit, dashboard, và khi sau này dùng JWT scoped per agent.
- Quyền ghi thực tế vẫn do **agent contract** trong [docs/AGENT-OS.md](../docs/AGENT-OS.md) §7 kiểm soát.

---

## Lỗi thường gặp

| Triệu chứng | Cách xử lý |
|-------------|------------|
| `relation already exists` | Bảng đã tạo — chuyển sang verify |
| RLS chặn insert từ dashboard | Dùng service role hoặc tắt RLS tạm (không khuyến nghị prod) |
| Agent không ghi được | Kiểm tra `SUPABASE_URL` / key trên Railway; redeploy |
| Skill không connect | Dùng **service_role**, không phải anon |

---

## Sau Phase 2

→ [SOP-03 Research Agent](../knowledge/sops/SOP-03-research-agent.md) · [runbooks/04-research-agent.md](04-research-agent.md) (Phase 3)

**Prompt Telegram tiếp theo (Phase 3):** cài TinyFish skill + cấu hình `research-agent`.
