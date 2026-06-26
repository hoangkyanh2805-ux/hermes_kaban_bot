# SOP-08: Hardening & Reproducibility

**Phase 8** · Milestone M9

## Purpose

Make the pipeline deployable by a third party from documentation alone in under 2 hours.

## Prerequisites

- SOP-07 complete
- [checklists/go-live.md](../checklists/go-live.md)
- [checklists/pre-deploy-security.md](../checklists/pre-deploy-security.md)

## Procedure

1. Complete `deploy/railway/README.md` and `deploy/vps/README.md` (implementation phase).
2. Add schema tests in `tests/test_schema_sql.py`.
3. Run security checklist — no secrets in git.
4. Consolidate [docs/10-runbook.md](../../docs/10-runbook.md).
5. Hand runbook to fresh operator; time deploy.
6. Run 2 consecutive weekly (or manual) pipeline successes.

## Acceptance

- M9: external deploy < 2 hours
- 2 successful unattended or manual full runs
- All phase gates in checklists green

## References

- [knowledge/tasks/PHASE-TASKS.md](../tasks/PHASE-TASKS.md) Phase 8 tasks
- [implementation/cursor/PHASE-08-hardening.md](../implementation/cursor/PHASE-08-hardening.md)
