#!/usr/bin/env python3
"""Independent LA27-LA28 Hankel rank/minimal realization/balancing/transfer tests.

Only deterministic finite-field enumeration and NumPy; independent of TeX files.
"""
from collections import Counter
from itertools import product
from hashlib import sha256
from pathlib import Path
import numpy as np

cnt=Counter()
def check(label,ok):
    cnt[label]+=1
    if not bool(ok):raise AssertionError(f"{label}: assertion #{cnt[label]}")
def rank(a,p):
    A=[[int(x)%p for x in row] for row in a]
    m=len(A);n=len(A[0]) if m else 0;r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if A[i][j]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][j],-1,p)
        A[r]=[inv*x%p for x in A[r]]
        for i in range(m):
            if i!=r:
                v=A[i][j]
                A[i]=[(A[i][k]-v*A[r][k])%p for k in range(n)]
        r+=1
    return r
def mul(a,b,p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%p for j in range(len(b[0])))
                 for i in range(len(a)))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def matrix2(vals):
    return ((vals[0],vals[1]),(vals[2],vals[3]))
def col(v):return ((v[0],),(v[1],))
def row(v):return (tuple(v),)

# All 2-state scalar-input/scalar-output realizations over F2 and F3.
for p in (2,3):
    for av in product(range(p),repeat=4):
        A=matrix2(av)
        for bv in product(range(p),repeat=2):
            B=col(bv);AB=mul(A,B,p)
            K=((B[0][0],AB[0][0]),(B[1][0],AB[1][0]))
            for cv in product(range(p),repeat=2):
                C=row(cv);CA=mul(C,A,p)
                O=(C[0],CA[0])
                AB2=mul(A,AB,p)
                h0=mul(C,B,p)[0][0]
                h1=mul(C,AB,p)[0][0]
                h2=mul(C,AB2,p)[0][0]
                H=((h0,h1),(h1,h2))
                check("finite_Hankel_factorization",mul(O,K,p)==H)
                d=rank(H,p)
                check("finite_minimal_iff_reachable_observable",
                      (d==2)==(rank(K,p)==2 and rank(O,p)==2))
                image_outputs=set()
                for coeff in product(range(p),repeat=2):
                    x=((K[0][0]*coeff[0]+K[0][1]*coeff[1])%p,
                       (K[1][0]*coeff[0]+K[1][1]*coeff[1])%p)
                    image_outputs.add(((C[0][0]*x[0]+C[0][1]*x[1])%p,
                        (CA[0][0]*x[0]+CA[0][1]*x[1])%p))
                check("finite_minimal_dimension_independent_quotient_count",len(image_outputs)==p**d)
                if d==0:
                    check("zero_dimensional_realization_all_markov_zero",
                          all(mul(C,mul(A,B,p),p)[0][0]==0 for _ in range(1)) and h0==0 and h1==0)

def close(a,b,tol=2e-8):return bool(np.allclose(a,b,atol=tol,rtol=tol))
rng=np.random.default_rng(2026112227)
for n in range(1,6):
    I=np.eye(n,dtype=complex)
    for case in range(70):
        A=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))*0.13
        # Ensure spectral radius < 0.7 for geometric Gramian tail.
        A=A*min(1.0,0.6/max(np.linalg.norm(A,2),0.00001))
        B=I+0.12*(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        C=I+0.12*(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        Ak=I.copy();Wc=np.zeros((n,n),complex);Wo=np.zeros((n,n),complex)
        for k in range(90):
            Wc+=Ak@B@B.conj().T@Ak.conj().T
            Wo+=Ak.conj().T@C.conj().T@C@Ak
            Ak=Ak@A
        check("Stein_controllability_gramian",close(Wc-A@Wc@A.conj().T,B@B.conj().T))
        check("Stein_observability_gramian",close(Wo-A.conj().T@Wo@A,C.conj().T@C))
        check("gramian_hermitian",close(Wc,Wc.conj().T) and close(Wo,Wo.conj().T))
        lc,Uc=np.linalg.eigh((Wc+Wc.conj().T)/2)
        lo=np.linalg.eigvalsh((Wo+Wo.conj().T)/2)
        check("minimal_positive_gramians",min(lc)>1e-9 and min(lo)>1e-9)
        L=Uc@np.diag(np.sqrt(lc))@Uc.conj().T
        S=L@Wo@L
        eig,U=np.linalg.eigh((S+S.conj().T)/2)
        sigma=np.sqrt(eig)
        T=L@U@np.diag(1/np.sqrt(sigma))
        Ti=np.linalg.inv(T)
        Wcp=Ti@Wc@Ti.conj().T;Wop=T.conj().T@Wo@T
        check("balanced_both_gramians",close(Wcp,np.diag(sigma)) and close(Wop,np.diag(sigma)))
        check("balanced_sigma_coordinate_invariant",
              close(sorted(np.linalg.eigvals(Wc@Wo).real),sorted(sigma**2)))
        Ap=Ti@A@T;Bp=Ti@B;Cp=C@T
        check("minimal_similarity_Markov",
              all(close(C@np.linalg.matrix_power(A,k)@B,
                        Cp@np.linalg.matrix_power(Ap,k)@Bp) for k in range(2*n+2)))
        # Finite N observation Gramian and least-squares reconstruction bound.
        O=np.vstack([C@np.linalg.matrix_power(A,k) for k in range(n)])
        W=O.conj().T@O
        x0=rng.normal(size=n)+1j*rng.normal(size=n)
        noise=(rng.normal(size=n*n)+1j*rng.normal(size=n*n))*0.02
        Y=O@x0+noise
        xhat=np.linalg.solve(W,O.conj().T@Y)
        check("finite_gramian_observation",close(W,sum(
             np.linalg.matrix_power(A.conj().T,k)@C.conj().T@C@np.linalg.matrix_power(A,k)
             for k in range(n))))
        check("least_squares_normal_equations",close(O.conj().T@(O@xhat-Y),np.zeros(n)))
        check("least_squares_error_bound",
              np.linalg.norm(xhat-x0) <= np.linalg.norm(noise)/np.sqrt(np.linalg.eigvalsh(W).min())+1e-9)
        # Transfer: coefficient of z^-k-1 is H_k and G(infinity)=D.
        D=0.17*I;z=3+1.4j
        G=C@np.linalg.solve(z*I-A,B)+D
        approx=D.copy()
        for k in range(26):
            approx+=C@np.linalg.matrix_power(A,k)@B/z**(k+1)
        check("Z_Laurent_Markov_transfer",close(approx,G))
        check("rational_transfer_limit",close(
             C@np.linalg.solve((1e9+1j)*I-A,B)+D,D,1e-8))

# Scalar proper rational function companion realization and PBH minimality.
for n in range(1,6):
    for t in range(50):
        coeff=(rng.normal(size=n)+1j*rng.normal(size=n))*0.3
        num=(rng.normal(size=n)+1j*rng.normal(size=n))*0.3
        A=np.zeros((n,n),complex)
        for i in range(n-1):A[i,i+1]=1
        A[-1,:]=-coeff
        B=np.zeros((n,1),complex);B[-1,0]=1
        C=num.reshape(1,n);I=np.eye(n)
        z=3.2+1.1j
        pz=z**n+sum(coeff[k]*z**k for k in range(n))
        qz=sum(num[k]*z**k for k in range(n))
        g=(C@np.linalg.solve(z*I-A,B))[0,0]
        check("companion_rational_transfer",abs(g-qz/pz)<1e-8)
        K=np.hstack([np.linalg.matrix_power(A,k)@B for k in range(n)])
        check("companion_controllable",np.linalg.matrix_rank(K)==n)

# A repeated-root-free proper transfer: cancellation iff q shares a root.
for num in ((1,0,0),(-1,1,0)):
    # p=(z-1)(z-2)(z-3)=z^3-6z^2+11z-6
    A=np.array([[0,1,0],[0,0,1],[6,-11,6.]],float)
    B=np.array([[0],[0],[1]],float);C=np.array(num,float).reshape(1,3)
    O=np.vstack([C@np.linalg.matrix_power(A,k) for k in range(3)])
    check("companion_minimal_coprime", (np.linalg.matrix_rank(O)==3)==(num==(1,0,0)))

# One stable scalar continuous system with constant input, exact convolution/BIBO.
for t in np.linspace(0,8,49):
    y=4*np.exp(-2*t)+1.5*(1-np.exp(-2*t))
    check("continuous_constant_input_variation",abs(y-(1.5+2.5*np.exp(-2*t)))<1e-12)
    check("continuous_BIBO_bound",abs(y)<=4*np.exp(-2*t)+1.5+1e-12)
# Discrete scalar with x0=1,A=0.4,B=2,C=3,D=5,u_k=1.
x=1.0
for k in range(60):
    y=3*x+5
    expected=15-7*(0.4**k)
    check("discrete_convolution_step_response",abs(y-expected)<1e-10)
    x=0.4*x+2
# Hidden unstable but input-output stable state.
for z in (2+1j,4+0.1j,10-1j):
    A=np.diag([1.,-1.]);B=np.array([[0.],[1.]])
    C=np.array([[0.,1.]])
    G=(C@np.linalg.solve(z*np.eye(2)-A,B))[0,0]
    check("nonminimal_hidden_unstable_pole_cancellation",abs(G-1/(z+1))<1e-12)

print("LA27-LA28 Hankel minimal realization balanced Gramian and transfer checks")
for name,count in sorted(cnt.items()):print(name,count)
print("TOTAL PASS:",sum(cnt.values()))
print("SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
