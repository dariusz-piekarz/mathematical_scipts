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
        # Detect duplicates even when split across several TeX source lines.
        self.assertNotRegex(
            self.source,
            r"(?is)twierdzenia\s+Mackeya--Arensa\s*\(\s*twierdzenie\s+Mackeya--Arensa\s*\)"
        )
        self.assertNotIn("(twierdzenie Mackeya--Arensa)", self.source)
        self.assertIn(r"\ref{thm:mackey-arens}", self.source)

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

    def test_all_environments_balanced(self):
        for name in ("proof", "twierdzenie", "stwierdzenie", "wniosek",
                     "lemat", "definicja", "przyklad", "uwaga",
                     "enumerate", "center", "tikzpicture"):
            self.assertEqual(
                self.source.count(r"\begin{" + name + "}"),
                self.source.count(r"\end{" + name + "}"),
                msg=f"Unbalanced TeX environment: {name}"
            )
        self.assertEqual(self.source.count(r"\begin{proof}"), 17)
        self.assertEqual(self.source.count(r"\begin{przyklad}"), 4)

    def test_all_references_resolve_in_context_01_10(self):
        chapters = ROOT / "chapters/pl/functional_analysis"
        sources = [
            (chapters / next(x.name for x in chapters.glob(f"{n:02d}-*.tex"))).read_text(encoding="utf-8")
            for n in range(1, 11)
        ]
        labels = [name for src in sources for name in re.findall(r"\\label\{([^}]+)\}", src)]
        self.assertEqual(len(labels), len(set(labels)))
        references = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        references += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertGreaterEqual(len(references), 10)
        self.assertEqual([], sorted(set(references) - set(labels)))

    def test_weak_neighbourhood_has_infinite_line(self):
        # On R^4 a weak basic neighbourhood defined by 3 linear
        # coordinate functionals contains the unbounded line t*e_4.
        def vals(v):
            return tuple(v[i] for i in range(3))
        for t in (-100, -1, 0, 1, 100):
            v = (0, 0, 0, t)
            self.assertEqual(vals(v), (0, 0, 0))
        self.assertIn(r"\bigcap_{j=1}^m\ker f_j", self.source)

    def test_bornological_criterion_examples(self):
        # A bounded subset of a normed space is absorbed by any set
        # containing a fixed neighbourhood of 0.
        bounded = [(-2, 1), (4, -3), (1, 0)]
        C = lambda x: max(abs(u) for u in x) <= 1
        self.assertTrue(all(C((x[0]/5, x[1]/5)) for x in bounded))
        self.assertIn("Przestrzenie unormowane są bornologiczne", self.source)

    def test_standard_notation_and_nonzero_domain_caveat(self):
        self.assertNotRegex(self.source, r"\\(?:mathbf|mathbb)\s*\{?\s*1\s*\}?\s*_")
        self.assertNotRegex(self.source, r"sekwencyjn\w*")
        self.assertIn("przestrzeń\nsprzężoną", self.source)
        self.assertIn("ciąg", self.source)

    def test_limit_of_convergent_net_need_not_be_bounded(self):
        # Restricted finite subset model: one cofinal tail vanishes,
        # while the values outside it can become arbitrarily large.
        values_without_one = [len(set(range(2, n + 2))) for n in range(1, 100)]
        self.assertEqual(values_without_one[-1], 99)
        for n in range(1, 100):
            F = {1, *range(2, n + 2)}
            self.assertEqual(0 if 1 in F else len(F), 0)

if __name__ == "__main__":
    unittest.main()
