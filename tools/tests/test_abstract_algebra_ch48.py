#!/usr/bin/env python3
"""AA-48 exact SymPy regression: rational Riccati poles and linear P-equations.

Finite symbolic examples confirm computational formulas; they do not
replace the proof of completeness for arbitrary rational potentials.
"""
import re
import unittest
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"chapters/pl/abstract_algebra/48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex"
x=s.symbols("x")

def equal(a,b):
    return s.cancel(s.together(a-b))==0

def potential(r):
    return s.factor(s.diff(r,x)+r*r)

def poly_equation(u,p,q):
    return s.cancel(s.together(s.diff(p,x,2)+2*u*s.diff(p,x)+
                          (s.diff(u,x)+u*u-q)*p))

class AA48RationalKovacicSympy(unittest.TestCase):
    def test_01_simple_fixed_pole(self):
        r=x+1/(x-1)
        q=x*x+3+2/(x-1)
        self.assertTrue(equal(potential(r),q))
        self.assertEqual(s.limit((x-1)*q,x,1),2)
        self.assertEqual(s.limit((x-1)*r,x,1),1)
        self.assertTrue(equal(poly_equation(r,1,q),0))
        z=(x-1)*s.exp(x*x/2)
        self.assertTrue(equal(s.diff(z,x,2)/z,q))

    def test_02_double_pole_both_residues(self):
        q=2/x**2
        roots=s.solve(s.Eq(s.Symbol("c")*(s.Symbol("c")-1),2),s.Symbol("c"))
        self.assertEqual(set(roots),{s.Integer(2),s.Integer(-1)})
        for c,z in ((s.Integer(2),x*x),(s.Integer(-1),1/x)):
            self.assertTrue(equal(potential(c/x),q))
            self.assertTrue(equal(s.diff(z,x,2)/z,q))
            self.assertTrue(equal(poly_equation(c/x,1,q),0))

    def test_03_fourth_order_pole_recursion(self):
        q=1/x**4-2/x**3
        c2=s.Symbol("c2",nonzero=True)
        c1=s.Symbol("c1")
        u=c2/x**2+c1/x
        expr=s.expand(s.diff(u,x)+u*u)
        self.assertEqual(expr.coeff(x,-4),c2*c2)
        self.assertEqual(expr.coeff(x,-3),2*c2*c1-2*c2)
        self.assertTrue(equal(potential(1/x**2),q))
        self.assertTrue(equal(poly_equation(1/x**2,1,q),0))

    def test_04_odd_high_order_obstruction(self):
        for m in (3,5,7,9):
            q=1/(x-2)**m
            den=s.Poly(s.denom(s.cancel(q)),x)
            roots=s.roots(den)
            self.assertEqual(roots,{s.Integer(2):m})
            self.assertEqual(m%2,1)
            self.assertGreater(m,2)

    def test_05_movable_pole_at_regular_point(self):
        q=x*x+3
        r=x+1/x
        p=x
        self.assertTrue(equal(potential(r),q))
        self.assertTrue(equal(poly_equation(x,p,q),0))
        self.assertEqual(s.limit(x*r,x,0),1)
        self.assertEqual(s.limit(x**2*q,x,0),0)

    def test_06_infinity_positive_polynomial_part(self):
        q=x*x+3+2/(x-1)
        u=x+1/(x-1)
        delta=s.factor(q-s.diff(u,x)-u*u)
        self.assertTrue(equal(delta,0))
        # For q=x^2+3, omega=x, R=0, and n=1.
        q2=x*x+3;omega=x
        delta2=s.expand(q2-s.diff(omega,x)-omega*omega)
        self.assertEqual(s.limit(delta2,x,s.oo),2)
        self.assertEqual(s.limit(delta2,x,s.oo)/2,1)

    def test_07_infinity_constant_polynomial_part(self):
        q=1+2/x
        u=1+1/x
        self.assertTrue(equal(potential(u),q))
        d=s.cancel(q-s.diff(u,x)-u*u)
        self.assertEqual(s.limit(x*d,x,s.oo),0)
        # q=2/x^2, R=2/x, gives rho=2, beta=2, n=0.
        rho=s.Integer(2);beta=s.Integer(2)
        n=s.symbols("n")
        self.assertIn(s.Integer(0),s.solve((n+rho)*(n+rho-1)-beta,n))

    def test_08_zero_potential_and_free_pole(self):
        for a in (s.Integer(-2),s.Integer(0),s.Rational(3,2)):
            r=1/(x-a)
            self.assertTrue(equal(potential(r),0))
            p=x-a
            self.assertTrue(equal(poly_equation(0,p,0),0))
        n=s.symbols("n")
        self.assertEqual(set(s.solve(n*(n-1),n)),{0,1})

    def test_09_quadratic_algebraic_escape(self):
        q=x+5/(16*x*x)
        r=s.sqrt(x)-1/(4*x)
        self.assertTrue(equal(potential(r),q))
        numerator,denominator=s.fraction(s.cancel(q))
        poly_part=s.div(numerator,denominator,x)[0]
        self.assertEqual(s.degree(poly_part,x),1)

    def test_10_p_zero_at_singularity_must_be_rejected(self):
        # With q=2/x^2, choose the local branch u=-1/x.
        # P=x^3 solves the P equation, but P(0)=0,
        # so that P belongs to a different branch and is inadmissible here.
        q=2/x**2;u=-1/x;p=x**3
        self.assertTrue(equal(poly_equation(u,p,q),0))
        self.assertEqual(p.subs(x,0),0)
        self.assertTrue(equal(potential(u+s.diff(p,x)/p),q))
        self.assertTrue(equal(u+s.diff(p,x)/p,2/x))

    def test_11_source_structure(self):
        data=SOURCE.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),22)
        self.assertGreaterEqual(data.count(r"\begin{proof}"),6)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        for expected in ("aa:tw:kov-rational-complete-algorithm",
                         "aa:lem:kov-rational-local-orders",
                         "aa:lem:kov-rational-local-candidates",
                         "aa:lem:kov-rational-infinity",
                         "aa:eq:kov-rational-P-ode"):
            self.assertIn(r"\label{"+expected+"}",data)

if __name__=="__main__":
    unittest.main()
