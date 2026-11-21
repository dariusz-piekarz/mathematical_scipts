"""Global Polish manuscript rule: coordinate chart = mapa, mapping = odwzorowanie."""
from __future__ import annotations

from pathlib import Path
import unittest

from scripts.audit_chart_terminology import (
    CARD_GAME_EXCEPTIONS,
    scan,
    unexpected_matches,
)

ROOT = Path(__file__).resolve().parents[2]


class GlobalChartTerminologyAudit(unittest.TestCase):
    def test_no_unreviewed_karta_used_in_tex_sources(self):
        candidates = scan(ROOT)
        unexpected = unexpected_matches(candidates)
        self.assertFalse(
            unexpected,
            "Coordinate chart must be mapa, not karta:\n"
            + "\n".join(
                f"{x['path']}:{x['line']}: {x['context']}"
                for x in unexpected[:50]
            ),
        )
        self.assertTrue(
            all(item["path"] in CARD_GAME_EXCEPTIONS for item in candidates)
        )

    def test_exceptions_are_only_playing_cards_in_probability(self):
        candidates = scan(ROOT)
        by_path = {}
        for entry in candidates:
            by_path[entry["path"]] = by_path.get(entry["path"], 0) + 1
        self.assertTrue(by_path)
        for path, count in by_path.items():
            with self.subTest(path=path):
                self.assertIn(path, CARD_GAME_EXCEPTIONS)
                self.assertLessEqual(count, CARD_GAME_EXCEPTIONS[path])
                self.assertTrue(
                    "probability" in path or "prawdopodobienstwa" in path
                )

    def test_unreviewed_chart_in_new_chapter_fails(self):
        fake = [{
            "path": "chapters/pl/general_topology/99-new-chapter.tex",
            "line": 10,
            "word": "karcie",
            "context": "W karcie współrzędnych...",
        }]
        self.assertEqual(unexpected_matches(fake), fake)

    def test_editorial_standard_records_both_translation_distinctions(self):
        standard = (ROOT / "docs/pl/standardy_terminologiczne.md").read_text(
            encoding="utf-8"
        )
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Angielskie „chart” to „mapa”", standard)
        self.assertIn("**mapping**", standard)
        self.assertIn("translate **chart**", agents)
        self.assertIn("**„mapa”**", agents)
        self.assertIn("**„odwzorowanie”**", agents)


if __name__ == "__main__":
    unittest.main()
