# Prompt: X Optimizer Configuration

**Phase 5** · SOP-05

---

Configure the **x-optimizer-agent** profile using the content-pipeline-x-optimizer skill.

**Read:** Latest script draft from Supabase `scripts` for pipeline_run_id `{PIPELINE_RUN_ID}`.

**Rewrite as:** X post + thread optimized for engagement using open-source X algorithm signals:
- Replies worth 27× a like — engineer for replies
- Author reply to commenter: 150×
- **No external links in the root post** — put link in the **first reply** only
- Target 5+ replies in the first 15 minutes
- Suggested post time: 07:00–09:00 or 18:00–20:00

**Save to:** `x_posts` with main_post, thread (JSONB), virality_score (1–100), and signals_applied (JSONB documenting weights used).

**Kanban:** Complete when finished. Result: `x: {topic_slug} virality={n}`

Run the X optimizer agent now.

---

## Verify

- [ ] No URL in main_post
- [ ] Link in thread reply 1
- [ ] signals_applied JSONB complete
