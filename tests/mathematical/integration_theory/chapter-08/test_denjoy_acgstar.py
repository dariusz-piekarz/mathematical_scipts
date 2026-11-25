from fractions import Fraction as F
import unittest


class Denjoy08(unittest.TestCase):
    def test_gap_split_telescopes(self):
        # E contains the endpoints of the middle subinterval.
        u,p,q,v=map(F,("0.1","0.2","0.6","0.8"))
        fun=lambda x:x*x-x
        pieces=[fun(p)-fun(u),fun(q)-fun(p),fun(v)-fun(q)]
        self.assertEqual(sum(pieces),fun(v)-fun(u))
        self.assertLessEqual(abs(sum(pieces)),sum(map(abs,pieces)))

    def test_tail_and_head_budget(self):
        eps=F(1,100)
        m=5
        middle=eps/4
        tail=2*eps/8
        head=2*m*eps/(8*(m+1))
        self.assertLess(middle+tail+head,eps)
        self.assertLess(sum(eps/F(2**(n+1)) for n in range(1,20)),eps)

    def test_affine_extension_gap_integral(self):
        l,r=F(1,4),F(3,4)
        fl,fr=F(2),F(-1)
        G=lambda x:fl+(x-l)/(r-l)*(fr-fl)
        self.assertEqual(G(l),fl)
        self.assertEqual(G(r),fr)
        for u,v in ((l,r),(l,(l+r)/2),((l+r)/2,r)):
            self.assertEqual(abs(G(v)-G(u)),abs(fr-fl)/(r-l)*(v-u))
            self.assertTrue(min(fl,fr)<=G(u)<=max(fl,fr))

    def test_gap_oscillation_exceptional_set(self):
        # A summable family of oscillations, d_k=4^-k.
        for m in (1,2,10):
            for n in (1,3,8):
                finite=sum(4*m*F(1,4**k) for k in range(n,n+10))
                bound=4*m*F(1,4**n)/F(3,4)
                self.assertLess(finite,bound)
            d=F(1,1000)
            x=F(0)
            l=m*d
            y=l+F(1,100)
            self.assertLessEqual(d/(y-x),F(1,m))

    def test_alternating_groups_preserve_separation(self):
        intervals=[(F(j,8),F(j+1,8)) for j in range(8)]
        n=3
        for parity in (0,1):
            group=intervals[parity::2]
            approx=[(max(F(0),u-F(1,64)),v) for u,v in group]
            for u,v in approx:
                self.assertLess(v-u,F(1,n))
            for (_,v),(u,_) in zip(approx,approx[1:]):
                self.assertLess(v,u)
            self.assertLessEqual(sum(v-u for u,v in approx),1)

    def test_gap_oscillation_tail_control(self):
        # Dyadic gaps of length 2^(-k-1), d_k=4^-k.
        for m in (2,4,8):
            eta=F(1,2**(m+1))
            self.assertTrue(all(F(1,2**(k+1))>=eta for k in range(1,m+1)))
            tail=F(1,4**(m+1))/F(3,4)
            self.assertLess(sum(F(1,4**k) for k in range(m+1,m+20)),tail)
            self.assertLess(2*tail,F(1,4**m))

    def test_large_gap_gauge_excludes_far_endpoint(self):
        for l,r in ((F(0),F(1,2)),(F(1,4),F(3,4))):
            d=(r-l)/4
            for t in (l,r):
                other=r if t==l else l
                self.assertGreater(abs(other-t),d)
                y=t+d/2 if t==l else t-d/2
                self.assertLess(abs(y-t),d)
                self.assertTrue(l<=y<=r)

    def test_derivative_error_two_endpoints(self):
        # F(x)=x^2, exact local remainder (y-t)^2.
        eps=F(1,10)
        t=F(1,2)
        d=eps/3
        u,v=t-d/2,t+d/3
        fun=lambda x:x*x
        slope=2*t
        for y in (u,v):
            self.assertLessEqual(abs(fun(y)-fun(t)-slope*(y-t)),d*abs(y-t))
        self.assertLessEqual(abs(fun(v)-fun(u)-slope*(v-u)),d*(v-u))


if __name__=="__main__":
    unittest.main()
