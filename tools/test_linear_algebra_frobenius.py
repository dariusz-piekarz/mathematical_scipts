"""LA19: independent Smith factors and rational canonical-form regression.

All 2x2 matrices over F2 and F3; all 3x3 over F2;
500 seeded 3x3 samples over F3. No third-party modules.
"""
from itertools import product, combinations, permutations
from random import Random


def trim(a):
    a = [x for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([( (a[i] if i < len(a) else 0) +
                   (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def neg(a, p):
    return [(-x) % p for x in a]


def mul(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] = (out[i+j]+v*w) % p
    return trim(out)


def divmod_poly(a, b, p):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        degree = len(a)-len(b)
        scalar = a[-1] * pow(b[-1], -1, p) % p
        q[degree] = scalar
        subtract = [0]*degree+[scalar*x % p for x in b]
        a = add(a, neg(subtract, p), p)
    return trim(q), a


def gcd(a, b, p):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, divmod_poly(a, b, p)[1]
    if a == [0]:
        return a
    inverse = pow(a[-1], -1, p)
    return trim([x*inverse % p for x in a])


def determinant(m, p):
    n = len(m)
    total = [0]
    for perm in permutations(range(n)):
        term = [1]
        inversions = sum(perm[i] > perm[j] for i in range(n)
                         for j in range(i+1, n))
        for i, col in enumerate(perm):
            term = mul(term, m[i][col], p)
        if inversions % 2:
            term = neg(term, p)
        total = add(total, term, p)
    return total


def smith_factors(a, n, p):
    m = [[trim([-a[n*i+j] % p, int(i == j)])
          for j in range(n)] for i in range(n)]
    divisors = [[1]]
    for k in range(1, n+1):
        d = [0]
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                sub = [[m[i][j] for j in cols] for i in rows]
                d = gcd(d, determinant(sub, p), p)
        assert d != [0]
        divisors.append(d)
    factors = []
    for k in range(1, n+1):
        q, remainder = divmod_poly(divisors[k], divisors[k-1], p)
        assert remainder == [0]
        factors.append(q)
    assert all(divmod_poly(factors[i+1], factors[i], p)[1] == [0]
               for i in range(n-1))
    return factors, divisors[-1]


def matmul(a, b, n, p):
    return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def evaluate(coeffs, a, n, p):
    ident = tuple(int(i == j) for i in range(n) for j in range(n))
    z = (0,)*(n*n)
    power = ident
    for c in coeffs:
        z = tuple((x+c*y) % p for x, y in zip(z, power))
        power = matmul(power, a, n, p)
    return z


def minimal_polynomial(a, n, p):
    for degree in range(n+1):
        for coeffs in product(range(p), repeat=degree):
            candidate = list(coeffs)+[1]
            if evaluate(candidate, a, n, p) == (0,)*(n*n):
                return list(candidate)
    raise AssertionError("Cayley-Hamilton failed")


def companion(f, p):
    n = len(f)-1
    c = [[0]*n for _ in range(n)]
    for j in range(n-1):
        c[j+1][j] = 1
    for i in range(n):
        c[i][n-1] = -f[i] % p
    return c


def frobenius(factors, p):
    fs = [f for f in factors if len(f)>1]
    n = sum(len(f)-1 for f in fs)
    a = [[0]*n for _ in range(n)]
    off = 0
    for f in fs:
        c = companion(f, p)
        d = len(c)
        for i in range(d):
            for j in range(d):
                a[off+i][off+j] = c[i][j]
        off += d
    return tuple(x for row in a for x in row)


def check(a, n, p):
    factors, characteristic = smith_factors(a, n, p)
    minimal = minimal_polynomial(a, n, p)
    prod = [1]
    for f in factors:
        prod = mul(prod, f, p)
    assert prod == characteristic
    assert factors[-1] == minimal, (a, factors, minimal)
    fs = [f for f in factors if len(f)>1]
    assert sum(len(f)-1 for f in fs) == n
    assert (len(fs) == 1) == (minimal == characteristic)
    rational = frobenius(factors, p)
    r_factors, r_char = smith_factors(rational, n, p)
    assert r_factors == factors and r_char == characteristic

    if n >= 2:
        ident = [int(i == j) for i in range(n) for j in range(n)]
        e = [0]*(n*n)
        e[1] = 1
        shear = tuple((u+v) % p for u, v in zip(ident, e))
        inverse = tuple((u-v) % p for u, v in zip(ident, e))
        conjugated = matmul(matmul(inverse, a, n, p), shear, n, p)
        assert smith_factors(conjugated, n, p)[0] == factors
    return True


def run():
    rng = Random(19019)
    stats = []
    for p, n, matrices in (
        (2, 2, list(product(range(2), repeat=4))),
        (3, 2, list(product(range(3), repeat=4))),
        (2, 3, list(product(range(2), repeat=9))),
        (3, 3, [tuple(rng.randrange(3) for _ in range(9))
                for _ in range(500)]),
    ):
        for a in matrices:
            check(a, n, p)
        stats.append((p, n, len(matrices)))
    print("LA19 Smith/Frobenius regression OK:", stats)


if __name__ == "__main__":
    run()
