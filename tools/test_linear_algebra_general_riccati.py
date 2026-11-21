"""LA26 regression: generalized stabilizing CARE/DARE with semidefinite Q.

All identities are evaluated over rational numbers using Fraction.
There is deliberately no positive-definite-Q assumption: all
matrix examples have a nontrivial unobserved stable subspace.
"""
from fractions import Fraction as F
from math import exp, isclose
from random import Random
from test_linear_algebra_riccati import (
    matrix, eye, tr, mm, add, sub, neg, inv,
    riccati_dare_rhs, riccati_care_lhs, closed_loop, sq,
)


def semidefinite_data():
    ad = matrix([[2, 0], [0, F(1, 2)]])
    bd = matrix([[1], [0]])
    qd = matrix([[F(4, 5), 0], [0, 0]])
    rd = matrix([[1]])
    pd = matrix([[4, 0], [0, 0]])
    ac = matrix([[1, 0], [0, -2]])
    bc = matrix([[1], [0]])
    qc = matrix([[3, 0], [0, 0]])
    rc = matrix([[1]])
    pc = matrix([[3, 0], [0, 0]])
    return (ad, bd, qd, rd, pd), (ac, bc, qc, rc, pc)


def assert_zeros(a):
    assert all(x == 0 for row in a for x in row), a


def normsq(x):
    return sum((y[0] * y[0] for y in x), F(0))


def discrete_semidefinite_matrix():
    (a, b, q, r, p), _ = semidefinite_data()
    rhs, k, m = riccati_dare_rhs(a, b, q, r, p)
    assert rhs == p
    assert k == matrix([[F(8, 5), 0]])
    assert m == matrix([[5]])
    d = closed_loop(a, b, k)
    assert d == matrix([[F(2, 5), 0], [0, F(1, 2)]])
    assert sub(p, mm(mm(tr(d), p), d)) == add(q, mm(mm(tr(k), r), k))
    assert p[1][1] == 0 and q[1][1] == 0  # not positive definite
    rng = Random(26)
    for _ in range(250):
        x = matrix([[rng.randint(-10, 10)], [rng.randint(-10, 10)]])
        u = matrix([[rng.randint(-9, 9)]])
        nx = add(mm(a, x), mm(b, u))
        lhs = sq(x, q) + sq(u, r) + sq(nx, p) - sq(x, p)
        rhs = sq(add(u, mm(k, x)), m)
        assert lhs == rhs, (lhs, rhs, x, u)
    # Comparison matrix for the arbitrary stabilizing gain K_0=(2,0).
    k0 = matrix([[2, 0]])
    d0 = closed_loop(a, b, k0)
    assert d0 == matrix([[0, 0], [0, F(1, 2)]])
    h = add(q, mm(mm(tr(k0), r), k0))
    w = matrix([[F(24, 5), 0], [0, 0]])
    assert sub(w, mm(mm(tr(d0), w), d0)) == h
    assert w[0][0] >= p[0][0]
    print("LA26: DARE semidefinite 2x2 exact feedback/energy/bound OK")


def continuous_semidefinite_matrix():
    _, (a, b, q, r, p) = semidefinite_data()
    assert_zeros(riccati_care_lhs(a, b, q, r, p))
    k = mm(mm(inv(r), tr(b)), p)
    assert k == matrix([[3, 0]])
    d = closed_loop(a, b, k)
    assert d == matrix([[-2, 0], [0, -2]])
    assert add(mm(tr(d), p), mm(p, d)) == neg(add(q, mm(mm(tr(k), r), k)))
    rng = Random(2600)
    for _ in range(250):
        x = matrix([[rng.randint(-10, 10)], [rng.randint(-10, 10)]])
        u = matrix([[rng.randint(-9, 9)]])
        xdot = add(mm(a, x), mm(b, u))
        derivative = (mm(mm(tr(xdot), p), x)[0][0]
                      + mm(mm(tr(x), p), xdot)[0][0])
        lhs = sq(x, q) + sq(u, r) + derivative
        rhs = sq(add(u, mm(k, x)), r)
        assert lhs == rhs, (lhs, rhs, x, u)
    k0 = matrix([[2, 0]])
    d0 = closed_loop(a, b, k0)
    assert d0 == matrix([[-1, 0], [0, -2]])
    h = add(q, mm(mm(tr(k0), r), k0))
    w = matrix([[F(7, 2), 0], [0, 0]])
    assert add(mm(tr(d0), w), mm(w, d0)) == neg(h)
    assert w[0][0] >= p[0][0]
    print("LA26: CARE semidefinite 2x2 exact feedback/energy/bound OK")


def unstable_scalar_examples():
    # Unstable open loop, detectable scalar, Q=4/5.
    a, b, q, r, p = F(2), F(1), F(4, 5), F(1), F(4)
    assert p == q + a*a*p - a*a*b*b*p*p/(r+b*b*p)
    kd = (r+b*b*p)**-1 * b*p*a
    assert kd == F(8, 5)
    assert a-b*kd == F(2, 5)
    other = F(-1, 5)
    assert other == q + a*a*other - a*a*other*other/(r+other)
    assert a-b * (b*other*a/(r+b*b*other)) == F(5, 2)
    # Riccati monotonicity and boundedness by finite stabilizing cost.
    p0 = F(0)
    vals = [p0]
    for _ in range(18):
        p0 = q + a*a*p0 - a*a*p0*p0/(r+p0)
        vals.append(p0)
    assert vals[1] == F(4, 5)
    assert vals[2] == F(116, 45)
    assert all(F(0) <= vals[j] <= vals[j+1] <= F(4)
               for j in range(len(vals)-1))
    assert abs(float(vals[-1]-4)) < 1e-10
    assert F(4) <= F(24, 5)  # cost bound using K_0=2

    # Continuous unstable open loop, detectable, Q=3.
    a, b, q, r, p = F(1), F(1), F(3), F(1), F(3)
    assert 2*a*p - (b*b*p*p)/r + q == 0
    assert a-b*p/r == -2
    assert 2*a*F(-1) - F(-1)**2 + q == 0
    assert a-b*F(-1) == 2
    for t in (0., .1, .2, .5, 1., 4.):
        z = exp(-4*t)
        s = 3*(1-z)/(1+3*z)
        derivative = 48*z/(1+3*z)**2
        assert isclose(derivative, 2*s-s*s+3, rel_tol=1e-12, abs_tol=1e-12)
        assert 0 <= s < 3
    print("LA26: unstable scalar CARE/DARE and Riccati recursions OK")


def missing_hypotheses():
    # Q=0, A unstable, B nonzero: detectable fails, minimum finite
    # horizon value P_N=0 despite stabilizing algebraic root P=3.
    p = F(0)
    for _ in range(12):
        p = 4*p/(1+p)
        assert p == 0
    assert F(3) == 4*F(3)/(1+F(3))
    assert F(2)-F(3)*F(2)/(1+F(3)) == F(1, 2)
    # Continuous Q=0: P=0 and P=2 solve CARE, only 2 stabilizes.
    assert 2*F(0)-F(0)**2 == 0
    assert 2*F(2)-F(2)**2 == 0
    # B=0; detectable but not stabilizable: only negative ARE roots.
    assert F(-1, 3) == 1 + 4*F(-1, 3)
    assert 2*F(-1, 2) + 1 == 0
    print("LA26: explicit failure of detectability / stabilizability OK")


def energy_values():
    # Closed-loop exponential/geometric energy agrees with x_0^* P x_0.
    (ad, bd, qd, rd, pd), (ac, bc, qc, rc, pc) = semidefinite_data()
    x0 = F(3)
    d = F(2, 5)
    kd = F(8, 5)
    stage = F(4, 5) + kd*kd
    assert stage == (1-d*d)*F(4)
    assert stage/(1-d*d)*x0*x0 == F(4)*x0*x0
    kc = F(3)
    rate = F(-2)
    continuous_stage = F(3)+kc*kc
    assert continuous_stage/(-2*rate) == F(3)
    print("LA26: infinite-horizon optimal costs and energy sums OK")


if __name__ == "__main__":
    discrete_semidefinite_matrix()
    continuous_semidefinite_matrix()
    unstable_scalar_examples()
    missing_hypotheses()
    energy_values()
