"""Independent LA-16 regression: characteristic/minimal polynomials in F2 and F3.

Exhausts all 512 matrices of size 3 over F2 and checks 500 seeded matrices
over F3. Checks Cayley-Hamilton, m_T | chi_T, the split squarefree
criterion, generalized eigenspace dimensions, and cyclic companions.
Only the Python standard library is used.
"""
from itertools import product
from random import Random


def multiply(a, b, p, n):
    return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def evaluate(coeffs, a, p, n):
    z = (0,) * (n*n)
    identity = tuple(int(i == j) for i in range(n) for j in range(n))
    power = identity
    for scalar in coeffs:
        z = tuple((x + scalar*y) % p for x, y in zip(z, power))
        power = multiply(power, a, p, n)
    return z


def minimal_polynomial(a, p, n):
    for degree in range(n+1):
        for coeffs in product(range(p), repeat=degree):
            candidate = (*coeffs, 1)
            if evaluate(candidate, a, p, n) == (0,) * (n*n):
                return candidate
    raise AssertionError("No annihilating polynomial of degree <= n")


def divides(monic, poly, p):
    remainder = list(poly)
    while len(remainder) >= len(monic):
        shift, factor = len(remainder)-len(monic), remainder[-1]
        for j, value in enumerate(monic):
            remainder[shift+j] = (remainder[shift+j]-factor*value) % p
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return not remainder


def characteristic_3(a, p):
    trace = a[0] + a[4] + a[8]
    second = (a[0]*a[4]-a[1]*a[3] + a[0]*a[8]-a[2]*a[6]
              + a[4]*a[8]-a[5]*a[7])
    determinant = (a[0]*(a[4]*a[8]-a[5]*a[7])
                   - a[1]*(a[3]*a[8]-a[5]*a[6])
                   + a[2]*(a[3]*a[7]-a[4]*a[6]))
    return tuple(x % p for x in (-determinant, second, -trace, 1))


def rank_mod(vectors, p):
    rows = [list(v) for v in vectors if any(v)]
    if not rows:
        return 0
    nrows, ncols = len(rows), len(rows[0])
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows)
                      if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][col], -1, p)
        rows[rank] = [v*inverse % p for v in rows[rank]]
        for i in range(nrows):
            if i != rank:
                factor = rows[i][col]
                rows[i] = [(x-factor*y) % p
                           for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == ncols:
            break
    return rank


def matvec(a, v, p, n):
    return tuple(sum(a[n*i+j]*v[j] for j in range(n)) % p
                 for i in range(n))


def check_3(a, p):
    char = characteristic_3(a, p)
    assert evaluate(char, a, p, 3) == (0,) * 9
    minimal = minimal_polynomial(a, p, 3)
    assert divides(minimal, char, p), (a, p, minimal, char)

    roots = [value for value in range(p)
             if sum(minimal[i]*pow(value, i, p)
                    for i in range(len(minimal))) % p == 0]
    vectors = [v for v in product(range(p), repeat=3) if any(v)]
    eigenvectors = [v for v in vectors
                    if any(matvec(a, v, p, 3) ==
                           tuple(value*x % p for x in v)
                           for value in range(p))]
    diagonalizable = rank_mod(eigenvectors, p) == 3
    split_distinct = len(roots) == len(minimal)-1
    assert diagonalizable == split_distinct, (a, p, minimal)

    if split_distinct:
        dimensions = []
        for value in roots:
            shifted = tuple((a[3*i+j]-(value if i == j else 0)) % p
                            for i in range(3) for j in range(3))
            third = multiply(multiply(shifted, shifted, p, 3),
                             shifted, p, 3)
            rows = [third[3*i:3*i+3] for i in range(3)]
            dimensions.append(3-rank_mod(rows, p))
        assert sum(dimensions) == 3, (a, p, dimensions)
    return diagonalizable


def check_companions():
    checked = 0
    for p in (2, 3):
        for degree in (1, 2, 3):
            for coeffs in product(range(p), repeat=degree):
                companion = [0] * (degree*degree)
                for j in range(degree-1):
                    companion[degree*(j+1)+j] = 1
                for i in range(degree):
                    companion[degree*i+degree-1] = -coeffs[i] % p
                minimal = minimal_polynomial(tuple(companion), p, degree)
                assert minimal == (*coeffs, 1), (p, coeffs, minimal)
                checked += 1
    return checked


def run():
    rng = Random(1602)
    f2 = list(product(range(2), repeat=9))
    f3 = [tuple(rng.randrange(3) for _ in range(9))
          for _ in range(500)]
    d2 = sum(check_3(a, 2) for a in f2)
    d3 = sum(check_3(a, 3) for a in f3)
    companions = check_companions()
    print("LA16 3x3 regression OK:", len(f2), "F2 cases,",
          len(f3), "F3 cases,", d2+d3, "diagonalizable;",
          companions, "cyclic companion matrices.")


if __name__ == "__main__":
    run()
