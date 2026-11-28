"""Finite-field regression for LA chapter 16 (no third-party packages).

Exhaustive 2x2 matrices over F2 and F3: Cayley-Hamilton, minimal
polynomial divisibility, diagonalizability criterion, invariant lines,
and a cyclic-vector test including Jordan blocks.
"""
from itertools import product


def ident(p):
    return (1 % p, 0, 0, 1 % p)


def zero():
    return (0, 0, 0, 0)


def add(a, b, p):
    return tuple((x + y) % p for x, y in zip(a, b))


def mul(a, b, p):
    return tuple(sum(a[2 * i + k] * b[2 * k + j]
                     for k in range(2)) % p
                 for i in range(2) for j in range(2))


def scale(c, a, p):
    return tuple(c * x % p for x in a)


def evaluate(coeffs, a, p):
    """Coefficients are in increasing degree."""
    total = zero()
    power = ident(p)
    for coeff in coeffs:
        total = add(total, scale(coeff, power, p), p)
        power = mul(power, a, p)
    return total


def matvec(a, v, p):
    return ((a[0] * v[0] + a[1] * v[1]) % p,
            (a[2] * v[0] + a[3] * v[1]) % p)


def independent(v, w, p):
    return (v[0] * w[1] - v[1] * w[0]) % p != 0


def minpoly(a, p):
    for d in range(0, 3):
        for coeffs in product(range(p), repeat=d):
            poly = (*coeffs, 1)
            if evaluate(poly, a, p) == zero():
                return poly
    raise AssertionError("Cayley-Hamilton bound failed")


def divides(f, g, p):
    """Polynomials in increasing degree; f monic."""
    rem = list(g)
    while len(rem) >= len(f):
        c = rem[-1]
        shift = len(rem) - len(f)
        for j, a in enumerate(f):
            rem[shift + j] = (rem[shift + j] - c * a) % p
        while rem and rem[-1] == 0:
            rem.pop()
    return not rem


def eigenspace_vectors(a, p):
    vectors = [v for v in product(range(p), repeat=2) if v != (0, 0)]
    eigen = {}
    for lam in range(p):
        eigen[lam] = [v for v in vectors if matvec(a, v, p) ==
                      tuple(lam * x % p for x in v)]
    return eigen


def run():
    checked = 0
    cyclic = 0
    diagonal = 0
    line_factors = 0
    for p in (2, 3):
        for a in product(range(p), repeat=4):
            tr = (a[0] + a[3]) % p
            det = (a[0] * a[3] - a[1] * a[2]) % p
            chi = (det, -tr % p, 1)
            assert evaluate(chi, a, p) == zero(), (p, a)
            m = minpoly(a, p)
            assert divides(m, chi, p), (p, a, m, chi)
            assert not any(
                evaluate((*cs, 1), a, p) == zero()
                for d in range(len(m) - 1)
                for cs in product(range(p), repeat=d)
            )
            eigen = eigenspace_vectors(a, p)
            shared = [v for group in eigen.values() for v in group]
            diagonalizable = any(independent(v, w, p)
                                 for v in shared for w in shared)
            roots = [lam for lam in range(p)
                     if sum(m[i] * pow(lam, i, p)
                            for i in range(len(m))) % p == 0]
            distinct_linear = len(roots) == len(m) - 1
            assert diagonalizable == distinct_linear, (p, a, m, eigen)
            diagonal += diagonalizable
            for group in eigen.values():
                for v in group:
                    # Eigenline is invariant, and its quotient has
                    # eigenvalue tr - lambda.
                    lam = next(k for k, ws in eigen.items() if v in ws)
                    mu = (tr - lam) % p
                    assert (lam * mu) % p == det
                    line_factors += 1
            vectors = [v for v in product(range(p), repeat=2)
                       if v != (0, 0)]
            for v in vectors:
                if independent(v, matvec(a, v, p), p):
                    cyclic += 1
                    assert len(m) == 3
            checked += 1
    print("LA16 finite-field checks OK:",
          checked, "matrices;",
          diagonal, "diagonalizable matrices;",
          line_factors, "invariant eigenlines;",
          cyclic, "cyclic vectors.")


if __name__ == "__main__":
    run()
