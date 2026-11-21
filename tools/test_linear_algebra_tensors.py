"""Independent finite-field regression checks for linear algebra chapter 09.

Pure Python; deliberately does not import the manuscript's formulas or NumPy.
Run: python tools/test_linear_algebra_tensors.py
"""
from itertools import product


def matrices(p: int, n: int):
    return [
        [list(entries[i * n:(i + 1) * n]) for i in range(n)]
        for entries in product(range(p), repeat=n * n)
    ]


def rank_mod(rows, p: int) -> int:
    a = [list(row) for row in rows]
    if not a:
        return 0
    nrows, ncols = len(a), len(a[0])
    pivot = 0
    for col in range(ncols):
        index = next(
            (r for r in range(pivot, nrows) if a[r][col] % p), None
        )
        if index is None:
            continue
        a[pivot], a[index] = a[index], a[pivot]
        scalar = pow(a[pivot][col] % p, -1, p)
        a[pivot] = [(scalar * x) % p for x in a[pivot]]
        for r in range(nrows):
            if r != pivot:
                value = a[r][col]
                a[r] = [
                    (x - value * y) % p
                    for x, y in zip(a[r], a[pivot])
                ]
        pivot += 1
        if pivot == nrows:
            break
    return pivot


def matmul(a, b, p: int):
    return [
        [sum(x * y for x, y in zip(row, col)) % p for col in zip(*b)]
        for row in a
    ]


def transpose(a):
    return [list(col) for col in zip(*a)]


def kronecker(a, b, p: int):
    return [
        [(x * y) % p for x in row_a for y in row_b]
        for row_a in a
        for row_b in b
    ]


def flat(a):
    return tuple(x for row in a for x in row)


def simple_coefficients(p: int):
    vectors = list(product(range(p), repeat=2))
    return {
        tuple((x * y) % p for x in v for y in w)
        for v in vectors
        for w in vectors
    }


def relation_rank(p: int, n: int, m: int):
    """Rank of bilinearity relations in the free space K^(K^n x K^m)."""
    vs = list(product(range(p), repeat=n))
    ws = list(product(range(p), repeat=m))
    pairs = [(v, w) for v in vs for w in ws]
    position = {pair: i for i, pair in enumerate(pairs)}
    relations = []

    def add_relation(terms):
        row = [0] * len(pairs)
        for coeff, v, w in terms:
            row[position[(v, w)]] = (row[position[(v, w)]] + coeff) % p
        relations.append(row)

    for v in vs:
        for u in vs:
            s = tuple((x + y) % p for x, y in zip(v, u))
            for w in ws:
                add_relation([(1, s, w), (-1, v, w), (-1, u, w)])
    for v in vs:
        for w in ws:
            for a in range(p):
                av = tuple(a * x % p for x in v)
                aw = tuple(a * x % p for x in w)
                add_relation([(1, av, w), (-a, v, w)])
                add_relation([(1, v, aw), (-a, v, w)])
    for v in vs:
        for w in ws:
            for u in ws:
                s = tuple((x + y) % p for x, y in zip(w, u))
                add_relation([(1, v, s), (-1, v, w), (-1, v, u)])
    return len(pairs), rank_mod(relations, p)


def test_tensor_quotients():
    scenarios = [(2, 2, 2), (3, 1, 1), (3, 1, 2), (2, 0, 2)]
    for p, n, m in scenarios:
        free_dim, rel_dim = relation_rank(p, n, m)
        assert free_dim - rel_dim == n * m, (
            "tensor quotient dimension", p, n, m, free_dim, rel_dim
        )
    return len(scenarios)


def test_tensor_matrices():
    pair_checks = 0
    composition_checks = 0
    simple_checks = 0
    for p in (2, 3):
        all_mats = matrices(p, 2)
        ranks = [rank_mod(a, p) for a in all_mats]
        for i, a in enumerate(all_mats):
            for j, b in enumerate(all_mats):
                tensor = kronecker(a, b, p)
                assert rank_mod(tensor, p) == ranks[i] * ranks[j], (
                    "Kronecker rank", p, i, j
                )
                assert transpose(tensor) == kronecker(
                    transpose(a), transpose(b), p
                ), ("Kronecker transpose", p, i, j)
                pair_checks += 1

                # Deterministic third factor, traversing all first two factors.
                c = all_mats[(i * 37 + j * 19) % len(all_mats)]
                left = kronecker(matmul(a, b, p), matmul(b, c, p), p)
                right = matmul(
                    kronecker(a, b, p), kronecker(b, c, p), p
                )
                assert left == right, ("mixed product", p, i, j)
                composition_checks += 1

        simple = simple_coefficients(p)
        expected = {flat(a) for a in all_mats if rank_mod(a, p) <= 1}
        assert simple == expected, ("decomposable criterion", p)
        assert flat([[1, 0], [0, 1]]) not in simple, (
            "identity is not decomposable", p
        )
        simple_checks += len(all_mats)

    return pair_checks, composition_checks, simple_checks


def main():
    quotient_checks = test_tensor_quotients()
    pairs, compositions, simple = test_tensor_matrices()
    print(
        "Tensor regression tests OK:",
        quotient_checks, "free-space quotient dimensions;",
        pairs, "Kronecker rank and transpose pairs;",
        compositions, "Kronecker mixed-product compositions;",
        simple, "tensor decomposability checks;",
        "fields F_2 and F_3, including a zero-dimensional factor."
    )


if __name__ == "__main__":
    main()
