"""Finite-model and TeX regressions for chapter 21: Riesz–Markov–Kakutani.

Tests verify atomic analogues of measure representation, norm, positivity,
outer measure, localization, and total variation. They are not general proofs.
Run: python -m unittest discover -s tools/tests -p 'test_measure_theory_ch21.py' -v
"""
import math
import random
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/measure_theory/21-twierdzenie-riesza-markowa-kakutaniego.tex"


def subsets(n):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask & (1 << i))


class TestMeasureTheoryChapter21(unittest.TestCase):
    def test_positive_functional_compact_representation_and_norm(self):
        rng = random.Random(2101)
        for _ in range(180):
            mass = [rng.randrange(0, 9) / 3 for _ in range(5)]
            values = [rng.uniform(-2, 2) for _ in range(5)]
            result = sum(m * f for m, f in zip(mass, values))
            self.assertLessEqual(abs(result),
                                 max(abs(f) for f in values) * sum(mass) + 1e-12)
            self.assertAlmostEqual(sum(mass), sum(m * 1 for m in mass))
            # Evaluations at atomic singleton indicators determine the measure.
            recovered = [sum(mass[i] * (1 if i == j else 0)
                             for i in range(5)) for j in range(5)]
            self.assertEqual(recovered, mass)

    def test_metric_outer_measure_compact_atomic(self):
        rng = random.Random(2102)
        for _ in range(50):
            mass = [rng.randrange(0, 8) / 4 for _ in range(5)]
            m = {E: sum(mass[i] for i in E) for E in subsets(5)}
            self.assertEqual(m[()], 0)
            for A in m:
                for B in m:
                    if set(A).isdisjoint(B):
                        self.assertAlmostEqual(m[tuple(sorted(set(A) | set(B)))],
                                               m[A] + m[B])
                    if set(A).issubset(B):
                        self.assertLessEqual(m[A], m[B] + 1e-12)

    def test_compact_representation_layer_cake_bounds(self):
        rng = random.Random(2103)
        for _ in range(120):
            mass = [rng.randint(0, 6) for _ in range(5)]
            f = [rng.randint(0, 12) / 3 for _ in range(5)]
            M = max(f)
            if M == 0:
                continue
            N = 40
            delta = M / N
            value = sum(x * y for x, y in zip(mass, f))
            upper = delta * sum(sum(w for w, y in zip(mass, f) if y > i * delta)
                                for i in range(N))
            lower = delta * sum(sum(w for w, y in zip(mass, f) if y > i * delta)
                                for i in range(1, N + 1))
            self.assertLessEqual(lower, value + 1e-10)
            self.assertLessEqual(value, upper + 1e-10)
            self.assertLessEqual(upper - lower, delta * sum(mass) + 1e-10)

    def test_localization_and_gluing_of_radon_measures(self):
        rng = random.Random(2104)
        for _ in range(200):
            mass = [rng.randint(0, 9) / 4 for _ in range(7)]
            # U_n = first n+1 atoms; restriction consistency on overlaps.
            local = [mass[:n] for n in range(1, 8)]
            for n in range(1, 8):
                for m in range(n, 8):
                    self.assertEqual(local[m - 1][:n], local[n - 1])
            # B_n = new atom at stage n, so gluing recovers the measure.
            glued = [local[n - 1][n - 1] for n in range(1, 8)]
            self.assertEqual(glued, mass)

    def test_dense_compact_support_in_c0_discrete(self):
        # On the discrete natural numbers C_c consists of finite supports;
        # C_0 consists of sequences converging to zero.
        for n in (1, 2, 4, 8, 15, 30):
            values = [1 / (k + 1) for k in range(200)]
            cutoff = [v if k < n else 0 for k, v in enumerate(values)]
            distance = max(abs(x - y) for x, y in zip(values, cutoff))
            self.assertAlmostEqual(distance, 1 / (n + 1))
        self.assertLess(1 / 1001, 0.001)

    def test_complex_variation_and_operator_norm(self):
        rng = random.Random(2106)
        for _ in range(160):
            atoms = [complex(rng.randint(-4, 4), rng.randint(-4, 4)) for _ in range(5)]
            variation = sum(abs(z) for z in atoms)
            phases = [z.conjugate() / abs(z) if z else 0j for z in atoms]
            pairing = sum(z * phase for z, phase in zip(atoms, phases))
            self.assertAlmostEqual(pairing.real, variation, places=11)
            self.assertAlmostEqual(pairing.imag, 0, places=11)
            self.assertLessEqual(abs(sum(atoms)), variation + 1e-10)

    def test_order_of_positive_functionals_matches_measures(self):
        rng = random.Random(2107)
        for _ in range(180):
            first = [rng.randint(0, 5) for _ in range(5)]
            increment = [rng.randint(0, 5) for _ in range(5)]
            second = [a + b for a, b in zip(first, increment)]
            for E in subsets(5):
                self.assertLessEqual(sum(first[i] for i in E),
                                     sum(second[i] for i in E))
            # If the coordinate-wise inequality fails, one singleton test
            # immediately witnesses the failure of functional order.
            if second[0]:
                bad = second.copy()
                bad[0] = second[0] - 1
                witness = [1, 0, 0, 0, 0]
                self.assertLess(
                    sum(bad[i] * witness[i] for i in range(5)),
                    sum(second[i] * witness[i] for i in range(5))
                )

    def test_source_labels_and_partition_of_unity(self):
        src = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", src)
        self.assertGreaterEqual(len(labels), 20)
        self.assertEqual(len(labels), len(set(labels)))
        expected = {
            "thm:riesz-positive-21", "lem:metric-outer-borel-21",
            "thm:compact-riesz-21", "lem:exhaustion-21",
            "thm:riesz-c0-positive-21", "thm:riesz-complex-21",
            "cor:riesz-order-21", "cor:measures-separate-21",
            "ex:riesz-complex-atoms-21",
        }
        self.assertTrue(expected.issubset(set(labels)))
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", src):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack, "Unexpected LaTeX environment end")
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack, "Unclosed LaTeX environments")
        for snippet in (
            r"\theta_i=\chi\psi_i/\psi", r"\operatorname{supp}\chi\subseteq\{\psi>0\}",
            r"Jeśli $F=\varnothing$ lub $F=Z$",
            "spełnia", "drugi aksjomat przeliczalności",
        ):
            self.assertIn(snippet, src)
        self.assertNotIn("jest\ndrugiej przeliczalności", src)
        self.assertNotRegex(src, r"\\(?:mathbf|mathbb)\{1\}_")


if __name__ == "__main__":
    unittest.main()
