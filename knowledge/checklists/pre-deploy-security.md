# Pre-Deploy Security Checklist

## Repository

- [ ] `.env` in `.gitignore`
- [ ] No API keys in git history
- [ ] `.env.example` has placeholders only
- [ ] SECURITY.md reviewed

## Supabase

- [ ] RLS enabled on all 4 tables
- [ ] Service role key not in client-side code
- [ ] Anon key not used by agents

## Hermes

- [ ] Telegram user allowlist set
- [ ] Minimal toolsets per profile
- [ ] Storage agent only profile with pipeline_runs write

## Railway / VPS

- [ ] ADMIN_PASSWORD rotated from default
- [ ] Volume encryption at rest (provider default)
- [ ] No secrets in deploy logs

## Agents

- [ ] No auto-post to X (v1)
- [ ] No DELETE permissions on Supabase
- [ ] TinyFish key only on research profile

## Pre-open-source scan (if applicable)

- [ ] Rotate all keys used during development
- [ ] Scan for `SUPABASE_SERVICE_ROLE`, `TINYFISH`, `DEEPSEEK` in files
