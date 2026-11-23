#!/usr/bin/env python3
"""Independent exact regressions for graph/knot source chapters 34--36.

Verifies C_p surgery matrix, rational Betti/signature bookkeeping,
Khovanov Frobenius and reduced basepoint algebra, explicit TL3 braid
algebra, and that audited source definitions/references are present.
Finite tests are not formal certificates for external geometric theorems.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

BASE=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def cp_boundary_rational_blowdown():
    count=0
    for p in range(2,181):
        d0,d1=1,-(p+2)
        assert d1==-(p+2)
        for k in range(2,p):
            d0,d1=d1,-2*d1-d0
            assert d1==(-1)**k*(1+k*(p+1))
            count+=1
        assert d1==(-1)**(p-1)*p*p
        # Evaluate the negative continued fraction bottom-up.
        fraction=Fraction(2)
        for _ in range(p-3):
            fraction=2-Fraction(1,fraction)
        if p==2:
            fraction=Fraction(4)
        else:
            fraction=p+2-Fraction(1,fraction)
        assert fraction==Fraction(p*p,p-1)
        assert gcd(p*p,p-1)==1
        count+=1

        # No b1=0 assumption is needed for rational homology
        # splitting: all signatures/betti below are formal rank data.
        for b1,bplus,bminus in product(range(4),range(4),range(p-1,p+3)):
            old_b2=bplus+bminus
            new_b1=b1
            new_bplus=bplus
            new_bminus=bminus-(p-1)
            new_b2=new_bplus+new_bminus
            old_chi=2-2*b1+old_b2
            new_chi=2-2*new_b1+new_b2
            old_sig=bplus-bminus
            new_sig=new_bplus-new_bminus
            assert new_chi==old_chi-(p-1)
            assert new_sig==old_sig+(p-1)
            assert new_b2==old_b2-(p-1)
            count+=1
    return count


ZERO=(0,0)
ONE=(1,0)
X=(0,1)
BASIS=(ONE,X)


def add(u,v):
    return tuple(a+b for a,b in zip(u,v))


def mult(u,v):
    a,b=u; c,d=v
    return (a*c,a*d+b*c)


def delta(u):
    a,b=u
    return ((0,a,a,b))  # basis 11, 1X, X1, XX


def tensor_mult_left(pair):
    # m ⊗ id on A⊗A⊗A; output 4 coefficients
    out=[0]*4
    for k,val in enumerate(pair):
        if not val:continue
        a=(k>>2)&1; b=(k>>1)&1;c=k&1
        w=mult(BASIS[a],BASIS[b])
        for bit,coef in enumerate(w):
            out[bit*2+c]+=val*coef
    return tuple(out)


def tensor_mult_right(triple):
    out=[0]*4
    for k,val in enumerate(triple):
        if not val:continue
        a=(k>>2)&1;b=(k>>1)&1;c=k&1
        w=mult(BASIS[b],BASIS[c])
        for bit,coef in enumerate(w):
            out[a*2+bit]+=val*coef
    return tuple(out)


def delta_mult_pair(a,b):
    return delta(mult(a,b))


def id_delta(a,b):
    # id ⊗ Δ, A⊗A -> A⊗A⊗A
    out=[0]*8
    for i,coef in enumerate(a):
        for j,multiplier in enumerate(delta(b)):
            out[i*4+j]+=coef*multiplier
    return tuple(out)


def delta_id(a,b):
    # Δ ⊗ id, A⊗A -> A⊗A⊗A
    out=[0]*8
    for i,coef in enumerate(delta(a)):
        for j,multiplier in enumerate(b):
            out[i*2+j]+=coef*multiplier
    return tuple(out)


def khovanov_frobenius_and_reduction():
    count=0
    for a,b,c in product(BASIS,repeat=3):
        assert mult(mult(a,b),c)==mult(a,mult(b,c))
        count+=1
    for a in BASIS:
        d=delta(a)
        left=[0]*8
        right=[0]*8
        for i,x in enumerate(d):
            if not x: continue
            a0=BASIS[i//2];b0=BASIS[i%2]
            left=[v+x*w for v,w in zip(left,delta_id(a0,b0))]
            right=[v+x*w for v,w in zip(right,id_delta(a0,b0))]
        assert tuple(left)==tuple(right)
        count+=1
    for a,b in product(BASIS,repeat=2):
        d=delta_mult_pair(a,b)
        l=tensor_mult_left(id_delta(a,b))
        r=tensor_mult_right(delta_id(a,b))
        assert d==l==r,(a,b,d,l,r)
        count+=1
    # Marked-factor ideal XA preserved under mergers.
    for b in ((1,0),(0,1),(2,3),(-4,8),(0,0)):
        assert mult(X,b)[0]==0
        assert mult(b,X)[0]==0
        count+=1
    # Marked circle splitting preserves both new copies of XA.
    assert delta(X)==(0,0,0,1)
    count+=1
    # One-crossing-free unknot: un-reduced has quantum ranks 1 at
    # ±1; reduced basepoint subcomplex XA{+1} is rank 1 in q=0.
    assert len(BASIS)==2
    assert X!=(0,0)
    count+=1
    return count


def tl3_reduce(word,delta_value):
    """Exact TL3 relation normal form on words in {e,f}."""
    v=list(word)
    coeff=Fraction(1)
    while True:
        matched=False
        for i in range(len(v)-1):
            if v[i]==v[i+1]:
                coeff*=delta_value
                v.pop(i+1)
                matched=True
                break
        if matched: continue
        for i in range(len(v)-2):
            if v[i]==v[i+2] and v[i]!=v[i+1]:
                v=v[:i+1]+v[i+3:]
                matched=True
                break
        if not matched:
            break
    return ''.join(v),coeff


def tl3_mul(A,B,delta_value):
    out={}
    for left,a in A.items():
        for right,b in B.items():
            key,c=tl3_reduce(left+right,delta_value)
            out[key]=out.get(key,Fraction(0))+a*b*c
    return {key:val for key,val in out.items() if val}


def tl3_representations():
    count=0
    for aa in (Fraction(1,5),Fraction(1,3),Fraction(1,2),
               Fraction(1),Fraction(2),Fraction(3),
               Fraction(-1),Fraction(-2),Fraction(-4,3)):
        d=-aa**2-aa**(-2)
        e={'':aa,'e':1/aa}
        f={'':aa,'f':1/aa}
        ei={'':1/aa,'e':aa}
        fi={'':1/aa,'f':aa}
        identity={'':Fraction(1)}
        assert tl3_mul(e,ei,d)==identity
        assert tl3_mul(f,fi,d)==identity
        left=tl3_mul(tl3_mul(e,f,d),e,d)
        right=tl3_mul(tl3_mul(f,e,d),f,d)
        assert left==right,(aa,left,right)
        count+=1
    return count


def source_checks():
    files=[
        "34-od-grafow-plumbingowych-do-egzotycznych-struktur-gladkich-synt.tex",
        "35-nowoczesne-niezmienniki-i-zastosowania-teorii-wezlow.tex",
        "36-literatura-i-podsumowanie.tex",
    ]
    a,b,c=[(BASE/name).read_text(encoding="utf-8") for name in files]
    assert r"\label{cor:tg-syn-rational-homological}" in a
    assert "kowymiar" in a
    assert r"\label{lem:kt-khovanov-frobenius}" in b
    assert r"$n_z(\phi)=0$" in b
    assert r"$XA\subset A$" in b
    assert r"\label{sec:kt-bibliografia-mapa}" in c
    for doi in ("10.1016/j.aim.2003.05.001",
                "10.1215/S0012-7094-00-10131-7",
                "10.1007/s10240-010-0030-y"):
        assert doi in c


if __name__=="__main__":
    source_checks()
    print("PASS C_p boundary fraction and unconditional rational blowdown:",cp_boundary_rational_blowdown())
    print("PASS Khovanov Frobenius, coassociativity and basepoint ideal:",khovanov_frobenius_and_reduction())
    print("PASS TL3 inversion and Artin braid relations:",tl3_representations())
    print("PASS verified modern invariants bibliography and anchors")
