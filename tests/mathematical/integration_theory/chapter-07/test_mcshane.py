"""Finite witnesses for free-tag McShane arguments, not general proofs."""
from fractions import Fraction as Q
import unittest


class McShaneChapter07(unittest.TestCase):
    def test_common_refinement_free_tags(self):
        # On a subcell, both inherited tags may lie outside it.
        P=[(Q(0),Q(1,3),Q(9,10)),(Q(1,3),Q(1),Q(1,10))]
        R=[(Q(0),Q(2,3),Q(1,5)),(Q(2,3),Q(1),Q(4,5))]
        f=lambda t: 2*t-1
        plus=minus=diff=Q(0)
        outside=False
        for u,v,t in P:
            for a,b,s in R:
                l,r=max(u,a),min(v,b)
                if l>=r:
                    continue
                outside |= not(l<=t<=r) and not(l<=s<=r)
                x,y=f(t),f(s)
                plus+=(r-l)*max(x,y)
                minus+=(r-l)*min(x,y)
                diff+=(r-l)*abs(x-y)
        self.assertTrue(outside)
        self.assertEqual(plus-minus,diff)
        def absolute_sum(cells):
            return sum(abs(f(t))*(v-u) for u,v,t in cells)
        self.assertLessEqual(abs(absolute_sum(P)-absolute_sum(R)),diff)

    def test_repeated_free_tag_length(self):
        t,d=Q(1,2),Q(1,8)
        cells=[(Q(2,5),Q(9,20)),(Q(9,20),Q(19,40)),
               (Q(11,20),Q(3,5))]
        self.assertTrue(all(t-d<u<v<t+d for u,v in cells))
        self.assertTrue(all(not u<=t<=v for u,v in cells))
        self.assertLessEqual(sum(v-u for u,v in cells),2*d)

    def test_locality_split_and_side_constraint(self):
        c=Q(1,2)
        for t in (Q(1,8),Q(3,8),Q(5,8),Q(7,8)):
            d=abs(t-c)/2
            self.assertTrue(t+d<c if t<c else t-d>c)
        u,v=Q(1,4),Q(3,4)
        value=Q(-7)
        self.assertEqual(value*(v-u),value*(c-u)+value*(v-c))

    def test_riemann_boundary_budget(self):
        # A single boundary tag can occur on several disjoint cells.
        M,d=Q(3),Q(1,8)
        lengths=[Q(1,20),Q(1,20),Q(1,10)]
        self.assertLessEqual(sum(2*M*l for l in lengths),4*M*d)

    def test_truncation_integrals(self):
        # n=m^2: exact value of integral x^(-1/2) over [1/n,1].
        vals=[2*(1-Q(1,m)) for m in range(1,20)]
        self.assertTrue(all(x<=y for x,y in zip(vals,vals[1:])))
        self.assertEqual(2-vals[-1],Q(2,19))


if __name__=="__main__":
    unittest.main()
