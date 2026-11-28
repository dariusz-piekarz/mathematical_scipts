#!/usr/bin/env python3
"""AA-49 independent exact polynomial / Laurent arithmetic, no SymPy."""
from fractions import Fraction as Q
from pathlib import Path
import re
import unittest

SRC=Path(__file__).resolve().parents[2]/"chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex"

def add(A,B):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,Q(0))+v
    return {k:v for k,v in C.items() if v!=0}
def neg(A):return {k:-v for k,v in A.items()}
def sub(A,B):return add(A,neg(B))
def mul(A,B):
    C={}
    for k,a in A.items():
        for l,b in B.items():C[k+l]=C.get(k+l,Q(0))+a*b
    return {k:v for k,v in C.items() if v!=0}
def diff(A):return {k-1:k*v for k,v in A.items() if k!=0 and v!=0}
def scale(A,z):return {k:z*v for k,v in A.items() if z*v!=0}
def trace(phi,q):
    return sub(add(add(diff(diff(phi)),scale(mul(phi,diff(phi)),3)),mul(mul(phi,phi),phi)),
               add(scale(mul(q,phi),4),scale(diff(q),2)))
def disc(phi,q):
    return sub(sub(scale(q,4),scale(diff(phi),2)),mul(phi,phi))
def auxiliary(P,theta,q):
    thp=diff(theta)
    c1=sub(add(scale(mul(theta,theta),3),scale(thp,3)),scale(q,4))
    c0=sub(add(add(diff(thp),scale(mul(theta,thp),3)),mul(mul(theta,theta),theta)),
           add(scale(mul(q,theta),4),scale(diff(q),2)))
    return add(add(add(diff(diff(diff(P))),scale(mul(theta,diff(diff(P))),3)),
                   mul(c1,diff(P))),mul(c0,P))
def val(A,x):return sum((v*x**k for k,v in A.items()),Q(0))

class AA49FractionIndependent(unittest.TestCase):
    def test_01_first_trace_and_delta(self):
        q={1:Q(1),-2:Q(5,16)};phi={-1:Q(-1,2)}
        self.assertEqual(trace(phi,q),{})
        self.assertEqual(disc(phi,q),{1:Q(4)})
        self.assertEqual(add(diff(disc(phi,q)),scale(mul(phi,disc(phi,q)),2)),{})
    def test_02_first_third_order_P(self):
        q={1:Q(1),-2:Q(5,16)}
        theta={-1:Q(-1,2)}
        self.assertEqual(auxiliary({0:Q(1)},theta,q),{})
    def test_03_positive_degree_P(self):
        q={-1:Q(1,4),-2:Q(5,16)}
        theta={-1:Q(-1,2)}
        P={1:Q(1),0:Q(-1)}
        self.assertEqual(auxiliary(P,theta,q),{})
        for xx in (Q(-3),Q(-1),Q(1,3),Q(2),Q(5)):
            # phi = -1/(2x)+1/(x-1), Delta=x/(x-1)^2.
            p=-1/(2*xx)+1/(xx-1)
            pp=1/(2*xx**2)-1/(xx-1)**2
            qq=1/(4*xx)+Q(5,16)/xx**2
            self.assertEqual(4*qq-2*pp-p*p,xx/(xx-1)**2)
    def test_04_infinity_one_order_case(self):
        q={-1:Q(1),-2:Q(-3,16)}
        theta={-1:Q(1,2)}
        self.assertEqual(trace(theta,q),{})
        self.assertEqual(disc(theta,q),{-1:Q(4)})
        self.assertEqual(auxiliary({0:Q(1)},theta,q),{})
    def test_05_quadratic_local_E_sets(self):
        def candidates(b):
            # all b used are exact squares 1+4b
            roots={Q(5,16):Q(3,2),Q(-3,16):Q(1,2)}
            t=roots[b]
            return sorted({int(z) for z in (Q(2),Q(2)+2*t,Q(2)-2*t)
                           if z.denominator==1})
        self.assertEqual(candidates(Q(5,16)),[-1,2,5])
        self.assertEqual(candidates(Q(-3,16)),[1,2,3])
        self.assertEqual(((-1)-(-1))//2,0)
        self.assertEqual((1-(-1))//2,1)
        self.assertEqual((1-1)//2,0)
    def test_06_symmetric_square_direct(self):
        # q=2/x^2, v=x (solutions x^2 and x^-1).
        q={-2:Q(2)};v={1:Q(1)}
        self.assertEqual(sub(sub(diff(diff(diff(v))),
                                 scale(mul(q,diff(v)),4)),
                             scale(mul(diff(q),v),2)),{})
    def test_07_repeated_roots_from_discriminant(self):
        # Rational roots w=2/x, -1/x; trace 1/x; disc 9/x^2.
        phi={-1:Q(1)};q={-2:Q(2)}
        self.assertEqual(trace(phi,q),{})
        self.assertEqual(disc(phi,q),{-2:Q(9)})
        for xx in (Q(1,2),Q(1),Q(3)):
            delta=Q(3)/xx
            roots=((Q(1)/xx+delta)/2,(Q(1)/xx-delta)/2)
            self.assertEqual(roots,(Q(2)/xx,-Q(1)/xx))
    def test_08_airys_negative_degree(self):
        self.assertEqual((-1-0)*Q(1,2),Q(-1,2))
        self.assertNotEqual(Q(-1,2).denominator,1)
    def test_09_sampled_riccati_quadratic_solutions(self):
        # w=u ± g, with g'= -2*u*g; evaluate exact rational x=a^2.
        for a in (Q(1),Q(2),Q(3),Q(5)):
            xx=a*a
            u=-1/(4*xx); up=1/(4*xx**2)
            g=a; gp=1/(2*a)
            q=xx+Q(5,16)/xx**2
            for sign in (-1,1):
                w=u+sign*g
                wp=up+sign*gp
                self.assertEqual(wp+w*w,q)
    def test_10_tex_labels(self):
        s=SRC.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),24)
        self.assertEqual(s.count(r"\begin{proof}"),s.count(r"\end{proof}"))
        self.assertIn("przypadek Kovacica",s)
if __name__=="__main__":
    unittest.main()
