"""Finite-model and TeX structure regression for measure theory chapter 15.

These checks do NOT prove the infinite-dimensional theorems or certify LaTeX/PDF.
They detect regressions in midpoint inequalities, Lp dual pairing, the
nonintegrable kernel witness, and the references used in the chapter.
Run: python -m unittest test_measure_theory_ch15_li_gate.py
"""
import math
import random
import re
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
CHAPTER = BASE / "chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex"
DEPENDENCIES = (
    BASE / "chapters/pl/measure_theory/10-regularnosc-funkcji-mierzalnych-i-aproksymacja-funkcjami-ciaglymi.tex",
    BASE / "chapters/pl/measure_theory/14-przestrzenie-lp-i-ich-podstawowe-wlasnosci.tex",
)


def lp(z, weights, p):
    return sum(w * abs(v) ** p for w, v in zip(weights, z)) ** (1.0 / p)


def midpoint_gap(a, b, weights, p):
    midpoint = [(x + y) / 2 for x, y in zip(a, b)]
    return (lp(a, weights, p) ** p + lp(b, weights, p) ** p) / 2 - lp(midpoint, weights, p) ** p


class TestMeasureTheoryChapter15Gate(unittest.TestCase):
    def test_clarkson_and_small_p_midpoint_bound(self):
        rng = random.Random(150052)
        weights = (0.3, 1.1, 0.8, 2.3, 0.1, 1.4)
        for p in (1.1, 1.3, 1.7, 1.95, 2, 2.2, 3, 4, 8):
            for _ in range(500):
                a = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in weights]
                b = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in weights]
                v = [(x - y) / 2 for x, y in zip(a, b)]
                gap = midpoint_gap(a, b, weights, p)
                if p >= 2:
                    lower_bound = lp(v, weights, p) ** p
                else:
                    lower_bound = p * (p - 1) / 2 * lp(v, weights, p) ** 2 / (lp(a, weights, p) + lp(b, weights, p)) ** (2 - p)
                self.assertLessEqual(lower_bound, gap + 5e-10 * max(1, abs(gap), lower_bound))

    def test_conjugate_pairing_sharpness(self):
        weights = (1.0, 0.5, 3.0, 0.8)
        g = (1.2 + 0.1j, -0.5 + 2j, 1.1j, -0.2 + 0.3j)
        for p in (1.1, 1.5, 2, 3, 8):
            q = p / (p - 1)
            gnorm = lp(g, weights, q)
            f = [z.conjugate() * abs(z) ** (q - 2) / gnorm ** (q - 1) for z in g]
            pairing = sum(w * x * y for w, x, y in zip(weights, f, g))
            self.assertAlmostEqual(lp(f, weights, p), 1.0, places=11)
            self.assertAlmostEqual(pairing.real, gnorm, places=10)
            self.assertAlmostEqual(pairing.imag, 0.0, places=10)

    def test_l1_linf_pairing(self):
        weights = (0.1, 2, 0.25, 4)
        g = (1.5, -2.0j, 1.2 + 0.1j, 2.2j)
        idx = max(range(len(g)), key=lambda i: abs(g[i]))
        f = [0j] * len(g)
        f[idx] = g[idx].conjugate() / abs(g[idx]) / weights[idx]
        self.assertAlmostEqual(lp(f, weights, 1), 1.0)
        self.assertAlmostEqual(sum(w * x * y for w, x, y in zip(weights, f, g)).real, max(abs(z) for z in g))

    def test_variational_minimizer(self):
        rng = random.Random(150053)
        weights = (0.3, 1.1, 0.8, 2.3, 0.1, 1.4)
        for p in (1.1, 1.5, 2, 3, 5):
            q = p / (p - 1)
            for _ in range(300):
                alpha = rng.uniform(1.5, 3)
                g = [complex(rng.uniform(-.5, .5), rng.uniform(-.5, .5)) for _ in weights]
                f = [alpha ** (-1 / (p - 1)) * z.conjugate() * abs(z) ** (q - 2) if z else 0j for z in g]
                def energy(vals):
                    return sum(w * (alpha * abs(x) ** p / p - (x * y).real) for w, x, y in zip(weights, vals, g))
                modified = [x + complex(rng.uniform(-.4, .4), rng.uniform(-.4, .4)) for x in f]
                self.assertGreaterEqual(energy(modified) - energy(f), -1e-9)

    def test_nonintegrable_power_kernel_explicit_witness(self):
        # On (0,1), g=x^(-alpha), p=q=2. g_N=g*chi_{g<=N}.
        # The proof's normalized f_N has L2 norm 1 and pairing ||g_N||_2.
        for alpha in (0.5, 1.0, 1.5):
            integrals = []
            for N in (4, 8, 16, 32, 64, 128):
                cutoff = N ** (-1 / alpha)
                exponent = 2 * alpha
                integral = math.log(1 / cutoff) if exponent == 1 else (1 - cutoff ** (1 - exponent)) / (1 - exponent)
                integrals.append(integral)
                self.assertGreater(integral, 0)
            self.assertTrue(all(y > x for x, y in zip(integrals, integrals[1:])))
            self.assertGreater(integrals[-1], integrals[0])

    def test_rademacher_cancellation_on_dyadic_blocks(self):
        for n in range(1, 9):
            signs = [1 if k % 2 == 0 else -1 for k in range(2 ** (n + 1))]
            for m in range(n):
                block = 2 ** (n + 1 - m)
                self.assertEqual(sum(signs[:block]), 0)
                self.assertEqual(sum(signs), 0)

    def test_environment_nesting_labels_and_local_refs(self):
        source = CHAPTER.read_text(encoding="utf-8")
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), match[2])
        self.assertEqual(stack, [])
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), len(set(labels)))
        combined = source + "".join(path.read_text(encoding="utf-8") for path in DEPENDENCIES)
        known = set(re.findall(r"\\label\{([^}]+)\}", combined))
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
        self.assertFalse(set(refs) - known)
        self.assertGreaterEqual(len(refs), 15)

    def test_nonintegrable_kernel_witness_in_tex(self):
        source = CHAPTER.read_text(encoding="utf-8")
        for needle in (r"g_N=g\chi_{\{g\le N\}}", r"f_N=g_N^{q-1}/\|g_N\|_q^{q-1}", r"\|g_N\|_q\longrightarrow\infty"):
            self.assertIn(needle, source)
        self.assertNotIn(r"\mathbf{1}_", source)
        self.assertNotIn(r"\mathbb{1}_", source)


if __name__ == "__main__":
    unittest.main()
