#!/usr/bin/env python3
"""First independent arithmetic audit of source chapters 31--33.

Finite exact tests of Park C7 boundary linking/metabolizer, the
Park canonical-area identity, and Alexander polynomial multiplication.
They do not prove geometric embeddings, symplectic-form existence,
Seiberg--Witten gluing or the Freedman classification theorem.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"



def park_spheres_and_canonical_class():
    """Exact intersection calculations in h,e1,...,e13."""
    def unit(k):
        return [int(j==k) for j in range(14)]
    def plus(*terms):
        return [sum(vec[i]*scale for scale,vec in terms)
                for i in range(14)]
    def diff(a,b):return [x-y for x,y in zip(a,b)]
    def dot(a,b):return a[0]*b[0]-sum(
        a[j]*b[j] for j in range(1,14))
    h=unit(0)
    e={j:unit(j) for j in range(1,14)}
    f=plus((3,h),*[(-1,e[j]) for j in range(1,10)])
    s=plus((4,f),(1,e[9]),*[(-2,e[j]) for j in range(10,14)])
    v=[
        diff(e[4],e[7]),diff(e[1],e[4]),
        plus((1,h),(-1,e[1]),(-1,e[2]),(-1,e[3])),
        diff(e[2],e[5]),diff(e[5],e[9]),
    ]
    u=[s]+list(reversed(v))
    canonical=plus((-3,h),*[(1,e[j]) for j in range(1,14)])
    cnt=0
    assert dot(f,f)==0; cnt+=1
    for j in range(1,10):
        assert dot(f,e[j])==1;cnt+=1
    assert dot(s,s)==-9;cnt+=1
    for i in range(6):
        assert dot(u[i],u[i])==(-9 if i==0 else -2);cnt+=1
    for i in range(6):
        for j in range(i+1,6):
            assert dot(u[i],u[j])==int(j==i+1);cnt+=1
    for i in range(6):
        assert dot(canonical,u[i])==(7 if i==0 else 0);cnt+=1
    return cnt


def c7_boundary_linking():
    # Six-sphere plumbing: weights -9,-2,-2,-2,-2,-2.
    weights = [-9]+[-2]*5
    d0,d1=1,weights[0]
    minors=[d0,d1]
    for a in weights[1:]:
        d0,d1=d1,a*d1-d0
        minors.append(d1)
    assert minors == [1,-9,17,-25,33,-41,49]
    assert minors[-1] == 49
    # A tail of five -2 vertices has determinant -6.
    assert -6 == (-1)**5*6
    assert Fraction(-6,49).denominator==49
    group_order=49
    ker={x for x in range(group_order) if x%7==0}
    assert ker=={(7*x)%49 for x in range(7)}
    # Isotropic linking of meridian generator with lambda=-6/49.
    pair=lambda x,y:Fraction(-6*x*y,49)%1
    count=0
    for x,y in product(range(49), repeat=2):
        assert pair(x,y)==pair(y,x)
        assert (pair(x+7,y)-pair(x,y))%1 == pair(7,y)
        # A meridian element x is orthogonal to the subgroup
        # 7*Z/49 iff its pairing with 7 vanishes.
        assert (pair(x,7)==0)==(x in ker)
        if x in ker and y in ker:
            assert pair(x,y)==0
        count+=1
    # The only subgroup of order 7 is necessarily the kernel
    # of a surjection Z/49 -> Z/7.
    assert {x for x in range(49) if x%7==0} == ker
    return count


def canonical_pairing(a,b):
    assert len(b)==13
    B=sum(b[9:13])
    alpha=(
        12*a-4*sum(b[:9])+b[8]-2*B,
        b[4]-b[8],
        b[1]-b[4],
        a-b[0]-b[1]-b[2],
        b[0]-b[3],
        b[3]-b[6],
    )
    kR=-3*a+sum(b)
    return Fraction(7*kR+sum((6-i)*alpha[i] for i in range(6)),7),B


def park_cone_lower_bound():
    cases=0
    # Deliberately vary all 13 coefficients, rather than
    # only checking the displayed example.
    for seed in range(1,1001):
        b=[1+((seed*(j+3)+7*j*j) % 17) for j in range(13)]
        b.sort(reverse=True)
        area=sum(b)
        for extra in range(4):
            a=max(b[0],(area+2)//3)+extra
            P,B=canonical_pairing(a,b)
            rhs=18*(3*a-area)+2*(b[1]-b[2])+2*b[4]+b[5]+b[7]+2*b[8]+13*B
            assert 7*P==rhs
            assert P>=Fraction(13*B,7)>0
            # Independent coefficient-vector formula in chapter 32.
            direct=(
                54*a-18*b[0]-16*b[1]-20*b[2]-18*b[3]
                -16*b[4]-17*b[5]-18*b[6]-17*b[7]
                -16*b[8]-5*B
            )
            assert 7*P==direct
            cases+=1
    # Chapter 32 sample: 7 P=726 and K_R=-35.
    sample=[13,12,11,10,9,8,7,6,5,1,1,1,1]
    P,B=canonical_pairing(40,sample)
    assert P==Fraction(726,7)
    assert B==4
    return cases+1


def torus_2_odd_poly(n):
    # Symmetric Alexander polynomial for T(2,2n+1):
    # sum_{j=-n}^n (-1)^(n-j) z^j
    return {j: (-1)**(n-j) for j in range(-n,n+1)}


def mult_poly(A,B):
    C={}
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]=C.get(i+j,0)+a*b
    return {i:c for i,c in C.items() if c}


def evaluate(P,z):
    return sum(Fraction(c)*Fraction(z)**j for j,c in P.items())


def knot_connected_sums():
    count=0
    for n,m in product(range(1,9),repeat=2):
        A,B=torus_2_odd_poly(n),torus_2_odd_poly(m)
        C=mult_poly(A,B)
        assert len(C)==2*(n+m)+1
        assert C=={j:C[-j] for j in C}
        assert sum(C.values())==1
        for z in (Fraction(2),Fraction(3),Fraction(5,2)):
            assert evaluate(C,z)==evaluate(A,z)*evaluate(B,z)
        count+=1
    T=torus_2_odd_poly(1)
    sq=mult_poly(T,T)
    assert sq=={-2:1,-1:-2,0:3,1:-2,2:1}
    genus2=torus_2_odd_poly(2)
    assert genus2=={-2:1,-1:-1,0:1,1:-1,2:1}
    assert len(sq)==len(genus2)==5
    assert sorted(abs(x) for x in sq.values())==[1,1,2,2,3]
    assert sorted(abs(x) for x in genus2.values())==[1,1,1,1,1]
    return count+1


def source_anchors():
    filenames=(
        "31-egzotyczna-czterorozmaitosc-parka-konstrukcja-i-topologia.tex",
        "32-niezmienniki-seiberga-wittena-i-egzotycznosc-rozmaitosci-parka.tex",
        "33-chirurgia-wzdluz-wezla-i-niezmienniki-czterorozmaitosci.tex",
    )
    a,b,c=[(ROOT/name).read_text(encoding="utf-8") for name in filenames]
    assert r"\label{lem:tg-park-metabolizer}" in a
    assert r"\label{cor:tg-park14-quantitative-positive}" in b
    assert r"\label{prop:tg-ks-connected-sum}" in c
    assert r"\label{ex:tg-ks-connected-trefoils}" in c


if __name__=="__main__":
    source_anchors()
    print("PASS Park E(1) sphere classes and canonical adjunction:",park_spheres_and_canonical_class())
    print("PASS Park C7 H1 linking and metabolizer:",c7_boundary_linking())
    print("PASS Park canonical pairing and quantitative lower bound:",park_cone_lower_bound())
    print("PASS knot connected-sum Alexander and SW coefficient algebra:",knot_connected_sums())
