# Hermes Profiles — Content Pipeline

Fragment cấu hình cho 4 worker + 1 orchestrator. **Không phải** file runtime — merge vào Hermes qua `scripts/install_profiles.sh` hoặc Web UI.

## Danh sách profile

| File | Profile | Vai trò |
|------|---------|---------|
| `research-agent.yaml` | research-agent | RESEARCH — TinyFish (forex/gold/XAUUSD) |
| `script-agent.yaml` | script-agent | SCRIPT — trading-signal scripts |
| `x-optimizer-agent.yaml` | x-optimizer-agent | OPTIMIZE — X algorithm |
| `storage-agent.yaml` | storage-agent | STORAGE — pipeline_runs |
| `default-orchestrator.yaml` | default | Seed Kanban + cron |

## Tạo profile (CLI)

```bash
hermes profile create research-agent --description "Research trending topics via TinyFish"
hermes profile create script-agent --description "Write video scripts from Supabase topics"
hermes profile create x-optimizer-agent --description "Optimize X posts with algorithm signals"
hermes profile create storage-agent --description "Finalize pipeline runs in Supabase"
```

## Toolsets theo Hermes Kanban

| Profile | Toolsets bắt buộc |
|---------|-------------------|
| research-agent | `terminal`, `web` (+ kanban worker tools tự inject khi dispatch) |
| script-agent | `terminal` |
| x-optimizer-agent | `terminal` |
| storage-agent | `terminal` |
| default | `terminal`, **`kanban`** (seed task graph) |

Worker nhận `kanban_*` tools tự động qua `_KANBAN_TASK` — không cần bật `kanban` trên worker profile trừ khi profile cũng làm orchestrator.

## Skills (Phase 3+ gắn đầy đủ)

| Profile | Skills (sau khi cài) |
|---------|----------------------|
| research-agent | content-pipeline-research, content-pipeline-kanban, use-tinyfish |
| script-agent | content-pipeline-script, content-pipeline-kanban |
| x-optimizer-agent | content-pipeline-x-optimizer, content-pipeline-kanban |
| storage-agent | content-pipeline-storage, content-pipeline-kanban |
| default | pipeline-seeder, content-pipeline-kanban |

Phase 1: tạo profile + mô tả. Skills copy ở Phase 3.

## Model mặc định

Tutorial dùng **DeepSeek**. Đổi trong fragment hoặc:

```bash
hermes -p research-agent config set model.default deepseek/deepseek-chat
```

## Audience / niche

**Current:** `forex-gold-signals` — XAUUSD, gold macro, technical setups, trade plans.

Domain config: [content.yaml](../content.yaml) · Telegram reconfigure: [knowledge/prompts/reconfigure-audience-forex-gold.md](../knowledge/prompts/reconfigure-audience-forex-gold.md)

## Tham chiếu

- [docs/AGENT-OS.md](../docs/AGENT-OS.md)
- [skills/INSTALL.md](../skills/INSTALL.md)
