#!/usr/bin/env python3
"""AA-44: SymPy checks for polynomial-part and Liouville descent formulas."""
import unittest,re
from pathlib import Path
import sympy as sp
x,t=sp.symbols("x t")
SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/44-twierdzenie-liouvillea-o-calkowaniu-elementarnym.tex"
def eq(a,b): return sp.cancel(sp.together(a-b))==0
def D(a,dt): return sp.cancel(sp.diff(a,x)+dt*sp.diff(a,t))
def pp(a):
    p,q=sp.fraction(sp.cancel(sp.together(a)))
    return sp.div(p,q,t)[0]

class TestLiouville(unittest.TestCase):
    def test_01_primitive_polynomial_part(self):
        P=(x+1)*t**3+x*t+1
        Q=(x*t+2)/(t**3+(x+1)*t+3)
        for a in (1/x,x**2+1,sp.Rational(3,2)):
            self.assertTrue(eq(pp(D(P+Q,a)),D(P,a)))
    def test_02_exponential_polynomial_part(self):
        P=(x+1)*t**3+x*t+1
        Q=(x*t+2)/(t**3+(x+1)*t+3)
        for h in (1,2*x,x**2+1):
            self.assertTrue(eq(pp(D(P+Q,h*t)),D(P,h*t)))
    def test_03_logarithmic_polynomial_parts(self):
        b=x**2+1
        p=t**3+x*t**2+1
        q=t**2+(x+1)*t+2
        u=b*p/q
        for a in (1/x,sp.Rational(5,3),x**2+2):
            self.assertTrue(eq(pp(D(u,a)/u),sp.diff(b,x)/b))
        for h in (1,2*x,x**2+2):
            self.assertTrue(eq(pp(D(u,h*t)/u),sp.diff(b,x)/b+h))
    def test_04_trace_norm_example(self):
        f=x/(x**2+1)
        norm=-(x**2+1)
        self.assertTrue(eq(f,sp.diff(norm,x)/(2*norm)))
    def test_05_complex_partial_fractions(self):
        self.assertTrue(eq(1/(x**2+1),(1/(2*sp.I))*(1/(x-sp.I)-1/(x+sp.I))))
    def test_06_log_descent_examples(self):
        self.assertTrue(eq(D(3*t+x**2,1/x),3/x+2*x))
        self.assertTrue(eq(sp.expand(D(t**2+x,1/x)).coeff(t,1),2/x))
    def test_07_exponential_example(self):
        u=x*t**2/(t+1)
        self.assertTrue(eq(D(u,t)/u,1/x+2-t/(t+1)))
        self.assertTrue(eq(pp(D(u,t)/u),1/x+1))
    def test_08_new_constants_counterexample(self):
        self.assertTrue(eq(D(t-x,1),0))
        self.assertEqual(sp.Poly(t-x,t).degree(),1)
    def test_09_source(self):
        s=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),15)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        for tag in ("aa:tw:liouville-elementary-integration",
                    "aa:lem:liouville-polynomial-parts",
                    "aa:lem:liouville-algebraic-descent",
                    "aa:lem:liouville-log-descent",
                    "aa:lem:liouville-exp-descent"):
            self.assertIn(r"\label{"+tag+"}",s)
if __name__=="__main__": unittest.main()
