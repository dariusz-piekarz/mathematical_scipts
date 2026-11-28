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


def finite_complex(p, d0, d1):
    """Finite cochain complex, with each additive group indexed from zero."""
    vs = tuple(itertools.product(range(p), repeat=2))
    index = {v: i for i, v in enumerate(vs)}
    spaces = {q: vs if -1 <= q <= 1 else ((0, 0),)
              for q in range(-3, 4)}
    plus = {q: tuple(tuple(spaces[q].index(tuple((x+y) % p for x, y in zip(v, w)))
                           for w in spaces[q]) for v in spaces[q])
            for q in spaces}
    diffs = {q: tuple(index[mv(d, v, p)] for v in vs)
             for q, d in ((-1, d0), (0, d1))}
    for q in spaces:
        diffs.setdefault(q, (0,) * len(spaces[q]))
    return plus, diffs


def smart_truncate(complex_, r, upper):
    """Construct the kernel or quotient at the boundary, not just ranks."""
    plus, ds = complex_
    groups, maps = {}, {}
    inclusions, projections = {}, {}
    for q, table in plus.items():
        n = len(table)
        if upper and q == r:
            reps = tuple(i for i, x in enumerate(ds[q]) if x == 0)
            proj = {i: j for j, i in enumerate(reps)}
        elif not upper and q == r:
            image = set(ds.get(q-1, (0,)))
            reps, proj = [], {}
            for i in range(n):
                if i not in proj:
                    j = len(reps)
                    reps.append(i)
                    for x in image:
                        proj[table[i][x]] = j
            reps = tuple(reps)
        elif (upper and q > r) or (not upper and q < r):
            reps, proj = (0,), dict.fromkeys(range(n), 0)
        else:
            reps, proj = tuple(range(n)), {i: i for i in range(n)}
        inclusions[q], projections[q] = reps, proj
        groups[q] = tuple(tuple(proj[table[i][j]] for j in reps) for i in reps)
    for q, reps in inclusions.items():
        target = projections.get(q+1, {0: 0})
        if upper and q >= r or not upper and q < r:
            maps[q] = (0,) * len(reps)
        else:
            maps[q] = tuple(target[ds[q][i]] for i in reps)
    return groups, maps


def cohomology_sizes(complex_):
    plus, ds = complex_
    result = {}
    for q in plus:
        kernel = sum(x == 0 for x in ds[q])
        image = len(set(ds.get(q-1, (0,))))
        assert kernel % image == 0
        result[q] = kernel // image
    return result


class CategoryTheoryCh39(unittest.TestCase):
    def test_CAT_39_001_truncation_indexing(self):
        for p in (2, 3):
            ms = list(matrices(p, 2))
            zero = ((0, 0), (0, 0))
            dims = {-1: 2, 0: 2, 1: 2}
            for d0, d1 in itertools.product(ms, repeat=2):
                if multiply(d1, d0, p) != zero:
                    continue
                ds = {-1: d0, 0: d1}
                h = coh(dims, ds, p)
                complex_ = finite_complex(p, d0, d1)
                expected = {q: p**h.get(q, 0) for q in range(-3, 4)}
                self.assertEqual(cohomology_sizes(complex_), expected)
                ups = {a: smart_truncate(complex_, -a, True)
                       for a in range(-2, 3)}
                lows = {b: smart_truncate(complex_, -b, False)
                        for b in range(-2, 3)}
                for a, b in itertools.product(range(-2, 3), repeat=2):
                    first = smart_truncate(lows[b], -a, True)
                    second = smart_truncate(ups[a], -b, False)
                    want = {q: n if -b <= q <= -a else 1
                            for q, n in expected.items()}
                    self.assertEqual(cohomology_sizes(first), want)
                    self.assertEqual(cohomology_sizes(second), want)

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
        # X,Y are two-term complexes in degrees 0,1.
        # Cone(f) in degrees -1,0,1 has actual consecutive
        # differentials x -> (f0 x,-dX x), (y,x) -> dY y+f1 x.
        p = 3
        dx = ((1, 0), (0, 0))
        dy = ((0, 1), (0, 0))
        bad_sign_detected = False
        for f0, f1 in itertools.product(matrices(p, 2), repeat=2):
            if multiply(dy, f0, p) != multiply(f1, dx, p):
                continue
            for x in itertools.product(range(p), repeat=2):
                y = mv(f0, x, p)
                z = mv(dx, x, p)
                lhs = mv(dy, y, p)
                rhs = mv(f1, z, p)
                self.assertEqual(tuple((u-v) % p for u, v in zip(lhs, rhs)), (0, 0))
                if any((u+v) % p for u, v in zip(lhs, rhs)):
                    bad_sign_detected = True
        self.assertTrue(bad_sign_detected)

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
