"""AA-22 audit V: independent executed finite-field and subgroup calculations.
These finite examples check consequences of the proofs but do not prove the general results.
"""
from __future__ import annotations
import itertools
import math
import re
import unittest
from pathlib import Path

SRC = (Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex')
S = SRC.read_text(encoding='utf-8')

class FiniteField:
    def __init__(self,p,mod):
        self.p=p;self.mod=tuple(x%p for x in mod);self.n=len(mod)-1
        assert mod[-1]==1
        self.zero=(0,)*self.n;self.one=(1,)+(0,)*(self.n-1)
        self.elements=list(itertools.product(range(p),repeat=self.n))
    def add(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
    def neg(self,a):return tuple(-x%self.p for x in a)
    def mul(self,a,b):
        a=list(a); b=list(b);v=[0]*(2*self.n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%self.p
        for k in range(len(v)-1,self.n-1,-1):
            if v[k]:
                for j in range(self.n):v[k-self.n+j]=(v[k-self.n+j]-v[k]*self.mod[j])%self.p
        return tuple(v[:self.n])
    def pow(self,a,k):
        out=self.one
        while k:
            if k&1:out=self.mul(out,a)
            a=self.mul(a,a);k>>=1
        return out
    def Frob(self,a,j=1):return self.pow(a,self.p**j)
    def fixed(self,indices):return {a for a in self.elements if all(self.Frob(a,i)==a for i in indices)}
    def order(self,a):
        if a==self.zero:return 0
        x=self.one
        for d in range(1,len(self.elements)):
            x=self.mul(x,a)
            if x==self.one:return d
        raise AssertionError('element without finite order')
    def prod(self,ls):
        x=self.one
        for z in ls:x=self.mul(x,z)
        return x
    def orbit_poly(self,a,exponents):
        # The polynomial prod (X - a^(p^i)), coefficient list in ascending order.
        orbit=sorted({self.Frob(a,i) for i in exponents})
        coef=[self.one]
        for y in orbit:
            v=[self.zero]*(len(coef)+1)
            for i,c in enumerate(coef):
                v[i]=self.add(v[i], self.neg(self.mul(c,y)))
                v[i+1]=self.add(v[i+1],c)
            coef=v
        return coef,orbit
    def determinant(self,rows):
        n=len(rows);res=self.zero
        for perm in itertools.permutations(range(n)):
            sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            product=self.prod(rows[i][perm[i]] for i in range(n))
            res=self.add(res, product if sign==1 else self.neg(product))
        return res

F4=FiniteField(2,(1,1,1))
F8=FiniteField(2,(1,1,0,1))
F16=FiniteField(2,(1,1,0,0,1))
F27=FiniteField(3,(1,2,0,1))

class IndependentAuditV(unittest.TestCase):
    def test_01_source_exact_statement_counts(self):
        self.assertEqual(S.count(r'\begin{proof}'),5)
        self.assertEqual(S.count(r'\end{proof}'),5)
        self.assertEqual(S.count(r'\begin{przyklad}'),4)
    def test_02_source_all_unique_labels(self):
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual(len(labels),12)
        self.assertEqual(len(set(labels)),12)
    def test_03_source_reference_count(self):
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',S)),21)
    def test_04_source_multiplicative_orbit(self):
        self.assertIn('p_x(X)=\\prod_{y\\in Gx}(X-y)',S)
    def test_05_source_ref_to_extension(self):
        self.assertIn(r'\ref{aa:wn:extend-embedding-finite}',S)
    def test_06_F4_frobenius_order(self):
        self.assertTrue(all(F4.Frob(x,2)==x for x in F4.elements))
        self.assertTrue(any(F4.Frob(x)!=x for x in F4.elements))
    def test_07_F8_frobenius_order(self):
        self.assertTrue(all(F8.Frob(x,3)==x for x in F8.elements))
        self.assertTrue(any(F8.Frob(x,1)!=x for x in F8.elements))
    def test_08_F16_frobenius_order(self):
        self.assertTrue(all(F16.Frob(x,4)==x for x in F16.elements))
        self.assertTrue(any(F16.Frob(x,2)!=x for x in F16.elements))
    def test_09_F27_frobenius_order(self):
        self.assertTrue(all(F27.Frob(x,3)==x for x in F27.elements))
        self.assertTrue(any(F27.Frob(x)!=x for x in F27.elements))
    def test_10_F4_artin_fixed_field_size(self):
        self.assertEqual(len(F4.fixed([0])),4)
        self.assertEqual(len(F4.fixed([1])),2)
    def test_11_F8_artin_fixed_field_size(self):
        self.assertEqual(len(F8.fixed([0])),8)
        self.assertEqual(len(F8.fixed([1,2])),2)
    def test_12_F16_artin_fixed_field_size(self):
        self.assertEqual(len(F16.fixed([0])),16)
        self.assertEqual(len(F16.fixed([2])),4)
        self.assertEqual(len(F16.fixed([1,2,3])),2)
    def test_13_F27_artin_fixed_field_size(self):
        self.assertEqual(len(F27.fixed([0])),27)
        self.assertEqual(len(F27.fixed([1,2])),3)
    def test_14_F16_moore_independence(self):
        basis=[F16.one]+[tuple(1 if j==i else 0 for j in range(4)) for i in range(1,4)]
        matrix=[[F16.Frob(z,i) for z in basis] for i in range(4)]
        self.assertNotEqual(F16.determinant(matrix),F16.zero)
    def test_15_F8_moore_independence(self):
        basis=[tuple(1 if k==i else 0 for k in range(3)) for i in range(3)]
        matrix=[[F8.Frob(z,i) for z in basis] for i in range(3)]
        self.assertNotEqual(F8.determinant(matrix),F8.zero)
    def test_16_F16_orbit_poly_fixed_under_galois(self):
        for x in F16.elements:
            coeff,_=F16.orbit_poly(x,[0,1,2,3])
            self.assertTrue(all(F16.Frob(c)==c for c in coeff))
    def test_17_F16_orbit_poly_fixed_under_subgroup(self):
        for x in F16.elements:
            coeff,_=F16.orbit_poly(x,[0,2])
            self.assertTrue(all(F16.Frob(c,2)==c for c in coeff))
    def test_18_F27_orbit_poly_fixed_under_galois(self):
        for x in F27.elements:
            coeff,_=F27.orbit_poly(x,[0,1,2])
            self.assertTrue(all(F27.Frob(c)==c for c in coeff))
    def test_19_F16_multiplicative_group_cyclic(self):
        self.assertEqual(max(F16.order(z) for z in F16.elements),15)
        self.assertEqual(sum(F16.order(z)==15 for z in F16.elements),math.phi(15) if hasattr(math,'phi') else 8)
    def test_20_F27_multiplicative_group_cyclic(self):
        self.assertEqual(max(F27.order(z) for z in F27.elements),26)
        self.assertEqual(sum(F27.order(z)==26 for z in F27.elements),12)
    def test_21_cyclic12_subgroups_unique_by_index(self):
        # Group is Z/12Z. For every d|12 the subgroup generated by d has index d.
        for d in [1,2,3,4,6,12]:
            H={k*d%12 for k in range(12)}
            self.assertEqual(len(H),12//d)
            self.assertEqual({i for i in range(12) if i%d==0},H)
    def test_22_s3_normal_subgroups_orders(self):
        G=list(itertools.permutations(range(3)))
        e=(0,1,2)
        def comp(a,b):return tuple(a[b[i]] for i in range(3))
        def inv(a):return next(b for b in G if comp(a,b)==e)
        groups=[]
        for r in range(1,7):
            for choices in itertools.combinations(G,r):
                H=set(choices)
                if e in H and all(comp(a,b) in H for a in H for b in H):groups.append(H)
        self.assertEqual(sorted(len(h) for h in groups),[1,2,2,2,3,6])
        normal=[h for h in groups if all(comp(comp(g,x),inv(g)) in h for x in h for g in G)]
        self.assertEqual(sorted(map(len,normal)),[1,3,6])
    def test_23_V4_fixed_subfields(self):
        # elements a+b√2+c√3+d√6; s flips √2, t flips √3
        s=lambda q:(q[0],-q[1],q[2],-q[3])
        t=lambda q:(q[0],q[1],-q[2],-q[3])
        e=[tuple(int(i==j) for i in range(4)) for j in range(4)]
        self.assertEqual([i for i,x in enumerate(e) if s(x)==x],[0,2])
        self.assertEqual([i for i,x in enumerate(e) if t(x)==x],[0,1])
        self.assertEqual([i for i,x in enumerate(e) if s(t(x))==x],[0,3])
    def test_24_F16_galois_degree_lattice(self):
        # |Gal(L/L^H)| = |H| in a finite example with H=<Frob^d>.
        for d in (1,2,4):
            H={j*d%4 for j in range(4)}
            fixed=F16.fixed(H)
            self.assertEqual(len(fixed),2**d)
            self.assertEqual(len(H),4//d)
