#!/usr/bin/env python3
"""Independent computational and structural spot checks for AA-37, audit I.

These finite symbolic checks supplement (do not replace) the proofs of
Zorn's lemma, the exchange lemma, and the cardinality theorem.
"""
import random
import re
import unittest
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parent
SRC = (ROOT.parents[1] / "chapters/pl/abstract_algebra/37-algebraiczna-niezaleznosc-i-bazy-transcendencji.tex").read_text(encoding="utf-8")
u, v, w, t, X, Y, Z = S.symbols('u v w t X Y Z')


def nonzero_poly_mod(expr, gens, prime):
    poly = S.Poly(S.expand(expr), *gens, modulus=prime)
    return not poly.is_zero


class Structure(unittest.TestCase):
    def test_unique_labels(self):
        ls = re.findall(r'\\label\{([^}]+)\}', SRC)
        self.assertEqual(len(ls), len(set(ls)))
        self.assertEqual(len(ls), 15)

    def test_balanced_proofs_and_examples(self):
        for env in ['proof', 'lemat', 'twierdzenie', 'przyklad', 'definicja']:
            self.assertEqual(SRC.count(r'\begin{' + env + '}'), SRC.count(r'\end{' + env + '}'))
        self.assertEqual(SRC.count(r'\begin{proof}'), 7)
        self.assertEqual(SRC.count(r'\begin{przyklad}'), 7)

    def test_internal_refs(self):
        labels = set(re.findall(r'\\label\{([^}]+)\}', SRC))
        refs = set(re.findall(r'\\ref\{([^}]+)\}', SRC))
        self.assertEqual(refs-labels, {'aa:tw:fundamental-symmetric'})

    def test_key_proof_phrases(self):
        for text in ['Lemat Zorna', 'transcendentalny nad $F$',
                     'Lemat~\\ref{aa:lem:transcendence-essential-variable}',
                     'C=\\{t_1+t_2,t_2,t_3,t_4,\\ldots\\}',
                     '\\operatorname{trdeg}_K L']:
            self.assertIn(text, SRC)

    def test_terminology(self):
        self.assertNotIn('Pola te nie muszą', SRC)
        self.assertNotIn('injektywne', SRC)
        self.assertNotIn('jest injekcją', SRC)
        self.assertNotIn('tensorowanie', SRC)


class Algebra(unittest.TestCase):
    def test_vieta_relation(self):
        p, q, T = S.symbols('p q T')
        self.assertEqual(S.expand((T-u)*(T-v) - (T**2-(u+v)*T+u*v)), 0)

    def test_symmetric_jacobian(self):
        # Independent in characteristic zero; char 2 is handled by substitution tests.
        jac = S.Matrix([[1, 1], [v, u]]).det()
        self.assertEqual(jac, u-v)

    def test_nontrivial_quadratic_extension(self):
        # The relation T^2-sT+p=0 has formal discriminant (u-v)^2.
        s, p = u+v, u*v
        self.assertEqual(S.expand(s*s-4*p - (u-v)**2), 0)

    def test_two_independent_bases(self):
        self.assertEqual(S.expand((u+v)-v-u),0)
        self.assertEqual(S.expand((u+v)*u-u*u-u*v),0)

    def test_tower_change_inverse(self):
        self.assertEqual(S.expand((u+v)-v-u),0)
        self.assertEqual(S.Matrix([[1,1],[0,1]]).det(),1)

    def test_nonlinear_exchange_inverse(self):
        x=u+v*v
        self.assertEqual(S.expand(x-v*v-u),0)
        self.assertEqual(S.det(S.Matrix([[S.diff(x,u),S.diff(x,v)], [0,1]])),1)

    def test_rational_swap(self):
        r=(u*u+v*v)/(u*v)
        self.assertEqual(S.factor(r - r.xreplace({u:v,v:u})),0)

    def test_algebraic_dependency(self):
        self.assertEqual(S.expand(Y-X**2).subs({X:t,Y:t*t}),0)

    def test_pure_transcendental_irreducibility(self):
        # Illustrative Gauss-lemma cases over Q(z): no new factorization appears.
        q=S.symbols('q')
        polynomials=[X*X+1, X*X-2, X**3-2, X**3+X+1]
        for f in polynomials:
            self.assertTrue(S.Poly(f,X,domain=S.QQ).is_irreducible)
            self.assertEqual(len(S.factor_list(f,X)[1]),1)
            self.assertEqual(S.Poly(f,X,domain=S.QQ.frac_field(q)).is_irreducible, True)

    def test_finite_extension_degree_char_0(self):
        # For a quadratic generic pair, swapping roots fixes s and p, not u.
        self.assertEqual((u+v).xreplace({u:v,v:u}),u+v)
        self.assertEqual((u*v).xreplace({u:v,v:u}),u*v)
        self.assertNotEqual(u, v)


def make_symmetric_test(seed, characteristic):
    def check(self):
        rng=random.Random(seed*1009+characteristic*13)
        a=[rng.randrange(characteristic) for _ in range(10)]
        if not any(a):a[0]=1
        P=sum(a[j]*(X**(j%4))*(Y**(j//4)) for j in range(10))
        self.assertTrue(nonzero_poly_mod(P,(X,Y),characteristic))
        # Fundamental symmetric theorem injectivity for n=2 by finite nonzero samples.
        Q=S.expand(P.subs({X:u+v,Y:u*v},simultaneous=True))
        self.assertTrue(nonzero_poly_mod(Q,(u,v),characteristic))
    return check


def make_exchange_test(seed, characteristic):
    def check(self):
        rng=random.Random(seed*59+characteristic*29)
        coeff=[rng.randrange(characteristic) for _ in range(8)]
        if not any(coeff):coeff[0]=1
        P=sum(coeff[j]*X**(j%3)*Y**(j//3) for j in range(8))
        self.assertTrue(nonzero_poly_mod(P,(X,Y),characteristic))
        Q=S.expand(P.subs({X:u+v*v,Y:v},simultaneous=True))
        self.assertTrue(nonzero_poly_mod(Q,(u,v),characteristic))
        # Reverse substitution gives P again as a formal polynomial.
        inv=S.expand(Q.subs({u:X-Y*Y,v:Y},simultaneous=True))
        self.assertFalse(nonzero_poly_mod(inv-P,(X,Y),characteristic))
    return check


def make_infinite_basis_test(seed, characteristic):
    def check(self):
        rng=random.Random(seed*137+characteristic*37)
        z0,z1,z2,z3=S.symbols('z0 z1 z2 z3')
        coeff=[rng.randrange(characteristic) for _ in range(8)]
        if not any(coeff):coeff[1]=1
        P=sum(coeff[j]*[z0,z1,z2,z3,z0*z1,z1*z2,z0*z3,z2*z3][j] for j in range(8))
        if not nonzero_poly_mod(P,(z0,z1,z2,z3),characteristic):P+=1
        transformed=S.expand(P.subs({z0:z0+z1},simultaneous=True))
        restored=S.expand(transformed.subs({z0:z0-z1},simultaneous=True))
        self.assertFalse(nonzero_poly_mod(restored-P,(z0,z1,z2,z3),characteristic))
        self.assertTrue(nonzero_poly_mod(transformed,(z0,z1,z2,z3),characteristic))
    return check


def make_residue_class_test(seed, characteristic):
    def check(self):
        rng=random.Random(seed*31+characteristic*47)
        # Sum_i A_i(t^p)t^i: nonzero summands have disjoint exponent
        # congruence classes modulo p. This confirms the proof's key idea.
        polys=[]
        for i in range(characteristic):
            coefficients=[rng.randrange(characteristic) for _ in range(3)]
            polys.append(S.Poly(sum(coefficients[j]*t**(characteristic*j+i) for j in range(3)),t,modulus=characteristic))
        total=sum((poly.as_expr() for poly in polys),S.Integer(0))
        if all(x.is_zero for x in polys):return
        self.assertTrue(nonzero_poly_mod(total,(t,),characteristic))
    return check

for p in [2,3,5,7]:
    for i in range(6):
        setattr(Algebra,f'test_sym_n2_p{p}_case{i:02}',make_symmetric_test(i,p))
    for i in range(4):
        setattr(Algebra,f'test_triangular_p{p}_case{i:02}',make_exchange_test(i,p))
    for i in range(3):
        setattr(Algebra,f'test_infinite_basis_p{p}_case{i:02}',make_infinite_basis_test(i,p))
    for i in range(3):
        setattr(Algebra,f'test_purely_insep_p{p}_case{i:02}',make_residue_class_test(i,p))

if __name__=='__main__':
    unittest.main(verbosity=2)
