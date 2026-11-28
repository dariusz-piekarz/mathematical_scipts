"""Finite witnesses for product measure and Fubini; not proofs of general theorems."""
from fractions import Fraction as Q
import unittest


class ProductIntegrals11(unittest.TestCase):
    def test_weighted_section_identity(self):
        mu=[Q(1),Q(2),Q(0)]
        nu=[Q(3),Q(1,2)]
        E=[[1,0],[1,1],[0,1]]
        vertical=[sum(w*v for w,v in zip(nu,row)) for row in E]
        horizontal=[sum(mu[i]*E[i][j] for i in range(len(mu))) for j in range(len(nu))]
        self.assertEqual(sum(w*v for w,v in zip(mu,vertical)),
                         sum(w*v for w,v in zip(nu,horizontal)))

    def test_nonabsolute_iterated_sums(self):
        for N in (2,5,20):
            a=lambda m,n:int(n==m)-int(n==m+1)
            self.assertEqual(sum(sum(a(m,n) for n in range(1,N+2))
                                 for m in range(1,N+1)),0)
            self.assertEqual(sum(sum(a(m,n) for m in range(1,N+1))
                                 for n in range(1,N+1)),1)
            self.assertEqual(sum(abs(a(m,n)) for m in range(1,N+1)
                                 for n in range(1,N+2)),2*N)

    def test_null_slab_cover_budget(self):
        eps=Q(1,100)
        for k in (1,3,7):
            for n in (1,2,3):
                volume=(2*k+2)**n
                pieces=[eps/Q(volume*2**j) for j in range(1,15)]
                self.assertLess(sum(v*volume for v in pieces),eps)

    def test_exceptional_sections_and_completion(self):
        mu=[Q(0),Q(2)]
        nu=[Q(1),Q(3)]
        # The first section can be modified arbitrarily without changing
        # the product integral: only the parameter with zero mass is affected.
        g=[[Q(1),Q(2)],[Q(4),Q(-1)]]
        f=[[Q(1000),Q(-50)],g[1]]
        inner=lambda a:[sum(w*v for w,v in zip(nu,row)) for row in a]
        self.assertNotEqual(inner(f)[0],inner(g)[0])
        self.assertEqual(sum(w*v for w,v in zip(mu,inner(f))),
                         sum(w*v for w,v in zip(mu,inner(g))))

    def test_overlapping_representatives_off_exception(self):
        original=[{0,1},{2,3}]
        replaced=[{0,1,4},{2,3,4}]
        exceptional={4}
        for x in set(range(5))-exceptional:
            self.assertEqual(sum(c*(x in a) for c,a in zip((2,7),original)),
                             sum(c*(x in a) for c,a in zip((2,7),replaced)))
        self.assertEqual(sum(c*(4 in a) for c,a in zip((2,7),replaced)),9)

    def test_associative_product_weights(self):
        a=[Q(1,3),Q(2)]
        b=[Q(0),Q(4)]
        c=[Q(3),Q(1,7)]
        left=sum((x*y)*z for x in a for y in b for z in c)
        right=sum(x*(y*z) for x in a for y in b for z in c)
        self.assertEqual(left,right)
        self.assertEqual(left,sum(a)*sum(b)*sum(c))


if __name__=="__main__":
    unittest.main()
