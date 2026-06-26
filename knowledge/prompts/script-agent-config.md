# Prompt: Script Agent Configuration

**Phase 4** · SOP-04

---

Configure the **script-agent** profile using the content-pipeline-script skill.

**Task:** Pick the top virality-potential topic from Supabase `topics` for pipeline_run_id `{PIPELINE_RUN_ID}` (highest trending_score).

**Write:** A full video script with:
- Cold open
- Seven numbered steps
- Payoff
- Friction (honest caveats)
- Outro with CTA

**Save to:** Supabase `scripts` table as status `draft` with `structure` JSONB mapping sections.

**Kanban:** Complete the script card when finished. Result: `script: {topic_slug} words={n}`

Do not start until the research Kanban card is done.

Run the script agent now.

---

## Verify

- [ ] Script for highest-scored topic
- [ ] full_script populated
- [ ] Script card `done` only after research `done`
