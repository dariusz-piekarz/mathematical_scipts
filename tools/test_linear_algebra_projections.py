"""Deterministic regression tests for linear algebra chapter 13.

Tests Hermitian adjoints, orthogonal projections, normal equations and
least-squares behavior with independent and dependent columns. All matrices
are small; no third-party dependencies are needed.
"""
from __future__ import annotations

from itertools import product
from random import Random

EPS = 1e-9
VALS = (0j, 1+0j, -1+0j, 1j, -1j, 1+1j)


def near(x, y):
    return abs(x-y) < EPS*(1+abs(x)+abs(y))


def vv(x, y):
    return sum(a.conjugate()*b for a, b in zip(x, y))


def norm2(v):
    return vv(v, v).real


def matvec(a, x):
    return tuple(sum(row[j]*x[j] for j in range(len(x))) for row in a)


def matmul(a, b):
    if not a or not b:
        return [[0j for _ in range(len(b[0]) if b else 0)]
                for _ in range(len(a))]
    return [[sum(a[i][t]*b[t][j] for t in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def star(a):
    if not a:
        return []
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def transpose_cols(cols, n):
    return [[c[i] for c in cols] for i in range(n)]


def matrix_close(a, b):
    assert len(a)==len(b)
    for row1,row2 in zip(a,b):
        assert len(row1)==len(row2)
        assert all(near(x,y) for x,y in zip(row1,row2)), (a,b)


def inverse(a):
    n=len(a)
    t=[[complex(x) for x in row]+[complex(i==j) for j in range(n)]
       for i,row in enumerate(a)]
    for i in range(n):
        k=max(range(i,n),key=lambda j:abs(t[j][i]))
        if abs(t[k][i])<EPS:
            return None
        t[i],t[k]=t[k],t[i]
        pivot=t[i][i]
        t[i]=[v/pivot for v in t[i]]
        for j in range(n):
            if j==i:
                continue
            c=t[j][i]
            t[j]=[x-c*y for x,y in zip(t[j],t[i])]
    return [row[n:] for row in t]


def adjoints():
    rng=Random(13131)
    cases=0
    for m,n in ((1,2),(2,2),(3,2),(2,3)):
        for _ in range(140):
            a=[[rng.choice(VALS) for _ in range(n)] for _ in range(m)]
            u=tuple(rng.choice(VALS) for _ in range(n))
            w=tuple(rng.choice(VALS) for _ in range(m))
            left=vv(matvec(a,u),w)
            right=vv(u,matvec(star(a),w))
            assert near(left,right)
            matrix_close(star(star(a)),a)
            cases+=1
    return cases


def projection_trials():
    rng=Random(5678)
    cases=0
    for n,r in ((2,1),(3,1),(3,2),(4,2),(4,3)):
        for _ in range(190):
            cols=[tuple(rng.choice(VALS) for _ in range(n)) for _ in range(r)]
            b=transpose_cols(cols,n)
            gram=matmul(star(b),b)
            inv=inverse(gram)
            if inv is None:
                continue
            p=matmul(matmul(b,inv),star(b))
            matrix_close(p,star(p))
            matrix_close(p,matmul(p,p))
            for _ in range(5):
                v=tuple(rng.choice(VALS) for _ in range(n))
                pv=matvec(p,v)
                rem=tuple(x-y for x,y in zip(v,pv))
                assert near(norm2(v),norm2(pv)+norm2(rem))
                assert all(near(vv(c,rem),0) for c in cols)
                assert near(vv(pv,rem),0)
                x=tuple(rng.choice(VALS) for _ in range(r))
                trial=matvec(b,x)
                assert norm2(rem)<=norm2(tuple(a-c for a,c in zip(v,trial)))+EPS
                cases+=1
    return cases


def least_squares():
    rng=Random(731)
    cases=0
    for m,n in ((3,1),(3,2),(4,2),(4,3),(2,3)):
        for _ in range(190):
            a=[[rng.choice(VALS) for _ in range(n)] for _ in range(m)]
            gram=matmul(star(a),a)
            inv=inverse(gram)
            y=tuple(rng.choice(VALS) for _ in range(m))
            if inv is None:
                continue
            rhs=matvec(star(a),y)
            x=matvec(inv,rhs)
            fitted=matvec(a,x)
            residual=tuple(yy-ff for yy,ff in zip(y,fitted))
            assert all(near(t,0) for t in matvec(star(a),residual))
            for _ in range(5):
                z=tuple(rng.choice(VALS) for _ in range(n))
                rz=tuple(yy-ff for yy,ff in zip(y,matvec(a,z)))
                assert norm2(residual)<=norm2(rz)+EPS
                cases+=1
    # Rank-deficient example in the chapter; normal matrix is singular.
    a=[[1,1],[2,2]]
    y=(1,0)
    assert inverse(matmul(star(a),a)) is None
    for t in (-5,-1,0,.1,.5,2):
        x=(t,.2-t)
        fitted=matvec(a,x)
        assert all(near(v,w) for v,w in zip(fitted,(.2,.4)))
        assert all(near(v,0) for v in matvec(star(a),tuple(y[i]-fitted[i] for i in range(2))))
        assert norm2((.1,.1))<=norm2(x)+EPS
        cases+=1
    return cases


def commuting_projections():
    q=[[.5,.5],[.5,.5]]
    p=[[1,0],[0,0]]
    pq=matmul(p,q)
    qp=matmul(q,p)
    assert any(not near(pq[i][j],qp[i][j])
               for i in range(2) for j in range(2))
    assert near(matvec(pq,(0,1))[0],.5)
    # Orthogonal projections onto two coordinate axes commute.
    p1=[[1,0],[0,0]]
    p2=[[0,0],[0,1]]
    matrix_close(matmul(p1,p2),matmul(p2,p1))
    matrix_close(matmul(p1,p2),[[0,0],[0,0]])
    return 3


def main():
    counts=(adjoints(), projection_trials(), least_squares(),
            commuting_projections())
    print("Orthogonal projection regression tests OK:",
          counts[0],"adjoints;",
          counts[1],"Hermitian projection/best-fit cases;",
          counts[2],"least-square cases;",
          counts[3],"composition cases.")


if __name__=="__main__":
    main()
