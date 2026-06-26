"""Lint Supabase migration SQL — Phase 2 gate (no live DB required)."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MIGRATION = REPO_ROOT / "supabase" / "migrations" / "001_content_pipeline.sql"
RLS_POLICIES = REPO_ROOT / "supabase" / "policies" / "rls_agent_ownership.sql"
SCHEMAS_DIR = REPO_ROOT / "schemas"

REQUIRED_TABLES = ("pipeline_runs", "topics", "scripts", "x_posts")
REQUIRED_INDEXES = (
    "idx_topics_run_score",
    "idx_scripts_topic",
    "idx_x_posts_script",
    "idx_pipeline_runs_status",
)
REQUIRED_SCHEMA_FILES = (
    "pipeline_run.json",
    "topic.json",
    "script.json",
    "x_post.json",
)


class TestSchemaSql(unittest.TestCase):
    def test_migration_file_exists(self) -> None:
        self.assertTrue(MIGRATION.is_file(), f"Missing migration: {MIGRATION}")

    def test_rls_policies_file_exists(self) -> None:
        self.assertTrue(RLS_POLICIES.is_file(), f"Missing RLS policies: {RLS_POLICIES}")

    def test_migration_contains_required_tables(self) -> None:
        sql = MIGRATION.read_text(encoding="utf-8").lower()
        for table in REQUIRED_TABLES:
            self.assertIn(f"create table", sql)
            self.assertIn(f"public.{table}", sql, f"Missing table DDL: {table}")

    def test_migration_foreign_keys(self) -> None:
        sql = MIGRATION.read_text(encoding="utf-8").lower()
        self.assertIn("references public.pipeline_runs", sql)
        self.assertIn("references public.topics", sql)
        self.assertIn("references public.scripts", sql)

    def test_migration_unique_constraints(self) -> None:
        sql = MIGRATION.read_text(encoding="utf-8").lower()
        self.assertIn("topics_pipeline_run_title_unique", sql)
        self.assertIn("scripts_topic_id_unique", sql)
        self.assertIn("x_posts_script_id_unique", sql)
        self.assertIn("kanban_root_task_id text unique", sql)

    def test_migration_indexes(self) -> None:
        sql = MIGRATION.read_text(encoding="utf-8")
        for idx in REQUIRED_INDEXES:
            self.assertIn(idx, sql, f"Missing index: {idx}")

    def test_signals_applied_not_null(self) -> None:
        sql = MIGRATION.read_text(encoding="utf-8").lower()
        self.assertIn("signals_applied jsonb not null", sql)

    def test_rls_enables_row_security(self) -> None:
        sql = RLS_POLICIES.read_text(encoding="utf-8").lower()
        for table in REQUIRED_TABLES:
            self.assertIn(f"alter table public.{table} enable row level security", sql)

    def test_rls_agent_roles(self) -> None:
        sql = RLS_POLICIES.read_text(encoding="utf-8")
        for role in (
            "research-agent",
            "script-agent",
            "x-optimizer-agent",
            "storage-agent",
        ):
            self.assertIn(role, sql, f"Missing RLS role: {role}")

    def test_json_schema_files_exist_and_parse(self) -> None:
        for name in REQUIRED_SCHEMA_FILES:
            path = SCHEMAS_DIR / name
            self.assertTrue(path.is_file(), f"Missing JSON Schema: {path}")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data.get("type"), "object")

    def test_x_post_schema_requires_signals_applied(self) -> None:
        schema = json.loads((SCHEMAS_DIR / "x_post.json").read_text(encoding="utf-8"))
        required = schema["properties"]["signals_applied"]["required"]
        self.assertIn("algorithm_version", required)
        self.assertIn("no_root_external_link", required)


if __name__ == "__main__":
    unittest.main()
