"""CAT-22 finite regression checks; not a substitute for categorical proofs."""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/22-kategorie-addytywne-i-abelowe.tex"


def exact_at(source, middle, f, g, zero):
    return {f(x) for x in source} == {y for y in middle if g(y) == zero}


class CategoryTheoryCh22(unittest.TestCase):
    def test_CAT_22_001_snake_cyclic_extensions(self):
        # 0 -> Z/m -> Z/(mn) -> Z/n -> 0, with scalar t vertically.
        nonzero_connecting = 0
        for m, n, t in itertools.product(range(1, 8), range(1, 8), range(13)):
            ka = [x for x in range(m) if t*x % m == 0]
            kb = [x for x in range(m*n) if t*x % (m*n) == 0]
            kc = [x for x in range(n) if t*x % n == 0]
            da, db, dc = (math.gcd(t, d) for d in (m, m*n, n))
            qa, qb, qc = range(da), range(db), range(dc)
            I = lambda x: n*x
            P = lambda x: x % n
            delta = lambda x: (t*x // n) % da
            J = lambda x: (n*x) % db
            H = lambda x: x % dc
            self.assertEqual(len({I(x) for x in ka}), len(ka))
            self.assertTrue(all(I(x) in kb for x in ka))
            self.assertTrue(all(P(x) in kc for x in kb))
            self.assertTrue(exact_at(ka, kb, I, P, 0))
            self.assertTrue(exact_at(kb, kc, P, delta, 0))
            self.assertTrue(exact_at(kc, qa, delta, J, 0))
            self.assertTrue(exact_at(qa, qb, J, H, 0))
            self.assertEqual({H(x) for x in qb}, set(qc))
            for x in kc:
                # All lifts of x to the middle group yield the same class.
                self.assertEqual({(t*(x+n*j)//n) % da for j in range(m)},
                                 {delta(x)})
                for s in range(n):
                    self.assertEqual(delta((s*x) % n), s*delta(x) % da)
                for y in kc:
                    self.assertEqual(delta((x+y) % n), (delta(x)+delta(y)) % da)
                nonzero_connecting += int(delta(x) != 0)
        self.assertGreater(nonzero_connecting, 0)

    def test_CAT_22_002_nine_lemma_middle_complex(self):
        # Split exact columns over F_2. Outer rows use canonical inclusions
        # and projections, with every dimension of A and C equal to 0 or 1.
        def vecs(d):
            return list(itertools.product(range(2), repeat=d))

        def matvec(matrix, x):
            return tuple(sum(a*b for a, b in zip(row, x)) % 2 for row in matrix)

        def matrices(rows, cols):
            for flat in itertools.product(range(2), repeat=rows*cols):
                yield tuple(flat[i*cols:(i+1)*cols] for i in range(rows))

        def plus(x, y):
            return tuple((a+b) % 2 for a, b in zip(x, y))

        noncomplex = 0
        for a1, c1, a3, c3 in itertools.product(range(2), repeat=4):
            b1, b3 = a1+c1, a3+c3
            A, B, C = vecs(a1+a3), vecs(b1+b3), vecs(c1+c3)
            for U, V in itertools.product(matrices(b1, a3), matrices(c1, b3)):
                def u(x):
                    top = plus(x[:a1]+(0,)*c1, matvec(U, x[a1:]))
                    return top+x[a1:]+(0,)*c3

                def v(y):
                    top = plus(y[a1:b1], matvec(V, y[b1:]))
                    return top+y[b1+a3:]

                self.assertEqual(len({u(x) for x in A}), len(A))
                self.assertEqual({v(y) for y in B}, set(C))
                zero = (0,)*(c1+c3)
                is_complex = all(v(u(x)) == zero for x in A)
                self.assertEqual(exact_at(A, B, u, v, zero), is_complex)
                noncomplex += int(not is_complex)
        self.assertGreater(noncomplex, 0)

    def test_CAT_22_003_pullback_epimorphism(self):
        # Homomorphisms between finite cyclic groups and their fibre products.
        for e, b, x in itertools.product(range(1, 7), repeat=3):
            for a, d in itertools.product(range(b), repeat=2):
                if a*e % b or d*x % b:
                    continue
                if {a*y % b for y in range(e)} != set(range(b)):
                    continue
                pullback = [(y, z) for y in range(e) for z in range(x)
                            if (a*y-d*z) % b == 0]
                self.assertEqual({z for _, z in pullback}, set(range(x)))

    def test_CAT_22_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        self.assertEqual(len(labels), len(set(labels)))
        all_labels = []
        for path in CHAPTER.parent.glob("*.tex"):
            all_labels += re.findall(r"\\label\{([^}]+)\}", path.read_text(encoding="utf-8"))
        for label in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s):
            self.assertEqual(all_labels.count(label), 1, label)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for label in ("cat:thm:snake-lemma", "cat:eq:snake-connecting",
                      "cat:thm:nine-lemma", "cat:rem:nine-lemma-complex",
                      "cat:thm:adjoint-exactness"):
            self.assertIn(label, labels)
        self.assertIn(r"$v_2u_2=0$", s)
        book = (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8")
        self.assertIn(CHAPTER.name, book)
        targets = {
            "AA-16": "abstract_algebra/16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex",
            "AA-18": "abstract_algebra/18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex",
            "TOP-03": "algebraic_topology/03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex",
        }
        for code, label in re.findall(r"\\atlasref\{([^:}]+)::([^}]+)\}", s):
            target = (ROOT / "chapters/pl" / targets[code]).read_text(encoding="utf-8")
            self.assertEqual(target.count(r"\label{" + label + "}"), 1, label)
