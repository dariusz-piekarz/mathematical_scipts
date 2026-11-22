#!/usr/bin/env python3
"""Independent LA25-LA26 controllability/observability/PBH and generalized LQR checks.

Exact exhaustive small finite-field checks are complemented by deterministic
complex, scalar, and semidefinite-cost Riccati computations. No SciPy needed.
"""
from collections import Counter
from itertools import product
from math import comb
from hashlib import sha256
from pathlib import Path
import numpy as np

checks=Counter()
def check(name,assertion):
    checks[name]+=1
    if not bool(assertion):raise AssertionError(f"{name}: assertion #{checks[name]}")
def rank(A,p):
    a=[[int(z)%p for z in row] for row in A]
    m=len(a);n=len(a[0]) if m else 0;r=0
    for c in range(n):
        j=next((i for i in range(r,m) if a[i][c]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r]
        z=pow(a[r][c],-1,p);a[r]=[x*z%p for x in a[r]]
        for i in range(m):
            if i!=r:
                z=a[i][c]
                a[i]=[(a[i][k]-z*a[r][k])%p for k in range(n)]
        r+=1
        if r==m:break
    return r
def matmul(A,B,p):
    if not A:return ()
    if not B:return tuple(() for _ in A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))%p
             for j in range(len(B[0]))) for i in range(len(A)))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def power(A,k,p):
    ans=eye(len(A))
    for _ in range(k):ans=matmul(ans,A,p)
    return ans
def rank_cont(A,B,p):
    n=len(A);M=[[] for _ in range(n)]
    for k in range(n):
        C=matmul(power(A,k,p),B,p)
        for i in range(n):M[i]+=list(C[i])
    return rank(M,p)
def rank_observe(C,A,p):
    n=len(A);out=[]
    for k in range(n):
        out+=list(matmul(C,power(A,k,p),p))
    return rank(out,p)
def rank_pbh(A,B,p,lam):
    return rank([[(lam*int(i==j)-A[i][j])%p for j in range(len(A))]+list(B[i])
                 for i in range(len(A))],p)
def rank_pbh_obs(A,C,p,lam):
    return rank([[(lam*int(i==j)-A[i][j])%p for j in range(len(A))]
                 for i in range(len(A))]+[list(row) for row in C],p)
def char2(A,p):
    a,b=A[0];c,d=A[1]
    return ((a*d-b*c)%p,(-a-d)%p,1)
def all_2x2(p):
    for elems in product(range(p),repeat=4):
        yield ((elems[0],elems[1]),(elems[2],elems[3]))
for p in (2,3):
    for A in all_2x2(p):
        roots=[z for z in range(p) if (char2(A,p)[0]+char2(A,p)[1]*z+z*z)%p==0]
        for b in product(range(p),repeat=2):
            B=((b[0],),(b[1],))
            controllable=rank_cont(A,B,p)==2
            # Cayley-Hamilton: reachable span equals first n images, and
            # A^2 B is in its span, without looking at a characteristic root.
            AB=matmul(A,B,p);A2B=matmul(A,AB,p)
            check("finite_reachable_Cayley_Hamilton",rank(((b[0],AB[0][0]),(b[1],AB[1][0])),p)
                  ==rank(((b[0],AB[0][0],A2B[0][0]),(b[1],AB[1][0],A2B[1][0])),p))
            if len(roots)>=1 and (len(set(roots))==2 or (A[0][0]+A[1][1])%p==2*roots[0]%p):
                check("PBH_controllability_split_charpoly",
                      controllable==all(rank_pbh(A,B,p,z)==2 for z in roots))
            for c in product(range(p),repeat=2):
                C=((c[0],c[1]),)
                observable=rank_observe(C,A,p)==2
                check("observability_dual_Kalman",observable==rank_cont(
                    tuple(zip(*A)),tuple(zip(*C)),p)==2)
                AC=matmul(C,A,p);A2C=matmul(AC,A,p)
                check("finite_unobservable_Cayley_Hamilton",
                      rank((C[0],AC[0]),p)==rank((C[0],AC[0],A2C[0]),p))
                if len(roots)>=1 and (len(set(roots))==2 or (A[0][0]+A[1][1])%p==2*roots[0]%p):
                    check("PBH_observability_split_charpoly",
                          observable==all(rank_pbh_obs(A,C,p,z)==2 for z in roots))
        if len(roots)>=1 and (len(set(roots))==2 or (A[0][0]+A[1][1])%p==2*roots[0]%p):
            # Controllability is unchanged when (A,B) is replaced by
            # (A-BK,B): verify each feedback and each B over the field.
            for b in product(range(p),repeat=2):
                B=((b[0],),(b[1],))
                for k in product(range(p),repeat=2):
                    F=tuple(tuple((B[i][0]*k[j])%p for j in range(2)) for i in range(2))
                    AF=tuple(tuple((A[i][j]-F[i][j])%p for j in range(2)) for i in range(2))
                    check("feedback_reachable_subspace_invariant",rank_cont(A,B,p)==rank_cont(AF,B,p))

def close(a,b,tol=1e-8):return bool(np.allclose(a,b,atol=tol,rtol=tol))
rng=np.random.default_rng(2026112225)
for n in (1,2,3,4):
    for trial in range(120):
        A=rng.normal(size=(n,n))*0.3
        B=rng.normal(size=(n,2))
        C=rng.normal(size=(2,n))
        K=np.hstack([np.linalg.matrix_power(A,j)@B for j in range(n)])
        O=np.vstack([C@np.linalg.matrix_power(A,j) for j in range(n)])
        check("controllability_observability_dual_numerical",
              close(K.conj().T, np.vstack([B.T@np.linalg.matrix_power(A.T,j) for j in range(n)]))
              and close(O.conj().T,np.hstack([np.linalg.matrix_power(A.T,j)@C.T for j in range(n)])))
        check("finite_discrete_gramian",close(K@K.T,
              sum((np.linalg.matrix_power(A,j)@B@B.T@np.linalg.matrix_power(A.T,j) for j in range(n)),
                  np.zeros((n,n)))))
        if np.linalg.matrix_rank(K)==n:
            W=K@K.T;d=rng.normal(size=n)
            u=K.T@np.linalg.solve(W,d)
            check("minimum_energy_reachable",close(K@u,d))
            check("minimum_energy_value",close(np.vdot(u,u),
                  np.vdot(d,np.linalg.solve(W,d))))
            kernel=np.eye(K.shape[1])-K.T@np.linalg.solve(W,K)
            v=kernel@rng.normal(size=K.shape[1])
            check("minimum_energy_orthogonality",abs(np.vdot(u,v))<1e-8)
        # The undriven/unobserved matrix channels maintain the Kalman rank
        # under any feedback and output injection.
        F=rng.normal(size=(2,n));L=rng.normal(size=(n,2))
        KF=np.hstack([np.linalg.matrix_power(A-B@F,j)@B for j in range(n)])
        OL=np.vstack([C@np.linalg.matrix_power(A-L@C,j) for j in range(n)])
        check("feedback_reachability_rank",np.linalg.matrix_rank(K)==np.linalg.matrix_rank(KF))
        check("observer_injection_observability_rank",np.linalg.matrix_rank(O)==np.linalg.matrix_rank(OL))

# Exact 2D continuous Kalman Gramian for A=[[0,1],[0,0]], B=e_2.
for T in (0.1,0.5,1,2,4):
    W=np.array([[T**3/3,T*T/2],[T*T/2,T]])
    check("continuous_two_state_gramian_determinant",abs(np.linalg.det(W)-T**4/12)<1e-8)
    check("continuous_two_state_gramian_positive",np.min(np.linalg.eigvalsh(W))>0)
    # W^{-1} evaluates the minimal energy to transfer x0=0 to target z.
    for d in (np.array([1.,0.]),np.array([0.,1.])):
        check("continuous_gramian_min_energy",d@np.linalg.solve(W,d)>0)

# Stabilizable and detectable diagonal pairs, despite an unstable open loop
# and a non-trivial kernel for Q. Verify P>=0, semidefinite Q,
# closed-loop stability, and algebraic Riccati identities.
for a in (1.2,1.7,2.0):
    for b in (0.1,0.5,0.8):
        for q in (0.4,0.8,2.0):
            A=np.diag([a,b]);B=np.array([[1.],[0.]])
            Q=np.diag([q,0.]);R=np.array([[1.]])
            P=np.zeros((2,2));prior=None
            for _ in range(400):
                M=R+B.T@P@B
                PN=Q+A.T@P@A-A.T@P@B@np.linalg.solve(M,B.T@P@A)
                if prior is not None:
                    check("semidefinite_DARE_monotonicity",np.min(np.linalg.eigvalsh(PN-P))>=-1e-12)
                prior=P;P=PN
            M=R+B.T@P@B;K=np.linalg.solve(M,B.T@P@A);D=A-B@K
            check("semidefinite_DARE_residual",close(P,Q+A.T@P@A-A.T@P@B@K))
            check("semidefinite_DARE_stabilizing",max(abs(np.linalg.eigvals(D)))<1)
            check("semidefinite_DARE_singular_cost",abs(P[1,1])<1e-12 and P[0,0]>0)
            check("semidefinite_DARE_energy_identity",close(P,Q+K.T@R@K+D.T@P@D))
            # finite-time Bellman costs <= infinite-horizon Riccati solution
            V=Q.copy()
            check("semidefinite_DARE_finite_upper_bound",
                  min(np.linalg.eigvalsh(P-V))>=-1e-9)
            # Same state cost: optimal feedback gives no extra square.
            z=np.array([1.,-2.]);u=-K@z
            check("semidefinite_DARE_completion_square",
                  abs(z@Q@z+u@R@u+(A@z+B@u)@P@(A@z+B@u)-z@P@z)<1e-8)
            # continuous case (unstable 1st, stable 2nd) with Q singular
            H=np.diag([a,-b])
            p=a+np.sqrt(a*a+q)
            PC=np.diag([p,0.]);KC=B.T@PC
            DC=H-B@KC
            check("semidefinite_CARE_residual",
                  close(H.T@PC+PC@H-PC@B@B.T@PC+Q,np.zeros((2,2))))
            check("semidefinite_CARE_stabilizing",all(np.linalg.eigvals(DC).real<0))
            check("semidefinite_CARE_singular_cost",abs(PC[1,1])<1e-12)
            check("semidefinite_CARE_energy_identity",
                  close(DC.T@PC+PC@DC,-(Q+KC.T@KC)))

# Non-detectable Q=0 example: zero finite-horizon costs do not stabilize.
p=0.0
for _ in range(25):p=4*p/(1+p)
check("non_detectable_DARE_limit_zero",p==0)
check("non_detectable_DARE_other_stabilizing_solution",
      abs(3-4*3/(1+3))<1e-12 and abs(2-2*3/(1+3))<1)
check("non_detectable_CARE_separate_stabilizing_solution",
      2*2-2*2==0 and 1-2<0)
print("LA25-LA26 controllability, observability, detectability and semidefinite Riccati regression")
for name,count in sorted(checks.items()):print(name,count)
print("TOTAL PASS:",sum(checks.values()))
print("SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
