# SOP-01: Railway Deploy + Kanban Team

**Phase 1** · Video steps 1–2 · Milestones M1–M2

## Purpose

Deploy Hermes on Railway, verify Kanban, connect Telegram, create four agent profiles and Kanban cards.

## Prerequisites

- Phase 0 signed off
- DeepSeek (or other) API key
- Telegram bot token from @BotFather
- [knowledge/prompts/kanban-team-setup.md](../prompts/kanban-team-setup.md)

## Procedure

### 1. Deploy Hermes (≈2 min)

1. Open [Railway Hermes template](https://railway.com/deploy/hermes-agent).
2. Set `DEEPSEEK_API_KEY` (or provider key).
3. Mount volume at `/data`.
4. Wait for service healthy.

### 2. Configure gateway

1. Open Railway public URL → config UI (basic auth from deploy logs).
2. Add Telegram channel with bot token.
3. Set allowed user IDs (recommended).
4. Verify `hermes gateway` running (auto on Railway).

### 3. Initialize Kanban

1. Open Hermes dashboard → **Kanban** tab (left sidebar).
2. Run `hermes kanban init` if prompted.
3. Confirm board visible.

### 4. Create four profiles

Create Hermes profiles per `profiles/` (Phase 1 implementation):

- `research-agent`
- `script-agent`
- `x-optimizer-agent`
- `storage-agent`

Enable `kanban` toolset on default/cron profile for seeding.

### 5. Create Kanban team

Send Telegram message using [kanban-team-setup prompt](../prompts/kanban-team-setup.md).

Verify four cards in **To Do** with correct assignees.

### 6. Smoke test

1. Create test card assigned to `research-agent`.
2. Watch dispatcher claim and complete (or manual verify spawn).
3. Confirm Telegram completion notification.

## Outputs

- [ ] Gateway 24h stable
- [ ] Kanban tab operational
- [ ] Four profiles + four cards
- [ ] Dispatcher spawns worker

## Failure handling

| Issue | Action |
|-------|--------|
| No Kanban tab | Upgrade Hermes ≥ v2026.5.7 |
| Telegram silent | Check allowlist; originate create from Telegram |
| Worker not spawning | Confirm gateway running |

## References

- [SOP-02](SOP-02-supabase-schema.md) next
- [checklists/phase-gates.md](../checklists/phase-gates.md) M1–M2
