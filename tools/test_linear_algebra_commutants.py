"""LA21: independent commutant dimensions via modular linear algebra.

Exhaustive over 2x2/F2,F3 and 3x3/F2; seeded F3 samples.
Compares centralizer dimension from AX=XA, Smith invariant factors,
and elementary divisors, plus selected exact group cardinalities.
No third-party dependencies.
"""
from itertools import product
from random import Random

from test_linear_algebra_frobenius import (
    companion, matmul, smith_factors,
)
from test_linear_algebra_elementary import elementary, rebuild, poly_evaluate


def rank(matrix, p):
    a = [list(map(lambda x: x % p, row)) for row in matrix]
    if not a:
        return 0
    nrow = len(a)
    ncol = len(a[0])
    r = 0
    for c in range(ncol):
        pivot = next((i for i in range(r, nrow) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [x * inv % p for x in a[r]]
        for i in range(nrow):
            if i == r:
                continue
            fac = a[i][c]
            a[i] = [(x - fac * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == nrow:
            break
    return r


def commute_matrix(a, n, p):
    """Linear map X -> AX-XA, rows indexed (i,j), cols indexed (k,l)."""
    basis = []
    for k in range(n):
        for l in range(n):
            x = [0] * (n * n)
            x[k * n + l] = 1
            ax = matmul(a, x, n, p)
            xa = matmul(x, a, n, p)
            basis.append([(u - v) % p for u, v in zip(ax, xa)])
    return [list(col) for col in zip(*basis)]


def direct_dimension(a, n, p):
    return n * n - rank(commute_matrix(a, n, p), p)


def gcd_poly(a, b, p):
    from test_linear_algebra_frobenius import gcd
    return gcd(a, b, p)


def factor_dimension(smith, p):
    fs = [f for f in smith if len(f) > 1]
    return sum(len(gcd_poly(f, g, p)) - 1 for f in fs for g in fs)


def elementary_dimension(smith, p):
    elems = elementary(smith, p)
    answer = 0
    for q in {q for q, _ in elems}:
        exp = [e for prime, e in elems if prime == q]
        answer += (len(q) - 1) * sum(min(a, b) for a in exp for b in exp)
    return answer


def check_matrix(a, n, p):
    smith, _ = smith_factors(a, n, p)
    d1 = direct_dimension(a, n, p)
    d2 = factor_dimension(smith, p)
    d3 = elementary_dimension(smith, p)
    assert d1 == d2 == d3, (p, n, a, smith, d1, d2, d3)
    assert n <= d1 <= n * n
    cyclic = len([f for f in smith if len(f) > 1]) == 1
    assert (d1 == n) == cyclic
    scalar = all(a[n*i+j] == (a[0] if i == j else 0)
                 for i in range(n) for j in range(n))
    assert (d1 == n * n) == scalar


def block_diag(blocks, p):
    n = sum(len(b) for b in blocks)
    out = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i, row in enumerate(b):
            for j, x in enumerate(row):
                out[off+i][off+j] = x % p
        off += len(b)
    return tuple(x for row in out for x in row)


def jordan_nil(s):
    return [[int(j == i + 1) for j in range(s)] for i in range(s)]


def cyclic_unit_count_4x4():
    p = 2
    f = [1, 0, 1, 0, 1]  # (t^2+t+1)^2
    c = companion(f, p)
    a = tuple(x for row in c for x in row)
    check_matrix(a, 4, 2)
    units = 0
    for cs in product(range(2), repeat=4):
        matrix = poly_evaluate(cs, a, 4, p)
        if rank([matrix[i*4:(i+1)*4] for i in range(4)], p) == 4:
            units += 1
    assert units == 12, units
    print("LA21 cyclic 4x4/F2 unit centralizer = 12")


def nilpotent_2plus1_count():
    a = block_diag([jordan_nil(2), jordan_nil(1)], 3)
    check_matrix(a, 3, 3)
    assert direct_dimension(a, 3, 3) == 5
    matrix = commute_matrix(a, 3, 3)
    units = 0
    for coeffs in product(range(3), repeat=9):
        vector = [(sum(row[j] * coeffs[j] for j in range(9)) % 3)
                  for row in matrix]
        if any(vector):
            continue
        rows = [coeffs[i * 3:(i + 1) * 3] for i in range(3)]
        if rank(rows, 3) == 3:
            units += 1
    assert units == (3-1)**2 * 3**3, units
    print("LA21 nilpotent 2+1/F3 unit centralizer = 108")


def run():
    rng = Random(21021)
    for p, n, matrices in (
        (2, 2, product(range(2), repeat=4)),
        (3, 2, product(range(3), repeat=4)),
        (2, 3, product(range(2), repeat=9)),
        (3, 3, [tuple(rng.randrange(3) for _ in range(9))
                for _ in range(150)]),
    ):
        count = 0
        for a in matrices:
            check_matrix(a, n, p)
            count += 1
        print(f"LA21 commutant OK: F{p} {n}x{n}, {count} matrices")
    a = block_diag([jordan_nil(3), jordan_nil(3)], 2)
    b = block_diag([jordan_nil(3), jordan_nil(2), jordan_nil(1)], 2)
    assert direct_dimension(a, 6, 2) == 12
    assert direct_dimension(b, 6, 2) == 14
    nilpotent_2plus1_count()
    cyclic_unit_count_4x4()


if __name__ == "__main__":
    run()
