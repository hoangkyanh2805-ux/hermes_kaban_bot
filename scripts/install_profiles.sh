#!/usr/bin/env bash
# install_profiles.sh — Hướng dẫn áp dụng profile fragments lên Hermes
# Chạy trên máy host Hermes (Railway shell / VPS). Không commit secrets.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROFILES_SRC="${REPO_ROOT}/profiles"
HERMES_HOME="${HERMES_HOME:-/data}"

if [[ ! -d "$HERMES_HOME" && -d "$HOME/.hermes" ]]; then
  HERMES_HOME="$HOME/.hermes"
fi

echo "=== Hermes Content Pipeline — Cài profiles ==="
echo "Repo:      $REPO_ROOT"
echo "HERMES_HOME: $HERMES_HOME"
echo ""

PROFILES=(research-agent script-agent x-optimizer-agent storage-agent)

for name in "${PROFILES[@]}"; do
  if ! hermes profile list 2>/dev/null | grep -q "$name"; then
    echo "[TẠO] hermes profile create $name"
    hermes profile create "$name" --description "Content pipeline worker: $name" || true
  else
    echo "[OK] Profile đã tồn tại: $name"
  fi
done

echo ""
echo "=== Fragment YAML (tham chiếu — merge thủ công hoặc qua Web UI) ==="
for name in "${PROFILES[@]}"; do
  fragment="${PROFILES_SRC}/${name}.yaml"
  if [[ -f "$fragment" ]]; then
    echo "--- $fragment ---"
    head -n 20 "$fragment"
    echo "..."
    dest="${HERMES_HOME}/profiles/${name}/PROFILE.fragment.yaml"
    mkdir -p "$(dirname "$dest")" 2>/dev/null || true
    if [[ -w "$(dirname "$dest")" ]]; then
      cp "$fragment" "$dest"
      echo "Đã copy → $dest"
    fi
  fi
done

orch="${PROFILES_SRC}/default-orchestrator.yaml"
if [[ -f "$orch" ]]; then
  echo ""
  echo "=== Orchestrator (default profile) ==="
  echo "Bật toolset 'kanban' cho profile default — xem: $orch"
fi

echo ""
echo "=== Bước tiếp theo ==="
echo "1. hermes -p research-agent config set model.default deepseek/deepseek-chat"
echo "2. Web UI → default profile → bật toolset kanban"
echo "3. runbooks/02-kanban-team.md — tạo 4 thẻ Kanban"
echo "4. Phase 3: skills/INSTALL.md — copy skills"
