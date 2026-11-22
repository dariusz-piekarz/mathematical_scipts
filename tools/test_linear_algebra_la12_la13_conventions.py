#!/usr/bin/env python3
"""LA12-13: independent complex scalar-product, Riesz, Gram, adjoint and projection checks."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import numpy as np

rng=np.random.default_rng(2026112219)
count=Counter()
def chk(name,ok):
    count[name]+=1
    if not bool(ok): raise AssertionError((name,count[name]))
def close(a,b): return np.allclose(a,b,rtol=3e-9,atol=3e-9)
def vec(n): return rng.normal(size=n)+1j*rng.normal(size=n)
def mat(m,n): return rng.normal(size=(m,n))+1j*rng.normal(size=(m,n))
def norm2(v): return np.vdot(v,v).real

for n in range(7):
    for _ in range(125):
        u,v,w=vec(n),vec(n),vec(n)
        a,b=rng.normal(size=2)+1j*rng.normal(size=2)
        pol=(norm2(u+v)-norm2(u-v)-1j*norm2(u+1j*v)+1j*norm2(u-1j*v))/4
        chk("polarization_antilinear_first",close(pol,np.vdot(u,v)))
        chk("sesquilinear_first",close(np.vdot(a*u+b*w,v),np.conj(a)*np.vdot(u,v)+np.conj(b)*np.vdot(w,v)))
        chk("linear_second",close(np.vdot(u,a*v+b*w),a*np.vdot(u,v)+b*np.vdot(u,w)))
        chk("cauchy_schwarz",abs(np.vdot(u,v))**2<=norm2(u)*norm2(v)+1e-8)
        chk("parallelogram",close(norm2(u+v)+norm2(u-v),2*norm2(u)+2*norm2(v)))
        c=vec(n)
        chk("riesz_conjugate_coefficients",close(np.vdot(np.conj(c),v),c@v))
        if n:
            Q,_=np.linalg.qr(mat(n,n))
            k=int(rng.integers(n+1))
            E=Q[:,:k]
            chk("bessel",np.linalg.norm(E.conj().T@v)**2<=norm2(v)+1e-8)
            chk("orthonormal_projection",close(E.conj().T@E,np.eye(k)))
            if k:
                residual=v-E@(E.conj().T@v)
                chk("bessel_equality_remainder",close(norm2(v),np.linalg.norm(E.conj().T@v)**2+norm2(residual)))

for m in range(7):
    for n in range(7):
        for t in range(75):
            A=mat(m,n)
            v,w=vec(n),vec(m)
            Ah=A.conj().T
            chk("adjoint_identity",close(np.vdot(A@v,w),np.vdot(v,Ah@w)))
            chk("gram_positive_semidefinite",np.vdot(v,Ah@A@v).real>=-1e-8)
            chk("gram_hermitian",close(Ah@A,(Ah@A).conj().T))
            x=np.linalg.pinv(A,rcond=1e-13)@w
            chk("normal_equations",close(Ah@(A@x-w),np.zeros(n)))
            chk("minnorm_solution",close(np.linalg.pinv(A,rcond=1e-13)@A@x,x))
            U,S,Vh=np.linalg.svd(A,full_matrices=True)
            rank=sum(s>1e-10 for s in S)
            null=Vh[rank:,:].conj().T
            chk("kernel_dimension",null.shape==(n,n-rank) and close(A@null,np.zeros((m,n-rank))))
            projection=U[:,:rank]@U[:,:rank].conj().T
            chk("least_squares_projection",close(A@x,projection@w))
            chk("least_squares_orthogonality",close(Ah@(w-A@x),np.zeros(n)))
            if n>0:
                D=A.copy()
                D[:,-1]=D[:,0] if n>1 and t%2 else 0
                z=np.linalg.pinv(D,rcond=1e-13)@w
                chk("rank_deficient_normal",close(D.conj().T@(D@z-w),np.zeros(n)))
                chk("rank_deficient_minnorm",close(np.linalg.pinv(D,rcond=1e-13)@D@z,z))
            if 0<m and t<30:
                k=min(n,m)
                B=mat(m,k)
                while np.linalg.matrix_rank(B)<k: B=mat(m,k)
                G=B.conj().T@B
                P=B@np.linalg.inv(G)@B.conj().T
                chk("gram_projection_selfadjoint",close(P,P.conj().T))
                chk("gram_projection_idempotent",close(P@P,P))
                chk("gram_projection_image",close(P@B,B))
                chk("gram_projection_residual",close(B.conj().T@(w-P@w),np.zeros(k)))
                chk("gram_projection_pythagoras",close(norm2(w),norm2(P@w)+norm2(w-P@w)))
                chk("gram_projection_rank",close(np.trace(P),k))

for n in range(7):
    for t in range(120):
        if n: Q,_=np.linalg.qr(mat(n,n))
        else: Q=np.zeros((0,0),dtype=complex)
        chk("unitary_inverse",close(Q.conj().T@Q,np.eye(n)) and close(Q@Q.conj().T,np.eye(n)))
        v=vec(n)
        chk("unitary_norm_preservation",close(norm2(Q@v),norm2(v)))
        a=t%(n+1);b=(t//(n+1))%(n+1)
        P=Q@np.diag([1]*a+[0]*(n-a))@Q.conj().T
        R=Q@np.diag([1]*b+[0]*(n-b))@Q.conj().T
        chk("projection_selfadjoint",close(P,P.conj().T))
        chk("projection_idempotent",close(P@P,P))
        chk("commuting_projections",close(P@R,R@P))
        chk("intersection_projection",close(P@R,Q@np.diag([1]*min(a,b)+[0]*(n-min(a,b)))@Q.conj().T))

print("LA12-LA13 COMPLEX CONVENTIONS REGRESSION")
for name,n in sorted(count.items()): print(name,n)
print("TOTAL PASS:",sum(count.values()))
print("SHA256:",sha256(Path(__file__).read_bytes()).hexdigest())
