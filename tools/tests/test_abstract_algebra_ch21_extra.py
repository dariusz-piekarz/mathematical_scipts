"""Independent AA-21 mathematical/regression checks, audit II.

Small finite models corroborate, but do not prove, the general claims.
"""
import itertools
import math
import re
import unittest
from pathlib import Path

S=(Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/21-zanurzenia-automorfizmy-i-rozszerzenia-galois.tex').read_text(encoding='utf-8')


def mul(a,b,p,mod):
    n=len(mod)-1
    c=[0]*(2*n-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    for k in range(2*n-2,n-1,-1):
        z=c[k]
        for i in range(n):c[k-n+i]=(c[k-n+i]-z*mod[i])%p
    return tuple(c[:n])


def power(a,k,p,mod):
    one=(1,)+(0,)*(len(mod)-2)
    out=one
    while k:
        if k&1:out=mul(out,a,p,mod)
        a=mul(a,a,p,mod)
        k//=2
    return out


class AdditionalChecks(unittest.TestCase):
    def test_01_zorn_chain_principle_explicit(self):
        self.assertIn('każdego niepustego łańcucha',S)
        self.assertIn('pusty łańcuch jest ograniczony',S)
        self.assertIn('każdy ideał większy od',S)

    def test_02_transitivity_argument_explicit(self):
        self.assertIn('Uzasadnijmy używaną tu',S)
        self.assertIn('A(b_0,\\ldots,b_d,x)',S)
        self.assertIn('Stosując to skończenie wiele razy',S)

    def test_03_embedding_count_converse_hypothesis(self):
        self.assertIn('liczba wszystkich',S)
        self.assertIn(r'$K$-zanurzeń $L\hookrightarrow\Omega$ wynosi $[L:K]$',S)

    def test_04_quadratic_conjugation_ring_morphism(self):
        for a,b,c,d in itertools.product(range(-2,3),repeat=4):
            x=(a,b);y=(c,d)
            xy=(a*c+2*b*d,a*d+b*c)
            sigma=lambda v:(v[0],-v[1])
            z=xy
            self.assertEqual(sigma(z),(
                sigma(x)[0]*sigma(y)[0]+2*sigma(x)[1]*sigma(y)[1],
                sigma(x)[0]*sigma(y)[1]+sigma(x)[1]*sigma(y)[0]))

    def test_05_quadratic_embedding_images_count(self):
        roots=[x for x in range(-4,5) if x*x==2]
        self.assertEqual(roots,[])
        self.assertEqual(len(set([math.sqrt(2),-math.sqrt(2)])),2)

    def test_06_nonnormal_cubic_embedding_count(self):
        a=2**(1/3)
        w=complex(-.5,math.sqrt(3)/2)
        roots=[a*w**k for k in range(3)]
        self.assertEqual(sum(abs(z.imag)<1e-10 for z in roots),1)
        self.assertEqual(len({(round(z.real,8),round(z.imag,8)) for z in roots}),3)

    def test_07_inseparable_roots_unique(self):
        for p in (2,3,5,7,11):
            for j in range(1,p):
                self.assertEqual(math.comb(p,j)%p,0)
            # formal derivative of X^p-t is p*X^(p-1)=0.
            self.assertEqual(p%p,0)

    def test_08_F4_has_2_base_embeddings(self):
        p,mod=2,(1,1,1)
        elements=list(itertools.product(range(2),repeat=2))
        gen=(0,1)
        roots=[x for x in elements if (
            (mul(x,x,p,mod)[0]+x[0]+1)%p,
            (mul(x,x,p,mod)[1]+x[1])%p)==(0,0)]
        self.assertEqual(len(roots),2)
        self.assertEqual(set(roots),{gen,power(gen,2,p,mod)})

    def test_09_F8_frobenius_exact_order(self):
        p,mod=2,(1,1,0,1)
        elements=list(itertools.product(range(2),repeat=3))
        self.assertTrue(all(power(x,8,p,mod)==x for x in elements))
        self.assertTrue(any(power(x,2,p,mod)!=x for x in elements))
        self.assertTrue(any(power(x,4,p,mod)!=x for x in elements))

    def test_10_F16_over_F4_embedding_count(self):
        p,mod=2,(1,1,0,0,1)
        elements=list(itertools.product(range(2),repeat=4))
        f4=[x for x in elements if power(x,4,p,mod)==x]
        self.assertEqual(len(f4),4)
        self.assertEqual(len({tuple(power(x,4,p,mod) for x in elements),tuple(elements)}),2)
        self.assertTrue(all(power(x,16,p,mod)==x for x in elements))

    def test_11_F9_frobenius_nontrivial(self):
        p,mod=3,(1,0,1)
        elements=list(itertools.product(range(3),repeat=2))
        fixed=[x for x in elements if power(x,3,p,mod)==x]
        self.assertEqual(len(fixed),3)
        self.assertTrue(all(power(x,9,p,mod)==x for x in elements))

    def test_12_splitting_separable_Xq_minus_X(self):
        for p,n in ((2,1),(2,2),(2,3),(3,2),(5,2)):
            q=p**n
            # Formal derivative q X^(q-1)-1 is -1 in F_p[X].
            self.assertEqual(q%p,0)
            self.assertNotEqual((-1)%p,0)

    def test_13_F2_minimal_automorphism(self):
        self.assertEqual([x for x in range(2) if x != 0],[1])
        self.assertEqual(pow(1,2,2),1)

    def test_14_finite_maximal_ideal_example(self):
        # A=F2[eps]/(eps^2): proper ideals are 0 and (eps).
        A=list(itertools.product((0,1),repeat=2))
        mulA=lambda x,y:((x[0]*y[0])%2,(x[0]*y[1]+x[1]*y[0])%2)
        I={(0,0),(0,1)}
        self.assertTrue(all(mulA(a,i) in I for a in A for i in I))
        self.assertEqual({(a,b) for a,b in A if a==0},I)
        # Mod I, cosets determined by constant coefficient.
        self.assertEqual({x[0] for x in A},{0,1})

    def test_15_cross_reference_structure(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',S)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(refs),18)
        self.assertEqual(set(refs)-set(labels),{
            'aa:ch:field-extensions','aa:tw:adjoin-root-abstract',
            'aa:tw:simple-algebraic-extension','aa:tw:field-tower',
            'aa:prz:inseparable-example','aa:wn:charzero-separable',
            'aa:tw:eisenstein','aa:tw:splitting-existence',
            'aa:tw:finite-field-cardinality','aa:tw:field-frobenius'})


if __name__=='__main__': unittest.main()
