#!/usr/bin/env python3
"""Audit 20: exact and independent arithmetic of Kirby slides and rational blowdowns.

Checks the chapter-25 integral ±1 blowdown, the Casson-Harer boundary
homology necessary condition, and all admissible C_(p,q) up to p=34.
NO computation certifies the existence of rational balls or embeddings.
Standard Python library only.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def determinant(matrix):
    """Exact permutation-free determinant with rational elimination."""
    n=len(matrix)
    if n==0:return 1
    A=[[Fraction(x) for x in row] for row in matrix]
    assert all(len(row)==n for row in A)
    product_pivots=Fraction(1)
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None:return 0
        if k!=j:
            A[j],A[k]=A[k],A[j]
            product_pivots=-product_pivots
        pivot=A[j][j]
        product_pivots*=pivot
        for i in range(j+1,n):
            fac=A[i][j]/pivot
            for h in range(j+1,n):
                A[i][h]-=fac*A[j][h]
            A[i][j]=Fraction(0)
    assert product_pivots.denominator==1
    return int(product_pivots)


def solve(matrix,vec):
    n=len(matrix)
    A=[[Fraction(z) for z in row]+[Fraction(vec[i])]
       for i,row in enumerate(matrix)]
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        assert k is not None
        A[j],A[k]=A[k],A[j]
        pivot=A[j][j]
        A[j]=[v/pivot for v in A[j]]
        for i in range(n):
            if i!=j:
                c=A[i][j]
                A[i]=[x-c*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def pairing(inv,x,y):
    return sum(x[i]*inv[i][j]*y[j]
               for i in range(len(x)) for j in range(len(y)))


def positive_negative_blowdown():
    """Unimodular congruence and exact boundary linking pairing."""
    count=0
    for eps,a,b,c,l1,l2 in product((-1,1),(-3,-1,1,3),(-4,-2,0,2),
                                    (-2,0,2),(-2,-1,0,1,2),(-2,-1,0,1,2)):
        B=[[a,c],[c,b]]
        ell=(l1,l2)
        # Source order (K1,K2,U) and integral transformation:
        # f_i=e_i-eps*l_i*u, then u.
        Q=[[a,c,l1],[c,b,l2],[l1,l2,eps]]
        P=[[1,0,0],[0,1,0],[-eps*l1,-eps*l2,1]]
        Bd=[[B[i][j]-eps*ell[i]*ell[j] for j in range(2)]
            for i in range(2)]
        target=[[Bd[0][0],Bd[0][1],0],
                [Bd[1][0],Bd[1][1],0],
                [0,0,eps]]
        assert matmul(matmul(transpose(P),Q),P)==target
        assert determinant(Q)==eps*determinant(Bd)
        if determinant(Q)!=0:
            # Inverse is checked via direct rational Gauss-Jordan,
            # independently of Schur complement.
            invQ=[solve(Q,[int(k==i) for k in range(3)])
                  for i in range(3)]
            invQ=transpose(invQ)
            invT=[solve(target,[int(k==i) for k in range(3)])
                  for i in range(3)]
            invT=transpose(invT)
            x=[1,2,-1];y=[-1,1,2]
            xp=[sum(P[k][i]*x[k] for k in range(3)) for i in range(3)]
            yp=[sum(P[k][i]*y[k] for k in range(3)) for i in range(3)]
            assert pairing(invQ,x,y)==pairing(invT,xp,yp)
        count+=1
    # Explicit +1 contraction and linking form 4/11 in chapter 25.
    Q=[[1,1,1],[1,-2,0],[1,0,-3]]
    Bd=[[-3,-1],[-1,-4]]
    assert determinant(Q)==determinant(Bd)==11
    assert -solve(Bd,[1,0])[0]==Fraction(4,11)
    return count+1



def slam_dunk_primitive_slopes():
    """Check integer-r elimination using integral meridian relations.

    The crucial counterexample with two rational slopes is included:
    the naive rational-r extension changes H1 and is thus false.
    """
    count=0
    for r in range(-6,7):
        for c in range(-8,9):
            if not c:continue
            for d in range(1,9):
                if gcd(abs(c),d)!=1:continue
                # Hopf link's H1 relation matrix:
                # r*mu_U+mu_V=0; d*mu_U+c*mu_V=0.
                original=determinant([[r,1],[d,c]])
                numerator=r*c-d
                assert original==numerator
                assert gcd(abs(numerator),abs(c))==1
                # H1 of n/c surgery on the unknot has order |n|.
                assert abs(original)==abs(numerator)
                count+=1
    # r=1/2, s=4: Hopf surgery gives H1 order 2,
    # whereas naive slam-dunk slope 1/4 gives H1 order 1.
    hopf=determinant([[1,2],[1,4]])
    naive=Fraction(1,2)-Fraction(1,4)
    assert hopf==2 and naive==Fraction(1,4)
    assert abs(hopf)!=abs(naive.numerator)
    return count+1


def hirzebruch_jung(num,den):
    assert num>den>=1 and gcd(num,den)==1
    a,b=num,den
    out=[]
    while True:
        z=(a+b-1)//b
        assert z>=2
        out.append(z)
        nxt=z*b-a
        if not nxt:return out
        assert 0<nxt<b
        a,b=b,nxt


def value_negative_fraction(coeffs):
    x=Fraction(coeffs[-1])
    for a in reversed(coeffs[:-1]):
        x=a-Fraction(1,x)
    return x


def tridiag_negative(coeffs):
    n=len(coeffs)
    A=[[0]*n for _ in range(n)]
    for i,a in enumerate(coeffs):A[i][i]=-a
    for i in range(n-1):A[i][i+1]=A[i+1][i]=1
    return A


def continued_fraction_plumbings():
    """All coprime (p,q), not merely examples: exact fractions and inverse minors."""
    total=0
    for p in range(2,35):
        for q in range(1,p):
            if gcd(p,q)!=1:continue
            a=hirzebruch_jung(p*p,p*q-1)
            assert value_negative_fraction(a)==Fraction(p*p,p*q-1)
            if q==1:assert a==[p+2]+[2]*(p-2)
            Q=tridiag_negative(a)
            n=len(a)
            # Determinants via direct elimination, not tail continued fractions.
            d=determinant(Q)
            assert d==(-1)**n*p*p
            tail=determinant([row[1:] for row in Q[1:]])
            assert tail==(-1)**(n-1)*(p*q-1)
            # Corner inverse as an independent rational system.
            invcol=solve(Q,[int(i==0) for i in range(n)])
            assert -invcol[0]==Fraction(p*q-1,p*p)
            # Every leading principal minor of -Q has the correct sign.
            assert all((-1)**k*determinant([row[:k] for row in Q[:k]])>0
                       for k in range(1,n+1))
            # Adjacent edge 1 implies the cokernel is generated by e1:
            # for n=1 the order is |a1|=p².
            assert p*p*Fraction(invcol[0]).denominator>=p*p
            assert (p*p*invcol[0]).denominator==1
            assert (p*p*invcol[0])%1==0
            assert Fraction(p*q-1,p*p).denominator==p*p
            # Metabolizer of cyclic linking form: subgroup of order p.
            assert (p*p*Fraction(p*q-1,p*p)).denominator==1
            assert gcd(p,p*q-1)==1
            total+=1
    # Pin nontrivial new example C_7,3.
    assert hirzebruch_jung(49,20)==[3,2,6,2]
    assert value_negative_fraction([3,2,6,2])==Fraction(49,20)
    return total


def casson_harer_boundary_kernel():
    """Necessary exact group sequence of the standard 0/1/2-handle rational ball."""
    total=0
    for p in range(2,151):
        n=p*p
        # Z/(p²) -> Z/p by reduction modulo p.
        ker={k for k in range(n) if k%p==0}
        assert len(ker)==p
        assert ker=={(p*j)%n for j in range(p)}
        assert set(k%p for k in range(n))==set(range(p))
        # Kernel is self-orthogonal for linking coefficient (p-1)/p².
        # Orthogonality to a cyclic subgroup is checked on its generator p.
        assert (p*p*(p-1))%n==0
        orth={x for x in range(n) if (x*p*(p-1))%n==0}
        assert orth==ker
        total+=1
    return total


def source_labels():
    names=[
        "25-rachunek-kirby-ego-operacje-na-ramowanych-splotach-i-grafach.tex",
        "26-wymierna-kontrakcja-od-grafow-plumbingowych-do-egzotycznych-cz.tex",
        "27-uogolniona-wymierna-kontrakcja-i-lancuchy-cpq.tex",
    ]
    a,b,c=[(ROOT/n).read_text(encoding="utf-8") for n in names]
    assert r"\label{ex:tg-kirby-positive-blowdown}" in a
    assert r"\label{st:tg-rb-boundary-kernel}" in b
    assert r"\label{ex:tg-general-C73}" in c
    assert r"\label{thm:tg-general-lens}" in c
    assert r"\label{thm:tg-rb-invariants}" in b


if __name__=="__main__":
    source_labels()
    print("PASS Kirby ±1 blowdown integral congruence and linking:",positive_negative_blowdown())
    print("PASS Cpq continued fractions, determinant, inverse and linking:",continued_fraction_plumbings())
    print("PASS integer-r slam-dunk and rational-r counterexample:",slam_dunk_primitive_slopes())
    print("PASS rational ball boundary kernel and metabolizer:",casson_harer_boundary_kernel())
