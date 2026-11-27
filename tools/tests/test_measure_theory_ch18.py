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
    def test_density_change_with_extended_weights(self):
        # Extended nonnegative arithmetic must handle 0*infinity.
        from itertools import product

        def mul(a, b):
            return 0 if a == 0 or b == 0 else a * b

        values = (0, 1, 2, math.inf)
        for base, density, integrand in product(values, repeat=3):
            mass_after = mul(base, density)
            self.assertEqual(mul(integrand, mass_after),
                             mul(mul(integrand, density), base))
            for E in (False, True):
                self.assertEqual(mul(int(E), mass_after),
                                 mul(mul(int(E), density), base))
        # A nonzero finite integrand may meet infinite density only
        # on a base-null set if its weighted integral is finite.
        for base, density, value in product(values, values, (0, 1, 2)):
            integral = mul(mul(value, density), base)
            if math.isfinite(integral) and density == math.inf and value:
                self.assertEqual(base, 0)

    def test_conditional_expectation_null_blocks_and_tower(self):
        from fractions import Fraction
        from itertools import product

        def cond(p, y, groups, null_value):
            z = [Fraction(0)] * len(p)
            for block in groups:
                mass = sum(p[i] for i in block)
                avg = (sum(p[i] * y[i] for i in block) / mass
                       if mass else Fraction(null_value))
                for i in block:
                    z[i] = avg
            return z

        fine = ((0, 1), (2,), (3,))
        coarse = ((0, 1, 2), (3,))
        for p0 in product(range(3), repeat=4):
            if not sum(p0):
                continue
            p = [Fraction(v, sum(p0)) for v in p0]
            for y in product((-1, 0, 2), repeat=4):
                z = cond(p, y, fine, 17)
                other = cond(p, y, fine, -19)
                self.assertEqual(sum(p[i] * abs(z[i] - other[i])
                                     for i in range(4)), 0)
                for block in fine:
                    self.assertEqual(sum(p[i] * (y[i] - z[i])
                                         for i in block), 0)
                self.assertLessEqual(sum(p[i] * z[i] ** 2 for i in range(4)),
                                     sum(p[i] * y[i] ** 2 for i in range(4)))
                tower = cond(p, z, coarse, 0)
                direct = cond(p, y, coarse, 0)
                self.assertEqual(tower, direct)

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
        combined = source + "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(CHAPTER.parent.glob("[0-9][0-9]-*.tex"))
            if path != CHAPTER
        )
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        # Preserve every existing label, including migrated integration
        # results, without rejecting legitimate future additions.
        required_labels = {
            "ch:radon-nikodym-18",
            "eq:RN-question-18",
            "def:RN-derivative-18",
            "lem:integration-density-18",
            "eq:integration-density-18",
            "thm:RN-finite-18",
            "eq:RN-finite-18",
            "eq:RN-lambda-h-18",
            "eq:RN-mu-nu-h-18",
            "thm:RN-sigfin-18",
            "eq:RN-general-18",
            "eq:RN-integral-change-18",
            "ex:RN-failure-nonsigma-18",
            "thm:RN-complex-18",
            "eq:RN-complex-18",
            "cor:RN-lebesgue-sum-18",
            "eq:RN-Lebesgue-decomp-18",
            "thm:polar-complex-measure-18",
            "eq:polar-complex-measure-18",
            "thm:RN-chain-18",
            "eq:RN-chain-18",
            "thm:RN-inverse-18",
            "eq:RN-inverse-18",
            "cor:RN-linearity-18",
            "def:conditional-exp-18",
            "eq:CE-def-18",
            "thm:CE-existence-18",
            "thm:CE-orthogonal-18",
            "it:thm:stieltjes-decomposition",
            "it:thm:stieltjes-generator-decomposition",
            "it:cor:stieltjes-signed-integrability",
        }
        self.assertFalse(required_labels - set(labels),
                         f"Missing labels: {sorted(required_labels - set(labels))}")
        self.assertEqual(len(labels), len(set(labels)))
        known = set(re.findall(r"\\label\{([^}]+)\}", combined))
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
        self.assertFalse(set(refs) - known)
        atlas_targets = {
            "P1-10": "probability_volume_i/10-*.tex",
            "ME-04": "measure_theory/04-*.tex",
            "ME-08": "measure_theory/08-*.tex",
            "ME-16": "measure_theory/16-*.tex",
            "ME-17": "measure_theory/17-*.tex",
            "ME-25": "measure_theory/25-*.tex",
        }
        for code, label in re.findall(r"\\atlasref\{([^{}:]+)::([^{}]+)\}", source):
            with self.subTest(code=code, label=label):
                self.assertIn(code, atlas_targets)
                targets = list((ROOT / "chapters/pl").glob(atlas_targets[code]))
                self.assertEqual(len(targets), 1)
                self.assertIn(r"\label{" + label + "}", targets[0].read_text(encoding="utf-8"))
        self.assertNotRegex(source, r"\\inL\b")

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
