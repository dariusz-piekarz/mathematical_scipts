"""Independent finite-model and TeX regressions for measure theory chapter 16.

Finite atomic models test Hahn/Jordan, variation, density and oscillating
examples. They are not proofs for arbitrary measurable spaces.
Run: python -m unittest tools.tests.test_measure_theory_ch16 -v
"""
import itertools
import math
import random
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/measure_theory/16-miary-ze-znakiem-miary-zespolone-i-wariacja-calkowita.tex"


def subsets(n):
    return ([i for i in range(n) if (mask >> i) & 1] for mask in range(1 << n))


def partitions(items):
    items = tuple(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for partition in partitions(rest):
        yield [[first]] + [block[:] for block in partition]
        for i in range(len(partition)):
            candidate = [block[:] for block in partition]
            candidate[i].append(first)
            yield candidate


def partition_variation(weights):
    return max(
        sum(abs(sum(weights[i] for i in block)) for block in partition)
        for partition in partitions(range(len(weights)))
    )


class TestMeasureTheoryChapter16(unittest.TestCase):
    def test_hahn_jordan_atomic_extrema(self):
        rng = random.Random(16001)
        for _ in range(250):
            weights = [rng.choice([0, -3, -2, -1, 1, 2, 3]) for _ in range(5)]
            positive = [i for i, w in enumerate(weights) if w >= 0]
            negative = [i for i, w in enumerate(weights) if w < 0]
            self.assertEqual(set(positive) | set(negative), set(range(5)))
            self.assertFalse(set(positive) & set(negative))
            for part in subsets(5):
                self.assertGreaterEqual(sum(weights[i] for i in part if i in positive), 0)
                self.assertLessEqual(sum(weights[i] for i in part if i in negative), 0)
            masses = [sum(weights[i] for i in subset) for subset in subsets(5)]
            self.assertEqual(max(masses), sum(max(w, 0) for w in weights))
            self.assertEqual(min(masses), sum(min(w, 0) for w in weights))

    def test_signed_variation_all_partitions(self):
        rng = random.Random(16002)
        for _ in range(150):
            weights = [rng.randint(-5, 5) for _ in range(5)]
            self.assertEqual(partition_variation(weights), sum(abs(w) for w in weights))
            self.assertLessEqual(abs(sum(weights)), partition_variation(weights))

    def test_complex_variation_bounds_all_partitions(self):
        rng = random.Random(16003)
        for _ in range(140):
            weights = [complex(rng.randint(-4, 4), rng.randint(-4, 4)) for _ in range(5)]
            tv = partition_variation(weights)
            self.assertAlmostEqual(tv, sum(abs(z) for z in weights), places=11)
            self.assertLessEqual(tv, sum(abs(z.real) + abs(z.imag) for z in weights) + 1e-10)
            self.assertLessEqual(abs(sum(weights)), tv + 1e-10)

    def test_minimal_dominating_measure_on_every_set(self):
        rng = random.Random(16004)
        for _ in range(180):
            weights = [rng.randint(-6, 6) for _ in range(5)]
            rho = [abs(w) + rng.randrange(5) for w in weights]
            for E in subsets(len(weights)):
                signed = sum(weights[i] for i in E)
                total_variation = sum(abs(weights[i]) for i in E)
                mass_rho = sum(rho[i] for i in E)
                self.assertLessEqual(abs(signed), mass_rho)
                self.assertLessEqual(total_variation, mass_rho)

    def test_density_variation_and_dual_tests(self):
        rng = random.Random(16005)
        for _ in range(180):
            base = [rng.randrange(0, 6) / 3 for _ in range(5)]
            density = [complex(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(5)]
            atoms = [m * f for m, f in zip(base, density)]
            total_variation = sum(m * abs(f) for m, f in zip(base, density))
            self.assertAlmostEqual(partition_variation(atoms), total_variation, places=11)
            phase = [z.conjugate() / abs(z) if z else 0 for z in atoms]
            pairing = sum(p * z for p, z in zip(phase, atoms))
            self.assertAlmostEqual(pairing.real, total_variation, places=11)
            self.assertAlmostEqual(pairing.imag, 0.0, places=11)
            for E in subsets(len(atoms)):
                eta_E = sum(atoms[i] for i in E)
                self.assertLessEqual(abs(eta_E), sum(abs(atoms[i]) for i in E) + 1e-10)

    def test_completeness_truncation_example(self):
        # A countably supported measure with weights (-1)^k / 2^(k+1).
        # The total variation distance from its first n atoms is 2^(-n).
        for n in range(1, 20):
            tail = 2.0 ** (-n)
            approx = sum(2.0 ** (-(k + 1)) for k in range(n))
            self.assertAlmostEqual(approx + tail, 1.0, places=13)
            self.assertLess(tail, 1.0 / (n + 1))

    def test_oscillatory_example_interval_cancellation(self):
        # An exact primitive proves the sin(nx) integral vanishes on intervals.
        for n in (1, 2, 3, 4, 7, 13, 40, 100, 250):
            self.assertAlmostEqual((1 - math.cos(2 * math.pi * n)) / n, 0, places=11)
            self.assertEqual(4, 4 * n / n)  # integral_0^(2pi)|sin(nx)| dx
            for a, b in ((0, .35), (.1, 1.3), (1.2, 4.7), (3, 2 * math.pi)):
                integral = (math.cos(n * a) - math.cos(n * b)) / n
                self.assertLessEqual(abs(integral), 2 / n + 1e-12)

    def test_source_labels_and_key_proofs(self):
        source = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertGreaterEqual(len(labels), 20)
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack)
        refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
        self.assertFalse(set(refs) - set(labels))
        for needle in (
            r"\label{thm:hahn-16}", r"\label{thm:jordan-16}",
            r"\label{thm:complex-variation-16}", r"\label{thm:complete-measures-16}",
            r"\int_X f(x)\,\mathrm d\nu_n(x)", r"monotoniczności $|\eta|$",
        ):
            self.assertIn(needle, source)
        self.assertNotIn(r"\mathrm d\nu(x)_n", source)
        self.assertNotRegex(source, r"\\(?:mathbf|mathbb)\{1\}_")


if __name__ == "__main__":
    unittest.main()
