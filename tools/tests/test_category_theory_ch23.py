"""Finite regression models for CAT-23, complementing categorical proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/23-obiekty-rzutowe-injektywne-i-rezolucje.tex"


class CategoryTheoryCh23(unittest.TestCase):
    def test_CAT_23_001_comparison_cyclic_resolutions(self):
        # Z --m--> Z and Z --n--> Z; u([x])=[k*x].
        for m, n in itertools.product(range(2, 13), repeat=2):
            for k in range(n):
                if m*k % n:
                    continue
                for s, t in itertools.product(range(-2, 3), repeat=2):
                    f0, g0 = k+n*s, k+n*t
                    f1, g1 = m*f0//n, m*g0//n
                    h0 = s-t
                    self.assertEqual(n*f1, f0*m)
                    self.assertEqual(n*g1, g0*m)
                    self.assertEqual(f0-g0, n*h0)
                    self.assertEqual(f1-g1, h0*m)

    def test_CAT_23_002_horseshoe_cyclic_extension(self):
        # 0 -> Z/m -> Z/(mn) -> Z/n -> 0.
        # Middle differential D(x,y)=(m*x-y,n*y),
        # augmentation epsilon(x,y)=[n*x+y].
        for m, n in itertools.product(range(2, 10), repeat=2):
            self.assertEqual({(n*x+y) % (m*n)
                              for x in range(m) for y in range(n)},
                             set(range(m*n)))
            self.assertEqual((n*m) % (m*n), 0)
            self.assertEqual((-n+n) % (m*n), 0)
            for x, y in itertools.product(range(-12, 13), repeat=2):
                if (n*x+y) % (m*n) == 0:
                    self.assertEqual(y % n, 0)
                    v = y//n
                    self.assertEqual((x+v) % m, 0)
                    u = (x+v)//m
                    self.assertEqual((m*u-v, n*v), (x,y))
                D = (m*x-y, n*y)
                self.assertEqual((n*D[0]+D[1]) % (m*n), 0)
                self.assertEqual(D == (0,0), (x,y) == (0,0))
                self.assertEqual((m*x,0), (m*x-0,n*0))
                self.assertEqual(D[1], n*y)

    def test_CAT_23_003_schanuel_split_fibre_product(self):
        # Over F_2 use coordinate projections F_2^p,F_2^q -> F_2^x.
        def vectors(d):
            return list(itertools.product(range(2), repeat=d))

        for x, a, b in itertools.product(range(3), repeat=3):
            P, Q = vectors(x+a), vectors(x+b)
            D = [(p,q) for p in P for q in Q if p[:x] == q[:x]]
            left = {(p[x:],q) for p,q in D}
            right = {(q[x:],p) for p,q in D}
            self.assertEqual(left, set(itertools.product(vectors(a),Q)))
            self.assertEqual(right, set(itertools.product(vectors(b),P)))
            self.assertEqual(len(D), len(left))
            self.assertEqual(len(D), len(right))

    def test_CAT_23_004_coinduction_noncommutative(self):
        # R=M_2(F_2), D=F_2 as an additive group, M=F_2^2.
        # The adjunction bijection itself does not require D injective.
        def bits(n):
            return list(itertools.product(range(2), repeat=n))

        def mul(r,s):
            return tuple(sum(r[2*i+k]*s[2*k+j] for k in range(2)) % 2
                         for i in range(2) for j in range(2))

        def act(r,m):
            return tuple(sum(r[2*i+k]*m[k] for k in range(2)) % 2
                         for i in range(2))

        def dot(a,b):
            return sum(x*y for x,y in zip(a,b)) % 2

        one=(1,0,0,1)
        for r,s,m,chi in itertools.product(bits(4),bits(4),bits(2),bits(2)):
            self.assertEqual(dot(chi,act(s,act(r,m))),
                             dot(chi,act(mul(s,r),m)))
            self.assertEqual(dot(chi,act(one,m)),dot(chi,m))
        # Check left action on the coinduced module for all linear forms.
        for r,t,s in itertools.product(bits(4), repeat=3):
            self.assertEqual(mul(mul(s,r),t),mul(s,mul(r,t)))

    def test_CAT_23_005_structure(self):
        c = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", c)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = []
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}", p.read_text(encoding="utf-8")))
        for label in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", c):
            self.assertEqual(all_labels.count(label),1,label)
        stack=[]
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}",c):
            if cmd=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        for label in ("cat:thm:resolution-comparison","cat:thm:schanuel",
                      "cat:thm:baer","cat:thm:enough-injectives-mod",
                      "cat:thm:horseshoe","cat:prop:syzygy-dimension"):
            self.assertIn(label,labels)
        targets={
            "AA-16":"abstract_algebra/16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex",
            "TOP-03":"algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex",
        }
        for code,label in re.findall(r"\\atlasref\{([^:}]+)::([^}]+)\}",c):
            t=(ROOT/"chapters/pl"/targets[code]).read_text(encoding="utf-8")
            self.assertEqual(t.count(r"\label{"+label+"}"),1,label)
        self.assertIn(CHAPTER.name,(ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))
