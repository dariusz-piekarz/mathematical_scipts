"""Finite-model regressions for measure-theory chapter 03.

These tests challenge the formulas; they are not a proof in general.
"""
from collections import Counter
from itertools import product
from math import inf

VALUES = (0, 1, 2, inf)


def caratheodory_sets(outer, universe):
    return {e for e in range(universe + 1)
            if all(outer[t] == outer[t & e] + outer[t & (universe ^ e)]
                   for t in range(universe + 1))}


def check_outer_measure_axioms():
    universe = 7
    sizes = Counter()
    count = 0
    for rest in product(VALUES, repeat=universe):
        outer = (0, *rest)
        if any(outer[a] > outer[b] for a in range(8)
               for b in range(8) if a & b == a):
            continue
        if any(outer[a | b] > outer[a] + outer[b]
               for a in range(8) for b in range(8)):
            continue
        count += 1
        measurable = caratheodory_sets(outer, universe)
        sizes[len(measurable)] += 1
        assert 0 in measurable and universe in measurable
        for e in measurable:
            assert (universe ^ e) in measurable
            if outer[e] == 0:
                for t in range(8):
                    if t & e == t:
                        assert t in measurable and outer[t] == 0
        for a, b in product(measurable, repeat=2):
            assert a | b in measurable
            if a & b == 0:
                assert outer[a | b] == outer[a] + outer[b]
    assert count == 81 and sizes == {2: 16, 4: 27, 8: 38}
    print("PASS: 81 three-point outer measures, 16/27/38 measurable algebras")


def partitions(seq):
    if not seq:
        yield ()
        return
    first = seq[0]
    for part in partitions(seq[1:]):
        yield (frozenset((first,)),) + part
        for i, block in enumerate(part):
            yield part[:i] + (block | {first},) + part[i+1:]


def check_premeasure_extensions():
    universe = 15
    seen = set()
    models = sigma_finite = measurable_sets = 0
    for part in partitions(tuple(range(4))):
        blocks = tuple(sorted(sum(1 << x for x in block) for block in part))
        assert blocks not in seen
        seen.add(blocks)
        algebra = {sum(block for i, block in enumerate(blocks)
                       if choice & (1 << i))
                   for choice in range(1 << len(blocks))}
        assert len(algebra) == 1 << len(blocks)
        for weights in product(VALUES, repeat=len(blocks)):
            models += 1
            pre = {a: sum(w for block, w in zip(blocks, weights)
                          if a & block) for a in algebra}
            assert pre[0] == 0
            for a, b in product(algebra, repeat=2):
                if a & b == 0:
                    assert pre[a | b] == pre[a] + pre[b]
            outer = {e: min(pre[a] for a in algebra if e & a == e)
                     for e in range(16)}
            expected = {e: sum(w for block, w in zip(blocks, weights)
                               if e & block) for e in range(16)}
            assert outer == expected
            assert all(outer[a] == pre[a] for a in algebra)
            measurable = caratheodory_sets(outer, universe)
            measurable_sets += len(measurable)
            assert algebra.issubset(measurable)
            for a, b in product(measurable, repeat=2):
                assert a | b in measurable
                if a & b == 0:
                    assert outer[a | b] == outer[a] + outer[b]
            completion = {
                e for e in range(16)
                if any(a & e == a and e & b == e
                       and pre[b & (universe ^ a)] == 0
                       for a in algebra for b in algebra if a & b == a)
            }
            assert completion.issubset(measurable)
            if all(w < inf for w in weights):
                sigma_finite += 1
                assert completion == measurable
    assert len(seen) == 15 and models == 756
    assert sigma_finite == 309 and measurable_sets == 9812
    print("PASS: 15 four-point algebras, 756 premeasures, "
          "309 sigma-finite, 9812 measurable-set instances")


def check_condition_is_not_necessary():
    # On P({a,b}), c(unknown nonempty)=1 is not a premeasure.
    # Its induced outer measure still equals c on every set.
    cost = (0, 1, 1, 1)
    assert cost[3] != cost[1] + cost[2]
    induced = [min(cost[a] for a in range(4) if e & a == e)
               for e in range(4)]
    assert induced == list(cost)
    print("PASS: premeasure condition is sufficient, not necessary")


if __name__ == "__main__":
    check_outer_measure_axioms()
    check_premeasure_extensions()
    check_condition_is_not_necessary()
