# Cursor Prompt — Phase 8: Hardening

## Context

Phase 8 · [SOP-08](../../sops/SOP-08-hardening.md) · M9 reproducibility

## Your task

1. `deploy/vps/hermes-gateway.service` — systemd unit template
2. `deploy/vps/README.md` — VPS alternative to Railway
3. `deploy/vps/install.sh` — idempotent skill copy + config hints (no secrets)
4. `tests/test_profile_yaml.py` — validate all profiles/*.yaml parse and contain name + toolsets
5. Expand `tests/test_schema_sql.py` if needed
6. Finalize `docs/10-runbook.md` as single operator entry
7. Cross-link all runbooks from README.md

## Security

Run [pre-deploy-security checklist](../../checklists/pre-deploy-security.md) — document results template in runbook

## Acceptance

M9 · go-live checklist · external deploy path documented < 2h

## Do NOT

- Force-push or commit secrets
