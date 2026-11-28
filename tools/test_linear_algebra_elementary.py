"""LA20: independent elementary-divisor reconstruction and kernel dimensions.

Checks all 2x2 matrices over F2 and F3, all 3x3 over F2,
100 seeded 3x3 over F3, plus a nonlinear 4x4 primary block over F2.
Uses no third-party packages.
"""
from itertools import product
from random import Random

from test_linear_algebra_frobenius import (
    companion, divmod_poly, frobenius, matmul, mul, smith_factors, trim,
)


def monic_polynomials(p, degree):
    for c in product(range(p), repeat=degree):
        yield list(c) + [1]


def factor_monic(f, p):
    """Trial division by monics of increasing degree; smaller factors go first."""
    f = trim(list(f))
    assert f != [0] and f[-1] == 1
    factors = []
    degree = 1
    while len(f) > 1:
        found = False
        for candidate in monic_polynomials(p, degree):
            q, rem = divmod_poly(f, candidate, p)
            if rem == [0]:
                count = 1
                f = q
                while len(f) > 1:
                    q, rem = divmod_poly(f, candidate, p)
                    if rem != [0]:
                        break
                    f = q
                    count += 1
                factors.append((tuple(candidate), count))
                found = True
                break
        if not found:
            degree += 1
            assert degree <= len(f) - 1
        else:
            degree = 1
    return factors


def elementary(factors, p):
    """Remove Smith units and split each factor over F_p."""
    return sorted((irreducible, e)
                  for f in factors if len(f) > 1
                  for irreducible, e in factor_monic(f, p))


def rebuild(elements, p):
    grouped = {}
    for poly, exponent in elements:
        grouped.setdefault(poly, []).append(exponent)
    if not grouped:
        return []
    for exponents in grouped.values():
        exponents.sort()
    size = max(map(len, grouped.values()))
    columns = [[0] * (size - len(exponents)) + exponents
               for exponents in grouped.values()]
    factors = []
    for j in range(size):
        f = [1]
        for poly, exponents in zip(grouped, columns):
            for _ in range(exponents[j]):
                f = mul(f, poly, p)
        assert len(f) > 1
        factors.append(f)
    return factors


def poly_evaluate(f, a, n, p):
    ident = tuple(int(i == j) for i in range(n) for j in range(n))
    result = (0,) * (n * n)
    power = ident
    for c in f:
        result = tuple((x + c * y) % p for x, y in zip(result, power))
        power = matmul(power, a, n, p)
    return result


def rank(a, n, p):
    m = [[a[n * i + j] % p for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        pivot = next((k for k in range(r, n) if m[k][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][c], -1, p)
        m[r] = [inv * x % p for x in m[r]]
        for i in range(n):
            if i == r:
                continue
            fac = m[i][c]
            m[i] = [(x - fac * y) % p for x, y in zip(m[i], m[r])]
        r += 1
        if r == n:
            break
    return r


def test_matrix(a, n, p):
    smith, _ = smith_factors(a, n, p)
    elements = elementary(smith, p)
    assert rebuild(elements, p) == [f for f in smith if len(f) > 1]
    assert sum((len(q) - 1) * e for q, e in elements) == n
    ident = tuple(int(i == j) for i in range(n) for j in range(n))
    for q in sorted({q for q, _ in elements}):
        exponents = [e for poly, e in elements if poly == q]
        base = poly_evaluate(q, a, n, p)
        power = ident
        for k in range(max(exponents) + 2):
            observed = n - rank(power, n, p)
            expected = (len(q) - 1) * sum(min(k, e) for e in exponents)
            assert observed == expected, (a, p, q, k, observed, expected)
            power = matmul(power, base, n, p)


def main():
    rng = Random(20020)
    for p, n, matrices in (
        (2, 2, product(range(2), repeat=4)),
        (3, 2, product(range(3), repeat=4)),
        (2, 3, product(range(2), repeat=9)),
        (3, 3, [tuple(rng.randrange(3) for _ in range(9))
                for _ in range(100)]),
    ):
        count = 0
        for matrix in matrices:
            test_matrix(matrix, n, p)
            count += 1
        print(f"LA20 primary factors OK: F{p}, {n}x{n}: {count} matrices")
    poly = [1, 0, 1, 0, 1]  # (t^2+t+1)^2 over F2
    c = companion(poly, 2)
    a = tuple(v for row in c for v in row)
    test_matrix(a, 4, 2)
    print("LA20 nonlinear degree-2 primary block OK")


if __name__ == "__main__":
    main()
