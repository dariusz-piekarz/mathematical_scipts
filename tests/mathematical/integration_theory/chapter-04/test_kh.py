from fractions import Fraction as F
import unittest


class KHChapter04(unittest.TestCase):
    def test_repeated_tag_total_length(self):
        tag=F(1,2)
        d=F(1,8)
        intervals=[(tag-d/2,tag),(tag,tag+3*d/4)]
        length=sum(v-u for u,v in intervals)
        self.assertLess(length,2*d)
        self.assertTrue(all(tag-d<u<=tag<=v<tag+d for u,v in intervals))

    def test_hake_boundary_tag_split(self):
        # c_n=2^-n, adjacent intervals, tag at their common endpoint.
        for n in range(1,10):
            c=F(1,2**n)
            left=c/2
            right=2*c
            d=min(c-left,right-c)/2
            u,v=c-d/2,c+d/2
            self.assertTrue(left<u<c<v<right)
            value=F(3)
            self.assertEqual(value*(v-u),value*(c-u)+value*(v-c))
            # local errors <= eps*2^(-n-2) sum to <= eps/4
        self.assertLess(sum(F(1,2**(n+2)) for n in range(1,10)),F(1,4))

    def test_locality_shared_complement(self):
        # Compare tagged sums on [1/2,1] using the same complement.
        def total(cells):
            return sum(t*t*(v-u) for t,u,v in cells)
        left=[(F(0),F(0),F(1,2))]
        p=[(F(1,2),F(1,2),F(1))]
        q=[(F(3,4),F(1,2),F(3,4)),(F(1),F(3,4),F(1))]
        self.assertEqual(total(left+p)-total(left+q),total(p)-total(q))

    def test_null_modification_zero_tags_and_budget(self):
        eps=F(1,10)
        # |h|=0 contributes nothing even at a point of N.
        self.assertEqual(F(0)*F(1,3),0)
        total=sum(k*eps/F(k*2**(k+1)) for k in range(1,20))
        self.assertLess(total,eps/2)

    def test_dyadic_tail_partial_interval(self):
        for n in range(2,10):
            a=F((-1)**(n+1),n)
            low=F(1,2**n)
            high=2*low
            for c in (low,(low+high)/2,high):
                partial=2**n*a*(high-c)
                self.assertLessEqual(abs(partial),abs(a))
            self.assertEqual(2**n*a*(high-low),a)

    def test_equiintegrable_finite_sum_pointwise(self):
        p=[F(0),F(1,3),F(1)]
        for n in (1,10,100):
            for tags in ((p[0],p[1]),(p[1],p[2])):
                total=sum(t/n*(v-u) for t,u,v in zip(tags,p,p[1:]))
                self.assertLessEqual(abs(total),F(1,n))
                self.assertLessEqual(abs(total-F(1,2*n)),F(1,2*n))

if __name__=="__main__":
    unittest.main()
