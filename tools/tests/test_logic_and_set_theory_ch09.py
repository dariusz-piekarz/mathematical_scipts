"""Chapter 09 regression: finite words, parsing and capture-avoiding substitution.

Finite checks are independent falsification attempts, not proofs of general
syntax theorems. Tokens of the small test grammar are distinct.
"""
from itertools import product
import unittest


def v(i):
    return ("v", i)


def f(a, b):
    return ("f", a, b)


def fv_term(t):
    if t[0] == "v":
        return {t[1]}
    if t[0] == "c":
        return set()
    return fv_term(t[1]) | fv_term(t[2])


def sub_term(t, x, u):
    if t[0] == "v":
        return u if t[1] == x else t
    if t[0] == "c":
        return t
    return f(sub_term(t[1], x, u), sub_term(t[2], x, u))


def fv_formula(p):
    tag = p[0]
    if tag == "eq":
        return fv_term(p[1]) | fv_term(p[2])
    if tag == "neg":
        return fv_formula(p[1])
    if tag in {"all", "ex"}:
        return fv_formula(p[2]) - {p[1]}
    return fv_formula(p[1]) | fv_formula(p[2])


def admissible(p, x, u):
    tag = p[0]
    if tag == "eq":
        return True
    if tag == "neg":
        return admissible(p[1], x, u)
    if tag in {"and", "imp"}:
        return admissible(p[1], x, u) and admissible(p[2], x, u)
    if p[1] == x or x not in fv_formula(p[2]):
        return True
    return p[1] not in fv_term(u) and admissible(p[2], x, u)


def substitute(p, x, u):
    tag = p[0]
    if tag == "eq":
        return ("eq", sub_term(p[1], x, u), sub_term(p[2], x, u))
    if tag == "neg":
        return ("neg", substitute(p[1], x, u))
    if tag in {"and", "imp"}:
        return (tag, substitute(p[1], x, u), substitute(p[2], x, u))
    if p[1] == x or x not in fv_formula(p[2]):
        return p
    return (tag, p[1], substitute(p[2], x, u))


def terms():
    return [
        v(0), v(1), v(2), ("c",), f(v(0), v(1)),
        f(v(1), ("c",)), f(v(2), v(2)),
        f(f(v(0), ("c",)), v(2)),
    ]


def formulas():
    base_atoms = [("eq", a, b) for a in terms()[:4]
                  for b in terms()[:4]]
    acc = list(base_atoms)
    for depth in range(3):
        base = base_atoms[:10] if depth == 0 else acc[-min(140, len(acc)):]
        new = []
        for a in base:
            new.append(("neg", a))
            for i in range(3):
                new.append(("all", i, a))
                new.append(("ex", i, a))
        for i in range(min(45, len(base))):
            new.append(("imp" if i % 2 else "and",
                        base[i], base[(i + 3) % len(base)]))
        acc.extend(new)
    return acc


def term_string(t):
    if t[0] == "v":
        return "v" + str(t[1])
    if t[0] == "c":
        return "c"
    return "f(" + term_string(t[1]) + "," + term_string(t[2]) + ")"


def parse_term(s, pos):
    if s.startswith("c", pos):
        return ("c",), pos + 1
    if s.startswith("v", pos):
        j = pos + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        assert j > pos + 1
        return v(int(s[pos + 1:j])), j
    assert s.startswith("f(", pos)
    a, j = parse_term(s, pos + 2)
    assert s[j] == ","
    b, j = parse_term(s, j + 1)
    assert s[j] == ")"
    return f(a, b), j + 1


class TestLogicAndSetTheoryChapter09(unittest.TestCase):
    def test_free_monoid_with_noncommutative_target(self):
        identity = (0, 1, 2)
        mapping = {"a": (1, 2, 0), "b": (0, 2, 1)}
        mul = lambda p, q: tuple(p[q[i]] for i in range(3))

        def extend(word):
            out = identity
            for letter in word:
                out = mul(out, mapping[letter])
            return out

        words = [tuple(w) for n in range(5)
                 for w in product(("a", "b"), repeat=n)]
        for w in words:
            self.assertEqual(extend(w + ()), extend(w))
            self.assertEqual(extend((),), identity)
            for z in words:
                self.assertEqual(extend(w + z), mul(extend(w), extend(z)))
        self.assertNotEqual(mul(mapping["a"], mapping["b"]),
                            mul(mapping["b"], mapping["a"]))

    def test_unique_term_parsing_and_fv(self):
        for t in terms():
            written = term_string(t)
            decoded, end = parse_term(written, 0)
            self.assertEqual(decoded, t)
            self.assertEqual(end, len(written))
            for x in range(3):
                for u in terms():
                    got = fv_term(sub_term(t, x, u))
                    expected = (fv_term(t) - {x}) | fv_term(u) \
                        if x in fv_term(t) else fv_term(t)
                    self.assertEqual(got, expected)

    def test_formula_substitution_and_shadowing(self):
        fs = formulas()
        self.assertEqual(len(fs), 1838)
        checked, admissible_count, rejected = 0, 0, 0
        for phi in fs:
            for x in range(3):
                for u in terms():
                    checked += 1
                    if not admissible(phi, x, u):
                        rejected += 1
                        continue
                    admissible_count += 1
                    out = substitute(phi, x, u)
                    base = fv_formula(phi)
                    expected = ((base - {x}) | fv_term(u)
                                if x in base else base)
                    self.assertEqual(fv_formula(out), expected)
                    if x not in base:
                        self.assertEqual(out, phi)
                    if phi[0] in {"all", "ex"} and phi[1] == x:
                        self.assertEqual(out, phi)
        self.assertEqual((checked, admissible_count, rejected),
                         (44112, 37612, 6500))

    def test_capture_boundary(self):
        phi = ("all", 1, ("eq", v(0), v(1)))
        self.assertFalse(admissible(phi, 0, v(1)))
        renamed = ("all", 2, ("eq", v(0), v(2)))
        self.assertTrue(admissible(renamed, 0, v(1)))
        self.assertEqual(substitute(renamed, 0, v(1)),
                         ("all", 2, ("eq", v(1), v(2))))
        shadow = ("all", 0, ("eq", v(0), v(1)))
        self.assertEqual(substitute(shadow, 0, v(1)), shadow)


if __name__ == "__main__":
    unittest.main()
