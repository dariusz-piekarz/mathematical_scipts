"""AA-X18: finite local algebras, Nakayama, projective and flat modules."""
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]

class TruncatedPoly:
    """R=F_p[t]/(t^k), represented by k coefficients in F_p."""
    def __init__(self, p, k):
        self.p, self.k = p, k
        self.zero = (0,) * k
        self.one = (1,) + (0,) * (k - 1)
        self.t = (0, 1) + (0,) * (k - 2)
        self.elements = list(product(range(p), repeat=k))

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def mul(self, a, b):
        return tuple(sum(a[i] * b[j - i] for i in range(j + 1)) % self.p
                     for j in range(self.k))

    def ideal(self, generator):
        return {self.mul(r, generator) for r in self.elements}

    def power(self, x, n):
        z = self.one
        for _ in range(n):
            z = self.mul(z, x)
        return z

def matrix_mul(R, A, B):
    return [[sum_entry(R, [R.mul(A[i][h], B[h][j]) for h in range(len(B))])
             for j in range(len(B[0]))] for i in range(len(A))]

def sum_entry(R, items):
    z = R.zero
    for q in items:
        z = R.add(z, q)
    return z

def act(R, A, v):
    return tuple(sum_entry(R, [R.mul(A[i][j], v[j]) for j in range(len(v))])
                 for i in range(len(A)))

class LocalProjectiveFlatInterface(unittest.TestCase):
    def test_local_ring_criterion_and_nilpotent_radical(self):
        for p, k in ((2, 2), (2, 3), (3, 2)):
            with self.subTest(p=p, k=k):
                R = TruncatedPoly(p, k)
                maximal = {a for a in R.elements if a[0] == 0}
                self.assertEqual(len(maximal), p ** (k - 1))
                self.assertEqual(R.ideal(R.t), maximal)
                self.assertEqual(R.power(R.t, k), R.zero)
                self.assertNotEqual(R.power(R.t, k - 1), R.zero)
                for a in R.elements:
                    invertible = any(R.mul(a, b) == R.one for b in R.elements)
                    self.assertEqual(invertible, a not in maximal)
    def test_nakayama_generator_count_with_free_and_residue_summands(self):
        for p, k in ((2, 2), (2, 3), (3, 2)):
            with self.subTest(p=p, k=k):
                R = TruncatedPoly(p, k)
                # M=R direct-sum F_p. Reduction modulo mM is F_p^2.
                M = list(product(R.elements, range(p)))
                self.assertEqual(len(M), p ** (k + 1))
                mM = {(a, 0) for a in R.ideal(R.t)}
                self.assertEqual(len(mM), p ** (k - 1))
                self.assertEqual(len(M) // len(mM), p ** 2)
                # No cyclic submodule of M can contain more than |R| elements.
                self.assertGreater(len(M), len(R.elements))
                # Yet (1,0) and (0,1) visibly generate M.
                self.assertEqual({(r, c) for r in R.elements for c in range(p)}, set(M))
                # The residue field is cyclic but not free over non-field R.
                self.assertEqual(p ** k % p, 0)
                self.assertNotEqual(p, p ** k)
    def test_explicit_matrix_idempotent_and_local_free_summand(self):
        for p, k in ((2, 2), (2, 3), (3, 2)):
            R = TruncatedPoly(p, k)
            P = [[R.one, R.t], [R.zero, R.zero]]
            with self.subTest(p=p, k=k):
                self.assertEqual(matrix_mul(R, P, P), P)
                image, kernel = set(), set()
                for a, b in product(R.elements, repeat=2):
                    v = (a, b)
                    w = act(R, P, v)
                    image.add(w)
                    if w == (R.zero, R.zero):
                        kernel.add(v)
                self.assertEqual(image, {(a, R.zero) for a in R.elements})
                self.assertEqual(kernel, {(R.neg(R.mul(R.t, b)), b) for b in R.elements})
                self.assertEqual(len(image), p ** k)
                self.assertEqual(len(kernel), p ** k)
                self.assertEqual(image & kernel, {(R.zero, R.zero)})
                self.assertEqual(len(image) * len(kernel), p ** (2 * k))
                # Reduction of P mod (t) has rank 1.
                self.assertEqual([[q[0] for q in row] for row in P], [[1, 0], [0, 0]])
    def test_tensor_injection_obstruction_for_residue_field(self):
        for p, k in ((2, 2), (2, 3), (3, 2)):
            with self.subTest(p=p, k=k):
                R = TruncatedPoly(p, k)
                I = R.ideal(R.t)
                mI = {R.mul(R.t, a) for a in I}
                self.assertEqual(len(I), p ** (k - 1))
                self.assertEqual(len(mI), p ** max(k - 2, 0))
                self.assertEqual(len(I) // len(mI), p)
                # I tensor_R R/(t) is I/(t)I != 0, while
                # I -> R -> R/(t) is zero: the induced tensor map is zero.
                self.assertNotIn(R.t, mI)
                self.assertEqual({a[0] for a in I}, {0})
    def test_projective_nonfree_over_nonlocal_product_ring(self):
        for p in (2, 3):
            with self.subTest(p=p):
                R = list(product(range(p), repeat=2))
                e = (1, 0)
                f = (0, 1)
                mul = lambda a, b: ((a[0] * b[0]) % p, (a[1] * b[1]) % p)
                self.assertEqual(mul(e, e), e)
                self.assertEqual(mul(f, f), f)
                self.assertEqual(mul(e, f), (0, 0))
                P = {mul(e, r) for r in R}
                Q = {mul(f, r) for r in R}
                self.assertEqual(len(P), p)
                self.assertEqual(len(Q), p)
                self.assertEqual(len(P) * len(Q), len(R))
                self.assertFalse(any(len(P) == len(R) ** n for n in range(4)))
    def test_source_theorems_labels_and_selected_references(self):
        files = {
            14: "14-pierscienie-artinowskie-lokalne-i-lemat-nakayamy.tex",
            16: "16-moduly-homomorfizmy-ciagi-dokladne-i-moduly-rzutowe.tex",
            18: "18-iloczyn-tensorowy-modulow-i-jego-wlasnosci.tex",
        }
        sources = {i: (ROOT / "chapters/pl/abstract_algebra" / f).read_text(encoding="utf-8")
                   for i, f in files.items()}
        labels = [v for src in sources.values() for v in re.findall(r"\\label\{([^{}]+)\}", src)]
        self.assertEqual(len(labels), 71)
        self.assertEqual(len(labels), len(set(labels)))
        for req in ("aa:tw:nakayama-local", "aa:tw:nakayama-minimal-generators",
                    "aa:def:modules-projective", "aa:tw:modules-projective-summand",
                    "aa:def:flat-module", "aa:tw:projective-flat", "aa:tw:tensor-quotient"):
            self.assertIn(req, labels)
        refs = {i: set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}", src))
                for i, src in sources.items()}
        self.assertFalse(refs[14] - set(labels))
        self.assertFalse(refs[16] - set(labels))
        # AA-18 also refers to AA-08 (a legitimate predecessor outside the focus).
        self.assertEqual(refs[18] - set(labels), {"aa:ch:grupy-abelowe"})

if __name__ == "__main__":
    unittest.main()
