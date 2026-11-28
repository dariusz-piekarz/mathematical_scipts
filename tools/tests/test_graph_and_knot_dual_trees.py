#!/usr/bin/env python3
"""TG19-DUAL-01: exact complementary and weighted dual tree regression."""
from fractions import Fraction
from itertools import combinations
from math import prod


def trees(n, edges):
    result = set()
    for subset in combinations(range(len(edges)), n - 1):
        parent = list(range(n))
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for i in subset:
            u, v = edges[i]
            a, b = root(u), root(v)
            if a == b:
                break
            parent[a] = b
        else:
            if len({root(v) for v in range(n)}) == 1:
                result.add(frozenset(subset))
    return result


def main():
    # Correspondence by index, with explicit spherical dual embeddings.
    models = [
        (1, [], 1, []),
        (2, [(0, 1)], 1, [(0, 0)]),
        (1, [(0, 0)], 2, [(0, 1)]),
        (3, [(0, 1), (1, 2), (2, 0)], 2, [(0, 1)] * 3),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)],
         3, [(0, 2), (0, 2), (1, 2), (1, 2), (0, 1)]),
    ]
    for n, E, f, D in models:
        assert n - len(E) + f == 2 and len(E) == len(D)
        primal, dual = trees(n, E), trees(f, D)
        all_edges = frozenset(range(len(E)))
        assert primal and {all_edges - T for T in primal} == dual
        for w in ([Fraction(i + 2) for i in all_edges],
                  [Fraction((-1)**i, i + 2) for i in all_edges]):
            left = sum(prod(w[i] for i in T) for T in primal)
            right = prod(w) * sum(prod(1 / w[i] for i in T) for T in dual)
            assert left == right
        print(f"PASS TG19-DUAL-01 n={n} m={len(E)} f={f} trees={len(primal)}")
    # Even vertex degrees do not require even face-boundary lengths.
    assert all(d % 2 == 0 for d in (2, 2, 2))
    assert 3 % 2 == 1  # a triangular face of the embedded cycle C3


if __name__ == "__main__":
    main()
