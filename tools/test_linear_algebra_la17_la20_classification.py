#!/usr/bin/env python3
"""Independent LA17-LA20 finite-field Jordan, Smith, Frobenius, elementary and CRT checks.
No SymPy, NumPy, randomness, or external dependencies.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb
from hashlib import sha256
from pathlib import Path

checks=Counter()
def ck(label,ok):
    checks[label]+=1
    if not ok: raise AssertionError(f"{label}: failed assertion {checks[label]}")
def trim(a,p):
    a=[int(x)%p for x in a]
    while a and not a[-1]:a.pop()
    return tuple(a)
def plus(a,b,p):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)
def neg(a,p):return trim([-v for v in a],p)
def mul(a,b,p):
    if not a or not b:return ()
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c,p)
def divmodp(a,b,p):
    a=trim(a,p);b=trim(b,p)
    if not b:raise ZeroDivisionError()
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        off=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p;q[off]=c
        a=plus(a,neg((0,)*off+tuple(c*x for x in b),p),p)
    return trim(q,p),a
def monic(a,p):
    a=trim(a,p)
    return tuple(x*pow(a[-1],-1,p)%p for x in a) if a else ()
def gcd(a,b,p):
    while b:a,b=b,divmodp(a,b,p)[1]
    return monic(a,p)
def detpol(A,p):
    n=len(A)
    if n==0:return (1,)
    s=()
    for perm in permutations(range(n)):
        t=(1,)
        for i in range(n):t=mul(t,A[i][perm[i]],p)
        inversion=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        s=plus(s,t if inversion%2==0 else neg(t,p),p)
    return s
def signed_poly_matrix(A,p):
    n=len(A)
    return tuple(tuple(((-A[i][j])%p,int(i==j)) if i==j else trim((-A[i][j],),p) for j in range(n)) for i in range(n))
def smith(A,p):
    n=len(A);B=signed_poly_matrix(A,p)
    delta=[(1,)]
    for k in range(1,n+1):
        current=()
        for I in combinations(range(n),k):
            for J in combinations(range(n),k):
                minor=detpol(tuple(tuple(B[i][j] for j in J) for i in I),p)
                current=gcd(current,minor,p)
        delta.append(current)
    factors=[]
    for k in range(1,n+1):
        q,r=divmodp(delta[k],delta[k-1],p)
        ck("smith_determinantal_divisors_integral",not r)
        factors.append(q)
    return tuple(factors),delta
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def zero(n):return tuple((0,)*n for _ in range(n))
def ma(A,B,p):
    return tuple(tuple((A[i][j]+B[i][j])%p for j in range(len(A))) for i in range(len(A)))
def ms(A,B,p):return ma(A,tuple(tuple(-x for x in row) for row in B),p)
def scale(A,x,p):return tuple(tuple(x*v%p for v in row) for row in A)
def mm(A,B,p):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
def power(A,k,p):
    R=eye(len(A))
    for _ in range(k):R=mm(R,A,p)
    return R
def peval(f,A,p):
    n=len(A);R=zero(n);I=eye(n)
    for c in reversed(f):R=ma(mm(R,A,p),scale(I,c,p),p)
    return R
def rank(A,p):
    n=len(A)
    if not n:return 0
    a=[list(row) for row in A];r=0
    for j in range(n):
        k=next((i for i in range(r,n) if a[i][j]%p),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        v=pow(a[r][j],-1,p);a[r]=[x*v%p for x in a[r]]
        for i in range(n):
            if i!=r:
                u=a[i][j];a[i]=[(a[i][h]-u*a[r][h])%p for h in range(n)]
        r+=1
        if r==n:break
    return r
def linear_solve(M,b,p):
    m=len(M);n=len(M[0]) if m else 0
    a=[list(M[i])+[b[i]%p] for i in range(m)];r=0;col=[]
    for j in range(n):
        t=next((i for i in range(r,m) if a[i][j]%p),None)
        if t is None:continue
        a[t],a[r]=a[r],a[t];z=pow(a[r][j],-1,p);a[r]=[x*z%p for x in a[r]]
        for i in range(m):
            if i!=r:
                c=a[i][j];a[i]=[(a[i][k]-c*a[r][k])%p for k in range(n+1)]
        col.append(j);r+=1
    if any(not any(row[:n]) and row[n] for row in a):return None
    out=[0]*n
    for i,j in enumerate(col):out[j]=a[i][n]
    return out
def minpoly(A,p):
    n=len(A)
    if not n:return (1,)
    ps=[eye(n)]
    for d in range(n+1):
        target=[v for row in ps[d] for v in row]
        M=[[ps[j][i//n][i%n] for j in range(d)] for i in range(n*n)]
        coeff=linear_solve(M,target,p)
        if coeff is not None:return trim([-x for x in coeff]+[1],p)
        ps.append(mm(ps[-1],A,p))
    raise AssertionError("No annihilating polynomial of degree <=n")
def companion(f,p):
    d=len(f)-1
    return tuple(tuple((1 if i==j+1 else 0) if j<d-1 else -f[i]%p for j in range(d)) for i in range(d))
def blockdiag(A,B):
    m=len(A);n=len(B)
    return tuple(tuple(A[i][j] if j<m else 0 for j in range(m+n)) for i in range(m))+tuple(tuple(0 if j<m else B[i-m][j-m] for j in range(m+n)) for i in range(m,m+n))
def jordan(n,lam,p):
    return tuple(tuple((lam if i==j else (1 if j==i+1 else 0))%p for j in range(n)) for i in range(n))
def powpoly(a,k,p):
    r=(1,)
    for _ in range(k):r=mul(r,a,p)
    return r

# Exhaustive matrices for F2 up to n=3, F3 and F5 up to n=2;
# reproducible additional ternary n=3 matrices, including nontrivial Jordan forms.
cases=[]
for p,n in ((2,0),(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2)):
    cases.extend((p,tuple(tuple(e[n*i+j] for j in range(n)) for i in range(n)))
                 for e in product(range(p),repeat=n*n))
for k in range(270):
    e=tuple(((k//(3**((j*5+2)%9)))+j*j+3*j+k*j)%3 for j in range(9))
    cases.append((3,tuple(tuple(e[3*i+j] for j in range(3)) for i in range(3))))
for p,A in cases:
    n=len(A);d,delta=smith(A,p);chi=detpol(signed_poly_matrix(A,p),p);mini=minpoly(A,p)
    ck("smith_chain",all(not divmodp(d[i+1],d[i],p)[1] for i in range(len(d)-1)))
    ck("smith_product_is_characteristic",__import__("functools").reduce(lambda a,b:mul(a,b,p),d,(1,))==chi)
    ck("frobenius_last_factor_is_minimal",next((x for x in reversed(d) if len(x)>1),(1,))==mini)
    ck("smith_degree_equals_dimension",sum(len(f)-1 for f in d)==n)
    ck("Cayley_Hamilton_independent",peval(chi,A,p)==zero(n))
    ck("annihilation_minimal_independent",peval(mini,A,p)==zero(n))
    ck("smith_determinantal_gcd_consistency",delta[-1]==chi)
    for f in d:
        if len(f)>1 and len(f)<=4:
            C=companion(f,p)
            ck("companion_minimal_polynomial",minpoly(C,p)==f)
            ck("companion_characteristic_polynomial",detpol(signed_poly_matrix(C,p),p)==f)

# Explicit primary companion blocks for irreducibles of degrees 1 and 2.
for p,ps in ((2,((0,1),(1,1),(1,1,1))), (3,((0,1),(1,1),(1,0,1)))):
    for f in ps:
        d=len(f)-1
        for a in (1,2,3):
            powerf=powpoly(f,a,p);A=companion(powerf,p);Z=zero(len(A))
            ck("primary_companion_annihilated",peval(powerf,A,p)==Z)
            ck("primary_companion_is_cyclic",minpoly(A,p)==powerf)
            P=peval(f,A,p)
            for k in range(a+2):
                actual=len(A)-rank(power(P,k,p),p)
                ck("elementary_kernel_dimensions",actual==d*min(k,a))
            # Consecutive kernel differences recover block length a and count 1.
            ds=[len(A)-rank(power(P,k,p),p) for k in range(a+3)]
            ck("elementary_kernel_second_differences",all((2*ds[k]-ds[k-1]-ds[k+1])//d==int(k==a) for k in range(1,a+1)))

# Nilpotent Jordan decomposition: every partition of 1..7, over F2,F3.
def partitions(n,cap=None):
    if n==0:yield ()
    else:
        for k in range(min(n,cap or n),0,-1):
            for tail in partitions(n-k,k):yield (k,)+tail
for p in (2,3):
    for n in range(1,8):
        for sizes in partitions(n):
            A=()
            for size in sizes:A=blockdiag(A,jordan(size,0,p)) if A else jordan(size,0,p)
            ds=[n-rank(power(A,k,p),p) for k in range(n+2)]
            ck("Jordan_kernel_filtration",all(ds[k]==sum(min(k,s) for s in sizes) for k in range(n+2)))
            ck("Jordan_block_sizes_from_second_difference",all(2*ds[k]-ds[k-1]-ds[k+1]==sizes.count(k) for k in range(1,n+1)))
            ck("Jordan_nilpotence_index",power(A,max(sizes),p)==zero(n) and (max(sizes)==1 or power(A,max(sizes)-1,p)!=zero(n)))
            if n<=4:
                ck("Jordan_characteristic_polynomial",detpol(signed_poly_matrix(A,p),p)==(0,)*n+(1,))
                ck("Jordan_minimal_polynomial",minpoly(A,p)==(0,)*max(sizes)+(1,))

# Chinese remainder polynomial projectors and Hasse coefficients for two generalized eigenvalues.
for p in (2,3):
    for a in range(1,4):
        for b in range(1,4):
            A=blockdiag(jordan(a,0,p),jordan(b,1,p));n=a+b
            f0=(0,)*(a)+(1,);f1=powpoly((-1,1),b,p)
            q0=next((q for q in product(range(p),repeat=n)
                 if divmodp(plus(q,(-1,),p),f0,p)[1]==() and divmodp(q,f1,p)[1]==()),None)
            ck("CRT_projector_exists",q0 is not None)
            P0=peval(q0,A,p);P1=ms(eye(n),P0,p)
            exp0=blockdiag(eye(a),zero(b))
            ck("CRT_projector_correct",P0==exp0)
            ck("CRT_projector_idempotent",mm(P0,P0,p)==P0 and mm(P1,P1,p)==P1 and mm(P0,P1,p)==zero(n))
            S=scale(P1,1,p);N=ms(A,S,p)
            ck("Chevalley_commutative",mm(S,N,p)==mm(N,S,p))
            ck("Chevalley_nilpotent",power(N,max(a,b),p)==zero(n))
            ck("Chevalley_semisimple",S==blockdiag(zero(a),eye(b)))
            for deg in range(7):
                coeff=tuple((j*j+deg+j+1)%p for j in range(deg+1))
                rhs=zero(n)
                for lam,exp,P in ((0,a,P0),(1,b,P1)):
                    for j in range(exp):
                        hj=sum(coeff[k]*comb(k,j)*pow(lam,k-j) for k in range(j,len(coeff)))%p
                        rhs=ma(rhs,scale(mm(power(N,j,p),P,p),hj,p),p)
                ck("Hasse_Taylor_functional_calculus",peval(coeff,A,p)==rhs)

print("LA17-LA20 independent exact-field classification checks, no external packages")
print("CASE MATRICES:",len(cases))
for key,value in sorted(checks.items()):print(key,value)
print("TOTAL PASS:",sum(checks.values()))
print("SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
