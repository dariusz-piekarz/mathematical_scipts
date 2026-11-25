"""AM1-36: finite exact checks of Stieltjes convergence estimates."""
from fractions import Fraction as Q
import unittest


class TestStieltjesLimits(unittest.TestCase):
    def test_variation_seminorm_estimates(self):
        xs = [Q(k, 8) for k in range(9)]
        tags = [(u+v)/2 for u,v in zip(xs,xs[1:])]
        g = lambda x: x*x-2*(x >= Q(1, 2))
        f = lambda t: 2*t-1
        for n in range(1, 12):
            h = lambda x: g(x)+Q(1, n)*(x+3*(x >= Q(1, 4)))+7
            ds = sum(f(t)*(h(v)-h(u)-g(v)+g(u))
                     for u,v,t in zip(xs,xs[1:],tags))
            self.assertLessEqual(abs(ds), Q(4, n))
            df = sum(Q(1,n)*(g(v)-g(u)) for u,v in zip(xs,xs[1:]))
            self.assertLessEqual(abs(df), Q(3,n))

    def test_uniform_integrator_bound(self):
        xs = [Q(k, 8) for k in range(9)]
        tags = [(u+v)/2 for u,v in zip(xs,xs[1:])]
        f = lambda t: 3*t-1
        for n in range(1, 12):
            g = [Q((-1)**k,n) for k in range(len(xs))]
            s = sum(f(t)*(v-u) for t,u,v in zip(tags,g,g[1:]))
            self.assertLessEqual(abs(s), Q(7,n))


if __name__ == '__main__':
    unittest.main()
