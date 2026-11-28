#!/usr/bin/env python3
"""AA-45 regression models using SymPy; samples do not replace general proofs."""
import unittest,re
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"chapters/pl/abstract_algebra/45-kryteria-hiperwykladnicze-i-calki-nieelementarne.tex"
x,t,z=s.symbols("x t z")
I=s.I

def same(a,b):
    return s.cancel(s.together(a-b))==0
def deriv(a,h):
    return s.diff(a,x)+h*t*s.diff(a,t)

class AA45MathematicalRegression(unittest.TestCase):
    def test_01_hyperexponential_positive_models(self):
        for h,r in [(-2*x,-s.Rational(1,2)),(2*x,s.Rational(1,2)),
                    (1,1/x),(1,x**2+1)]:
            target=s.diff(r,x)+h*r
            self.assertTrue(same(deriv(r*t,h),target*t))
        self.assertTrue(same(s.diff(s.exp(x)/x,x),
                             s.exp(x)*(1/x-1/x**2)))

    def test_02_laurent_positive_and_negative(self):
        h=2*x+1
        for k in (-5,-3,-1,1,2,4):
            r=(x**2+2)/(x+1)
            target=s.diff(r,x)+k*h*r
            self.assertTrue(same(deriv(r*t**k,h),target*t**k))
        self.assertTrue(same((t-t**(-1))/(2*I*x),
                             (t-t**(-1))/(2*I*x)))

    def test_03_sine_coefficient(self):
        h=I
        a=1/(2*I*x)
        self.assertTrue(same(2*I*a,1/x))
        self.assertTrue(same(deriv(t/(2*I*x),h)/t,
                             s.diff(1/(2*I*x),x)+I/(2*I*x)))

    def test_04_simple_pole_dominant_coefficient(self):
        for m in range(1,6):
            for a in (-2,0,3):
                u=x-a
                r=(u+2)/u**m
                h=u**2+3*u+1
                deriv_rhs=s.diff(r,x)+h*r
                self.assertEqual(s.limit(u**(m+1)*deriv_rhs,x,a),-2*m)

    def test_05_gaussian_degree_barrier(self):
        for degree in range(6):
            cs=s.symbols("c0:"+str(degree+1))
            r=sum(c*x**i for i,c in enumerate(cs))
            poly=s.Poly(s.diff(r,x)-2*x*r-1,x)
            solution=s.linsolve(list(poly.all_coeffs()),cs)
            self.assertEqual(solution,s.EmptySet)

    def test_06_partial_fractions(self):
        f=x/(x**2+1)
        self.assertTrue(same(f,s.diff(x**2+1,x)/(2*(x**2+1))))
        self.assertTrue(same(1/(x**2+1),
                             1/(2*I)*(1/(x-I)-1/(x+I))))
        for a in (s.Rational(1,3),-2,5):
            self.assertTrue(same(s.diff((x-a)**(-3),x),
                                 -3/(x-a)**4))

    def test_07_elliptic_quadratic_relation(self):
        y=s.symbols("y",nonzero=True)
        yp=-2*x**3/y
        self.assertTrue(same(2*y*yp+4*x**3,0))
        self.assertTrue(same(yp/y,-2*x**3/(1-x**4))==False)
        # Reduction modulo y^2-(1-x^4) makes those equal.
        expr=s.cancel(yp/y+2*x**3/(1-x**4))
        self.assertEqual(s.rem(s.together(expr).as_numer_denom()[0],
                                s.Poly(y*y-(1-x**4),y).as_expr(),y),0)

    def test_08_elliptic_local_charts(self):
        for a in (1,-1,I,-I):
            yy=s.symbols("yy")
            xx=a*(1-yy**2)**s.Rational(1,4)
            dxx=s.diff(xx,yy)
            self.assertEqual(s.simplify(dxx/yy+1/(2*xx**3)),0)
        ss,w=s.symbols("ss w",nonzero=True)
        self.assertTrue(same((-1/ss**2)/(w/ss**2),-1/w))

    def test_09_elliptic_local_orders(self):
        # At a=1, (x-1)/y^2 -> -1/4, so ord(x-1)=2.
        yy=s.symbols("yy")
        ratio=((1-yy**2)**s.Rational(1,4)-1)/yy**2
        self.assertEqual(s.limit(ratio,yy,0),-s.Rational(1,4))
        for m in (-3,-2,-1,0,1,2,3):
            actual=s.limit(ratio**m,yy,0)
            self.assertEqual(s.simplify(actual-(-s.Rational(1,4))**m),0)
        # At infinity, x=1/ss and y=w/ss^2 with w(0)=+i or -i.
        ss=s.symbols("ss")
        for w0 in (s.I,-s.I):
            for m,n in ((1,0),(0,1),(-2,1),(3,-1)):
                expr=(1/ss)**m*(w0/ss**2)**n
                normalised=s.simplify(ss**(m+2*n)*expr)
                self.assertEqual(s.simplify(normalised-w0**n),0)

    def test_10_source_labels_proofs(self):
        data=SRC.read_text(encoding="utf-8")
        labs=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(len(labs),24)
        self.assertGreaterEqual(data.count(r"\begin{proof}"),11)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        for target in ("aa:tw:hyperexponential-criterion","aa:tw:laurent-hyperexp-criterion",
                       "aa:tw:gaussian-nonelementary","aa:tw:sine-integral-nonelementary",
                       "aa:tw:logarithmic-integral-nonelementary",
                       "aa:tw:elliptic-integral-nonelementary"):
            self.assertIn(r"\label{"+target+"}",data)

if __name__=="__main__": unittest.main()
