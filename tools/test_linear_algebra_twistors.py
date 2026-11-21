"""Exact twistor regression: incidence, Pluecker, Segre, J, quaternionic fibers."""
from itertools import product
from random import Random

rng=Random(32026)

def determinant(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def mv(A,v):
    return (A[0][0]*v[0]+A[0][1]*v[1],
            A[1][0]*v[0]+A[1][1]*v[1])

def diff(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def pluecker(A):
    a,b=A[0]
    c,d=A[1]
    return a*d-b*c,-b,a,-d,c,1

checks=0
for _ in range(5000):
    X=((rng.randint(-5,5),rng.randint(-5,5)),
       (rng.randint(-5,5),rng.randint(-5,5)))
    a,b,c,d,e,f=pluecker(X)
    assert a*f-b*e+c*d==0
    assert a==determinant(X) and f==1
    u=(rng.randint(-4,4),rng.randint(-4,4))
    alpha=(rng.randint(-4,4),rng.randint(-4,4))
    P=((u[0]*alpha[0],u[0]*alpha[1]),
       (u[1]*alpha[0],u[1]*alpha[1]))
    assert determinant(P)==0
    pi=(-alpha[1],alpha[0])
    assert mv(P,pi)==(0,0)
    Y=((X[0][0]+P[0][0],X[0][1]+P[0][1]),
       (X[1][0]+P[1][0],X[1][1]+P[1][1]))
    assert determinant(diff(X,Y))==0 and mv(X,pi)==mv(Y,pi)
    omega=(rng.randint(-5,5),rng.randint(-5,5))
    A=((omega[0],rng.randint(-5,5)),(omega[1],rng.randint(-5,5)))
    B=((omega[0],rng.randint(-5,5)),(omega[1],rng.randint(-5,5)))
    assert mv(A,(1,0))==omega==mv(B,(1,0))
    assert determinant(diff(A,B))==0
    checks+=1

assert determinant(diff(((0,0),(0,0)),((1,0),(0,1))))==1
assert mv(((1,0),(0,0)),(0,1))==(0,0)

def J(z):
    a,b,c,d=z
    return (-b.conjugate(),a.conjugate(),-d.conjugate(),c.conjugate())

def left_mul(q,v):
    s,t=q
    a,b=v
    return (s*a-t.conjugate()*b,t*a+s.conjugate()*b)

for _ in range(2000):
    z=tuple(complex(rng.randint(-4,4),rng.randint(-4,4)) for _ in range(4))
    lam=complex(rng.randint(-3,3),rng.randint(-3,3))
    assert J(J(z))==tuple(-x for x in z)
    assert J(tuple(lam*x for x in z))==tuple(lam.conjugate()*x for x in J(z))
    v=z[:2]
    q=(complex(rng.randint(-3,3),rng.randint(-3,3)),
       complex(rng.randint(-3,3),rng.randint(-3,3)))
    w=left_mul(q,v)
    jv=J((v[0],v[1],0j,0j))[:2]
    assert J((*v,*w))==(*jv,*left_mul(q,jv))
    v2=z[2:]
    alpha,beta=complex(2,-1),complex(-1,3)
    lhs=left_mul(q,(alpha*v[0]+beta*v2[0],alpha*v[1]+beta*v2[1]))
    r1,r2=left_mul(q,v),left_mul(q,v2)
    assert lhs==(alpha*r1[0]+beta*r2[0],alpha*r1[1]+beta*r2[1])
    checks+=1

for t,x,y,z in product(range(-2,3),repeat=4):
    H=((t+z,complex(x,-y)),(complex(x,y),t-z))
    assert determinant(H)==t*t-x*x-y*y-z*z
    checks+=1

print(f"Twistor Segre/Pluecker/incidence/J/quaternion checks: {checks} PASS")
