#!/usr/bin/env python3
"""Exact finite-field checks: determinants, dual maps, symmetrization and alternation.
No third-party dependencies.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial

checks=Counter()
def ck(name,ok):
    checks[name]+=1
    if not ok:raise AssertionError(f"{name} at {checks[name]}")
def det(A,p):
    n=len(A);v=0
    for pi in permutations(range(n)):
        inv=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        x=-1 if inv%2 else 1
        for i in range(n):x*=A[i][pi[i]]
        v+=x
    return v%p
def prod(A,B,p):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
def minor(A,i,j):
    return tuple(tuple(x for t,x in enumerate(row) if t!=j) for s,row in enumerate(A) if s!=i)
def adj(A,p):
    n=len(A)
    return tuple(tuple(((-1 if (i+j)%2 else 1)*det(minor(A,j,i),p))%p for j in range(n)) for i in range(n))
def rank(A,p,n):
    a=[list(row) for row in A];m=len(a);r=0
    for j in range(n):
        z=next((i for i in range(r,m) if a[i][j]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r];inv=pow(a[r][j],-1,p)
        a[r]=[v*inv%p for v in a[r]]
        for i in range(r+1,m):
            x=a[i][j];a[i]=[(a[i][t]-x*a[r][t])%p for t in range(n)]
        r+=1
        if r==m:break
    return r
def mx(A,x,p):
    return tuple(sum(z*v for z,v in zip(row,x))%p for row in A)
def dot(x,y,p):
    return sum(a*b for a,b in zip(x,y))%p

matrix_cases=0
for p,n in ((2,0),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(5,2)):
    matrices=[tuple(tuple(x[n*i+j] for j in range(n)) for i in range(n))
              for x in product(range(p),repeat=n*n)]
    for index,A in enumerate(matrices):
        d=det(A,p)
        ck("det_transpose",det(tuple(zip(*A)) if A else (),p)==d)
        ck("det_invertibility",(d!=0)==(rank(A,p,n)==n))
        ck("adjugate_identity",prod(A,adj(A,p),p)==tuple(tuple(d if i==j else 0 for j in range(n)) for i in range(n)))
        for i in range(n):
            expansion=sum(A[i][j]*((-1 if (i+j)%2 else 1)*det(minor(A,i,j),p)) for j in range(n))%p
            ck("laplace_expansion",expansion==d)
        B=matrices[(7*index+11)%len(matrices)]
        ck("det_multiplicative",det(prod(A,B,p),p)==d*det(B,p)%p)
        if d and n:
            b=tuple((i+1+index)%p for i in range(n))
            x=[det(tuple(tuple(b[s] if j==i else A[s][j] for j in range(n)) for s in range(n)),p)*pow(d,-1,p)%p for i in range(n)]
            ck("cramer_solution",mx(A,x,p)==b)
        matrix_cases+=1

dual_cases=0
for p,m,n in ((2,2,3),(2,3,2),(2,3,3),(3,2,2),(3,2,3),(3,3,2),(2,3,0),(2,0,3),(3,0,0)):
    X=tuple(product(range(p),repeat=n))
    Y=tuple(product(range(p),repeat=m))
    for entries in product(range(p),repeat=m*n):
        A=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(m))
        At=tuple(tuple(A[i][j] for i in range(m)) for j in range(n))
        image={mx(A,x,p) for x in X}
        kernel={x for x in X if mx(A,x,p)==(0,)*m}
        image_dual={mx(At,y,p) for y in Y}
        kernel_dual={y for y in Y if mx(At,y,p)==(0,)*n}
        ann_image={y for y in Y if all(dot(y,z,p)==0 for z in image)}
        ann_kernel={x for x in X if all(dot(x,z,p)==0 for z in kernel)}
        r=rank(A,p,n)
        ck("dual_kernel_ann_image",kernel_dual==ann_image)
        ck("dual_image_ann_kernel",image_dual==ann_kernel)
        ck("dual_rank",len(image_dual)==p**r)
        ck("dual_rank_nullity",len(kernel)==p**(n-r))
        dual_cases+=1

def sign(pi):
    return (-1)**sum(pi[i]>pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))
def sym_alt(F,p,n,k):
    sym,alt={},{}
    for ids in product(range(n),repeat=k):
        ss=aa=0
        for pi in permutations(range(k)):
            val=F[tuple(ids[pi[t]] for t in range(k))]
            ss+=val;aa+=sign(pi)*val
        sym[ids]=ss%p;alt[ids]=aa%p
    return sym,alt

form_cases=0
for p,n,k in ((2,2,2),(3,2,2),(2,3,2),(2,2,3)):
    ids=tuple(product(range(n),repeat=k))
    pis=tuple(permutations(range(k)))
    for entries in product(range(p),repeat=n**k):
        F=dict(zip(ids,entries))
        sym,alt=sym_alt(F,p,n,k)
        for I in ids:
            for pi in pis:
                J=tuple(I[pi[t]] for t in range(k))
                ck("sym_operator_invariance",sym[I]==sym[J])
                ck("alt_operator_signed",alt[J]==sign(pi)*alt[I]%p)
            if len(set(I))<k:
                ck("alt_operator_repeated_basis",alt[I]==0)
            if len(set(I))==k and factorial(k)%p:
                ck("alt_square",sym_alt(alt,p,n,k)[1][I]==factorial(k)*alt[I]%p)
        form_cases+=1

F={(0,0):1,(0,1):0,(1,0):0,(1,1):0}
ck("char2_symmetric_not_alternating",F[(0,1)]==F[(1,0)] and F[(0,0)]!=0)
print("LA06-LA08 EXACT FINITE-FIELD CHECKS")
print("matrix_cases",matrix_cases)
print("dual_matrix_cases",dual_cases)
print("multilinear_form_cases",form_cases)
for name,n in sorted(checks.items()):print(name,n)
print("TOTAL_PASS",sum(checks.values()))
