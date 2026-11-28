"""CAT-21 finite checks of monoids, duality and trace."""
import itertools
import re
import unittest
from pathlib import Path
CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/21-monoidy-komonoidy-i-dualnosc.tex"
class CategoryTheoryCh21(unittest.TestCase):
    def test_CAT_21_001_monoid_actions(self):
        count=0
        for op in itertools.product(range(2),repeat=4):
            m=lambda a,b:op[2*a+b]
            for e in range(2):
                if not all(m(e,a)==a==m(a,e) for a in range(2)):
                    continue
                if not all(m(m(a,b),c)==m(a,m(b,c)) for a,b,c in itertools.product(range(2),repeat=3)):
                    continue
                for table in itertools.product(range(2),repeat=4):
                    act=lambda a,x:table[2*a+x]
                    module=all(act(e,x)==x for x in range(2)) and all(act(m(a,b),x)==act(a,act(b,x)) for a,b,x in itertools.product(range(2),repeat=3))
                    eta=lambda x:(e,x)
                    mu=lambda a,b,x:(m(a,b),x)
                    algebra=all(act(*eta(x))==x for x in range(2)) and all(act(*mu(a,b,x))==act(a,act(b,x)) for a,b,x in itertools.product(range(2),repeat=3))
                    self.assertEqual(module,algebra)
                    count+=1
        self.assertGreater(count,0)
    def test_CAT_21_002_cartesian_comonoids(self):
        for n in range(5):
            pairs=list(itertools.product(range(n),repeat=2))
            good=[d for d in itertools.product(pairs,repeat=n)
                  if all(d[x]==(x,x) for x in range(n))]
            self.assertEqual(good,[tuple((x,x) for x in range(n))])
    def test_CAT_21_003_snakes_trace(self):
        for p in (2,3,5):
            for n in range(4):
                basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
                for v in itertools.product(range(p),repeat=n):
                    self.assertEqual(tuple(sum(v[j]*basis[j][i] for j in range(n))%p for i in range(n)),v)
                matrices=itertools.product(range(p),repeat=4) if n==2 else [tuple(int(i==j) for i in range(n) for j in range(n))]
                for f in matrices:
                    self.assertEqual(sum(f[j*n+j] for j in range(n))%p,
                        sum(sum(basis[j][i]*f[i*n+j] for i in range(n)) for j in range(n))%p)
    def test_CAT_21_004_tensor_duality_order(self):
        for n,m in itertools.product(range(4),repeat=2):
            for a,b,c,d in itertools.product(range(n),range(m),range(m),range(n)):
                self.assertEqual(int(a==d)*int(b==c),int((a,b)==(d,c)))
    def test_CAT_21_005_structure(self):
        s=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels+=re.findall(r"\\label\{([^}]+)\}",p.read_text(encoding="utf-8"))
        for label in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",s):
            self.assertEqual(all_labels.count(label),1)
        stack=[]
        for cmd,env in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd=="begin": stack.append(env)
            else: self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)

    def test_CAT_21_006_dual_functoriality(self):
        # A map k^n -> k^m is represented by an m-by-n matrix.
        def transpose(a, m, n):
            return tuple(a[i*n+j] for j in range(n) for i in range(m))

        def compose(g, f, l, m, n, p):
            return tuple(sum(g[i*m+k]*f[k*n+j] for k in range(m)) % p
                         for i in range(l) for j in range(n))

        for p, n, m, l in ((2, 1, 2, 3), (3, 2, 1, 2),
                            (2, 0, 2, 1), (2, 2, 0, 2)):
            for f in itertools.product(range(p), repeat=m*n):
                ft = transpose(f, m, n)
                for g in itertools.product(range(p), repeat=l*m):
                    gt = transpose(g, l, m)
                    self.assertEqual(transpose(compose(g, f, l, m, n, p), l, n),
                                     compose(ft, gt, n, m, l, p))
                for v in itertools.product(range(p), repeat=n):
                    for phi in itertools.product(range(p), repeat=m):
                        fv = compose(f, v, m, n, 1, p)
                        ftphi = compose(ft, phi, n, m, 1, p)
                        self.assertEqual(sum(a*b for a, b in zip(phi, fv)) % p,
                                         sum(a*b for a, b in zip(ftphi, v)) % p)
            for d in (n, m, l):
                identity = tuple(int(i == j) for i in range(d) for j in range(d))
                self.assertEqual(transpose(identity, d, d), identity)

    def test_CAT_21_007_rectangular_trace(self):
        for p, m, n in ((2, 2, 3), (3, 1, 2), (2, 0, 3), (2, 3, 0)):
            for f in itertools.product(range(p), repeat=m*n):
                for g in itertools.product(range(p), repeat=n*m):
                    gf = tuple(sum(g[i*m+k]*f[k*n+j] for k in range(m)) % p
                               for i in range(n) for j in range(n))
                    fg = tuple(sum(f[i*n+k]*g[k*m+j] for k in range(n)) % p
                               for i in range(m) for j in range(m))
                    self.assertEqual(sum(gf[i*n+i] for i in range(n)) % p,
                                     sum(fg[i*m+i] for i in range(m)) % p)

    def test_CAT_21_008_cross_book_reference(self):
        root = CHAPTER.parents[3]
        source = CHAPTER.read_text(encoding="utf-8")
        target = (root / "chapters/pl/differential_geometry_and_topology/"
                  "03-algebra-tensorowa-i-zewnetrzna.tex").read_text(encoding="utf-8")
        book = (root / "books/pl/category_theory.tex").read_text(encoding="utf-8")
        self.assertIn(r"\atlasref{DG-03::prop:kontrakcja-slad}", source)
        self.assertEqual(target.count(r"\label{prop:kontrakcja-slad}"), 1)
        self.assertIn(r"\providecommand{\atlasref}[2]{#2}", book)
        for label in ("cat:prop:dual-functoriality", "cat:eq:dual-morphism-eval",
                      "cat:eq:dual-morphism-coeval", "cat:prop:trace-cyclic"):
            self.assertEqual(source.count(r"\label{" + label + "}"), 1)
