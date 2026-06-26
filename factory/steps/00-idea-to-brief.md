# Step 0 — Idea → Brief

**Trước Step 1** · Không dùng skill riêng — brainstorm + brief thủ công hoặc chat.

---

## Input

- Link video YouTube (primary reference)
- Case study, bài Facebook, repo GitHub liên quan
- Business goal sơ bộ
- Niche / audience (có thể đổi sau — vd. AI → forex/gold)

---

## Checklist brainstorm

- [ ] Xem **toàn bộ** video — ghi architecture, thứ tự build
- [ ] Liệt kê: Telegram, Hermes, Kanban, 4 agent, Supabase, cron
- [ ] Ghi **không làm gì**: custom queue, auto-post X v1, SaaS-only
- [ ] Chọn niche content (audience)
- [ ] Chọn deploy target: Railway / VPS
- [ ] Điền [ops/templates/PROJECT-BRIEF.md](../ops/templates/PROJECT-BRIEF.md)

---

## Primary reference (dự án mẫu)

**Video:** https://www.youtube.com/watch?v=2oKmF--xJAI

Extract từ video:

| Chủ đề | Ghi chú |
|--------|---------|
| System architecture | Telegram → Hermes → Kanban → 4 agents → Supabase |
| Development order | Railway → Kanban team → Supabase → TinyFish → agents → full run → cron |
| Agent roles | Research, Script, X Optimizer, Storage |
| Kanban | Card dependencies, dispatcher |
| Skills | TinyFish, Supabase agent |
| DB | topics, scripts, x_posts, pipeline_runs |
| Scheduler | Weekly Monday |
| Philosophy | Kanban is the bus |

---

## Supporting links

| Resource | URL |
|----------|-----|
| Supabase | https://supabase.plug.dev/ykdVN09 |
| Hermes GitHub | https://github.com/NousResearch/hermes-agent |
| Kanban docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban |
| Railway | https://railway.com/deploy/hermes-agent |
| TinyFish | https://tinyfish.ai |
| X Algorithm | https://github.com/xai-org/x-algorithm |
| Prompts ref | https://github.com/derekcheungsa/ai-automation-resources |

---

## Output Step 0

1. `ops/PROJECT-BRIEF-{slug}.md` (filled)
2. Quyết định: reproduce tutorial **hay** adapt niche (vd. forex/gold)
3. Sign-off → chuyển **Step 1**

---

## Next

→ [01-project-kickstart-os.md](01-project-kickstart-os.md)
