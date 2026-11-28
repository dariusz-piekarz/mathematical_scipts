"""CAT-04 finite-model regressions; general proofs remain in the chapter."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/04-transformacje-naturalne.tex"

def selectors(n,m):
    return itertools.product(range(n), repeat=m)

def pick(a,x):
    return tuple(x[i] for i in a)

def horizontal(a,b,x):
    return tuple(pick(a,x[j]) for j in b)

class CategoryTheoryCh04(unittest.TestCase):
    def test_CAT_04_001_interchange(self):
        # Natural transformations X^n -> X^m induced by coordinate selectors.
        for a,aa,b,bb in itertools.product(selectors(2,3),selectors(3,2),
                                             selectors(2,3),selectors(3,2)):
            for x in itertools.product(itertools.product(range(2),repeat=2),repeat=2):
                lhs=horizontal(pick(aa,a),pick(bb,b),x)
                rhs=horizontal(aa,bb,horizontal(a,b,x))
                self.assertEqual(lhs,rhs)

    def test_CAT_04_002_horizontal_naturality(self):
        for a,b,f in itertools.product(selectors(2,3),selectors(2,3),selectors(2,2)):
            for x in itertools.product(itertools.product(range(2),repeat=2),repeat=2):
                def apply(y):
                    return tuple(tuple(f[i] for i in row) for row in y)
                self.assertEqual(apply(horizontal(a,b,x)),horizontal(a,b,apply(x)))

    def test_CAT_04_003_tensor_unit(self):
        # Z/n-module Z/n; multiplication by a scalar gives a module map.
        for n in range(1,10):
            for r,x,a in itertools.product(range(n),repeat=3):
                self.assertEqual(a*(r*x)%n,r*(a*x)%n)

    def test_CAT_04_004_biddual_finite(self):
        for n in range(5):
            vs=list(itertools.product(range(2),repeat=n))
            evaluations={tuple(sum(a*b for a,b in zip(v,w))%2 for w in vs) for v in vs}
            self.assertEqual(len(evaluations),len(vs))

    def test_CAT_04_005_natural_inverse(self):
        # Commuting squares of functions with bijective horizontal arrows.
        fs=list(itertools.product(range(3),repeat=3))
        perms=list(itertools.permutations(range(3)))
        def comp(g,f): return tuple(g[i] for i in f)
        def inv(p): return tuple(p.index(i) for i in range(len(p)))
        for a,b,f in itertools.product(perms,perms,fs):
            g=comp(comp(b,f),inv(a))
            self.assertEqual(comp(g,a),comp(b,f))
            self.assertEqual(comp(f,inv(a)),comp(inv(b),g))

    def test_CAT_04_006_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:naturalne","def:naturalna","tw:fun-posety",
                      "przyklad:podwojny-dual","tw:skalarnosc","tw:only-id-set",
                      "tw:nat-iso-components","cat:def:horizontal",
                      "cat:thm:interchange","cat:prop:horizontal-assoc",
                      "cat:ex:connecting-natural","cat:ex:derham-natural"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
