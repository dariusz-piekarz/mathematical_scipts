#!/usr/bin/env python3
"""Independent SECOND pass on graph/knot chapters 31--33.

All tests are exact algebraic computations, not certificates of Park's
symplectic embedding, a topological homeomorphism, or SW gluing.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def inverse_fraction(M):
    """Independent exact Gauss-Jordan inverse, with no Q_n formula."""
    n=len(M)
    rows=[[Fraction(x) for x in row]+
          [Fraction(int(i==j)) for j in range(n)]
          for i,row in enumerate(M)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if rows[i][j]),None)
        assert pivot is not None
        rows[j],rows[pivot]=rows[pivot],rows[j]
        x=rows[j][j]
        rows[j]=[v/x for v in rows[j]]
        for i in range(n):
            if i==j: continue
            x=rows[i][j]
            rows[i]=[y-x*z for y,z in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]


def park_Q_inverse_full():
    n=6
    Q=[[-9 if i==j==0 else -2 if i==j else
        1 if abs(i-j)==1 else 0 for j in range(n)]for i in range(n)]
    inv=inverse_fraction(Q)
    counted=0
    diagonals=[6,45,68,75,66,41]
    for i,j in product(range(n),repeat=2):
        candidate=Fraction(
            -(8*min(i,j)+1)*(6-max(i,j)),49
        )
        assert inv[i][j]==candidate,(i,j,inv[i][j],candidate)
        val=sum(Fraction(Q[i][k])*inv[k][j] for k in range(n))
        assert val==int(i==j)
        counted+=1
    for i in range(n):
        assert inv[i][i]==Fraction(-diagonals[i],49)
        assert gcd(diagonals[i],49)==1
        counted+=1
    return counted


def rational_blowdown_family():
    """Generalized C_p matrix family, testing Q_7 as one member."""
    count=0
    for p in range(2,19):
        n=p-1
        Q=[[-(p+2) if i==j==0 else -2 if i==j else
            1 if abs(i-j)==1 else 0 for j in range(n)]
           for i in range(n)]
        I=inverse_fraction(Q)
        for i in range(n):
            for j in range(n):
                cand=Fraction(-((p+1)*min(i,j)+1)*(n-max(i,j)),p*p)
                assert I[i][j]==cand,(p,i,j,I[i][j],cand)
                count+=1
        # The first-meridian linking form is -(p-1)/p^2,
        # and <p*mu> is an isotropic subgroup of order p.
        assert I[0][0]==Fraction(-(p-1),p*p)
        assert gcd(p-1,p*p)==1
        count+=1
    return count


def park_cone_counterexample():
    b=[4,4,4]+[1]*10
    a=10
    assert len(b)==13
    assert a>=b[0] and all(b[j]>=b[j+1] for j in range(12))
    assert min(b)>0 and 3*a>sum(b)
    assert a-b[0]-b[1]-b[2]==-2
    count=1
    # Many choices satisfy the formal positive-cone inequalities
    # but give a NEGATIVE area on the (-2) sphere v3.
    for A in range(6,23):
        for b1 in range(2,9):
            for b2 in range(2,b1+1):
                for b3 in range(2,b2+1):
                    bs=[b1,b2,b3]+[1]*10
                    if not A>=b1 or not 3*A>sum(bs):
                        continue
                    if A>=b1+b2+b3:
                        continue
                    assert A-b1-b2-b3<0
                    count+=1
    assert count>100
    return count


def mult(A,B):
    C={}
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]=C.get(i+j,0)+a*b
    return {k:v for k,v in C.items() if v}


def poly_eval(P,z):
    return sum(Fraction(c)*Fraction(z)**j for j,c in P.items())


def equal_basic_count_families():
    trefoil={-1:1,0:-1,1:1}
    current={0:1}
    count=0
    for n in range(1,41):
        current=mult(current,trefoil)
        torus={j:(-1)**(n-j) for j in range(-n,n+1)}
        assert sorted(current)==list(range(-n,n+1))
        assert len(current)==len(torus)==2*n+1
        for j in range(-n,n+1):
            assert current[j]!=0
            assert (current[j]>0)==((-1)**(n-j)>0)
            assert current[j]==current[-j]
            count+=1
        assert current[n-1]==-n
        assert current[n]==1
        assert sum(current.values())==1
        for z in (Fraction(2),Fraction(3,2),Fraction(7,3)):
            assert poly_eval(current,z)==poly_eval(trefoil,z)**n
            count+=1
        if n>=2:
            assert max(abs(v) for v in current.values())>=n>1
            assert all(abs(v)==1 for v in torus.values())
            assert sorted(abs(v) for v in current.values())!=(
                sorted(abs(v) for v in torus.values()))
            count+=1
    return count


def anchors():
    file_names=(
       "31-egzotyczna-czterorozmaitosc-parka-konstrukcja-i-topologia.tex",
       "32-niezmienniki-seiberga-wittena-i-egzotycznosc-rozmaitosci-parka.tex",
       "33-chirurgia-wzdluz-wezla-i-niezmienniki-czterorozmaitosci.tex")
    a,b,c=[(ROOT/n).read_text(encoding="utf-8") for n in file_names]
    assert r"\label{lem:tg-park-Q-inverse-full}" in a
    assert r"\label{ex:tg-park14-cone-not-sufficient}" in b
    assert r"\label{thm:tg-ks-equal-basic-count}" in c


if __name__=="__main__":
    anchors()
    print("PASS independent Park Q7 Gauss-Jordan inverse:",park_Q_inverse_full())
    print("PASS generalized C_p rational inverse entries:",rational_blowdown_family())
    print("PASS Park positive-cone counterexamples:",park_cone_counterexample())
    print("PASS equal-basic-count knot surgery families:",equal_basic_count_families())
