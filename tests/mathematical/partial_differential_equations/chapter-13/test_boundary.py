"""Exact arithmetic regression checks for PDE chapter 13 (not proof verification)."""
from fractions import Fraction as Q
import unittest

class BoundaryTests(unittest.TestCase):
    def test_transmission(self):
        C, D = Q(-3,10), Q(1,5)
        left = lambda x: -x*x/2+C*x+D
        right = lambda x: -x*x/8+C*x/4+D
        self.assertEqual(left(Q(-1)), 0)
        self.assertEqual(right(Q(1)), 0)
        self.assertEqual(left(Q(0)), right(Q(0)))
        self.assertEqual(C, 4*(C/4))
        self.assertEqual(C/4-C, Q(9,40))
        self.assertEqual(left(C), Q(49,200))
        self.assertEqual(-C+C, 0)

    def test_resonance(self):
        for n in range(2, 101):
            with self.subTest(n=n):
                self.assertLessEqual(Q(n*n,n*n-1), Q(4,3))
                self.assertLessEqual(Q(1,n*n-1), Q(1,3))
                self.assertEqual((n*n-1)*Q(1,n*n-1), 1)
        self.assertEqual(Q(1,2*2-1), Q(1,3))

    def test_shift(self):
        for lam in map(Q, (1, 2, 5)):
            for b in map(Q, (-3, 0, 4)):
                for c in map(Q, (-2, 0, 3)):
                    gamma = b*b/(2*lam)+max(-c, 0)
                    mu = gamma+lam/2
                    for x in map(Q, (-2, 0, 3)):
                        for y in map(Q, (-1, 0, 2)):
                            self.assertGreaterEqual(
                                lam*x*x+b*x*y+(c+mu)*y*y,
                                lam/2*(x*x+y*y))

    def test_robin_one_endpoint(self):
        # On (0,1), u=a+b*x; positive Robin weight only at x=0.
        # D=sqrt(2), trace bound 2, r=1/sqrt(beta).
        # D_beta^2=18, r^2=1/beta.
        for beta in (Q(1,100), Q(1,2), Q(1), Q(10)):
            for lam in (Q(1,5), Q(1), Q(5)):
                for a in map(Q, (-2,0,3)):
                    for b in map(Q, (-1,0,2)):
                        norm2=a*a+a*b+b*b/3+b*b
                        energy=lam*b*b+beta*a*a
                        self.assertGreaterEqual(energy,
                            min(lam,1)*norm2/(18+1/beta))

if __name__ == "__main__":
    unittest.main()
