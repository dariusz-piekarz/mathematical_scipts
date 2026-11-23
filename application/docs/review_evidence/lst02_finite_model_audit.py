"""Independent finite-model sanity checks for LST-02 mappings, not a proof.

No Mathlib, application runtime, or GitHub checkout is required.
Checks all Boolean predicates on domain cardinalities 0..3 (unary: 0..4).
"""
from __future__ import annotations

from itertools import product
import json


def all_truth_assignments(size: int):
    yield from product((False, True), repeat=size)


def test_unary() -> dict:
    checked = 0
    for d in range(5):
        for truth in all_truth_assignments(d):
            values = list(truth)
            # LST-02: thm:negation-quantifiers (classical Boolean semantics)
            assert (not all(values)) == any(not x for x in values)
            assert (not any(values)) == all(not x for x in values)
            # LST-02: thm:unique-expansion-xli
            exists_unique = sum(values) == 1
            exists_and_unique = any(
                values[x] and all((not values[y]) or y == x for y in range(d))
                for x in range(d)
            )
            assert exists_unique == exists_and_unique
            checked += 1
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
                p = lambda x, y: predicate[x, y]
                # LST-02: thm:same-quantifier-order
                ff_xy = all(all(p(x, y) for y in range(e)) for x in range(d))
                ff_yx = all(all(p(x, y) for x in range(d)) for y in range(e))
                assert ff_xy == ff_yx
                ee_xy = any(any(p(x, y) for y in range(e)) for x in range(d))
                ee_yx = any(any(p(x, y) for x in range(d)) for y in range(e))
                assert ee_xy == ee_yx
                # LST-02: thm:swap-mixed, only this forward implication.
                exists_forall = any(all(p(x, y) for x in range(d)) for y in range(e))
                forall_exists = all(any(p(x, y) for y in range(e)) for x in range(d))
                assert not exists_forall or forall_exists
                # The unclaimed reverse implication is generally false.
                if forall_exists and not exists_forall:
                    reverse_counterexamples += 1
                    empty_empty_counterexample |= d == 0 and e == 0
                    positive_positive_counterexample |= d > 0 and e > 0
                checked += 1
    assert empty_empty_counterexample
    assert positive_positive_counterexample
    return {
        "binary_predicates": checked,
        "domain_sizes": list(range(4)),
        "reverse_mixed_counterexamples": reverse_counterexamples,
        "has_empty_empty_counterexample": empty_empty_counterexample,
        "has_nonempty_nonempty_counterexample": positive_positive_counterexample,
    }


def main() -> None:
    result = {
        "scope": "finite Boolean models only; not a semantic certificate",
        "unary": test_unary(),
        "binary": test_binary(),
        "status": "passed",
        "certificate": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
