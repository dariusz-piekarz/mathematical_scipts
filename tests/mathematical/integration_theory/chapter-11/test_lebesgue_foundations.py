"""Finite exact regression witnesses for the foundations of Lebesgue integration."""
from fractions import Fraction as Q
import unittest


class LebesgueFoundations11(unittest.TestCase):
    def test_canonical_simple_approximation(self):
        for f in (Q(0),Q(1,3),Q(9,2),Q(101,7)):
            vals=[]
            for n in range(1,16):
                v=Q(int(2**n*min(f,n)),2**n)
                self.assertTrue(0<=v<=f)
                if n>f:
                    self.assertLess(f-v,Q(1,2**n))
                vals.append(v)
            self.assertEqual(vals,sorted(vals))

    def test_simple_refinement_with_empty_cells(self):
        mu=[Q(2),Q(3),Q(0),Q(7)]
        a=[Q(1),Q(1),Q(100),Q(2)]
        self.assertEqual(sum(x*y for x,y in zip(mu,a)),19)
        self.assertEqual(5+2*7,19)

    def test_signed_monotonicity_and_positive_parts(self):
        w=[Q(2),Q(3),Q(0)]
        f=[Q(-3),Q(4),Q(100)]
        g=[Q(-1),Q(5),Q(-100)]
        integral=lambda z:sum(x*y for x,y in zip(w,z))
        self.assertLessEqual(integral(f),integral(g))
        self.assertEqual(integral(f),integral([max(x,0) for x in f])-integral([max(-x,0) for x in f]))

    def test_l1_quotient_zero_weight(self):
        w=[Q(2),Q(3),Q(0)]
        norm=lambda z:sum(m*abs(x) for m,x in zip(w,z))
        f=[Q(1),Q(-2),Q(0)]
        g=[Q(1),Q(-2),Q(7)]
        self.assertEqual(norm([a-b for a,b in zip(f,g)]),0)
        self.assertEqual(norm(f),norm(g))
        self.assertEqual(norm([3*x for x in f]),3*norm(f))

    def test_layer_cake_simple(self):
        a=[Q(1),Q(3),Q(4)]
        w=[Q(2),Q(5),Q(1)]
        cuts=[Q(0)]+a
        layer=sum((v-u)*sum(m for x,m in zip(a,w) if x>u) for u,v in zip(cuts,cuts[1:]))
        self.assertEqual(layer,sum(x*m for x,m in zip(a,w)))
        power=sum((v*v-u*u)*sum(m for x,m in zip(a,w) if x>u) for u,v in zip(cuts,cuts[1:]))
        self.assertEqual(power,sum(x*x*m for x,m in zip(a,w)))

    def test_series_and_riemann_error_budgets(self):
        for n in range(1,12):
            self.assertLess(sum(Q(1,2**k) for k in range(n,30)),Q(2,2**n))
            self.assertLess(sum(Q(1,2**k) for k in range(n+1,30)),Q(1,2**n))


if __name__=="__main__":
    unittest.main()
