"""Independent regression tests for stable AA-05; finite tests do not replace proofs."""
from itertools import permutations, product
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[2]
SRC=(ROOT/"chapters/pl/abstract_algebra/05-szeregi-podnormalne-rozwiazalnosc-i-nilpotentnosc.tex").read_text("utf-8")

def mul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    return tuple(a.index(i) for i in range(len(a)))

def generated(gens):
    e=tuple(range(len(gens[0])))
    s={e}
    while True:
        n=s|{mul(x,g) for x in s for g in gens}|{mul(x,inv(g)) for x in s for g in gens}
        if n==s:return frozenset(n)
        s=n

def comm(a,b):
    return mul(mul(mul(a,b),inv(a)),inv(b))

def derived(group):
    return generated(tuple(comm(a,b) for a in group for b in group))

def even(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

class AA05Regressions(unittest.TestCase):
    def test_labels_proofs_and_refs(self):
        ls=re.findall(r'\\label\{([^}]+)\}',SRC)
        self.assertEqual(len(ls),27)
        self.assertEqual(len(ls),len(set(ls)))
        self.assertEqual(SRC.count(r'\begin{proof}'),14)
        self.assertEqual(SRC.count(r'\end{proof}'),14)
        labels=set(ls)
        folder=ROOT/"chapters/pl/abstract_algebra"
        for p in folder.glob("0[1-4]-*.tex"):
            labels.update(re.findall(r'\\label\{([^}]+)\}',p.read_text("utf-8")))
        self.assertTrue(set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',SRC))<=labels)

    def test_s4_and_a4_derived_series(self):
        s4=frozenset(permutations(range(4)))
        a4=frozenset(p for p in s4 if even(p))
        v4=frozenset({(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)})
        self.assertEqual(derived(s4),a4)
        self.assertEqual(derived(a4),v4)
        self.assertEqual(len(derived(v4)),1)

    def test_a5_class_sizes_and_simplicity_arithmetic(self):
        a5=frozenset(p for p in permutations(range(5)) if even(p))
        classes={frozenset(mul(mul(h,g),inv(h)) for h in a5) for g in a5}
        sizes=sorted(map(len,classes))
        self.assertEqual(sizes,[1,12,12,15,20])
        classes=list(classes)
        for mask in range(1<<len(classes)):
            size=sum(len(c) for i,c in enumerate(classes) if mask>>i&1)
            if any((0,1,2,3,4) in c for i,c in enumerate(classes) if mask>>i&1):
                if 60%size==0:
                    self.assertIn(size,(1,60))

    def test_disjoint_transposition_factorization(self):
        import itertools
        def cyc(*values):
            p=list(range(4))
            for i,x in enumerate(values):p[x]=values[(i+1)%len(values)]
            return tuple(p)
        for a,b,c,d in itertools.permutations(range(4)):
            self.assertEqual(mul(cyc(a,b),cyc(c,d)),mul(cyc(a,c,b),cyc(a,c,d)))

    def test_c4_and_klein_factors_do_not_determine_group(self):
        c4=generated(((1,2,3,0),))
        v4=generated(((1,0,3,2),(2,3,0,1)))
        e=(0,1,2,3)
        self.assertEqual(len(c4),len(v4))
        self.assertEqual(len(v4),4)
        self.assertTrue(any(mul(x,x)!=e for x in c4))
        self.assertTrue(all(mul(x,x)==e for x in v4))

    def test_nilpotent_dihedral_and_non_nilpotent_s3(self):
        d8=generated(((1,2,3,0),(0,3,2,1)))
        e=(0,1,2,3)
        dprime=derived(d8)
        self.assertEqual(len(dprime),2)
        self.assertTrue(all(comm(x,y)==e for x in dprime for y in d8))
        s3=frozenset(permutations(range(3)))
        sprime=derived(s3)
        self.assertEqual(len(sprime),3)
        self.assertEqual(generated(tuple(comm(x,y) for x in sprime for y in s3)),sprime)

    def test_trivial_and_prime_cyclic_series(self):
        e=(0,1,2)
        s3=frozenset(permutations(range(3)))
        a3=derived(s3)
        self.assertEqual(len(a3),3)
        self.assertEqual(len(derived(a3)),1)
        self.assertEqual(len(s3)//len(a3),2)

if __name__=="__main__":
    unittest.main()
