"""ALG-09: analytification, GAGA, Chow, Kähler and Hodge regressions.

Checks source integrity and independent elementary calculations; the
external GAGA, Chow, Cartan, Kodaira, Hodge and Lefschetz theorems are
not proved by these tests.
"""
import itertools
import re
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "09-geometria-algebraiczna-a-analiza-zespolona-analityfikacja-chow.tex")


class ALG09Regressions(unittest.TestCase):
    def test_cech_p1_cohomology_and_euler_characteristic(self):
        for n in range(-100, 101):
            h0 = max(n+1, 0)
            h1 = max(-n-1, 0)
            self.assertEqual(h0-h1, n+1)
            self.assertEqual(h1, max(-(n+2)+1, 0))

    def test_cech_p1_laurent_exponents(self):
        for n in range(-20, 21):
            missing = tuple(j for j in range(n+1, 0) if n+1 <= j <= -1)
            # Nonzero H1 classes are z^(n+1), ..., z^(-1).
            expected = tuple(range(n+1, 0)) if n <= -2 else ()
            self.assertEqual(missing, expected)
            self.assertEqual(len(expected), max(-n-1, 0))

    def test_serre_duality_p1_twists(self):
        for n in range(-30, 31):
            h1n = max(-n-1, 0)
            h0dual = max((-n-2)+1, 0)
            self.assertEqual(h1n, h0dual)

    def test_fubini_study_normalized_integral(self):
        # Integral over disc radius R is R^2/(1+R^2).
        for R in range(1, 101):
            value = Fraction(R*R, 1+R*R)
            self.assertGreater(value, 0)
            self.assertLess(value, 1)
            self.assertLess(1-value, Fraction(1, R*R))
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\int_{\PP^1(\C)}\omega_{\rm FS}", src)
        self.assertIn(r"=1.", src)

    def test_fubini_study_positive_hermitian_form(self):
        for z1, z2, v1, v2 in itertools.product(range(-2, 3), repeat=4):
            if v1 == v2 == 0:
                continue
            A = 1 + z1*z1 + z2*z2
            numerator = A*(v1*v1+v2*v2) - (z1*v1+z2*v2)**2
            self.assertGreaterEqual(numerator, v1*v1+v2*v2)
            self.assertGreater(numerator, 0)

    def test_plane_curve_adjunction_and_genus(self):
        for d in range(1, 100):
            g = (d-1)*(d-2)//2
            self.assertEqual(2*g-2, d*(d-3))
            self.assertGreaterEqual(g, 0)

    def test_hodge_symmetry_makes_odd_betti_even(self):
        for degree in range(1, 30, 2):
            dimensions = {(p, degree-p): ((p*7+degree)%11)
                          for p in range(degree+1)}
            for p in range(degree+1):
                q = degree-p
                if p < q:
                    dimensions[q, p] = dimensions[p, q]
            self.assertEqual(sum(dimensions.values()) % 2, 0)

    def test_stein_vs_affine_global_functions(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\C[z]", src)
        self.assertIn(r"e^z", src)
        self.assertIn("Steinowskie", src)
        self.assertIn(r"\mathbb G_m", src)

    def test_analytification_has_morphism_of_ringed_spaces(self):
        src = SOURCE.read_text(encoding="utf-8")
        block = src.split(r"\begin{definicja}[Analityfikacja]", 1)[1].split(
            r"\end{definicja}", 1)[0]
        self.assertIn(r"a:X^{\rm an}\to X", block)
        self.assertIn(r"a^{-1}\mathcal O_X\to\mathcal O_{X^{\rm an}}", block)
        self.assertIn(r"X(\C)", block)

    def test_chow_and_gaga_hypotheses(self):
        src = SOURCE.read_text(encoding="utf-8")
        chow = src.split(r"\label{tw:ga9-chow}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        gaga = src.split(r"\label{tw:ga9-gaga}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(r"$n\ge0$", chow)
        self.assertIn("zamkniętym", chow)
        self.assertIn("schematem właściwym", gaga)
        self.assertIn(r"\operatorname{Coh}(X)", gaga)

    def test_plane_curve_adjunction_has_correct_bundle_types(self):
        src = SOURCE.read_text(encoding="utf-8")
        proof = src.split(r"\section{Rachunek łączący stopień", 1)[1].split(
            r"\end{proof}", 1)[0]
        self.assertIn(r"\omega_C\cong", proof)
        self.assertIn(r"\omega_{\PP^2}\cong\mathcal O_{\PP^2}(-3)", proof)
        self.assertNotIn(r"K_C=(K_{\PP^2}+C)|_C\cong", proof)

    def test_source_terminology_and_crossrefs(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIsNone(re.search(
            r"dywizor|chart|injekc|tensorowanie|zwartościowan|sekwencyjn",
            src, re.IGNORECASE))
        labels = re.findall(r"\\label\{([^}]+)\}", src)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertGreaterEqual(len(labels), 25)

    def test_tikz_and_environment_balance(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(src.count(r"\begin{tikzpicture}"), 2)
        self.assertEqual(src.count(r"\end{tikzpicture}"), 2)
        stack = []
        for m in re.finditer(r"\\(begin|end)\{([a-zA-Z*]+)\}", src):
            if m[1] == "begin":
                stack.append(m[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), m[2])
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
