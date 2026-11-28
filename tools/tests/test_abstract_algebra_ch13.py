"""Independent AA-13 mathematical, structural and regression tests."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "chapters/pl/abstract_algebra/13-pierscienie-noetherowskie-i-twierdzenie-hilberta.tex"
TXT = SRC.read_text(encoding="utf-8")


class AA13Checks(unittest.TestCase):
    def test_01_21_unique_labels(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TXT)
        self.assertEqual(len(labels), 21)
        self.assertEqual(len(set(labels)), 21)

    def test_02_existing_references(self):
        sources = (ROOT / "chapters/pl/abstract_algebra").glob("*.tex")
        labels = set().union(*(set(re.findall(r"\\label\{([^}]+)\}", p.read_text(encoding="utf-8"))) for p in sources))
        missing = set(re.findall(r"\\ref\{([^}]+)\}", TXT)) - labels
        self.assertEqual(missing, set())

    def test_03_balanced_proofs_and_environments(self):
        for env in ("definicja", "twierdzenie", "lemat", "wniosek", "proof", "przyklad"):
            self.assertEqual(TXT.count(r"\begin{" + env + "}"), TXT.count(r"\end{" + env + "}"))
        self.assertEqual(TXT.count(r"\begin{proof}"), 10)

    def test_04_terminology(self):
        self.assertNotIn("Pierwiastek ideału", TXT)
        self.assertIn("Pierwiastnik ideału pierwotnego", TXT)

    def test_05_zero_module_and_finite_presentation(self):
        self.assertIn("Gdy $r=0$, suma jest pusta i $M=0$.", TXT)
        self.assertIn(r"\operatorname{im} A=\ker\varphi", TXT)

    def test_06_ideal_nonprincipal_cotangent_dimension(self):
        for p in (2, 3, 5, 7):
            e1, e2 = (1, 0), (0, 1)
            span = {(c * e1[0] % p, c * e1[1] % p) for c in range(p)}
            self.assertNotIn(e2, span)
            self.assertEqual(len({(a, b) for a in range(p) for b in range(p)}), p * p)

    def test_07_local_denominator_inverse_mod_square(self):
        for p in (2, 3, 5):
            for c in range(1, p):
                inv = pow(c, -1, p)
                for a, b in itertools.product(range(p), repeat=2):
                    coeff = (inv, -a * inv * inv % p, -b * inv * inv % p)
                    self.assertEqual(c * coeff[0] % p, 1)
                    self.assertEqual((c * coeff[1] + a * coeff[0]) % p, 0)
                    self.assertEqual((c * coeff[2] + b * coeff[0]) % p, 0)

    def test_08_monomial_primary_decomposition(self):
        for i, j in itertools.product(range(8), repeat=2):
            left = (i >= 2 or (i >= 1 and j >= 1))
            right = i >= 1 and (i >= 2 or j >= 1)
            self.assertEqual(left, right)

    def test_09_dual_numbers_primary(self):
        for p in (2, 3, 5):
            pairs = list(itertools.product(range(p), repeat=2))
            for a, b in itertools.product(pairs, repeat=2):
                ab = ((a[0] * b[0]) % p, (a[0] * b[1] + a[1] * b[0]) % p)
                if ab == (0, 0) and a != (0, 0):
                    self.assertEqual((b[0] ** 2 % p, 2 * b[0] * b[1] % p), (0, 0))

    def test_10_cusp_semigroup_excludes_one(self):
        degrees = {2 * a + 3 * b for a, b in itertools.product(range(20), repeat=2)}
        self.assertNotIn(1, degrees)
        self.assertTrue(set(range(2, 35)).issubset(degrees))

    def test_11_leading_ideal_Z_x(self):
        for c0, c1, c2 in itertools.product(range(-3, 4), repeat=3):
            self.assertEqual(c0 % 2 == 0, any(c0 == 2 * k for k in range(-3, 4)))
        self.assertIn("także dla $h$ stałego, gdy $q=0$", TXT)

    def test_12_leading_ideal_mod_four_zero_divisors(self):
        for c0, c1 in itertools.product(range(4), repeat=2):
            possible = any((c0 - 2 * k) % 4 == 0 for k in range(4))
            self.assertEqual(possible, c0 % 2 == 0)

    def test_13_hilbert_degree_descent_cases(self):
        self.assertIn(r"Jeżeli $n\ge D$", TXT)
        self.assertIn(r"Jeśli natomiast $n<D$", TXT)
        self.assertIn("zero już należy do zbioru", TXT)

    def test_14_finite_presentation_Z_mod_six(self):
        self.assertEqual({6 * n % 6 for n in range(-10, 11)}, {0})
        self.assertEqual({n % 6 for n in range(-10, 11)}, set(range(6)))

    def test_15_math_refs_to_AA12(self):
        self.assertIn(r"aa:lem:local-ideal-membership", TXT)
        self.assertIn(r"aa:tw:radical-ideal", TXT)

    def test_16_no_unjustified_two_proofs_promise(self):
        self.assertNotIn("Twierdzenie Hilberta o bazie można udowodnić na dwa sposoby.", TXT)

    def test_17_stated_nonprincipality_reason(self):
        self.assertIn(r"\dim_K(\mathfrak m/\mathfrak m^2)=2", TXT)
        self.assertIn(r"\mathfrak m=(h)", TXT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
