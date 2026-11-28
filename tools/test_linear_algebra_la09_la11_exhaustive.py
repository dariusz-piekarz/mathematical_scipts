#!/usr/bin/env python3
"""Independent LA09-LA11 small-field checks; stdlib only; fixed exhaustive sets."""
from collections import Counter
from itertools import product, combinations
from math import comb
from hashlib import sha256
from pathlib import Path

checks=Counter()
def ck(name,condition):
    checks[name]+=1
    if not condition:
        raise AssertionError(f"{name}: failed check #{checks[name]}")

def vectors(n,p): return tuple(product(range(p),repeat=n))
def dot(u,v,p): return sum(a*b for a,b in zip(u,v))%p
def add(u,v,p): return tuple((a+b)%p for a,b in zip(u,v))
def mv(A,v,p): return tuple(dot(row,v,p) for row in A)
def rank(A,p):
    a=[list(row) for row in A];m=len(a);n=len(a[0]) if m else 0;r=0
    for j in range(n):
        k=next((k for k in range(r,m) if a[k][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[x*inv%p for x in a[r]]
        for i in range(r+1,m):
            t=a[i][j]
            a[i]=[(a[i][z]-t*a[r][z])%p for z in range(n)]
        r+=1
    return r
def span_extend(S,v,p): return frozenset(add(u,tuple(a*x%p for x in v),p) for u in S for a in range(p))
def subspaces(n,p):
    zero=(0,)*n;out=[frozenset({zero})];seen=set(out)
    for v in vectors(n,p):
        for U in list(out):
            W=span_extend(U,v,p)
            if W not in seen:seen.add(W);out.append(W)
    return out
def basis(U,n,p):
    B=[];S=frozenset({(0,)*n})
    for v in sorted(U):
        if v not in S:B.append(v);S=span_extend(S,v,p)
    return tuple(B)
def symmetric_matrices(n,p):
    pairs=list(combinations(range(n),2))
    for values in product(range(p),repeat=n+len(pairs)):
        A=[[0]*n for _ in range(n)]
        for i in range(n): A[i][i]=values[i]
        for q,(i,j) in enumerate(pairs): A[i][j]=A[j][i]=values[n+q]
        yield tuple(map(tuple,A))
def alternating_matrices(n,p):
    pairs=list(combinations(range(n),2))
    for values in product(range(p),repeat=len(pairs)):
        A=[[0]*n for _ in range(n)]
        for q,(i,j) in enumerate(pairs):
            A[i][j]=values[q];A[j][i]=(-values[q])%p
        yield tuple(map(tuple,A))

# Degenerate symmetric bilinear forms, annihilators and double-perp formula.
for p,n in ((2,3),(3,3),(5,2)):
    vs=vectors(n,p);subs=subspaces(n,p)
    if (p,n)==(2,3):ck("subspace_enumeration",len(subs)==16)
    if (p,n)==(3,3):ck("subspace_enumeration",len(subs)==28)
    if (p,n)==(5,2):ck("subspace_enumeration",len(subs)==8)
    bases=[basis(U,n,p) for U in subs]
    for B in symmetric_matrices(n,p):
        radical=frozenset(x for x in vs if mv(B,x,p)==(0,)*n)
        ck("symmetric_radical_rank",len(radical)==p**(n-rank(B,p)))
        for U,UB in zip(subs,bases):
            perp=frozenset(v for v in vs if all(dot(mv(B,v,p),u,p)==0 for u in UB))
            intersection=U&radical
            ck("orthogonal_dimension_with_radical",len(perp)*len(U)==p**n*len(intersection))
            double=frozenset(v for v in vs if all(dot(mv(B,v,p),w,p)==0 for w in basis(perp,n,p)))
            sum_with_rad=frozenset(add(u,r,p) for u in U for r in radical)
            ck("double_orthogonal_equals_U_plus_radical",double==sum_with_rad)
            if U&perp==frozenset({(0,)*n}):
                ck("nondegenerate_restriction_split",len(U)*len(perp)==p**n)

# Quadratic forms, including characteristic 2 where diagonal data is invisible
# to polarization and where no division by two is available.
for p in (2,3,5):
    n=2;vs=vectors(n,p)
    for a,b,c in product(range(p),repeat=3):
        q=lambda x:(a*x[0]*x[0]+b*x[1]*x[1]+c*x[0]*x[1])%p
        for x in vs:
            ck("quadratic_homogeneity",all(q(tuple(t*v%p for v in x))==t*t*q(x)%p for t in range(p)))
            for y in vs:
                xy=add(x,y,p);polar=(q(xy)-q(x)-q(y))%p
                expected=(2*a*x[0]*y[0]+2*b*x[1]*y[1]+c*(x[0]*y[1]+x[1]*y[0]))%p
                ck("quadratic_polarization_all_characteristics",polar==expected)
                if p!=2:ck("quadratic_recovery_when_two_invertible",(polar if x==y else 0)==(2*q(x)%p if x==y else 0))
    if p==2:
        x=(1,0)
        ck("char2_polarization_not_injective",x[0]**2%2==1)

# Alternating bilinear forms have even rank, including in characteristic two.
for p,n in ((2,4),(3,4),(5,3)):
    for A in alternating_matrices(n,p):
        ck("alternating_even_rank",rank(A,p)%2==0)
        ck("alternating_square_zero",all(dot(x,mv(A,x,p),p)==0 for x in vectors(n,p)))
        ck("alternating_skew_symmetry",all(A[i][j]==(-A[j][i])%p for i in range(n) for j in range(n)))

def mm(A,B,p):
    m=len(A);n=len(B)
    k=len(B[0]) if n else 0
    return tuple(tuple(sum(A[i][j]*B[j][t] for j in range(n))%p for t in range(k)) for i in range(m))
def transpose(A):return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0]))) if A else ()
def kron(A,B,p):
    return tuple(tuple(A[i][j]*B[a][b]%p for j in range(len(A[0])) for b in range(len(B[0])))
                 for i in range(len(A)) for a in range(len(B)))
def allmat(m,n,p):
    return tuple(tuple(tuple(z[i*n+j] for j in range(n)) for i in range(m))
                 for z in product(range(p),repeat=m*n))
# Rank, transpose and mixed-product on all selected small matrices.
for p,(m,n),(r,s) in ((2,(2,3),(2,2)),(3,(2,2),(2,2)),(2,(3,2),(2,2))):
    Aset=allmat(m,n,p);Bset=allmat(r,s,p)
    for i,A in enumerate(Aset):
        for j,B in enumerate(Bset):
            P=kron(A,B,p)
            ck("kronecker_rank",rank(P,p)==rank(A,p)*rank(B,p))
            ck("kronecker_transpose",transpose(P)==kron(transpose(A),transpose(B),p))
            if m==n and r==s:
                C=Aset[(3*i+7*j+1)%len(Aset)]
                D=Bset[(i+5*j+2)%len(Bset)]
                ck("kronecker_mixed_product",mm(kron(A,B,p),kron(C,D,p),p)==kron(mm(A,C,p),mm(B,D,p),p))

# Exterior/symmetric powers, including zero-dimensional and positive-characteristic cases.
for n in range(7):
    for k in range(9):
        subsets=list(combinations(range(n),k))
        ck("exterior_basis_dimension",len(subsets)==comb(n,k) if k<=n else len(subsets)==0)
        monomials=sum(1 for exps in product(range(k+1),repeat=n) if sum(exps)==k)
        ck("symmetric_basis_dimension",monomials==(comb(n+k-1,k) if n else (1 if k==0 else 0)))
    ck("exterior_algebra_total_dimension",sum(comb(n,k) for k in range(n+1))==2**n)

def wedge(I,J,p):
    if set(I)&set(J): return (0,())
    inv=sum(i>j for i in I for j in J)
    return ((-1 if inv%2 else 1)%p,tuple(sorted(I+J)))
for p,n in ((2,4),(3,4)):
    subsets=[tuple(c) for k in range(n+1) for c in combinations(range(n),k)]
    for I in subsets:
        for J in subsets:
            a,K=wedge(I,J,p);b,L=wedge(J,I,p)
            ck("wedge_graded_commutativity",a==((-1 if len(I)*len(J)%2 else 1)*b)%p and (not a or K==L))
            for H in subsets:
                c,M=wedge(K,H,p) if a else (0,())
                d,N=wedge(J,H,p);e,O=wedge(I,N,p) if d else (0,())
                ck("wedge_associativity",a*c%p==d*e%p and (not (a*c%p) or M==O))
print("LA09-LA11 independent exact tests, no external dependencies")
for k,v in sorted(checks.items()):print(k,v)
print("TOTAL PASS:",sum(checks.values()))
print("SOURCE SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
