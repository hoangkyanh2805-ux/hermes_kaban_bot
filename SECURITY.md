# Security

Trust surface for the Hermes Kanban Content Pipeline. Read before deploying.

---

## Assets

| Asset | Sensitivity | Location |
|-------|-------------|----------|
| `SUPABASE_SERVICE_ROLE_KEY` | Critical | Hermes gateway env only |
| `TINYFISH_API_KEY` | High | Research profile env |
| `DEEPSEEK_API_KEY` / LLM keys | High | Hermes config |
| `TELEGRAM_BOT_TOKEN` | High | Hermes gateway config |
| Kanban SQLite | Medium | `/data` volume — coordination only |
| Supabase content | Medium | Cloud Postgres — RLS protected |

---

## RLS model

Each agent profile writes only to tables it owns. Service role is scoped by RLS policies — not unrestricted admin.

See `supabase/policies/rls_agent_ownership.sql` (Phase 2).

---

## Pre-deploy checklist

- [ ] No secrets in git (`git log -p` scan)
- [ ] `.env` in `.gitignore`
- [ ] Telegram allowlist configured
- [ ] Railway public endpoint removed after setup (tutorial pattern)
- [ ] Supabase RLS enabled on all 4 tables

---

## Pre-publish checklist (if open-sourcing adapted copy)

- [ ] Rotate all API keys shown during development
- [ ] Remove `SUPABASE_SERVICE_ROLE_KEY` from any logs
- [ ] Scan for embedded URLs with tokens

---

## Threat model

Single-operator self-hosted deployment. Trusted local user. Not multi-tenant SaaS.

LLM agents can execute shell commands — limit toolsets per profile to minimum required.
