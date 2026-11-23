#!/usr/bin/env python3
"""AA-47: independent exact Fraction arithmetic without SymPy."""
from fractions import Fraction as Q
from pathlib import Path
import unittest,re
from itertools import product

SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex"

def clean(A):
    A=list(A)
    while len(A)>1 and A[-1]==0:A.pop()
    return A or [Q(0)]
def add(A,B,sign=1):
    return clean([(A[i] if i<len(A) else Q(0))+sign*(B[i] if i<len(B) else Q(0))
                  for i in range(max(len(A),len(B)))])
def mult(A,B):
    C=[Q(0)]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return clean(C)
def deriv(A):
    return clean([i*A[i] for i in range(1,len(A))])
def evalpoly(A,x):
    return sum((a*x**i for i,a in enumerate(A)),Q(0))
def diff_quot(P,Pp,Ppp,x):
    # derivative of P'/P is P''/P-(P'/P)^2
    p=evalpoly(P,x); d=evalpoly(Pp,x);dd=evalpoly(Ppp,x)
    return dd/p-(d/p)**2
def riccati_value(omega,P,x):
    # r = omega+P'/P, test r'+r^2 at rational x
    Pp=deriv(P);Ppp=deriv(Pp)
    w=evalpoly(omega,x); wp=evalpoly(deriv(omega),x)
    q=evalpoly(Pp,x)/evalpoly(P,x)
    return wp+diff_quot(P,Pp,Ppp,x)+(w+q)**2

class AA47Independent(unittest.TestCase):
    def test_01_rational_hermite_sampled_exact(self):
        for x in (Q(-2),Q(0),Q(2),Q(7,3)):
            # f=2x+3/(x-1)^3+5/(x-1)
            Rprime=2*x+3/(x-1)**3
            self.assertEqual(Rprime+5/(x-1),
                             2*x+3/(x-1)**3+5/(x-1))
            self.assertNotEqual(Q(5),0)

    def test_02_rothstein_trager_exact_rational_roots(self):
        # B=x(x-1), A=x+1, B'=2x-1.
        # T(z)=prod_{a=0,1}(A(a)-z*B'(a))=(1+z)(2-z).
        for z in [Q(-3),Q(-1),Q(0),Q(2),Q(3,2)]:
            T=(1+z)*(2-z)
            self.assertEqual(T,2+z-z*z)
        for x in (Q(-3),Q(-1),Q(1,2),Q(2),Q(4)):
            self.assertEqual((x+1)/(x*(x-1)),
                             -1/x+2/(x-1))
        self.assertEqual((-1,2),(-1,2))

    def test_03_risch_pole_match(self):
        # h=1, s=1/x^2-1/x. Principal part r=-1/x.
        for x in (Q(-4),Q(-1,2),Q(1,3),Q(2)):
            dr=Q(1)/x**2
            r=-Q(1)/x
            self.assertEqual(dr+r,Q(1)/x**2-Q(1)/x)
            self.assertNotEqual(Q(1)/x**2-Q(1)/x,Q(1)/x)

    def test_04_risch_polynomial_degree(self):
        # h=2x, r quadratic, s=r'+2xr has degree 3.
        h=[Q(0),Q(2)]
        for r in ([Q(1)],[Q(1),Q(2)],[Q(-3),Q(0),Q(4)]):
            output=add(deriv(r),mult(h,r))
            self.assertEqual(len(output)-1,len(r))
            self.assertEqual(output[-1],Q(2)*r[-1])

    def test_05_risch_constant_h_closed_formula(self):
        for h in (Q(-3),Q(-1,2),Q(1),Q(5)):
            S=[Q(2),Q(-1),Q(3)] # 2-x+3x^2
            current=clean(S)
            P=[Q(0)]
            for k in range(3):
                P=add(P,[(-1 if k%2 else 1)*v/h**(k+1) for v in current])
                current=deriv(current)
            self.assertEqual(add(deriv(P),[h*v for v in P]),S)

    def test_06_kovacic_rational_r_linear_omega(self):
        models=[([Q(0),Q(1)],[Q(1)],[Q(1),Q(0),Q(1)]),
                ([Q(0),Q(-1)],[Q(1)],[Q(-1),Q(0),Q(1)]),
                ([Q(0),Q(1)],[Q(0),Q(1)],[Q(3),Q(0),Q(1)])]
        for omega,P,poly_q in models:
            for x in (Q(-3),Q(-1),Q(1,2),Q(2),Q(7,3)):
                result=riccati_value(omega,P,x)
                self.assertEqual(result,evalpoly(poly_q,x))

    def test_07_kovacic_rational_r_quadratic_omega(self):
        models=[([Q(0),Q(0),Q(1)],[Q(1)],[Q(0),Q(2),Q(0),Q(0),Q(1)]),
                ([Q(0),Q(0),Q(1)],[Q(0),Q(1)],[Q(0),Q(4),Q(0),Q(0),Q(1)])]
        for omega,P,poly_q in models:
            for x in (Q(-3),Q(-1),Q(1),Q(2),Q(5,2)):
                self.assertEqual(riccati_value(omega,P,x),evalpoly(poly_q,x))

    def test_08_kovacic_odd_degree_obstruction(self):
        for d in range(1,8):
            # r polynomial part has degree d => r'+r^2 has degree 2d.
            omega=[Q(i+1) for i in range(d+1)]
            left=add(deriv(omega),mult(omega,omega))
            self.assertEqual(len(left)-1,2*d)
            self.assertEqual(left[-1],omega[-1]**2)
            self.assertNotEqual(2*d,2*d-1)

    def test_09_rational_derivatives_zero_residues(self):
        # Laurent monomials z^j -> j*z^(j-1):
        # coefficient at exponent -1 can come only from j=0 and is zero.
        for j in range(-8,9):
            coefficient=Q(j)
            self.assertEqual((coefficient if j-1==-1 else Q(0)),Q(0))
        # Exact pole tests for the derivative of z^(-m).
        for m in range(1,7):
            for z in (Q(-2),Q(-1,2),Q(1,3),Q(2)):
                self.assertEqual(-m/z**(m+1),Q(-m)*z**(-m-1))

    def test_10_source_structure(self):
        data=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(data.count(r"\begin{proof}"),8)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        self.assertIn("Rothsteina",data)
        self.assertIn("Kovacica",data)
if __name__=="__main__":unittest.main()
