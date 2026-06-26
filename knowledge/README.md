# Knowledge Assets

Reusable AI assets distilled from [PROJECT-OS.md](../docs/PROJECT-OS.md) and [AGENT-OS.md](../docs/AGENT-OS.md). Implementation-ready documentation only — no application code.

## Quick navigation

| Asset type | Location |
|------------|----------|
| **Master index** | [ASSET-INDEX.md](ASSET-INDEX.md) |
| **Folder map** | [FOLDER-STRUCTURE.md](FOLDER-STRUCTURE.md) |
| **Hermes skills** | [../skills/](../skills/) |
| **SOPs** | [sops/](sops/) |
| **Prompt templates** | [prompts/](prompts/) |
| **Checklists** | [checklists/](checklists/) |
| **Development tasks** | [tasks/](tasks/) |
| **Cursor prompts** | [implementation/cursor/](implementation/cursor/) |
| **Claude Code prompts** | [implementation/claude-code/](implementation/claude-code/) |

## How to use

1. **Operators** — Follow SOPs in phase order (`sops/SOP-01` → `SOP-08`).
2. **Implementers** — Pick phase tasks from `tasks/`, run matching Cursor or Claude Code prompt.
3. **Hermes runtime** — Install skills from `skills/` into `~/.hermes/skills/` per `skills/INSTALL.md`.
4. **Prompts** — Copy templates from `prompts/` into Telegram when configuring agents (adapt placeholders).

## Source lineage

| Step | Artifact | This layer |
|------|----------|------------|
| 1 | Project OS | SOPs, folder structure, phase tasks |
| 2 | Agent OS | Skills, checklists, prompt templates |
| 3 | Knowledge factory | This `knowledge/` tree |
