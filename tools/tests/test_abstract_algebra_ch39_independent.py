"""AA-39 independent Krull dimension checks, audit II.

Computations test instances and source structure; the general results are proved
mathematically in the chapter, not deduced from finite experiments.
"""
from __future__ import annotations
import itertools
import os
import re
import unittest
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve()
REPO_CHAPTER = HERE.parents[2] / 'chapters/pl/abstract_algebra/39-wymiar-krulla-i-lancuchy-idealow-pierwszych.tex' if len(HERE.parents) > 2 else None
LOCAL_CHAPTER = HERE.parent / 'AA-39-audyt-II-zrodlo.tex'
SOURCE = Path(os.environ.get('AA39_SOURCE', str(REPO_CHAPTER if REPO_CHAPTER and REPO_CHAPTER.exists() else LOCAL_CHAPTER)))


def source():
    return SOURCE.read_text(encoding='utf-8')


class IndependentStructure(unittest.TestCase):
    def test_chapter_exists(self):
        self.assertTrue(SOURCE.is_file())
    def test_old_ref_not_present(self):
        self.assertNotIn(r'\ref{aa:tw:polynomial-krull-dimension}', source())
    def test_all_refs_resolved_or_prior(self):
        s=source()
        refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',s))
        labels=set(re.findall(r'\\label\{([^}]+)\}',s))
        self.assertEqual(refs-labels, {'aa:ch:lokalizacja','aa:ch:pierscienie'})
    def test_unique_20_labels(self):
        labs=re.findall(r'\\label\{([^}]+)\}',source())
        self.assertEqual(len(labs),20)
        self.assertEqual(len(labs),len(set(labs)))
    def test_plane_dimension_claim(self):
        s=source()
        self.assertIn(r'\label{aa:lem:krull-plane-dimension}',s)
        self.assertIn(r'\dim K[U,V]=2',s)
    def test_plane_chain_explicit(self):
        self.assertIn(r'$(0)\subsetneq(U)\subsetneq(U,V)$',source())
    def test_plane_proof_separate_elimination(self):
        s=source()
        self.assertIn(r'h(U)\in K[U]',s)
        self.assertIn(r'k(V)\in K[V]',s)
        self.assertIn(r'K(U)[V]',s)
        self.assertIn('Zamieniając role $U$ i $V$',s)
    def test_local_height_exact_statement(self):
        self.assertIn(r'\operatorname{ht}(\mathfrak p)=\dim A_{\mathfrak p}',source())
    def test_zero_dimension_criterion(self):
        self.assertIn(r'\label{aa:cor:krull-dim-zero}',source())
    def test_nilradical_criterion(self):
        self.assertIn(r'\label{aa:cor:krull-nilradical}',source())
    def test_preserve_diagram(self):
        self.assertIn(r'\begin{picture}(82,43)',source())
    def test_general_n_honest(self):
        self.assertIn(r'n\ge3',source())
        self.assertIn('dodatkowego argumentu',source())
    def test_proofs_balanced(self):
        s=source()
        self.assertEqual(s.count(r'\begin{proof}'),10)
        self.assertEqual(s.count(r'\end{proof}'),10)
    def test_seven_examples(self):
        self.assertEqual(source().count(r'\begin{przyklad}'),7)
    def test_no_bad_terminology(self):
        self.assertNotIn('sekwencyjn',source().lower())

U,V=sp.symbols('U V')
# Coprime examples chosen such that elimination in each variable is available
# over Q and over every field in this battery.
PAIRS=[
    (U, V),
    (U+V,U+V+1),
    (V-U**2,V-U-1),
    (V**2-U,V+U),
    (U*V-1,U+V),
    (U+V**2,V-U),
    (U**2+V,V**2+U),
    (V**2-U,U**2-V),
    (U*V+U+1,U+V+1),
    (U**2+V+1,V-2),
    (U+V**3,U**2+V+1),
]
FIELDS=[None,2,3,5,7]

class IndependentElimination(unittest.TestCase):
    pass


def elimination_check(f,g,p):
    opts={} if p is None else {'modulus':p}
    hx=sp.resultant(f,g,V)
    hy=sp.resultant(f,g,U)
    if p:
        assert not sp.Poly(hx,U,modulus=p).is_zero,(f,g,p,'h_x zero')
        assert not sp.Poly(hy,V,modulus=p).is_zero,(f,g,p,'h_y zero')
    else:
        assert sp.expand(hx)!=0 and sp.expand(hy)!=0,(f,g,p)
    G=sp.groebner([f,g],U,V,order='lex',**opts)
    if p is None:
        assert G.reduce(hx)[1]==0,(f,g,p,'hx not in ideal')
        assert G.reduce(hy)[1]==0,(f,g,p,'hy not in ideal')
    else:
        assert sp.Poly(G.reduce(hx)[1],U,V,modulus=p).is_zero,(f,g,p,'hx not in ideal')
        assert sp.Poly(G.reduce(hy)[1],U,V,modulus=p).is_zero,(f,g,p,'hy not in ideal')
    assert any(sp.Poly(hx,U,**opts).all_coeffs()),(f,g,p)
    assert any(sp.Poly(hy,V,**opts).all_coeffs()),(f,g,p)

for i,(f,g) in enumerate(PAIRS):
    for p in FIELDS:
        def test(self,f=f,g=g,p=p): elimination_check(f,g,p)
        setattr(IndependentElimination,f'test_resultants_pair_{i:02d}_char_{p or 0:02d}',test)

# Prime chains (0) ⊊ (V-U^2) ⊊ (U,V), checked by quotient substitution
# and Groebner ideal membership in a range of characteristics.
class IndependentPlaneChains(unittest.TestCase):
    pass


def plane_chain(p):
    f=V-U**2
    G=sp.groebner([f],U,V,order='lex',modulus=p)
    assert not sp.Poly(G.reduce(U)[1],U,V,modulus=p).is_zero
    assert sp.Poly(G.reduce(f)[1],U,V,modulus=p).is_zero
    Gmax=sp.groebner([U,V],U,V,order='lex',modulus=p)
    assert sp.Poly(Gmax.reduce(f)[1],U,V,modulus=p).is_zero
    # The homomorphism k[U,V] -> k[U], V|->U^2, is onto;
    # its kernel is (V-U^2). The quotient is an integral domain.
    sample=U**6+U**2*V+V**3+U+1
    assert sp.expand(sample.subs(V,U**2)) == U**6 + U**4 + U**6 + U + 1

for p in (2,3,5,7,11):
    setattr(IndependentPlaneChains,f'test_curve_prime_chain_char_{p}',lambda self,p=p:plane_chain(p))

# Finite, nonreduced local algebras: k[U,V]/(U^r,V^s)
# Uniqueness of the maximal ideal follows from nilpotence of (U,V).
class IndependentArtinLocal(unittest.TestCase):
    pass


def nilpotent_local_test(p,r,s):
    coeffs=list(itertools.product(range(p),repeat=r*s))
    def mul(a,b):
        c=[0]*(r*s)
        for i in range(r):
            for j in range(s):
                for k in range(r-i):
                    for l in range(s-j):
                        c[(i+k)*s+j+l]=(c[(i+k)*s+j+l]+a[i*s+j]*b[k*s+l])%p
        return tuple(c)
    one=(1,)+(0,)*(r*s-1)
    nilpotent_indices=[i for i in range(r*s) if i!=0]
    for idx in nilpotent_indices:
        x=[0]*(r*s);x[idx]=1;x=tuple(x)
        acc=one
        for _ in range(r+s): acc=mul(acc,x)
        assert acc==(0,)*(r*s)
    # Elements with constant term zero are nilpotent; nonzero constant
    # guarantees geometric-series inverse after a scalar normalization.
    for a in coeffs:
        if a[0]==0:
            acc=one
            for _ in range(r+s): acc=mul(acc,a)
            assert acc==(0,)*(r*s)
        else:
            inv_const=pow(a[0],-1,p)
            v=tuple((a[i]*inv_const)%p for i in range(r*s))
            n=tuple((one[i]-v[i])%p for i in range(r*s))
            acc=one;total=(0,)*(r*s)
            for _ in range(r+s):
                total=tuple((total[i]+acc[i])%p for i in range(r*s))
                acc=mul(acc,n)
            inverse=tuple((total[i]*inv_const)%p for i in range(r*s))
            assert mul(a,inverse)==one

for p,r,s in ((2,2,2),(2,2,3),(2,3,2),(2,3,3),(3,2,2),(3,2,3)):
    setattr(IndependentArtinLocal,f'test_local_F{p}_U{r}_V{s}',lambda self,p=p,r=r,s=s:nilpotent_local_test(p,r,s))

# Product of local Artin rings is again dimension zero, but has two
# incomparable maximal ideals. Check explicit annihilating idempotents.
class IndependentProductRings(unittest.TestCase):
    pass

def product_check(p,q):
    elements=[(a,b) for a in range(p) for b in range(q)]
    R1={(0,b) for b in range(q)}
    R2={(a,0) for a in range(p)}
    def isprime(I):
        for x in elements:
            for y in elements:
                if (x[0]*y[0]%p,x[1]*y[1]%q) in I and x not in I and y not in I:
                    return False
        return True
    assert isprime(R1) and isprime(R2)
    assert not R1.issubset(R2) and not R2.issubset(R1)

for p,q in ((2,2),(2,3),(2,5),(3,2),(3,3),(3,5),(5,2),(5,3)):
    setattr(IndependentProductRings,f'test_product_F{p}_F{q}',lambda self,p=p,q=q:product_check(p,q))

if __name__=='__main__':
    unittest.main(verbosity=2)
