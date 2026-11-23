"""Finite and analytic regression examples for measure theory chapter 20.

These tests check illustrative models and source integrity; they do not
constitute a proof of the general regularity and representation theorems.
Run: python -m unittest discover -s tools/tests -p test_measure_theory_ch20.py -v
"""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex"
CH17 = ROOT / "chapters/pl/measure_theory/17-bezwzgledna-ciaglosc-osobliwosc-i-rozklad-lebesguea-miar.tex"
CH23 = ROOT / "chapters/pl/measure_theory/23-miara-haara-i-grupy-lokalnie-zwarte.tex"


def finite_subsets(n):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask & (1 << i))


def cutoff(x):
    """Continuous compactly supported function equal to one on [-1, 1]."""
    d_to_outside = max(0.0, 1.5 - abs(x))
    d_to_k = max(0.0, abs(x) - 1.0)
    denominator = d_to_outside + d_to_k
    return d_to_outside / denominator if denominator else 0.0


class TestMeasureTheoryChapter20(unittest.TestCase):
    def test_finite_discrete_metric_regular_and_compact(self):
        # Every subset of a finite discrete space is open, closed and compact.
        weights = [0.0, 2.0, 1.5, 3.5, 0.0]
        for E in finite_subsets(len(weights)):
            mass = sum(weights[i] for i in E)
            self.assertAlmostEqual(sum(weights[i] for i in E), mass)
            self.assertGreaterEqual(mass, 0)
            # The same E is the inner and outer approximant.
            self.assertEqual(set(E).difference(E), set())

    def test_polish_tight_geometric_atomic_distribution(self):
        # A probability supported on a countable dense subset of R is tight:
        # its first n atoms form a compact set with tail mass 2^(-n).
        for n in range(1, 30):
            compact_mass = sum(2.0 ** (-k) for k in range(1, n + 1))
            tail = 2.0 ** (-n)
            self.assertAlmostEqual(compact_mass + tail, 1, places=12)
            self.assertLessEqual(tail, 1 / n)

    def test_sigma_finite_locally_finite_atomic_models(self):
        # On countable discrete space with finite atom masses,
        # every singleton has finite measure; finite sets are compact.
        weights = [1 + n / 3 for n in range(1, 21)]
        for first in range(0, 19):
            for last in range(first + 1, 21):
                self.assertTrue(math.isfinite(sum(weights[first:last])))
        for n in range(1, 21):
            self.assertTrue(math.isfinite(sum(weights[:n])))

    def test_dense_atomic_support_and_measure_zero_complement(self):
        # Enumerate dense rational atoms and put positive mass on each.
        rationals = sorted({p / q for q in range(1, 26) for p in range(-2*q, 2*q+1)})
        w = [2 ** (-(i + 1)) for i in range(len(rationals))]
        self.assertTrue(all(weight > 0 for weight in w))
        for a, b in ((-1.2, -.9), (-.1, .1), (.15, .25), (.9, 1.05)):
            self.assertTrue(any(a < q < b for q in rationals))
            self.assertGreater(sum(weight for weight, q in zip(w, rationals) if a < q < b), 0)
        self.assertLess(sum(w), 1.0 + 1e-12)

    def test_cutoff_compact_support_real_line(self):
        for k in range(-100, 101):
            x = k / 25.0
            y = cutoff(x)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(y, 1)
            if abs(x) <= 1:
                self.assertAlmostEqual(y, 1)
            if abs(x) >= 1.5:
                self.assertAlmostEqual(y, 0)
        # Continuity at K and boundary of V by one-sided limits.
        for point in (1.0, 1.5, -1.0, -1.5):
            for n in (1000, 10000):
                self.assertLessEqual(abs(cutoff(point + 1/n) - cutoff(point)), .003)

    def test_cc_integrals_separate_finite_atomic_measures(self):
        atoms = [0.0, 1.0, 2.0]
        mu, nu = [1.0, 2.0, 3.0], [1.0, 2.0, 4.0]
        for atom in atoms:
            # Hat with compact support of radius 0.4 isolates this atom.
            hat = [max(0, 1 - abs(x - atom) / .4) for x in atoms]
            i_mu = sum(w * f for w, f in zip(mu, hat))
            i_nu = sum(w * f for w, f in zip(nu, hat))
            if atom == 2.0:
                self.assertNotEqual(i_mu, i_nu)
            else:
                self.assertEqual(i_mu, i_nu)

    def test_cc_density_on_finite_atomic_l_p(self):
        # Continuous compactly supported hats interpolate arbitrary
        # values on finitely many separated atoms, so the Lp error is 0.
        atoms, weights = [0, 2, 4, 6], [1.0, 2.0, 3.0, 4.0]
        values = [-3.0, 1.0, 0.5, 2.0]
        for p in (1, 1.5, 2, 3, 5):
            approximated = []
            for x in atoms:
                approximated.append(sum(
                    v * max(0.0, 1 - abs(x - a) / .5)
                    for a, v in zip(atoms, values)
                ))
            error = sum(w * abs(x - y) ** p for w, x, y in zip(weights, values, approximated))
            self.assertAlmostEqual(error, 0)

    def test_tex_environments_labels_references_and_language(self):
        src = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", src)
        self.assertGreaterEqual(len(labels), 20)
        self.assertEqual(len(labels), len(set(labels)))
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", src):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack, "Unmatched environment end")
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack, "Unclosed environments")
        self.assertNotIn("przestrzenią drugiej przeliczalności", src)
        self.assertIn("spełniającą drugi aksjomat przeliczalności", src)
        self.assertNotRegex(src, r"\\(?:mathbf|mathbb)\{1\}_")
        required = {
            "def:radon-measure-20", "thm:polish-tight-20",
            "thm:lch-secondcountable-radon-20", "lem:cutoff-radon-20",
            "thm:uniqueness-cc-20", "thm:cc-dense-lp-radon-20",
        }
        self.assertTrue(required.issubset(set(labels)))
        other = CH17.read_text(encoding="utf-8") + CH23.read_text(encoding="utf-8")
        all_labels = set(labels) | set(re.findall(r"\\label\{([^}]+)\}", other))
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", src)
        self.assertFalse(set(refs) - all_labels)


if __name__ == "__main__":
    unittest.main()
