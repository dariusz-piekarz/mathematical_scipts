"""Finite witnesses for Radon regularity estimates and cutoff functions."""
from fractions import Fraction as Q
import unittest


class RadonRegularity13(unittest.TestCase):
    def test_finite_regular_error_budget(self):
        for N in (1,5,30):
            errors=sum(Q(1,2**(n+3)) for n in range(1,N+1))
            self.assertLess(2*errors+Q(1,4),Q(1,2))

    def test_compact_inner_approximation(self):
        E={1,2,3}
        U={1,2,3,4}
        F={1,2,4}
        W={4,5}
        K=F-W
        self.assertLessEqual(K,E)
        self.assertGreaterEqual(len(K),len(F)-len(W))

    def test_cover_localization(self):
        E={0,2,4}
        Vs=[{0,1,2},{2,3,4}]
        Bs=[Vs[0],Vs[1]-Vs[0]]
        Us=[{0,2,3},{0,4,5}]
        U=set.union(*(u&v for u,v in zip(Us,Vs)))
        self.assertLessEqual(E,U)
        self.assertLessEqual(len(U-E),sum(len((u&v)-(E&b)) for u,v,b in zip(Us,Vs,Bs)))

    def test_distance_cutoff(self):
        # K={0}, V=(-2,2), X=R.
        for x in (Q(-3),Q(-2),Q(-1),Q(0),Q(1,2),Q(2),Q(3)):
            a=max(Q(0),2-abs(x))
            b=abs(x)
            self.assertGreater(a+b,0)
            f=a/(a+b)
            self.assertTrue(0<=f<=1)
            if x==0:
                self.assertEqual(f,1)
            if abs(x)>=2:
                self.assertEqual(f,0)

    def test_cutoff_integral_squeeze(self):
        weights=[Q(2),Q(1,3),Q(5),Q(4)]
        K=[1,0,0,0]
        U=[1,1,1,0]
        f=[Q(1),Q(1,2),Q(1,5),Q(0)]
        integrate=lambda g:sum(w*v for w,v in zip(weights,g))
        self.assertLessEqual(integrate(K),integrate(f))
        self.assertLessEqual(integrate(f),integrate(U))


if __name__=="__main__":
    unittest.main()
