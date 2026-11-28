from fractions import Fraction as F
import itertools
import unittest

class Chapter02(unittest.TestCase):
    def test_principal_cut_witnesses(self):
        for r,s in itertools.product(map(F,range(-3,4)),repeat=2):
            q=r+s-F(1,7)
            h=(r+s-q)/2
            self.assertLess(r-h,r)
            self.assertLess(s-h,s)
            self.assertEqual((r-h)+(s-h),q)
        for r,s in itertools.product(map(F,range(1,5)),repeat=2):
            for q in (F(0),r*s/2,r*s-F(1,17)):
                a=(q/s+r)/2
                b=(q/a+s)/2
                self.assertTrue(0<a<r and 0<b<s and q<a*b)

    def test_inverse_witness(self):
        for a,u in itertools.product(map(F,range(1,7)),repeat=2):
            if a>=u: continue
            q=a/(2*u)
            b=(q/a+1/u)/2
            self.assertTrue(q<a*b<1)
            self.assertLess(b,1/u)

    def test_signed_extension(self):
        for p,q,u,v in itertools.product(range(4),repeat=4):
            self.assertEqual(p*u+q*v-p*v-q*u,(p-q)*(u-v))
            self.assertEqual((p+2)*u+(q+2)*v-(p+2)*v-(q+2)*u,(p-q)*(u-v))

    def test_cauchy_product_bound(self):
        vals=[F(i,3) for i in range(-3,4)]
        for a,b,c,d in itertools.product(vals,repeat=4):
            m=max(F(1),abs(a),abs(c),abs(b),abs(d))
            self.assertLessEqual(abs(a*b-c*d),m*(abs(a-c)+abs(b-d)))

    def test_inverse_bracket_bound(self):
        for a,u in itertools.product(map(F,range(1,16)),repeat=2):
            if a>=u: continue
            for q in (F(0),F(1,4),F(1,2),F(3,4),F(9,10)):
                if u-a >= (1-q)*a: continue
                self.assertLess((u-a)/u,1-q)
                self.assertLess(q,a/u)
                b=(q/a+1/u)/2
                self.assertTrue(0<b<1/u and q<a*b<1)

    def test_distributivity_witness(self):
        for a,b,c in itertools.product(map(F,range(1,5)),repeat=3):
            q=a*(b+c)-F(1,7)
            eta=(a*(b+c)-q)/4
            u,v=a*b-eta,a*c-eta
            self.assertLess(u,a*b)
            self.assertLess(v,a*c)
            self.assertGreater(u+v,q)

    def test_cauchy_reciprocal_bound(self):
        vals=[F(i,4) for i in range(-12,13) if abs(i)>=2]
        c=F(1,2)
        for a,b in itertools.product(vals,repeat=2):
            self.assertLessEqual(abs(1/a-1/b),abs(a-b)/c**2)
        for n in range(1,31):
            a=F(1)+F(1,n)
            self.assertEqual(a*(1/a),1)
            self.assertLessEqual(abs(1/a-1),F(1,n))

if __name__=="__main__": unittest.main()
