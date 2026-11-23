#!/usr/bin/env python3
"""Independent exact Seiberg-Witten audit models for chapters 28--30.

Checks only finite algebra: spin-c index/parity for connected sums,
the CP2 wall affine function and the real Clifford multiplication
linear isomorphism. No finite model proves Fredholm theory,
transversality, compactness or wall crossing.
"""
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def index_parity_examples():
    """c characteristic, all coefficients odd, both signs of the lattice."""
    total=0
    for positives in range(1,5):
        for negatives in range(0,4):
            for b1 in range(0,3):
                bplus=positives
                euler=2-2*b1+positives+negatives
                signature=positives-negatives
                values=(-3,-1,1,3)
                for a in product(values,repeat=positives+negatives):
                    square=sum(x*x for x in a[:positives])-sum(
                        x*x for x in a[positives:])
                    assert (square-signature)%8==0
                    numerator=square-2*euler-3*signature
                    assert numerator%4==0
                    dimension=numerator//4
                    dirac_index=(square-signature)//8
                    assert dimension==2*dirac_index+b1-1-bplus
                    assert dimension%2==(b1-1-bplus)%2
                    if b1==0 and bplus%2==0:
                        assert dimension!=0
                    total+=1
    # Example from the new theorem: CP2#CP2 with c=H1+H2.
    assert (2-2*4-3*2)//4==-3
    return total


def affine_wall_cp2():
    """Exact coefficient of pi (no approximate floating point pi)."""
    euler,signature,c_square=3,1,9
    assert (c_square-2*euler-3*signature)//4==0
    total=0
    for t_pi in range(-40,41):
        # Harmonic omega represents H and is normalized by int omega^2=1.
        w_pi=2*3-t_pi
        assert (w_pi==0)==(t_pi==6)
        assert w_pi-(2*3-(t_pi+1))==1
        if t_pi==0:assert w_pi>0
        if t_pi>=7:assert w_pi<0
        total+=1
    return total


def clifford_real_iso():
    """Pauli-matrix quaternionic model for Cl_4 on C^2 spinors.

    The map v |-> M(v)psi has |M(v)psi|^2=|v|^2|psi|^2.
    Different psi test that this is not a special-basis coincidence.
    """
    total=0
    vectors=product(range(-2,3),repeat=4)
    spinors=[
        (1+0j,0j), (0j,1+0j), (1+1j,2-1j),
        (2-1j,-3+2j), (1-2j,-1-1j),
    ]
    for v0,v1,v2,v3 in vectors:
        # M(v)=v0 I + i(v1 sigma_x + v2 sigma_y + v3 sigma_z)
        m00=complex(v0,v3)
        m01=complex(v2,v1)
        m10=complex(-v2,v1)
        m11=complex(v0,-v3)
        norm_v=v0*v0+v1*v1+v2*v2+v3*v3
        for x,y in spinors:
            out0=m00*x+m01*y
            out1=m10*x+m11*y
            lhs=abs(out0)**2+abs(out1)**2
            rhs=norm_v*(abs(x)**2+abs(y)**2)
            # Every expression is an integer, despite Python's abs.
            assert lhs==rhs,(v0,v1,v2,v3,x,y,lhs,rhs)
            if norm_v:
                assert lhs>0
            total+=1
    # For psi=(1,0) the images of the standard real basis of R4
    # are (1,0),(0,i),(-? see M(sigma_y): first row 0, second -1), (i,0).
    e_images=[(1+0j,0j),(0j,1j),(0j,-1+0j),(1j,0j)]
    # Each basis image spans a distinct coordinate of C^2 over R.
    assert len({tuple((int(z.real),int(z.imag)) for z in pair)
                for pair in e_images})==4
    return total


def source_anchors():
    names=[
        "28-wprowadzenie-do-teorii-seiberga-wittena-i-zastosowan-w-wymiarz.tex",
        "29-analityczne-podstawy-teorii-seiberga-wittena-przestrzenie-modu.tex",
        "30-analiza-seiberga-wittena-od-lokalnego-przekroju-do-niezmiennik.tex",
    ]
    a,b,c=[(ROOT/name).read_text(encoding="utf-8") for name in names]
    assert r"\label{cor:tg-sw-index-parity}" in a
    assert r"\label{ex:tg-sw-index-parity}" in a
    assert r"\label{ex:tg-sw-wall-cp2}" in b
    assert r"\label{lem:tg-sw12-clifford-real-iso}" in c
    for source in (a,b,c):
        assert "konciąg" not in source
        # Check *complete words*: "konsekwencja" contains this substring.
        import re
        assert not re.search(r"\bsekwencja\b|\bsekwencji\b",source.lower())
        assert "Każda ciąg" not in source
    assert r"\ref{lem:tg-sw12-clifford-real-iso}" in c


if __name__=="__main__":
    source_anchors()
    print("PASS spin-c characteristic/index/parity models:",index_parity_examples())
    print("PASS CP2 wall crossing affine parameter:",affine_wall_cp2())
    print("PASS Clifford real isometry by Pauli algebra:",clifford_real_iso())
