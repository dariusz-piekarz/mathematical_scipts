"""Retain IT-11 source regression against canonical measure theory chapters."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class MigratedLebesgueSourceIntegrity(unittest.TestCase):
    def setUp(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "measure_theory" and b["language"] == "pl")
        self.sources = {
            Path(p).name[:2]: (ROOT / p).read_text(encoding="utf-8")
            for p in book["chapters"] if re.match(r"\d{2}-", Path(p).name)
        }

    def test_fallback_precedes_first_use(self):
        source = self.sources["08"]
        fallback = r"\providecommand{\atlasref}[2]{#2}"
        self.assertIn(fallback, source)
        first = source.find(r"\atlasref{")
        if first >= 0:
            self.assertLess(source.index(fallback), first)

    def test_canonical_lebesgue_targets(self):
        expected = {
            "07": ("ch:calkowanie-lebesgue",),
            "08": ("thm:mct", "thm:mct-ae", "thm:fatou", "thm:dct",
                   "cor:dct-l1", "cor:bct", "thm:sum-nonnegative-integrals",
                   "thm:sum-absolutely-integrable"),
            "11": ("ch:parametry-calki",),
            "12": ("thm:fubini-12",),
            "13": ("thm:change-variables-13",),
            "14": ("thm:riesz-fischer-14",),
            "25": ("thm:lebesgue-diff-25",),
        }
        for chapter, labels in expected.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    token = r"\label{" + label + "}"
                    self.assertEqual(self.sources[chapter].count(token), 1)
                    self.assertFalse(any(token in s for ch, s in self.sources.items() if ch != chapter))


if __name__ == "__main__":
    unittest.main()
