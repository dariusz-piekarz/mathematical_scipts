#!/usr/bin/env python3
"""AA-50: exact symbolic tests of Kovacic's finite primitive case.

The classical local completeness theorem is cited, not proved by examples.
"""
import re
import unittest
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex"
x,t=s.symbols("x t")

def same(a,b=0):
    return s.cancel(s.together(a-b))==0

def qtet():
    return -s.Rational(3,16)/x**2-s.Rational(2,9)/(x-1)**2+s.Rational(3,16)/(x*(x-1))

def local_set(n,b):
    return sorted({int(v) for k in range(-n//2,n//2+1)
                   for v in [s.simplify(6+s.Rational(12*k,n)*s.sqrt(1+4*b))]
                   if v.is_integer is True})
def get_p(n,S,theta,q,P):
    items={n+1:s.Integer(0),n:-P}
    for i in range(n,-1,-1):
        items[i-1]=s.factor(-S*s.diff(items[i],x)
               +((n-i)*s.diff(S,x)-S*theta)*items[i]
               -(n-i)*(i+1)*S*S*q*items[i+1])
    return items
def polynomial_F(n,S,items):
    return s.factor(sum(S**i*items[i]*t**i/s.factorial(n-i)
                        for i in range(n+1)))
def transport(F,n,S,theta,q):
    lhs=s.diff(F,x)+(q-t*t)*s.diff(F,t)
    rhs=(-n*t+n*s.diff(S,x)/S-theta)*F
    return s.cancel(s.together(lhs-rhs))

class AA50KovacicFiniteSymPy(unittest.TestCase):
    def test_01_tetrahedral_potential_and_orders(self):
        q=qtet()
        self.assertTrue(same(q,-s.Rational(3,16)/x**2-
                s.Rational(2,9)/(x-1)**2+s.Rational(3,16)/(x*(x-1))))
        self.assertEqual(s.limit(x*x*q,x,0),-s.Rational(3,16))
        self.assertEqual(s.limit((x-1)**2*q,x,1),-s.Rational(2,9))
        self.assertEqual(s.limit(x*x*q,x,s.oo),-s.Rational(2,9))

    def test_02_case_three_exact_local_lists(self):
        self.assertEqual(local_set(4,-s.Rational(3,16)),[3,6,9])
        self.assertEqual(local_set(4,-s.Rational(2,9)),[4,5,6,7,8])
        self.assertEqual(local_set(4,s.Integer(2)),[-12,-3,6,15,24])
        self.assertEqual(local_set(6,s.Integer(2)),[-12,-6,0,6,12,18,24])
        self.assertEqual(local_set(12,s.Integer(2)),list(range(-12,25,3)))

    def test_03_degree_and_theta_tetrahedron(self):
        self.assertEqual(s.Rational(4,12)*(7-3-4),0)
        theta=s.Rational(4,12)*(s.Rational(3)/x+s.Rational(4)/(x-1))
        self.assertTrue(same(theta,1/x+s.Rational(4,3)/(x-1)))
        S=x*(x-1)
        self.assertTrue(same(S*theta,s.Rational(7,3)*x-1))
        self.assertTrue(same(S*S*qtet(),
                             -s.Rational(2,9)*x*x+s.Rational(3,16)*x-s.Rational(3,16)))

    def test_04_recurrence_tetrahedral_poly_coefficients(self):
        q=qtet();S=x*(x-1);theta=1/x+s.Rational(4,3)/(x-1)
        a=get_p(4,S,theta,q,s.Integer(1))
        expected={
          4:-1,
          3:(7*x-3)/3,
          2:-(48*x*x-41*x+9)/12,
          1:(320*x**3-409*x*x+180*x-27)/72,
          0:-(2048*x**4-3484*x**3+2313*x*x-702*x+81)/864
        }
        for k,v in expected.items():
            self.assertTrue(same(a[k],v),str((k,a[k])))
        self.assertTrue(same(a[-1]))

    def test_05_transport_for_tetrahedral_polynomial(self):
        q=qtet();S=x*(x-1);theta=1/x+s.Rational(4,3)/(x-1)
        a=get_p(4,S,theta,q,s.Integer(1));F=polynomial_F(4,S,a)
        self.assertEqual(s.degree(F,t),4)
        self.assertTrue(same(transport(F,4,S,theta,q)))
        self.assertTrue(same(s.LC(s.Poly(F,t)),-S**4))
        # F is nonconstant and squarefree over Q(x): roots satisfy Riccati.
        self.assertTrue(same(s.gcd(s.Poly(F,t),s.Poly(s.diff(F,t),t)).as_expr(),1))

    def test_06_rational_case_can_pass_primitive_recursion(self):
        q=2/x**2;S=x
        for n in (4,6,12):
            theta=s.Rational(n,2)/x
            a=get_p(n,S,theta,q,s.Integer(1))
            self.assertTrue(same(a[-1]),str((n,a[-1])))
            F=polynomial_F(n,S,a)
            self.assertEqual(s.degree(F,t),n)
            self.assertTrue(same(transport(F,n,S,theta,q)))
            for root in (2/x,-1/x):
                self.assertTrue(same(F.subs(t,root)),str((n,root)))

    def test_07_infinity_order_greater_than_two(self):
        # E∞(n) for q decaying faster than 1/x²: local b=0.
        self.assertEqual(local_set(4,s.Integer(0)),[0,3,6,9,12])
        self.assertEqual(local_set(6,s.Integer(0)),[0,2,4,6,8,10,12])
        self.assertEqual(local_set(12,s.Integer(0)),list(range(13)))

    def test_08_airy_and_poles_obstructions(self):
        q=x
        self.assertEqual(s.degree(s.denom(q),x)-s.degree(s.numer(q),x),-1)
        q2=1/x**3
        den=s.factor_list(s.denom(q2))[1]
        self.assertEqual(den,[(x,3)])

    def test_09_case_two_distinct_from_three(self):
        q=x+s.Rational(5,16)/x**2
        r=s.sqrt(x)-1/(4*x)
        self.assertTrue(same(s.diff(r,x)+r*r,q))
        self.assertEqual(s.degree(s.denom(q),x)-s.degree(s.numer(q),x),-1)

    def test_10_recurrence_is_linear_in_monic_p(self):
        q=qtet();S=x*(x-1);theta=1/x+s.Rational(4,3)/(x-1)
        a,b=s.symbols("a b")
        for n in (4,):
            out=get_p(n,S,theta,q,x*x+a*x+b)[-1]
            self.assertTrue(same(s.diff(out,a,2)))
            self.assertTrue(same(s.diff(out,b,2)))
            self.assertTrue(same(s.diff(out,a,b)))

    def test_11_source_labels_and_scope(self):
        data=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),22)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        self.assertGreaterEqual(data.count(r"\begin{proof}"),3)
        for tag in ("aa:tw:kov3-classification","aa:tw:kov3-local-sets",
                    "aa:lem:kov3-transport","aa:lem:kov3-roots",
                    "aa:eq:kov3-recurrence","aa:prz:kov3-tetrahedral"):
            self.assertIn(r"\label{"+tag+"}",data)
        self.assertIn("cytowany",data.lower())
if __name__=="__main__":
    unittest.main()
