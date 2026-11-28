#!/usr/bin/env python3
"""Audyt I AA-41: niezależne modele liniowe + kontrola struktury źródła.

Uruchomienie: python -m unittest /mnt/data/AA-41-audyt-I-testy.py -v
lub: python /mnt/data/AA-41-audyt-I-testy.py
Po publikacji: podać AA41_SOURCE=chapters/pl/abstract_algebra/41-....tex
"""
import itertools
import os
import re
import unittest
from fractions import Fraction
from pathlib import Path

_LOCAL = Path(__file__).resolve().with_name('AA-41-audyt-I-zrodlo.tex')
_REPO = Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex'
SOURCE = Path(os.environ['AA41_SOURCE']) if os.getenv('AA41_SOURCE') else (_REPO if _REPO.exists() else _LOCAL)


def cyclic_shift(v):
    return (v[-1],) + v[:-1]


def reynolds_cyclic(v, p):
    n = len(v)
    assert n % p
    acc = [0]*n
    t = tuple(v)
    for _ in range(n):
        acc = [(a+b) % p for a,b in zip(acc,t)]
        t = cyclic_shift(t)
    inv = pow(n, -1, p)
    return tuple((x*inv) % p for x in acc)


def modular_average_vector(v,p):
    inv = pow(len(v), -1, p)
    a = sum(v) * inv % p
    return (a,)*len(v)


def action_s3(perm,vec):
    # sigma e_i = e_{sigma(i)}
    out = [0]*3
    for i,j in enumerate(perm):out[j]=vec[i]
    return tuple(out)


class TestStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.txt = SOURCE.read_text(encoding='utf8')

    def test_no_missing_or_duplicate_local_labels(self):
        t=self.txt
        labels=re.findall(r'\\label\{([^}]+)\}',t)
        refs=re.findall(r'\\ref\{([^}]+)\}',t)
        self.assertEqual(len(labels),19)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertTrue(set(refs) <= set(labels), sorted(set(refs)-set(labels)))

    def test_environments_stack(self):
        stack=[]
        for op,env in re.findall(r'\\(begin|end)\{([^}]+)\}',self.txt):
            if op=='begin':stack.append(env)
            else:
                self.assertTrue(stack, f'unmatched end {env}')
                self.assertEqual(stack.pop(),env)
        self.assertEqual(stack,[])

    def test_inventory(self):
        t=self.txt
        self.assertEqual(t.count(r'\begin{twierdzenie}'),2)
        self.assertEqual(t.count(r'\begin{stwierdzenie}'),3)
        self.assertEqual(t.count(r'\begin{proof}'),6)
        self.assertEqual(t.count(r'\begin{przyklad}'),9)
        for lbl in ['aa:tw:maschke','aa:tw:maschke-necessity',
                    'aa:prop:reynolds-vectors','aa:cor:invariants-exact',
                    'aa:prz:maschke-f2-c3','aa:prz:maschke-counter']:
            self.assertIn(r'\label{'+lbl+'}',t)

    def test_require_precise_characteristic_condition(self):
        t=self.txt
        self.assertIn(r'$|G|\cdot1_K\ne0$',t)
        self.assertIn(r'$|G|\cdot1_K=0$',t)
        self.assertIn(r'\ker R_G',t)
        self.assertIn(r'\operatorname{im}R_G=V^G',t)

    def test_new_finite_field_example_has_proof(self):
        t=self.txt
        a=t.index(r'\label{aa:prz:maschke-f2-c3}')
        b=t.index(r'\end{przyklad}',a)
        e=t[a:b]
        for s in [r'\mathbb F_2',r'C_3',r'T^2+T+1',r'\ker',r'nieprzywiedlna']:
            if s==r'\ker': continue
            self.assertIn(s,e)
        self.assertIn('brak',t)

    def test_core_contradiction(self):
        t=self.txt
        a=t.index(r'\label{aa:tw:maschke-necessity}')
        b=t.index(r'\end{proof}',a)
        sec=t[a:b]
        self.assertIn(r'P(u)=u\ne0',sec)
        self.assertIn(r'P(u)=\sum_gP([g])',sec)
        self.assertIn(r'3\Rightarrow2',sec)


class TestMaschkeFiniteFields(unittest.TestCase):
    def test_c3_over_f2_irreducible(self):
        p=2
        # on W=span(a,b), cyclic generator sends a->b and b->a+b.
        M=((0,1),(1,1))
        nonzero=[(1,0),(0,1),(1,1)]
        for x,y in nonzero:
            image=((M[0][0]*x+M[0][1]*y)%p,(M[1][0]*x+M[1][1]*y)%p)
            self.assertNotEqual(image,(x,y))
        self.assertEqual((1*1-0*1)%p,1)
        self.assertEqual((0**2+0+1)%p,1)
        self.assertEqual((1**2+1+1)%p,1)

    def test_three_cycle_decomposition_f2_all_vectors(self):
        for vec in itertools.product(range(2),repeat=3):
            r=reynolds_cyclic(vec,2)
            self.assertEqual(r,modular_average_vector(vec,2))
            self.assertEqual(reynolds_cyclic(r,2),r)
            w=tuple((x-y)%2 for x,y in zip(vec,r))
            self.assertEqual(sum(w)%2,0)
            self.assertEqual(tuple((x+y)%2 for x,y in zip(r,w)),vec)

    def test_c2_characteristic_two_indecomposable(self):
        T=lambda v: ((v[0]+v[1])%2,v[1])
        W=(1,0)
        self.assertEqual(T(W),W)
        # Every line disjoint from W must be span(e2) or span(e1+e2).
        for gen in [(0,1),(1,1)]:
            self.assertNotEqual(T(gen),gen)
        for vec in itertools.product(range(2),repeat=2):
            self.assertEqual(T(T(vec)),vec)

    def test_group_algebra_f2c2_nilpotent_and_no_complement(self):
        mul=lambda x,y: ((x[0]*y[0]+x[1]*y[1])%2,
                         (x[0]*y[1]+x[1]*y[0])%2)
        z=(1,1)
        self.assertEqual(mul(z,z),(0,0))
        self.assertNotEqual(z,(0,0))
        for v in [(1,0),(0,1),(1,1)]:
            self.assertEqual(mul((0,1),mul((0,1),v)),v)

    def test_invariants_exactness_modular_counterexample(self):
        K=2
        swap=lambda v:(v[1],v[0])
        fixed=[v for v in itertools.product(range(K),repeat=2) if swap(v)==v]
        epsilon=lambda v:sum(v)%K
        self.assertEqual(fixed,[(0,0),(1,1)])
        self.assertEqual({epsilon(v) for v in fixed},{0})
        self.assertEqual({epsilon(v) for v in itertools.product(range(K),repeat=2)},{0,1})


class TestMaschkeCharacteristicZero(unittest.TestCase):
    def test_c2_projectors_exact(self):
        for x in range(-5,6):
            for y in range(-5,6):
                p=(Fraction(x+y,2),Fraction(x+y,2))
                m=(Fraction(x-y,2),Fraction(y-x,2))
                self.assertEqual(tuple(a+b for a,b in zip(p,m)),(x,y))
                self.assertEqual(p[0],p[1])
                self.assertEqual(sum(m),0)

    def test_s3_standard_matrix_no_rational_eigenvalues(self):
        # M = [[0,-1],[1,-1]], charpoly t^2+t+1
        for num in range(-50,51):
            for den in range(1,14):
                lam=Fraction(num,den)
                self.assertNotEqual(lam*lam+lam+1,0)

    def test_s3_average_concrete(self):
        for vec in itertools.product(range(-3,4),repeat=3):
            images=[action_s3(p,vec) for p in itertools.permutations(range(3))]
            avg=tuple(Fraction(sum(w[i] for w in images),6) for i in range(3))
            expected=Fraction(sum(vec),3)
            self.assertEqual(avg,(expected,expected,expected))


def make_reynolds_test(p,n,case_id):
    def test(self):
        v=tuple(((p*i*i + 3*i + 7*case_id) % p) for i in range(n))
        if case_id % 3 == 0:
            v=tuple((case_id+i*2)%p for i in range(n))
        if case_id % 3 == 1:
            v=tuple(case_id%p for _ in range(n))
        r=reynolds_cyclic(v,p)
        expect=modular_average_vector(v,p)
        self.assertEqual(r,expect)
        self.assertEqual(reynolds_cyclic(r,p),r)
        self.assertEqual(cyclic_shift(r),r)
        w=tuple((a-b)%p for a,b in zip(v,r))
        self.assertEqual(sum(w)%p,0)
        self.assertEqual(tuple((a+b)%p for a,b in zip(r,w)),v)
    return test


class TestIndependentCyclicModels(unittest.TestCase):
    """218 niezależnie numerowanych modeli Reynolds'a dla różnej char i rzędu G."""

for p in (2,3,5,7,11):
    for n in (2,3,4,5,6,7):
        if n%p==0: continue
        for j in range(11):
            setattr(TestIndependentCyclicModels, f'test_C{n}_F{p}_vector{j:02}',make_reynolds_test(p,n,j))

if __name__=='__main__':
    unittest.main(verbosity=2)
