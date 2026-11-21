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

def dimension_three_cases():
    """Verify spectral projectors also for repeated eigenvalues in C^3."""
    checks=0
    for eigenvalues in ((1,2,3),(2,2,-1),(0,0,0),
                        (1j,1j,-2j),(1,1,1)):
        for theta,phase in ((.3,.4),(.8,1.6),(1.2,2.4)):
            v=unitary(theta,phase)
            w=unitary(theta/2,phase+.7)
            u12=[[v[0][0],v[0][1],0],
                 [v[1][0],v[1][1],0],[0,0,1]]
            u23=[[1,0,0],[0,w[0][0],w[0][1]],
                 [0,w[1][0],w[1][1]]]
            u=multiply(u12,u23)
            equals(multiply(adjoint(u),u),eye(3))
            a=multiply(multiply(u,diagonal(eigenvalues)),adjoint(u))
            equals(multiply(adjoint(a),a),multiply(a,adjoint(a)))
            distinct=tuple(dict.fromkeys(eigenvalues))
            projections={}
            for eig in distinct:
                p=eye(3)
                for other in distinct:
                    if eig != other:
                        p=multiply(p,scale(1/(eig-other),
                                           add(a,scale(-other,eye(3)))))
                equals(p,adjoint(p))
                equals(multiply(p,p),p)
                projections[eig]=p
            total=[[0j]*3 for _ in range(3)]
            rebuild=[[0j]*3 for _ in range(3)]
            polynomial=[[0j]*3 for _ in range(3)]
            for eig,p in projections.items():
                total=add(total,p)
                rebuild=add(rebuild,scale(eig,p))
                polynomial=add(polynomial,scale((eig+1)**2,p))
                for other,q in projections.items():
                    if eig!=other:
                        equals(multiply(p,q),[[0j]*3 for _ in range(3)])
            equals(total,eye(3))
            equals(rebuild,a)
            equals(polynomial,add(add(multiply(a,a),scale(2,a)),eye(3)))
            # Nontrivial eigenspace multiplicity is checked by every column
            # of the unitary change-of-basis, including repeated eigenvalues.
            for j,eig in enumerate(eigenvalues):
                column=tuple(u[i][j] for i in range(3))
                assert all(close(x,eig*y) for x,y in
                           zip(matvec(a,column),column))
                projected=matvec(projections[eig],column)
                assert all(close(x,y) for x,y in zip(projected,column))
            checks+=1
    return checks


def commuting_schur_cases():
    """A common unitary triangularizes two commuting defective matrices."""
    n=[[0j,1+0j],[0j,0j]]
    gs=add(eye(2),n)
    gt=add(scale(2,eye(2)),scale(3,n))
    assert gs[0][1]!=0 and gt[0][1]!=0
    count=0
    for theta,phase in ((0.,0.),(.2,.3),(.7,1.1),(1.2,2.0)):
        q=unitary(theta,phase)
        u=adjoint(q)
        equals(multiply(u,q),eye(2))
        s=multiply(multiply(q,gs),u)
        t=multiply(multiply(q,gt),u)
        equals(multiply(s,t),multiply(t,s))
        equals(multiply(multiply(u,s),adjoint(u)),gs)
        equals(multiply(multiply(u,t),adjoint(u)),gt)
        equals(multiply(multiply(adjoint(u),gs),u),s)
        equals(multiply(multiply(adjoint(u),gt),u),t)
        nonnormal=any(not close(x,y)
                      for row1,row2 in zip(multiply(s,adjoint(s)),
                                           multiply(adjoint(s),s))
                      for x,y in zip(row1,row2))
        assert nonnormal
        count+=1
    return count



def commuting_diagonalizable_cases():
    """Commuting matrices with a common (possibly nonorthogonal) eigenbasis."""
    cases = (
        ([[1, 1], [0, 1]], [[1, -1], [0, 1]],
         (1, 2), (3, 5)),
        ([[1, 1, 0], [0, 1, 1], [0, 0, 1]],
         [[1, -1, 1], [0, 1, -1], [0, 0, 1]],
         (1, 1, 2), (3, 4, 5)),
    )
    count = 0
    for p, pinv, eig_s, eig_t in cases:
        n = len(p)
        equals(multiply(p, pinv), eye(n))
        equals(multiply(pinv, p), eye(n))
        ds, dt = diagonal(eig_s), diagonal(eig_t)
        s = multiply(multiply(p, ds), pinv)
        t = multiply(multiply(p, dt), pinv)
        equals(multiply(s, t), multiply(t, s))
        equals(multiply(multiply(pinv, s), p), ds)
        equals(multiply(multiply(pinv, t), p), dt)
        for j in range(n):
            v = tuple(p[i][j] for i in range(n))
            assert all(close(x, eig_s[j] * y)
                       for x, y in zip(matvec(s, v), v))
            assert all(close(x, eig_t[j] * y)
                       for x, y in zip(matvec(t, v), v))
            count += 1
        assert any(
            not close(s[i][j], adjoint(s)[i][j])
            for i in range(n) for j in range(n)
        )
    return count



def finite_field_simultaneous_diagonalization_cases():
    """Exhaustive 2x2 test over F2 and F3, including repeated eigenvalues."""
    from itertools import product

    def matvec_mod(a, v, p):
        return ((a[0]*v[0]+a[1]*v[1]) % p,
                (a[2]*v[0]+a[3]*v[1]) % p)

    def mul_mod(a, b, p):
        return tuple(
            sum(a[2*i+k]*b[2*k+j] for k in range(2)) % p
            for i in range(2) for j in range(2)
        )

    def eigenvector(a, v, p):
        w=matvec_mod(a, v, p)
        return any(w==tuple(lam*x % p for x in v)
                   for lam in range(p))

    def independent(v, w, p):
        return (v[0]*w[1]-v[1]*w[0]) % p != 0

    results={}
    for p in (2, 3):
        matrices=list(product(range(p), repeat=4))
        vectors=[v for v in product(range(p), repeat=2) if v != (0, 0)]
        eigen={a:{v for v in vectors if eigenvector(a, v, p)}
               for a in matrices}
        diagonalizable=[
            a for a in matrices
            if any(independent(v, w, p) for v in eigen[a]
                   for w in eigen[a])
        ]
        count=0
        for s in diagonalizable:
            for t in diagonalizable:
                if mul_mod(s, t, p) != mul_mod(t, s, p):
                    continue
                count += 1
                shared = eigen[s] & eigen[t]
                assert any(independent(v, w, p) for v in shared
                           for w in shared), (p,s,t)
        results[p]=count
    assert results == {2: 40, 3: 441}, results
    return sum(results.values())



if __name__=="__main__":
    a=normal_cases()
    b=hermitian_cases()
    c=counterexamples_and_commuting()
    d=dimension_three_cases()
    e=commuting_schur_cases()
    f=commuting_diagonalizable_cases()
    g=finite_field_simultaneous_diagonalization_cases()
    print("Spectral regression tests OK:",
          a,"normal similarities and projectors;",
          b,"Hermitian Rayleigh tests;",
          c,"commuting/defective checks;",
          d,"3x3 normal and repeated-eigenvalue checks;",
           e,"commuting Schur tests;",
          f,"simultaneous diagonalization checks;",
          g,"finite-field commuting diagonalization checks.")
