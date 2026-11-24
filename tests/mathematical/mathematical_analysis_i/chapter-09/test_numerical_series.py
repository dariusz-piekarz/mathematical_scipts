from fractions import Fraction as F
from math import factorial
import itertools
import unittest

class Chapter09(unittest.TestCase):
    def test_partial_sum_and_tail_indexing(self):
        a=[F((-1)**n,n) for n in range(1,13)]
        S=[F(0)]
        for x in a: S.append(S[-1]+x)
        for p in range(1,len(a)+1):
            for q in range(p,len(a)+1):
                self.assertEqual(sum(a[p-1:q]),S[q]-S[p-1])

    def test_geometric_finite_identity(self):
        for q in (F(0),F(1,2),F(-2,3),F(1),F(2),F(-1)):
            for N in range(20):
                s=sum(q**n for n in range(N+1))
                self.assertEqual((1-q)*s,1-q**(N+1))
                if abs(q)<1:
                    self.assertEqual(1/(1-q)-s,q**(N+1)/(1-q))

    def test_telescoping_and_harmonic(self):
        for N in range(1,61):
            self.assertEqual(sum(F(1,n*(n+1)) for n in range(1,N+1)),1-F(1,N+1))
            self.assertGreaterEqual(sum(F(1,n) for n in range(N+1,2*N+1)),F(1,2))

    def test_condensation_block_bounds(self):
        for p in (1,2,3):
            for k in range(8):
                block=sum(F(1,n**p) for n in range(2**k,2**(k+1)))
                self.assertLessEqual(F(2**k,2**((k+1)*p)),block)
                self.assertLessEqual(block,F(2**k,2**(k*p)))
                self.assertEqual(F(2**k,2**(k*p)),F(2)**((1-p)*k))

    def test_absolute_remainder_bound(self):
        q=F(2,3)
        for N in range(10):
            for M in range(N+1,21):
                self.assertLessEqual(abs(sum((-q)**n for n in range(N+1,M+1))),q**(N+1)/(1-q))

    def test_ratio_induction_and_boundary(self):
        for k in range(1,15):
            self.assertLessEqual(F(1,factorial(k+2)),F(1,2)*F(1,3)**k)
            self.assertEqual(F(k,k+1)**2,F(1,(k+1)**2)/F(1,k*k))
            self.assertEqual(F(k,k+1),F(1,k+1)/F(1,k))

    def test_root_boundary_polynomial_estimate(self):
        for delta in (F(1,4),F(1,2),F(1),F(2)):
            for n in range(4,41):
                self.assertGreaterEqual((1+delta)**n,F(n*(n-1)*(n-2),6)*delta**3)
                self.assertGreaterEqual(F(n*(n-1)*(n-2),6)*delta**3,F(n**3,24)*delta**3)
            n=max(4,int(24/delta**3)+1)
            self.assertGreater(F(n**3,24)*delta**3,n*n)

    def test_factorial_tail(self):
        for N in range(1,15):
            for M in range(N+1,N+12):
                self.assertLessEqual(sum(F(1,factorial(n)) for n in range(N+1,M+1)),F(1,N*factorial(N)))

if __name__=="__main__": unittest.main()
