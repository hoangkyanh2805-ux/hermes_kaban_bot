"""Lint profile YAML fragments — Phase 1 gate."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
PROFILES_DIR = REPO_ROOT / "profiles"

REQUIRED_PROFILES = [
    "research-agent.yaml",
    "script-agent.yaml",
    "x-optimizer-agent.yaml",
    "storage-agent.yaml",
    "default-orchestrator.yaml",
]

REQUIRED_KEYS = {"profile", "description", "toolsets"}


class TestProfileYaml(unittest.TestCase):
    def test_all_profile_files_exist(self) -> None:
        for name in REQUIRED_PROFILES:
            path = PROFILES_DIR / name
            self.assertTrue(path.is_file(), f"Missing profile fragment: {path}")

    def test_profile_yaml_parses(self) -> None:
        for name in REQUIRED_PROFILES:
            path = PROFILES_DIR / name
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict, f"{name} must be a YAML mapping")
            missing = REQUIRED_KEYS - set(data.keys())
            self.assertFalse(missing, f"{name} missing keys: {missing}")

    def test_profile_names_match_filenames(self) -> None:
        for name in REQUIRED_PROFILES:
            path = PROFILES_DIR / name
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            expected_stem = name.replace(".yaml", "")
            if expected_stem == "default-orchestrator":
                self.assertEqual(data["profile"], "default")
            else:
                self.assertEqual(data["profile"], expected_stem)

    def test_worker_assignee_names(self) -> None:
        workers = {
            "research-agent.yaml": "research-agent",
            "script-agent.yaml": "script-agent",
            "x-optimizer-agent.yaml": "x-optimizer-agent",
            "storage-agent.yaml": "storage-agent",
        }
        for filename, assignee in workers.items():
            data = yaml.safe_load((PROFILES_DIR / filename).read_text(encoding="utf-8"))
            self.assertEqual(data.get("kanban", {}).get("assignee_name"), assignee)


if __name__ == "__main__":
    unittest.main()
