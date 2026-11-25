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
