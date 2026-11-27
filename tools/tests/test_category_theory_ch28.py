"""CAT-28: finite comonad and comparison models, not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/28-monady-komonady-i-twierdzenie-becka.tex"


class CategoryTheoryCh28(unittest.TestCase):
    def test_CAT_28_001_product_comonad_coalgebras(self):
        for e,n in itertools.product(range(3),repeat=2):
            pairs = list(itertools.product(range(e),range(n)))
            coalgebras = []
            for c in itertools.product(pairs,repeat=n):
                if all(c[x][1]==x and (c[x][0],c[x]) ==
                       (c[x][0],c[c[x][1]]) for x in range(n)):
                    coalgebras.append(c)
            self.assertEqual(set(coalgebras),
                             {tuple(zip(p,range(n)))
                              for p in itertools.product(range(e),repeat=n)})
            for c in coalgebras:
                for m in range(3):
                    # Cofree target (E x M, diagonal): transpose a map
                    # h:X->E x M to its second coordinate.
                    target = list(itertools.product(range(e),range(m)))
                    compatible = {h for h in itertools.product(target,repeat=n)
                                  if all(h[x][0]==c[x][0] for x in range(n))}
                    induced = {tuple((c[x][0],f[x]) for x in range(n))
                               for f in itertools.product(range(m),repeat=n)}
                    self.assertEqual(compatible,induced)

    def test_CAT_28_002_structure(self):
        source=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",source)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",
                                         p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",source):
            self.assertEqual(all_labels.count(ref),1,ref)
        stack=[]
        for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",source):
            if kind=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}",source):
            self.assertTrue(source[m.end():].lstrip().startswith(r"\begin{proof}"))
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(),
                      (ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))

    def test_CAT_28_003_split_coequalizer_universal_property(self):
        # Exhaustive finite diagrams with at most two elements per object.
        # Check factorization even for empty domains/codomains.
        count = 0
        for a,b,c in itertools.product(range(3), repeat=3):
            maps = lambda m,n: itertools.product(range(n), repeat=m)
            for f,g in itertools.product(maps(a,b), repeat=2):
                for p in maps(b,c):
                    if any(p[f[x]] != p[g[x]] for x in range(a)):
                        continue
                    for s in maps(c,b):
                        if any(p[s[x]] != x for x in range(c)):
                            continue
                        for t in maps(b,a):
                            if any(f[t[x]] != x or g[t[x]] != s[p[x]]
                                   for x in range(b)):
                                continue
                            count += 1
                            for z in range(3):
                                for h in maps(b,z):
                                    if any(h[f[x]] != h[g[x]] for x in range(a)):
                                        continue
                                    k = tuple(h[s[x]] for x in range(c))
                                    factors = [v for v in maps(c,z)
                                               if tuple(v[p[x]] for x in range(b)) == h]
                                    self.assertEqual(factors, [k])
        self.assertGreater(count, 0)

    def test_CAT_28_004_reflexive_not_split(self):
        # A connected reflexive relation whose edges have neither
        # a common target nor a common source.
        edges = ((0,0),(1,1),(2,2),(0,1),(1,2))
        f,g = tuple(zip(*edges))
        self.assertTrue(all((b,b) in edges for b in range(3)))
        equalizing = [h for h in itertools.product(range(3), repeat=3)
                      if all(h[x] == h[y] for x,y in edges)]
        self.assertEqual(equalizing, [(x,x,x) for x in range(3)])
        for first,second in ((f,g),(g,f)):
            splits = [(c,t) for c in range(3)
                      for t in itertools.product(range(len(edges)), repeat=3)
                      if all(first[t[b]] == b and second[t[b]] == c
                             for b in range(3))]
            self.assertEqual(splits, [])

    def test_CAT_28_005_group_coequalizer_not_preserved(self):
        # Finite analogue Z/4 -> Z/4, f(x)=2x and g(x)=0.
        # The set quotient has classes {0,2}, {1}, {3}; the group
        # quotient additionally identifies 1 and 3.
        set_classes = {frozenset({0,2}), frozenset({1}), frozenset({3})}
        group_classes = {frozenset({0,2}), frozenset({1,3})}
        for h in itertools.product(range(3), repeat=4):
            equalizes = all(h[(2*x)%4] == h[0] for x in range(4))
            constant_on_classes = all(len({h[x] for x in cls}) == 1
                                      for cls in set_classes)
            self.assertEqual(equalizes, constant_on_classes)
        self.assertNotEqual(set_classes, group_classes)
        self.assertEqual({frozenset((x+y)%4 for y in (0,2))
                          for x in range(4)}, group_classes)
