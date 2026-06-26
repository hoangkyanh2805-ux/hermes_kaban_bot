# Skill Installation Guide

Install project and vendor skills into Hermes (`/data/skills/` on Railway or `~/.hermes/skills/` on VPS).

---

## 1. Vendor skills (do first)

### Supabase agent skill

In Telegram (or `hermes chat`):

```text
Install the Supabase agent skill from the official source.
My project URL is: {SUPABASE_URL}
My service role key is: {SUPABASE_SERVICE_ROLE_KEY}
```

Confirm Hermes reports connection success.

### TinyFish skill

```text
Install the TinyFish skill from the tinyfish cookbook (use-tinyfish).
My TinyFish API key is: {TINYFISH_API_KEY}
```

---

## 2. Project skills (copy from repo)

```bash
# From repo root on the Hermes host
SKILLS_SRC="./skills"
HERMES_SKILLS="/data/skills"   # or ~/.hermes/skills

for skill in research-agent script-agent x-optimizer-agent storage-agent pipeline-seeder content-pipeline-kanban; do
  mkdir -p "$HERMES_SKILLS/$skill"
  cp "$SKILLS_SRC/$skill/SKILL.md" "$HERMES_SKILLS/$skill/"
done
```

Or ask Hermes:

```text
Copy the content pipeline skills from {REPO_PATH}/skills/ into my skills directory.
Bind research-agent profile to content-pipeline-research and use-tinyfish.
```

---

## 3. Profile binding

Each profile must reference its skills in `config.yaml` or profile YAML. See `profiles/` (Phase 1+).

| Profile | Skills |
|---------|--------|
| research-agent | content-pipeline-research, content-pipeline-kanban, use-tinyfish |
| script-agent | content-pipeline-script, content-pipeline-kanban |
| x-optimizer-agent | content-pipeline-x-optimizer, content-pipeline-kanban |
| storage-agent | content-pipeline-storage, content-pipeline-kanban |
| default (cron) | pipeline-seeder, content-pipeline-kanban |

---

## 4. Verify

- [ ] `hermes` lists skills without error
- [ ] Research profile sees TinyFish tools
- [ ] Script profile can query Supabase
- [ ] Kanban tools enabled on seeder profile

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Skill not loaded | Restart gateway after copy |
| Supabase RLS deny | Apply policies from `supabase/policies/` |
| TinyFish 401 | Rotate API key in env |
