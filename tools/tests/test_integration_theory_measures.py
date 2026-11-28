"""IT-10: exact finite regression checks for measure constructions."""
from fractions import Fraction as Q
import unittest


class TestIntegrationMeasures(unittest.TestCase):
    def test_stieltjes_atom_and_telescoping(self):
        # Right-continuous alpha(x)=x+2*chi_[1/2,infty)(x).
        alpha = lambda x: x + 2 * (x >= Q(1, 2))
        points = [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]
        masses = [alpha(v)-alpha(u) for u,v in zip(points,points[1:])]
        self.assertEqual(sum(masses), 3)
        self.assertEqual(masses[1], Q(9, 4))
        for n in range(2, 20):
            self.assertEqual(alpha(Q(1,2))-alpha(Q(1,2)-Q(1,2**n)), 2+Q(1,2**n))

    def test_cantor_cylinder_mass(self):
        for n in range(1, 10):
            self.assertEqual(2**n * Q(1,2**n), 1)
            self.assertEqual(Q(1,2**n), 2 * Q(1,2**(n+1)))

    def test_cantor_moments(self):
        # Independent digits, finite partial sums and exact limiting tails.
        for n in range(1, 10):
            mean = sum(Q(1,3**k) for k in range(1,n+1))
            variance = sum(Q(1,9**k) for k in range(1,n+1))
            self.assertEqual(mean + Q(1,2*3**n), Q(1,2))
            self.assertEqual(variance + Q(1,8*9**n), Q(1,8))
            self.assertEqual((mean + Q(1,2*3**n))**2 + variance + Q(1,8*9**n), Q(3,8))


if __name__ == "__main__":
    unittest.main()
