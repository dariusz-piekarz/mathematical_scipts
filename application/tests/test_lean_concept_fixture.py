"""Structural checks; the pinned Lean workflow performs actual compilation."""
from pathlib import Path
import re
import unittest

from backend import lean_concepts


class LeanConceptFixtureTests(unittest.TestCase):
    def test_every_dictionary_declaration_has_exact_fixture_entry(self):
        path = Path(__file__).resolve().parents[1] / "lean/checks/ConceptSignatures.lean"
        source = path.read_text(encoding="utf-8")
        entries = re.findall(r"^-- concept: ([a-z._]+)\n#check ([A-Za-z][A-Za-z0-9_.]*)$", source, re.M)
        expected = [(c.id, c.declaration) for c in lean_concepts._CONCEPTS]
        self.assertEqual(entries, expected)
        self.assertEqual(len(re.findall(r"^#check ", source, re.M)), len(expected))
        for section in source.split("-- concept: ")[1:]:
            self.assertIn("\nexample ", section)
        self.assertNotRegex(source, r"\b(sorry|admit|axiom)\b")

    def test_fixture_is_not_executable_browser_input(self):
        result = lean_concepts.lookup("zbiór", "set")
        self.assertIsNone(result["lean_code"])
        self.assertEqual(result["selected"]["declaration_check"], "not_run")
        self.assertFalse(result["certificate"])


if __name__ == "__main__":
    unittest.main()
