#!/usr/bin/env python3
"""Regression for AA-50: nonmonic products of distinct Riccati factors."""
import unittest
import sympy as s

x,t=s.symbols("x t")
q=2/x**2
def D(F):
    return s.diff(F,x)+(q-t*t)*s.diff(F,t)
def same(a,b=0):
    return s.cancel(s.together(a-b))==0

class NonmonicFactors(unittest.TestCase):
    def test_mixed_factors(self):
        f,g=t-2/x,t+1/x
        self.assertTrue(same(D(f),-(t+2/x)*f))
        self.assertTrue(same(D(g),-(t-1/x)*g))
        for u in (x,x*x+1,1/x):
            for m,n in ((1,1),(2,3),(4,1)):
                with self.subTest(u=u,m=m,n=n):
                    F=u*f**m*g**n
                    H=s.cancel(D(F)/F)
                    old=m*D(f)/f+n*D(g)/g
                    self.assertTrue(same(H,s.diff(u,x)/u+old))
                    self.assertFalse(same(H,old))
                    self.assertEqual(s.Poly(H,t).degree(),1)

    def test_riccati_roots(self):
        for w in (2/x,-1/x):
            self.assertTrue(same(s.diff(w,x)+w*w,q))

if __name__=="__main__":
    unittest.main()
