"""CAT-01 finite-model and source regressions; not substitutes for proofs."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/01-kategorie-i-ich-pierwsze-przyklady.tex"

def compose(s, r):
    return frozenset((a, c) for a, b in r for b2, c in s if b == b2)

class CategoryTheoryCh01(unittest.TestCase):
    def test_CAT_01_001_relation_category(self):
        pairs = list(itertools.product(range(2), repeat=2))
        relations = [frozenset(p for i, p in enumerate(pairs) if mask >> i & 1)
                     for mask in range(16)]
        identity = frozenset((a,a) for a in range(2))
        for r in relations:
            self.assertEqual(compose(identity,r),r)
            self.assertEqual(compose(r,identity),r)
        for r,s,t in itertools.product(relations,repeat=3):
            self.assertEqual(compose(t,compose(s,r)),compose(compose(t,s),r))

    def test_CAT_01_002_pair_groupoid(self):
        for a,b,c,d in itertools.product(range(3),repeat=4):
            f,g,h=(a,b),(b,c),(c,d)
            def comp(y,x):
                self.assertEqual(x[1],y[0])
                return x[0],y[1]
            self.assertEqual(comp(h,comp(g,f)),comp(comp(h,g),f))
            self.assertEqual(comp((b,a),f),(a,a))
            self.assertEqual(comp(f,(b,a)),(b,b))
            self.assertEqual(comp((b,b),f),f)
            self.assertEqual(comp(f,(a,a)),f)

    def test_CAT_01_003_opposite_noncommutative(self):
        fs=list(itertools.product(range(2),repeat=2))
        def comp(g,f):
            return tuple(g[f[x]] for x in range(2))
        def op(g,f):
            return comp(f,g)
        ident=(0,1)
        for f,g,h in itertools.product(fs,repeat=3):
            self.assertEqual(op(h,op(g,f)),op(op(h,g),f))
            self.assertEqual(op(g,f),comp(f,g))
            self.assertEqual(op(ident,f),f)
            self.assertEqual(op(f,ident),f)
        self.assertNotEqual(op((0,0),(1,1)),comp((0,0),(1,1)))

    def test_CAT_01_004_module_maps(self):
        # Linear maps on the left regular module of the noncommutative ring M_2(F_2):
        # right multiplication by a fixed matrix.
        mats=list(itertools.product(range(2),repeat=4))
        def mul(a,b):
            return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%2
                         for i in range(2) for j in range(2))
        for x,r,a,b in itertools.product(mats,repeat=4):
            self.assertEqual(mul(mul(mul(r,x),a),b),mul(r,mul(mul(x,a),b)))

    def test_CAT_01_005_source_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:kategorie","def:kategoria","def:op","przyklad:poset",
                      "przyklad:monoid-kat","przyklad:mat","przyklad:sciezki",
                      "cat:def:uniwersum","cat:def:konkretna","cat:def:grupoid"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
