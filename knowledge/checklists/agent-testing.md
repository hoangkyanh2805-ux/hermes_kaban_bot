# Agent Testing Checklist

Per [docs/AGENT-OS.md](../../docs/AGENT-OS.md). Run after each agent is configured.

---

## ResearchAgent

- [ ] Card assigned to `research-agent`
- [ ] kanban_show() as first action
- [ ] TinyFish returns real URLs
- [ ] ≥5 topics inserted
- [ ] trending_score 1–100
- [ ] Result line: `top: ... score=... topics=...`
- [ ] Retry: kill worker → reclaim, no duplicate topics
- [ ] Skill: [skills/research-agent/SKILL.md](../../skills/research-agent/SKILL.md)

---

## ScriptAgent

- [ ] Blocked until research `done`
- [ ] Selects highest trending_score
- [ ] Sections: cold open, 7 steps, payoff, friction, outro
- [ ] scripts.status = draft
- [ ] Word count ≥ 1200
- [ ] Result line: `script: {slug} words={n}`

---

## XOptimizerAgent

- [ ] Blocked until script `done`
- [ ] main_post has zero URLs
- [ ] Link in thread index 1
- [ ] signals_applied has all required keys
- [ ] virality_score 1–100
- [ ] suggested_post_time in allowed window

---

## StorageAgent

- [ ] Blocked until ALL x-optimize siblings `done`
- [ ] Counts match Supabase
- [ ] pipeline_runs.status set correctly
- [ ] No content edits to topics/scripts/x_posts
- [ ] Root card audit comment posted
- [ ] Result: `run: completed packages=2/2`

---

## Full chain integration

- [ ] TODO → RESEARCH → SCRIPT → OPTIMIZE → STORAGE → DONE
- [ ] Telegram notifications on each complete
- [ ] 2-topic tutorial benchmark met
- [ ] pipeline_runs.completed_at set

---

## Dependency violation test

- [ ] Manually verify script card stays `todo` while research `in_progress`
- [ ] Storage stays `todo` until last x-optimize `done`
