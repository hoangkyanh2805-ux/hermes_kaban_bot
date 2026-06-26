# SOP-00: Project Foundation

**Phase 0** · Milestone M0

## Purpose

Confirm architecture and agent OS are signed off before any Hermes deployment or schema work.

## Prerequisites

- [docs/PROJECT-OS.md](../../docs/PROJECT-OS.md) complete
- [docs/AGENT-OS.md](../../docs/AGENT-OS.md) complete
- [knowledge/ASSET-INDEX.md](../ASSET-INDEX.md) reviewed

## Procedure

1. Read PROJECT-OS vision and constraints (Hermes Kanban only, no custom engine).
2. Read AGENT-OS agent contracts and Kanban workflow.
3. Confirm four agents: Research, Script, X Optimizer, Storage.
4. Confirm Supabase four-table model: topics, scripts, x_posts, pipeline_runs.
5. Stakeholder sign-off on pipeline shape and weekly cron requirement.

## Outputs

- Approved Phase 0 gate in [checklists/phase-gates.md](../checklists/phase-gates.md)
- No implementation code in repo yet

## Escalation

Architecture change requests → update PROJECT-OS + AGENT-OS before Phase 1.
