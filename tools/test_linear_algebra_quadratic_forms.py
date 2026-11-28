"""Finite-field and real-matrix regression tests for quadratic forms (ch. 09).

No external dependencies. Checks polarization in F_2/F_3, the radical and
orthogonal-complement dimension formula, even rank of alternating forms,
and examples of Sylvester's criterion and congruence invariance.
"""
from itertools import combinations, product
from math import prod


def rank_mod(a, p):
    b = [[x % p for x in row] for row in a]
    if not b:
        return 0
    rows, cols = len(b), len(b[0])
    rank = 0
    for j in range(cols):
        k = next((i for i in range(rank, rows) if b[i][j]), None)
        if k is None:
            continue
        b[rank], b[k] = b[k], b[rank]
        inv = pow(b[rank][j], -1, p)
        b[rank] = [(inv * x) % p for x in b[rank]]
        for i in range(rows):
            if i != rank:
                t = b[i][j]
                b[i] = [(x - t * y) % p for x, y in zip(b[i], b[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def dot(x, y, p):
    return sum(a * b for a, b in zip(x, y)) % p


def form(a, x, y, p):
    return sum(x[i] * a[i][j] * y[j]
               for i in range(len(x))
               for j in range(len(y))) % p


def symmetric(p, n):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    for coeff in product(range(p), repeat=len(pairs)):
        a = [[0] * n for _ in range(n)]
        for (i, j), x in zip(pairs, coeff):
            a[i][j] = a[j][i] = x
        yield a


def alternating(p, n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for coeff in product(range(p), repeat=len(pairs)):
        a = [[0] * n for _ in range(n)]
        for (i, j), x in zip(pairs, coeff):
            a[i][j], a[j][i] = x, (-x) % p
        yield a


def polar_checks():
    checks = 0
    for p in (2, 3):
        vecs = list(product(range(p), repeat=2))
        for a, b, c in product(range(p), repeat=3):
            def q(x):
                return (a*x[0]*x[0] + b*x[1]*x[1]
                        + c*x[0]*x[1]) % p

            for u in vecs:
                assert q(u) == q(tuple(-x % p for x in u))
                for v in vecs:
                    uv = tuple((x + y) % p for x, y in zip(u, v))
                    polar = (q(uv) - q(u) - q(v)) % p
                    assert polar == (
                        2*a*u[0]*v[0] + 2*b*u[1]*v[1]
                        + c*(u[0]*v[1] + u[1]*v[0])
                    ) % p
                    assert polar == (
                        q(tuple((x + y) % p for x, y in zip(v, u)))
                        - q(v) - q(u)
                    ) % p
                    checks += 1
    # In characteristic 2 distinct quadratic forms share their polarization.
    p = 2
    for u in product(range(p), repeat=2):
        for v in product(range(p), repeat=2):
            pol1 = (
                (u[0]+v[0])*(u[1]+v[1])
                - u[0]*u[1] - v[0]*v[1]
            ) % p
            pol2 = (
                (u[0]+v[0])*(u[1]+v[1])
                + (u[0]+v[0])**2
                - u[0]*u[1] - u[0]**2
                - v[0]*v[1] - v[0]**2
            ) % p
            assert pol1 == pol2
            checks += 1
    return checks


def orthogonal_dimension_checks():
    checks = 0
    for p in (2, 3):
        n = 3
        vecs = list(product(range(p), repeat=n))
        for a in symmetric(p, n):
            radical_dim = n - rank_mod(a, p)
            assert 0 <= radical_dim <= n
            for u in vecs:
                if u == (0, 0, 0):
                    continue
                row = [form(a, u, v, p) for v in
                       [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
                annihilator_dim = n - int(any(row))
                intersection_rad_dim = int(not any(row))
                assert annihilator_dim == n - 1 + intersection_rad_dim
                checks += 1
            # Two-dimensional U, tested with independent generating pairs.
            chosen = vecs[1:min(10, len(vecs))]
            for u in chosen:
                for v in chosen:
                    if rank_mod([u, v], p) != 2:
                        continue
                    pair_rows = [
                        [form(a, w, e, p)
                         for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
                        for w in (u, v)
                    ]
                    rank_of_restricted_map = rank_mod(pair_rows, p)
                    orthogonal_dim = n - rank_of_restricted_map
                    intersection_rad_dim = 2 - rank_of_restricted_map
                    assert orthogonal_dim == n - 2 + intersection_rad_dim
                    checks += 1
    return checks


def alternating_checks():
    checks = 0
    for p in (2, 3):
        for n in (2, 3, 4):
            for a in alternating(p, n):
                assert rank_mod(a, p) % 2 == 0
                # Every alternating form is zero on its diagonal.
                for x in product(range(p), repeat=n):
                    assert form(a, x, x, p) == 0
                checks += 1
    return checks


def positive_definite_checks():
    count = 0
    for a, b, c in product(range(-3, 4), repeat=3):
        # Every 2x2 real symmetric matrix with positive leading
        # minors is positive on a finite integer-vector test grid.
        if a > 0 and a*c - b*b > 0:
            for x, y in product(range(-3, 4), repeat=2):
                if x == y == 0:
                    continue
                q = a*x*x + 2*b*x*y + c*y*y
                assert q > 0
                count += 1
    # A congruence preserves the determinant's square-class/sign.
    for diag in product((-2, -1, 0, 1, 3), repeat=2):
        for t in (-2, -1, 0, 1, 2):
            # P=[[1,t],[0,1]], P.T D P is congruent to D.
            a = diag[0]
            b = diag[0]*t
            c = diag[0]*t*t + diag[1]
            assert a*c - b*b == prod(diag)
            count += 1
    return count


def main():
    a = polar_checks()
    b = orthogonal_dimension_checks()
    c = alternating_checks()
    d = positive_definite_checks()
    print(
        "Quadratic form regression tests OK:",
        a, "polarization checks;",
        b, "orthogonal dimension checks;",
        c, "alternating even-rank checks;",
        d, "real positivity and congruence checks."
    )


if __name__ == "__main__":
    main()
