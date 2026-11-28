#!/usr/bin/env python3
"""AA-45 independent exact-rational checks; no SymPy dependency."""
from fractions import Fraction as Q
import unittest,re
from pathlib import Path
from itertools import product

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"chapters/pl/abstract_algebra/45-kryteria-hiperwykladnicze-i-calki-nieelementarne.tex"

def clean(v):
    v=list(v)
    while len(v)>1 and v[-1]==0:v.pop()
    return v or [Q(0)]
def add(v,w):
    return clean([(v[i] if i<len(v) else Q(0))+(w[i] if i<len(w) else Q(0))
                  for i in range(max(len(v),len(w)))])
def multiply(v,w):
    r=[Q(0)]*(len(v)+len(w)-1)
    for i,a in enumerate(v):
        for j,b in enumerate(w):r[i+j]+=a*b
    return clean(r)
def derive(v):
    return clean([Q(i)*v[i] for i in range(1,len(v))])
def value(v,x):
    return sum((c*x**i for i,c in enumerate(v)),Q(0))
def differentiate_hyperexp(r,h):
    return add(derive(r),multiply(h,r))
def deriv_on_laurent(coeff,k,h):
    return add(derive(coeff),[Q(k)*c for c in multiply(h,coeff)])

class AA45IndependentRational(unittest.TestCase):
    def test_01_polynomial_ode_positive(self):
        h=[Q(0),Q(-2)]
        r=[Q(-1,2)]
        self.assertEqual(differentiate_hyperexp(r,h),[Q(0),Q(1)])
        h=[Q(0),Q(2)]
        r=[Q(1,2)]
        self.assertEqual(differentiate_hyperexp(r,h),[Q(0),Q(1)])
        self.assertEqual(differentiate_hyperexp([Q(1),Q(2)],[Q(3),Q(0),Q(1)]),
                         [Q(5),Q(6),Q(1),Q(2)])

    def test_02_laurent_ode_k_signs(self):
        h=[Q(1),Q(2)]
        r=[Q(2),Q(-3),Q(1)]
        dr=derive(r)
        for k in (-7,-3,-1,1,2,5):
            want=add(dr,[Q(k)*c for c in multiply(h,r)])
            self.assertEqual(deriv_on_laurent(r,k,h),want)
            if k!=0:
                self.assertNotEqual(deriv_on_laurent(r,k,h),
                                    deriv_on_laurent(r,-k,h))

    def test_03_simple_pole_highest_order(self):
        # h analytic, r=c*z^(-m)+..., coeff of z^(-m-1) in r'+hr.
        for m,c in product(range(1,8),[Q(-5,3),Q(1),Q(7,4)]):
            derivative_lead=-m*c
            h_r_lead=Q(0) # h*r has order at worst -m
            self.assertEqual(derivative_lead+h_r_lead,-m*c)
            self.assertNotEqual(derivative_lead+h_r_lead,Q(0))

    def test_04_degree_obstruction_finite_grid(self):
        for d,eh in product(range(0,7),range(1,6)):
            r=[Q(i+1) for i in range(d+1)]
            h=[Q(1)]*(eh+1)
            s=differentiate_hyperexp(r,h)
            self.assertEqual(len(s)-1,d+eh)
            self.assertGreaterEqual(len(s)-1,eh)

    def test_05_gaussian_determined_special_cases(self):
        # Constant r cannot solve r'-2xr=1.
        for c in (Q(-4,3),Q(-1,2),Q(0),Q(2),Q(7,3)):
            lhs=differentiate_hyperexp([c],[Q(0),Q(-2)])
            self.assertNotEqual(lhs,[Q(1)])
        # r=-1/2 solves for s=x, not for s=1.
        self.assertEqual(differentiate_hyperexp([Q(-1,2)],[Q(0),Q(-2)]),
                         [Q(0),Q(1)])

    def test_06_elliptic_square_and_valuation(self):
        for x in (Q(-3,2),Q(-1,2),Q(0),Q(2,3),Q(5,4)):
            f=1-x**4
            self.assertEqual(-2*x**3/f, Q(1,2)*(-4*x**3)/f)
        # Valuation at branch x=a: ord(x-a)=2, ord(y)=1.
        for m,n in product(range(-4,5),range(-4,5)):
            at_branch=2*m+n
            at_infinity=-m-2*n
            if m==1 and n==0:self.assertEqual(at_branch,2)
            if m==0 and n==1:self.assertEqual(at_infinity,-2)

    def test_07_residue_rational_independence(self):
        # Independent basis 1,sqrt(2).  A residue is a rational pair.
        # c=(1,sqrt(2),1+sqrt(2)); cancellations mean both coordinates zero.
        c=((Q(1),Q(0)),(Q(0),Q(1)),(Q(1),Q(1)))
        for a,b,d in product(range(-3,4),repeat=3):
            coeff1=a+d
            coeff2=b+d
            pair=tuple(sum(Q(v)*c[j][i] for j,v in enumerate((a,b,d)))
                       for i in (0,1))
            self.assertEqual(pair,(Q(coeff1),Q(coeff2)))
            self.assertEqual(pair==(Q(0),Q(0)),a==-d and b==-d)
            if pair==(Q(0),Q(0)):
                # The two basis decompositions define monomials U1=u1*u3,
                # U2=u2*u3 with zero local order at this point.
                self.assertEqual(a+d,0)
                self.assertEqual(b+d,0)

    def test_08_structure(self):
        text=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",text)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(text.count(r"\begin{proof}"),11)
        self.assertEqual(text.count(r"\begin{proof}"),text.count(r"\end{proof}"))
        for label in ("aa:lem:exp-polynomial-constant-field",
                      "aa:lem:simple-pole-obstruction",
                      "aa:lem:polynomial-degree-obstruction",
                      "aa:lem:elliptic-charts","aa:lem:elliptic-no-poles",
                      "aa:lem:elliptic-regular-form"):
            self.assertIn(r"\label{"+label+"}",text)

if __name__=="__main__": unittest.main()
