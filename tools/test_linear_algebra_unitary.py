"""Deterministic complex inner-product regression tests for LA chapter 12.

No third-party dependencies. Checks polarization conventions, Hermitian
Gram matrices, Gram-Schmidt, finite-dimensional Riesz representation,
Gram determinants, Bessel inequalities and unitary matrices.
"""
from __future__ import annotations

from itertools import product
from math import cos, sin, sqrt

EPS = 1e-10
SCALARS = (0j, 1 + 0j, -1 + 0j, 1j, -1j, 1 + 1j)


def inner(u, v):
    return sum(a.conjugate() * b for a, b in zip(u, v))


def norm2(u):
    return inner(u, u).real


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def times(z, v):
    return tuple(z * a for a in v)


def close(a, b):
    return abs(a - b) <= EPS * max(1.0, abs(a), abs(b))


def gram(vectors):
    return [[inner(u, v) for v in vectors] for u in vectors]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def test_polarization():
    tested = 0
    vecs = list(product(SCALARS, repeat=2))
    for u in vecs:
        for v in vecs:
            q_u_plus_v = norm2(add(u, v))
            q_u_minus_v = norm2(sub(u, v))
            q_u_plus_iv = norm2(add(u, times(1j, v)))
            q_u_minus_iv = norm2(sub(u, times(1j, v)))
            polar = (q_u_plus_v - q_u_minus_v
                     - 1j * (q_u_plus_iv - q_u_minus_iv)) / 4
            assert close(polar, inner(u, v)), (u, v, polar, inner(u, v))
            assert close(inner(v, u), inner(u, v).conjugate())
            assert close(inner(times(1j, u), v), -1j * inner(u, v))
            assert close(inner(u, times(1j, v)), 1j * inner(u, v))
            tested += 1
    return tested


def test_gram():
    checked = 0
    vecs = list(product(SCALARS, repeat=2))
    for u in vecs:
        for v in vecs:
            g = gram((u, v))
            assert close(g[0][1], g[1][0].conjugate())
            assert close(g[0][0], norm2(u))
            assert close(g[1][1], norm2(v))
            d = det2(g)
            assert abs(d.imag) < EPS
            assert d.real >= -EPS
            # In C^2, det Gram is the squared magnitude of det[u|v].
            volume = u[0] * v[1] - u[1] * v[0]
            assert close(d, abs(volume) ** 2), (u, v, d, volume)
            checked += 1
    return checked


def orthonormalize(vectors):
    out = []
    for v in vectors:
        residual = v
        for e in out:
            residual = sub(residual, times(inner(e, v), e))
        length = sqrt(norm2(residual))
        if length < EPS:
            return None
        out.append(times(1 / length, residual))
    return out


def test_gram_schmidt():
    checked = 0
    vecs = list(product(SCALARS, repeat=2))
    for u in vecs:
        for v in vecs:
            es = orthonormalize((u, v))
            if es is None:
                continue
            e1, e2 = es
            assert close(inner(e1, e1), 1)
            assert close(inner(e2, e2), 1)
            assert close(inner(e1, e2), 0)
            assert close(inner(e2, e1), 0)
            # Every new vector lies in the span of the initial pair.
            assert close(norm2(e1), 1)
            assert close(norm2(e2), 1)
            checked += 1
    return checked


def test_riesz_and_bessel():
    checked = 0
    for coefficients in product(SCALARS, repeat=2):
        representing = tuple(z.conjugate() for z in coefficients)
        for vector in product(SCALARS, repeat=2):
            f = sum(c * x for c, x in zip(coefficients, vector))
            assert close(inner(representing, vector), f)
            for e in ((1 + 0j, 0j), (0j, 1 + 0j)):
                assert abs(inner(e, vector)) ** 2 <= norm2(vector) + EPS
            assert close(
                abs(inner((1 + 0j, 0j), vector)) ** 2
                + abs(inner((0j, 1 + 0j), vector)) ** 2,
                norm2(vector)
            )
            checked += 1
    return checked


def matvec(a, v):
    return tuple(sum(row[j] * v[j] for j in range(len(v))) for row in a)


def adjoint(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def matmul(a, b):
    return [[sum(a[i][j] * b[j][k] for j in range(len(b)))
             for k in range(len(b[0]))]
            for i in range(len(a))]


def test_unitary():
    checked = 0
    vectors = list(product(SCALARS, repeat=2))
    # A standard 2x2 unitary family of non-real matrices.
    for theta in (0.0, 0.2, 0.5, 1.0, 1.9, 3.14):
        for phi in (0.0, 0.4, 1.1, 2.7):
            a = complex(cos(theta), 0.0)
            b = complex(sin(theta) * cos(phi), sin(theta) * sin(phi))
            u = [[a, b], [-b.conjugate(), a.conjugate()]]
            p = matmul(adjoint(u), u)
            for i in range(2):
                for j in range(2):
                    assert close(p[i][j], int(i == j))
            assert close(abs(det2(u)), 1)
            for v in vectors:
                uv = matvec(u, v)
                assert close(norm2(uv), norm2(v))
                checked += 1
    return checked


def main():
    results = [
        test_polarization(), test_gram(), test_gram_schmidt(),
        test_riesz_and_bessel(), test_unitary()
    ]
    print(
        "Unitary chapter regression tests OK: "
        f"{results[0]} polarization; {results[1]} Gram determinants; "
        f"{results[2]} Gram-Schmidt; {results[3]} Riesz/Bessel; "
        f"{results[4]} unitary norm checks."
    )


if __name__ == "__main__":
    main()
