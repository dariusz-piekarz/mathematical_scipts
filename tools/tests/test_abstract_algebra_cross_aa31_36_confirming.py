#!/usr/bin/env python3
"""AA-X03 confirming audit: exhaustive modular quartics and Frobenius.
Independent, pure-stdlib implementation (no earlier repository helpers).
Run: python tools/tests/test_abstract_algebra_cross_aa31_36_confirming.py
"""
from itertools import product

PRIMES = (2, 3, 5, 7)


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    result = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            result[i + j] = (result[i + j] + u * v) % p
    return trim(result, p)


def rem(a, b, p):
    assert b != [0]
    a = trim(a, p)
    b = trim(b, p)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        factor = a[-1] * pow(b[-1], -1, p) % p
        for i, v in enumerate(b):
            a[shift + i] = (a[shift + i] - factor * v) % p
        a = trim(a, p)
    return a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    a = trim(a, p)
    return trim([v * pow(a[-1], -1, p) for v in a], p) if a != [0] else a


def power_mod(a, n, modulus, p):
    out = [1]
    while n:
        if n & 1:
            out = rem(mul(out, a, p), modulus, p)
        a = rem(mul(a, a, p), modulus, p)
        n >>= 1
    return out


def derivative(a, p):
    return trim([i * a[i] for i in range(1, len(a))] or [0], p)


def resultant(a, b, m, n, p):
    """Formal-degree Sylvester matrix, columns in ascending power basis."""
    size = m + n
    columns = []
    for poly, count in ((a, n), (b, m)):
        for shift in range(count):
            v = [0] * size
            for i, coefficient in enumerate(poly):
                if i + shift < size:
                    v[i + shift] = coefficient % p
            columns.append(v)
    matrix = [[columns[j][i] for j in range(size)] for i in range(size)]
    det = 1
    for i in range(size):
        pivot = next((r for r in range(i, size) if matrix[r][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            det = -det
        c = matrix[i][i]
        det = det * c % p
        inverse = pow(c, -1, p)
        for r in range(i + 1, size):
            multiple = matrix[r][i] * inverse % p
            for j in range(i, size):
                matrix[r][j] = (matrix[r][j] - multiple * matrix[i][j]) % p
    return (-det if m * n % 2 else det) % p


def discriminant(f, degree, p):
    R = resultant(f, derivative(f, p), degree, degree - 1, p)
    return (-R if degree * (degree - 1) // 2 % 2 else R) % p


def quartic_resolvent(f, p):
    d, c, b, a, leading = f
    assert leading == 1
    return trim([-a*a*d-c*c+4*b*d, a*c-4*d, -b, 1], p)


def frobenius_factor_degrees(f, p):
    """Recover squarefree factor counts from deg gcd(f,X^(p^k)-X)."""
    x_power = [0, 1]
    degrees = {0: 0}
    for k in range(1, 5):
        x_power = power_mod(x_power, p, f, p)
        degrees[k] = len(gcd(f, add(x_power, [0, -1], p), p)) - 1
    d = degrees
    assert (d[2] - d[1]) % 2 == 0
    assert (d[3] - d[1]) % 3 == 0
    assert (d[4] - d[2]) % 4 == 0
    counts = (d[1], (d[2]-d[1])//2,
              (d[3]-d[1])//3, (d[4]-d[2])//4)
    assert all(v >= 0 for v in counts)
    assert sum((i+1)*v for i, v in enumerate(counts)) == 4
    return counts


def run():
    checks = 0
    stats = {}
    for p in PRIMES:
        good = bad = parity = 0
        for d, c, b, a in product(range(p), repeat=4):
            f = [d, c, b, a, 1]
            r = quartic_resolvent(f, p)
            disc = discriminant(f, 4, p)
            assert disc == discriminant(r, 3, p), (p, f, r)
            checks += 1
            is_squarefree = gcd(f, derivative(f, p), p) == [1]
            is_resolvent_squarefree = gcd(r, derivative(r, p), p) == [1]
            assert (disc != 0) == is_squarefree == is_resolvent_squarefree
            checks += 1
            if not is_squarefree:
                bad += 1
                continue
            good += 1
            counts = frobenius_factor_degrees(f, p)
            checks += 1
            if p % 2:
                character = pow(disc, (p-1)//2, p)
                sign = (-1) ** (4 - sum(counts))
                assert (1 if character == 1 else -1) == sign
                assert character in (1, p-1)
                checks += 1
                parity += 1
        stats[p] = (p**4, good, bad, parity)
    assert checks == 11478, checks
    assert stats == {
        2: (16, 8, 8, 0),
        3: (81, 54, 27, 54),
        5: (625, 500, 125, 500),
        7: (2401, 2058, 343, 2058),
    }, stats
    print(f"AA-X03 independent confirming audit: {checks}/{checks} PASS")
    for p, item in stats.items():
        print(f"F_{p}: total={item[0]}, squarefree={item[1]},"
              f" repeated={item[2]}, parity_checked={item[3]}")


if __name__ == "__main__":
    run()
