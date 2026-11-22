"""ALG-08: independent algebraic-surface and birational-geometry regressions.

Checks computations and source invariants; does not prove the external
Castelnuovo, cone/contraction or Zariski-decomposition theorems.
"""
import itertools
import re
import unittest
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / "chapters" / "pl"
          / "algebraic_geometry"
          / "08-geometria-biwymierna-i-modele-minimalne-powierzchni.tex")


def pairing(a, b):
    """Intersection form in the basis H,E1,E2,E3."""
    return a[0]*b[0] - sum(a[i]*b[i] for i in range(1, 4))


class ALG08Regressions(unittest.TestCase):
    def test_standard_cremona_base_points(self):
        for p in (3, 5, 7):
            roots = set()
            for x, y, z in itertools.product(range(p), repeat=3):
                if x == y == z == 0:
                    continue
                if (y*z) % p == (x*z) % p == (x*y) % p == 0:
                    triple = (x, y, z)
                    i = next(i for i, v in enumerate(triple) if v)
                    inv = pow(triple[i], -1, p)
                    roots.add(tuple(v*inv % p for v in triple))
            self.assertEqual(roots, {(1, 0, 0), (0, 1, 0), (0, 0, 1)})

    def test_cremona_is_involution_on_dense_torus(self):
        for p in (3, 5, 7, 11):
            for x, y, z in itertools.product(range(1, p), repeat=3):
                a, b, c = y*z % p, x*z % p, x*y % p
                xx, yy, zz = b*c % p, a*c % p, a*b % p
                scale = x*y*z % p
                self.assertEqual((xx, yy, zz),
                                 (scale*x % p, scale*y % p, scale*z % p))

    def test_exceptional_curves_six_and_hexagon(self):
        H = (1, 0, 0, 0)
        K = (-3, 1, 1, 1)
        E = [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
        self.assertEqual(pairing(H, H), 1)
        self.assertTrue(all(pairing(H, e) == 0 for e in E))
        for i, e in enumerate(E):
            self.assertEqual(pairing(e, e), -1)
            for j in range(i+1, 3):
                self.assertEqual(pairing(e, E[j]), 0)
        L = {}
        for i, j in itertools.combinations(range(3), 2):
            v = tuple(H[k]-E[i][k]-E[j][k] for k in range(4))
            L[(i, j)] = v
            self.assertEqual(pairing(v, v), -1)
            self.assertEqual(pairing(K, v), -1)
            for k, e in enumerate(E):
                self.assertEqual(pairing(v, e), int(k in (i, j)))
        for a, b in itertools.combinations(L.values(), 2):
            self.assertEqual(pairing(a, b), 0)
        self.assertEqual(sum(pairing(e, e) for e in E), -3)

    def test_cremona_pullback_of_target_line(self):
        H_prime = (2, -1, -1, -1)
        self.assertEqual(pairing(H_prime, H_prime), 1)
        for i, j in itertools.combinations(range(1, 4), 2):
            v = [1, 0, 0, 0]
            v[i] = v[j] = -1
            self.assertEqual(pairing(H_prime, v), 0)
        for e in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)):
            self.assertEqual(pairing(H_prime, e), 1)

    def test_hirzebruch_cone_and_canonical_intersections(self):
        for n in range(0, 35):
            def dot(a, b):
                return -n*a[0]*b[0] + a[0]*b[1] + a[1]*b[0]
            s, f, k = (1, 0), (0, 1), (-2, -n-2)
            self.assertEqual(dot(s, s), -n)
            self.assertEqual(dot(s, f), 1)
            self.assertEqual(dot(f, f), 0)
            self.assertEqual(dot(k, s), n-2)
            self.assertEqual(dot(k, f), -2)

    def test_adjunction_identifies_negative_canonical_minus_one(self):
        for csq, kc in itertools.product(range(-30, 0), repeat=2):
            if (csq + kc) % 2:
                continue
            pa = (csq + kc + 2)//2
            if pa >= 0:
                self.assertEqual((csq, kc, pa), (-1, -1, 0))

    def test_blowup_preserves_noether_sum(self):
        for r in range(0, 10):
            ksq, c2, chi = 9-r, 3+r, 1
            self.assertEqual(ksq+c2, 12*chi)
            self.assertEqual((ksq-1)+(c2+1), 12*chi)

    def test_kodaira_product_plurigenera(self):
        for g, h, m in itertools.product(range(2, 9), range(2, 9),
                                         range(2, 11)):
            curve = (2*m-1)*(g-1)
            product = curve*(2*m-1)*(h-1)
            self.assertGreater(curve, 0)
            self.assertEqual(product, (2*m-1)**2*(g-1)*(h-1))

    def test_zariski_example_H_plus_E(self):
        H, E = (1, 0, 0, 0), (0, 1, 0, 0)
        D = tuple(a+b for a, b in zip(H, E))
        self.assertEqual(pairing(D, D), 0)
        self.assertEqual(pairing(H, E), 0)
        self.assertEqual(pairing(E, E), -1)
        self.assertEqual(pairing(D, E), -1)

    def test_source_distinguishes_divisor_from_line_bundle(self):
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"[K_X]=-3H+E_1+E_2+E_3", s)
        self.assertNotIn(r"$K_X=-3H+E_1+E_2+E_3$", s)
        self.assertIn(r"\mathcal O_S(H)\cong\pi^*\mathcal O_{\PP^2}(1)", s)
        self.assertIn("nieprzechodzącej przez $p$", s)

    def test_source_standard_terminology(self):
        s = SOURCE.read_text(encoding="utf-8")
        self.assertIsNone(re.search(
            r"dywizor|chart|injektyw|tensorowanie|zwartościowan",
            s, flags=re.IGNORECASE))
        self.assertIn("iniektywność", s)
        self.assertIn("Ze wzoru Noether", s)

    def test_kodaira_and_mmp_same_base_field(self):
        src = SOURCE.read_text(encoding="utf-8")
        for label in ("def:ga8-kodaira", "st:ga8-plurigenera-blowup"):
            block = src.split(r"\label{" + label + "}", 1)[1].split(
                r"\end{", 1)[0]
            self.assertIn("charakterystyki zero", block)
            self.assertIn("nad $k$", block)
            self.assertNotIn(r"nad $\C$", block)
        mmp = src.split(r"\label{tw:ga8-surface-mmp}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn("charakterystyki zero", mmp)

    def test_castelnuovo_open_complements(self):
        src = SOURCE.read_text(encoding="utf-8")
        theorem = src.split(r"\label{tw:ga8-castelnuovo}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(r"S\setminus E", theorem)
        self.assertIn(r"S'\setminus\{p\}", theorem)

    def test_relative_picard_number_mori_fibration(self):
        src = SOURCE.read_text(encoding="utf-8")
        theorem = src.split(
            r"\label{tw:ga8-surface-contraction}", 1)[1].split(
            r"\end{twierdzenie}", 1)[0]
        self.assertIn(r"\rho(S/Y)=1", theorem)
        self.assertIn("numerycznych klas krzywych kontraktowanych", theorem)
        example = src.split(r"\label{prz:ga8-f1-two-rays}", 1)[1].split(
            r"\end{przyklad}", 1)[0]
        self.assertIn(r"\rho(S/\PP^1)=\rho(S)-\rho(\PP^1)=2-1=1", example)

    def test_canonical_class_linear_equivalence(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"K_{\mathbb F_n}\sim-2s-(n+2)f", src)
        self.assertIn(r"K_S\sim-2s-3f", src)
        self.assertIn(r"K_{\widetilde S}\sim\pi^*K_S+E", src)
        self.assertNotIn(r"K_{\widetilde S}=\pi^*K_S+E", src)
        self.assertIn(r"h^0(S,\omega_S)=h^0(S',\omega_{S'})", src)

    def test_polish_coordinate_charts_and_explicit_fields(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn("W pierwszej mapie rozdmuchania", src)
        self.assertIn("W drugiej mapie kładziemy", src)
        self.assertNotIn("pierwszym mapie", src)
        self.assertNotIn("drugim mapie", src)
        for label in ("def:ga8-rational", "tw:ga8-function-fields",
                      "def:ga8-cremona", "st:ga8-hexagon",
                      "st:ga8-cremona-linear", "st:ga8-classes-blowup",
                      "st:ga8-fn-cone", "def:ga8-minus-one",
                      "def:ga8-nef", "def:ga8-minimal"):
            with self.subTest(label=label):
                statement = src.split(r"\label{" + label + "}", 1)[1].split(
                    r"\end{", 1)[0]
                self.assertIn("Niech $k$ będzie ciałem", statement)

    def test_source_figure_proof_and_environment_balance(self):
        s = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(s.count(r"\begin{tikzpicture}"), 4)
        self.assertEqual(s.count(r"\end{tikzpicture}"), 4)
        self.assertEqual(s.count(r"\begin{proof}"), s.count(r"\end{proof}"))
        stack = []
        for match in re.finditer(r"\\(begin|end)\{([a-zA-Z*]+)\}", s):
            if match[1] == "begin":
                stack.append(match[2])
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), match[2])
        self.assertFalse(stack)

    def test_unique_labels_and_key_results(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertGreaterEqual(len(labels), 35)
        for label in (
            "st:ga8-cremona-basic", "st:ga8-hexagon",
            "st:ga8-fn-cone", "tw:ga8-negative-implies-minusone",
            "tw:ga8-surface-mmp", "tw:ga8-zariski-decomposition",
        ):
            self.assertIn(label, labels)


if __name__ == "__main__":
    unittest.main()
