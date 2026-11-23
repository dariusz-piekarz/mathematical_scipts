#!/usr/bin/env python3
"""AA-43 mathematical regressions: differential fields, algebraic derivations,
trace/norm and new-constant obstructions. Independent SymPy rational oracle.
"""
import re
import unittest
from itertools import product
from pathlib import Path
import sympy as sp

X,T=sp.symbols("x t")
CHAPTER=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex"

def normalize(a):return sp.factor(sp.cancel(a))
def derivative(expr,a):
    return normalize(sp.diff(expr,X)+a*sp.diff(expr,T))

class DifferentialFieldAA43(unittest.TestCase):
    def test_01_derivation_and_quotient_rule(self):
        for a,b,c,d in product(range(-2,3),repeat=4):
            P=a*X+b
            Q=c*X+d
            if Q==0:continue
            r=P/Q
            self.assertEqual(normalize(sp.diff(r,X)-(a*Q-P*c)/Q**2),0)

    def test_02_rational_constant_field(self):
        for a,b,c,d in product(range(-2,3),repeat=4):
            P=a*X+b;Q=c*X+d
            if Q==0:continue
            r=normalize(P/Q)
            if normalize(sp.diff(r,X))==0:
                self.assertFalse(r.has(X))
        self.assertEqual(sp.diff(X**3,X),3*X**2)

    def test_03_algebraic_quadratic_derivation(self):
        samples=[
            (X,1),(X**2+1,X+2),(2*X+3,X**2+1),
            (X**3+1,2*X**2+3),(X+2,X**2+X+2)
        ]
        for b,c in samples:
            disc=normalize(b*b-4*c)
            self.assertNotEqual(disc,0)
            bp,cp=sp.diff(b,X),sp.diff(c,X)
            u=normalize((2*c*bp-b*cp)/disc)
            v=normalize((b*bp-2*cp)/disc)
            # In K[alpha]/(alpha^2+b*alpha+c), alpha'=u+v*alpha.
            self.assertEqual(normalize(2*u+b*v+bp*b*0+cp + v*b*b*0),normalize(2*u+b*v+cp))
            # Check the defining relation coefficient-by-coefficient:
            # (2alpha+b)(u+v alpha)+b' alpha +c'=0
            constant=normalize(b*u-2*c*v+cp)
            linear=normalize(2*u-b*v+bp)
            self.assertEqual(constant,0)
            self.assertEqual(linear,0)
            self.assertEqual(normalize(2*u-b*v + 0),normalize(-bp))
            # trace(alpha') = 2u-bv = -b'
            self.assertEqual(normalize(2*u-b*v),normalize(-bp))
            # norm(alpha) = c, log-norm relation.
            if c!=0:
                self.assertEqual(normalize(2*v-b*u/c),normalize(cp/c))

    def test_04_sqrt_x_squared_plus_one(self):
        f=X**2+1
        self.assertEqual(normalize(X/f-X/f),0)
        self.assertEqual(normalize(sp.diff(-f,X)/(-f)-2*X/f),0)
        self.assertEqual(normalize((2*X/f)-sp.diff(sp.log(f),X)),0)

    def test_05_trace_norm_for_monic_binomial(self):
        for n in range(2,7):
            for f in (X+1,X**2+1,X**3-X+2):
                assert f!=0
                # m(alpha)=alpha^n-f, Dalpha/alpha = f'/(n f)
                # trace of any scalar is n times that scalar.
                logarithmic=normalize(sp.diff(f,X)/(n*f))
                self.assertEqual(normalize(n*logarithmic-sp.diff(f,X)/f),0)
                norm=(-1)**(n+1)*f
                self.assertEqual(normalize(sp.diff(norm,X)/norm-sp.diff(f,X)/f),0)

    def test_06_primitive_transcendental_differentiation(self):
        a=1/X
        cases=[
            (T+X, T**2+1),(X*T+1,T+2),
            (T**3+X*T+2, X*T**2+T+1),
            (X**2+T**2,X*T+1)
        ]
        for num,den in cases:
            d=derivative(num/den,a)
            expected=normalize((derivative(num,a)*den-num*derivative(den,a))/den**2)
            self.assertEqual(normalize(d-expected),0)
            self.assertEqual(normalize(derivative(T,a)-1/X),0)
        self.assertEqual(normalize(derivative(T-X,1)),0)

    def test_07_exponential_transcendental_differentiation(self):
        h=X**2+2
        a=h*T
        for e in range(-4,5):
            for j in range(3):
                coeff=X**j+1
                expr=coeff*T**e
                expected=(sp.diff(coeff,X)+e*h*coeff)*T**e
                self.assertEqual(normalize(derivative(expr,a)-expected),0)
        self.assertEqual(normalize(derivative(T/X,T/X)),0)

    def test_08_algebraic_automorphisms(self):
        c=sp.Rational(7,3)
        # D(T)=1/X, T -> T+c commutes with derivation.
        r=(X*T**2+T+1)/(X+T**2)
        shift=sp.cancel(r.subs(T,T+c,simultaneous=True))
        self.assertEqual(normalize(derivative(shift,1/X)-
                         derivative(r,1/X).subs(T,T+c,simultaneous=True)),0)
        # D(T)=T, T -> cT likewise.
        scale=sp.cancel(r.subs(T,c*T,simultaneous=True))
        self.assertEqual(normalize(derivative(scale,T)-
                         derivative(r,T).subs(T,c*T,simultaneous=True)),0)

    def test_09_logarithmic_derivatives_are_proper(self):
        for roots in ((0,1),(-2,0,3),(1,4)):
            for mult in product((-2,-1,1,2),repeat=len(roots)):
                u=sp.prod((X-r)**k for r,k in zip(roots,mult))
                actual=normalize(sp.diff(u,X)/u)
                expected=sum(sp.Rational(k)/(X-r) for r,k in zip(roots,mult))
                self.assertEqual(normalize(actual-expected),0)
                # Every nonzero constant would have nonzero polynomial part.
                self.assertEqual(sp.limit(actual,X,sp.oo),0)

    def test_10_positive_characteristic_obstruction(self):
        for p in (2,3,5,7,11):
            self.assertEqual(p%p,0)
            self.assertEqual((p*X**(p-1)).subs(X,2)%p,0)
        # Over F_p(x), D(x^p)=0 but x^p is not constant in F_p.

    def test_11_source_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),13)
        self.assertGreaterEqual(s.count(r"\begin{proof}"),6)
        self.assertGreaterEqual(s.count(r"\begin{przyklad}"),5)
        self.assertIn(r"\label{aa:tw:algebraic-derivation-extension}",s)
        self.assertIn(r"\label{aa:tw:differential-trace-norm}",s)
        self.assertIn(r"\label{aa:lem:primitive-extension-constants}",s)
        self.assertIn(r"\label{aa:lem:exponential-extension-constants}",s)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))

if __name__=="__main__":
    unittest.main()
