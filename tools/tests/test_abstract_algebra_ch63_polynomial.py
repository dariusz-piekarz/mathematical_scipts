"""AA-63: exact symbolic regular-element parametrization in sl_2."""
import sympy as sp


def test_regular_parameterization():
    s, u, c, a, d = sp.symbols("s u c a d")
    H = sp.diag(c, -c)
    U = sp.Matrix([[1 + s*u, s], [u, 1]])
    F = sp.simplify(U * H * U.inv())
    expected = sp.Matrix([
        [c*(1 + 2*s*u), -2*c*s*(1 + s*u)],
        [2*c*u, -c*(1 + 2*s*u)],
    ])
    assert sp.simplify(F - expected) == sp.zeros(2)
    # Coordinates in the ordered basis (e,f,h).
    coords = sp.Matrix([F[0, 1], F[1, 0], F[0, 0]])
    assert sp.factor(coords.jacobian([s, u, c]).det()) == -4*c**2
    assert sp.simplify(F[0, 0]**2 + F[0, 1]*F[1, 0] - c**2) == 0
    # For d != 0 and a^2 + b*d != 0, choose c^2=a^2+b*d.
    # Then s=(a-c)/d and u=d/(2*c) recover the target matrix.
    G = F.subs({s: (a-c)/d, u: d/(2*c)}, simultaneous=True)
    G = G.applyfunc(sp.factor)
    assert sp.simplify(G - sp.Matrix([
        [a, (c*c-a*a)/d], [d, -a]
    ])) == sp.zeros(2)


if __name__ == "__main__":
    test_regular_parameterization()
    print("AA-63 symbolic sl2 polynomial map: PASS")
