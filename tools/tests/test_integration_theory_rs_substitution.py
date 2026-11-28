"""Regression checks IT-03: tagged sums, not formal proofs.
Source: chapters/pl/integration_theory/03-calka-riemanna-stieltjesa.tex
Labels: it:thm:rs-reparametrization, it:thm:rs-integrator-substitution.
"""
from fractions import Fraction as Q
import unittest


def tagged_sum(points, tags, f, alpha):
    return sum((f(t) * (alpha(v) - alpha(u))
                for u, v, t in zip(points, points[1:], tags)), Q(0))


class TestRSSubstitution(unittest.TestCase):
    def test_it03_reparametrization_plateau_and_reverse(self):
        points = [Q(i, 8) for i in range(9)]
        tags = [(u + v) / 2 for u, v in zip(points, points[1:])]
        f = lambda x: x*x
        alpha = lambda x: x - 2*int(x >= Q(1, 2))
        phi = lambda t: max(Q(0), 2*t-1)
        image = [(phi(u), phi(v), phi(t))
                 for u,v,t in zip(points, points[1:], tags) if phi(u)!=phi(v)]
        expected = sum((f(t)*(alpha(v)-alpha(u)) for u,v,t in image), Q(0))
        self.assertEqual(tagged_sum(points, tags, lambda t:f(phi(t)),
                                    lambda t:alpha(phi(t))), expected)
        self.assertEqual(tagged_sum(points, tags, lambda t:f(1-t),
                                    lambda t:alpha(1-t)),
                         -tagged_sum(points, tags, f, alpha))

    def test_it03_signed_atom_and_error_bound(self):
        beta = lambda x: x - 2*int(x >= Q(1, 2))
        G = lambda x: x*x/2 - int(x >= Q(1, 2))
        expected = -Q(1, 6)
        for n in (15, 32, 63, 128):
            points = [Q(i, n) for i in range(n+1)]
            for tags in (points[:-1], points[1:],
                         [(u+v)/2 for u,v in zip(points, points[1:])]):
                left = tagged_sum(points, tags, lambda x:x, G)
                right = tagged_sum(points, tags, lambda x:x*x, beta)
                # Var(beta)=3, ||f||=1, omega_g(h)=h.
                self.assertLessEqual(abs(left-right), Q(3,n))
                self.assertLessEqual(abs(right-expected), Q(6,n))
                self.assertLessEqual(abs(left-expected), Q(9,n))


if __name__ == '__main__':
    unittest.main()
