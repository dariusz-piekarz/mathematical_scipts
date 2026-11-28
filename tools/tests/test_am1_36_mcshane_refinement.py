"""Finite checks of the Riemann-to-McShane retagging estimate."""
from fractions import Fraction as Q
import unittest


class McShaneRetaggingTests(unittest.TestCase):
    def test_free_tags_and_boundary_contribution(self):
        # Coarse cells [0,1/2], [1/2,1]; fine cells of length 1/8.
        xs = [Q(i, 8) for i in range(9)]
        tags = [Q(1,4), Q(1,4), Q(1,4), Q(1,2),
                Q(1,2), Q(3,4), Q(3,4), Q(3,4)]
        f = lambda x: x if x < Q(1,2) else 2+x
        ordinary = [(u+v)/2 for u,v in zip(xs,xs[1:])]
        good = sum(abs(f(t)-f(s))*(v-u)
                   for t,s,u,v in zip(tags,ordinary,xs,xs[1:]) if t != Q(1,2))
        bad = sum(abs(f(t)-f(s))*(v-u)
                  for t,s,u,v in zip(tags,ordinary,xs,xs[1:]) if t == Q(1,2))
        coarse_oscillation = Q(5,2)*Q(1,2)+Q(1,2)*Q(1,2)
        self.assertLessEqual(good, coarse_oscillation)
        self.assertLessEqual(bad, 4*Q(3)*Q(1,7))
        self.assertLessEqual(abs(sum((f(t)-f(s))*(v-u)
                                    for t,s,u,v in zip(tags,ordinary,xs,xs[1:]))), good+bad)


if __name__ == '__main__':
    unittest.main()
