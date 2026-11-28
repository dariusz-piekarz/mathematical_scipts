"""AA-40 audit I — mathematical regression, examples, and TeX structure.

Run: python -m unittest /mnt/data/AA-40-audyt-I-testy.py -v
Repo: AA40_SOURCE=chapters/pl/abstract_algebra/40-calokowitosc-i-idealy-pierwsze.tex python ...
"""
from __future__ import annotations
import os
import re
import unittest
from pathlib import Path
from itertools import product
import sympy as sp

X,T=sp.symbols('X T')


def source_text():
    explicit=os.getenv('AA40_SOURCE')
    candidates=[explicit] if explicit else [
        str(Path(__file__).with_name('AA-40-audyt-I-zrodlo.tex')),
        'chapters/pl/abstract_algebra/40-calokowitosc-i-twierdzenia-o-idealach-pierwszych.tex',
        '/mnt/data/AA-40-audyt-I-zrodlo.tex',
    ]
    for c in candidates:
        if c and Path(c).exists():
            return Path(c).read_text(encoding='utf8')
    raise FileNotFoundError(candidates)


class SourceIntegrity(unittest.TestCase):
    def test_all_labels_unique(self):
        text=source_text();labels=re.findall(r'\\label\{([^}]+)\}',text)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),23)
    def test_internal_refs_resolve(self):
        text=source_text(); labels=set(re.findall(r'\\label\{([^}]+)\}',text))
        external={'aa:tw:krull-localization-primes','aa:tw:krull-pid',
                  'aa:lem:noether-monic','aa:tw:noether-normalization',
                  'aa:wn:noether-dimension','aa:ch:noether-normalization'}
        refs=set(re.findall(r'\\ref\{([^}]+)\}',text))
        self.assertFalse(refs-labels-external,refs-labels-external)
    def test_environment_balances(self):
        text=source_text()
        begins=re.findall(r'\\begin\{([^}]+)\}',text)
        ends=re.findall(r'\\end\{([^}]+)\}',text)
        self.assertEqual(sorted(begins),sorted(ends))
        self.assertEqual(len(re.findall(r'\\begin\{proof\}',text)),11)
    def test_finite_fiber_hypotheses_and_proof(self):
        text=source_text()
        for term in ['aa:tw:integral-finite-fibers',r'\kappa(\mathfrak p)',
                     r'\mathfrak p B',r'\dim_{\kappa(\mathfrak p)}C\le m',
                     'Chińskie twierdzenie o resztach']:
            self.assertIn(term,text)
    def test_gaussian_ramification(self):
        text=source_text()
        for term in ['aa:prz:integral-gaussian-two',r'(2)=\mathfrak q^2',
                     r'\varepsilon^2=0',r'\mathbb F_2[T]/((T+1)^2)']:
            self.assertIn(term,text)
    def test_no_circular_dependency_dimension(self):
        text=source_text()
        first=text.index(r'\label{aa:cor:integral-dimension}')
        second=text.index(r'\label{aa:tw:polynomial-krull-dimension}')
        self.assertLess(first,second)
        self.assertIn(r'\label{aa:tw:integral-lying-over}',text)


class GaussianIntegerCalculations(unittest.TestCase):
    pass


def test_gaussian(a,b):
    def run(self):
        # Multiplication by a+bi on the Z-basis 1,i has characteristic polynomial.
        M=sp.Matrix([[a,-b],[b,a]])
        char=sp.expand((T*sp.eye(2)-M).det())
        rhs=T**2-2*a*T+(a*a+b*b)
        self.assertEqual(sp.expand(char-rhs),0)
        self.assertEqual(M*M-2*a*M+(a*a+b*b)*sp.eye(2),sp.zeros(2))
    return run

for a,b in product(range(-3,4),repeat=2):
    setattr(GaussianIntegerCalculations,f'test_norm_a{a:+d}_b{b:+d}'.replace('+','p').replace('-','m'),test_gaussian(a,b))


class FibersOfZGaussian(unittest.TestCase):
    pass


def gaussian_fiber(p):
    def run(self):
        f=sp.Poly(T*T+1,T,modulus=p)
        _,factors=f.factor_list()
        # Fp[T]/(f) has one prime for each distinct irreducible factor.
        self.assertLessEqual(len(factors),2)
        expected=1 if p==2 or p%4==3 else 2
        self.assertEqual(len(factors),expected)
        if p==2:
            self.assertEqual(len(factors),1)
            g,e=factors[0]
            self.assertEqual(e,2)
            self.assertEqual(g.degree(),1)
        else:
            self.assertTrue(all(e==1 for g,e in factors))
    return run

for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
    setattr(FibersOfZGaussian,f'test_prime_{p}',gaussian_fiber(p))


class FiniteDimensionalFibers(unittest.TestCase):
    pass


def finite_fiber(p,coeff):
    def run(self):
        f=sp.Poly(sum(c*T**i for i,c in enumerate(coeff)) + T**len(coeff),T,modulus=p)
        _,factors=f.factor_list()
        self.assertTrue(factors)
        self.assertLessEqual(len(factors),f.degree())
        self.assertEqual(sum(g.degree()*e for g,e in factors),f.degree())
        for g,e in factors:
            self.assertGreaterEqual(e,1)
            self.assertGreaterEqual(g.degree(),1)
    return run

for p in [2,3,5,7]:
    for deg in [1,2,3,4]:
        coeff=tuple((i*i+2*i+p+deg)%p for i in range(deg))
        setattr(FiniteDimensionalFibers,f'test_p{p}_degree{deg}',finite_fiber(p,coeff))


class CuspIntegralExtension(unittest.TestCase):
    pass


def cusp_case(n):
    def run(self):
        # Semigroup of exponents in k[t^2,t^3] is {0} union {m>=2}.
        self.assertGreaterEqual(n,2)
        if n%2==0:
            a,b=n//2,0
        else:
            a,b=(n-3)//2,1
        self.assertGreaterEqual(a,0)
        self.assertEqual(2*a+3*b,n)
        self.assertNotEqual(n,1)
    return run

for n in range(2,42):
    setattr(CuspIntegralExtension,f'test_monomial_t_{n}',cusp_case(n))


if __name__=='__main__':
    unittest.main(verbosity=2)
