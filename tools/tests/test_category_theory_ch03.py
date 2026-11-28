"""CAT-03 finite-model regression checks; not replacements for general proofs."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/03-funktory-odwzorowania-miedzy-kategoriami.tex"

def comp(g, f):
    return tuple(g[i] for i in f)

class CategoryTheoryCh03(unittest.TestCase):
    def test_CAT_03_001_hom_bifunctor(self):
        maps = list(itertools.product(range(2), repeat=2))
        for a, b, aa, bb, u in itertools.product(maps, repeat=5):
            self.assertEqual(comp(bb, comp(comp(b, comp(u,a)), aa)),
                             comp(comp(bb,b),comp(u,comp(a,aa))))
        for u in maps:
            self.assertEqual(comp((0,1),comp(u,(0,1))),u)

    def test_CAT_03_002_power_set_variance(self):
        for f,g in itertools.product(itertools.product(range(3),repeat=3),repeat=2):
            gf=comp(g,f)
            for mask in range(8):
                s={i for i in range(3) if mask>>i&1}
                self.assertEqual({i for i in range(3) if gf[i] in s},
                                 {i for i in range(3) if f[i] in {j for j in range(3) if g[j] in s}})
                self.assertEqual({gf[i] for i in s},{g[j] for j in {f[i] for i in s}})

    def test_CAT_03_003_tensor_counterexample(self):
        # Z tensor Z/2 identified with Z/2 by 1 tensor y -> y.
        self.assertEqual({2*y%2 for y in range(2)},{0})
        self.assertNotEqual(0,1)
        for x,y in itertools.product(range(2),repeat=2):
            self.assertEqual((2*x*y)%2,0)

    def test_CAT_03_004_spec_contraction(self):
        # Coordinate projections between products of F2.
        # Prime ideals are kernels of the coordinate projections.
        for n,m,k in itertools.product(range(1,4),repeat=3):
            elems=list(itertools.product(range(2),repeat=n))
            for f,g in itertools.product(itertools.product(range(n),repeat=m),
                                         itertools.product(range(m),repeat=k)):
                for j in range(k):
                    contraction={x for x in elems if x[f[g[j]]]==0}
                    self.assertEqual(contraction,{x for x in elems if x[comp(f,g)[j]]==0})
                    for r in elems:
                        self.assertEqual(int(r not in contraction),r[f[g[j]]])

    def test_CAT_03_005_homology_quotient(self):
        # Complex F2^2 -> F2^2 -> F2 with d2 image span(e1), d1=0.
        # Chain maps at degree 1 preserving the boundary subspace.
        xs=list(itertools.product(range(2),repeat=2))
        mats=[a for a in itertools.product(range(2),repeat=4) if a[2]==0]
        def act(a,x):
            return ((a[0]*x[0]+a[1]*x[1])%2,(a[2]*x[0]+a[3]*x[1])%2)
        for f,g,x in itertools.product(mats,mats,xs):
            self.assertEqual(act(g,act(f,x))[1],g[3]*f[3]*x[1]%2)
            self.assertEqual(act(f,x)[1],act(f,(1-x[0],x[1]))[1])

    def test_CAT_03_006_source_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for label in ("sec:funktory","def:funktor","def:pelny","def:hom-funktory",
                      "tw:funktory-iso","tw:ff-reflect-iso","przyklad:dzialanie-funktor",
                      "przyklad:dualny","cat:prop:hom-bifunctor","cat:ex:spec-functor",
                      "cat:ex:homology-functor","cat:ex:derham-functor"):
            self.assertIn(label,labels)
        stack=[]
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
