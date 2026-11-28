#!/usr/bin/env python3
"""Second independent audit (23) of SW chapters 28--30.

Finite exact checks only: C2 rational-blowdown Spin-c index obstruction,
affine wall intersections, and the principal symbol of d* + d+.
These checks do NOT certify existence of Spin-c gluing or moduli spaces,
transversality, Fredholm theory, compactness, or wall crossing.
"""
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "chapters/pl/graph_and_knot_theory"


def source_anchors():
    paths = (
        "28-wprowadzenie-do-teorii-seiberga-wittena-i-zastosowan-w-wymiarz.tex",
        "29-analityczne-podstawy-teorii-seiberga-wittena-przestrzenie-modu.tex",
        "30-analiza-seiberga-wittena-od-lokalnego-przekroju-do-niezmiennik.tex",
    )
    a, b, c = [(ROOT / x).read_text(encoding="utf-8") for x in paths]
    assert r"\label{lem:tg-sw-c2-admissible-pairing}" in a
    assert r"\ref{lem:tg-sw-c2-admissible-pairing}" in a
    assert r"\label{lem:tg-sw-affine-wall}" in b
    assert r"\label{lem:tg-sw12-symbol-matrix}" in c
    assert r"\ref{lem:tg-sw12-symbol}" in c


def c2_spin_c_obstruction():
    """C2 has S²=-4, c|S=m and κ(X_(2))=κ(X)+1."""
    count = 0
    # For E(4), κ=2*48+3*(-32)=0 and c²=0 for 0,±2F.
    e, sig, square_c = 48, -32, 0
    kappa = 2*e+3*sig
    assert kappa == 0
    assert 2*(e-1)+3*(sig+1) == kappa+1
    for m in range(-100, 101, 2):
        restriction_square = Fraction(-m*m, 4)
        square_c_prime = Fraction(square_c)-restriction_square
        d_x = Fraction(square_c-kappa, 4)
        d_prime = Fraction(square_c_prime-(kappa+1), 4)
        assert d_x-d_prime == Fraction(4-m*m, 16)
        if d_prime.denominator == 1:
            # A matching Spin-c structure may only exist if this
            # necessary integrality condition holds; not sufficient.
            assert m % 4 == 2
        else:
            assert m % 4 == 0
        assert (d_x==d_prime)==(abs(m)==2)
        if abs(m)==2:
            assert d_x==d_prime==0
        if m==0:
            assert d_prime==Fraction(-1,4)
        count+=1

    # The three E(4) basic classes: c=±2F evaluate ±2 on
    # the section, whereas c=0 evaluates 0 and cannot
    # give a matching Spin-c lift with this rational ball.
    survival = {-2: True, 0: False, 2: True}
    for m, valid in survival.items():
        delta = Fraction(4-m*m,16)
        assert (delta==0)==valid
    return count+len(survival)


def affine_wall_crossings():
    """Exact rational parameter, no floating point pi approximation."""
    checked=0
    for c,eta0,num,den in product(range(-7,8),range(-7,8),
                                   range(-5,6),range(1,8)):
        # The wall coefficient is calculated in units of pi:
        # w(t)/pi = 2*c - eta0 - t*(num/den).
        w0=Fraction(2*c-eta0)
        a=Fraction(num,den)
        if a:
            tstar=w0/a
            assert w0-tstar*a==0
            # Moving by one unit from the unique crossing
            # gives opposite, nonzero wall values.
            assert w0-(tstar-1)*a==a
            assert w0-(tstar+1)*a==-a
        else:
            assert all(w0-t*a==w0 for t in (-100,-1,0,1,100))
        checked+=1
    # CP²: c1=3H, eta_t=t omega; wall is 6*pi - t
    assert Fraction(2*3)-Fraction(6)==0
    return checked+1


def determinant4(A):
    out=0
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        sign=-1 if inversions%2 else 1
        val=sign
        for i in range(4):
            val*=A[i][p[i]]
        out+=val
    return out


def symbol_matrix():
    """B=2 M(xi) in the unnormalized selfdual 2-form basis.

    B B^T = |xi|² diag(4,1,1,1); det B = -2 |xi|^4.
    """
    cases=0
    sample_a=((1,0,0,0),(0,1,0,0),(0,0,1,0),
              (0,0,0,1),(1,-2,3,-1))
    for u,v,w,t in product(range(-3,4),repeat=4):
        if not (u or v or w or t):
            continue
        norm=u*u+v*v+w*w+t*t
        B=((-2*u,-2*v,-2*w,-2*t),
           (-v,u,-t,w),
           (-w,t,u,-v),
           (-t,-w,v,u))
        for i in range(4):
            for j in range(4):
                row_inner=sum(B[i][k]*B[j][k] for k in range(4))
                expect=norm*(4 if i==0 else 1) if i==j else 0
                assert row_inner==expect,(u,v,w,t,i,j,row_inner,expect)
        assert determinant4(B)==-2*norm*norm
        for a in sample_a:
            values=[sum(B[i][k]*a[k] for k in range(4))
                    for i in range(4)]
            # B^T diag(1/4,1,1,1) B = norm * I.
            assert values[0]**2 + 4*sum(z*z for z in values[1:]) == (
                4*norm*sum(z*z for z in a))
            cases+=1
    return cases


if __name__ == "__main__":
    source_anchors()
    print("PASS C2 index, mod-4 gluing obstruction and E(4) classes:",
          c2_spin_c_obstruction())
    print("PASS exact affine wall intersection/transversality:",
          affine_wall_crossings())
    print("PASS quaternionic principal-symbol orthogonality/determinant:",
          symbol_matrix())
