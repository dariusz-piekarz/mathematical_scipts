"""Exhaustive finite-field regression for LA-05: Gaussian elimination and RREF.

Exact arithmetic: all matrices <=3x3 over F_2 and <=2x3 over F_3,
including zero-size cases. No third-party dependencies.
"""
from itertools import product


def mats(m, n, p):
    for entries in product(range(p), repeat=m*n):
        yield tuple(tuple(entries[i*n:(i+1)*n]) for i in range(m))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matmul(A, B, ninner, nout, p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(ninner)) % p
                       for j in range(nout)) for i in range(len(A)))


def vec(A, x, p):
    return tuple(sum(a*b for a, b in zip(row, x)) % p for row in A)


def span(vectors, ambient, p):
    z = (0,) * ambient
    out = {z}
    for v in vectors:
        out = {tuple((x[i]+a*v[i]) % p for i in range(ambient))
               for x in out for a in range(p)}
    return frozenset(out)


def rref(A, m, n, p, choose_last=False):
    """Return RREF, pivot columns and accumulated left row multiplier P."""
    R = [list(row) for row in A]
    E = [list(row) for row in identity(m)]
    pivots = []
    target = 0
    for j in range(n):
        candidates = [i for i in range(target, m) if R[i][j] % p != 0]
        if not candidates:
            continue
        k = candidates[-1] if choose_last else candidates[0]
        R[target], R[k] = R[k], R[target]
        E[target], E[k] = E[k], E[target]
        inv = next(a for a in range(1, p) if a*R[target][j] % p == 1)
        R[target] = [(inv*v) % p for v in R[target]]
        E[target] = [(inv*v) % p for v in E[target]]
        for i in range(m):
            if i == target:
                continue
            factor = R[i][j]
            R[i] = [(x-factor*y) % p for x, y in zip(R[i], R[target])]
            E[i] = [(x-factor*y) % p for x, y in zip(E[i], E[target])]
        pivots.append(j)
        target += 1
        if target == m:
            break
    return tuple(map(tuple, R)), tuple(pivots), tuple(map(tuple, E))


def matrix_col(A, j):
    return tuple(row[j] for row in A)


def check(m, n, p):
    allx = list(product(range(p), repeat=n))
    allb = list(product(range(p), repeat=m))
    zeros = (0,) * m
    matrices = equations = colchecks = kernelchecks = 0
    for A in mats(m, n, p):
        R, piv, P = rref(A, m, n, p)
        R2, piv2, P2 = rref(A, m, n, p, choose_last=True)
        assert R == R2 and piv == piv2, (p, m, n, A, R, R2)
        assert R == matmul(P, A, m, n, p)
        assert R2 == matmul(P2, A, m, n, p)
        if m:
            assert len(rref(P, m, m, p)[1]) == m
        rank = len(piv)
        image = frozenset(vec(A, x, p) for x in allx)
        ker = frozenset(x for x in allx if vec(A, x, p) == zeros)
        assert len(ker) == p ** (n-rank)
        assert len(image) == p ** rank
        assert len(image) * len(ker) == p ** n

        # Use columns from the ORIGINAL matrix (not columns of RREF).
        pivcols = [matrix_col(A, j) for j in piv]
        assert span(pivcols, m, p) == image
        assert len(span(pivcols, m, p)) == p ** len(pivcols)
        colchecks += 1

        free = [j for j in range(n) if j not in piv]
        basis = []
        for f in free:
            v = [0] * n
            v[f] = 1
            for i, j in enumerate(piv):
                v[j] = (-R[i][f]) % p
            assert vec(A, v, p) == zeros
            basis.append(tuple(v))
        assert span(basis, n, p) == ker
        assert len(basis) == n-rank
        kernelchecks += 1

        # Solve every right-hand side; check rank, pivot row contradiction,
        # and the solution coset x0+ker(A).
        for b in allb:
            sols = {x for x in allx if vec(A, x, p) == b}
            Aug = tuple(tuple(list(A[i]) + [b[i]]) for i in range(m))
            AugR, augp, _ = rref(Aug, m, n+1, p)
            contradiction = any(
                all(row[j] == 0 for j in range(n)) and row[n] != 0
                for row in AugR
            )
            assert bool(sols) == (len(augp) == rank) == (not contradiction)
            if sols:
                x0 = next(iter(sols))
                assert sols == {
                    tuple((x0[j]+k[j]) % p for j in range(n)) for k in ker
                }
                assert len(sols) == len(ker)
            equations += 1

        # Elementary row operations must preserve RREF.
        if m > 1:
            swapped = list(A)
            swapped[0], swapped[-1] = swapped[-1], swapped[0]
            assert rref(swapped, m, n, p)[0] == R
            added = list(map(list, A))
            added[0] = [(added[0][j]+added[1][j]) % p for j in range(n)]
            assert rref(added, m, n, p)[0] == R
        if m > 0 and p > 2:
            scaled = list(map(list, A))
            scaled[0] = [2*a % p for a in scaled[0]]
            assert rref(scaled, m, n, p)[0] == R

        if m == n:
            # Gauss-Jordan inversion of [A | I_n].
            Aug = tuple(tuple(A[i]) + tuple(identity(n)[i])
                        for i in range(n))
            RA, _, _ = rref(Aug, n, 2*n, p)
            left = tuple(tuple(row[:n]) for row in RA)
            if rank == n:
                assert left == identity(n)
                Inv = tuple(tuple(row[n:]) for row in RA)
                assert matmul(A, Inv, n, n, p) == identity(n)
                assert matmul(Inv, A, n, n, p) == identity(n)
            else:
                assert left != identity(n)
        matrices += 1
    return matrices, equations, colchecks, kernelchecks


if __name__ == "__main__":
    results = []
    for p, maxm, maxn in ((2, 3, 3), (3, 2, 3)):
        for m in range(maxm+1):
            for n in range(maxn+1):
                results.append(check(m, n, p))
    totals = [sum(r[i] for r in results) for i in range(4)]
    print("LA-05 PASS: matrices=%d systems=%d original-pivot-column-bases=%d kernel-bases=%d" % tuple(totals))
