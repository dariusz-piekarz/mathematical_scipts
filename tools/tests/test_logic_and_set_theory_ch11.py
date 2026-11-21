"""Finite-model falsification tests for natural deduction chapter 11.

These independent checks concern truth preservation and eigenvariable
conditions; they do not replace proofs of soundness for arbitrary models.
"""
from itertools import product
from pathlib import Path
import unittest


def boolean_formulas():
    return (
        lambda s: s[0], lambda s: s[1], lambda s: s[2],
        lambda s: s[0] and s[1], lambda s: s[0] or s[1],
        lambda s: not s[0] or s[1], lambda s: s[1] == s[2],
        lambda s: not s[0], lambda s: not s[2],
    )


class TestLogicAndSetTheoryChapter11(unittest.TestCase):
    def test_propositional_rules(self):
        checks = 0
        for assignment in product((False, True), repeat=3):
            for phi, psi, theta in product(boolean_formulas(), repeat=3):
                a, b, c = (fn(assignment) for fn in (phi, psi, theta))
                cases = (
                    not (a and b) or (a and b),              # conjunction I
                    not (a and b) or a,                      # conjunction E1
                    not (a and b) or b,                      # conjunction E2
                    not a or (a or b),                       # disjunction I1
                    not b or (a or b),                       # disjunction I2
                    not ((a or b) and (not a or c)
                         and (not b or c)) or c,              # disjunction E
                    not ((not a or b) and a) or b,           # implication E
                    not ((not a or b) and (not b or a))
                    or (a == b),                             # equivalence I
                    not (a == b) or (not a or b),            # equivalence E1
                    not (a == b) or (not b or a),            # equivalence E2
                    not (a and not a),                       # contradiction
                    not (not a and not (not a)),
                    a or not a,                              # classical LEM
                )
                checks += len(cases)
                self.assertTrue(all(cases))
        self.assertEqual(checks, 75816)

    def test_deduction_equivalence(self):
        fs = boolean_formulas()
        valuations = tuple(product((False, True), repeat=3))
        checks = 0
        for mask in range(64):
            gamma = tuple(f for i, f in enumerate(fs[:6])
                          if mask & (1 << i))
            for phi, psi in product(fs, repeat=2):
                left = all(not all(f(s) for f in gamma)
                           or (not phi(s) or psi(s))
                           for s in valuations)
                right = all(not (all(f(s) for f in gamma) and phi(s))
                            or psi(s) for s in valuations)
                checks += 1
                self.assertEqual(left, right)
        self.assertEqual(checks, 5184)

    def test_exists_elimination_freshness(self):
        checks = 0
        for n in (1, 2, 3):
            universe = tuple(range(n))
            rmasks = (0, (1 << (n * n)) - 1) + tuple(
                1 << bit for bit in range(n * n))
            for pmask, rmask in product(range(1 << n), rmasks):
                P = {a for a in universe if pmask & (1 << a)}
                R = lambda x, z: bool(rmask & (1 << (x * n + z)))
                for _y, z in product(universe, repeat=2):
                    formulas = (
                        lambda x, z: x in P,
                        lambda x, z: R(x, z),
                        lambda x, z: x == z,
                        lambda x, z: x != z,
                        lambda x, z: x not in P or R(x, z),
                    )
                    goals = (
                        lambda z: z in P,
                        lambda z: all(a in P for a in universe),
                        lambda z: any(R(a, z) for a in universe),
                        lambda z: False,
                        lambda z: True,
                    )
                    for phi, theta in product(formulas, goals):
                        major = any(phi(x, z) for x in universe)
                        # The local derivation can be sound under every
                        # possible assignment of the *fresh* eigenvariable.
                        local = all(not phi(y, z) or theta(z)
                                    for y in universe)
                        self.assertTrue(not (major and local) or theta(z))
                        checks += 1
        self.assertEqual(checks, 22350)

    def test_removing_freshness_is_unsound(self):
        domain = (0, 1)
        y = 0
        # Illegitimate eigenvariable in the major premise.
        major = any(x != y for x in domain)
        goal = all(z != z for z in domain)
        # Assuming not(y=y) gives contradiction by equality introduction,
        # then the false goal by ex falso.
        self.assertTrue(major)
        self.assertFalse(y != y)
        self.assertFalse(goal)

        # Illegitimate eigenvariable in another open premise.
        P = {0}
        y = 1
        R = all(z in P for z in domain)
        premise = y not in P or R  # P(y) -> R
        local = all(not (a in P and (a not in P or R)) or R
                    for a in domain)
        self.assertTrue(any(x in P for x in domain))
        self.assertTrue(premise and local)
        self.assertFalse(R)

    def test_capture_avoidance_and_finite_context(self):
        # In P(x) := forall z R(x,z), instantiation x:=z is not free-for.
        # Instantiation x:=x is always free-for x.
        free_variable, bound_variable = "x", "z"
        self.assertNotEqual(free_variable, bound_variable)
        text = (Path(__file__).resolve().parents[2]
                / "chapters/pl/logic_and_set_theory/"
                  "11-dowody-formalne-i-dedukcja-naturalna.tex"
                ).read_text(encoding="utf-8")
        self.assertIn("podstawiając za $x$ samą", text)
        self.assertIn("zbiór ten może być nieskończony", text)
        self.assertNotIn("niewystępującą\nw $\\Gamma$", text)
        self.assertIn(r"$H:=\exists x\,\neg(x=y)$", text)


    def test_equality_symmetry_requires_fresh_placeholder(self):
        # A correct substitution for the symmetry proof must not modify
        # the fixed term on the right-hand side of z=t.
        def var(i):
            return ("v", i)

        def fv(term):
            if term[0] == "v":
                return {term[1]}
            if term[0] == "c":
                return set()
            if term[0] == "f":
                return fv(term[1])
            return fv(term[1]) | fv(term[2])

        def substitute(term, variable, replacement):
            if term[0] == "v":
                return replacement if term[1] == variable else term
            if term[0] == "c":
                return term
            if term[0] == "f":
                return ("f", substitute(term[1], variable, replacement))
            return ("g", substitute(term[1], variable, replacement),
                    substitute(term[2], variable, replacement))

        base = [var(0), var(1), var(2), ("c",)]
        terms = (base
                 + [("f", t) for t in base]
                 + [("g", a, b) for a in base for b in base]
                 + [("f", ("f", var(0))),
                    ("g", ("f", var(0)), var(1))])
        self.assertEqual(len(terms), 26)
        checks = 0
        for t, u in product(terms, repeat=2):
            z = 3
            self.assertNotIn(z, fv(t) | fv(u))
            # theta(z) := (z=t). Substitution acts on *both* sides.
            theta = (var(z), t)
            self.assertEqual(tuple(substitute(e, z, t) for e in theta),
                             (t, t))
            self.assertEqual(tuple(substitute(e, z, u) for e in theta),
                             (u, t))
            checks += 1
        self.assertEqual(checks, 676)

        # Why the original theta(x) := x=t was invalid for arbitrary t:
        x, t, u = var(0), ("f", var(0)), ("c",)
        theta = (x, t)
        self.assertNotEqual(
            tuple(substitute(e, 0, t) for e in theta), (t, t))
        self.assertNotEqual(
            tuple(substitute(e, 0, u) for e in theta), (u, t))

        chapter = (Path(__file__).resolve().parents[2]
                   / "chapters/pl/logic_and_set_theory/"
                     "11-dowody-formalne-i-dedukcja-naturalna.tex"
                   ).read_text(encoding="utf-8")
        self.assertIn("nie występuje ani w $t$", chapter)
        self.assertIn(r"$\theta[z:=t]$", chapter)


if __name__ == "__main__":
    unittest.main()
