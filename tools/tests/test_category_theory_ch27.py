"""CAT-27: finite models of ends/coends; not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/27-konce-i-kokonce.tex"


class CategoryTheoryCh27(unittest.TestCase):
    def test_CAT_27_001_end_natural_transformations(self):
        # A = 0 -> 1. Functors to Set are single functions.
        for a,b,c,d in itertools.product(range(3), repeat=4):
            for F in itertools.product(range(b), repeat=a):
                for G in itertools.product(range(d), repeat=c):
                    pairs = list(itertools.product(
                        itertools.product(range(c), repeat=a),
                        itertools.product(range(d), repeat=b)))
                    end = [(u,v) for u,v in pairs
                           if tuple(G[u[x]] for x in range(a)) ==
                              tuple(v[F[x]] for x in range(a))]
                    # Count natural transformations independently via fibers:
                    # for fixed v, choices for each u(x) lie in a fiber of G.
                    count = 0
                    for v in itertools.product(range(d),repeat=b):
                        prod = 1
                        for x in range(a):
                            prod *= sum(y == v[F[x]] for y in G)
                        count += prod
                    self.assertEqual(len(end), count)

    def test_CAT_27_002_coend_separable_bifunctor(self):
        # A = 0 -> 1, T(a,b)=P(a) x F(b) for a presheaf P
        # and a covariant set-valued functor F.
        for p0,p1,f0,f1 in itertools.product(range(3),repeat=4):
            for P in itertools.product(range(p0),repeat=p1):
                for F in itertools.product(range(f1),repeat=f0):
                    Z = ([(0,x,y) for x in range(p0) for y in range(f0)]
                         + [(1,x,y) for x in range(p1) for y in range(f1)])
                    parent = {z:z for z in Z}
                    def root(z):
                        while parent[z] != z:
                            z = parent[z]
                        return z
                    for x,y in itertools.product(range(p1),range(f0)):
                        parent[root((0,P[x],y))] = root((1,x,F[y]))
                    relations = [((0,P[x],y),(1,x,F[y]))
                                 for x,y in itertools.product(range(p1),range(f0))]
                    # Every compatible map from the diagonal factors uniquely
                    # through the quotient, checked for two-element targets.
                    roots = sorted({root(z) for z in Z})
                    compatible = {v for v in itertools.product(range(2),repeat=len(Z))
                                  if all(v[Z.index(z)]==v[Z.index(w)]
                                         for z,w in relations)}
                    induced = {tuple(v[roots.index(root(z))] for z in Z)
                               for v in itertools.product(range(2),repeat=len(roots))}
                    self.assertEqual(compatible,induced)

    def test_CAT_27_003_dinatural_noncomposition(self):
        # S constant singleton, T has empty (1,0), other entries singleton.
        # U has empty (1,0) and two distinct maps from diagonal to (0,1).
        def compose(g,f):
            return tuple(g[x] for x in f)
        def dinatural(S,T,alpha):
            left=compose(T[0],compose(alpha[0],S[2]))
            right=compose(T[1],compose(alpha[1],S[3]))
            return left==right
        # Entries: (diagonal -> upper) twice, (lower -> diagonal) twice.
        S=((0,),(0,),(0,),(0,))
        T=((0,),(0,),(),())
        U=((0,),(1,),(),())
        alpha=((0,),(0,))
        beta=((0,),(0,))
        self.assertTrue(dinatural(S,T,alpha))
        self.assertTrue(dinatural(T,U,beta))
        self.assertFalse(dinatural(S,U,tuple(compose(b,a)
                                            for a,b in zip(alpha,beta))))

    def test_CAT_27_004_structure(self):
        source = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",source)
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


if __name__ == "__main__":
    unittest.main()
