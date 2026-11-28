"""Deterministic finite-field regression tests for linear algebra chapter 10.

Checks wedge signs and vanishing, minor coordinates, Cauchy--Binet,
shuffle products and symmetric/exterior basis dimensions over F_2 and F_3.
Run: python tools/test_linear_algebra_exterior.py
No third-party dependencies.
"""
from itertools import combinations, permutations, product
from math import comb
from random import Random


def det(a, p):
    n = len(a)
    if n == 0:
        return 1
    value = 0
    for order in permutations(range(n)):
        inversions = sum(
            order[i] > order[j]
            for i in range(n)
            for j in range(i + 1, n)
        )
        prod = 1 if inversions % 2 == 0 else -1
        for i, j in enumerate(order):
            prod *= a[i][j]
        value += prod
    return value % p


def wedge(vectors, p):
    """Exterior product in the canonical ordered basis, as a sparse dict."""
    state = {(): 1}
    for vector in vectors:
        nxt = {}
        for indices, coeff in state.items():
            for j, x in enumerate(vector):
                if j in indices:
                    continue
                order = tuple(sorted((*indices, j)))
                parity = sum(index > j for index in indices)
                sign = -1 if parity % 2 else 1
                nxt[order] = (
                    nxt.get(order, 0) + coeff * x * sign
                ) % p
        state = {indices: x for indices, x in nxt.items() if x}
    return state


def matmul(a, b, p):
    return [
        [
            sum(a[i][t] * b[t][j] for t in range(len(b))) % p
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def submatrix(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def vectors(p, n):
    return list(product(range(p), repeat=n))


def test_wedges():
    cases = 0
    for p, n in ((2, 3), (3, 3), (2, 4), (3, 2)):
        vs = vectors(p, n)
        for v in vs:
            assert wedge((v, v), p) == {}, ("v wedge v", p, n, v)
            cases += 1
        for u in vs:
            for v in vs:
                a, b = wedge((u, v), p), wedge((v, u), p)
                for indices in set(a) | set(b):
                    assert (a.get(indices, 0) + b.get(indices, 0)) % p == 0, (
                        "antisymmetry", p, n, u, v, indices
                    )
                cases += 1
    return cases


def test_minor_coordinates():
    rng = Random(13073)
    count = 0
    for p, n, k in ((2, 3, 2), (2, 3, 3), (3, 3, 2),
                    (3, 3, 3), (2, 4, 3)):
        vs = vectors(p, n)
        inputs = list(product(vs, repeat=k)) if p == 2 else [
            tuple(vs[rng.randrange(len(vs))] for _ in range(k))
            for _ in range(3000)
        ]
        for args in inputs:
            coeffs = wedge(args, p)
            for idx in combinations(range(n), k):
                mat = [[vec[i] for vec in args] for i in idx]
                assert coeffs.get(idx, 0) == det(mat, p), (
                    "minor coordinates", p, n, k, args, idx
                )
                count += 1
    return count


def test_cauchy_binet():
    rng = Random(20261121)
    count = 0
    for p in (2, 3):
        matrices_a = [
            [list(flat[i * 3:(i + 1) * 3]) for i in range(2)]
            for flat in product(range(p), repeat=6)
        ]
        matrices_b = [
            [list(flat[i * 2:(i + 1) * 2]) for i in range(3)]
            for flat in product(range(p), repeat=6)
        ]
        pairs = (
            product(matrices_a, matrices_b)
            if p == 2 else
            ((matrices_a[rng.randrange(len(matrices_a))],
              matrices_b[rng.randrange(len(matrices_b))])
             for _ in range(3000))
        )
        for a, b in pairs:
            ab = matmul(a, b, p)
            for k in range(3):
                for rows in combinations(range(2), k):
                    for cols in combinations(range(2), k):
                        left = det(submatrix(ab, rows, cols), p)
                        right = sum(
                            det(submatrix(a, rows, mid), p)
                            * det(submatrix(b, mid, cols), p)
                            for mid in combinations(range(3), k)
                        ) % p
                        assert left == right, (
                            "Cauchy-Binet", p, k, a, b, rows, cols
                        )
                        count += 1
    # k=2 exceeds the 1-dimensional intermediate space.
    for p in (2, 3):
        for coeff in product(range(p), repeat=4):
            a = [[coeff[0]], [coeff[1]]]
            b = [[coeff[2], coeff[3]]]
            assert det(matmul(a, b, p), p) == 0
            count += 1
    return count


def test_shuffles():
    rng = Random(271828)
    count = 0
    for p in (2, 3):
        for r, s in ((1, 2), (2, 1), (1, 1), (0, 3)):
            n = 3
            k = r + s
            for _ in range(1200):
                covectors = [
                    [rng.randrange(p) for _ in range(n)]
                    for _ in range(k)
                ]
                args = [
                    [rng.randrange(p) for _ in range(n)]
                    for _ in range(k)
                ]
                full = [
                    [sum(a * b for a, b in zip(row, col)) % p
                     for col in args]
                    for row in covectors
                ]
                expected = det(full, p)
                actual = 0
                for order in permutations(range(k)):
                    if order[:r] != tuple(sorted(order[:r])):
                        continue
                    if order[r:] != tuple(sorted(order[r:])):
                        continue
                    inversions = sum(
                        order[i] > order[j]
                        for i in range(k)
                        for j in range(i + 1, k)
                    )
                    sign = -1 if inversions % 2 else 1
                    left = det(submatrix(full, range(r), order[:r]), p)
                    right = det(
                        submatrix(full, range(r, k), order[r:]), p
                    )
                    actual += sign * left * right
                assert expected == actual % p, (
                    "shuffle product", p, r, s, full
                )
                count += 1
    return count


def test_dimensions():
    count = 0
    for n in range(5):
        for k in range(6):
            exterior = sum(1 for _ in combinations(range(n), k))
            assert exterior == (comb(n, k) if k <= n else 0)
            if n == 0:
                symmetric = int(k == 0)
            else:
                symmetric = sum(
                    sum(a) == k
                    for a in product(range(k + 1), repeat=n)
                )
                assert symmetric == comb(n + k - 1, k)
            count += 1
    return count


def main():
    a = test_wedges()
    b = test_minor_coordinates()
    c = test_cauchy_binet()
    d = test_shuffles()
    e = test_dimensions()
    print(
        "Exterior algebra regression tests OK:",
        a, "alternation cases;",
        b, "minor-coordinate comparisons;",
        c, "Cauchy-Binet comparisons;",
        d, "shuffle-product comparisons;",
        e, "dimension checks; over F_2 and F_3."
    )


if __name__ == "__main__":
    main()
