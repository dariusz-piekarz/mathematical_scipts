"""LA-27: Gramian, minimal-realization and Hankel regression.

Exhaustive 2x2 one-input/one-output state-space systems over F2/F3.
Also verifies exact rational Gramian equations, similarity invariance,
observable state reconstruction, minimal reduction and balancing.
No external dependencies.
"""
from fractions import Fraction as F
from itertools import product

from test_linear_algebra_control import rank
from test_linear_algebra_riccati import matrix, eye, tr, mm, add, sub, inv


def finite_hankel_tests():
    for p in (2, 3):
        count, minimal, zero = 0, 0, 0
        for a00,a01,a10,a11,b0,b1,c0,c1 in product(range(p),repeat=8):
            a=((a00,a01),(a10,a11))
            b=(b0,b1)
            c=(c0,c1)
            xs=[b]
            for _ in range(4):
                x=xs[-1]
                xs.append(((a00*x[0]+a01*x[1])%p,
                           (a10*x[0]+a11*x[1])%p))
            h=[(c0*x[0]+c1*x[1])%p for x in xs]
            k=[[xs[0][0],xs[1][0]], [xs[0][1],xs[1][1]]]
            o=[[c[0],c[1]],
               [(c0*a00+c1*a10)%p,(c0*a01+c1*a11)%p]]
            hk2=[[h[0],h[1]],[h[1],h[2]]]
            hk3=[[h[0],h[1],h[2]],
                 [h[1],h[2],h[3]],
                 [h[2],h[3],h[4]]]
            ok=[[sum(o[i][t]*k[t][j] for t in range(2))%p
                 for j in range(2)] for i in range(2)]
            r=rank(hk2,p)
            assert r==rank(ok,p)==rank(hk3,p), (
                p, a,b,c, h, r,rank(ok,p),rank(hk3,p))
            is_minimal=rank(k,p)==rank(o,p)==2
            assert is_minimal == (r==2)
            minimal+=is_minimal
            zero+=(r==0)
            count+=1
        assert count==p**8
        print(f"LA27 exhaustive F{p}: {count} systems, "
              f"minimal={minimal}, zero-transfer={zero}; Hankel rank OK")


def test_reduction():
    a=matrix([[2,0,0],[0,F(1,2),0],[0,0,3]])
    b=matrix([[1],[0],[1]])
    c=matrix([[1,0,0]])
    am=matrix([[2]])
    bm=matrix([[1]])
    cm=matrix([[1]])
    for k in range(15):
        if k==0:
            a_power=eye(3)
            am_power=eye(1)
        else:
            a_power=mm(a_power,a)
            am_power=mm(am_power,am)
        h=mm(mm(c,a_power),b)
        hmin=mm(mm(cm,am_power),bm)
        assert h==hmin==matrix([[2**k]])
    h3=matrix([[1,2,4],[2,4,8],[4,8,16]])
    assert h3[1]==[2*x for x in h3[0]]
    assert h3[2]==[4*x for x in h3[0]]
    print("LA27 exact 3-state to 1-state quotient realization OK")


def test_similarity_minimal():
    # Minimal two-state realization and its nonorthogonal similarity.
    a=matrix([[0,1],[0,0]])
    b=matrix([[0],[1]])
    c=matrix([[1,0]])
    t=matrix([[1,1],[1,2]])
    tinv=inv(t)
    a2=mm(mm(tinv,a),t)
    b2=mm(tinv,b)
    c2=mm(c,t)
    aa=eye(2)
    ab=eye(2)
    for k in range(12):
        assert mm(mm(c,aa),b)==mm(mm(c2,ab),b2)
        aa=mm(aa,a)
        ab=mm(ab,a2)
    assert mm(t,a2)==mm(a,t)  # transformed T^-1 A T
    assert mm(t,b2)==b
    assert mm(c2,tinv)==c
    print("LA27 minimal realizations related by similarity OK")


def test_discrete_observation_and_stein():
    a=matrix([[0,1],[0,0]])
    b=matrix([[0],[1]])
    c=matrix([[1,0]])
    ac=mm(a,b)
    wc=add(mm(b,tr(b)),mm(ac,tr(ac)))
    ca=mm(c,a)
    wo=add(mm(tr(c),c),mm(tr(ca),ca))
    assert wc==eye(2)==wo
    y0=matrix([[3]])
    y1=matrix([[5]])
    obs=matrix([[1,0],[0,1]])
    y=matrix([[3],[5]])
    assert mm(inv(wo),mm(tr(obs),y))==matrix([[3],[5]])
    # Stable diagonal 2x2 with B=C=I.
    d=matrix([[F(1,2),0],[0,F(1,3)]])
    w=matrix([[F(4,3),0],[0,F(9,8)]])
    assert sub(w,mm(mm(d,w),tr(d)))==eye(2)
    assert sub(w,mm(mm(tr(d),w),d))==eye(2)
    # coordinate transform T=diag(2,3)
    t=matrix([[2,0],[0,3]])
    tinv=inv(t)
    wct=mm(mm(tinv,w),tr(tinv))
    wot=mm(mm(tr(t),w),t)
    assert wct==matrix([[F(1,3),0],[0,F(1,8)]])
    assert wot==matrix([[F(16,3),0],[0,F(81,8)]])
    assert mm(wct,wot)==matrix([[F(16,9),0],[0,F(81,64)]])
    assert mm(mm(t,mm(wct,wot)),tinv)==mm(w,w)
    print("LA27 exact discrete Stein, observability and balanced coordinates OK")


def test_continuous_lapunov():
    d=matrix([[-1,0],[0,-2]])
    w=matrix([[F(1,2),0],[0,F(1,4)]])
    assert add(mm(d,w),mm(w,tr(d)))==matrix([[-1,0],[0,-1]])
    assert add(mm(tr(d),w),mm(w,d))==matrix([[-1,0],[0,-1]])
    # Nilpotent 2x2, T=1, C=e1^T: W_o=[[1,1/2],[1/2,1/3]]
    wo=matrix([[1,F(1,2)],[F(1,2),F(1,3)]])
    assert wo[0][0]*wo[1][1]-wo[0][1]*wo[1][0]==F(1,12)
    print("LA27 continuous Lyapunov and finite Gramian rational checks OK")


def test_least_squares():
    # Observable, not orthogonal columns: O=[[1,1],[1,2]].
    obs=matrix([[1,1],[1,2]])
    w=mm(tr(obs),obs)
    assert w==matrix([[2,3],[3,5]])
    assert w[0][0]*w[1][1]-w[0][1]**2==1
    x=matrix([[2],[-1]])
    eps=matrix([[1],[-2]])
    y=add(mm(obs,x),eps)
    xhat=mm(mm(inv(w),tr(obs)),y)
    resid=sub(y,mm(obs,xhat))
    assert mm(tr(obs),resid)==matrix([[0],[0]])
    # Here O is square and invertible: the error is O^-1 eps.
    assert sub(xhat,x)==mm(inv(obs),eps)
    # The Gramian lower eigenvalue lambda_min=(7-sqrt(45))/2.
    import math
    lam=(7-math.sqrt(45))/2
    err=sub(xhat,x)
    lhs=sum(float(z[0]**2) for z in err)
    noise=sum(float(z[0]**2) for z in eps)
    assert lhs*lam<=noise+1e-12
    print("LA27 exact least squares normal equations and perturbation bound OK")


if __name__=="__main__":
    finite_hankel_tests()
    test_reduction()
    test_similarity_minimal()
    test_discrete_observation_and_stein()
    test_continuous_lapunov()
    test_least_squares()
