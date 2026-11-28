from fractions import Fraction as F
from unittest import TestCase, main

def partial(a):
    s=F(0); out=[]
    for x in a:
        s+=x; out.append(s)
    return out

class Chapter13(TestCase):
    def test_cesaro_triangular_weights(self):
        a=[F((-1)**n,n+1) for n in range(30)]
        s=partial(a)
        for n in range(len(a)):
            self.assertEqual(sum(s[:n+1])/F(n+1),sum(F(n-j+1,n+1)*a[j] for j in range(n+1)))
    def test_grandi_and_constant(self):
        s=partial([F((-1)**n) for n in range(80)])
        t=partial([F(1)]*80)
        for n in range(80):
            self.assertEqual(sum(s[:n+1])/F(n+1),F(n//2+1,n+1))
            self.assertEqual(sum(t[:n+1])/F(n+1),F(n+2,2))
    def test_abel_not_cesaro(self):
        s=partial([F((-1)**n*(n+1)) for n in range(80)])
        for m in range(40):
            self.assertEqual(s[2*m],m+1)
            self.assertEqual(s[2*m+1],-m-1)
            self.assertEqual(sum(s[:2*m+1])/F(2*m+1),F(m+1,2*m+1))
            self.assertEqual(sum(s[:2*m+2]),0)
    def test_finite_summation_by_parts(self):
        a=[F((-1)**n,n+1) for n in range(16)]
        s=partial(a); b=partial(s)
        for r in [F(0),F(1,3),F(9,10)]:
            for n in range(len(a)):
                A=sum(a[j]*r**j for j in range(n+1))
                S=sum(s[j]*r**j for j in range(n+1))
                B=sum(b[j]*r**j for j in range(n+1))
                self.assertEqual(A,(1-r)*S+s[n]*r**(n+1))
                self.assertEqual(S,(1-r)*B+b[n]*r**(n+1))
    def test_geometric_weights(self):
        for r in [F(0),F(1,3),F(9,10)]:
            for n in range(25):
                self.assertEqual(sum((1-r)*r**j for j in range(n+1)),1-r**(n+1))
                self.assertEqual(sum((1-r)**2*(j+1)*r**j for j in range(n+1)),1-r**(n+1)*(n+2-(n+1)*r))
    def test_signed_geometric_square(self):
        for r in [F(0),F(1,3),F(9,10)]:
            for n in range(20):
                x=-r
                self.assertEqual((1-x)**2*sum((j+1)*x**j for j in range(n+1)),1-x**(n+1)*(n+2-(n+1)*x))
    def test_shift_cesaro(self):
        a=[F((-1)**n,n+1) for n in range(20)]
        s=partial(a)
        for m in range(5):
            h=sum(a[:m]); t=partial(a[m:])
            for n in range(len(t)):
                c=sum(s[:n+m+1])/F(n+m+1)
                d=sum(t[:n+1])/F(n+1)
                self.assertEqual(d,F(n+m+1,n+1)*c-sum(s[:m])/F(n+1)-h)
    def test_shift_abel(self):
        a=[F((-1)**n,n+1) for n in range(15)]
        for r in [F(0),F(1,2),F(9,10)]:
            for m in range(len(a)):
                self.assertEqual(sum(x*r**n for n,x in enumerate(a)),sum(x*r**n for n,x in enumerate(a[:m]))+r**m*sum(x*r**n for n,x in enumerate(a[m:])))
    def test_bounded_means_growth(self):
        # Prescribe bounded means, reconstruct the two successive differences.
        c=[F((-1)**n,n%5+1) for n in range(40)]
        M=max(map(abs,c))
        b=[(n+1)*x for n,x in enumerate(c)]
        s=[v-(b[n-1] if n else 0) for n,v in enumerate(b)]
        a=[v-(s[n-1] if n else 0) for n,v in enumerate(s)]
        self.assertEqual(partial(a),s)
        self.assertEqual(partial(s),b)
        for n in range(len(c)):
            self.assertEqual(sum(s[:n+1])/F(n+1),c[n])
            self.assertLessEqual(abs(b[n]),M*(n+1))
            self.assertLessEqual(abs(s[n]),M*(2*n+1))
            self.assertLessEqual(abs(a[n]),4*M*(n+1))

    def test_linearity(self):
        a=[F((-1)**n,n+1) for n in range(20)]
        d=[F(n+1,2**n) for n in range(20)]
        u,v=F(-3,2),F(4,3)
        z=[u*x+v*y for x,y in zip(a,d)]
        A,D,Z=map(partial,(a,d,z))
        for n in range(len(z)):
            self.assertEqual(sum(Z[:n+1]),u*sum(A[:n+1])+v*sum(D[:n+1]))
            for r in [F(0),F(1,3),F(9,10)]:
                self.assertEqual(sum(z[j]*r**j for j in range(n+1)),
                                 u*sum(a[j]*r**j for j in range(n+1))+
                                 v*sum(d[j]*r**j for j in range(n+1)))

if __name__ == "__main__": main()
