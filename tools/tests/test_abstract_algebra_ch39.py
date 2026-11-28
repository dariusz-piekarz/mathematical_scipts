"""AA-39 audit I: structural, modular, elimination, product-ring checks.

Run:
    AA39_SOURCE=/path/to/file.tex python -m unittest AA-39-audyt-I-testy.py -v
As installed in a repository:
    python -m unittest tools.tests.test_abstract_algebra_ch39 -v
These finite computations are regression checks, not proofs of arbitrary-field statements.
"""
from __future__ import annotations
import os
import re
import math
import unittest
from pathlib import Path
import sympy as sp

CURRENT = Path(__file__).resolve()
REPO_SOURCE = CURRENT.parents[2] / "chapters/pl/abstract_algebra/39-wymiar-krulla-i-lancuchy-idealow-pierwszych.tex" if len(CURRENT.parents) > 2 else None
SOURCE = Path(os.environ.get("AA39_SOURCE", str(REPO_SOURCE if REPO_SOURCE and REPO_SOURCE.exists() else CURRENT.parent / "AA-39-audyt-I-zrodlo.tex")))
HISTORICAL = CURRENT.parent / "AA-39--wymiar-krulla-i-lancuchy-idealow-pierwszych.tex"


def latex_source():
    return SOURCE.read_text(encoding="utf-8")


class SourceChecks(unittest.TestCase):
    def test_source_exists(self):
        self.assertTrue(SOURCE.is_file())
    def test_chapter_still_labelled(self):
        self.assertIn(r"\label{aa:ch:krull-dimension}", latex_source())
    def test_unique_labels(self):
        labels = re.findall(r"\\label\{([^}]+)\}", latex_source())
        self.assertEqual(len(labels), len(set(labels)))
    def test_all_original_labels_preserved(self):
        if HISTORICAL.exists():
            old = set(re.findall(r"\\label\{([^}]+)\}", HISTORICAL.read_text(encoding="utf-8")))
            new = set(re.findall(r"\\label\{([^}]+)\}", latex_source()))
            self.assertFalse(old-new, old-new)
        else:
            self.assertIn(r"\label{aa:fig:crossed-lines}", latex_source())
    def test_no_forward_undefined_krull_ref(self):
        self.assertNotIn(r"\ref{aa:tw:polynomial-krull-dimension}", latex_source())
    def test_self_contained_plane_lemma(self):
        self.assertIn(r"\label{aa:lem:krull-plane-dimension}", latex_source())
        self.assertIn(r"\dim K[U,V]=2", latex_source())
    def test_zero_dimension_criterion(self):
        self.assertIn(r"\label{aa:cor:krull-dim-zero}", latex_source())
    def test_lemma_elimination_both_variables(self):
        s=latex_source()
        self.assertIn(r"h(U)\in K[U]",s)
        self.assertIn(r"k(V)\in K[V]",s)
        self.assertIn(r"R/(f,g)",s)
    def test_proofs_balanced(self):
        s=latex_source()
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        self.assertGreaterEqual(s.count(r"\begin{proof}"),10)
    def test_examples_preserved(self):
        s=latex_source()
        self.assertEqual(s.count(r"\begin{przyklad}"),7)
    def test_reference_targets_local_or_known(self):
        s=latex_source();labels=set(re.findall(r"\\label\{([^}]+)\}",s))
        refs=set(re.findall(r"\\ref\{([^}]+)\}",s))
        self.assertEqual(refs-labels,{"aa:ch:lokalizacja","aa:ch:pierscienie"})
    def test_figure_unchanged(self):
        s=latex_source()
        self.assertIn(r"\label{aa:fig:crossed-lines}",s)
        self.assertIn(r"\begin{picture}(82,43)",s)


U,V=sp.symbols("U V")
# Each pair is coprime as a pair of multivariable polynomials (possibly generates the unit ideal).
PAIRS=[
    (U,V),
    (U-1,V+1),
    (U+V,U+V+1),
    (U+V,U-V-1),
    (U*V-1,U),
    (U*V-1,U+V),
    (V**2-U,U**2-V),
    (U**2+V,V**2+U),
    (U+V**2,V+1),
    (U*V+U+1,U+V+1),
    (U**2+V+1,V-2),
    (U+V**3,U**2+V+1),
]
FIELDS=[None,2,3,5,7]


class EliminationChecks(unittest.TestCase):
    pass


def elimination_test(f,g,p):
    domain_args={} if p is None else {"modulus":p}
    G=sp.groebner([f,g],U,V,order="lex",**domain_args)
    # A zero-dimensional quotient is finite over the ground field.
    # The unit ideal gives the zero vector space, which is also finite.
    unit=any(v.as_expr()==1 for v in G.polys)
    if not unit and not G.is_zero_dimensional:
        raise AssertionError(f"not zero-dimensional: {f=}, {g=}, {p=}, {G=}")


for i,(f,g) in enumerate(PAIRS):
    for p in FIELDS:
        def check(self,f=f,g=g,p=p):
            elimination_test(f,g,p)
        setattr(EliminationChecks,f"test_pair_{i:02d}_char_{str(p or 0):>02}".replace(' ','0'),check)


class ModularQuotientChecks(unittest.TestCase):
    pass


def isprime_integer_ideal(n,d):
    # Ideal (d) of Z/n for d | n; prime iff d is a prime integer.
    I={x for x in range(n) if x%d==0}
    if len(I)==n:
        return False
    for a in range(n):
        for b in range(n):
            if (a*b)%n in I and not (a in I or b in I):
                return False
    return True


def modular_test(n):
    divisors=[d for d in range(1,n+1) if n%d==0]
    prime_ideals={d for d in divisors if isprime_integer_ideal(n,d)}
    expected={d for d in divisors if sp.isprime(d)}
    if prime_ideals!=expected:
        raise AssertionError(f"Z/{n}: prime ideals {prime_ideals}, expected {expected}")
    # No two different prime ideals comparable, hence Krull dimension zero.
    for x in prime_ideals:
        for y in prime_ideals:
            if x!=y and (x%y==0 or y%x==0):
                raise AssertionError(f"Comparable prime ideals in Z/{n}: {x},{y}")


for n in range(2,52):
    def test(self,n=n):
        modular_test(n)
    setattr(ModularQuotientChecks,f"test_Z_mod_{n:02d}",test)


class ProductFieldChecks(unittest.TestCase):
    pass


def product_test(p,q):
    elements=[(x,y) for x in range(p) for y in range(q)]
    zero_left={(0,y) for y in range(q)}
    zero_right={(x,0) for x in range(p)}
    def is_prime_ideal(I):
        for (a,b) in elements:
            for (c,d) in elements:
                if ((a*c)%p,(b*d)%q) in I and not ((a,b) in I or (c,d) in I):
                    return False
        return True
    assert is_prime_ideal(zero_left) and is_prime_ideal(zero_right)
    assert not (zero_left <= zero_right) and not (zero_right <= zero_left)


for p,q in [(2,2),(2,3),(2,5),(3,5),(3,7)]:
    def test(self,p=p,q=q):
        product_test(p,q)
    setattr(ProductFieldChecks,f"test_F{p}_product_F{q}",test)


class NilpotentQuotientChecks(unittest.TestCase):
    pass


def nilpotent_test(p,m):
    # F_p[T]/(T^m): any element has form a0 + ... + a_(m-1) T^(m-1).
    # An element is invertible iff its constant coefficient is nonzero.
    # Hence the only prime is (T), and Krull dimension is zero.
    basis=[tuple((int(j==i)) for j in range(m)) for i in range(m)]
    t=basis[1]
    def multiply(a,b):
        coeff=[0]*m
        for i in range(m):
            for j in range(m-i):
                coeff[i+j]=(coeff[i+j]+a[i]*b[j])%p
        return tuple(coeff)
    power=(1,)+(0,)*(m-1)
    for j in range(m):
        power=multiply(power,t)
    assert power==(0,)*m
    for k in range(1,m):
        x=(0,)*k+(1,)+(0,)*(m-k-1)
        assert x!=(0,)*m


for p in [2,3,5]:
    for m in [2,3,4]:
        def test(self,p=p,m=m):
            nilpotent_test(p,m)
        setattr(NilpotentQuotientChecks,f"test_char_{p}_nilpotence_{m}",test)

if __name__=="__main__":
    unittest.main(verbosity=2)
