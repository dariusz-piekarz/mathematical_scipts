"""AM1-36: exact finite regressions for wide Denjoy calculus identities."""
from fractions import Fraction as Q
import unittest


class WideDenjoyCalculusTests(unittest.TestCase):
    def test_bv_multiplier_jump_cancellation(self):
        # F(x)=x^2, g(x)=1+2 chi_[1/2,1](x), H=Fg-int F dg.
        c = Q(1, 2)
        F = lambda x: x*x
        g = lambda x: 1+2*(x >= c)
        J = lambda x: 2*F(c)*(x >= c)
        H = lambda x: F(x)*g(x)-J(x)
        self.assertEqual(H(c), F(c))
        self.assertEqual(H(Q(1))-H(Q(0)), Q(5, 2))
        for n in range(2, 12):
            u, v = c-Q(1, 2**n), c+Q(1, 2**n)
            self.assertEqual(H(v)-H(u), g(v)*(F(v)-F(u))-2*(F(c)-F(u)))

    def test_reversed_substitution(self):
        F = lambda x: x**3
        phi = lambda t: 1-t/2
        points = [Q(k, 8) for k in range(17)]
        self.assertEqual(sum(F(phi(v))-F(phi(u))
                             for u, v in zip(points, points[1:])), -1)

    def test_hake_tail_primitive(self):
        # Alternating geometric increments on dyadic intervals.
        L = Q(1, 3)
        for n in range(1, 20):
            partial = sum((-Q(1, 2))**(k-1)/2 for k in range(1, n+1))
            self.assertEqual(L-partial, L*(-Q(1, 2))**n)
            self.assertLessEqual(abs(L-partial), Q(1, 2**n))


if __name__ == '__main__':
    unittest.main()
