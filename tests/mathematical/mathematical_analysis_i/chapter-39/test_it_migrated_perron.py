"""Finite arithmetic witnesses for Perron comparison arguments; not general proofs."""
from fractions import Fraction as Q
import unittest


class PerronChapter05(unittest.TestCase):
    def test_comparison_on_both_sides_of_tag(self):
        f=Q(-3,2)
        eta=Q(1,10)
        M=lambda x:(f+eta)*x
        m=lambda x:(f-eta)*x
        u,v=Q(1,4),Q(3,4)
        for t in (u,(u+v)/2,v):
            for y in (u,v):
                if y!=t:
                    self.assertGreaterEqual((M(y)-M(t))/(y-t),f-eta)
                    self.assertLessEqual((m(y)-m(t))/(y-t),f+eta)
            self.assertLessEqual(m(v)-m(u)-eta*(v-u),f*(v-u))
            self.assertLessEqual(f*(v-u),M(v)-M(u)+eta*(v-u))

    def test_gap_envelope_both_endpoints(self):
        R=[Q(x) for x in (0,2,1,4,2,0)]
        L=[max(R[:i+1]) for i in range(len(R))]
        B=[max(R[i:]) for i in range(len(R))]
        K=[l+B[0]-b for l,b in zip(L,B)]
        self.assertEqual(K[0],0)
        self.assertEqual(K[-1],2*max(R))
        for i in range(len(R)):
            self.assertGreaterEqual(K[i]-K[0],R[i])
            self.assertGreaterEqual(K[-1]-K[i],R[i])
        self.assertTrue(all(x<=y for x,y in zip(K,K[1:])))

    def test_local_correction_signs(self):
        for slope in map(Q,(-11,-1,0,2,9)):
            for f in map(Q,(-17,-2,0,3,12)):
                h=abs(slope)+abs(f)
                for dy in (Q(-1,10),Q(1,10)):
                    self.assertGreaterEqual((slope*dy+h*dy)/dy,f)
                    self.assertLessEqual((slope*dy-h*dy)/dy,f)

    def test_piecewise_absolute_value_and_exception(self):
        # F=|x|, f(0)=17; H has slope 19 near 0.
        f0=Q(17)
        B=Q(19)
        for y in (Q(-1,100),Q(1,100)):
            self.assertGreaterEqual((abs(y)+B*y)/y,f0)
            self.assertLessEqual((abs(y)-B*y)/y,f0)
        self.assertEqual(abs(Q(2))-abs(Q(-1)),1)

    def test_exception_budget(self):
        eps=Q(1,10)
        total=sum(eps/Q(2**(n+2)) for n in range(1,20))
        self.assertLess(2*total,eps/2)


if __name__=="__main__":
    unittest.main()
