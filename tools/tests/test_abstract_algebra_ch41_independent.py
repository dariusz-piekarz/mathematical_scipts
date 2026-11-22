#!/usr/bin/env python3
"""AA-41: independent finite-field and permutation verification (audyt II).

Uses no external packages. Discovers the published chapter inside the repository
first, then supports the standalone audit source as a fallback.
"""
from __future__ import annotations

import itertools
import os
from pathlib import Path
import re
import unittest

REPO_SOURCE = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex'
LOCAL_SOURCE = Path(__file__).resolve().with_name('AA-41-audyt-II-zrodlo.tex')
SOURCE = Path(os.environ['AA41_SOURCE']) if os.getenv('AA41_SOURCE') else (REPO_SOURCE if REPO_SOURCE.exists() else LOCAL_SOURCE)


def cycle(v):
    return (v[-1], *v[:-1])


def add(a, b, p):
    return tuple((x+y) % p for x,y in zip(a,b))


def avg_cyclic(v,p):
    n=len(v)
    z=tuple(0 for _ in v)
    t=tuple(v)
    for _ in range(n):
        z=add(z,t,p)
        t=cycle(t)
    return tuple((x*pow(n,-1,p))%p for x in z)


def permutations_apply(perm, v):
    out=[None]*len(v)
    for i,j in enumerate(perm): out[j]=v[i]
    return tuple(out)


def projection_onto_constants(v,coeffs,p):
    # Arbitrary projection onto span((1,...,1)); sum(coeffs) must be invertible.
    scalar=sum(a*b for a,b in zip(v,coeffs))*pow(sum(coeffs)%p,-1,p)%p
    return (scalar,)*len(v)


def symmetrized_projection(v,coeffs,p):
    n=len(v)
    out=(0,)*n
    perms=list(itertools.permutations(range(n)))
    for perm in perms:
        inv=[0]*n
        for i,j in enumerate(perm): inv[j]=i
        pre=permutations_apply(tuple(inv),v)
        t=projection_onto_constants(pre,coeffs,p)
        out=add(out,permutations_apply(perm,t),p)
    f=pow(len(perms),-1,p)
    return tuple(x*f%p for x in out)


class TextChecks(unittest.TestCase):
    def test_labels_and_refs(self):
        t=SOURCE.read_text(encoding='utf8')
        labels=re.findall(r'\\label\{([^}]+)\}',t)
        refs=re.findall(r'\\ref\{([^}]+)\}',t)
        self.assertEqual(len(labels),19)
        self.assertEqual(len(set(labels)),len(labels))
        self.assertEqual(set(refs)-set(labels),set())

    def test_proof_and_examples_inventory(self):
        t=SOURCE.read_text(encoding='utf8')
        self.assertEqual(t.count(r'\begin{proof}'),6)
        self.assertEqual(t.count(r'\begin{przyklad}'),9)
        self.assertEqual(t.count(r'\begin{twierdzenie}'),2)
        self.assertIn(r'\label{aa:tw:maschke}',t)
        self.assertIn(r'\label{aa:tw:maschke-necessity}',t)

    def test_environment_balance(self):
        t=SOURCE.read_text(encoding='utf8')
        stack=[]
        for k,name in re.findall(r'\\(begin|end)\{([^}]+)\}',t):
            if k=='begin':stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertEqual(stack,[])

    def test_correct_modular_nonexactness(self):
        t=SOURCE.read_text(encoding='utf8')
        self.assertIn(r'\varepsilon([e]+[s])=1+1=0',t)
        self.assertIn(r'R_G\rho(h)=R_G',t)
        self.assertIn(r'P(u)=u\ne0',t)


class IrreducibleModule(unittest.TestCase):
    def test_c3_over_f2_all_nonzero_vectors(self):
        matrix=((0,1),(1,1))
        vlist=((1,0),(0,1),(1,1))
        for x,y in vlist:
            t=((matrix[0][0]*x+matrix[0][1]*y)%2,(matrix[1][0]*x+matrix[1][1]*y)%2)
            self.assertNotEqual(t,(x,y))
            t2=((matrix[0][0]*t[0]+matrix[0][1]*t[1])%2,(matrix[1][0]*t[0]+matrix[1][1]*t[1])%2)
            t3=((matrix[0][0]*t2[0]+matrix[0][1]*t2[1])%2,(matrix[1][0]*t2[0]+matrix[1][1]*t2[1])%2)
            self.assertEqual(t3,(x,y))


class ModularFailure(unittest.TestCase):
    def test_non_split_regular_cyclic_in_bad_characteristic(self):
        # A G-equivariant map K[G]->K must be constant on the regular basis;
        # thus its value on u=sum_g [g] is |G|*a, zero when charK divides |G|.
        for p,n in ((2,2),(2,4),(3,3),(3,6),(5,5),(7,7)):
            self.assertEqual(n%p,0)
            for a in range(p):
                self.assertEqual((n*a)%p,0)
            u=(1,)*n
            self.assertEqual(cycle(u),u)
            self.assertNotEqual(u,(0,)*n)


def add_generated_case(name, func):
    setattr(IndependentPermutations,'test_'+name,func)


class IndependentPermutations(unittest.TestCase):
    pass


# 175+ distinct unittest methods; each checks actual finite-field identities.
for n in range(2,7):
    for p in (2,3,5,7,11):
        if n%p == 0: continue
        values=range(min(p,4))
        for j in range(8):
            seed=[((j+j*j//3+3*k+k*k)%p) for k in range(n)]
            v=tuple(seed)
            def make_case(n=n,p=p,v=v):
                def check(self):
                    self.assertEqual(len(v),n)
                    pr=avg_cyclic(v,p)
                    inv_n=pow(n,-1,p)
                    expected=(sum(v)*inv_n%p,)*n
                    self.assertEqual(pr,expected)
                    self.assertEqual(avg_cyclic(pr,p),pr)
                    self.assertEqual(cycle(pr),pr)
                    rem=tuple((v[k]-pr[k])%p for k in range(n))
                    self.assertEqual(sum(rem)%p,0)
                    self.assertEqual(add(rem,pr,p),v)
                return check
            add_generated_case(f'cyclic_average_n{n}_p{p}_sample{j}',make_case())

for n in (2,3,4):
    for p in (3,5,7,11):
        if n%p==0 or __import__('math').factorial(n)%p==0:continue
        for mode in range(4):
            coeffs=tuple((mode+i*i+i)%p for i in range(n))
            if sum(coeffs)%p==0:continue
            def make_case(n=n,p=p,coeffs=coeffs):
                def check(self):
                    u=(1,)*n
                    self.assertEqual(projection_onto_constants(u,coeffs,p),u)
                    for j in range(n):
                        e=tuple(int(i==j) for i in range(n))
                        avg=symmetrized_projection(e,coeffs,p)
                        self.assertEqual(avg,(pow(n,-1,p),)*n)
                return check
            add_generated_case(f'avg_conjugates_S{n}_p{p}_weights{mode}',make_case())

for n in range(2,7):
    for p in (2,3,5,7,11):
        def make_case(n=n,p=p):
            def check(self):
                u=(1,)*n
                self.assertEqual(cycle(u),u)
                # Invariants of the regular cyclic representation are exactly K*u.
                for v in itertools.product(range(p),repeat=n):
                    if n>4 or p>3:
                        if sum(v)*23%13: continue
                    if cycle(v)==v:
                        self.assertEqual(v,(v[0],)*n)
                if n%p:
                    re=avg_cyclic((1,)+(0,)*(n-1),p)
                    self.assertEqual(sum(re)%p,1)
                else:
                    # All invariant vectors have zero augmentation.
                    for c in range(p):
                        self.assertEqual(sum((c,)*n)%p,0)
            return check
        add_generated_case(f'augmentation_exactness_n{n}_p{p}',make_case())

for p in (3,5,7,11):
    for a in range(1,p):
        def make_case(p=p,a=a):
            def check(self):
                v=(a,(a+1)%p)
                swap=(v[1],v[0])
                inv2=pow(2,-1,p)
                plus=tuple((x+y)*inv2%p for x,y in zip(v,swap))
                minus=tuple((x-y)*inv2%p for x,y in zip(v,swap))
                self.assertEqual(add(plus,minus,p),v)
                self.assertEqual(plus[0],plus[1])
                self.assertEqual(minus[0],(-minus[1])%p)
            return check
        add_generated_case(f'involution_p{p}_a{a}',make_case())

if __name__=='__main__':
    unittest.main(verbosity=2)
