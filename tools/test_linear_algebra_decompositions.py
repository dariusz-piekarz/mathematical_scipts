"""Exact/rational and complex regression for linear algebra chapter 15.

Standard library only. Tests general pivoted LU incl singular matrices,
positive-definite Hermitian Cholesky, complex QR, SVD, Moore-Penrose,
polar decomposition and Eckart-Young rank-one approximation.
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, sin, sqrt
from random import Random

EPS = 2e-9


def near(x, y):
    return abs(x-y) <= EPS*(1+abs(x)+abs(y))


def mm(a,b):
    return [[sum(a[i][t]*b[t][j] for t in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def star(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def diag(entries):
    n=len(entries)
    return [[entries[i] if i==j else 0 for j in range(n)]
            for i in range(n)]


def closem(a,b):
    assert len(a)==len(b)
    for x,y in zip(a,b):
        assert len(x)==len(y)
        assert all(near(q,r) for q,r in zip(x,y)), (a,b)


def vecdot(x,y):
    return sum(a.conjugate()*b for a,b in zip(x,y))


def norm2(x):
    return vecdot(x,x).real


def colmatrix(cols):
    return [[col[i] for col in cols] for i in range(len(cols[0]))]


def add(a,b):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(a,b)]


def sub(a,b):
    return [[x-y for x,y in zip(row,other)] for row,other in zip(a,b)]


def plu(a):
    """Exact Gaussian elimination with row pivoting, including zero pivots."""
    n=len(a)
    u=[[Fraction(x) for x in row] for row in a]
    l=ident(n)
    p=ident(n)
    for j in range(n):
        pivot=next((i for i in range(j,n) if u[i][j]),None)
        if pivot is None:
            continue
        if pivot!=j:
            u[j],u[pivot]=u[pivot],u[j]
            p[j],p[pivot]=p[pivot],p[j]
            for k in range(j):
                l[j][k],l[pivot][k]=l[pivot][k],l[j][k]
        for i in range(j+1,n):
            c=u[i][j]/u[j][j]
            l[i][j]=c
            for k in range(j,n):
                u[i][k]-=c*u[j][k]
    return p,l,u


def check_plu():
    rng=Random(15151)
    count=0
    for n in (1,2,3,4):
        for _ in range(190):
            a=[[rng.randint(-3,3) for j in range(n)] for i in range(n)]
            p,l,u=plu(a)
            closem(mm(p,a),mm(l,u))
            for i in range(n):
                assert near(l[i][i],1)
                for j in range(n):
                    if j>i:
                        assert not l[i][j]
                    if j<i:
                        assert not u[i][j]
            count+=1
    # Explicit missing leading pivot.
    a=[[0,2],[1,3]]
    p,l,u=plu(a)
    closem(mm(p,a),mm(l,u))
    return count+1


def cholesky(a):
    n=len(a)
    l=[[0j]*n for _ in range(n)]
    for j in range(n):
        d=a[j][j]-sum(l[j][k]*l[j][k].conjugate() for k in range(j))
        assert abs(d.imag) < EPS and d.real>EPS
        l[j][j]=sqrt(d.real)
        for i in range(j+1,n):
            z=a[i][j]-sum(l[i][k]*l[j][k].conjugate() for k in range(j))
            l[i][j]=z/l[j][j]
    return l


def check_cholesky():
    rng=Random(202615)
    count=0
    choices=[-2,-1,0,1,2,1j,-1j,1+1j]
    for n in (1,2,3,4):
        for _ in range(120):
            b=[[rng.choice(choices) for j in range(n)] for i in range(n)]
            h=add(mm(b,star(b)),ident(n))
            l=cholesky(h)
            closem(mm(l,star(l)),h)
            for i in range(n):
                assert l[i][i].real>0 and near(l[i][i].imag,0)
                for j in range(i+1,n):
                    assert not l[i][j]
            count+=1
    # Explicit complex Hermitian example from the chapter.
    h=[[4,2j],[-2j,5]]
    closem(mm(cholesky(h),star(cholesky(h))),h)
    return count+1


def gs_qr(a):
    """Thin QR for m>=n, including linearly dependent columns."""
    m=len(a);n=len(a[0])
    basis=[]
    for j in range(n):
        vec=[a[i][j] for i in range(m)]
        for q in basis:
            c=vecdot(q,vec)
            vec=[x-c*y for x,y in zip(vec,q)]
        length=sqrt(norm2(vec))
        if length<EPS:
            # Complete the current orthonormal system by an arbitrary
            # direction. This is necessary for rank-deficient QR.
            chosen=None
            for k in range(m):
                candidate=[complex(i==k) for i in range(m)]
                for q in basis:
                    c=vecdot(q,candidate)
                    candidate=[x-c*y for x,y in zip(candidate,q)]
                candidate_norm=sqrt(norm2(candidate))
                if candidate_norm>EPS:
                    chosen=tuple(x/candidate_norm for x in candidate)
                    break
            assert chosen is not None, "m>=n guarantees a complement"
            basis.append(chosen)
        else:
            basis.append(tuple(x/length for x in vec))
    q=colmatrix(basis)
    r=mm(star(q),a)
    return q,r


def check_qr():
    rng=Random(15152)
    choices=[-2,-1,0,1,2,1j,-1j,1+1j]
    count=0
    for m,n in ((2,2),(3,2),(4,3)):
        for _ in range(180):
            a=[[rng.choice(choices) for j in range(n)] for i in range(m)]
            q,r=gs_qr(a)
            closem(mm(q,r),a)
            closem(mm(star(q),q),ident(n))
            for i in range(n):
                assert near(r[i][i].imag,0) and r[i][i].real>=-EPS
                for j in range(i):
                    assert near(r[i][j],0)
            count+=1
    # Explicit complex rank-one matrix: col_2=i col_1.
    a=[[1,1j],[1j,-1],[0,0]]
    q,r=gs_qr(a)
    closem(mm(q,r),a)
    closem(mm(star(q),q),ident(2))
    assert near(r[1][1],0)
    count+=1
    return count


def unitary(angle,phase):
    c=cos(angle)
    s=sin(angle)
    z=complex(cos(phase),sin(phase))
    return [[c,s*z],[-s*z.conjugate(),c]]


def trace_frob2(a):
    return sum(abs(z)**2 for row in a for z in row)


def operator_norm_diag2(a):
    # Norm only needed for the known diagonal error matrix.
    return max(abs(a[0][0]),abs(a[1][1]))


def svd_based(s1,s2,u,v):
    singular=diag((s1,s2))
    a=mm(mm(u,singular),star(v))
    pseudo=mm(mm(v,diag((1/s1 if s1 else 0,1/s2 if s2 else 0))),star(u))
    partial=mm(mm(u,diag((int(s1>0),int(s2>0)))),star(v))
    positive=mm(mm(v,singular),star(v))
    return a,pseudo,partial,positive


def check_svd_and_polar():
    rng=Random(15153)
    sigmas=((4.,3.),(3.,2.),(3.,0.),(1.,1.),(0.,0.))
    count=0
    for s1,s2 in sigmas:
        for theta,phase in ((.0,.0),(.4,.5),(1.2,2.)):
            u=unitary(theta,phase)
            v=unitary(theta/2,phase+.3)
            a,pseudo,w,h=svd_based(s1,s2,u,v)
            closem(mm(star(u),u),ident(2))
            closem(mm(star(v),v),ident(2))
            closem(mm(w,h),a)
            closem(star(h),h)
            closem(mm(h,h),mm(star(a),a))
            closem(mm(mm(a,pseudo),a),a)
            closem(mm(mm(pseudo,a),pseudo),pseudo)
            closem(star(mm(a,pseudo)),mm(a,pseudo))
            closem(star(mm(pseudo,a)),mm(pseudo,a))
            closem(mm(star(w),w),mm(pseudo,a))
            closem(mm(w,star(w)),mm(a,pseudo))
            assert near(trace_frob2(a),s1*s1+s2*s2)
            if s2>0:
                closem(mm(pseudo,a),ident(2))
            # Eckart-Young: rank-one SVD truncation has squared
            # Frobenius error equal to the trailing singular value squared.
            ak=mm(mm(u,diag((s1,0))),star(v))
            assert near(trace_frob2(sub(a,ak)),s2*s2)
            if s1>=s2 and s2>0:
                for _ in range(15):
                    x=tuple(rng.randrange(-2,3) for _ in range(2))
                    y=tuple(rng.randrange(-2,3) for _ in range(2))
                    trial=[[x[i]*y[j] for j in range(2)] for i in range(2)]
                    assert trace_frob2(sub(a,trial)) >= s2*s2-EPS
            count+=1
    # Rectangular rank-two example: the canonical singular values are 3,2.
    rect=[[3.,0.,0.],[0.,2.,0.]]
    rect_pseudo=[[1/3,0.],[0.,1/2],[0.,0.]]
    closem(mm(mm(rect,rect_pseudo),rect),rect)
    closem(mm(mm(rect_pseudo,rect),rect_pseudo),rect_pseudo)
    # Deficient-rank example from LA13.
    deficient=[[1.,1.],[2.,2.]]
    deficient_pseudo=[[.1,.2],[.1,.2]]
    closem(mm(mm(deficient,deficient_pseudo),deficient),deficient)
    assert near(mm(deficient_pseudo,[[1.],[0.]])[0][0],.1)
    return count+2


def main():
    a=check_plu()
    b=check_cholesky()
    c=check_qr()
    d=check_svd_and_polar()
    print("Linear-algebra matrix-decomposition regressions OK:",
          a,"PLU incl singular;",
          b,"Hermitian Cholesky;",
          c,"QR including rank-deficient;",
          d,"SVD/pseudoinverse/polar and Eckart-Young.")


if __name__=="__main__":
    main()
