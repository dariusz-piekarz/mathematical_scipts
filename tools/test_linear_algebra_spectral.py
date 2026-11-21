"""Regression tests for LA 14: finite-dimensional complex and real spectral theorem.

Pure Python, no external packages. Constructs explicit unitary similarities,
checks eigenpairs, normality, polynomial projectors, Rayleigh bounds, and
commuting Hermitian operators, including a defective nonnormal counterexample.
"""
from cmath import exp
from itertools import product
from math import cos, sin, sqrt
from random import Random

EPS=1e-9
def close(a,b):
    return abs(a-b)<=EPS*(1+abs(a)+abs(b))
def eye(n):
    return [[complex(i==j) for j in range(n)] for i in range(n)]
def diagonal(x):
    return [[x[i] if i==j else 0j for j in range(len(x))]
            for i in range(len(x))]
def add(a,b):
    return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scale(c,a):
    return [[c*x for x in row] for row in a]
def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def adjoint(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]
def matvec(a,v):
    return tuple(sum(a[i][j]*v[j] for j in range(len(v)))
                 for i in range(len(a)))
def dot(u,v):
    return sum(x.conjugate()*y for x,y in zip(u,v))
def equals(a,b):
    assert len(a)==len(b)
    for x,y in zip(a,b):
        assert len(x)==len(y)
        for p,q in zip(x,y):
            assert close(p,q), (a,b,p,q)
def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def unitary(theta,phi):
    c=cos(theta);s=sin(theta);e=exp(1j*phi)
    return [[c,s*e],[-s*e.conjugate(),c]]

def normal_cases():
    rng=Random(142026)
    spectrum=(0j,1+0j,-2+0j,1j,-1j,2+3j)
    count=0
    for lam,mu in product(spectrum,repeat=2):
        for theta,phase in ((.1,.4),(.4,1.2),(1.,2.4)):
            u=unitary(theta,phase)
            equals(multiply(adjoint(u),u),eye(2))
            a=multiply(multiply(u,diagonal((lam,mu))),adjoint(u))
            a_star=adjoint(a)
            equals(multiply(a,a_star),multiply(a_star,a))
            for j,eig in enumerate((lam,mu)):
                v=tuple(u[i][j] for i in range(2))
                assert all(close(x,eig*y) for x,y in zip(matvec(a,v),v))
            assert close(a[0][0]+a[1][1],lam+mu)
            assert close(det2(a),lam*mu)
            for _ in range(5):
                v=tuple(rng.choice(spectrum) for _ in range(2))
                assert dot(matvec(a,v),matvec(a,v)).real <= (
                    max(abs(lam),abs(mu))**2*dot(v,v).real+EPS)
            if not close(lam,mu):
                p=scale(1/(lam-mu),add(a,scale(-mu,eye(2))))
                q=scale(1/(mu-lam),add(a,scale(-lam,eye(2))))
                equals(add(p,q),eye(2))
                equals(multiply(p,p),p)
                equals(multiply(q,q),q)
                equals(multiply(p,q),[[0,0],[0,0]])
                equals(adjoint(p),p)
                equals(add(scale(lam,p),scale(mu,q)),a)
                poly=add(add(multiply(a,a),scale(2,a)),eye(2))
                projected=add(scale((lam+1)**2,p),scale((mu+1)**2,q))
                equals(poly,projected)
            count+=1
    return count

def hermitian_cases():
    count=0
    h=[[2,1j],[-1j,2]]
    e1=(-1j/sqrt(2),1/sqrt(2))
    e3=(1j/sqrt(2),1/sqrt(2))
    assert close(dot(e1,e3),0)
    for eigenvalue,v in ((1,e1),(3,e3)):
        assert all(close(x,eigenvalue*y) for x,y in zip(matvec(h,v),v))
    for v in product((0,1,-1,1j,-1j,2+3j),repeat=2):
        norm=dot(v,v).real
        if norm<EPS:
            continue
        rayleigh=dot(v,matvec(h,v))/norm
        assert close(rayleigh.imag,0)
        assert 1-EPS<=rayleigh.real<=3+EPS
        count+=1
    u=unitary(.4,1.2)
    indefinite=multiply(multiply(u,diagonal((-2,5))),adjoint(u))
    for lam,j in ((-2,0),(5,1)):
        v=tuple(u[i][j] for i in range(2))
        assert close(dot(v,matvec(indefinite,v)),lam)
        count+=1
    real=[[2,1],[1,2]]
    q=[[1/sqrt(2),1/sqrt(2)],[1/sqrt(2),-1/sqrt(2)]]
    equals(multiply(multiply(adjoint(q),real),q),diagonal((3,1)))
    count+=1
    return count

def counterexamples_and_commuting():
    defective=[[1,1],[0,1]]
    left=multiply(defective,adjoint(defective))
    right=multiply(adjoint(defective),defective)
    assert any(not close(left[i][j],right[i][j])
               for i in range(2) for j in range(2))
    assert close(det2(add(defective,scale(-1,eye(2)))),0)
    v=(1,0)
    assert all(close(x,y) for x,y in zip(matvec(defective,v),v))
    u=unitary(.7,.4)
    a=multiply(multiply(u,diagonal((2,5))),adjoint(u))
    b=multiply(multiply(u,diagonal((7,-3))),adjoint(u))
    equals(multiply(a,b),multiply(b,a))
    for j in range(2):
        e=tuple(u[i][j] for i in range(2))
        assert all(close(x,(2,5)[j]*y) for x,y in zip(matvec(a,e),e))
        assert all(close(x,(7,-3)[j]*y) for x,y in zip(matvec(b,e),e))
    return 8

if __name__=="__main__":
    a=normal_cases()
    b=hermitian_cases()
    c=counterexamples_and_commuting()
    print("Spectral regression tests OK:",
          a,"normal similarities and projectors;",
          b,"Hermitian Rayleigh tests;",
          c,"commuting/defective checks.")
