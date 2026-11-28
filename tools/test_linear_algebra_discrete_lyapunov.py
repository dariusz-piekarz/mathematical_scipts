"""LA23: Stein spectral criterion and discrete Lyapunov, exact regressions."""
from fractions import Fraction as F
from itertools import product
from random import Random

from test_linear_algebra_frobenius import smith_factors, gcd


def rank(rows, p):
    a = [[int(x) % p for x in row] for row in rows]
    if not a:
        return 0
    n, m = len(a), len(a[0])
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(n):
            if i != r:
                scale = a[i][col]
                a[i] = [(x - scale*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def mm(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)]
            for row in a]


def tr(a):
    return [list(x) for x in zip(*a)]


def flat(a):
    return [x for row in a for x in row]


def stein_matrix(a, n, p):
    matrix = [list(a[n*i:n*(i+1)]) for i in range(n)]
    at = tr(matrix)
    columns = []
    for i in range(n):
        for j in range(n):
            e = [[int(k == i and l == j) for l in range(n)]
                 for k in range(n)]
            transformed = mm(mm(at,e),matrix)
            columns.append([(x-y)%p for x,y in zip(flat(transformed),flat(e))])
    return [list(x) for x in zip(*columns)]


def invertible_by_reciprocal(a, n, p):
    char = smith_factors(a, n, p)[1]  # low-to-high coefficients
    reciprocal = char[::-1]  # t^n chi(1/t), also for singular A
    return gcd(char, reciprocal, p) == [1]


def test_spectrum():
    rng = Random(23023)
    cases = [
        (2, 2, product(range(2), repeat=4)),
        (3, 2, product(range(3), repeat=4)),
        (2, 3, product(range(2), repeat=9)),
        (3, 3, [tuple(rng.randrange(3) for _ in range(9))
                for _ in range(160)]),
    ]
    for p, n, matrices in cases:
        total = unique = 0
        for a in matrices:
            rank_condition = rank(stein_matrix(a,n,p),p) == n*n
            characteristic_condition = invertible_by_reciprocal(a,n,p)
            assert rank_condition == characteristic_condition, (p,n,a)
            total += 1
            unique += rank_condition
        print(f"LA23 Stein spectral F{p} {n}x{n}: "
              f"{total} matrices, {unique} unique")


def check_stein(a,p,q):
    out=mm(mm(tr(a),p),a)
    assert all(out[i][j]-p[i][j] == -q[i][j]
               for i in range(len(a)) for j in range(len(a)))


def test_exact_examples():
    ident=[[F(1),F(0)],[F(0),F(1)]]
    a=[[F(1,2),F(1,2)],[F(0),F(1,4)]]
    p=[[F(4,3),F(8,21)],[F(8,21),F(32,21)]]
    check_stein(a,p,ident)
    assert p[0][0]*p[1][1]-p[0][1]*p[1][0]==F(832,441)
    assert p[1][1]-p[0][1]**2/p[0][0]==F(208,147)

    a=[[F(0),F(1)],[F(0),F(0)]]
    p=[[F(1),F(0)],[F(0),F(2)]]
    check_stein(a,p,ident)

    a=[[F(2),F(0)],[F(0),F(1,3)]]
    p=[[F(-1,3),F(0)],[F(0),F(9,8)]]
    check_stein(a,p,ident)
    assert p[0][0]<0

    a=[[F(2),F(0)],[F(0),F(1,2)]]
    for v in [F(-3),F(0),F(5,7)]:
        p=[[F(-1,3),v],[v,F(4,3)]]
        check_stein(a,p,ident)

    for a0 in [F(0),F(1,2),F(-1,3),F(3,4)]:
        for q0 in [F(1),F(5,2)]:
            p0=q0/(1-a0*a0)
            assert a0*a0*p0-p0==-q0 and p0>0
    print("LA23 exact nilpotent, nonnormal, unstable and scalar examples OK")


def test_energy():
    a=[[F(1,2),F(1,2)],[F(0),F(1,4)]]
    p=[[F(4,3),F(8,21)],[F(8,21),F(32,21)]]
    q=[[F(1),F(0)],[F(0),F(1)]]
    x=[[F(2)],[F(-1)]]
    for k in range(12):
        energy=mm(mm(tr(x),p),x)[0][0]
        loss=mm(mm(tr(x),q),x)[0][0]
        nx=mm(a,x)
        after=mm(mm(tr(nx),p),nx)[0][0]
        assert after-energy==-loss and after>=0, k
        x=nx
    print("LA23 12 exact energy steps OK")


if __name__=="__main__":
    test_spectrum()
    test_exact_examples()
    test_energy()
