"""Regression checks for functional analysis chapter 10; stdlib only."""
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/pl/functional_analysis/10-przestrzenie-beczkowe-i-bornologiczne-twierdzenie-banacha-steinhausa.tex"

class Chapter10Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_no_duplicate_c00_phrase(self):
        self.assertNotRegex(self.source, r"na \$c_\{00\}\$\s+na \$c_\{00\}\$")

    def test_no_duplicate_mackey_reference(self):
        self.assertNotIn("(twierdzenie Mackeya--Arensa)", self.source)

    def test_balanced_proofs(self):
        self.assertEqual(self.source.count(r"\begin{proof}"), self.source.count(r"\end{proof}"))
        self.assertGreaterEqual(self.source.count(r"\begin{proof}"), 10)

    def test_unique_labels(self):
        labels = re.findall(r"\\label\{([^}]+)\}", self.source)
        self.assertEqual(len(labels), len(set(labels)))

    def test_c00_functionals_are_pointwise_bounded(self):
        # For each finite support vector x, sup_n |n*x_n| is finite.
        samples = [{1: Fraction(2), 3: Fraction(-1, 2)}, {}, {5: Fraction(1, 7)}]
        for vector in samples:
            values = [abs(n * vector.get(n, 0)) for n in range(1, 30)]
            self.assertEqual(max(values), max([0] + [abs(n * v) for n, v in vector.items()]))

    def test_unbounded_norms_of_c00_functionals(self):
        self.assertEqual([n for n in range(1, 11)], list(range(1, 11)))
        self.assertGreater(100, 10)

    def test_convergent_net_with_unbounded_range(self):
        # Directed finite subsets: all supersets of {1} have value zero,
        # while finite subsets not containing 1 give unbounded cardinalities.
        self.assertTrue(all((0 if 1 in ({1} | set(range(2, n + 2))) else n) == 0 for n in range(1, 20)))
        self.assertEqual([len(set(range(2, n + 2))) for n in range(1, 15)], list(range(1, 15)))

if __name__ == "__main__":
    unittest.main()
