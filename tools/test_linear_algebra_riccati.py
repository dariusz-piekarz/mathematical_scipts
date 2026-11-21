"""LA24 independent rational checks of continuous/discrete Riccati identities.

Uses Fraction only (no NumPy/SymPy). Checks DARE/CARE residuals,
finite-horizon recursion, square completion, feedback identities,
non-normal two-state examples and scalar nonstabilizing roots.
"""
from fractions import Fraction as F
from math import exp, isclose
from random import Random


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(row, other)] for row, other in zip(a, b)]


def neg(a):
    return [[-x for x in row] for row in a]


def sub(a, b):
    return add(a, neg(b))


def inv(a):
    n = len(a)
    aug = [row[:] + identity for row, identity in zip(a, eye(n))]
    for j in range(n):
        k = next((i for i in range(j, n) if aug[i][j] != 0), None)
        assert k is not None, "inversion requires nonsingular matrix"
        aug[j], aug[k] = aug[k], aug[j]
        scale = aug[j][j]
        aug[j] = [x/scale for x in aug[j]]
        for i in range(n):
            if i == j:
                continue
            t = aug[i][j]
            aug[i] = [x-t*y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def sq(z, m):
    return mm(mm(tr(z), m), z)[0][0]


def riccati_dare_rhs(a, b, q, r, p):
    m = add(r, mm(mm(tr(b), p), b))
    gain = mm(inv(m), mm(mm(tr(b), p), a))
    rhs = sub(add(q, mm(mm(tr(a), p), a)),
              mm(mm(mm(tr(a), p), b), gain))
    return rhs, gain, m


def riccati_care_lhs(a, b, q, r, p):
    return add(sub(add(mm(tr(a), p), mm(p, a)),
                   mm(mm(mm(mm(p, b), inv(r)), tr(b)), p)), q)


def closed_loop(a, b, k):
    return sub(a, mm(b, k))


def test_discrete_scalar():
    a, q, r = F(1, 2), F(7, 8), F(1)
    p = F(0)
    vals = [p]
    for _ in range(18):
        p = q + a*a*p - a*a*p*p/(r+p)
        vals.append(p)
    assert vals[1] == F(7, 8)
    assert vals[2] == F(119, 120)
    assert all(vals[i] <= vals[i+1] <= 1 for i in range(len(vals)-1))
    assert abs(float(vals[-1] - 1)) < 1.e-11
    assert 8*F(1)**2 - F(1) - 7 == 0
    assert 8*F(-7, 8)**2 - F(-7, 8) - 7 == 0
    assert a - (F(1)/(1+F(1)))*F(1)*a == F(1, 4)
    assert a - (F(1)/(1+F(-7, 8)))*F(-7, 8)*a == 4
    print("LA24 DARE scalar recursion/branches OK")


def test_continuous_scalar():
    assert -2*F(1)-F(1)**2+3 == 0
    assert -2*F(-3)-F(-3)**2+3 == 0
    for t in [0., .1, .5, 1., 2., 4.]:
        z=exp(-4*t)
        p=3*(1-z)/(3+z)
        derivative=48*z/(3+z)**2
        rhs=3-2*p-p*p
        assert isclose(derivative, rhs, rel_tol=1.e-13, abs_tol=1.e-13)
        assert 0 <= p < 1
    print("LA24 continuous scalar differential Riccati identity OK")


def test_discrete_matrix():
    a = matrix([[F(1,2),F(1,2)],[0,F(1,4)]])
    b = eye(2)
    r = eye(2)
    p = eye(2)
    q = matrix([[F(7,8), F(-1,8)],
                [F(-1,8), F(27,32)]])
    rhs, k, m = riccati_dare_rhs(a,b,q,r,p)
    assert rhs == p
    assert k == [[x/2 for x in row] for row in a]
    assert m == matrix([[2,0],[0,2]])
    ac = closed_loop(a,b,k)
    assert ac == [[x/2 for x in row] for row in a]
    assert sub(p, mm(mm(tr(ac),p),ac)) == add(q,mm(mm(tr(k),r),k))
    # complete square for many exact x, u
    rng=Random(24024)
    for _ in range(120):
        x=matrix([[rng.randint(-4,4)],[rng.randint(-4,4)]])
        u=matrix([[rng.randint(-3,3)],[rng.randint(-3,3)]])
        nx=add(mm(a,x),mm(b,u))
        left=sq(x,q)+sq(u,r)+sq(nx,p)-sq(x,p)
        right=sq(add(u,mm(k,x)),m)
        assert left == right, (x,u,left,right)
    assert q[0][0]>0 and q[0][0]*q[1][1]-q[0][1]**2>0
    print("LA24 nonnormal discrete matrix, square completion and feedback OK")


def test_continuous_matrix():
    a=matrix([[-1,F(1,3)],[0,-2]])
    b=eye(2)
    r=eye(2)
    p=eye(2)
    q=matrix([[3,F(-1,3)],[F(-1,3),5]])
    assert riccati_care_lhs(a,b,q,r,p) == matrix([[0,0],[0,0]])
    k=mm(mm(inv(r),tr(b)),p)
    assert k==eye(2)
    ac=closed_loop(a,b,k)
    assert ac==matrix([[-2,F(1,3)],[0,-3]])
    assert add(mm(tr(ac),p),mm(p,ac))==neg(add(q,mm(mm(tr(k),r),k)))
    rng=Random(243)
    for _ in range(120):
        x=matrix([[rng.randint(-3,3)],[rng.randint(-3,3)]])
        u=matrix([[rng.randint(-3,3)],[rng.randint(-3,3)]])
        xdot=add(mm(a,x),mm(b,u))
        derivative=mm(mm(tr(xdot),p),x)[0][0]+mm(mm(tr(x),p),xdot)[0][0]
        assert sq(x,q)+sq(u,r)+derivative == sq(add(u,mm(k,x)),r)
    assert q[0][0]>0 and q[0][0]*q[1][1]-q[0][1]**2>0
    print("LA24 nonnormal continuous matrix and infinite cost identity OK")


def test_two_state_examples():
    a=matrix([[-1,0],[0,-2]])
    b=eye(2)
    p=eye(2)
    r=eye(2)
    q=matrix([[3,0],[0,5]])
    assert riccati_care_lhs(a,b,q,r,p)==matrix([[0,0],[0,0]])
    ad=matrix([[F(1,2),0],[0,F(1,3)]])
    qd=matrix([[F(7,8),0],[0,F(17,18)]])
    rhs,k,_=riccati_dare_rhs(ad,b,qd,r,p)
    assert rhs==p
    assert k==[[x/2 for x in row] for row in ad]
    print("LA24 continuous/discrete two-state examples OK")


def run():
    test_discrete_scalar()
    test_continuous_scalar()
    test_discrete_matrix()
    test_continuous_matrix()
    test_two_state_examples()


if __name__=="__main__":
    run()
