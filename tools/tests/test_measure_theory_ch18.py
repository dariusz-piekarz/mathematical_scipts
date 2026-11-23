"""Finite-model and TeX regressions for chapter 18 (Radon–Nikodym).

These models test exact identities in atomic measure spaces and cannot
prove the general theorems for arbitrary sigma-algebras.
Run: python -m unittest tools.tests.test_measure_theory_ch18 -v
"""
import math
import random
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/measure_theory/18-twierdzenie-radona-nikodyma-i-pochodne-miar.tex"
DEPS = (
    ROOT / "chapters/pl/measure_theory/16-miary-ze-znakiem-miary-zespolone-i-wariacja-calkowita.tex",
    ROOT / "chapters/pl/measure_theory/17-bezwzgledna-ciaglosc-osobliwosc-i-rozklad-lebesguea-miar.tex",
)


def subsets(n):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask & (1 << i))


def mass(weights, E):
    return sum(weights[i] for i in E)


class TestMeasureTheoryChapter18(unittest.TestCase):
    def test_finite_rn_via_hilbert_common_measure(self):
        rng = random.Random(18001)
        for _ in range(180):
            mu = [rng.randint(0, 6) for _ in range(5)]
            nu = [rng.randint(0, 6) if m > 0 else 0 for m in mu]
            lam = [m + v for m, v in zip(mu, nu)]
            h = [v / l if l else 0 for l, v in zip(lam, nu)]
            f = [v / m if m else 0 for m, v in zip(mu, nu)]
            self.assertTrue(all(0 <= x <= 1 for x in h))
            for E in subsets(5):
                self.assertAlmostEqual(mass(nu, E), sum(h[i] * lam[i] for i in E))
                self.assertAlmostEqual(mass(mu, E), sum((1 - h[i]) * lam[i] for i in E))
                self.assertAlmostEqual(mass(nu, E), sum(f[i] * mu[i] for i in E))
            for i, m in enumerate(mu):
                if m:
                    self.assertAlmostEqual(f[i], h[i] / (1 - h[i]))
            self.assertAlmostEqual(sum(f[i] * mu[i] for i in range(5)), sum(nu))

    def test_sigma_finite_disjoint_gluing(self):
        rng = random.Random(18002)
        cells = ((0, 3), (3, 5), (5, 8))
        for _ in range(170):
            mu = [rng.randint(0, 5) for _ in range(8)]
            nu = [rng.randint(0, 7) if x > 0 else 0 for x in mu]
            f = [v / m if m else 0 for m, v in zip(mu, nu)]
            for left, right in cells:
                for E in subsets(right - left):
                    indices = [left + i for i in E]
                    self.assertAlmostEqual(
                        mass(nu, indices), sum(mu[i] * f[i] for i in indices)
                    )
            for E in subsets(8):
                self.assertAlmostEqual(mass(nu, E), sum(mu[i] * f[i] for i in E))

    def test_chain_and_inverse_rule(self):
        mu = [1.0, 0.0, 2.0, 3.0, 0.0]
        f = [2.0, 0.0, 0.5, 0.0, 0.0]
        g = [0.5, 1000.0, 3.0, 7.0, 0.0]
        nu = [x * y for x, y in zip(mu, f)]
        rho = [x * y for x, y in zip(nu, g)]
        for E in subsets(5):
            self.assertAlmostEqual(mass(rho, E), sum(mu[i] * f[i] * g[i] for i in E))
        mu2 = [1.0, 2.0, 3.0]
        f2 = [0.5, 2.0, 4.0]
        nu2 = [x * y for x, y in zip(mu2, f2)]
        for E in subsets(3):
            self.assertAlmostEqual(mass(mu2, E), sum(nu2[i] / f2[i] for i in E))

    def test_complex_rn_total_variation_and_polar(self):
        rng = random.Random(18004)
        for _ in range(180):
            mu = [rng.randint(0, 5) for _ in range(5)]
            eta = [complex(rng.randint(-5, 5), rng.randint(-5, 5)) if m else 0j for m in mu]
            f = [v / m if m else 0j for m, v in zip(mu, eta)]
            variation = [abs(v) for v in eta]
            u = [v / abs(v) if v else (1 + 0j) for v in eta]
            for E in subsets(5):
                self.assertAlmostEqual(abs(mass(eta, E) - sum(f[i] * mu[i] for i in E)), 0)
                self.assertAlmostEqual(mass(variation, E), sum(mu[i] * abs(f[i]) for i in E))
                self.assertAlmostEqual(abs(mass(eta, E) - sum(u[i] * variation[i] for i in E)), 0)
            self.assertTrue(all(abs(abs(z) - 1) < 1e-13 for z in u))

    def test_conditional_expectation_weighted_partitions(self):
        weights = [0.1, 0.2, 0.3, 0.4]
        Y = [3.0, -2.0, 1.0, 4.0]
        blocks = ((0, 1), (2, 3))
        Z = [0.0] * 4
        for block in blocks:
            weight = sum(weights[i] for i in block)
            average = sum(weights[i] * Y[i] for i in block) / weight
            for i in block:
                Z[i] = average
            self.assertAlmostEqual(
                sum(weights[i] * Z[i] for i in block),
                sum(weights[i] * Y[i] for i in block)
            )
        self.assertLessEqual(sum(w * abs(z) for w, z in zip(weights, Z)),
                             sum(w * abs(y) for w, y in zip(weights, Y)))
        self.assertLessEqual(sum(w * z * z for w, z in zip(weights, Z)),
                             sum(w * y * y for w, y in zip(weights, Y)))
        # Passing to the coarser trivial sigma-algebra yields E[Y].
        self.assertAlmostEqual(sum(w * z for w, z in zip(weights, Z)),
                               sum(w * y for w, y in zip(weights, Y)))

    def test_conditional_expectation_orthogonal_projection(self):
        p = [0.1, 0.2, 0.3, 0.4]
        y = [2.0, -1.0, 5.0, 1.0]
        groups = ((0, 1), (2, 3))
        z = [0.0] * 4
        for block in groups:
            avg = sum(p[i] * y[i] for i in block) / sum(p[i] for i in block)
            for i in block:
                z[i] = avg
        for w1, w2 in ((1.0, 1.0), (0.5, -2.0), (-7.0, 3.0)):
            w = [w1, w1, w2, w2]
            orthogonality = sum(p[i] * (y[i] - z[i]) * w[i] for i in range(4))
            self.assertAlmostEqual(orthogonality, 0, places=12)
        self.assertLessEqual(sum(p[i] * z[i] ** 2 for i in range(4)),
                             sum(p[i] * y[i] ** 2 for i in range(4)))

    def test_nonsigma_finite_nu_counterexample(self):
        # mu is finite Lebesgue on (0,1); nu(E)=inf for mu(E)>0.
        # Every bounded nonnegative density integrates finitely over (0,1).
        for m in (1, 2, 3, 10, 100):
            E_mass = 1 / m
            nu_mass = math.inf if E_mass > 0 else 0.0
            integral_of_bounded_function = m * E_mass
            self.assertEqual(nu_mass, math.inf)
            self.assertTrue(math.isfinite(integral_of_bounded_function))

    def test_source_references_and_rn_independence(self):
        source = CHAPTER.read_text(encoding="utf-8")
        combined = source + "".join(path.read_text(encoding="utf-8") for path in DEPS)
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), 28)
        self.assertEqual(len(labels), len(set(labels)))
        known = set(re.findall(r"\\label\{([^}]+)\}", combined))
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
        self.assertFalse(set(refs) - known)
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack)
        self.assertIn(r"\label{thm:RN-finite-18}", source)
        self.assertIn(r"\label{thm:RN-sigfin-18}", source)
        self.assertIn(r"\label{thm:CE-orthogonal-18}", source)
        self.assertIn(r"\nu(E_m)=\infty", source)
        self.assertIn(r"\kappa\perp\mu", source)
        self.assertNotRegex(source, r"\\(?:mathbf|mathbb)\{1\}_")
        finite_proof = source.split(r"\begin{twierdzenie}[Radon--Nikodym dla miar skończonych]", 1)[1]
        finite_proof = finite_proof.split(r"\end{proof}", 1)[0]
        self.assertNotIn(r"\ref{thm:RN-sigfin-18}", finite_proof)


if __name__ == "__main__":
    unittest.main()
