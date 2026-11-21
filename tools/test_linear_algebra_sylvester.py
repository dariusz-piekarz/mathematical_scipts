"""LA22: independent finite-field Sylvester regression and exact Lyapunov check."""
from itertools import product
from random import Random
from fractions import Fraction as F
from test_linear_algebra_frobenius import smith_factors, gcd


def rank(mat,p):
    m=[list(x) for x in mat]
    if not m:return 0
    nr,nc=len(m),len(m[0]);r=0
    for j in range(nc):
        pivot=next((i for i in range(r,nr) if m[i][j]%p),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        u=pow(m[r][j]%p,-1,p)
        m[r]=[u*x%p for x in m[r]]
        for i in range(nr):
            if i==r:continue
            c=m[i][j]%p
            m[i]=[(x-c*y)%p for x,y in zip(m[i],m[r])]
        r+=1
        if r==nr:break
    return r


def sylvester_matrix(a,b,n,m,p):
    cols=[]
    for k in range(n):
        for l in range(m):
            c=[[0]*m for _ in range(n)]
            c[k][l]=1
            out=[[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    out[i][j]=(sum(a[n*i+h]*c[h][j] for h in range(n))-
                               sum(c[i][h]*b[m*h+j] for h in range(m)))%p
            cols.append([v for row in out for v in row])
    return [list(x) for x in zip(*cols)]


def expected_kernel(a,b,n,m,p):
    fs=[f for f in smith_factors(a,n,p)[0] if len(f)>1]
    gs=[g for g in smith_factors(b,m,p)[0] if len(g)>1]
    return sum(len(gcd(f,g,p))-1 for f in fs for g in gs)


def check_pair(a,b,n,m,p):
    sm=sylvester_matrix(a,b,n,m,p)
    observed=n*m-rank(sm,p)
    expected=expected_kernel(a,b,n,m,p)
    assert observed==expected,(p,n,m,a,b,observed,expected)
    characteristic_a=smith_factors(a,n,p)[1]
    characteristic_b=smith_factors(b,m,p)[1]
    assert (observed==0)==(gcd(characteristic_a,characteristic_b,p)==[1])
    return observed


def matrix_mult(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def transpose(a):
    return [list(x) for x in zip(*a)]


def exact_lyapunov_example():
    a=[[F(-1),F(1)],[F(0),F(-2)]]
    q=[[F(1),F(0)],[F(0),F(1)]]
    p=[[F(1,2),F(1,6)],[F(1,6),F(1,3)]]
    z=matrix_mult(transpose(a),p)
    w=matrix_mult(p,a)
    assert all(z[i][j]+w[i][j]==-q[i][j] for i in range(2) for j in range(2))
    assert p[0][0]>0 and p[0][0]*p[1][1]-p[0][1]**2==F(5,36)


def run():
    rng=Random(22022)
    configs=[
        (2,1,1,[tuple(x) for x in product(range(2),repeat=1)],
                 [tuple(x) for x in product(range(2),repeat=1)]),
        (2,2,2,[tuple(x) for x in product(range(2),repeat=4)],
                 [tuple(x) for x in product(range(2),repeat=4)]),
        (3,2,2,[tuple(rng.randrange(3) for _ in range(4)) for _ in range(50)],
                 [tuple(rng.randrange(3) for _ in range(4)) for _ in range(50)]),
        (2,3,2,[tuple(rng.randrange(2) for _ in range(9)) for _ in range(50)],
                 [tuple(rng.randrange(2) for _ in range(4)) for _ in range(50)])
    ]
    for p,n,m,aa,bb in configs:
        count=0; singular=0
        for a in aa:
            for b in bb:
                singular+=check_pair(a,b,n,m,p)>0
                count+=1
        print(f"LA22 Sylvester F{p} {n}x{m} pairs={count}, singular={singular}")
    # Over Q: A=[[1,1],[0,1]], B=3 and C=(2,4), solution X=(-2,-2).
    A=[[1,1],[0,1]]
    X=[-2,-2]
    AX=[A[i][0]*X[0]+A[i][1]*X[1] for i in range(2)]
    assert [AX[i]-3*X[i] for i in range(2)]==[2,4]
    exact_lyapunov_example()
    print("LA22 rational Sylvester and positive Lyapunov solution OK")


if __name__=="__main__":
    run()
