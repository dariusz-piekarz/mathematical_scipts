"""AA-35 audit I: independent modular/Sylvester/Frobenius regression tests.
Run: python -m unittest AA-35-audyt-I-testy.py -v
Requires sympy. Each dynamically named method is a separate unittest case.
"""
import math
import unittest
import sympy as sp

X = sp.Symbol('X')
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 59]
F = {
    'linear': X-2,
    'quadratic': X**2-5,
    'cubic_S3': X**3-X-1,
    'cubic_C3': X**3-3*X+1,
    'quartic_D4': X**4-2,
    'quartic_V4': X**4-10*X**2+1,
    'quartic_S4': X**4-X-1,
    'reducible': (X**2-2)*(X-3),
}


def det_sylvester_with_formal_derivative(f, p):
    """Determinant with formal derivative degree n-1, even if leading term reduces to 0."""
    poly = sp.Poly(f, X, domain=sp.ZZ)
    n = poly.degree()
    fc = [int(c) % p for c in poly.all_coeffs()]
    dc = [(n-i)*fc[i] % p for i in range(n)]  # formal deg n-1
    rows = []
    for i in range(n-1):
        rows.append([0]*i+fc+[0]*(n-2-i))
    for i in range(n):
        rows.append([0]*i+dc+[0]*(n-1-i))
    return int(sp.Matrix(rows).det()) % p


def reduce_factorization(f, p):
    g = sp.Poly(f, X, modulus=p)
    _, factors = sp.factor_list(g.as_expr(), X, modulus=p)
    return g, [(sp.Poly(h, X, modulus=p), int(m)) for h, m in factors]


def mulmod(a, b, h, p):
    """Independent coefficient-list multiplication in F_p[X]/(h), h monic."""
    d = len(h)-1
    coeff = [0]*(2*d-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            coeff[i+j] = (coeff[i+j] + x*y) % p
    for k in range(2*d-2,d-1,-1):
        c=coeff[k]
        for j in range(d):
            coeff[k-d+j]=(coeff[k-d+j]-c*h[j]) % p
    return tuple(coeff[:d])


def xpmod(hpoly, p, exp):
    hcoeff=[int(c) % p for c in reversed(hpoly.all_coeffs())]
    d=len(hcoeff)-1
    one=tuple([1]+[0]*(d-1))
    xx=tuple(([0,1]+[0]*(d-2)) if d>1 else [-hcoeff[0] % p])
    ret=one
    while exp:
        if exp&1:ret=mulmod(ret,xx,hcoeff,p)
        xx=mulmod(xx,xx,hcoeff,p)
        exp//=2
    return ret


class GoodReduction(unittest.TestCase):
    pass


def good_test(f,p):
    def test(self):
        degree=sp.Poly(f,X).degree()
        disc=int(sp.discriminant(f,X))
        mod=sp.Poly(f,X, modulus=p)
        _,fac=reduce_factorization(f,p)
        degree_sum=sum(q.degree()*m for q,m in fac)
        self.assertEqual(degree,degree_sum)
        sqfree=all(m==1 for q,m in fac)
        gcd_degree=mod.gcd(mod.diff()).degree()
        self.assertEqual(gcd_degree==0, sqfree)
        self.assertEqual(disc%p !=0, sqfree)
        self.assertEqual(int(mod.discriminant())%p, disc%p)
        result=det_sylvester_with_formal_derivative(f,p)
        sign=(-1)**(degree*(degree-1)//2)
        self.assertEqual((sign*result)%p, disc%p)
    return test

for name,f in F.items():
    for p in P:
        setattr(GoodReduction, f'test_{name}_{p:02}', good_test(f,p))


class FrobeniusOrbits(unittest.TestCase):
    pass


def frob_orbit_test(f,p):
    def test(self):
        g,fac=reduce_factorization(f,p)
        if any(m>1 for _,m in fac):
            self.skipTest('bad prime: repeated factors are excluded by hypothesis')
        for factor,exponent in fac:
            d=factor.degree()
            h=[int(c)%p for c in reversed(factor.all_coeffs())]
            first=tuple([0,1]+[0]*(d-2)) if d>1 else (-h[0]%p,)
            reached=first
            for k in range(1,d):
                reached=xpmod(factor,p,p**k)
                self.assertNotEqual(reached,first, f'p={p}, factor={factor}, k={k}')
            self.assertEqual(xpmod(factor,p,p**d),first)
        self.assertEqual(sum(fac_.degree() for fac_,m in fac),g.degree())
    return test

for name,f in F.items():
    for p in [2,3,5,7,11,13,17,19,23,59]:
        if int(sp.discriminant(f,X))%p != 0:
            setattr(FrobeniusOrbits,f'test_frobenius_{name}_{p:02}',frob_orbit_test(f,p))


class GroupCycleRestrictions(unittest.TestCase):
    def test_cubic_S3_two_types(self):
        for p,expected in [(2,(3,)),(5,(1,2)),(59,(1,1,1))]:
            _,fac=reduce_factorization(F['cubic_S3'],p)
            self.assertEqual(tuple(sorted(q.degree() for q,m in fac)),expected)

    def test_cubic_C3_all_good_types(self):
        for p in P:
            if p==3:continue
            _,fac=reduce_factorization(F['cubic_C3'],p)
            self.assertIn(tuple(sorted(q.degree() for q,m in fac)),{(3,),(1,1,1)})

    def test_quartic_D4_forbids_3_cycle(self):
        for p in P:
            if p==2:continue
            _,fac=reduce_factorization(F['quartic_D4'],p)
            self.assertNotIn(3,[q.degree() for q,m in fac])
            self.assertIn(tuple(sorted(q.degree() for q,m in fac)),{(4,),(2,2),(1,1,2),(1,1,1,1)})

    def test_quartic_V4_only_double_transpositions(self):
        for p in P:
            if int(sp.discriminant(F['quartic_V4'],X))%p==0:continue
            _,fac=reduce_factorization(F['quartic_V4'],p)
            self.assertIn(tuple(sorted(q.degree() for q,m in fac)),{(1,1,1,1),(2,2)})

    def test_reducible_quadratic_plus_linear(self):
        self.assertEqual(sp.expand(F['reducible']),X**3-3*X**2-2*X+6)
        self.assertEqual(int(sp.discriminant(F['reducible'],X)),392)
        _,fac=reduce_factorization(F['reducible'],5)
        self.assertEqual(tuple(sorted(q.degree() for q,m in fac)),(1,2))

    def test_bad_prime_23(self):
        _,fac=reduce_factorization(F['cubic_S3'],23)
        self.assertEqual(sorted((q.degree(),m) for q,m in fac),[(1,1),(1,2)])

    def test_bad_prime_2(self):
        _,fac=reduce_factorization(X**2-5,2)
        self.assertEqual([(q.degree(),m) for q,m in fac],[(1,2)])

    def test_example_59_exact_roots(self):
        self.assertEqual([a for a in range(59) if (a**3-a-1)%59==0],[4,13,42])

    def test_nontrivial_group_despite_complete_split(self):
        self.assertEqual(tuple(sorted(q.degree() for q,m in reduce_factorization(F['cubic_S3'],59)[1])),(1,1,1))
        self.assertEqual(tuple(sorted(q.degree() for q,m in reduce_factorization(F['cubic_S3'],2)[1])),(3,))

    def test_parity_cubic_C3(self):
        self.assertEqual(int(sp.discriminant(F['cubic_C3'],X)),81)
        for p in P:
            if p==3:continue
            _,fac=reduce_factorization(F['cubic_C3'],p)
            self.assertEqual((3-len(fac))%2,0)

    def test_parity_cubic_S3_bad_vs_good(self):
        self.assertEqual(int(sp.discriminant(F['cubic_S3'],X)),-23)
        g,fac=reduce_factorization(F['cubic_S3'],5)
        self.assertEqual((g.degree()-len(fac))%2,1)

    def test_derivative_zero_characteristic_2(self):
        g=sp.Poly(X**4+X**2+1,X,modulus=2)
        self.assertTrue(g.diff().is_zero)
        self.assertEqual(g.gcd(g.diff()).degree(),4)
        self.assertEqual(int(g.discriminant())%2,0)

    def test_derivative_degree_drop_in_char3(self):
        f=X**3+2*X+1
        g=sp.Poly(f,X,modulus=3)
        self.assertEqual(g.diff().degree(),0)
        self.assertEqual(int(g.discriminant())%3,int(sp.discriminant(f,X))%3)


class FieldFourFrobenius(unittest.TestCase):
    @staticmethod
    def mul16(a,b):
        out=0
        for i in range(4):
            if (b>>i)&1:out^=a<<i
        for i in range(6,3,-1):
            if (out>>i)&1:out^=(0b10011 << (i-4))
        return out

    @classmethod
    def pow16(cls,a,n):
        res=1
        while n:
            if n&1:res=cls.mul16(res,a)
            a=cls.mul16(a,a)
            n//=2
        return res

    def test_field_subfield_F4_four_elements(self):
        self.assertEqual(len([a for a in range(16) if self.pow16(a,4)==a]),4)

    def test_F16_q4_frobenius_2_cycle(self):
        outside=[a for a in range(16) if self.pow16(a,4)!=a]
        self.assertTrue(outside)
        for a in outside:
            self.assertEqual(self.pow16(a,16),a)
            self.assertNotEqual(self.pow16(a,4),a)

    def test_quadratic_F4_coefficient_trace_norm(self):
        base={a for a in range(16) if self.pow16(a,4)==a}
        for a in range(16):
            if a in base:continue
            aq=self.pow16(a,4)
            self.assertIn(a^aq,base)
            self.assertIn(self.mul16(a,aq),base)

    def test_q4_factor_degrees_one_and_two(self):
        a=2  # root of X^4+X+1 in F16, not in the F4 subfield
        self.assertNotEqual(self.pow16(a,4),a)
        self.assertEqual(self.pow16(a,16),a)
        b=1  # linear root in F4
        self.assertEqual(self.pow16(b,4),b)
        self.assertNotEqual(a,b)
        self.assertNotEqual(self.pow16(a,4),b)


if __name__ == '__main__':
    unittest.main(verbosity=2)
