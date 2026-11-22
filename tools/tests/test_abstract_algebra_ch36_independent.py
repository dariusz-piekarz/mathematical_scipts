"""Independent AA-36 stabilization checks: algebra, group action, examples, LaTeX.
Not a replacement for mathematical proofs of generic Galois statements.
Run: python -m unittest tools.tests.test_abstract_algebra_ch36_independent -v
"""
import itertools
import math
import os
from pathlib import Path
import re
import unittest

import sympy as sp
from sympy.combinatorics.named_groups import AlternatingGroup, SymmetricGroup

SOURCE = Path(os.getenv('AA36_SOURCE', str(Path(__file__).resolve().parents[2] /
    'chapters/pl/abstract_algebra/36-wielomian-ogolny-i-grupy-symetryczne.tex')))
TEX = SOURCE.read_text(encoding='utf-8')


def elem(xs, k):
    return sum((math.prod(combo) for combo in itertools.combinations(xs, k)), 0)


class IndependentAA36(unittest.TestCase):
    def test_text_requires_A5_instead_of_unproven_An(self):
        self.assertIn('\\ref{aa:wn:a5-not-solvable}', TEX)
        self.assertIn('zawiera podgrupę izomorficzną', TEX)
        self.assertNotIn('grupa $A_n$ jest prosta', TEX)

    def test_generic_main_theorem_hypotheses(self):
        self.assertIn('Dla każdego ciała $k$', TEX)
        self.assertIn('\\label{aa:tw:generic-sn}', TEX)
        self.assertIn('jest nierozkładalny', TEX)
        self.assertIn('jest izomorficzna z grupą symetryczną $S_n$', TEX)

    def test_char_independence_observation(self):
        self.assertIn('dzielenia przez $n!$', TEX)
        self.assertIn('również w dodatniej charakterystyce', TEX)

    def test_main_proof_four_steps(self):
        self.assertEqual(TEX.count('\\emph{Krok '), 4)
        self.assertIn('$L=K(x_1,\\ldots,x_n)$', TEX)

    def test_inseparable_specialization_scope(self):
        self.assertIn('t_1=\\cdots=t_{p-1}=0',TEX)
        self.assertIn('t_p=t',TEX)
        self.assertIn('trywialna',TEX)

    def test_labels_unique_and_count(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEX)
        self.assertEqual(len(labels),12)
        self.assertEqual(len(labels),len(set(labels)))

    def test_internal_references_all_exist(self):
        labels=set(re.findall(r'\\label\{([^}]+)\}',TEX))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',TEX))
        external={'aa:wn:a5-not-solvable','aa:tw:fundamental-symmetric',
                  'aa:ch:radicals','aa:tw:fundamental-galois','aa:prz:quartic-v4'}
        self.assertEqual(refs-labels,external)

    def test_theorem_environment_integrity(self):
        for kind in ['twierdzenie','wniosek','lemat','definicja','przyklad','uwaga','proof']:
            self.assertEqual(TEX.count('\\begin{'+kind+'}'), TEX.count('\\end{'+kind+'}'))
        self.assertEqual(TEX.count('\\begin{proof}'),4)
        self.assertEqual(TEX.count('\\begin{przyklad}'),5)

    def test_discriminant_cubic_symbolic(self):
        x=sp.symbols('x0:3')
        e1,e2,e3=(elem(x,k) for k in (1,2,3))
        d=e1**2*e2**2-4*e2**3-4*e1**3*e3-27*e3**2+18*e1*e2*e3
        v=math.prod((x[i]-x[j])**2 for i in range(3) for j in range(i+1,3))
        self.assertEqual(sp.expand(d-v),0)

    def test_basic_cubic_specializations(self):
        x=sp.Symbol('x')
        self.assertTrue(sp.Poly(x**3-2,x).is_irreducible)
        self.assertTrue(sp.Poly(x**3-3*x+1,x).is_irreducible)
        self.assertEqual(sp.discriminant(x**3-2,x),-108)
        self.assertEqual(sp.discriminant(x**3-3*x+1,x),81)

    def test_quartic_specialization(self):
        x=sp.Symbol('x')
        self.assertTrue(sp.Poly(x**4-2,x).is_irreducible)
        self.assertEqual(sp.discriminant(x**4-2,x),-2048)

    def test_A5_derived_group_is_whole(self):
        a=AlternatingGroup(5)
        self.assertEqual(a.order(),60)
        self.assertEqual(a.derived_subgroup().order(),a.order())

    def test_distinct_generators_of_L(self):
        for n in range(2,7):
            xs=sp.symbols('x1:'+str(n+1))
            self.assertEqual(len(set(xs)),n)

# Independently generated parameterized checks.
for n in range(2,6):
    def poly_factorization(self, n=n):
        xx=sp.symbols('x1:'+str(n+1)); X=sp.Symbol('X')
        expected=sp.expand(sp.prod(X-z for z in xx))
        actual=sp.expand(X**n+sum((-1)**j*elem(xx,j)*X**(n-j) for j in range(1,n+1)))
        self.assertEqual(expected,actual)
    setattr(IndependentAA36,f'test_generic_factorization_degree_{n}',poly_factorization)

for n in range(2,7):
    def symmetric_invariance(self,n=n):
        xs=sp.symbols('x1:'+str(n+1))
        permutations=list(itertools.permutations(xs)) if n<=4 else [xs, xs[::-1], xs[1:]+xs[:1]]
        for pi in permutations:
            for k in range(1,n+1):
                self.assertEqual(sp.expand(elem(xs,k)-elem(pi,k)),0)
    setattr(IndependentAA36,f'test_invariance_degree_{n}',symmetric_invariance)

for p in (2,3,5,7,11):
    def finite_field_vieta(self,p=p):
        for n in range(2,6):
            roots=[(i*i+4*i+1)%p for i in range(n)]
            coefficients=[1]+[((-1)**j*elem(roots,j))%p for j in range(1,n+1)]
            X=sp.Symbol('X')
            expanded=[int(v)%p for v in sp.Poly(sp.prod(X-z for z in roots),X).all_coeffs()]
            self.assertEqual(coefficients,expanded)
    setattr(IndependentAA36,f'test_finite_field_vieta_p_{p}',finite_field_vieta)

for p in (2,3,5,7,11,13):
    def characteristic_discriminant(self,p=p):
        for roots in itertools.product(range(min(p,4)), repeat=3):
            e1,e2,e3=(elem(roots,j) for j in (1,2,3))
            d=e1**2*e2**2-4*e2**3-4*e1**3*e3-27*e3**2+18*e1*e2*e3
            v=math.prod((roots[i]-roots[j])**2 for i in range(3) for j in range(i+1,3))
            self.assertEqual((d-v)%p,0)
    setattr(IndependentAA36,f'test_discriminant_characteristic_{p}',characteristic_discriminant)

for n in range(5,10):
    def embedding_a5(self,n=n):
        group=SymmetricGroup(n)
        self.assertEqual(group.order(),math.factorial(n))
        # Even permutations of the first five indices, fixing the rest.
        perms=[perm for perm in itertools.permutations(range(5)) if 
               sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))%2==0]
        images={perm+tuple(range(5,n)) for perm in perms}
        self.assertEqual(len(images),60)
        self.assertEqual(AlternatingGroup(5).order(),len(images))
    setattr(IndependentAA36,f'test_A5_embeds_S_{n}',embedding_a5)

for p in (2,3,5,7):
    def inseparable(self,p=p):
        x,t=sp.symbols('x t')
        F=x**p-t
        self.assertTrue(all(math.comb(p,j)%p==0 for j in range(1,p)))
        self.assertEqual(sp.Poly(F,x).degree(),p)
        self.assertEqual(sp.Poly(F,x).LC(),1)
        self.assertEqual(sp.Poly(F,x).TC(),-t)
    setattr(IndependentAA36,f'test_purely_inseparable_{p}',inseparable)

if __name__=='__main__':
    unittest.main()
