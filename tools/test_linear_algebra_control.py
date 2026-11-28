"""LA25: exact controllability / observability / PBH regression tests.

Exhaustive two-dimensional checks over F2 and F3, including
roots of characteristic polynomials over algebraic extensions
through polynomial gcd of PBH maximal minors.
Real rational feedback, Gramian and minimum energy examples.
"""
from fractions import Fraction as F
from itertools import product
from test_linear_algebra_frobenius import gcd


def rank(rows, p):
    a=[[int(x)%p for x in row] for row in rows]
    if not a:
        return 0
    h,w=len(a),len(a[0])
    r=0
    for j in range(w):
        pivot=next((i for i in range(r,h) if a[i][j]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        q=pow(a[r][j],-1,p)
        a[r]=[(q*x)%p for x in a[r]]
        for i in range(h):
            if i==r:
                continue
            d=a[i][j]
            a[i]=[(x-d*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==h:
            break
    return r


def mm(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in zip(*b)] for row in a]


def tr(a):
    return [list(x) for x in zip(*a)]


def small_kalman(a,b,p):
    u,v=b
    return [[u,(a[0][0]*u+a[0][1]*v)%p],
            [v,(a[1][0]*u+a[1][1]*v)%p]]


def small_observability(a,c,p):
    u,v=c
    return [[u,v],
            [(u*a[0][0]+v*a[1][0])%p,
             (u*a[0][1]+v*a[1][1])%p]]


def trim(q,p):
    out=[x%p for x in q]
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def pbh_full_row_rank_for_all_eigenvalues(a,b,p):
    """GCD of all 2x2 minors of [tI-A | B] = 1 over Fp[t]."""
    x,y=a[0]
    z,w=a[1]
    u,v=b
    characteristic=[(x*w-y*z)%p,(-x-w)%p,1]
    minor02=[(-x*v+z*u)%p,v%p]
    minor12=[(w*u-y*v)%p,(-u)%p]
    common=gcd(gcd(characteristic,trim(minor02,p),p),
               trim(minor12,p),p)
    return common==[1]


def exhaustive_finite_fields():
    for p in (2,3):
        total=0
        controllable=0
        observable=0
        for a00,a01,a10,a11,b0,b1 in product(range(p),repeat=6):
            a=[[a00,a01],[a10,a11]]
            b=(b0,b1)
            k=small_kalman(a,b,p)
            r=rank(k,p)
            is_ctrl=(r==2)
            assert is_ctrl==pbh_full_row_rank_for_all_eigenvalues(a,b,p), (p,a,b)
            controllable+=is_ctrl
            # Invariance: rank [K | A K] agrees with rank(K).
            ak=[[sum(a[i][h]*k[h][j] for h in range(2))%p
                 for j in range(2)] for i in range(2)]
            assert rank([k[i]+ak[i] for i in range(2)],p)==r

            # Observability of (B^T,A) is dual to controllability of (A^T,B).
            at=tr(a)
            ob=small_observability(a,b,p)
            kt=small_kalman(at,b,p)
            is_obs=(rank(ob,p)==2)
            assert is_obs==(rank(kt,p)==2)
            assert is_obs==pbh_full_row_rank_for_all_eigenvalues(at,b,p)
            observable+=is_obs
            total+=1
        print(f"LA25 exhaustive F{p}: {total} systems, "
              f"ctrl={controllable}, obs={observable}, PBH minors/duality OK")


def mat2(a,b,c,d):
    return [[F(a),F(b)],[F(c),F(d)]]


def exact_feedback():
    samples=0
    for a,b,c,d,u,v in product((-2,-1,0,1,2),repeat=6):
        if not u and not v:
            continue
        A=mat2(a,b,c,d)
        B=[F(u),F(v)]
        AB=[F(a*u+b*v),F(c*u+d*v)]
        kalman_det=B[0]*AB[1]-B[1]*AB[0]
        if kalman_det==0:
            continue
        # Prescribe characteristic polynomial (t+1)(t+2).
        alpha=F(d*u-b*v)
        beta=F(a*v-c*u)
        rhs1=F(a+d+3)
        rhs2=F(a*d-b*c-2)
        delta=B[0]*beta-B[1]*alpha
        assert delta==-kalman_det
        k1=(rhs1*beta-B[1]*rhs2)/delta
        k2=(B[0]*rhs2-alpha*rhs1)/delta
        closed=mat2(F(a)-B[0]*k1, F(b)-B[0]*k2,
                    F(c)-B[1]*k1, F(d)-B[1]*k2)
        assert closed[0][0]+closed[1][1]==-3
        assert closed[0][0]*closed[1][1]-closed[0][1]*closed[1][0]==2
        samples+=1
        if samples>=500:
            break
    assert samples==500
    print("LA25 rational feedback: 500 controllable 2x2 pairs, poles -1,-2 OK")


def exact_examples():
    # A nilpotent chain: Kalman rank 2, observable with C=e1^T.
    a=mat2(0,1,0,0)
    b=[F(0),F(1)]
    assert small_kalman(a,b,7)==[[F(0),F(1)],[F(1),F(0)]]
    assert small_observability(a,(1,0),7)==[[F(1),F(0)],[F(0),F(1)]]
    assert small_observability(a,(0,1),7)==[[F(0),F(1)],[F(0),F(0)]]

    # W_2^d = B B^T + AB (AB)^T = I.
    bb=[[b[0]],[b[1]]]
    ab=mm(a,bb)
    w=[[bb[i][0]*bb[j][0]+ab[i][0]*ab[j][0]
        for j in range(2)] for i in range(2)]
    assert w==mat2(1,0,0,1)

    # W_1^c for exp(t A) B = (t,1): integral of rank-one matrices.
    wc=mat2(F(1,3),F(1,2),F(1,2),F(1))
    det=wc[0][0]*wc[1][1]-wc[0][1]*wc[1][0]
    assert det==F(1,12)
    inverse=mat2(wc[1][1]/det,-wc[0][1]/det,
                 -wc[1][0]/det,wc[0][0]/det)
    assert mm(wc,inverse)==mat2(1,0,0,1)

    # Reachable / observable but not controllable / observable.
    diag=mat2(1,0,0,-2)
    b=(1,0)
    assert rank(small_kalman(diag,b,7),7)==1
    assert rank(small_observability(diag,(1,0),7),7)==1
    K=[F(3),F(0)]
    B=[[F(1)],[F(0)]]
    close=[[diag[i][j]-B[i][0]*K[j] for j in range(2)] for i in range(2)]
    assert close==mat2(-2,0,0,-2)
    L=[[F(3)],[F(0)]]
    C=[[F(1),F(0)]]
    observe_closed=[[diag[i][j]-mm(L,C)[i][j] for j in range(2)]
                    for i in range(2)]
    assert observe_closed==mat2(-2,0,0,-2)

    # Uncontrollable mode 2 cannot be moved by feedback.
    un=mat2(1,0,0,2)
    for k1,k2 in ((0,0),(1,5),(3,-7)):
        changed=[[un[i][j]-B[i][0]*F((k1,k2)[j]) for j in range(2)]
                 for i in range(2)]
        assert changed[1]==[F(0),F(2)]

    # Discrete stabilizable but not controllable example.
    stable=mat2(F(3,2),0,0,F(1,2))
    kd=[F(1),F(0)]
    changed=[[stable[i][j]-B[i][0]*kd[j] for j in range(2)]
             for i in range(2)]
    assert changed==mat2(F(1,2),0,0,F(1,2))
    print("LA25 rational Gramians, reachability and continuous/discrete feedback OK")


if __name__=="__main__":
    exhaustive_finite_fields()
    exact_feedback()
    exact_examples()
