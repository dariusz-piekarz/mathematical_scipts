#!/usr/bin/env python3
"""AA-48 independent model: exact Laurent arithmetic on fractions.Fraction.

No SymPy, NumPy, floating point, or CAS in this suite.
"""
from fractions import Fraction as Q
from pathlib import Path
import re
import unittest
from itertools import product

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"chapters/pl/abstract_algebra/48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex"

def add(p,q):
    output=dict(p)
    for k,v in q.items():
        output[k]=output.get(k,Q(0))+v
    return {k:v for k,v in output.items() if v}
def multiply(p,q):
    result={}
    for k,v in p.items():
        for h,w in q.items():
            result[k+h]=result.get(k+h,Q(0))+v*w
    return {k:v for k,v in result.items() if v}
def derive(p):
    return {k-1:Q(k)*v for k,v in p.items() if k!=0 and v!=0}
def riccati(p):
    return add(derive(p),multiply(p,p))
def value(p,x):
    return sum((v*x**k for k,v in p.items()),Q(0))

class AA48IndependentLaurent(unittest.TestCase):
    def test_01_regular_potential_forces_residue_one(self):
        for c in (Q(-3),Q(-1),Q(0),Q(1),Q(2),Q(4)):
            p={-1:c,0:Q(2)}
            q=riccati(p)
            self.assertEqual(q.get(-2,Q(0)),c*(c-1))
            if c==1:
                self.assertNotIn(-2,q)
                self.assertEqual(q.get(-1,Q(0)),4)

    def test_02_order_two_local_quadratic(self):
        for c in (Q(-4),Q(-1),Q(2),Q(3),Q(5,2)):
            q=riccati({-1:c})
            self.assertEqual(q.get(-2,Q(0)),c*(c-1))
        self.assertEqual(riccati({-1:Q(2)}),{-2:Q(2)})
        self.assertEqual(riccati({-1:Q(-1)}),{-2:Q(2)})

    def test_03_high_even_order_local_recursion(self):
        # Principal parts for m=2,3,4 and a nonzero leading coefficient.
        for m,c in product(range(2,5),[Q(-3,2),Q(1),Q(2)]):
            r={-m:c,-(m-1):Q(3,2)}
            q=riccati(r)
            self.assertEqual(min(q),-2*m)
            self.assertEqual(q[-2*m],c*c)
            # At x^(-(2m-1)): 2c*c_{-m+1}, plus derivative for m=2.
            expected=2*c*Q(3,2)
            if m==2: expected-=m*c
            self.assertEqual(q[-(2*m-1)],expected)

    def test_04_fourth_order_explicit(self):
        r={-2:Q(1)}
        self.assertEqual(riccati(r),{-4:Q(1),-3:Q(-2)})
        for z in (Q(-2),Q(-1,2),Q(1,3),Q(5)):
            self.assertEqual(value(riccati(r),z),1/z**4-2/z**3)

    def test_05_polynomial_part_and_movable_residue(self):
        # r=x+1/x at infinity has polynomial part x, Laurent n=1.
        r={1:Q(1),-1:Q(1)}
        self.assertEqual(riccati(r),{2:Q(1),0:Q(3)})
        for z in (Q(-3),Q(-1),Q(1,2),Q(2)):
            self.assertEqual(value(riccati(r),z),z*z+3)

    def test_06_infinity_vanishing_case(self):
        for rho,beta,n in [(Q(2),Q(2),0),(Q(-1),Q(2),0),
                           (Q(0),Q(0),0),(Q(0),Q(0),1)]:
            self.assertEqual((rho+n)*(rho+n-1),beta)
        for rho,beta in ((Q(2),Q(2)),(Q(-1),Q(2)),(Q(0),Q(0))):
            possible=[n for n in range(0,9)
                      if (rho+n)*(rho+n-1)==beta]
            self.assertGreater(len(possible),0)

    def test_07_rational_pole_fraction_examples(self):
        # r=x+1/(x-1), q=x^2+3+2/(x-1):
        # calculate with z=x-1, r=z+1+1/z.
        r={1:Q(1),0:Q(1),-1:Q(1)}
        q=riccati(r)
        # x=z+1 => x^2+3+2/z = z^2+2z+4+2/z.
        expected={2:Q(1),1:Q(2),0:Q(4),-1:Q(2)}
        self.assertEqual(q,expected)
        for z in (Q(-3),Q(-1),Q(1,2),Q(2)):
            self.assertEqual(value(q,z),(z+1)**2+3+2/z)

    def test_08_rational_multiple_pole_singularity_filter(self):
        # Fixed singular x=0: u=-1/x, P=x^3 leads back to r=2/x.
        # But P(0)=0, hence this P is forbidden in the branch with u=-1/x.
        for z in (Q(-2),Q(-1,2),Q(1),Q(3)):
            u=-1/z
            p_log=3/z
            r=u+p_log
            self.assertEqual(r,2/z)
            self.assertEqual(-2/z**2+r*r,2/z**2)
        self.assertEqual(0**3,0)

    def test_09_source_labels(self):
        data=SOURCE.read_text(encoding="utf-8")
        labs=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(len(labs),22)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        self.assertGreaterEqual(data.count(r"\begin{proof}"),6)
        self.assertIn("nieujemną liczbą całkowitą",data)

if __name__=="__main__":
    unittest.main()
