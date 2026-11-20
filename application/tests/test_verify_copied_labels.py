"""Regression checks for library LaTeX copy preservation."""
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.verify_copied_labels import compare


class CopyLabelPreservationTests(unittest.TestCase):
    ORIGINAL = (
        r"\chapter{Przykład}\label{ch:stary}" "\n"
        r"\begin{twierdzenie}\label{tw:stary}Wynik\end{twierdzenie}" "\n"
        r"Zobacz \ref{tw:stary} i \eqref{eq:stara}."
    )

    def test_identical_symbols_survive_reformatting(self):
        copied = self.ORIGINAL.replace("Wynik", "Wynik z dodatkową uwagą")
        self.assertTrue(compare(self.ORIGINAL, copied)["preserved"])

    def test_detect_missing_original_label(self):
        copied = self.ORIGINAL.replace(r"\label{tw:stary}", "")
        out = compare(self.ORIGINAL, copied)
        self.assertFalse(out["preserved"])
        self.assertEqual(out["missing_labels"], [{"name": "tw:stary", "count": 1}])

    def test_detect_changed_reference_target(self):
        copied = self.ORIGINAL.replace(r"\ref{tw:stary}", r"\ref{tw:nowy}")
        out = compare(self.ORIGINAL, copied)
        self.assertFalse(out["preserved"])
        self.assertEqual(out["missing_references"], [{"name": ["ref", "tw:stary"], "count": 1}])

    def test_detect_reference_or_label_multiplicity(self):
        copied = self.ORIGINAL + r"\ref{tw:stary}"
        out = compare(self.ORIGINAL, copied)
        self.assertFalse(out["preserved"])
        self.assertEqual(out["extra_references"], [{"name": ["ref", "tw:stary"], "count": 1}])

    def test_ignores_commented_references(self):
        copied = self.ORIGINAL + "\n% \\ref{ghost} \\label{ghost}\n"
        self.assertTrue(compare(self.ORIGINAL, copied)["preserved"])


if __name__ == "__main__":
    unittest.main()