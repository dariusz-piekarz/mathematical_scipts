"""Finite-model sanity checks for LST-02. Does not certify Lean/LaTeX semantics.

This executable intentionally uses explicit exceptions rather than ``assert``:
Python -O and -OO remove assert statements and must not disable the audit.
"""
from __future__ import annotations

from itertools import product
import json


class FiniteModelAuditError(RuntimeError):
    """A finite-model requirement or its negative control failed."""


def require(condition: bool, detail: str) -> None:
    if not condition:
        raise FiniteModelAuditError(detail)


def all_truth_assignments(size: int):
    yield from product((False, True), repeat=size)


def test_unary() -> dict:
    checked = 0
    for d in range(5):
        for values in all_truth_assignments(d):
            # Classical Boolean semantics: both quantifier De Morgan laws.
            require((not all(values)) == any(not x for x in values),
                    f"not-forall law fails at d={d}, P={values}")
            require((not any(values)) == all(not x for x in values),
                    f"not-exists law fails at d={d}, P={values}")
            # Exists-unique means one and only one witness.
            exists_unique = sum(values) == 1
            exists_and_unique = any(
                values[x] and all((not values[y]) or y == x for y in range(d))
                for x in range(d)
            )
            require(exists_unique == exists_and_unique,
                    f"unique-exists expansion fails at d={d}, P={values}")
            checked += 1
    require(checked == 31, f"expected 31 unary models, got {checked}")
    return {"unary_predicates": checked, "domain_sizes": list(range(5))}


def test_binary() -> dict:
    checked = 0
    reverse_counterexamples = 0
    empty_empty_counterexample = False
    positive_positive_counterexample = False
    for d in range(4):
        for e in range(4):
            pairs = list(product(range(d), range(e)))
            for bits in all_truth_assignments(len(pairs)):
                predicate = dict(zip(pairs, bits, strict=True))
                def p(x: int, y: int) -> bool:
                    return predicate[x, y]
                # Switch the order of binders, not argument order of P(x,y).
                ff_xy = all(all(p(x, y) for y in range(e)) for x in range(d))
                ff_yx = all(all(p(x, y) for x in range(d)) for y in range(e))
                require(ff_xy == ff_yx,
                        f"forall-commutation fails at d={d}, e={e}, P={bits}")
                ee_xy = any(any(p(x, y) for y in range(e)) for x in range(d))
                ee_yx = any(any(p(x, y) for x in range(d)) for y in range(e))
                require(ee_xy == ee_yx,
                        f"exists-commutation fails at d={d}, e={e}, P={bits}")
                exists_forall = any(all(p(x, y) for x in range(d)) for y in range(e))
                forall_exists = all(any(p(x, y) for y in range(e)) for x in range(d))
                require(not exists_forall or forall_exists,
                        f"mixed forward implication fails at d={d}, e={e}, P={bits}")
                if forall_exists and not exists_forall:
                    reverse_counterexamples += 1
                    empty_empty_counterexample |= d == 0 and e == 0
                    positive_positive_counterexample |= d > 0 and e > 0
                checked += 1
    require(checked == 689, f"expected 689 binary models, got {checked}")
    require(reverse_counterexamples == 201,
            f"expected 201 countermodels, got {reverse_counterexamples}")
    require(empty_empty_counterexample, "missing empty-empty reverse countermodel")
    require(positive_positive_counterexample, "missing nonempty reverse countermodel")
    return {
        "binary_predicates": checked,
        "domain_sizes": list(range(4)),
        "reverse_mixed_counterexamples": reverse_counterexamples,
        "has_empty_empty_counterexample": empty_empty_counterexample,
        "has_nonempty_nonempty_counterexample": positive_positive_counterexample,
    }


def test_negative_controls() -> dict:
    """Ensure false claims actually fail, even if Python has -O enabled."""
    vals = (True, False)
    incorrect_de_morgan = (not all(vals)) == all(not x for x in vals)
    vals_two = (True, True)
    incorrect_unique = (sum(vals_two) == 1) == any(vals_two)
    # A nonempty counterexample: D=E={0,1}, P(x,y) iff x=y.
    reverse_mixed_false_claim = (
        not all(any(x == y for y in range(2)) for x in range(2))
        or any(all(x == y for x in range(2)) for y in range(2))
    )
    rejected = 0
    for name, false_claim in (
        ("wrong_not_forall", incorrect_de_morgan),
        ("wrong_unique", incorrect_unique),
        ("wrong_reverse_mixed", reverse_mixed_false_claim),
    ):
        try:
            require(false_claim, f"negative control: {name}")
        except FiniteModelAuditError:
            rejected += 1
        else:
            raise FiniteModelAuditError(f"negative control silently passed: {name}")
    require(rejected == 3, "not all negative controls were rejected")
    return {"deliberately_false_claims_rejected": rejected}


def main() -> None:
    result = {
        "scope": "finite Boolean models only; not a semantic certificate",
        "unary": test_unary(),
        "binary": test_binary(),
        "negative_controls": test_negative_controls(),
        "status": "passed",
        "certificate": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
