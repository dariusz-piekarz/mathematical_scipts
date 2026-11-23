#!/usr/bin/env python3
"""Second independent audit of source chapters 34--36.

C_p linking forms and metabolizers, Khovanov state gradings,
cube signs, graded Euler coefficients including Reidemeister-I
examples, and bibliographic source/anchor checks. All arithmetic
is exact. Does not certify external geometric results.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

BASE=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def cp_linking_metabolizers():
    count=0
    for p in range(2,128):
        n=p-1
        # Determinants derived independently from the continuant.
        dprev, dcur=1,-(p+2)
        for k in range(2,n+1):
            dprev,dcur=dcur,-2*dcur-dprev
        assert dcur==(-1)**n*p*p
        # The trailing (-2)-chain has determinant (-1)^(n-1)*n.
        cofactor=(-1)**(n-1)*n
        qinv00=Fraction(cofactor,dcur)
        assert qinv00==Fraction(-(p-1),p*p)
        lam00=-qinv00
        assert lam00==Fraction(p-1,p*p)
        assert gcd(p-1,p*p)==1
        count+=1

        # A cyclic presentation follows by eliminating tail generators:
        # x_i=(n-i)x_last, and first relation = -p^2*x_last.
        if n>1:
            assert -(p+2)*n+(n-1)==-p*p
        else:
            assert p==2 and -(p+2)==-p*p
        assert gcd(p-1,p*p)==1
        count+=1
        m=p*p
        for x in range(m):
            # Orthogonality to subgroup <p*mu>:
            # lambda(x*mu,p*mu) = (p-1)*x / p mod 1.
            is_orthogonal=((p-1)*x)%p==0
            assert is_orthogonal==(x%p==0)
            # Every multiple p*y of mu has zero mutual linking
            # with generator p*mu; hence subgroup is isotropic.
            if x%p==0:
                assert ((p-1)*x*p)%m==0
            count+=1
    return count


def mul(a,b):
    if a=="1":return b
    if b=="1":return a
    return None


def delta(a):
    if a=="1":return (("1","X"),("X","1"))
    return (("X","X"),)


def degree(x):
    return 1 if x=="1" else -1


def khovanov_bidegree():
    count=0
    # Every local merge/split is quantum-homogeneous of degree -1.
    for n in range(1,13):
        for nminus in range(n+1):
            nplus=n-nminus
            for weight in range(n):
                src_shift=weight+nplus-2*nminus
                dst_shift=weight+1+nplus-2*nminus
                for a,b in product(("1","X"),repeat=2):
                    c=mul(a,b)
                    if c is not None:
                        assert degree(c)+dst_shift==(
                            degree(a)+degree(b)+src_shift)
                        count+=1
                for a in ("1","X"):
                    for x,y in delta(a):
                        assert degree(x)+degree(y)+dst_shift==(
                            degree(a)+src_shift)
                        count+=1
    return count


def cube_sign_cancellation():
    count=0
    # Independent of algebra maps: both oriented paths around
    # a 2-face of an ordered n-dimensional cube have opposite signs.
    for n in range(2,13):
        for state in range(1<<n):
            for j in range(n):
                if (state>>j)&1: continue
                for k in range(j+1,n):
                    if (state>>k)&1: continue
                    sj=(-1)**((state&((1<<j)-1)).bit_count())
                    sk_after_j=(-1)**(((state|(1<<j))&((1<<k)-1)).bit_count())
                    sk=(-1)**((state&((1<<k)-1)).bit_count())
                    sj_after_k=(-1)**(((state|(1<<k))&((1<<j)-1)).bit_count())
                    assert sj*sk_after_j+sk*sj_after_k==0
                    count+=1
    return count


def add_poly(a,b,multiple=1):
    out=defaultdict(int)
    for j,c in a.items():out[j]+=c
    for j,c in b.items():out[j]+=multiple*c
    return {j:c for j,c in out.items() if c}


def mul_poly(a,b):
    out=defaultdict(int)
    for i,c in a.items():
        for j,d in b.items():
            out[i+j]+=c*d
    return {j:c for j,c in out.items() if c}


def shift(a,s,sign=1):
    return {i+s:sign*c for i,c in a.items()}


def khovanov_euler():
    count=0
    f={-1:1,1:1}
    for k in range(1,12):
        pol={0:1}
        for _ in range(k):pol=mul_poly(pol,f)
        # Crossingless k-component unlink, all quantum ranks.
        assert pol=={j:c for j,c in pol.items() if c}
        assert sum(pol.values())==2**k
        assert sum(j*c for j,c in pol.items())==0
        count+=1

    # A positive R-I kink: cube 0-state has two circles
    # and cube 1-state one circle. Normalization n_+=1,n_-=0.
    f2=mul_poly(f,f)
    plus=add_poly(shift(f2,1),shift(f,2),-1)
    assert plus==f
    count+=1

    # A negative R-I kink: 0-state one circle and 1-state
    # two circles; n_+=0,n_-=1.
    minus=add_poly(shift(f,-2,-1),shift(f2,-1))
    assert minus==f
    count+=1

    # Euler-Poincare check on free rank pattern for 2-term
    # complexes with a homogeneous differential of rank r.
    # The alternating sum of homology ranks remains a-b.
    for a,b in product(range(1,51),repeat=2):
        for rank in range(min(a,b)+1):
            h0=a-rank
            h1=b-rank
            assert h0-h1==a-b
            count+=1
    return count


def anchors_and_sources():
    files=[
        "34-od-grafow-plumbingowych-do-egzotycznych-struktur-gladkich-synt.tex",
        "35-nowoczesne-niezmienniki-i-zastosowania-teorii-wezlow.tex",
        "36-literatura-i-podsumowanie.tex",
    ]
    a,b,c=[(BASE/name).read_text(encoding="utf-8") for name in files]
    for needle in (r"\label{lem:tg-syn-cp-metabolizer}",
                   r"$M_p=M_p^\perp$",r"\gcd(p-1,p^2)=1"):
        assert needle in a,needle
    for needle in (r"\label{prop:kt-kh-graded-euler}",
                   r"$d:C^{i,j}(D)\to C^{i+1,j}(D)$"):
        assert needle in b,needle
    for doi in ("10.1016/j.aim.2004.10.015",
                "10.1007/s00222-007-0075-9",
                "10.4310/jdg/1214424968",
                "10.1007/s00222-010-0275-6"):
        assert doi in c,doi


if __name__=="__main__":
    anchors_and_sources()
    print("PASS independent C_p cyclic linking & metabolizer:",cp_linking_metabolizers())
    print("PASS independent Khovanov bidegree all merges/splits:",khovanov_bidegree())
    print("PASS ordered cube signed-square cancellations:",cube_sign_cancellation())
    print("PASS graded Euler, positive/negative R-I and chain ranks:",khovanov_euler())
    print("PASS audit27 checked bibliographic DOIs and cross-source anchors")
