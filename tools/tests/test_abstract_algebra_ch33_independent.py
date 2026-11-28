"""AA-33 independent stabilization tests: direct Sylvester determinants and algebraic oracles."""
import unittest
import itertools
import sympy as S

X=S.Symbol('X')


def res_by_columns(f,g,m=None,n=None):
    f,g=S.Poly(f,X),S.Poly(g,X)
    if m is None: m=f.degree()
    if n is None: n=g.degree()
    if m < 1 or n < 1 or f.degree()>m or g.degree()>n:
        raise ValueError('formal degrees must be positive bounds')
    size=m+n
    # Independently build direct matrix from the universal coefficient definition.
    C=[[S.Integer(0)]*size for _ in range(size)]
    for col in range(n):
        for k in range(m+1): C[k+col][col]=f.nth(k)
    for j in range(m):
        for k in range(n+1): C[k+j][n+j]=g.nth(k)
    return S.expand((-1)**(m*n)*S.Matrix(C).det(method='bareiss'))


def gcd_degree_mod_p(f,g,p):
    def rem(a,b):
        a=a[:]
        while a and a[-1]==0: a.pop()
        while b and b[-1]==0: b.pop()
        while len(a)>=len(b) and b:
            d=len(a)-len(b)
            factor=(a[-1]*pow(b[-1],-1,p))%p
            for j in range(len(b)):
                a[d+j]=(a[d+j]-factor*b[j])%p
            while a and a[-1]==0: a.pop()
        return a
    aa=[int(v)%p for v in S.Poly(f,X).all_coeffs()[::-1]]
    bb=[int(v)%p for v in S.Poly(g,X).all_coeffs()[::-1]]
    while aa and aa[-1]==0: aa.pop()
    while bb and bb[-1]==0: bb.pop()
    while bb: aa,bb=bb,rem(aa,bb)
    return len(aa)-1 if aa else -1

class AA33Independent(unittest.TestCase):
    def test_sign_linear(self):
        self.assertEqual(res_by_columns(2*X+1,X+3),5)
        self.assertEqual(res_by_columns(X+3,2*X+1),-5)
    def test_formal_padding_1(self):
        self.assertEqual(res_by_columns(2*X+1,X+3,1,2),10)
    def test_formal_padding_2(self):
        self.assertEqual(res_by_columns(2*X+1,X+3,2,1),-5)
    def test_formal_padding_3(self):
        self.assertEqual(res_by_columns(X+1,X+1,2,2),0)
    def test_repeated_roots(self):
        self.assertEqual(res_by_columns((X-1)**3,(X+2)**2),729)
    def test_resultant_symmetric_sign(self):
        for f,g in [(X+1,2*X-3),(X**2+1,X**3+X+1),(X**2+X+1,X**2+2)]:
            m,n=S.degree(f,X),S.degree(g,X)
            self.assertEqual(res_by_columns(g,f),(-1)**(m*n)*res_by_columns(f,g))
    def test_exact_biquadratic(self):
        s,t=S.symbols('s t')
        self.assertEqual(S.expand(res_by_columns(X**2-s,X**2-t)-(s-t)**2),0)
    def test_elimination(self):
        s,t=S.symbols('s t')
        self.assertEqual(S.expand(res_by_columns(X**2-s,X-t)-(t*t-s)),0)
    def test_multiplicativity(self):
        a,b,c=X+1,X-2,X**2+X+1
        self.assertEqual(res_by_columns(a*b,c),res_by_columns(a,c)*res_by_columns(b,c))
    def test_scaling(self):
        f=X**3+2*X+1;g=X**2+3
        self.assertEqual(res_by_columns(f,3*g),3**3*res_by_columns(f,g))
    def test_nonunit_linear(self):
        f=1+2*X
        self.assertEqual(res_by_columns(f,f),0)
        self.assertEqual(S.Poly(S.expand(f*(1-2*X))-1,X).all_coeffs()[0] % 4, 0)
        self.assertTrue(all((1+2*r)%4!=0 for r in range(4)))
    def test_derivative_char2(self):
        self.assertEqual(res_by_columns(X**2+1,2*X,2,1)%2,0)
    def test_derivative_char3(self):
        self.assertEqual(res_by_columns(X**3+1,3*X**2,3,2)%3,0)
    def test_degree4_disc(self):
        f=X**4-2*X**2+4*X+3
        v=res_by_columns(f,S.diff(f,X),4,3)
        self.assertEqual(v,S.discriminant(f,X))  # (-1)^6
    def test_degree3_disc(self):
        f=X**3-4*X+7
        v=res_by_columns(f,S.diff(f,X),3,2)
        self.assertEqual(-v,S.discriminant(f,X))  # (-1)^3
    def test_base_change_zero_coefficient(self):
        f=2*X**2+3*X+1;g=X**2+3
        v=int(res_by_columns(f,g))
        for p in (2,3,5,7):
            self.assertEqual(v%p,int(res_by_columns(f,g,2,2))%p)
    def test_roots_direct_product(self):
        f=(X-1)**2*(X+3);g=(X-2)*(X+5)
        self.assertEqual(res_by_columns(f,g),S.expand((g.subs(X,1))**2 *g.subs(X,-3)))
    def test_primitive_monic_symmetry(self):
        f=X**3+X+1;g=X**2+X+1
        self.assertEqual(res_by_columns(f,g),S.resultant(f,g,X))

POLY_PAIRS=[
 (X**2+X+1,X+1),(X**2+X+1,X-1),(X**3+X+1,X**2+1),
 ((X+1)**3,(X+1)**2),(X**3+2*X+2,2*X**2+X+1),
 (X**4+1,X**2+1),(X**3-X-1,X**2-X+1),
 (X**3+3*X+1,X**2+X+2),(X**2+X+1,X**2-X+1),
 (X**4+X+1,X**2+X+1),
]
for i,(f,g) in enumerate(POLY_PAIRS,1):
    def independent_pair(self, f=f, g=g):
        self.assertEqual(res_by_columns(f,g),S.resultant(f,g,X))
        self.assertEqual(res_by_columns(f,g)==0,S.degree(S.gcd(f,g),X)>0)
    setattr(AA33Independent, f'test_direct_pair_{i:02}', independent_pair)

MOD_PAIRS=[(X**2+X+1,X**2+1),(X**2-1,X-1),(X**3+X+1,X**2+X+1),
           (X**3+1,X+1)]
for p in (2,3,5,7):
    for i,(f,g) in enumerate(MOD_PAIRS,1):
        def mod_pair(self,p=p,f=f,g=g):
            self.assertEqual(int(res_by_columns(f,g))%p==0, gcd_degree_mod_p(f,g,p)>0)
        setattr(AA33Independent,f'test_mod_p{p}_pair{i}',mod_pair)

if __name__=='__main__': unittest.main(verbosity=2)
