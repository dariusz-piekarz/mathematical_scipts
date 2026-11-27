"""Finite arithmetic regression witnesses for broad Denjoy; not general proofs."""
from fractions import Fraction as Q
import unittest


class BroadDenjoy09(unittest.TestCase):
    def test_density_intersection_budget(self):
        # Union bound for two finite sets of bad samples.
        domain=set(range(100))
        bad_f={1,2,3}
        bad_g={3,4,5,6}
        self.assertLessEqual(len(bad_f | bad_g),len(bad_f)+len(bad_g))
        self.assertGreaterEqual(len(domain-(bad_f | bad_g)),93)

    def test_affine_extension_gap(self):
        l,r=Q(1,3),Q(2,3)
        fl,fr=Q(2),Q(-1)
        u=lambda x:fl+(fr-fl)*(x-l)/(r-l)
        self.assertEqual(u(l),fl)
        self.assertEqual(u(r),fr)
        for s,t in ((l,r),(l,(l+r)/2),((l+r)/2,r)):
            self.assertEqual(abs(u(t)-u(s)),abs(fr-fl)/(r-l)*(t-s))

    def test_cantor_cylinder_oscillation(self):
        for r in range(7):
            previous=None
            for n in range(r+1,r+12):
                count=2**(n-r-1)
                total_length=count*Q(1,3**n)
                self.assertEqual(count*Q(1,2**n),Q(1,2**(r+1)))
                if previous is not None:
                    self.assertEqual(total_length,previous*Q(2,3))
                previous=total_length

    def test_cantor_level_variation(self):
        for n in range(1,15):
            count=2**(n-1)
            amp=Q(1,2**n)
            self.assertEqual(count*2*amp,1)
            self.assertEqual(count*(amp-amp),0)

    def test_gluing_preserves_increments(self):
        a,c,b=Q(0),Q(1,2),Q(1)
        F1=lambda x:x*x+7
        F2=lambda x:3*x-5
        shift=F1(c)-F2(c)
        self.assertEqual(F2(c)+shift,F1(c))
        self.assertEqual(F2(b)+shift-F1(a),
                         F1(c)-F1(a)+F2(b)-F2(c))


    def test_approx_derivative_support_density(self):
        for n in range(1, 21):
            c=Q(1,2**n)
            r=Q(1,2**(3*n+2))
            next_c=c/2
            next_r=r/8
            self.assertLessEqual(r,c/16)
            self.assertLess(next_c+next_r,c-r)
            tail=2*r/(1-Q(1,8))
            self.assertEqual(tail,Q(4,7)*c**3)
            self.assertEqual(tail/(2*c),Q(2,7)*c**2)

    def test_stieltjes_to_lebesgue_error_bound(self):
        # F(x)=x, g(x)=x^2 on [0,1]; integral F g'=2/3.
        for n in (1,2,4,8,16,32):
            for offset in (Q(0),Q(1,2),Q(1)):
                total=sum((Q(j)+offset)/n *
                          (Q(j+1,n)**2-Q(j,n)**2)
                          for j in range(n))
                self.assertLessEqual(abs(total-Q(2,3)),Q(1,n))

    def test_hake_primitive_normalization(self):
        # f(x)=1/sqrt(x) for x>0: local primitives differ by constants.
        L=Q(2)
        for k in range(2,12):
            c=Q(1,k*k)
            G=lambda sqrt_x:2*sqrt_x+7
            integral_c_b=G(Q(1))-G(Q(1,k))
            self.assertEqual(L-integral_c_b,2*Q(1,k))
            self.assertEqual(L-integral_c_b,G(Q(1,k))+L-G(Q(1)))
            self.assertGreater(c,0)


if __name__=="__main__":
    unittest.main()
