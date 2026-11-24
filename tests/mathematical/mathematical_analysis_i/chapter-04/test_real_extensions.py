from fractions import Fraction as F
import itertools
import unittest

class Chapter04(unittest.TestCase):
    def test_extended_indeterminate_examples(self):
        for n in range(1,51):
            self.assertEqual(n-n,0)
            self.assertEqual(n+(1-n),1)
            self.assertEqual(2*n-n,n)
            self.assertEqual(F(1,n)*n,1)
            self.assertEqual(F(1,n*n)*n,F(1,n))
            self.assertEqual(F(1,n)*n*n,n)

    def test_principal_ultrafilter_partition(self):
        # Finite principal ultrafilters illustrate the Boolean laws.
        # They are not models of a nonprincipal ultrafilter on N.
        I=frozenset(range(4))
        subsets=[frozenset(k for k in I if mask & (1<<k)) for mask in range(16)]
        for i in I:
            U={A for A in subsets if i in A}
            self.assertIn(I,U)
            self.assertNotIn(frozenset(),U)
            for A,B in itertools.product(subsets,repeat=2):
                self.assertEqual(A & B in U,A in U and B in U)
                self.assertNotEqual(A in U,I-A in U)
                if A in U and A<=B: self.assertIn(B,U)
            for assignment in itertools.product(range(3),repeat=4):
                pieces=[frozenset(k for k in I if assignment[k]==j) for j in range(3)]
                self.assertEqual(sum(A in U for A in pieces),1)

    def test_coordinate_quotient(self):
        # Principal finite analogue of independence of representatives.
        for a,b in itertools.product(itertools.product(range(-1,2),repeat=3),repeat=2):
            for i in range(3):
                aa=tuple(x if k==i else x+2 for k,x in enumerate(a))
                bb=tuple(x if k==i else x-2 for k,x in enumerate(b))
                self.assertEqual(a[i]+b[i],aa[i]+bb[i])
                self.assertEqual(a[i]*b[i],aa[i]*bb[i])
                self.assertEqual(a[i]<b[i],aa[i]<bb[i])
                inv=tuple(1/F(x) if x else F(0) for x in a)
                if a[i]: self.assertEqual(a[i]*inv[i],1)

    def test_finite_and_infinitesimal_estimates(self):
        for n in range(1,51):
            d=F(1,n)
            self.assertEqual(n*d,1)
            for r,s in itertools.product(map(F,range(-3,4)),repeat=2):
                x,y=r+d,s-d
                self.assertEqual(x+y-(r+s),(x-r)+(y-s))
                self.assertEqual(x*y-r*s,x*(y-s)+(x-r)*s)
                self.assertLessEqual(abs(x*y-r*s),abs(x)*d+abs(s)*d)

    def test_standard_part_uniqueness_bound(self):
        for s,t in itertools.product(map(F,range(-3,4)),repeat=2):
            if s==t: continue
            eps=abs(s-t)/3
            self.assertLess(2*eps,abs(s-t))
            self.assertFalse(any(abs(x-s)<eps and abs(x-t)<eps
                for x in (F(k,12) for k in range(-48,49))))

if __name__=="__main__": unittest.main()
