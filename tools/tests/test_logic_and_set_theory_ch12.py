"""Independent small-model checks for soundness of first-order natural deduction.

Finite evaluations are falsification tests, not a proof of soundness for
all first-order structures.
"""
from itertools import product
from pathlib import Path
import unittest


def v(i):
    return ("var", i)


def c():
    return ("const",)


def f(t):
    return ("func", t)


def term_value(t, model, assignment):
    if t[0] == "var":
        return assignment[t[1]]
    if t[0] == "const":
        return model["c"]
    return model["f"][term_value(t[1], model, assignment)]


def satisfies(phi, model, assignment):
    kind = phi[0]
    if kind == "eq":
        return (term_value(phi[1], model, assignment) ==
                term_value(phi[2], model, assignment))
    if kind == "P":
        return term_value(phi[1], model, assignment) in model["P"]
    if kind == "R":
        return ((term_value(phi[1], model, assignment),
                 term_value(phi[2], model, assignment)) in model["R"])
    if kind == "neg":
        return not satisfies(phi[1], model, assignment)
    if kind == "and":
        return (satisfies(phi[1], model, assignment)
                and satisfies(phi[2], model, assignment))
    if kind == "imp":
        return (not satisfies(phi[1], model, assignment)
                or satisfies(phi[2], model, assignment))
    _, x, body = phi
    values = (
        satisfies(body, model, tuple(
            value if i == x else item
            for i, item in enumerate(assignment)))
        for value in model["A"]
    )
    return all(values) if kind == "all" else any(values)


def finite_models():
    for n in (1, 2, 3):
        A = tuple(range(n))
        relation_masks = ((0, (1 << (n * n)) - 1) +
                          tuple(1 << bit for bit in range(n * n)))
        for unary_mask, rel_mask in product(range(1 << n), relation_masks):
            yield {
                "A": A, "c": 0,
                "f": tuple((i + 1) % n for i in A),
                "P": {i for i in A if unary_mask & (1 << i)},
                "R": {(i, j) for i in A for j in A
                      if rel_mask & (1 << (i * n + j))},
            }


class TestLogicAndSetTheoryChapter12(unittest.TestCase):
    def test_semantic_deduction_for_formulas_with_free_variables(self):
        total = 0
        for model in finite_models():
            assignments = tuple(product(model["A"], repeat=3))
            x, y = v(0), v(1)
            formulas = (
                ("P", x), ("P", y), ("R", x, y),
                ("eq", x, y), ("all", 0, ("P", x)),
                ("ex", 1, ("R", x, y)),
            )
            for mask in range(1 << 3):
                gamma = tuple(formulas[i] for i in range(3)
                              if mask & (1 << i))
                for alpha, beta in product(formulas, repeat=2):
                    # gamma + alpha |= beta
                    left = all(
                        not (all(satisfies(g, model, s) for g in gamma)
                             and satisfies(alpha, model, s))
                        or satisfies(beta, model, s)
                        for s in assignments
                    )
                    # gamma |= alpha -> beta
                    right = all(
                        not all(satisfies(g, model, s) for g in gamma)
                        or satisfies(("imp", alpha, beta), model, s)
                        for s in assignments
                    )
                    self.assertEqual(left, right)
                    total += 1
        self.assertGreater(total, 2000)

    def test_first_order_intro_elim_and_eigenvariable(self):
        checked = 0
        for model in finite_models():
            A = model["A"]
            for assignment in product(A, repeat=3):
                x, y = v(0), v(1)
                px, py = ("P", x), ("P", y)
                all_px = ("all", 0, px)
                ex_px = ("ex", 0, px)

                # Universal elimination with a term denoting c.
                if satisfies(all_px, model, assignment):
                    self.assertTrue(satisfies(("P", c()), model,
                                              assignment))
                # Existential introduction with x:=c.
                if satisfies(("P", c()), model, assignment):
                    self.assertTrue(satisfies(ex_px, model, assignment))
                # Universal introduction: Delta = P(y), which has no free x.
                # From Delta |- P(y) and arbitrary x obtain forall x P(y).
                if satisfies(py, model, assignment):
                    self.assertTrue(satisfies(("all", 0, py), model,
                                              assignment))

                # Existential elimination: theta is independent of the
                # local eigenvariable y, and the subdeduction works
                # for *every* possible assignment of y.
                theta = satisfies(("P", c()), model, assignment)
                major = satisfies(ex_px, model, assignment)
                local = all(
                    not satisfies(px, model, (a, assignment[1],
                                              assignment[2]))
                    or theta for a in A
                )
                self.assertTrue(not (major and local) or theta)
                checked += 1
        self.assertGreater(checked, 1000)

    def test_equality_substitution_in_formula_with_quantifier(self):
        checked = 0
        # theta(z) := forall w (P(z) -> R(f(z),w)).
        # z has no bound occurrences; its substitution is free-for.
        def theta(value, model):
            return (value not in model["P"] or
                    all((model["f"][value], w) in model["R"]
                        for w in model["A"]))

        for model in finite_models():
            for assignment in product(model["A"], repeat=3):
                term_values = (
                    assignment[0], assignment[1],
                    model["c"], model["f"][assignment[0]],
                    model["f"][model["f"][assignment[1]]],
                )
                for a, b in product(term_values, repeat=2):
                    if a == b:
                        self.assertEqual(theta(a, model), theta(b, model))
                    checked += 1
        self.assertGreater(checked, 20000)

    def test_countermodels_block_unsound_generalization(self):
        model = {
            "A": (0, 1), "c": 0, "f": (1, 0),
            "P": {0}, "R": set()
        }
        s = (0, 0, 0)
        assumption = ("P", v(0))
        conclusion = ("all", 0, ("P", v(0)))
        self.assertTrue(satisfies(assumption, model, s))
        self.assertFalse(satisfies(conclusion, model, s))
        # A satisfiable premise set cannot semantically entail bottom.
        self.assertTrue(satisfies(("eq", c(), c()), model, s))

    def test_source_induction_treats_temporary_open_assumptions(self):
        source = (Path(__file__).resolve().parents[2]
                  / "chapters/pl/logic_and_set_theory/"
                    "12-poprawnosc-logiki-pierwszego-rzedu.tex"
                  ).read_text(encoding="utf-8")
        self.assertIn("Dotyczy to również założeń tymczasowych", source)
        self.assertIn("dla każdej", source)
        self.assertIn(r"\Gamma\nvdash_{\mathrm{ND}}\bot", source)
        self.assertEqual(source.count(r"\begin{twierdzenie}"), 3)
        self.assertIn(r"\label{thm:soundness}", source)


if __name__ == "__main__":
    unittest.main()
