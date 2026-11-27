"""Check canonical destinations of the retired CAL-11 material."""
from pathlib import Path
import unittest


class CanonicalLebesgueMigration(unittest.TestCase):
    def test_canonical_label_owners(self):
        root = Path(__file__).resolve().parents[4]
        chapters = root / "chapters/pl/measure_theory"
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
            with self.subTest(chapter=chapter):
                files = list(chapters.glob(chapter + "-*.tex"))
                self.assertEqual(len(files), 1)
                source = files[0].read_text(encoding="utf-8-sig")
                for label in labels:
                    self.assertEqual(source.count(r"\label{" + label + "}"), 1, label)


if __name__ == "__main__":
    unittest.main()
