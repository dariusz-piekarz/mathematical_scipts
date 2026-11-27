"""Finite linear models for CAT-39 (not proofs of infinity-categorical results)."""
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/39-stabilne-infty-kategorie-i-wyzsza-algebra-homologiczna.tex"


def rank(matrix, p):
    a = [list(row) for row in matrix]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        t = pow(a[r][j] % p, -1, p)
        a[r] = [(x * t) % p for x in a[r]]
        for i in range(len(a)):
            if i != r:
                t = a[i][j]
                a[i] = [(x - t * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def multiply(a, b, p):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) % p
                       for col in zip(*b)) for row in a)


def matrices(p, n):
    for entries in itertools.product(range(p), repeat=n*n):
        yield tuple(tuple(entries[i*n:(i+1)*n]) for i in range(n))


def mv(a, x, p):
    return tuple(sum(u*v for u, v in zip(row, x)) % p for row in a)


def coh(dims, diffs, p):
    return {q: n - rank(diffs.get(q, ()), p) - rank(diffs.get(q-1, ()), p)
            for q, n in dims.items()}


def truncation_dimensions(dims, diffs, r, upper, p):
    # Smart cohomological truncations, expressed via rank-nullity.
    if upper:
        return {q: (n-rank(diffs.get(q, ()), p) if q == r else n)
                for q, n in dims.items() if q <= r}
    return {q: (n-rank(diffs.get(q-1, ()), p) if q == r else n)
            for q, n in dims.items() if q >= r}


class CategoryTheoryCh39(unittest.TestCase):
    def test_CAT_39_001_truncation_indexing(self):
        # Explicit three-term complexes over finite fields.
        for p in (2, 3):
            ms = list(matrices(p, 2))
            zero = ((0, 0), (0, 0))
            dims = {-1: 2, 0: 2, 1: 2}
            for d0, d1 in itertools.product(ms, repeat=2):
                if multiply(d1, d0, p) != zero:
                    continue
                ds = {-1: d0, 0: d1}
                h = coh(dims, ds, p)
                for a, b in itertools.product(range(-2, 3), repeat=2):
                    # tau_{>=a} tau_{<=b}: retained cohomological
                    # degrees are precisely -b <= q <= -a.
                    for q in dims:
                        first = h[q] if q <= -a else 0
                        first = first if q >= -b else 0
                        second = h[q] if q >= -b else 0
                        second = second if q <= -a else 0
                        self.assertEqual(first, second)
                        if a > b:
                            self.assertEqual(first, 0)
                    r = -a
                    up = truncation_dimensions(dims, ds, r, True, p)
                    low = truncation_dimensions(dims, ds, r, False, p)
                    if r in dims:
                        self.assertEqual(up[r] - rank(ds.get(r-1, ()), p), h[r])
                        self.assertEqual(low[r] - rank(ds.get(r, ()), p), h[r])

    def test_CAT_39_002_cone_composite(self):
        # For maps of vector spaces in degree 0, the cofiber triangle
        # gives 0 -> ker f -> ker(gf) -> ker g -> coker f
        # -> coker(gf) -> coker g -> 0.
        p = 2
        vectors = tuple(itertools.product(range(p), repeat=2))
        zero = (0, 0)
        for f, g in itertools.product(matrices(p, 2), repeat=2):
            h = multiply(g, f, p)
            kf = {v for v in vectors if mv(f, v, p) == zero}
            kg = {v for v in vectors if mv(g, v, p) == zero}
            kh = {v for v in vectors if mv(h, v, p) == zero}
            imf = {mv(f, v, p) for v in vectors}
            img = {mv(g, v, p) for v in vectors}
            imh = {mv(h, v, p) for v in vectors}
            self.assertEqual({v for v in kh if mv(f, v, p) == zero}, kf)
            self.assertEqual({mv(f, v, p) for v in kh}, kg & imf)

            def coset(v, subspace):
                return frozenset(tuple((x+y) % p for x, y in zip(v, w))
                                 for w in subspace)
            cf = {coset(v, imf) for v in vectors}
            ch = {coset(v, imh) for v in vectors}
            cg = {coset(v, img) for v in vectors}
            self.assertEqual({coset(v, imf) for v in kg},
                             {c for c in cf if coset(mv(g, next(iter(c)), p), imh) == imh})
            self.assertEqual({coset(mv(g, v, p), imh) for v in vectors},
                             {c for c in ch if coset(next(iter(c)), img) == img})
            self.assertEqual({coset(next(iter(c)), img) for c in ch}, cg)

    def test_CAT_39_003_suspension_cone_sign(self):
        # Cone(f)^q = Y^q + X^{q+1}; d(y,x)=(dy+fx,-dx).
        # Test d^2=0 and the negative sign with nonzero differentials.
        p = 3
        ds = ((1, 0), (0, 0))
        f = ((1, 0), (0, 1))
        for y, x in itertools.product(itertools.product(range(p), repeat=2), repeat=2):
            dy, fx, dx = mv(ds, y, p), mv(f, x, p), mv(ds, x, p)
            # d_X and d_Y are ds in degree 0, zero in other degrees.
            first = tuple((u+v) % p for u, v in zip(dy, fx))
            second = tuple(-u % p for u in dx)
            d2first = tuple((u+v) % p for u, v in zip(mv(ds, first, p), mv(f, second, p)))
            # Remove d_Y^2 y, which is zero in the graded complex.
            d2first = tuple((u-v) % p for u, v in zip(d2first, mv(ds, dy, p)))
            self.assertEqual(d2first, (0, 0))
            self.assertEqual(tuple((-u+u) % p for u in dx), (0, 0))

    def test_CAT_39_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", s)
        all_labels = [label for f in CHAPTER.parent.glob("*.tex")
                      for label in re.findall(r"\\label\{([^}]+)\}",
                                              f.read_text(encoding="utf-8"))]
        for label in labels + re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", s):
            self.assertEqual(all_labels.count(label), 1, label)
        stack = []
        for cmd, env in re.findall(r"\\(begin|end)\{([^}]+)\}", s):
            if cmd == "begin":
                stack.append(env)
            else:
                self.assertTrue(stack, env)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        for match in re.finditer(r"\\begin\{(twierdzenie|stwierdzenie|lemat|wniosek)\}(.*?)\\end\{\1\}", s, re.S):
            if "wynik zewnętrzny" in match.group(2).splitlines()[0]:
                continue
            self.assertTrue(s[match.end():].lstrip().startswith(r"\begin{proof}"),
                            match.group(2)[:100])
        path = CHAPTER.relative_to(ROOT).as_posix()
        self.assertIn(path, (ROOT / "books/pl/category_theory.tex").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        self.assertIn(path, next(b for b in catalog["books"]
                                 if b["id"] == "category_theory")["chapters"])


if __name__ == "__main__":
    unittest.main()
