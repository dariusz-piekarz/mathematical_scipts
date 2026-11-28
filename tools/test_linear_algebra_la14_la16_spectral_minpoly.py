#!/usr/bin/env python3
"""Independent LA14-16 checks: exact finite-field minimal polynomials and complex spectral/SVD identities."""
from collections import Counter
from itertools import product, permutations
from hashlib import sha256
from pathlib import Path
import numpy as np

counts=Counter()
def check(tag,condition):
    counts[tag]+=1
    if not bool(condition):raise AssertionError((tag,counts[tag]))
def close(a,b):return np.allclose(a,b,atol=3e-8,rtol=3e-8)
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mm(A,B,p):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
def rank(A,p):
    A=[list(row) for row in A];m=len(A);n=len(A[0]) if m else 0;r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if A[i][col]%p),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][col],-1,p)
        A[r]=[v*inv%p for v in A[r]]
        for i in range(m):
            if i!=r:
                v=A[i][col];A[i]=[(A[i][j]-v*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r
def solve(M,b,p):
    """A column-system M x=b with many equations, few unknowns; return one solution or None."""
    m=len(M);n=len(M[0]) if m else 0
    A=[list(M[i])+[b[i]%p] for i in range(m)]
    r=0;pivots=[]
    for j in range(n):
        i=next((i for i in range(r,m) if A[i][j]),None)
        if i is None:continue
        A[r],A[i]=A[i],A[r]
        inv=pow(A[r][j],-1,p);A[r]=[(v*inv)%p for v in A[r]]
        for k in range(m):
            if k!=r:
                c=A[k][j];A[k]=[(A[k][z]-c*A[r][z])%p for z in range(n+1)]
        pivots.append(j);r+=1
    if any(not any(A[i][:n]) and A[i][n] for i in range(m)):return None
    ans=[0]*n
    for i,j in enumerate(pivots):ans[j]=A[i][n]
    return ans
def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c
def charpoly(A,p):
    n=len(A);out=[0]*(n+1)
    for perm in permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[1]
        for i in range(n):
            term=poly_mul(term,[(-A[i][perm[i]])%p,1] if perm[i]==i else [(-A[i][perm[i]])%p],p)
        fac=-1 if inv%2 else 1
        for j,x in enumerate(term):out[j]=(out[j]+fac*x)%p
    return out
def poly_val(c,x,p):return sum(v*pow(x,i,p) for i,v in enumerate(c))%p
def polyevalmat(c,A,p):
    n=len(A);I=eye(n);Z=tuple((0,)*n for _ in range(n))
    result=Z
    for t in reversed(c):
        result=mm(result,A,p)
        result=tuple(tuple((result[i][j]+t*I[i][j])%p for j in range(n)) for i in range(n))
    return result
def divisible(p,q,field):
    a=list(p);b=list(q);d=len(b)-1
    while len(a)>=len(b):
        c=a[-1]*pow(b[-1],-1,field)%field
        k=len(a)-len(b)
        for j in range(d+1):a[j+k]=(a[j+k]-c*b[j])%field
        while a and a[-1]==0:a.pop()
    return not a
def minpoly(A,p):
    n=len(A)
    if n==0:return [1]
    powers=[eye(n)]
    for degree in range(n+1):
        current=powers[degree]
        b=[x for row in current for x in row]
        M=[[powers[j][i//n][i%n] for j in range(degree)] for i in range(n*n)]
        coeff=solve(M,b,p)
        if coeff is not None:return [(-a)%p for a in coeff]+[1]
        powers.append(mm(current,A,p))
    raise AssertionError("Cayley-Hamilton search bound exceeded")
for p,n in ((2,0),(2,1),(2,2),(2,3),(3,2),(3,3),(5,2)):
    for elems in product(range(p),repeat=n*n):
        A=tuple(tuple(elems[n*i+j] for j in range(n)) for i in range(n))
        chi=charpoly(A,p);mini=minpoly(A,p)
        Z=tuple((0,)*n for _ in range(n))
        check("finite_Cayley_Hamilton",polyevalmat(chi,A,p)==Z)
        check("finite_minimal_polynomial_annihilates",polyevalmat(mini,A,p)==Z)
        check("finite_minimal_divides_characteristic",divisible(chi,mini,p))
        check("finite_minimal_degree_bound",len(mini)-1<=n)
        roots=[lam for lam in range(p) if poly_val(mini,lam,p)==0]
        diag=sum(n-rank(tuple(tuple((A[i][j]-lam*int(i==j))%p for j in range(n)) for i in range(n)),p) for lam in roots)==n
        split_sqfree=len(roots)==len(mini)-1
        check("finite_diagonalization_minpoly_criterion",diag==split_sqfree)
        check("finite_minpoly_roots_equal_charpoly_roots",all((poly_val(chi,lam,p)==0)==(poly_val(mini,lam,p)==0) for lam in range(p)))
        if n:
            v=tuple((i+sum(elems))%p for i in range(n))
            # The generated cyclic span is invariant and its dimension equals degree of its vector minimal polynomial.
            U=[v]
            for j in range(1,n+1):
                U.append(tuple(sum(A[i][k]*U[-1][k] for k in range(n))%p for i in range(n)))
            dims=[rank(tuple(tuple(U[j][i] for j in range(k)) for i in range(n)),p) for k in range(n+2)]
            check("finite_cyclic_subspace_stabilization",dims[-1]==dims[-2] and all(dims[k]<=dims[k+1] for k in range(n+1)))

rng=np.random.default_rng(2026112222)
def complexmat(m,n):return rng.normal(size=(m,n))+1j*rng.normal(size=(m,n))
for n in range(1,7):
    for j in range(120):
        Q,_=np.linalg.qr(complexmat(n,n))
        diag=np.array([((i+1)*(-1 if i%2 else 1)+1j*((i+2)%3)) for i in range(n)],complex)
        D=np.diag(diag)
        T=Q@D@Q.conj().T
        P=[np.outer(Q[:,i],Q[:,i].conj()) for i in range(n)]
        check("normal_decomposition",close(T@T.conj().T,T.conj().T@T))
        check("spectral_resolutions",close(sum(P),np.eye(n)) and close(sum(diag[i]*P[i] for i in range(n)),T))
        check("spectral_polynomial",close(np.linalg.matrix_power(T,3)-2*T+np.eye(n),Q@(D@D@D-2*D+np.eye(n))@Q.conj().T))
        check("normal_operator_norm",close(np.linalg.svd(T,compute_uv=False)[0],max(abs(diag))))
        check("spectral_trace_determinant",close(np.trace(T),sum(diag)) and close(np.linalg.det(T),np.prod(diag)))
        check("spectral_projector_polynomial",all(close(np.linalg.matrix_power(P[i],2),P[i]) for i in range(n)))
        # The normalized projectors equal products of spectral interpolation factors.
        for k in range(n):
            poly=np.eye(n,dtype=complex)
            for t in range(n):
                if t!=k:poly=poly@(T-diag[t]*np.eye(n))/(diag[k]-diag[t])
            check("spectral_Lagrange_projection",close(poly,P[k]))
        H=Q@np.diag(np.arange(1,n+1,dtype=float))@Q.conj().T
        v=complexmat(n,1)[:,0]
        ray=np.vdot(v,H@v).real/np.vdot(v,v).real
        check("Hermitian_Rayleigh_bounds",1-1e-8<=ray<=n+1e-8)
        check("Hermitian_positive_definite",np.vdot(v,H@v).real>0)
        S=Q@np.diag(np.arange(n,dtype=float))@Q.conj().T
        check("simultaneous_Hermitian",close(H@S,S@H))

for m in range(1,7):
    for n in range(1,7):
        for t in range(60):
            A=complexmat(m,n)
            if t%4==0:A[:,-1]=0
            if n>1 and t%7==0:A[:,-1]=A[:,0]
            U,s,Vh=np.linalg.svd(A,full_matrices=True)
            p=min(m,n);r=sum(s>1e-9)
            Sig=np.zeros((m,n),complex)
            for i in range(p):Sig[i,i]=s[i]
            check("SVD_reconstruction",close(U@Sig@Vh,A))
            check("SVD_rank",r==np.linalg.matrix_rank(A,tol=1e-9))
            Ap=np.linalg.pinv(A,rcond=1e-12)
            check("Penrose_1",close(A@Ap@A,A))
            check("Penrose_2",close(Ap@A@Ap,Ap))
            check("Penrose_3",close(A@Ap,(A@Ap).conj().T))
            check("Penrose_4",close(Ap@A,(Ap@A).conj().T))
            W=U@np.pad(np.diag([1]*r+[0]*(p-r)).astype(complex),((0,m-p),(0,n-p)))@Vh
            absA=Vh.conj().T@np.diag(s.tolist()+[0]*(n-p))@Vh
            check("polar_factorization",close(W@absA,A))
            check("polar_partial_isometry",close(W.conj().T@W,Ap@A))
            check("polar_kernel",close(W@np.eye(n)-W@(Ap@A),np.zeros((m,n))))
            for k in range(p+1):
                Ak=U[:,:k]@np.diag(s[:k])@Vh[:k,:]
                check("Eckart_Young_Frobenius",close(np.linalg.norm(A-Ak,ord="fro")**2,sum(s[k:]**2)))
                check("Eckart_Young_operator",close(np.linalg.norm(A-Ak,ord=2),s[k] if k<len(s) else 0))
            b=complexmat(m,1)[:,0];x=Ap@b
            check("least_squares_normal_equations",close(A.conj().T@(A@x-b),np.zeros(n)))
            check("least_squares_minnorm",close(Ap@A@x,x))
            if n<=m and r==n:
                Q,R=np.linalg.qr(A,mode="reduced")
                check("QR_full_column_rank",close(Q@R,A) and close(Q.conj().T@Q,np.eye(n)))
                H=A.conj().T@A
                L=np.linalg.cholesky(H)
                check("Cholesky_positive_gram",close(L@L.conj().T,H) and all(L[i,i].real>0 for i in range(n)))

# Commuting, non-diagonalizable upper-triangular matrices: Schur's simultaneous statement.
for n in range(1,7):
    J=np.diag(np.ones(n-1),1).astype(complex)
    S=2*np.eye(n)+J;T=np.eye(n)-3*J+J@J
    Q,_=np.linalg.qr(complexmat(n,n))
    SA=Q@S@Q.conj().T;TA=Q@T@Q.conj().T
    check("simultaneous_Schur_commuting",close(SA@TA,TA@SA))
    check("simultaneous_Schur_upper_triangular",close(Q.conj().T@SA@Q,S) and close(Q.conj().T@TA@Q,T))
print("LA14-LA16 spectral, matrix decomposition and minimal-polynomial checks")
for k,v in sorted(counts.items()):print(k,v)
print("TOTAL PASS:",sum(counts.values()))
print("SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
