"""CAT-17: cross-category regression models."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/17-przyklady-przekrojowe-jedno-zadanie-wiele-kategorii.tex"


def subsets(xs):
    xs = tuple(xs)
    return [frozenset(x for i,x in enumerate(xs) if mask >> i & 1)
            for mask in range(1 << len(xs))]


def compose(g, f):
    return frozenset((x,z) for x,y in f for v,z in g if y == v)


class CategoryTheoryCh17(unittest.TestCase):
    def test_CAT_17_001_rel_product_coproduct(self):
        for a,b,z in itertools.product(range(3), repeat=3):
            A,B,Z = range(a),range(b),range(z)
            P = range(a+b)
            ia = frozenset((i,i) for i in A)
            ib = frozenset((i,a+i) for i in B)
            pa,pb = [frozenset((y,x) for x,y in r) for r in (ia,ib)]
            seen = set()
            for h in subsets(itertools.product(Z,P)):
                key = compose(pa,h),compose(pb,h)
                self.assertNotIn(key,seen)
                seen.add(key)
            expected = set(itertools.product(subsets(itertools.product(Z,A)),
                                             subsets(itertools.product(Z,B))))
            self.assertEqual(seen,expected)
            seen = set()
            for h in subsets(itertools.product(P,Z)):
                key = compose(h,ia),compose(h,ib)
                self.assertNotIn(key,seen)
                seen.add(key)
            expected = set(itertools.product(subsets(itertools.product(A,Z)),
                                             subsets(itertools.product(B,Z))))
            self.assertEqual(seen,expected)

    def test_CAT_17_002_commuting_images(self):
        # Maps C2 x C2 -> S3 with given involutions as images.
        S3 = tuple(itertools.permutations(range(3)))
        e = tuple(range(3))
        def mul(g,h):
            return tuple(g[i] for i in h)
        involutions = [g for g in S3 if mul(g,g) == e]
        D = tuple(itertools.product(range(2),repeat=2))
        for g,h in itertools.product(involutions,repeat=2):
            candidates = []
            for k in S3:
                f = dict(zip(D,(e,h,g,k)))
                if all(f[tuple(a^b for a,b in zip(x,y))] == mul(f[x],f[y])
                       for x,y in itertools.product(D,repeat=2)):
                    candidates.append(k)
            self.assertEqual(candidates,[mul(g,h)] if mul(g,h)==mul(h,g) else [])

    def test_CAT_17_003_natural_linear_operations(self):
        for p in (2,3,5):
            for a,b in itertools.product(range(p),repeat=2):
                for v,w in itertools.product(range(p),repeat=2):
                    for f in range(p):
                        self.assertEqual(f*(a*v+b*w)%p,(a*f*v+b*f*w)%p)
            self.assertEqual(len({(a,b) for a,b in itertools.product(range(p),repeat=2)}),p*p)

    def test_CAT_17_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        for name in ("sec:przekrojowe","cat:ex:cross-products","cat:ex:cross-coproducts",
                     "cat:ex:rel-biproduct","cat:ex:linear-natural-operations"):
            self.assertIn(name,labels)
        stack = []
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
