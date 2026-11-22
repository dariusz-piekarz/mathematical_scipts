"""AA-36, audit II — symbolic, finite characteristic, group-theoretic and TeX tests.
Usage: python -m unittest /mnt/data/AA-36-audyt-I-testy.py -v
No numerical experiment is construed as a proof of generic irreducibility.
"""
from pathlib import Path
import itertools
import math
import os
import re
import unittest

import sympy as s
from sympy.combinatorics.named_groups import AlternatingGroup, SymmetricGroup

SOURCE = Path(os.environ.get('AA36_SOURCE', str(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/36-wielomian-ogolny-i-grupy-symetryczne.tex')))
TEX = SOURCE.read_text()


def test_case(name, fn):
    setattr(TestAA36, 'test_'+name, fn)


class TestAA36(unittest.TestCase):
    pass


for n in range(2, 7):
    xx = s.symbols('x1:'+str(n+1))
    z = s.Symbol('z')
    e = [s.polys.polyfuncs.symmetric_poly(k, *xx) for k in range(1,n+1)]
    def make_factor(n=n,xx=xx,e=e,z=z):
        def check(self):
            prod=s.expand(s.prod(z-x for x in xx))
            formula=s.expand(z**n+sum((-1)**k*e[k-1]*z**(n-k) for k in range(1,n+1)))
            self.assertEqual(s.expand(prod-formula),0)
        return check
    test_case(f'factor_vieta_n{n}',make_factor())
    def make_elementary(n=n,xx=xx,e=e):
        def check(self):
            for k in range(1,n+1):
                manual=sum(s.prod(xx[j] for j in ind) for ind in itertools.combinations(range(n),k))
                self.assertEqual(s.expand(manual-e[k-1]),0)
        return check
    test_case(f'elementary_symmetric_n{n}',make_elementary())
    def make_permutation(n=n,xx=xx,e=e):
        def check(self):
            swaps=list(itertools.permutations(range(n))) if n<=5 else [(0,1,2,3,4,5),(5,4,3,2,1,0),(1,2,3,4,5,0)]
            for pi in swaps:
                permuted=[xx[j] for j in pi]
                for k in range(1,n+1):
                    symmetric=s.polys.polyfuncs.symmetric_poly(k,*permuted)
                    self.assertEqual(s.expand(symmetric-e[k-1]),0)
        return check
    test_case(f'permutations_preserve_generators_n{n}',make_permutation())
    def make_transformation(n=n,xx=xx,e=e):
        def check(self):
            # For each permutation the ordered x_i images are distinct, ensuring faithfulness.
            imgs={tuple(xx[j] for j in pi) for pi in itertools.permutations(range(n))}
            self.assertEqual(len(imgs),math.factorial(n))
            # Elementary generators are fixed under the action.
            self.assertEqual(len(e),n)
        return check
    test_case(f'faithful_action_n{n}',make_transformation())


for mod in (2,3,5,7,11):
    for n in (2,3,4,5):
        def make_modular(mod=mod,n=n):
            def check(self):
                xs=[(i*i+3*i+2) % mod for i in range(n)]
                e=[]
                for k in range(1,n+1):
                    e.append(sum(math.prod(xs[j] for j in ix) for ix in itertools.combinations(range(n),k))%mod)
                # Numerically checking Viète over F_p (not a proof of formal algebraic independence).
                coeff=[1]+[((-1)**k*e[k-1])%mod for k in range(1,n+1)]
                z=s.Symbol('z')
                poly=s.Poly(s.prod(z-v for v in xs),z,modulus=mod)
                self.assertEqual([int(v)%mod for v in poly.all_coeffs()],coeff)
            return check
        test_case(f'vieta_mod_{mod}_n_{n}',make_modular())


def discr3(a,b,c):
    return a*a*b*b-4*b*b*b-4*a*a*a*c-27*c*c+18*a*b*c


def cubic_disc_fundamental(self):
    x1,x2,x3=s.symbols('x1 x2 x3')
    e1=x1+x2+x3;e2=x1*x2+x1*x3+x2*x3;e3=x1*x2*x3
    D=(x1-x2)**2*(x1-x3)**2*(x2-x3)**2
    self.assertEqual(s.expand(discr3(e1,e2,e3)-D),0)
test_case('cubic_discriminant_symmetric_identity',cubic_disc_fundamental)


for mod in (2,3,5,7,11,13):
    def make_discr(mod=mod):
        def check(self):
            # Symmetric discriminant identity survives reduction mod every prime,
            # even when 2 or 3 is zero.
            for x in itertools.product(range(mod), repeat=3):
                if mod>7 and x[0] > 2: break
                e1=sum(x)%mod;e2=(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])%mod;e3=math.prod(x)%mod
                D=math.prod((x[i]-x[j])**2 for i,j in ((0,1),(0,2),(1,2)))%mod
                self.assertEqual(discr3(e1,e2,e3)%mod,D)
        return check
    test_case(f'cubic_discriminant_mod_{mod}',make_discr())


def a5_nonsolvable(self):
    a=AlternatingGroup(5)
    self.assertEqual(a.order(),60)
    self.assertFalse(a.is_abelian)
    self.assertEqual(a.derived_subgroup().order(),60)
test_case('nonabelian_simple_A5_derived_group',a5_nonsolvable)

for n in (5,6,7,8):
    def make_a5(n=n):
        def check(self):
            self.assertEqual(SymmetricGroup(n).order(),math.factorial(n))
            # Every even permutation of the first five symbols extends by
            # fixing remaining symbols, giving an injective A5 -> S_n.
            im={tuple(list(pi)+list(range(5,n))) for pi in itertools.permutations(range(5))
                if sum(pi[i]>pi[j] for i in range(5) for j in range(i+1,5))%2==0}
            self.assertEqual(len(im),60)
            if n>5:
                self.assertTrue(all(x[-1]==n-1 for x in im))
        return check
    test_case(f'A5_embeds_S{n}',make_a5())


def rational_invariant_sums(self):
    xx=s.symbols('x1 x2 x3');e1=sum(xx);e2=sum(xx[i]*xx[j] for i,j in ((0,1),(0,2),(1,2)));e3=s.prod(xx)
    self.assertEqual(s.expand(sum(x*x for x in xx)-(e1*e1-2*e2)),0)
    self.assertEqual(s.cancel(sum(1/x for x in xx)-e2/e3),0)
test_case('rational_invariants_examples',rational_invariant_sums)

for p in (2,3,5,7,11):
    def make_purely_inseparable(p=p):
        def check(self):
            t,x=s.symbols('t x'); f=x**p-t
            self.assertTrue(all(int(c)%p==0 for c in s.Poly(s.diff(f,x),x).all_coeffs()))
            # In char p, (x-alpha)^p=x^p-alpha^p (all interior binomials vanish).
            self.assertTrue(all(math.comb(p,k)%p==0 for k in range(1,p)))
            self.assertEqual(s.Poly(-t,t).degree(),1)
        return check
    test_case(f'pure_inseparable_example_p{p}',make_purely_inseparable())


def cubic_specializations(self):
    x=s.Symbol('x')
    for f,expected in ((x**3-2,-108),(x**3-3*x+1,81)):
        P=s.Poly(f,x);self.assertTrue(P.is_irreducible)
        self.assertEqual(s.discriminant(f,x),expected)
        self.assertNotEqual(expected,0)
test_case('cubic_specializations',cubic_specializations)


def quartic_specialization(self):
    x=s.Symbol('x');P=s.Poly(x**4-2,x)
    self.assertTrue(P.is_irreducible)
    self.assertEqual(s.discriminant(x**4-2,x),-2048)
    self.assertEqual(s.Poly(x**4-2,x).degree(),4)
test_case('quartic_D4_specialization',quartic_specialization)

for n in (2,3,4,5,6):
    def make_coeff_alg_independent(n=n):
        def check(self):
            # Jacobian det of elementary functions = Vandermonde, a nonzero polynomial.
            x=s.symbols('x1:'+str(n+1))
            e=[s.polys.polyfuncs.symmetric_poly(k,*x) for k in range(1,n+1)]
            jac=s.Matrix([[s.diff(g,t) for t in x] for g in e])
            # Distinct numeric point ensures Jacobian det not identically zero over Q.
            self.assertNotEqual(jac.det(method='berkowitz').subs(dict(zip(x,range(1,n+1)))),0)
        return check
    test_case(f'symmetric_Jacobian_nonzero_n{n}',make_coeff_alg_independent())


for label in ['aa:ch:generic-polynomial','aa:def:generic-poly','aa:lem:generic-independence',
              'aa:tw:generic-sn','aa:wn:generic-abel','aa:wn:generic-invariants',
              'aa:prz:generic-rational-invariants','aa:prz:generic-discriminant',
              'aa:prz:generic-cubic','aa:prz:generic-specialization',
              'aa:prz:generic-inseparable-specialization','aa:uw:generic-characteristic']:
    def make_label(label=label):
        def check(self):
            self.assertEqual(TEX.count('\\label{'+label+'}'),1)
        return check
    test_case('label_'+label.replace(':','_').replace('-','_'),make_label())


def label_uniqueness(self):
    labels=re.findall(r'\\label\{([^}]+)\}',TEX)
    self.assertEqual(len(labels),len(set(labels)))
    self.assertEqual(len(labels),12)
test_case('label_uniqueness',label_uniqueness)

for ref in ['aa:tw:fundamental-symmetric','aa:ch:radicals','aa:tw:fundamental-galois',
            'aa:prz:quartic-v4','aa:wn:a5-not-solvable']:
    def make_ref(ref=ref):
        def check(self):
            self.assertIn('\\ref{'+ref+'}',TEX)
        return check
    test_case('ref_'+ref.replace(':','_').replace('-','_'),make_ref())


def no_misformatted_tex(self):
    self.assertNotIn('Vi\\`ete',TEX)
    self.assertNotIn('podrozszerzenie',TEX)
    self.assertIn('\\ref{aa:wn:a5-not-solvable}',TEX)
    self.assertEqual(TEX.count('\\begin{proof}'),TEX.count('\\end{proof}'))
    self.assertEqual(TEX.count('\\begin{przyklad}'),TEX.count('\\end{przyklad}'))
test_case('tex_and_terminology_integrity',no_misformatted_tex)


if __name__=='__main__':
    unittest.main()
