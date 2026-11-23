"""Independent exhaustive finite-model tests for chapter 02 (measure theory)."""
from itertools import combinations, product
from math import inf

X = frozenset(range(4))
subsets = [frozenset(s) for k in range(5) for s in combinations(X, k)]

def measure(a, weights):
    return sum((weights[x] for x in a), 0)

checked = 0
for weights in product((0, 1, 2, inf), repeat=4):
    m = {a: measure(a, weights) for a in subsets}
    assert m[frozenset()] == 0
    for a, b in product(subsets, repeat=2):
        assert m[a] <= m[a | b]
        assert m[a | b] <= m[a] + m[b]
        if a.isdisjoint(b):
            assert m[a | b] == m[a] + m[b]
        if a <= b and m[a] < inf:
            assert m[b - a] == m[b] - m[a]
        checked += 1
    atoms = [a for a in subsets if m[a] > 0 and all(
        m[t] == 0 or m[a-t] == 0 for t in subsets if t <= a
    )]
    if all(w < inf for w in weights):
        assert all(0 < m[a] < inf for a in atoms)
print(f"PASS: 256 measures, {checked} subset pairs")

def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for p in partitions(rest):
        yield [frozenset((first,))] + p
        for i in range(len(p)):
            q = p.copy()
            q[i] = q[i] | {first}
            yield q

def algebra(blocks):
    return {frozenset().union(*(blocks[i] for i in range(len(blocks))
              if mask & (1 << i))) for mask in range(1 << len(blocks))}

cases = 0
for blocks in partitions(list(X)):
    F = algebra(blocks)
    for weights in product((0, 1, 2), repeat=len(blocks)):
        def mu(a):
            return sum(weights[i] for i, block in enumerate(blocks) if block <= a)
        completed = {e for e in subsets if any(
            a <= e <= b and mu(b-a) == 0
            for a in F for b in F if a <= b
        )}
        assert F <= completed
        assert all((X-e) in completed for e in completed)
        assert all((a | b) in completed for a in completed for b in completed)
        def mubar(e):
            return mu(next(a for a in F if a <= e and any(
                e <= b and mu(b-a) == 0 for b in F
            )))
        for a, b in product(completed, repeat=2):
            if a.isdisjoint(b):
                assert mubar(a | b) == mubar(a) + mubar(b)
        for e in completed:
            if mubar(e) == 0:
                assert all(t in completed and mubar(t) == 0
                           for t in subsets if t <= e)
        cases += 1
print(f"PASS: {cases} partition-algebra/measure completions")
