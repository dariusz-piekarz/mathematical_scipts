"""AA-11: independent finite-model, arithmetic and source-structure regression tests."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import re, unittest

SRC=Path(__file__).resolve().parents[2]/'chapters/pl/abstract_algebra/11-pierscienie-wielomianow-i-kryteria-nierozkladalnosci.tex'
TEXT=SRC.read_text(encoding='utf-8')

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return tuple(p)

def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ])

def mul(a,b):
    if not a or not b:return ()
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): z[i+j]+=u*v
    return trim(z)

def evalpoly(p,x):
    y=0
    for c in reversed(p):y=y*x+c
    return y

def residue(p,n):return trim(tuple(x%n for x in p))
def divmod_field(f,g,p):
    f=residue(f,p);g=residue(g,p)
    if not g:raise ZeroDivisionError
    q=[0]*max(0,len(f)-len(g)+1)
    while len(f)>=len(g):
        d=len(f)-len(g);t=f[-1]*pow(g[-1],-1,p)%p;q[d]=(q[d]+t)%p
        tmp=list(f)
        for j,v in enumerate(g):tmp[d+j]=(tmp[d+j]-t*v)%p
        f=residue(tmp,p)
    return residue(q,p),f

def divmod_unit_ring(f,g,m):
    f=residue(f,m);g=residue(g,m)
    if not g or gcd(g[-1],m)!=1:raise ValueError
    q=[0]*max(0,len(f)-len(g)+1)
    while len(f)>=len(g):
        d=len(f)-len(g);t=f[-1]*pow(g[-1],-1,m)%m;q[d]=(q[d]+t)%m
        tmp=list(f)
        for j,v in enumerate(g):tmp[d+j]=(tmp[d+j]-t*v)%m
        f=residue(tmp,m)
    return residue(q,m),f

def content(f):
    d=0
    for x in f:d=gcd(d,abs(x))
    return d

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def irreducible_small_monic(f,p):
    f=residue(f,p);d=len(f)-1
    if d<1:return False
    for deg in range(1,d//2+1):
        for coeff in product(range(p),repeat=deg):
            if not divmod_field(f,coeff+(1,),p)[1]:return False
    return True

class AA11Regression(unittest.TestCase):
    def test_01_label_uniqueness_and_proofs(self):
        labels=re.findall(r'\\label\{([^}]+)\}',TEXT)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(labels),37)
        self.assertEqual(TEXT.count(r'\begin{proof}'),19)
        self.assertEqual(TEXT.count(r'\end{proof}'),19)
    def test_02_polynomial_finite_support(self):
        for a,b in product(((),(1,),(1,2),(-1,0,1)),repeat=2):
            self.assertLessEqual(len(mul(a,b)),max(0,len(a)+len(b)-1))
            self.assertEqual(mul((),a),())
            self.assertEqual(mul(a,()),())
    def test_03_associativity_and_distributivity(self):
        x=(1,2,3);y=(1,-1,2);z=(-3,1)
        self.assertEqual(mul(mul(x,y),z),mul(x,mul(y,z)))
        self.assertEqual(mul(x,add(y,z)),add(mul(x,y),mul(x,z)))
    def test_04_degree_additivity_integer_domain(self):
        ps=[a for d in range(1,4) for a in product((-2,-1,0,1,2),repeat=d) if a[-1]]
        for a in ps[::11]:
            for b in ps[::13]: self.assertEqual(len(mul(a,b)),len(a)+len(b)-1)
    def test_05_evaluation_ring_homomorphism(self):
        a=(1,-2,3);b=(-1,1,0,2)
        for x in range(-7,8):
            self.assertEqual(evalpoly(add(a,b),x),evalpoly(a,x)+evalpoly(b,x))
            self.assertEqual(evalpoly(mul(a,b),x),evalpoly(a,x)*evalpoly(b,x))
    def test_06_finite_field_kernel_xp_minus_x(self):
        for p in (2,3,5,7):
            f=tuple([0]* (p+1));f=list(f);f[1]=-1;f[p]=1
            for x in range(p):self.assertEqual(evalpoly(f,x)%p,0)
            self.assertTrue(all(evalpoly(f,x)%p==0 for x in range(p)))
    def test_07_unique_reduced_polynomial_representation(self):
        for p in (2,3,5):
            seen=set()
            for a in product(range(p),repeat=p):
                values=tuple(evalpoly(a,x)%p for x in range(p))
                self.assertNotIn(values,seen)
                seen.add(values)
            self.assertEqual(len(seen),p**p)
    def test_08_z8_four_roots(self):
        self.assertEqual([x for x in range(8) if (x*x-1)%8==0],[1,3,5,7])
    def test_09_monic_division_over_zero_divisor_ring(self):
        m=8
        for g in ((0,1),(3,1),(1,0,1),(2,3,1)):
            for f in product(range(m),repeat=3):
                q,r=divmod_unit_ring(f,g,m)
                self.assertEqual(residue(add(mul(q,g),r),m),residue(f,m))
                self.assertTrue(not r or len(r)<len(g))
    def test_10_field_division_mod_prime(self):
        for p in (2,3,5,7):
            for f in ((1,2,3,4),(0,0,1),(),(3,4,0,1)):
                for g in ((1,),(1,1),(2,1,1)):
                    q,r=divmod_field(f,g,p)
                    self.assertEqual(residue(add(mul(q,g),r),p),residue(f,p))
                    self.assertTrue(not r or len(r)<len(residue(g,p)))
    def test_11_factor_theorem(self):
        for a in range(-3,4):
            for f in ((-1,0,1),(1,2,3),(),(2,)):
                q,r=divmod_field(f,(-a,1),101)
                self.assertEqual((r[0] if r else 0),evalpoly(f,a)%101)
    def test_12_lagrange_basis(self):
        for p in (2,3,5):
            for a in range(p):
                for x in range(p):
                    y=1
                    for b in range(p):
                        if b!=a:y=y*(x-b)*pow(a-b,-1,p)%p
                    self.assertEqual(y,int(a==x))
    def test_13_frac_equivalence_relation(self):
        pairs=[(a,b) for a in range(-4,5) for b in range(-4,5) if b]
        for a,b in pairs:
            for c,d in pairs:
                self.assertEqual(a*d==b*c,Fraction(a,b)==Fraction(c,d))
    def test_14_frac_arithmetic(self):
        xs=[Fraction(a,b) for a in range(-3,4) for b in range(1,5)]
        for x,y in product(xs[::3],repeat=2):
            self.assertEqual(x+y,Fraction(x.numerator*y.denominator+y.numerator*x.denominator,x.denominator*y.denominator))
            self.assertEqual(x*y,Fraction(x.numerator*y.numerator,x.denominator*y.denominator))
    def test_15_gauss_content_multiplicative(self):
        fs=[a for a in product(range(-2,3),repeat=3) if any(a)]
        for f in fs[::5]:
            for g in fs[::9]:self.assertEqual(content(mul(f,g)),content(f)*content(g))
    def test_16_product_of_primitive_polynomials(self):
        fs=[a for a in product(range(-3,4),repeat=2) if content(a)==1]
        self.assertTrue(all(content(mul(f,g))==1 for f,g in product(fs,repeat=2)))
    def test_17_gauss_associates(self):
        f=(1,2,1);g=(-1,-2,-1)
        self.assertEqual(content(f),content(g))
        self.assertEqual(tuple(-x for x in f),g)
    def test_18_eisenstein_xn_p(self):
        for p,n in product((2,3,5,7,11),(1,2,3,4,5)):
            f=[0]*(n+1);f[0]=-p;f[n]=1
            self.assertEqual(f[-1]%p,1)
            self.assertTrue(all(x%p==0 for x in f[:-1]))
            self.assertNotEqual(f[0]%(p*p),0)
    def test_19_eisenstein_shift_x4plus1(self):
        f=(2,4,6,4,1)
        self.assertEqual(f,(2,4,6,4,1))
        for x in range(-5,6):
            self.assertEqual(evalpoly(f,x),(x+1)**4+1)
        self.assertTrue(all(c%2==0 for c in f[:-1]))
        self.assertNotEqual(f[0]%4,0)
    def test_20_irreducible_cubic_f2(self):
        self.assertTrue(irreducible_small_monic((1,1,0,1),2))
        self.assertEqual([evalpoly((1,1,0,1),x)%2 for x in range(2)],[1,1])
    def test_21_modp_irred_converse_false(self):
        self.assertEqual(residue((1,0,1),2),residue(mul((1,1),(1,1)),2))
        self.assertEqual(evalpoly((1,0,1),0),1)
    def test_22_preserve_degree_necessary(self):
        f=(1,3,2)
        self.assertEqual(mul((1,2),(1,1)),f)
        self.assertEqual(residue(f,2),(1,1))
    def test_23_rational_root_enumeration(self):
        f=(1,-3,0,2)
        candidates=[Fraction(i,j) for i in (-1,1) for j in (1,2)]
        roots=[x for x in candidates if evalpoly(f,x)==0]
        self.assertEqual(roots,[Fraction(1,1)])
        self.assertEqual(mul((-1,1),(-1,2,2)),f)
    def test_24_quartic_without_roots_factors(self):
        self.assertEqual(mul((2,-2,1),(2,2,1)),(4,0,0,0,1))
    def test_25_parabola_quotient_kernel(self):
        # Verify F(x,y)-F(x,x^2)=(y-x^2)Q(x,y) as polynomial identities.
        def plus(F,G):
            out=F.copy()
            for k,v in G.items():out[k]=out.get(k,0)+v
            return {k:v for k,v in out.items() if v}
        def prod(F,G):
            out={}
            for (i,j),a in F.items():
                for (k,l),b in G.items():
                    t=(i+k,j+l);out[t]=out.get(t,0)+a*b
            return {k:v for k,v in out.items() if v}
        divisor={(0,1):1,(2,0):-1}
        for a,b,c,d,e in product(range(-2,3),repeat=5):
            F={(0,0):a,(1,0):b,(0,1):c,(1,1):d,(0,2):e}
            F={k:v for k,v in F.items() if v}
            H={(0,0):a,(1,0):b,(2,0):c,(3,0):d,(4,0):e}
            H={k:v for k,v in H.items() if v}
            Q={(0,0):c,(1,0):d,(0,1):e,(2,0):e}
            Q={k:v for k,v in Q.items() if v}
            negH={k:-v for k,v in H.items()}
            self.assertEqual(plus(F,negH),prod(divisor,Q))
    def test_26_nilpotent_nonreduced_quotient(self):
        # image x mod x^2 is nonzero, but x*x mod x^2 = 0
        self.assertNotEqual((0,1),())
        self.assertEqual(divmod_field((0,0,1),(0,0,1),2)[1],())
        self.assertNotEqual(divmod_field((0,1),(0,0,1),2)[1],())
    def test_27_self_contained_statement_multivar(self):
        self.assertIn('Niech $R$ będzie przemiennym pierścieniem z jedynką\ni niech $n\\ge1$',TEXT)
    def test_28_self_contained_gauss_content(self):
        self.assertIn('Niech $R$ będzie dziedziną z jednoznacznym rozkładem\nna czynniki i niech $f,g\\in R[x]$ będą niezerowe.',TEXT)
    def test_29_polynomial_zero_factor_edgecase(self):
        self.assertIn('Jeżeli któryś z czynników jest wielomianem\nzerowym',TEXT)
    def test_30_proof_details_sqrt3(self):
        self.assertIn('$m^2=3n^2$',TEXT)



class AA11AuditIIRegression(unittest.TestCase):
    def test_31_zero_ring_factor_theorem(self):
        # In the zero ring, both x-a and f equal the zero polynomial.
        assert residue((0,0,0),1)==()
        self.assertEqual(evalpoly((),0)%1,0)
        # divisibility (0 | 0) is existential: 0=0*c.
        self.assertEqual(residue(mul((),(0,0,0)),1),())
        self.assertIn('Jeśli $R$ jest pierścieniem zerowym',TEXT)

    def test_32_division_same_remainder_implies_same_quotient(self):
        # Monic g: q*g=q'*g cannot hold for distinct q,q', even in Z/8Z.
        m=8;g=(3,1)
        qs=[residue(q,m) for q in product(range(4),repeat=2)]
        self.assertEqual(len({residue(mul(q,g),m) for q in qs}),len(qs))
        self.assertIn("jest wielomianem\nzerowym albo ma stopień mniejszy",TEXT)

    def test_33_division_degrees_independent_check(self):
        for m in (4,6,8,9):
            g=(2,1)
            for f in product(range(m),repeat=3):
                q,r=divmod_unit_ring(f,g,m)
                self.assertEqual(residue(add(mul(q,g),r),m),residue(f,m))
                self.assertTrue(not r or len(r)<2)

    def test_34_gauss_constant_primitive_edge(self):
        for a in range(-20,21):
            if not a: continue
            self.assertEqual(content((a,))==1,abs(a)==1)
        self.assertIn('dla stałego\npierwotnego $f_0$ przyjmujemy pusty iloczyn',TEXT)

    def test_35_eisenstein_nonprimitive_inputs(self):
        # f = 3*x^3 + 6*x^2 + 6*x + 6 has content 3 and is not Eisenstein at 2
        # because 2 | leading coefficient; build a nonprimitive example with content odd.
        f=(6,6,6,3);p=2
        self.assertEqual(content(f),3)
        primitive=tuple(c//3 for c in f)
        self.assertEqual(primitive,(2,2,2,1))
        self.assertTrue(all(c%p==0 for c in primitive[:-1]))
        self.assertTrue(primitive[0]%(p*p)!=0)

    def test_36_rational_roots_unit_and_zero_constant(self):
        for f in ((0,2),(0,0,2),(0,),(0,1,-1)):
            if len(f)<=1: continue
            self.assertEqual(evalpoly(f,0),0)
            self.assertEqual(f[0],0)

    def test_37_polynomial_translation_automorphism(self):
        # Polynomial shift f(x) -> f(x+1); inverse f(x) -> f(x-1).
        from math import comb
        def shift(f,c):
            z=[0]*len(f)
            for i,a in enumerate(f):
                for j in range(i+1):z[j]+=a*comb(i,j)*c**(i-j)
            return trim(z)
        for f in ((1,),(),(1,0,0,1),(-1,2,-3,5),(0,0,1)):
            self.assertEqual(shift(shift(f,1),-1),trim(f))
            self.assertEqual(evalpoly(shift(f,1),3),evalpoly(f,4))

    def test_38_prime_field_lagrange_interpolation(self):
        for p in (2,3,5):
            for values in product(range(p),repeat=p):
                # interpolate via Lagrange basis and reconstruct values
                def L(a,x):
                    z=1
                    for b in range(p):
                        if b!=a:z=z*(x-b)*pow(a-b,-1,p)%p
                    return z
                for x in range(p):
                    self.assertEqual(sum(values[a]*L(a,x) for a in range(p))%p,values[x])

if __name__=='__main__':
    unittest.main()


class AA11AuditIIIIndependent(unittest.TestCase):
    """Further independent edge-case models for audit III."""
    def test_39_universal_polynomial_map_mod_n(self):
        fs=[(),(1,),(0,1),(-3,2,1),(2,-1,4,-2)]
        for n in (1,2,3,4,6,8,9):
            for s in range(n):
                for f,g in product(fs,repeat=2):
                    h=lambda q:evalpoly(q,s)%n
                    self.assertEqual(h(add(f,g)),(h(f)+h(g))%n)
                    self.assertEqual(h(mul(f,g)),h(f)*h(g)%n)
                    self.assertEqual(h((1,)),1%n)

    def test_40_nonzero_polynomial_root_bound_bruteforce(self):
        for p in (2,3,5):
            for degree in range(4):
                for lower in product(range(p),repeat=degree):
                    for leading in range(1,p):
                        f=lower+(leading,)
                        self.assertLessEqual(sum(evalpoly(f,x)%p==0 for x in range(p)),degree)

    def test_41_mod2_irreducible_cubics_have_no_rational_roots(self):
        for a,b,c in product(range(-3,4),repeat=3):
            f=(c,b,a,1)
            if not irreducible_small_monic(f,2):continue
            for z in range(-abs(c)-1,abs(c)+2):
                self.assertNotEqual(evalpoly(f,z),0)

    def test_42_eisenstein_after_content_removal(self):
        f=(6,6,6,3)
        self.assertEqual(content(f),3)
        g=tuple(z//3 for z in f)
        self.assertEqual(g,(2,2,2,1))
        self.assertEqual(g[-1]%2,1)
        self.assertTrue(all(z%2==0 for z in g[:-1]))
        self.assertNotEqual(g[0]%4,0)
        for z in range(-3,4):
            self.assertNotEqual(evalpoly(g,z),0)

    def test_43_product_of_primitive_polynomials_high_degree(self):
        fs=[f for f in product((-2,-1,0,1,2),repeat=3) if content(f)==1]
        for f in fs[::4]:
            for g in fs[::5]:
                self.assertEqual(content(mul(f,g)),1)

    def test_44_linear_factor_theorem_zero_divisor_ring(self):
        for n in (4,6,8,9):
            for a in range(n):
                for f in product(range(n),repeat=3):
                    q,r=divmod_unit_ring(f,(-a,1),n)
                    self.assertEqual(residue(add(mul(q,(-a,1)),r),n),residue(f,n))
                    self.assertEqual(r[0] if r else 0,evalpoly(f,a)%n)

    def test_45_fraction_representatives_independent(self):
        for a,b in product(range(-4,5),range(1,5)):
            for c,d in product(range(-4,5),range(1,5)):
                x=Fraction(a,b);y=Fraction(c,d)
                for k,l in ((1,1),(-2,3),(3,-2)):
                    self.assertEqual(Fraction(k*a,k*b)+Fraction(l*c,l*d),x+y)
                    self.assertEqual(Fraction(k*a,k*b)*Fraction(l*c,l*d),x*y)

    def test_46_multivariate_parabola_substitution(self):
        for i,j in product(range(4),repeat=2):
            for x in range(-3,4):
                self.assertEqual(x**i*(x*x)**j,x**(i+2*j))
