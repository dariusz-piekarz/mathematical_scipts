#!/usr/bin/env python3
"""Exact exhaustive small-field regression: LA03 linear maps, LA04 bases, LA05 RREF.
Independent brute-force image and kernel enumerations, no external dependencies.
"""
from itertools import product
from collections import Counter
from hashlib import sha256
from pathlib import Path

checks=Counter(); matrices_by_case=Counter()
def ck(k,cond,detail=''):
    if not cond: raise AssertionError((k,detail))
    checks[k]+=1

def allvec(n,p): return tuple(product(range(p),repeat=n))
def A_x(A,x,p): return tuple(sum(a*v for a,v in zip(row,x))%p for row in A)
def matmul(A,B,p,nmiddle=None):
    if not A: return tuple()
    nb=len(B[0]) if B else 0
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(nb)) for i in range(len(A)))
def ident(n): return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def nullmatrix(m,n): return tuple((0,)*n for _ in range(m))
def subspace_span(vectors,n,p):
    S={(0,)*n}
    for v in vectors: S={tuple((x[i]+a*v[i])%p for i in range(n)) for x in S for a in range(p)}
    return frozenset(S)
def trans(A,m,n): return tuple(tuple(A[i][j] for i in range(m)) for j in range(n))
def rref(A,n,p,last=False):
    A=[list(r) for r in A];m=len(A); piv=[];r=0
    for j in range(n):
        opts=[i for i in range(r,m) if A[i][j]%p]
        if not opts: continue
        k=opts[-1] if last else opts[0]
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][j],-1,p)
        A[r]=[(v*inv)%p for v in A[r]]
        for i in range(m):
            if i==r:continue
            t=A[i][j]
            if t: A[i]=[(A[i][c]-t*A[r][c])%p for c in range(n)]
        piv.append(j);r+=1
        if r==m:break
    return tuple(map(tuple,A)),tuple(piv)
def kernel_from_R(R,piv,n,p):
    free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        x=[0]*n;x[f]=1
        for i,j in enumerate(piv):x[j]=-R[i][f]%p
        out.append(tuple(x))
    return out

def test_matrix(A,m,n,p):
    R,piv=rref(A,n,p)
    R2,piv2=rref(A,n,p,True)
    ck('rref_pivot_strategy_unique',R==R2 and piv==piv2)
    RR,pp=rref(R,n,p)
    ck('rref_idempotent',R==RR and pp==piv)
    # Output respects RREF pivot columns by construction, verify full row span using independent enumeration.
    row_S=subspace_span(A,n,p);row_R=subspace_span(R,n,p)
    ck('rref_row_space',row_S==row_R)
    ck('rref_row_permutation', rref(tuple(reversed(A)),n,p)[0]==R)
    k=len(piv)
    ck('row_rank',len(row_S)==p**k)
    basis=kernel_from_R(R,piv,n,p)
    ker_brute={x for x in allvec(n,p) if A_x(A,x,p)==(0,)*m}
    ck('kernel_membership', all(x in ker_brute for x in basis))
    ck('kernel_basis_span',subspace_span(basis,n,p)==ker_brute)
    ck('rank_nullity',len(ker_brute)==p**(n-k))
    original_cols=[tuple(A[i][j] for i in range(m)) for j in range(n)]
    pivot_cols=[original_cols[j] for j in piv]
    im_brute={A_x(A,x,p) for x in allvec(n,p)}
    ck('image_pivot_original_columns',subspace_span(pivot_cols,m,p)==im_brute)
    ck('image_dimension',len(im_brute)==p**k)
    ck('rank_transpose',len(subspace_span(original_cols,m,p))==len(row_S))
    # Augmented consistency check for zero, an arbitrary target and one known image.
    b_candidates={(0,)*m, tuple((i+1)%p for i in range(m)), A_x(A,(1,)*n,p)}
    for b in b_candidates:
        augmented=tuple(row+(b[i],) for i,row in enumerate(A))
        T,_=rref(augmented,n+1,p)
        contradiction=any(all(row[j]==0 for j in range(n)) and row[n]!=0 for row in T)
        ck('augmented_compatibility', (not contradiction)==(b in im_brute))
        if b in im_brute:
            solutions=[x for x in allvec(n,p) if A_x(A,x,p)==b]
            ck('affine_solution_count',len(solutions)==len(ker_brute))
            x0=solutions[0]
            ck('affine_solution_coset',set(solutions)=={tuple((x0[j]+z[j])%p for j in range(n)) for z in ker_brute})
    matrices_by_case[f'F{p}:{m}x{n}']+=1

for p,m,n in [(2,0,0),(2,0,3),(2,3,0),(2,1,3),(2,3,1),(2,2,2),(2,2,3),(2,3,2),(2,3,3),(2,3,4),(2,4,3),
              (3,0,2),(3,2,0),(3,2,2),(3,2,3),(3,3,2),(3,3,3),(5,2,2)]:
    for entries in product(range(p),repeat=m*n):
        A=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(m))
        test_matrix(A,m,n,p)

# Exhaustive basis-change formula for 2x2 matrices over F2/F3, sampling no random numbers.
for p in (2,3):
    vs=allvec(2,p)
    allA=[tuple(tuple(a[i*2+j] for j in range(2)) for i in range(2)) for a in product(range(p),repeat=4)]
    G=[]
    for M in allA:
        _,piv=rref(M,2,p)
        if len(piv)==2:G.append(M)
    ck('GL2_cardinality',len(G)==(p*p-1)*(p*p-p))
    for idx,A in enumerate(allA):
        for t in range(min(12,len(G))):
            B=G[(idx+3*t)%len(G)];C=G[(idx*3+5*t)%len(G)]
            Cinv=next(D for D in G if matmul(C,D,p)==ident(2))
            Ap=matmul(Cinv,matmul(A,B,p),p)
            for x in vs:
                lhs=A_x(Ap,x,p)
                rhs=A_x(Cinv,A_x(A,A_x(B,x,p),p),p)
                ck('change_of_basis_QinvAP',lhs==rhs)
    for P in allA:
        if matmul(P,P,p)!=P:continue
        im={A_x(P,x,p) for x in vs}
        ker={x for x in vs if A_x(P,x,p)==(0,0)}
        ck('idempotent_image_kernel',len(im)*len(ker)==len(vs) and im.intersection(ker)=={(0,0)})
        ck('projection_identity_on_image', all(A_x(P,y,p)==y for y in im))

print('MATRIX CASES:')
for k,v in sorted(matrices_by_case.items()):print(k,v)
print('CHECK GROUPS:')
for k,v in sorted(checks.items()):print(k,v)
print('TOTAL MATRIX SAMPLES:',sum(matrices_by_case.values()))
print('TOTAL PASS:',sum(checks.values()))
print('SOURCE SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
