"""Regression for LA chapter 17: Jordan block sizes and uniqueness.

Checks block sums of dimensions 1-4 over F2/F3, conjugacy
invariance of the kernel growth, characteristic annihilation,
minimal annihilating exponent per eigenvalue, and the diagonalizable case.
No nonstandard dependencies.
"""
from itertools import product
from random import Random


def eye(n, p):
    return [[int(i == j) % p for j in range(n)] for i in range(n)]


def multiply(a, b, p):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) % p
             for j in range(n)] for i in range(n)]


def rank(a, p):
    rows = [row[:] for row in a]
    n, m = len(rows), len(rows[0])
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][col], -1, p)
        rows[r] = [x*inv % p for x in rows[r]]
        for i in range(n):
            if i != r:
                factor = rows[i][col]
                rows[i] = [(x-factor*y) % p
                           for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == n:
            break
    return r


def invert(a, p):
    n = len(a)
    mat = [a[i][:]+eye(n, p)[i] for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if mat[i][col] % p), None)
        if pivot is None:
            return None
        mat[col], mat[pivot] = mat[pivot], mat[col]
        inverse = pow(mat[col][col], -1, p)
        mat[col] = [x*inverse % p for x in mat[col]]
        for i in range(n):
            if i != col:
                factor = mat[i][col]
                mat[i] = [(x-factor*y) % p
                          for x, y in zip(mat[i], mat[col])]
    return [row[n:] for row in mat]


def jordan(blocks, p):
    n = sum(s for s, _ in blocks)
    a = [[0]*n for _ in range(n)]
    offset = 0
    for s, lam in blocks:
        for i in range(s):
            a[offset+i][offset+i] = lam % p
            if i+1 < s:
                a[offset+i][offset+i+1] = 1
        offset += s
    return a


def d_at(a, lam, k, p):
    n = len(a)
    shifted = [[(a[i][j] - (lam if i == j else 0)) % p
                for j in range(n)] for i in range(n)]
    power = eye(n, p)
    for _ in range(k):
        power = multiply(power, shifted, p)
    return n-rank(power, p)


def check(blocks, p, rng):
    j = jordan(blocks, p)
    n = len(j)
    pmat = None
    pinv = None
    while pinv is None:
        pmat = [[rng.randrange(p) for _ in range(n)] for _ in range(n)]
        pinv = invert(pmat, p)
    a = multiply(multiply(pmat, j, p), pinv, p)
    for lam in range(p):
        dims = [d_at(a, lam, k, p) for k in range(n+2)]
        assert dims[0] == 0
        for k in range(1, n+1):
            assert dims[k] >= dims[k-1]
            count_exact = 2*dims[k]-dims[k-1]-dims[k+1]
            assert count_exact == sum(s == k and value == lam
                                      for s, value in blocks), (
                p, blocks, lam, k, count_exact
            )
        assert dims[-1] == sum(s for s, value in blocks if value == lam)
        assert dims[1] == sum(value == lam for s, value in blocks)
    # The maximal block for lambda is the exponent in m_T.
    for lam in range(p):
        highest = max((s for s, value in blocks if value == lam), default=0)
        if highest:
            assert d_at(a, lam, highest, p) == sum(
                s for s, value in blocks if value == lam)
    return True


def partitions(n, maximum=None):
    if maximum is None:
        maximum = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maximum), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,)+tail


def run():
    rng = Random(17017)
    count = 0
    for p in (2, 3):
        for n in (1, 2, 3, 4):
            for sizes in partitions(n):
                for lambdas in product(range(p), repeat=len(sizes)):
                    blocks = tuple(zip(sizes, lambdas))
                    for _ in range(3):
                        check(blocks, p, rng)
                        count += 1
    print("LA17 Jordan regression OK:", count,
          "independent conjugated block sums in F2/F3")


if __name__ == "__main__":
    run()
