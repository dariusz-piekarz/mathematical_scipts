"""AA-X28: Hilbert 90 -> Kummer eigenvectors, traces and norms.

Exact finite-field regression checks, not proofs of the general theorems.
"""
from itertools import product
from pathlib import Path
import unittest
import sympy as sp

MODELS = ((5, 2, 2), (7, 3, 2), (5, 4, 2))


class Field:
    """F_p[t]/(t^n-a), after an explicit irreducibility test."""
    def __init__(self, p, n, a):
        self.p, self.n, self.a = p, n, a
        t = sp.Symbol("t")
        assert sp.Poly(t**n-a, t, modulus=p).is_irreducible
        self.zero = (0,)*n
        self.one = (1,)+(0,)*(n-1)
        self.alpha = (0, 1)+(0,)*(n-2)

    def elements(self):
        return product(range(self.p), repeat=self.n)

    def scalar(self, k):
        return (k%self.p,)+(0,)*(self.n-1)

    def add(self, x, y):
        return tuple((u+v)%self.p for u,v in zip(x,y))

    def mul(self, x, y):
        t = [0]*(2*self.n-1)
        for i,u in enumerate(x):
            for j,v in enumerate(y):
                t[i+j] += u*v
        for k in range(2*self.n-2, self.n-1, -1):
            t[k-self.n] += self.a*t[k]
        return tuple(z%self.p for z in t[:self.n])

    def power(self, x, k):
        if k < 0:
            if x == self.zero:
                raise ZeroDivisionError
            x = self.power(x, self.p**self.n-2)
            k = -k
        z = self.one
        while k:
            if k & 1:
                z = self.mul(z,x)
            x = self.mul(x,x)
            k >>= 1
        return z

    def sigma(self, x):
        return self.power(x,self.p)

    def trace(self, x):
        z = self.zero
        for _ in range(self.n):
            z = self.add(z,x)
            x = self.sigma(x)
        return z

    def norm(self, x):
        z = self.one
        for _ in range(self.n):
            z = self.mul(z,x)
            x = self.sigma(x)
        return z


class TestAA28HilbertKummer(unittest.TestCase):
    def test_frobenius_and_primitive_eigenvalue(self):
        for p,n,a in MODELS:
            with self.subTest(p=p,n=n):
                f = Field(p,n,a)
                zeta = f.power(f.alpha,p-1)
                self.assertEqual(f.sigma(f.alpha),f.mul(zeta,f.alpha))
                self.assertEqual(f.power(zeta,n),f.one)
                for k in range(1,n):
                    self.assertNotEqual(f.power(zeta,k),f.one)
                self.assertEqual(f.power(f.alpha,n),f.scalar(a))
                for b in f.elements():
                    self.assertEqual(f.power(b,p**n),b)

    def test_hilbert90_norm_one_equals_ratio_image(self):
        for p,n,a in MODELS:
            with self.subTest(p=p,n=n):
                f = Field(p,n,a)
                image = {f.mul(b,f.power(f.sigma(b),-1))
                         for b in f.elements() if b != f.zero}
                kernel = {b for b in f.elements() if f.norm(b)==f.one}
                self.assertEqual(image,kernel)
                self.assertEqual(len(kernel),(p**n-1)//(p-1))

    def test_hilbert90_witness_and_one_dimensional_eigenspace(self):
        for p,n,a in MODELS:
            with self.subTest(p=p,n=n):
                f = Field(p,n,a)
                zeta = f.power(f.alpha,p-1)
                c = f.power(zeta,-1)
                self.assertEqual(f.norm(c),f.one)
                witnesses = {b for b in f.elements() if b != f.zero
                             and f.mul(b,f.power(f.sigma(b),-1))==c}
                expected = {f.mul(f.scalar(k),f.alpha) for k in range(1,p)}
                self.assertEqual(witnesses,expected)

    def test_generator_norm_and_trace(self):
        for p,n,a in MODELS:
            with self.subTest(p=p,n=n):
                f = Field(p,n,a)
                self.assertEqual(f.norm(f.alpha),f.scalar((-1)**(n-1)*a))
                self.assertEqual(f.trace(f.one),f.scalar(n))
                for j in range(1,n):
                    self.assertEqual(f.trace(f.power(f.alpha,j)),f.zero)

    def test_nonprimitive_eigenvalue_does_not_generate_full_field(self):
        f = Field(5,4,2)
        zeta = f.scalar(-1)   # order 2, not 4
        self.assertEqual(f.power(zeta,2),f.one)
        witnesses = [b for b in f.elements() if b != f.zero
                     and f.sigma(b)==f.mul(zeta,b)]
        self.assertEqual(len(witnesses),4)
        for b in witnesses:
            self.assertEqual(f.sigma(f.sigma(b)),b)
            self.assertNotEqual(f.sigma(b),b)
            square = f.power(b,2)
            self.assertEqual(square,f.scalar(square[0]))

    def test_chapter_inventory_and_stable_labels(self):
        root = Path(__file__).resolve().parents[2]
        base = root/"chapters/pl/abstract_algebra"
        self.assertEqual(len(list(base.glob("[0-9][0-9]-*.tex"))),56)
        ch25 = (base/"25-twierdzenie-hilberta-90-i-rownania-normowe.tex").read_text(encoding="utf-8")
        ch26 = (base/"26-rozszerzenia-cykliczne-i-teoria-kummera.tex").read_text(encoding="utf-8")
        self.assertIn(r"\label{aa:tw:hilbert90-multiplicative}",ch25)
        self.assertIn(r"\label{aa:tw:kummer-converse}",ch26)
        self.assertIn(r"\ref{aa:lem:dedekind-independent}",ch26)


if __name__ == "__main__":
    unittest.main()
