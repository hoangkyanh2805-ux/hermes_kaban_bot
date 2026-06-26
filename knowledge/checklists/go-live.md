# Go-Live Checklist

Before production weekly cron.

## Infrastructure

- [ ] Hermes gateway stable 72+ hours
- [ ] Railway volume backed up (or VPS disk snapshot)
- [ ] Telegram allowlist configured
- [ ] Public Railway endpoint removed (optional security)

## Secrets

- [ ] All keys in env only — not in repo
- [ ] `.env.example` documents all vars
- [ ] Service role key scoped via RLS

## Pipeline

- [ ] M7 full pipeline passed twice manually
- [ ] M8 cron dry-run passed (`*/5` test)
- [ ] Monday 07:00 cron active in correct TZ
- [ ] Overlap skip policy verified

## Skills

- [ ] All 6 project skills installed
- [ ] Vendor skills: Supabase + TinyFish
- [ ] Profile bindings verified

## Monitoring

- [ ] Operator knows how to check `hermes kanban list`
- [ ] Supabase SQL queries for run health documented
- [ ] Blocked card escalation path defined

## Sign-off

- [ ] Operator name: _______________
- [ ] Date: _______________
