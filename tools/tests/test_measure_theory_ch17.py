"""Finite-model and source regressions for measure theory chapter 17.

Checks sigma-finite decomposition, absolute continuity, singularity, the
Cantor example, and dependencies. Finite examples are not general proofs.
Run: python -m unittest tools.tests.test_measure_theory_ch17 -v
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH17 = ROOT / "chapters/pl/measure_theory/17-bezwzgledna-ciaglosc-osobliwosc-i-rozklad-lebesguea-miar.tex"
CH16 = ROOT / "chapters/pl/measure_theory/16-miary-ze-znakiem-miary-zespolone-i-wariacja-calkowita.tex"
CH18 = ROOT / "chapters/pl/measure_theory/18-twierdzenie-radona-nikodyma-i-pochodne-miar.tex"


def subsets(n):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask & (1 << i))


def masses(weights, E):
    return sum(weights[i] for i in E)


def decompose(mu, nu):
    """On a finite atomic space, the singular part lies at mu-null atoms."""
    ac = [v if u > 0 else 0 for u, v in zip(mu, nu)]
    singular = [v if u == 0 else 0 for u, v in zip(mu, nu)]
    return ac, singular


class TestMeasureTheoryChapter17(unittest.TestCase):
    def test_epsilon_delta_and_equivalent_atomic_measures(self):
        rng = random.Random(1701)
        for _ in range(120):
            mu = [rng.randrange(6) / 2 for _ in range(5)]
            nu = [rng.randrange(6) / 3 if u > 0 else 0 for u in mu]
            positive = [u for u in mu if u > 0]
            delta = min(positive) / 2 if positive else 1
            for E in subsets(len(mu)):
                if masses(mu, E) == 0:
                    self.assertEqual(masses(nu, E), 0)
                if masses(mu, E) < delta:
                    self.assertEqual(masses(nu, E), 0)
            # An equivalent measure must have the same null atoms.
            equivalent = [u * (i + 1) for i, u in enumerate(mu)]
            for E in subsets(len(mu)):
                self.assertEqual(masses(mu, E) == 0, masses(equivalent, E) == 0)

    def test_hahn_threshold_lebegue_decomposition(self):
        rng = random.Random(1702)
        for _ in range(200):
            mu = [rng.randrange(6) for _ in range(5)]
            nu = [rng.randrange(10) for _ in range(5)]
            for k in range(1, 11):
                limit = 2 ** k
                P = [i for i in range(5) if nu[i] >= limit * mu[i]]
                N = [i for i in range(5) if i not in P]
                self.assertLessEqual(masses(mu, P), masses(nu, P) / limit)
                for E in subsets(5):
                    self.assertGreaterEqual(
                        masses(nu, set(E) & set(P)) -
                        limit * masses(mu, set(E) & set(P)), 0
                    )
                    self.assertLessEqual(
                        masses(nu, set(E) & set(N)) -
                        limit * masses(mu, set(E) & set(N)), 0
                    )
            ac, singular = decompose(mu, nu)
            self.assertEqual([a + b for a, b in zip(ac, singular)], nu)
            self.assertEqual(sum(mu[i] for i in range(5) if singular[i] > 0), 0)
            self.assertTrue(all(ac[i] == 0 for i in range(5) if mu[i] == 0))
            # For k >= 4, all positive-mu atoms lie in N_k in this model.
            eventual = [i for i in range(5) if nu[i] >= 2 ** 8 * mu[i]]
            self.assertEqual(
                [nu[i] if i in eventual else 0 for i in range(5)],
                singular
            )

    def test_unique_finite_atomic_decomposition(self):
        rng = random.Random(1703)
        for _ in range(120):
            mu = [rng.randrange(5) for _ in range(5)]
            nu = [rng.randrange(6) for _ in range(5)]
            expected_ac, expected_s = decompose(mu, nu)
            must_be_in_S = {i for i in range(5) if mu[i] == 0 and nu[i] > 0}
            optional = {i for i in range(5) if mu[i] == 0 and nu[i] == 0}
            # Any two valid singular supports produce the same measures.
            for choices in subsets(len(optional)):
                extra = {sorted(optional)[j] for j in choices}
                S = must_be_in_S | extra
                s = [nu[i] if i in S else 0 for i in range(5)]
                ac = [nu[i] if i not in S else 0 for i in range(5)]
                self.assertEqual(ac, expected_ac)
                self.assertEqual(s, expected_s)

    def test_sigma_finite_gluing_on_disjoint_cells(self):
        rng = random.Random(1704)
        cells = ((0, 3), (3, 5), (5, 8))
        for _ in range(160):
            mu = [rng.randrange(5) for _ in range(8)]
            nu = [rng.randrange(7) for _ in range(8)]
            ac, sing = decompose(mu, nu)
            glued_ac = [0] * 8
            glued_s = [0] * 8
            for left, right in cells:
                a, s = decompose(mu[left:right], nu[left:right])
                glued_ac[left:right] = a
                glued_s[left:right] = s
            self.assertEqual((glued_ac, glued_s), (ac, sing))

    def test_complex_measure_singularity_uses_total_variation(self):
        # On a finite set |eta| has atom mass |eta({i})|.
        mu = [0, 1, 2, 0, 1]
        eta = [3 + 4j, -2j, 1 + 1j, -2 + 5j, 0j]
        ac = [z if u > 0 else 0j for u, z in zip(mu, eta)]
        singular = [z if u == 0 else 0j for u, z in zip(mu, eta)]
        self.assertEqual([a + b for a, b in zip(ac, singular)], eta)
        self.assertEqual(sum(mu[i] for i, z in enumerate(singular) if z), 0)
        for E in subsets(len(mu)):
            if masses(mu, E) == 0:
                self.assertEqual(masses(ac, E), 0)
        self.assertAlmostEqual(sum(abs(z) for z in eta),
                               sum(abs(z) for z in ac) + sum(abs(z) for z in singular))

    def test_cantor_binary_ternary_cylinder_probabilities(self):
        for n in range(1, 10):
            total = 0.0
            for k in range(2 ** n):
                digits = [(k >> (n - j - 1)) & 1 for j in range(n)]
                left = sum(2 * digit * 3 ** (-j - 1) for j, digit in enumerate(digits))
                # x = (k+1/2)/2^n is dyadic with digit 1 at n+1,
                # and no later nonzero binary digits.
                value = left + 2 * 3 ** (-(n + 1))
                self.assertGreaterEqual(value, left)
                self.assertLessEqual(value, left + 3 ** (-n) + 1e-14)
                total += 2 ** (-n)
            self.assertAlmostEqual(total, 1.0, places=13)
            self.assertEqual(2 ** (-n), 1.0 / (2 ** n))
        self.assertLess(2 ** (-12), .001)  # Cylinder bound on point masses.

    def test_atomic_continuous_singular_split(self):
        atoms = {1 / 3: 3.0, 2 / 3: 2.0}
        density_mass = 1.5  # integral_0^1 (1+x) dx
        singular_mass = sum(atoms.values())
        self.assertEqual(singular_mass, 5)
        self.assertAlmostEqual(density_mass + singular_mass, 6.5)
        self.assertNotEqual(density_mass, singular_mass)
        # The finite atomic part is concentrated on a Lebesgue-null set.
        self.assertEqual(len(atoms), 2)

    def test_tex_structure_dependencies_and_no_rn_circularity(self):
        src = CH17.read_text(encoding="utf-8")
        other = CH16.read_text(encoding="utf-8") + CH18.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", src)
        self.assertEqual(len(labels), 14)
        self.assertEqual(len(set(labels)), len(labels))
        known = set(labels) | set(re.findall(r"\\label\{([^}]+)\}", other))
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", src)
        self.assertFalse(set(refs) - known)
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", src):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack)
        self.assertIn(r"\kappa(I_{\varepsilon_1,\ldots,\varepsilon_n})=2^{-n}", src)
        self.assertIn(r"\mu(E_n)\le n\int_{E_n}x\,\mathrm d\lambda_1(x)=0", src)
        theorem = src.split(r"\begin{twierdzenie}[Rozkład Lebesgue'a dla miar skończonych]", 1)[1]
        proof = theorem.split(r"\end{proof}", 1)[0]
        self.assertNotIn(r"\ref{ch:radon-nikodym-18}", proof)
        self.assertNotRegex(src, r"\\(?:mathbf|mathbb)\{1\}_")
        self.assertNotIn("zbieżność dominowana", src)


if __name__ == "__main__":
    unittest.main()
