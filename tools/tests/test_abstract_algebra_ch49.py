#!/usr/bin/env python3
"""AA-49: SymPy cross-checks for Kovacic case two (quadratic Riccati).

Verifies algebraic identities and complete finite-candidate enumeration
for explicit exact models, not a substitute for Kovacic's local theorem.
"""
from itertools import product
from pathlib import Path
import re
import unittest
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex"
x=s.symbols("x")

def eq(a,b=0):
    return s.cancel(s.together(s.expand(a-b)))==0

def trace_operator(phi,q):
    return s.diff(phi,x,2)+3*phi*s.diff(phi,x)+phi**3-4*q*phi-2*s.diff(q,x)

def auxiliary_operator(p,theta,q):
    return (s.diff(p,x,3)+3*theta*s.diff(p,x,2)
       +(3*theta**2+3*s.diff(theta,x)-4*q)*s.diff(p,x)
       +(s.diff(theta,x,2)+3*theta*s.diff(theta,x)+theta**3
          -4*q*theta-2*s.diff(q,x))*p)

def discriminant(phi,q):
    return s.factor(4*q-2*s.diff(phi,x)-phi**2)

def case2_local_sets(q):
    """Local candidate sets for examples with rational polynomial roots."""
    q=s.cancel(q)
    if q==0:
        return {},[0,2,4]
    num,den=s.fraction(q)
    poles=s.roots(s.Poly(den,x))
    assert sum(poles.values())==s.degree(den,x), "test models require split denominator"
    E={}
    for a,m in poles.items():
        if m==1:
            values=[4]
        elif m==2:
            b=s.cancel(s.limit((x-a)**2*q,x,a))
            values=[2,2+2*s.sqrt(1+4*b),2-2*s.sqrt(1+4*b)]
        else:
            values=[m]
        E[a]=sorted({int(v) for v in values if v.is_integer is True})
    inf_ord=s.degree(den,x)-s.degree(num,x)
    if inf_ord>2:
        Einf=[0,2,4]
    elif inf_ord==2:
        b=s.limit(x**2*q,x,s.oo)
        vals=[2,2+2*s.sqrt(1+4*b),2-2*s.sqrt(1+4*b)]
        Einf=sorted({int(v) for v in vals if v.is_integer is True})
    else:
        Einf=[int(inf_ord)]
    return E,Einf

def case2_valid_degrees(E,Einf):
    poles=list(E)
    output=[]
    for values in product(*(E[a] for a in poles),Einf):
        selected=values[:-1]; last=values[-1]
        diff=last-sum(selected)
        if diff>=0 and diff%2==0:
            output.append((dict(zip(poles,selected)),last,diff//2))
    return output

class AA49SymPyRegression(unittest.TestCase):
    def test_01_trace_discriminant_identities(self):
        models=[
            (x+s.Rational(5,16)/x**2,-1/(2*x),4*x),
            ((4*x+5)/(16*x**2),-1/(2*x)+1/(x-1),x/(x-1)**2),
            (1/x-s.Rational(3,16)/x**2,1/(2*x),4/x)]
        for q,phi,Delta in models:
            self.assertTrue(eq(trace_operator(phi,q)))
            self.assertTrue(eq(discriminant(phi,q),Delta))
            self.assertTrue(eq(s.diff(Delta,x)+2*phi*Delta))
            self.assertNotEqual(Delta,0)
    def test_02_quadratic_roots_recover_riccati(self):
        models=[
            (x+s.Rational(5,16)/x**2,-1/(2*x),4*x),
            ((4*x+5)/(16*x**2),-1/(2*x)+1/(x-1),x/(x-1)**2),
            (1/x-s.Rational(3,16)/x**2,1/(2*x),4/x)]
        for q,phi,Delta in models:
            for sign in (1,-1):
                w=(phi+sign*s.sqrt(Delta))/2
                self.assertTrue(eq(s.diff(w,x)+w*w,q),str((q,w)))
    def test_03_quadratic_local_sets_first_example(self):
        q=x+s.Rational(5,16)/x**2
        E,Einf=case2_local_sets(q)
        self.assertEqual(E,{s.Integer(0):[-1,2,5]})
        self.assertEqual(Einf,[-1])
        self.assertIn(({s.Integer(0):-1},-1,0),case2_valid_degrees(E,Einf))
    def test_04_positive_degree_candidate(self):
        q=(4*x+5)/(16*x**2)
        E,Einf=case2_local_sets(q)
        self.assertEqual(E,{s.Integer(0):[-1,2,5]})
        self.assertEqual(Einf,[1])
        self.assertIn(({s.Integer(0):-1},1,1),case2_valid_degrees(E,Einf))
        theta=-1/(2*x);P=x-1
        self.assertTrue(eq(auxiliary_operator(P,theta,q)))
        phi=theta+s.diff(P,x)/P
        self.assertTrue(eq(discriminant(phi,q),x/(x-1)**2))
    def test_05_second_local_configuration(self):
        q=1/x-s.Rational(3,16)/x**2
        E,Einf=case2_local_sets(q)
        self.assertEqual(E,{s.Integer(0):[1,2,3]})
        self.assertEqual(Einf,[1])
        self.assertIn(({s.Integer(0):1},1,0),case2_valid_degrees(E,Einf))
        self.assertTrue(eq(auxiliary_operator(s.Integer(1),1/(2*x),q)))
    def test_06_airy_negative_degree(self):
        E,Einf=case2_local_sets(x)
        self.assertEqual(E,{})
        self.assertEqual(Einf,[-1])
        self.assertEqual(case2_valid_degrees(E,Einf),[])
    def test_07_polynomial_equation_from_third_order(self):
        q=(4*x+5)/(16*x**2)
        theta=-1/(2*x)
        coeff=s.symbols("c")
        P=x+coeff
        expression=s.together(auxiliary_operator(P,theta,q))
        poly=s.Poly(expression.as_numer_denom()[0],x)
        equations=[s.Eq(v,0) for v in poly.all_coeffs()]
        sol=s.solve(equations,[coeff],dict=True)
        self.assertEqual(sol,[{coeff:-1}])
    def test_08_nonsquare_discriminants(self):
        for delta in (4*x,x/(x-1)**2,4/x):
            numerator,denominator=s.fraction(s.cancel(delta))
            nroots=s.roots(numerator,x)
            droots=s.roots(denominator,x)
            self.assertTrue(any(m%2 for m in list(nroots.values())+list(droots.values())))
    def test_09_symmetric_square_product(self):
        # For q=2/x^2, z1=x^2 and z2=1/x are independent.
        q=2/x**2;v=x**2*(1/x)
        self.assertTrue(eq(s.diff(v,x,3)-4*q*s.diff(v,x)-2*s.diff(q,x)*v))
        self.assertTrue(eq(trace_operator(s.diff(v,x)/v,q)))
        # The discriminant is a rational square: not a new quadratic case.
        phi=s.diff(v,x)/v
        self.assertTrue(eq(discriminant(phi,q),9/x**2))
    def test_10_zero_potential(self):
        self.assertTrue(eq(s.diff(1/(x+3),x)+(1/(x+3))**2))
        self.assertTrue(eq(trace_operator(s.Integer(0),s.Integer(0))))
        self.assertTrue(eq(discriminant(s.Integer(0),s.Integer(0))))
    def test_11_documented_claims_and_labels(self):
        text=SOURCE.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",text)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),24)
        self.assertGreaterEqual(text.count(r"\begin{proof}"),5)
        self.assertEqual(text.count(r"\begin{proof}"),text.count(r"\end{proof}"))
        for needed in ("aa:tw:kov2-classical-candidates","aa:tw:kov2-algorithm",
                       "aa:lem:kov2-symmetric-square","aa:eq:kov2-P-equation",
                       "aa:prz:kov2-positive-degree"):
            self.assertIn(r"\label{"+needed+"}",text)
        self.assertIn("cytujemy",text)
if __name__=="__main__":
    unittest.main()
