# Cursor Prompt — Phase 3: Research Agent

## Context

Phase 3 · [SOP-03](../../sops/SOP-03-research-agent.md) · Skill: [skills/research-agent/SKILL.md](../../../skills/research-agent/SKILL.md)

## Your task

1. Verify/finalize `skills/research-agent/SKILL.md` against [docs/AGENT-OS.md §8](../../../docs/AGENT-OS.md)
2. `runbooks/04-research-agent.md` — operator steps + link to [research-agent-config prompt](../../prompts/research-agent-config.md)
3. Update `profiles/research-agent.yaml` with skills: content-pipeline-research, content-pipeline-kanban, use-tinyfish
4. `skills/INSTALL.md` — ensure TinyFish install steps are complete

## Do NOT

- Write a Python research module — Hermes + skill only
- Add prompts outside `knowledge/prompts/`

## Acceptance

[knowledge/checklists/agent-testing.md](../../checklists/agent-testing.md) § ResearchAgent
M4 in phase-gates

## Operator next step

Execute SOP-03 on live Hermes host after copying skills.
