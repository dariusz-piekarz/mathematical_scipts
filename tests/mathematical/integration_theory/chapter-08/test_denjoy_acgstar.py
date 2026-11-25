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
