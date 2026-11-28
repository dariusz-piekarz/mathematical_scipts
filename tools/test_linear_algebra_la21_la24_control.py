#!/usr/bin/env python3
"""Independent LA21-LA24 finite-field commutant/Sylvester, Lyapunov, and Riccati checks.
No random tests: finite-field enumeration is exhaustive in the stated sizes;
complex matrix tests use a reproducible fixed-seed generator.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import hashlib
from pathlib import Path
import numpy as np

totals=Counter()
def check(name,condition):
    totals[name]+=1
    if not bool(condition):raise AssertionError(f"{name} failed at assertion #{totals[name]}")

def rank(M,p):
    a=[[int(x)%p for x in row] for row in M]
    m=len(a);n=len(a[0]) if m else 0;r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p);a[r]=[x*inv%p for x in a[r]]
        for i in range(m):
            if i!=r:
                v=a[i][j]
                a[i]=[(a[i][k]-v*a[r][k])%p for k in range(n)]
        r+=1
    return r
def mm(A,B,p):
    if not A:return ()
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%p
                        for j in range(len(B[0]))) for i in range(len(A)))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def add(A,B,p):
    return tuple(tuple((A[i][j]+B[i][j])%p for j in range(len(A[0]))) for i in range(len(A)))
def neg(A,p):return tuple(tuple(-v%p for v in row) for row in A)
def scale(A,s,p):return tuple(tuple(s*v%p for v in row) for row in A)
def polytrim(a,p):
    a=[int(x)%p for x in a]
    while a and not a[-1]:a.pop()
    return tuple(a)
def polydiv(a,b,p):
    a=polytrim(a,p);b=polytrim(b,p)
    if not b:raise ZeroDivisionError
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        off=len(a)-len(b);v=a[-1]*pow(b[-1],-1,p)%p;q[off]=v
        a=polytrim([a[j] - (v*b[j-off] if off<=j<off+len(b) else 0) for j in range(len(a))],p)
    return polytrim(q,p),a
def gcd(a,b,p):
    a=polytrim(a,p);b=polytrim(b,p)
    while b:a,b=b,polydiv(a,b,p)[1]
    if not a:return ()
    return tuple(x*pow(a[-1],-1,p)%p for x in a)
def charpoly(A,p):
    n=len(A)
    if n==1:return ((-A[0][0])%p,1)
    if n==2:
        a,b=A[0];c,d=A[1]
        return ((a*d-b*c)%p,(-a-d)%p,1)
    if n==0:return (1,)
    raise ValueError("small n only")
def sylvester_operator(A,B,p):
    n=len(A);m=len(B);cols=[]
    for t in range(n*m):
        E=tuple(tuple(int(i==t//m and j==t%m) for j in range(m)) for i in range(n))
        AE=mm(A,E,p);EB=mm(E,B,p)
        cols.append(tuple((AE[i][j]-EB[i][j])%p for i in range(n) for j in range(m)))
    return tuple(tuple(cols[k][i] for k in range(n*m)) for i in range(n*m))
def commutant_dim(A,p):
    n=len(A)
    return n*n-rank(sylvester_operator(A,A,p),p)
def powmat(A,k,p):
    R=eye(len(A))
    for _ in range(k):R=mm(R,A,p)
    return R
def companion(f,p):
    n=len(f)-1
    return tuple(tuple((int(i==j+1) if j<n-1 else -f[i])%p for j in range(n)) for i in range(n))
def polys_eval(c,A,p):
    n=len(A);R=tuple(tuple(0 for j in range(n)) for i in range(n))
    for z in reversed(c):R=add(mm(R,A,p),scale(eye(n),z,p),p)
    return R
def matrices(n,p):
    for e in product(range(p),repeat=n*n):
        yield tuple(tuple(e[n*i+j] for j in range(n)) for i in range(n))

# Exact commutants, cyclicity and Sylvester spectral criterion.
for p,n in ((2,1),(2,2),(2,3),(3,1),(3,2)):
    for A in matrices(n,p):
        dim=commutant_dim(A,p)
        check("commutant_bounds",n<=dim<=n*n)
        scalar=all(A[i][j]==(A[0][0] if i==j else 0) for i in range(n) for j in range(n))
        check("commutant_maximum_iff_scalar", (dim==n*n)==scalar)
        powerlist=[powmat(A,k,p) for k in range(n)]
        cyclic=any(rank([[sum(powerlist[k][i][j]*v[j] for j in range(n))%p for k in range(n)]
                         for i in range(n)],p)==n for v in product(range(p),repeat=n))
        check("commutant_minimum_iff_cyclic", (dim==n)==cyclic)
        if n==2:
            for B in matrices(2,p):
                ker_dim=4-rank(sylvester_operator(A,B,p),p)
                coprime=gcd(charpoly(A,p),charpoly(B,p),p)==(1,)
                check("Sylvester_unique_iff_coprime_charpolys",(ker_dim==0)==coprime)
            for b in range(p):
                B=((b,),)
                ker_dim=2-rank(sylvester_operator(A,B,p),p)
                check("Sylvester_scalar_intertwiner_dim",
                      ker_dim==n-rank(tuple(tuple((A[i][j]-b*int(i==j))%p for j in range(n)) for i in range(n)),p))
            # Jordan-block intertwining with arbitrary lambda,mu over Fp.
            for la in range(p):
                JA=((la,1),(0,la))
                for mu in range(p):
                    JB=((mu,1),(0,mu))
                    dimJ=4-rank(sylvester_operator(JA,JB,p),p)
                    check("Jordan_intertwiner_equal_eigenvalues",dimJ==(2 if la==mu else 0))

# Cyclic finite-field centralizer unit count, including irreducible quadratics and repeated roots.
for p in (2,3,5):
    for a,b in product(range(p),repeat=2):
        f=(a,b,1)
        A=companion(f,p)
        check("cyclic_companion_centralizer_dim",commutant_dim(A,p)==2)
        units=0
        for x,y in product(range(p),repeat=2):
            X=add(scale(eye(2),x,p),scale(A,y,p),p)
            if rank(X,p)==2:units+=1
        roots=[z for z in range(p) if (a+b*z+z*z)%p==0]
        expected=Fraction(p*p,1)
        if roots:
            for z in set(roots):expected*=Fraction(p-1,p)
        else:
            expected*=Fraction(p*p-1,p*p)
        check("finite_cyclic_centralizer_unit_formula",units==expected)

# Exact Jordan-centralizer dimensions, including repeated blocks.
for p in (2,3):
    for a,b in ((1,1),(2,1),(2,2),(3,1)):
        n=a+b
        JA=tuple(tuple(int(j==i+1) for j in range(a)) for i in range(a))
        JB=tuple(tuple(int(j==i+1) for j in range(b)) for i in range(b))
        X=tuple((tuple(JA[i])+tuple([0]*b)) for i in range(a))+tuple(tuple([0]*a)+tuple(JB[i]) for i in range(b))
        expected=a+b+2*min(a,b)
        check("two_Jordan_blocks_centralizer_dimension",commutant_dim(X,p)==expected)

def close(A,B,tol=1e-8):return bool(np.allclose(A,B,atol=tol,rtol=tol))
def positive(A):return bool(np.min(np.linalg.eigvalsh((A+A.conj().T)/2))>1e-10)
rng=np.random.default_rng(2026112224)
for n in (1,2,3):
    I=np.eye(n,dtype=complex)
    for _ in range(70):
        M=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))*0.2
        Q=I+M.conj().T@M
        A=-(I+M.conj().T@M)+0.25*(M-M.conj().T)
        # vec_F(A*P+PA)=(I⊗A*+A^T⊗I)vec_F(P)
        L=np.kron(I,A.conj().T)+np.kron(A.T,I)
        P=np.linalg.solve(L,(-Q).reshape(n*n,order="F")).reshape((n,n),order="F")
        check("continuous_Lyapunov_hermitian",close(P,P.conj().T))
        check("continuous_Lyapunov_positive",positive(P))
        check("continuous_Lyapunov_residual",close(A.conj().T@P+P@A,-Q))
        eig=np.linalg.eigvals(A)
        check("continuous_Lyapunov_Hurwitz",all(eig.real<0))
        z=rng.normal(size=n)+1j*rng.normal(size=n)
        check("continuous_energy_derivative_sign",np.vdot(z,(A.conj().T@P+P@A)@z).real<0)
        D=M/(1.1+np.linalg.norm(M,2)) # strictly contractive, Schur
        St=np.eye(n*n)-np.kron(D.T,D.conj().T)
        W=np.linalg.solve(St,Q.reshape(n*n,order="F")).reshape((n,n),order="F")
        check("discrete_Lyapunov_hermitian",close(W,W.conj().T))
        check("discrete_Lyapunov_positive",positive(W))
        check("discrete_Lyapunov_residual",close(D.conj().T@W@D-W,-Q))
        check("discrete_Schur_stability",max(abs(np.linalg.eigvals(D)))<1)
        z=rng.normal(size=n)+1j*rng.normal(size=n)
        check("discrete_energy_difference",close(np.vdot(D@z,W@(D@z))-np.vdot(z,W@z),-np.vdot(z,Q@z)))
        # Series identity P=sum_{k=0}^infty (A*)^k Q A^k
        accum=np.zeros((n,n),complex);Ak=I.copy()
        for j in range(28):
            accum+=Ak.conj().T@Q@Ak
            Ak=Ak@D
        check("discrete_Lyapunov_series",close(accum,W))
        # Stein-operator eigenvalues: products of conjugate eigenvalues.
        E=np.linalg.eigvals(D)
        stein=np.kron(D.T,D.conj().T)
        expected=[np.conj(x)*y for x in E for y in E]
        actual=np.linalg.eigvals(stein)
        # Complex eigenvalue sorting is numerically unstable for conjugate
        # products whose real parts agree up to roundoff; match the multiset.
        pool=list(expected)
        multiset_ok=True
        for z in actual:
            j=min(range(len(pool)),key=lambda k:abs(pool[k]-z))
            if abs(pool[j]-z)>1e-7:
                multiset_ok=False
                break
            pool.pop(j)
        check("Stein_operator_spectrum",multiset_ok and not pool)

# Scalar DARE: fixed point and stabilizing branch, with B=R=1, Q>0, |A|<1.
for a in (-0.85,-0.5,0,0.5,0.85):
    for q in (0.5,1,3):
        p=0.0;history=[p]
        for _ in range(250):
            p=q+a*a*p-a*a*p*p/(1+p)
            history.append(p)
        c=(1-a*a)-q
        root=(-c+np.sqrt(c*c+4*q))/2
        check("DARE_converges_to_positive_solution",abs(p-root)<1e-10)
        check("DARE_monotonicity",all(history[k+1]+1e-12>=history[k] for k in range(len(history)-1)))
        check("DARE_residual",abs(p-(q+a*a*p-a*a*p*p/(1+p)))<1e-10)
        K=p*a/(1+p);Acl=a-K
        check("DARE_closed_loop_stabilizing",abs(Acl)<1)
        check("DARE_scalar_completion_square",abs(p-(q+K*K+Acl*Acl*p))<1e-10)
        anti=(-c-np.sqrt(c*c+4*q))/2
        if abs(1+anti)>1e-9:
            ka=anti*a/(1+anti)
            check("DARE_other_root_not_stabilizing",abs(a-ka)>=1-1e-9)

# Scalar CARE: stable A, B=R=1 and positive Q, solved by Riccati ODE.
for a in (-0.5,-1,-2):
    for q in (0.5,1,3):
        root=a+np.sqrt(a*a+q)
        check("CARE_scalar_residual",abs(2*a*root-root*root+q)<1e-10)
        check("CARE_closed_loop_Hurwitz",a-root<0)
        s=0.0;dt=0.005
        def rhs(x):return 2*a*x-x*x+q
        for k in range(2500):
            k1=rhs(s);k2=rhs(s+dt*k1/2);k3=rhs(s+dt*k2/2);k4=rhs(s+dt*k3)
            s+=dt*(k1+2*k2+2*k3+k4)/6
        check("DRE_converges_CARE",abs(s-root)<1e-8)
        check("CARE_scalar_completion_square",abs(2*(a-root)*root+(q+root*root))<1e-10)
        other=a-np.sqrt(a*a+q)
        check("CARE_other_root_not_stabilizing",a-other>0)

# Two-state examples with exact P=I, independent matrix equations.
I=np.eye(2)
Ac=np.diag([-1.,-2.]);Bc=I;Qc=np.diag([3.,5.]);Rc=I;Pc=I;Kc=Pc
check("CARE_two_state_exact",close(Ac.T@Pc+Pc@Ac-Pc@Bc@Bc.T@Pc+Qc,np.zeros((2,2))))
check("CARE_two_state_stable_feedback",all(np.linalg.eigvals(Ac-Bc@Kc).real<0))
Ad=np.diag([0.5,1/3]);Bd=I;Qd=np.diag([7/8,17/18]);Rd=I;Pd=I
Kd=np.linalg.solve(Rd+Bd.T@Pd@Bd,Bd.T@Pd@Ad)
check("DARE_two_state_exact",close(Qd+Ad.T@Pd@Ad-Ad.T@Pd@Bd@Kd,Pd))
check("DARE_two_state_stable_feedback",max(abs(np.linalg.eigvals(Ad-Bd@Kd)))<1)

print("LA21-LA24 independent exact-field and deterministic numerical regressions")
for key,value in sorted(totals.items()):print(key,value)
print("TOTAL PASS:",sum(totals.values()))
print("SHA256:",hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
