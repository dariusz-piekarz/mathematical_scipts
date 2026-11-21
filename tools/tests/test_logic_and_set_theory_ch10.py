"""Chapter 10: finite first-order semantics and second-order Henkin regression.

Finite structures check boundary cases; these are not proofs for arbitrary
infinite structures, nor a substitute for the mathematical audit.
"""
from itertools import product
from pathlib import Path
import unittest


def variable(i):
    return ("v", i)


def successor(t):
    return ("S", t)


def fv_term(t):
    if t[0] == "v":
        return {t[1]}
    if t[0] == "c":
        return set()
    return fv_term(t[1])


def substitute_term(t, x, u):
    if t[0] == "v":
        return u if t[1] == x else t
    if t[0] == "c":
        return t
    return successor(substitute_term(t[1], x, u))


def fv(phi):
    kind = phi[0]
    if kind in {"eq", "R"}:
        return fv_term(phi[1]) | fv_term(phi[2])
    if kind == "P":
        return fv_term(phi[1])
    if kind == "neg":
        return fv(phi[1])
    if kind == "bin":
        return fv(phi[2]) | fv(phi[3])
    return fv(phi[2]) - {phi[1]}


def admissible(phi, x, u):
    kind = phi[0]
    if kind in {"eq", "R", "P"}:
        return True
    if kind == "neg":
        return admissible(phi[1], x, u)
    if kind == "bin":
        return admissible(phi[2], x, u) and admissible(phi[3], x, u)
    if phi[1] == x or x not in fv(phi[2]):
        return True
    return phi[1] not in fv_term(u) and admissible(phi[2], x, u)


def substitute(phi, x, u):
    kind = phi[0]
    if kind in {"eq", "R"}:
        return (kind, substitute_term(phi[1], x, u),
                substitute_term(phi[2], x, u))
    if kind == "P":
        return ("P", substitute_term(phi[1], x, u))
    if kind == "neg":
        return ("neg", substitute(phi[1], x, u))
    if kind == "bin":
        return ("bin", phi[1], substitute(phi[2], x, u),
                substitute(phi[3], x, u))
    if phi[1] == x or x not in fv(phi[2]):
        return phi
    return ("q", phi[1], substitute(phi[2], x, u), phi[3])


def term_value(t, model, assignment):
    if t[0] == "v":
        return assignment[t[1]]
    if t[0] == "c":
        return model["c"]
    return model["S"][term_value(t[1], model, assignment)]


def satisfies(phi, model, assignment):
    kind = phi[0]
    if kind == "eq":
        return (term_value(phi[1], model, assignment)
                == term_value(phi[2], model, assignment))
    if kind == "R":
        return ((term_value(phi[1], model, assignment),
                 term_value(phi[2], model, assignment)) in model["R"])
    if kind == "P":
        return term_value(phi[1], model, assignment) in model["P"]
    if kind == "neg":
        return not satisfies(phi[1], model, assignment)
    if kind == "bin":
        a = satisfies(phi[2], model, assignment)
        b = satisfies(phi[3], model, assignment)
        return {"and": a and b, "or": a or b,
                "imp": not a or b, "iff": a == b}[phi[1]]
    _, x, body, q = phi
    vals = []
    for a in model["A"]:
        changed = tuple(a if i == x else b
                        for i, b in enumerate(assignment))
        vals.append(satisfies(body, model, changed))
    return all(vals) if q == "all" else any(vals)


def q(x, phi, kind):
    return ("q", x, phi, kind)


def sample_formulas():
    x, y, z = variable(0), variable(1), variable(2)
    return [
        ("eq", x, y), ("R", x, successor(y)),
        ("P", successor(x)), ("neg", ("P", y)),
        ("bin", "and", ("R", x, y), ("P", y)),
        ("bin", "imp", ("P", x), ("R", y, z)),
        q(0, ("R", x, y), "all"),
        q(1, ("eq", x, y), "ex"),
        q(0, q(1, ("R", x, y), "ex"), "all"),
        q(1, q(0, ("eq", x, y), "all"), "ex"),
        q(2, ("bin", "and", ("P", z), ("R", x, z)), "ex"),
        q(0, ("bin", "and", ("P", x),
              q(0, ("P", x), "ex")), "all"),
    ]


def models():
    for n in (1, 2, 3):
        A = tuple(range(n))
        masks = (0, 1, 17, 63, 129, 255, 341, 511) \
            if n == 3 else tuple(range(1 << (n * n)))
        for mask in masks:
            R = {(i, j) for i in A for j in A
                 if mask & (1 << (i * n + j))}
            for pmask in (0, 1, (1 << n) - 1):
                yield {"A": A, "R": R,
                       "P": {i for i in A if pmask & (1 << i)},
                       "c": 0, "S": tuple((i + 1) % n for i in A)}


class TestLogicAndSetTheoryChapter10(unittest.TestCase):
    def test_first_order_semantic_laws(self):
        terms = [variable(i) for i in range(3)] + [
            successor(variable(0)), successor(variable(1)),
            ("c",), successor(successor(variable(2))),
        ]
        fs = sample_formulas()
        substitution_count = quantifier_count = coincidence_count = 0
        structures = assignments = 0
        for model in models():
            structures += 1
            for assignment in product(model["A"], repeat=3):
                assignments += 1
                for phi in fs:
                    base = satisfies(phi, model, assignment)
                    for x in range(3):
                        for u in terms:
                            if not admissible(phi, x, u):
                                continue
                            substitution_count += 1
                            assigned = tuple(
                                term_value(u, model, assignment) if i == x
                                else a for i, a in enumerate(assignment))
                            self.assertEqual(
                                satisfies(substitute(phi, x, u),
                                          model, assignment),
                                satisfies(phi, model, assigned))
                        coincidence_count += 1
                        changed = tuple(
                            a if i in fv(phi) else
                            model["A"][(a + 1) % len(model["A"])]
                            for i, a in enumerate(assignment))
                        self.assertEqual(
                            base, satisfies(phi, model, changed))
                    for x in (0, 1):
                        quantifier_count += 2
                        self.assertEqual(
                            satisfies(("neg", q(x, phi, "all")),
                                      model, assignment),
                            satisfies(q(x, ("neg", phi), "ex"),
                                      model, assignment))
                        self.assertEqual(
                            satisfies(("neg", q(x, phi, "ex")),
                                      model, assignment),
                            satisfies(q(x, ("neg", phi), "all"),
                                      model, assignment))
                for phi in [
                    ("R", variable(0), variable(1)),
                    ("P", variable(0)),
                    ("eq", variable(0), successor(variable(1))),
                ]:
                    for kind in ("all", "ex"):
                        quantifier_count += 2
                        self.assertEqual(
                            satisfies(q(0, q(1, phi, kind), kind),
                                      model, assignment),
                            satisfies(q(1, q(0, phi, kind), kind),
                                      model, assignment))
                        self.assertEqual(
                            satisfies(q(0, q(0, phi, kind), kind),
                                      model, assignment),
                            satisfies(q(0, phi, kind), model, assignment))
        self.assertEqual((structures, assignments), (78, 1038))
        self.assertEqual((substitution_count, coincidence_count,
                          quantifier_count), (255348, 37368, 62280))

    def test_full_versus_henkin_second_order_induction(self):
        A = {0, 1}
        succ = {0: 0, 1: 1}
        def induction(D):
            antecedent = (0 in D and all(
                x not in D or succ[x] in D for x in A))
            return not antecedent or D == A

        full = [{x for x in A if mask & (1 << x)}
                for mask in range(1 << len(A))]
        henkin = [set(A)]
        self.assertFalse(all(induction(D) for D in full))
        self.assertTrue(all(induction(D) for D in henkin))

        source = (Path(__file__).resolve().parents[2]
                  / "chapters/pl/logic_and_set_theory/"
                    "10-struktury-wartosciowania-i-prawda.tex"
                 ).read_text(encoding="utf-8")
        self.assertIn(r"s(X^{(n)})\in\mathcal S_n", source)
        self.assertIn(r"D_n\in\mathcal S_n", source)
        self.assertIn(r"\mathcal S_n\subseteq\mathcal P(A^n)", source)


if __name__ == "__main__":
    unittest.main()
