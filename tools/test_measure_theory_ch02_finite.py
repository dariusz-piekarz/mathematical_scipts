"""Finite-model regression for chapter 02: measures and their basic properties.

Enumerates all sigma algebras on a four-point space, with atom weights
in {0, 1, 2, infinity}, and all pi-systems on a three-point space.
These checks are finite regressions, not proofs of general theorems.
"""
from itertools import combinations, product
from math import inf, isfinite

N = 4
X = (1 << N) - 1
WEIGHTS = (0, 1, 2, inf)


def partitions(items):
    if not items:
        yield ()
        return
    x, *rest = items
    for blocks in partitions(rest):
        yield (frozenset((x,)),) + blocks
        for i, block in enumerate(blocks):
            yield blocks[:i] + (block | frozenset((x,)),) + blocks[i + 1:]


def bitset(items):
    return sum(1 << i for i in items)


def powerset(items):
    return [sum(items[i] for i in range(len(items)) if mask & (1 << i))
            for mask in range(1 << len(items))]


def check_measures_and_completion():
    total = completed_instances = pairs = triples = pushforward_checks = 0
    finite_models = singular_models = 0
    all_subsets = list(range(1 << N))
    partitions_seen = set()

    for partition in partitions(tuple(range(N))):
        blocks = tuple(sorted(bitset(block) for block in partition))
        assert blocks not in partitions_seen
        partitions_seen.add(blocks)
        assert sum(blocks) == X
        field = tuple(sorted(powerset(blocks)))
        field_set = set(field)
        assert len(field) == len(field_set) == 1 << len(blocks)
        for a, b in product(field, repeat=2):
            assert a | b in field_set and X ^ a in field_set

        for weights in product(WEIGHTS, repeat=len(blocks)):
            total += 1
            values = {
                mask: sum(weight for block, weight in zip(blocks, weights)
                          if mask & block)
                for mask in field
            }
            mu = values.__getitem__
            assert mu(0) == 0
            for a, b in product(field, repeat=2):
                pairs += 1
                assert mu(a | b) <= mu(a) + mu(b)
                if not a & b:
                    assert mu(a | b) == mu(a) + mu(b)
                if a & b == a:
                    assert mu(a) <= mu(b)
                    if isfinite(mu(a)):
                        assert mu(b & ~a) == mu(b) - mu(a)

            for a, b, c in product(field, repeat=3):
                triples += 1
                if not (a & b or a & c or b & c):
                    assert mu(a | b | c) == mu(a) + mu(b) + mu(c)
                # Periodic three-term sequences: liminf is intersection;
                # limsup is union. The finite-total-mass hypothesis matters.
                assert mu(a & b & c) <= min(mu(a), mu(b), mu(c))
                if isfinite(mu(X)):
                    assert max(mu(a), mu(b), mu(c)) <= mu(a | b | c)

            # All witnesses of completion must assign the same measure.
            completed = {}
            for subset in all_subsets:
                witness_values = {
                    mu(a) for a in field for b in field
                    if (a & subset) == a and (subset & b) == subset
                    and mu(b & ~a) == 0
                }
                if witness_values:
                    assert len(witness_values) == 1, (blocks, weights, subset)
                    completed[subset] = witness_values.pop()
            domain = set(completed)
            completed_instances += len(domain)
            assert field_set.issubset(domain)
            assert 0 in domain and X in domain
            for subset in domain:
                assert X ^ subset in domain
                if completed[subset] == 0:
                    for sub in all_subsets:
                        if sub & subset == sub:
                            assert sub in domain and completed[sub] == 0
            for a, b in product(domain, repeat=2):
                assert a | b in domain
                assert completed[a | b] <= completed[a] + completed[b]
                if not a & b:
                    assert completed[a | b] == completed[a] + completed[b]
            assert all(completed[a] == mu(a) for a in field)

            atoms = [
                a for a in field if mu(a) > 0
                and all(mu(sub) == 0 or mu(a & ~sub) == 0
                        for sub in field if sub & a == sub)
            ]
            if all(map(isfinite, weights)):
                finite_models += 1
                assert all(0 < mu(atom) < inf for atom in atoms)
            else:
                singular_models += 1

            # All measurable pushforwards to a two-point target space.
            for mapping in product((0, 1), repeat=N):
                pre1 = bitset(i for i, v in enumerate(mapping) if v == 1)
                if pre1 not in field_set:
                    continue
                pre0 = X ^ pre1
                assert pre0 in field_set
                assert mu(pre0 | pre1) == mu(pre0) + mu(pre1)
                pushforward_checks += 1

    assert len(partitions_seen) == 15
    assert total == 756
    assert finite_models + singular_models == total
    print("PASS: 15 four-point sigma algebras")
    print(f"PASS: {total} measures ({finite_models} finite; "
          f"{singular_models} with infinite weights)")
    print(f"PASS: {pairs} ordered pairs and {triples} ordered triples")
    print(f"PASS: {completed_instances} completion-set instances")
    print(f"PASS: {pushforward_checks} measurable pushforwards")


def check_pi_lambda_uniqueness():
    # Test all nonempty intersection-closed families on three points.
    n = 3
    universe = (1 << n) - 1
    subsets = tuple(range(1 << n))
    systems = matching_pairs = 0
    for system_mask in range(1, 1 << len(subsets)):
        pi = {s for s in subsets if system_mask & (1 << s)}
        if any((a & b) not in pi for a, b in product(pi, repeat=2)):
            continue
        generated = set(pi) | {0, universe}
        while True:
            grown = generated | {universe ^ a for a in generated}
            grown |= {a | b for a, b in product(generated, repeat=2)}
            if grown == generated:
                break
            generated = grown
        systems += 1
        choices = tuple(product((0, 1, 2), repeat=n))
        for w1, w2 in product(choices, repeat=2):
            def mu(mask, weights):
                return sum(weights[i] for i in range(n)
                           if mask & (1 << i))
            if mu(universe, w1) != mu(universe, w2):
                continue
            if any(mu(a, w1) != mu(a, w2) for a in pi):
                continue
            matching_pairs += 1
            assert all(mu(a, w1) == mu(a, w2) for a in generated)
    assert systems == 121 and matching_pairs == 4509
    print(f"PASS: {systems} three-point pi-systems, "
          f"{matching_pairs} matching finite-measure pairs")


if __name__ == "__main__":
    check_measures_and_completion()
    check_pi_lambda_uniqueness()
