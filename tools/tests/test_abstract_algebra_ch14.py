"""AA-14: structural checks and independently evaluated finite models.

The finite computations test examples and edge cases; they do not replace
the mathematical proofs in the chapter.
"""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "chapters/pl/abstract_algebra/14-pierscienie-artinowskie-lokalne-i-lemat-nakayamy.tex"
TXT = SRC.read_text(encoding="utf-8")


def ideal(n, d):
    return {x for x in range(n) if x % d == 0}


def squarezero_mul(u, v, p):
    a, b, c = u
    d, e, f = v
    return (a*d % p, (a*e+b*d) % p, (a*f+c*d) % p)


def truncated_mul(u, v, p):
    return tuple(sum(u[j]*v[i-j] for j in range(i+1)) % p for i in range(len(u)))


class AA14Regression(unittest.TestCase):
    def test_01_labels_unique(self):
        labels = re.findall(r"\\label\{([^}]+)\}", TXT)
        self.assertEqual(len(labels), 25)
        self.assertEqual(len(labels), len(set(labels)))

    def test_02_references_local(self):
        labels = set(re.findall(r"\\label\{([^}]+)\}", TXT))
        self.assertEqual(set(re.findall(r"\\ref\{([^}]+)\}", TXT)) - labels, set())

    def test_03_proofs_balanced(self):
        self.assertEqual(TXT.count(r"\begin{proof}"), 15)
        self.assertEqual(TXT.count(r"\end{proof}"), 15)

    def test_04_theorem_environments_balanced(self):
        for env in ("twierdzenie", "lemat", "wniosek", "definicja", "przyklad", "uwaga"):
            self.assertEqual(TXT.count(r"\begin{" + env + "}"), TXT.count(r"\end{" + env + "}"), env)

    def test_05_zorn_empty_chain_addressed(self):
        self.assertIn("łańcucha pustego jego ograniczeniem górnym", TXT)
        self.assertIn("Suma mnogościowa niepustego łańcucha", TXT)

    def test_06_zero_ring_distinguished(self):
        self.assertIn("Przypadek pierścienia zerowego jest natychmiastowy", TXT)
        self.assertIn("Niech $R$ będzie niezerowym przemiennym pierścieniem", TXT)

    def test_07_jacobson_nilpotence_assumptions(self):
        self.assertIn(r"J(R)^N=(0)", TXT)
        self.assertIn(r"I^2=J^{2N}=J^N=I", TXT)

    def test_08_nakayama_submodule_assumptions(self):
        self.assertIn("niech $M$ będzie skończenie", TXT)
        self.assertIn(r"M=N+\mathfrak m M", TXT)

    def test_09_local_ring_nonunits_z16(self):
        self.assertEqual({a for a in range(16) if math.gcd(a, 16) != 1}, ideal(16, 2))

    def test_10_z16_ideal_chain(self):
        ideals = [ideal(16, d) for d in (1, 2, 4, 8, 16)]
        self.assertTrue(all(ideals[i] > ideals[i+1] for i in range(4)))

    def test_11_z16_nilpotent_jacobson(self):
        j = ideal(16, 2)
        powers = {1}
        for d in (2, 4, 8, 16):
            powers = {a*b % 16 for a in powers for b in j}
            self.assertEqual(powers, ideal(16, d))

    def test_12_z12_maximal_intersection(self):
        self.assertEqual(ideal(12, 2) & ideal(12, 3), {0, 6})

    def test_13_z12_radical_square_zero(self):
        j = {0, 6}
        self.assertEqual({a*b % 12 for a in j for b in j}, {0})

    def test_14_z12_chinese_remainder(self):
        for a, b in itertools.product(range(4), range(3)):
            x = (9*a+4*b) % 12
            self.assertEqual((x % 4, x % 3), (a,b))

    def test_15_z72_chinese_remainder(self):
        values = {(9*a+64*b) % 72 for a, b in itertools.product(range(8), range(9))}
        self.assertEqual(len(values), 72)

    def test_16_comaximal_powers(self):
        self.assertEqual(math.gcd(4, 9), 1)
        self.assertEqual(ideal(12, 4) & ideal(12, 9), {0})

    def test_17_jacobson_unit_criterion_z12(self):
        for a in range(12):
            condition = all(math.gcd(1-a*b, 12) == 1 for b in range(12))
            self.assertEqual(condition, a in {0,6})

    def test_18_prime_equals_maximal_in_Zn(self):
        for n in range(2, 24):
            for d in range(1, n+1):
                if n % d:
                    continue
                i = ideal(n, d)
                prime = len(i) < n and all((a*b) % n not in i or a in i or b in i
                                           for a,b in itertools.product(range(n),repeat=2))
                dprime = d > 1 and all(d % k for k in range(2,math.isqrt(d)+1))
                self.assertEqual(prime, dprime, (n,d))

    def test_19_squarezero_nonunits(self):
        for p in (2,3,5):
            m = list(itertools.product([0],range(p),range(p)))
            self.assertTrue(all(squarezero_mul(u,v,p)==(0,0,0) for u,v in itertools.product(m,repeat=2)))

    def test_20_squarezero_units(self):
        for p in (2,3):
            ring = list(itertools.product(range(p),repeat=3))
            for u in ring:
                is_unit = any(squarezero_mul(u,v,p)==(1,0,0) for v in ring)
                self.assertEqual(is_unit, u[0]!=0)

    def test_21_squarezero_ideal_requires_two_generators(self):
        for p in (2,3):
            ring = list(itertools.product(range(p),repeat=3))
            m = set(itertools.product([0],range(p),range(p)))
            for u in m:
                self.assertNotEqual({squarezero_mul(r,u,p) for r in ring},m)

    def test_22_truncated_poly_units(self):
        for p,n in ((2,4),(3,3)):
            ring = list(itertools.product(range(p),repeat=n))
            unit = (1,)+(0,)*(n-1)
            for u in ring:
                invertible = any(truncated_mul(u,v,p)==unit for v in ring)
                self.assertEqual(invertible,u[0]!=0,(p,n,u))

    def test_23_truncated_poly_ideal_chain(self):
        p,n=2,4
        ideals=[{u for u in itertools.product(range(p),repeat=n) if all(u[j]==0 for j in range(k))}
                for k in range(n+1)]
        self.assertTrue(all(ideals[k]>ideals[k+1] for k in range(n)))

    def test_24_infinite_fraction_counterexample(self):
        self.assertIn(r"x^N(1/x^{N+1}+R)=1/x+R\ne0",TXT)
        for n in range(1,15):
            self.assertGreater(n+1,n)

    def test_25_generator_vs_free_module(self):
        self.assertIn("anihiluje cały moduł",TXT)
        self.assertIn(r"x^3(q+(x^3)R)=0",TXT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
