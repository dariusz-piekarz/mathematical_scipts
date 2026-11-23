#!/usr/bin/env python3
"""AA-50: independent exact Fraction-polynomial recurrence model without SymPy."""
from fractions import Fraction as Q
from pathlib import Path
import unittest,re

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex"

def clean(v):
    v=list(v)
    while len(v)>1 and v[-1]==0:v.pop()
    return v or [Q(0)]
def add(a,b):
    return clean([(a[i] if i<len(a) else Q(0))+
                  (b[i] if i<len(b) else Q(0))
                  for i in range(max(len(a),len(b)))])
def mul(a,b):
    o=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return clean(o)
def neg(a):return [-z for z in a]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return clean([c*z for z in a])
def deriv(a):return clean([i*a[i] for i in range(1,len(a))])
def at(a,x):return sum((v*x**i for i,v in enumerate(a)),Q(0))
def derivative_product(a,b):
    return add(mul(deriv(a),b),mul(a,deriv(b)))

S=[Q(0),Q(-1),Q(1)]
SH=[Q(-1),Q(7,3)]   # S*theta = 7x/3-1.
SQ=[Q(-3,16),Q(3,16),Q(-2,9)] # S^2*q.

def power(a,n):
    v=[Q(1)]
    for _ in range(n):v=mul(v,a)
    return v

def recurrence(n,P,S=S,SH=SH,SQ=SQ):
    result={n+1:[Q(0)],n:neg(P)}
    for i in range(n,-1,-1):
        A=neg(mul(S,deriv(result[i])))
        B=mul(sub(scale(deriv(S),Q(n-i)),SH),result[i])
        C=scale(mul(SQ,result[i+1]),-Q((n-i)*(i+1)))
        result[i-1]=add(add(A,B),C)
    return result

def local_set(n,b):
    # Exact rational sqrt case via integer isqrt for particular b values.
    from math import isqrt
    delta=1+4*b
    root_num=isqrt(delta.numerator);root_den=isqrt(delta.denominator)
    assert root_num**2==delta.numerator and root_den**2==delta.denominator
    root=Q(root_num,root_den)
    values=[Q(6)+Q(12*k,n)*root for k in range(-n//2,n//2+1)]
    return sorted({int(v) for v in values if v.denominator==1})

class AA50IndependentFraction(unittest.TestCase):
    def test_01_exact_local_lists(self):
        self.assertEqual(local_set(4,Q(-3,16)),[3,6,9])
        self.assertEqual(local_set(4,Q(-2,9)),[4,5,6,7,8])
        self.assertEqual(local_set(4,Q(0)),[0,3,6,9,12])
        self.assertEqual(local_set(6,Q(0)),[0,2,4,6,8,10,12])
        self.assertEqual(local_set(12,Q(0)),list(range(13)))

    def test_02_infinity_and_degree(self):
        self.assertEqual(Q(4,12)*(7-3-4),0)
        self.assertLess(Q(4,12)*(4-9-8),0)
        self.assertEqual(Q(4,12)*(8-3-4),Q(1,3))
        self.assertEqual(SH, [Q(-1),Q(7,3)])

    def test_03_S_squared_q_from_partial_fractions(self):
        # S=x(x-1), q=-3/(16x²)-2/(9(x-1)²)+3/(16x(x-1)).
        for x in (Q(-2),Q(-1,2),Q(1,3),Q(2),Q(7,3)):
            q=-Q(3,16)/x**2-Q(2,9)/(x-1)**2+Q(3,16)/(x*(x-1))
            self.assertEqual(at(SQ,x),at(S,x)**2*q)

    def test_04_explicit_recurrence_tetrahedron(self):
        p=recurrence(4,[Q(1)])
        expected={
         4:[Q(-1)],
         3:[Q(-1),Q(7,3)],
         2:[Q(-3,4),Q(41,12),Q(-4)],
         1:[Q(-3,8),Q(5,2),Q(-409,72),Q(40,9)],
         0:[Q(-3,32),Q(13,16),Q(-257,96),Q(871,216),Q(-64,27)],
         -1:[Q(0)]
        }
        for j,values in expected.items():
            self.assertEqual(p[j],clean(values),(j,p[j],values))

    def test_05_full_recurrence_zero(self):
        self.assertEqual(recurrence(4,[Q(1)])[-1],[Q(0)])
        for x in (Q(-2),Q(-1),Q(0),Q(1,2),Q(2),Q(5)):
            self.assertEqual(at(recurrence(4,[Q(1)])[-1],x),0)

    def test_06_simplified_polynomial_F_specialization(self):
        p=recurrence(4,[Q(1)])
        # U=S*T; F = sum P_i U^i/(4-i)!.
        from math import factorial
        for x in (Q(-1),Q(2),Q(3)):
            coeff=[at(p[i],x)/factorial(4-i) for i in range(5)]
            self.assertEqual(coeff[-1],Q(-1))
            self.assertNotEqual(coeff[0],Q(0))
            self.assertEqual(coeff[3],at(p[3],x))
            self.assertEqual(coeff[4],Q(-1))

    def test_07_linearity_of_recurrence_operator(self):
        A=[Q(2),Q(-1),Q(3)]
        B=[Q(-1),Q(2)]
        pA=recurrence(4,A)[-1]
        pB=recurrence(4,B)[-1]
        C=add(scale(A,Q(3,2)),scale(B,Q(-2)))
        pC=recurrence(4,C)[-1]
        self.assertEqual(pC,add(scale(pA,Q(3,2)),scale(pB,Q(-2))))

    def test_08_rational_model_n4_n6_n12(self):
        # q=2/x², S=x, Sθ=(n/2), S²q=2.
        for n in (4,6,12):
            pp=recurrence(n,[Q(1)],[Q(0),Q(1)],[Q(n,2)],[Q(2)])
            self.assertEqual(pp[-1],[Q(0)])
            self.assertEqual(pp[n],[Q(-1)])
            for i in range(n):
                self.assertTrue(all(isinstance(z,Q) for z in pp[i]))

    def test_09_transport_identity_at_samples(self):
        # Independent numerical-EXACT polynomial coefficient identity.
        # For A_i=S^i P_i/(n-i)!, coefficient of T^i:
        # A_i'+(i+1)q A_{i+1}-(i-1)A_{i-1}
        # =-n A_{i-1}+(nS'/S-theta)A_i.
        from math import factorial
        p=recurrence(4,[Q(1)])
        n=4
        A={i:scale(mul([Q(1)] if i==0 else power(S,i),p[i]),Q(1,factorial(n-i)))
           for i in range(n+1)}
        for z in (Q(-2),Q(-1,2),Q(1,3),Q(2)):
            qv=at(SQ,z)/at(S,z)**2
            thov=at(SH,z)/at(S,z)
            mu=n*at(deriv(S),z)/at(S,z)-thov
            for i in range(n+1):
                a=at(A[i],z)
                ap=at(deriv(A[i]),z)
                up=at(A[i+1],z) if i<n else Q(0)
                down=at(A[i-1],z) if i>0 else Q(0)
                self.assertEqual(ap+(i+1)*qv*up-(i-1)*down,
                                 -n*down+mu*a,(i,z))
    def test_10_source_regression(self):
        data=SOURCE.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",data)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertGreaterEqual(len(labels),22)
        self.assertGreaterEqual(data.count(r"\begin{proof}"),3)
        self.assertEqual(data.count(r"\begin{proof}"),data.count(r"\end{proof}"))
        self.assertIn("klasyczny",data)
if __name__=="__main__":
    unittest.main()
