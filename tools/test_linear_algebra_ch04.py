"""LA-04 exact regression: matrix operations, basis changes and edge dimensions.

Finite fields F_2, F_3; zero-size matrices are represented by (m,n,flat)
to preserve the distinct 0-by-n and m-by-0 sizes. No dependencies.
"""
from itertools import product


def matrices(m, n, p):
    return ((m, n, x) for x in product(range(p), repeat=m*n))


def zero(m, n):
    return (m, n, (0,) * (m*n))


def ident(n):
    return (n, n, tuple(int(i == j) for i in range(n) for j in range(n)))


def mul(A, B, p):
    m, n, a = A
    n2, q, b = B
    assert n == n2
    return (m, q, tuple(sum(a[i*n+k]*b[k*q+j] for k in range(n)) % p
                        for i in range(m) for j in range(q)))


def transpose(A):
    m, n, a = A
    return (n, m, tuple(a[i*n+j] for j in range(n) for i in range(m)))


def matvec(A, x, p):
    m, n, a = A
    assert len(x) == n
    return tuple(sum(a[i*n+j]*x[j] for j in range(n)) % p for i in range(m))


def inverse(A, p):
    n, q, _ = A
    assert n == q
    for B in matrices(n, n, p):
        if mul(A, B, p) == ident(n) and mul(B, A, p) == ident(n):
            return B
    return None


def test_rectangular():
    matrix_count = fiber_count = 0
    for p in (2, 3):
        for m in range(3):
            for n in range(3):
                vs = list(product(range(p), repeat=n))
                ys = list(product(range(p), repeat=m))
                for A in matrices(m, n, p):
                    image = {matvec(A, v, p) for v in vs}
                    zeros = tuple([0]*m)
                    kernel = {v for v in vs if matvec(A, v, p) == zeros}
                    assert len(image)*len(kernel) == p**n
                    assert transpose(transpose(A)) == A
                    assert mul(ident(m), A, p) == A
                    assert mul(A, ident(n), p) == A
                    for y in ys:
                        fibers = [v for v in vs if matvec(A, v, p) == y]
                        assert len(fibers) == (len(kernel) if y in image else 0)
                        if fibers:
                            x0 = fibers[0]
                            assert set(fibers) == {
                                tuple((x0[i] + z[i]) % p for i in range(n))
                                for z in kernel
                            }
                        fiber_count += 1
                    matrix_count += 1
    return matrix_count, fiber_count


def test_inverses():
    checks = invertible = 0
    for p in (2, 3):
        for n in range(3):
            space = list(product(range(p), repeat=n))
            for A in matrices(n, n, p):
                B = inverse(A, p)
                kernel = {v for v in space if matvec(A, v, p) == tuple([0]*n)}
                assert (B is not None) == (len(kernel) == 1)
                if B is not None:
                    invertible += 1
                    assert inverse(B, p) == A
                    for v in space:
                        assert matvec(B, matvec(A, v, p), p) == v
                checks += 1
    return checks, invertible


def test_composition():
    triples = 0
    p = 2
    for m, n, q, r in product(range(3), repeat=4):
        AA = list(matrices(m, n, p))
        BB = list(matrices(n, q, p))
        CC = list(matrices(q, r, p))
        for A in AA:
            for B in BB:
                AB = mul(A, B, p)
                assert transpose(AB) == mul(transpose(B), transpose(A), p)
                for C in CC:
                    assert mul(AB, C, p) == mul(A, mul(B, C, p), p)
                    triples += 1
    return triples


def test_basis_change():
    checks = 0
    for p in (2, 3):
        # Rectangular dimensions as well as different domain/codomain bases.
        for m, n in product(range(3), repeat=2):
            all_P = [(P, inverse(P, p)) for P in matrices(n, n, p)]
            all_Q = [(Q, inverse(Q, p)) for Q in matrices(m, m, p)]
            ps = [e for e in all_P if e[1] is not None][:7]
            qs = [e for e in all_Q if e[1] is not None][:7]
            all_A = list(matrices(m, n, p))
            vectors = list(product(range(p), repeat=n))
            for A in all_A:
                for P, Pinv in ps:
                    for Q, Qinv in qs:
                        new = mul(mul(Qinv, A, p), P, p)
                        # New coordinates: [T]_(C' <- B') = Q^-1 A P.
                        for x in vectors:
                            assert matvec(Q, matvec(new, x, p), p) == matvec(A, matvec(P, x, p), p)
                        if m == n and P == Q:
                            assert new == mul(mul(Pinv, A, p), P, p)
                        checks += 1
    return checks


if __name__ == "__main__":
    mats, fibers = test_rectangular()
    invs, invyes = test_inverses()
    triples = test_composition()
    bases = test_basis_change()
    print(f"LA-04 PASS: {mats} rectangular matrices, {fibers} equation fibers, "
          f"{invs} inverse decisions ({invyes} invertible), "
          f"{triples} associativity cases, {bases} basis changes")
