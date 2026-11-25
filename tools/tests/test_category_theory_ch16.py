"""CAT-16 finite checks of cross-domain constructions."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/16-powiazania-z-innymi-dzialami-matematyki.tex"


def vectors(n, p):
    return list(itertools.product(range(p), repeat=n))


class CategoryTheoryCh16(unittest.TestCase):
    def test_CAT_16_001_exactness(self):
        for p in (2, 3):
            for n, m in itertools.product(range(3), repeat=2):
                for a in itertools.product(range(p), repeat=n*m):
                    def f(x):
                        return tuple(sum(a[i*n+j]*x[j] for j in range(n)) % p
                                     for i in range(m))
                    domain, codomain = vectors(n, p), vectors(m, p)
                    ker = {x for x in domain if f(x) == (0,)*m}
                    image = {f(x) for x in domain}
                    def coset(y):
                        return frozenset(tuple((u+v)%p for u,v in zip(y,z)) for z in image)
                    self.assertEqual({y for y in codomain if coset(y) == coset((0,)*m)}, image)
                    self.assertEqual(len(ker)*len(image), len(domain))
                    self.assertEqual(len({coset(y) for y in codomain})*len(image), len(codomain))

    def test_CAT_16_002_chain_naturality(self):
        # Finite model of the alternating face formula, including repeats.
        for f in itertools.product(range(3), repeat=3):
            for n in range(1, 5):
                for s in itertools.product(range(3), repeat=n+1):
                    left, right = {}, {}
                    image = tuple(f[i] for i in s)
                    for i in range(n+1):
                        a = image[:i] + image[i+1:]
                        b = tuple(f[j] for j in s[:i] + s[i+1:])
                        left[a] = left.get(a, 0) + (-1)**i
                        right[b] = right.get(b, 0) + (-1)**i
                    self.assertEqual(left, right)

    def test_CAT_16_003_gluing(self):
        # All covers of a 3-point discrete space by distinct subsets.
        subsets = [tuple(i for i in range(3) if mask >> i & 1) for mask in range(8)]
        for mask in range(256):
            cover = [u for i,u in enumerate(subsets) if mask >> i & 1]
            if set().union(*map(set, cover)) != set(range(3)):
                continue
            assignments = [list(itertools.product(range(2), repeat=len(u))) for u in cover]
            for local in itertools.product(*assignments):
                glue = {}
                consistent = True
                for u, vals in zip(cover, local):
                    for i, v in zip(u, vals):
                        if i in glue and glue[i] != v:
                            consistent = False
                        glue[i] = v
                matches = [f for f in itertools.product(range(2), repeat=3)
                           if all(tuple(f[i] for i in u) == vals
                                  for u, vals in zip(cover, local))]
                self.assertEqual(len(matches), int(consistent))

    def test_CAT_16_005_biproduct(self):
        # All linear maps into/out of a two-dimensional biproduct of lines.
        for p in (2, 3, 5):
            for u, v, r, s in itertools.product(range(p), repeat=4):
                for x in range(p):
                    pair = (u*x % p, v*x % p)
                    self.assertEqual(pair[0], u*x % p)
                    self.assertEqual(pair[1], v*x % p)
                    self.assertEqual((r*pair[0]+s*pair[1]) % p,
                                     ((r*u+s*v)*x) % p)
                for a, b in itertools.product(range(p), repeat=2):
                    left = (a, 0)
                    right = (0, b)
                    self.assertEqual(tuple((x+y) % p for x,y in zip(left,right)),
                                     (a,b))
                    self.assertEqual((r*a+s*b) % p,
                                     ((r*a) % p + (s*b) % p) % p)

    def test_CAT_16_006_qualified_cross_references(self):
        import json
        root = CHAPTER.parents[3]
        catalog = json.loads((root / "catalog/books.json").read_text(encoding="utf-8"))
        paths = {p for book in catalog["books"] for p in book["chapters"]}
        targets = [["TOP-03","def:ciag-dokladny","chapters/pl/algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex"],["TOP-05","prop:funktor-singularny","chapters/pl/algebraic_topology/05-homologia-przestrzeni.tex"],["FA-02","thm:quotient-norm","chapters/pl/functional_analysis/02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex"],["FA-02","thm:quotient-universal","chapters/pl/functional_analysis/02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex"],["ALG-04","def:snop","chapters/pl/algebraic_geometry/04-algebra-przemienna-snopy-i-krzywe-algebraiczne.tex"]]
        source = CHAPTER.read_text(encoding="utf-8")
        self.assertIn(r"\providecommand{\atlasref}[2]{#2}", source)
        actual = set(re.findall(r"\\atlasref\{([^}]+::[^}]+)\}", source))
        self.assertEqual(actual, {f"{doc}::{label}" for doc, label, _ in targets})
        for doc, label, path in targets:
            self.assertIn(path, paths)
            content = (root / path).read_text(encoding="utf-8")
            self.assertEqual(re.findall(r"\\label\{([^}]+)\}", content).count(label), 1)

    def test_CAT_16_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        for name in ("sec:powiazania", "cat:def:abelian-category",
                     "cat:prop:abelian-examples", "cat:ex:exact-sequence",
                     "cat:ex:normed-quotient", "cat:ex:continuous-sheaf",
                     "cat:ex:normed-nonabelian"):
            self.assertIn(name, labels)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
