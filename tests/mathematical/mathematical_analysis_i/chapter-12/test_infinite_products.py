from fractions import Fraction as F
from itertools import product, permutations
from math import prod
import unittest

class Chapter12(unittest.TestCase):
    def test_telescoping_products(self):
        for N in range(2,51):
            self.assertEqual(prod(1-F(1,n) for n in range(2,N+1)),F(1,N))
            self.assertEqual(prod(1+F(1,n) for n in range(2,N+1)),F(N+1,2))
            self.assertEqual(prod(1-F(1,n*n) for n in range(2,N+1)),F(N+1,2*N))

    def test_tail_ratio(self):
        u=[F(1)+F((-1)**n,2**n) for n in range(1,16)]
        P=[prod(u[:n]) for n in range(16)]
        for p in range(1,16):
            for q in range(p,16):
                self.assertEqual(prod(u[p-1:q]),P[q]/P[p-1])
                self.assertEqual(abs(P[q]-P[p-1]),abs(P[p-1])*abs(prod(u[p-1:q])-1))

    def test_finite_estimates(self):
        vals=[F(i,10) for i in range(-3,4)]
        for z in product(vals,repeat=4):
            s=sum(abs(t) for t in z)
            major=prod(1+abs(t) for t in z)
            self.assertLessEqual(abs(prod(1+t for t in z)-1),major-1)
            if s<1:
                self.assertLessEqual(major,1/(1-s))
                self.assertLessEqual(abs(prod(1+t for t in z)-1),s/(1-s))

    def test_positive_finite_bounds(self):
        for t in product([F(0),F(1,4),F(1,2),F(1)],repeat=4):
            self.assertGreaterEqual(prod(1+x for x in t),1+sum(t))
            self.assertGreaterEqual(prod(1-x for x in t),1-sum(t))
            self.assertLessEqual(prod(1-x for x in t),1/(1+sum(t)))

    def test_geometric_tail_error(self):
        for N in range(1,13):
            for M in range(N+1,N+10):
                self.assertLessEqual(abs(prod(1+F(1,2**n) for n in range(N+1,M+1))-1),F(1,2**N-1))
        self.assertLess(F(1,1023),F(1,1000))

    def test_rearrangement_finite_tail(self):
        a=[F((-1)**n,2**n) for n in range(1,7)]
        s=sum(abs(v) for v in a[2:])
        P=prod(1+v for v in a[:2])
        for p in permutations(range(6)):
            used=set()
            Q=F(1)
            for i in p:
                Q*=1+a[i]; used.add(i)
                if {0,1}<=used:
                    self.assertLessEqual(abs(Q/P-1),s/(1-s))

    def test_conditional_pairs(self):
        P=F(1); S=F(0)
        for k in range(1,61):
            t=F(1,k)
            P*=1+t; S+=t
            self.assertEqual(P,1+t)
            self.assertEqual(S,1)
            P/=1+t; S-=t/(1+t)
            self.assertEqual(P,1)
            self.assertEqual(S,1-F(1,k+1))

    def test_opposite_pair_and_reciprocal_algebra(self):
        # Rational witnesses for the identities used with real square roots.
        for m in range(1,51):
            t=F(1,m)
            self.assertEqual((1+t)*(1-t),1-t*t)
            self.assertEqual(t-t/(1+t),t*t/(1+t))
            self.assertGreaterEqual(t*t/(1+t),t*t/2)
        self.assertEqual(prod(F(k,k+1) for k in range(1,51)),F(1,51))

    def test_zero_factor_and_sign_convention(self):
        self.assertEqual(prod([F(2),F(0),F(3)]),0)
        self.assertEqual(prod([-2,-1,F(1,2),F(3,2)]),F(3,2))
        self.assertEqual(prod([-1]*5),-1)
        self.assertEqual(prod([-1]*6),1)

if __name__=="__main__": unittest.main()
