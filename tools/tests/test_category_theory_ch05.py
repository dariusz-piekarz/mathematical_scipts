"""CAT-05 finite-model regressions; general proofs are in the chapter."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/05-obiekty-uniwersalne-poczatkowe-koncowe-zerowe.tex"

def maps(n,m):
    return list(itertools.product(range(m),repeat=n))

def comp(g,f):
    return tuple(g[i] for i in f)

def relations(n,m):
    pairs=list(itertools.product(range(n),range(m)))
    return [frozenset(p for i,p in enumerate(pairs) if mask>>i&1)
            for mask in range(1<<len(pairs))]

def rcomp(s,r):
    return frozenset((a,c) for a,b in r for bb,c in s if b==bb)

class CategoryTheoryCh05(unittest.TestCase):
    def test_CAT_05_001_set_initial_terminal(self):
        for n in range(5):
            self.assertEqual(len(maps(0,n)),1)
            self.assertEqual(len(maps(n,1)),1)
            self.assertEqual(len(maps(n,0)),int(n==0))
            injections=[f for f in maps(2,n) if len(set(f))==2]
            if n==1:
                self.assertFalse(injections)
            self.assertEqual(len(maps(1,n)),n)

    def test_CAT_05_002_rel_zero_absorption(self):
        for n,m in itertools.product(range(3),repeat=2):
            self.assertEqual(relations(n,0),[frozenset()])
            self.assertEqual(relations(0,m),[frozenset()])
            self.assertEqual(rcomp(relations(0,m)[0],relations(n,0)[0]),frozenset())
            for r in relations(n,m):
                self.assertEqual(rcomp(frozenset(),r),frozenset())
                self.assertEqual(rcomp(r,frozenset()),frozenset())
            identity=frozenset((i,i) for i in range(n))
            self.assertEqual(identity==frozenset(),n==0)

    def test_CAT_05_003_pointed_zero(self):
        for n,m in itertools.product(range(1,5),repeat=2):
            for a,b in itertools.product(range(n),range(m)):
                out=[f for f in maps(1,n) if f[0]==a]
                inc=[f for f in maps(n,1) if f[a]==0]
                self.assertEqual(len(out),1)
                self.assertEqual(len(inc),1)
                self.assertEqual(comp((b,),inc[0]),(b,)*n)
                for f in maps(n,m):
                    if f[a]==b:
                        self.assertEqual(comp(f,(a,)*n),(b,)*n)
                        self.assertEqual(comp((a,)*m,f),(a,)*n)

    def test_CAT_05_004_ring_terminal_obstruction(self):
        # In Z/n, both 2*1=0 and 3*1=0 force n=1.
        for n in range(1,101):
            self.assertEqual(2%n==0 and 3%n==0,n==1)
            for a,b in itertools.product(range(-4,5),repeat=2):
                self.assertEqual((a*b)%n,((a%n)*(b%n))%n)

    def test_CAT_05_005_source_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:uniwersalne","def:poczatkowy","tw:unique-universal",
                      "cat:ex:initial-ring","cat:ex:pointed-zero",
                      "cat:def:strict-initial","cat:def:zero-morphism",
                      "cat:prop:zero-absorption","cat:prop:zero-functor"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
