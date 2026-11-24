"""AA-X30: Euler units, Galois fixed fields and cyclotomic composita.

Finite exact regression examples; general field-theoretic statements
are proved independently in the associated mathematical audit.
"""
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path
import unittest

import sympy as sp


@lru_cache(None)
def units(n):
    assert n >= 1
    return tuple(k for k in range(n) if gcd(k, n) == 1)


@lru_cache(None)
def phi(n):
    return len(units(n))


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    d, s, t = egcd(b, a % b)
    return d, t, s - (a // b) * t


def kernel(n, d):
    """Kernel (Z/nZ)^* -> (Z/dZ)^*, for d|n, including d=1."""
    assert n % d == 0
    return {k for k in units(n) if k % d == 1 % d}


def product_subgroups(n, a, b):
    return {(x*y) % n for x in a for y in b}


def element_order(n, k):
    if n == 1:
        return 1
    assert k in units(n)
    y = k % n
    count = 1
    while y != 1 % n:
        y = y*k % n
        count += 1
        assert count <= phi(n)
    return count


class CyclotomicCompositumAudit(unittest.TestCase):
    def test_euler_units_and_cyclotomic_degrees(self):
        x = sp.Symbol("x")
        for n in range(1, 49):
            with self.subTest(n=n):
                f = sp.Poly(sp.cyclotomic_poly(n, x), x, domain=sp.ZZ)
                self.assertEqual(phi(n), int(sp.totient(n)))
                self.assertEqual(f.degree(), phi(n))
                self.assertEqual(f.LC(), 1)
                self.assertTrue(f.is_irreducible)

    def test_surjectivity_of_unit_reduction(self):
        for n in range(2, 97):
            for d in range(1, n+1):
                if n % d:
                    continue
                with self.subTest(n=n,d=d):
                    target = set(units(d))
                    actual = {k % d for k in units(n)}
                    self.assertEqual(actual, target)
                    self.assertEqual(len(kernel(n,d)), phi(n)//phi(d))

    def test_product_of_galois_kernels_matches_gcd_conductor(self):
        for m in range(1, 22):
            for n in range(1, 22):
                N, d = lcm(m,n), gcd(m,n)
                with self.subTest(m=m,n=n):
                    hm, hn, hd = kernel(N,m), kernel(N,n), kernel(N,d)
                    self.assertEqual(product_subgroups(N,hm,hn),hd)
                    self.assertEqual(hm & hn, {1 % N})
                    self.assertEqual(len(hd),len(hm)*len(hn))
                    self.assertEqual(phi(N)//len(hd), phi(d))

    def test_totient_gcd_lcm_and_field_degree_identity(self):
        for m in range(1, 76):
            for n in range(1, 76):
                N, d = lcm(m,n), gcd(m,n)
                with self.subTest(m=m,n=n):
                    self.assertEqual(phi(m)*phi(n),phi(N)*phi(d))
                    self.assertEqual(phi(N)*phi(d),phi(m)*phi(n))

    def test_bezout_generates_primitive_lcm_root(self):
        for m in range(1, 76):
            for n in range(1, 76):
                N = lcm(m,n)
                a,b = N//m, N//n
                g,s,t = egcd(a,b)
                with self.subTest(m=m,n=n):
                    self.assertEqual(g,1)
                    self.assertEqual((s*a+t*b) % N,1 % N)
                    # Powers of a primitive N-th root have exact orders m,n.
                    self.assertEqual(N//gcd(N,a),m)
                    self.assertEqual(N//gcd(N,b),n)

    def test_selected_intersections_and_noncylcicity(self):
        cases = [(4,6,2,12),(8,12,4,24),(9,15,3,45),
                 (8,9,1,72),(5,5,5,5),(1,14,1,14)]
        for m,n,d,N in cases:
            with self.subTest(m=m,n=n):
                self.assertEqual(gcd(m,n),d)
                self.assertEqual(lcm(m,n),N)
                self.assertEqual(phi(N)*phi(d),phi(m)*phi(n))
                self.assertEqual(len(product_subgroups(N,kernel(N,m),kernel(N,n))),
                                 phi(N)//phi(d))
        self.assertEqual({element_order(8,k) for k in units(8)},{1,2})
        self.assertEqual(max(element_order(5,k) for k in units(5)),4)
        self.assertEqual(set(units(8)),{1,3,5,7})

    def test_reference_integrity_and_chapter_count(self):
        base=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra"
        import json
        root = Path(__file__).resolve().parents[2]
        catalog = json.loads((root / "catalog/books.json").read_text(encoding="utf-8"))
        expected = next(book["chapters"] for book in catalog["books"]
                        if book["id"] == "abstract_algebra" and book["language"] == "pl")
        self.assertGreaterEqual(len(expected), 67)
        self.assertEqual(sorted(p.relative_to(root).as_posix() for p in list(base.glob("[0-9][0-9]-*.tex"))),
                         sorted(expected))
        names={
            2:"02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex",
            22:"22-twierdzenie-artina-i-odpowiedniosc-galois.tex",
            28:"28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex",
        }
        texts={k:(base/v).read_text(encoding="utf8") for k,v in names.items()}
        self.assertIn(r"\label{aa:tw:phi-wzor}", texts[2])
        self.assertIn(r"\label{aa:tw:euler}", texts[2])
        self.assertIn(r"\label{aa:def:fixed-field}", texts[22])
        self.assertIn(r"\label{aa:tw:cyclotomic-galois}", texts[28])
        self.assertIn(r"\label{aa:prz:cyclotomic-eight}", texts[28])


if __name__=="__main__":
    unittest.main()
