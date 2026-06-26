"""Unit tests for scripts/verify_supabase.py validation helpers."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "verify_supabase.py"
_spec = importlib.util.spec_from_file_location("verify_supabase", _SCRIPTS)
assert _spec and _spec.loader
verify_supabase = importlib.util.module_from_spec(_spec)
sys.modules["verify_supabase"] = verify_supabase
_spec.loader.exec_module(verify_supabase)


class TestXPostValidation(unittest.TestCase):
    def test_valid_phoenix_row(self) -> None:
        row = {
            "main_post": "Hook only — no links here.",
            "thread": [
                "Hook only — no links here.",
                "Read more https://example.com/article",
            ],
            "virality_score": 85,
            "signals_applied": {
                "reply_weight": 27,
                "author_reply_weight": 150,
                "no_root_external_link": True,
                "link_placement": "first_reply",
                "early_velocity_target_replies_15min": 5,
                "algorithm_version": "phoenix-2026",
            },
        }
        self.assertEqual(verify_supabase.validate_x_post(row), [])

    def test_url_in_main_post_fails(self) -> None:
        row = {
            "main_post": "See https://bad.com",
            "thread": ["a", "https://bad.com"],
            "signals_applied": {},
        }
        errs = verify_supabase.validate_x_post(row)
        self.assertTrue(any("main_post" in e for e in errs))

    def test_missing_phoenix_keys_fails(self) -> None:
        ok, detail = verify_supabase.validate_signals_applied({"trending": True})
        self.assertFalse(ok)
        self.assertIn("missing keys", detail)

    def test_thread_object_format(self) -> None:
        texts = verify_supabase.thread_texts(
            [{"position": 1, "text": "hello"}, {"text": "https://x.com"}]
        )
        self.assertEqual(len(texts), 2)
        self.assertIn("https://", texts[1])


if __name__ == "__main__":
    unittest.main()
