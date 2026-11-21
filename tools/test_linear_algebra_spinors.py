"""Exact/almost exact matrix tests for Pauli, Spin(2), Spin(3), Bloch sphere."""
from cmath import exp
from itertools import product
from math import cos, sin, pi, sqrt
from random import Random

I = ((1+0j,0j),(0j,1+0j))
Z = ((0j,0j),(0j,0j))
s1 = ((0j,1+0j),(1+0j,0j))
s2 = ((0j,-1j),(1j,0j))
s3 = ((1+0j,0j),(0j,-1+0j))
sigmas=(s1,s2,s3)
rng=Random(31011)

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def scale(c,A):
    return tuple(tuple(c*A[i][j] for j in range(2)) for i in range(2))

def dagger(A):
    return tuple(tuple(A[j][i].conjugate() for j in range(2)) for i in range(2))

def close(A,B,tol=1e-10):
    assert all(abs(A[i][j]-B[i][j])<tol for i in range(2) for j in range(2)), (A,B)

checks=0
for i,j in product(range(3),repeat=2):
    a,b=scale(1j,sigmas[i]),scale(1j,sigmas[j])
    close(add(mul(a,b),mul(b,a)),scale(-2 if i==j else 0,I))
    checks+=1

# Chirality Γ=i*c(e1)c(e2)=σ3 and eigenvalues ±1.
close(scale(1j,mul(scale(1j,s1),scale(1j,s2))),s3)
for q in range(-12,13):
    theta=q*pi/6
    c,d=cos(theta/2),sin(theta/2)
    spin=add(scale(c,I),scale(-1j*d,s3))
    expected=((exp(-1j*theta/2),0j),(0j,exp(1j*theta/2)))
    close(spin,expected)
    v1=mul(mul(spin,s1),dagger(spin))
    close(v1,add(scale(cos(theta),s1),scale(sin(theta),s2)))
    checks+=1
close(add(scale(cos(pi),I),scale(-1j*sin(pi),s3)),scale(-1,I))

def quat_spin(a,b,c,d):
    return add(scale(a,I),scale(-1j,add(add(scale(b,s1),scale(c,s2)),scale(d,s3))))

def quat_mul(q,p):
    a,b,c,d=q; w,x,y,z=p
    return (a*w-b*x-c*y-d*z,
            a*x+b*w+c*z-d*y,
            a*y-b*z+c*w+d*x,
            a*z+b*y-c*x+d*w)

for _ in range(500):
    u=[rng.randint(-4,4) for _ in range(4)]
    v=[rng.randint(-4,4) for _ in range(4)]
    if not any(u) or not any(v):
        continue
    def normalize(x):
        length=sqrt(sum(z*z for z in x))
        return tuple(z/length for z in x)
    q,p=normalize(u),normalize(v)
    U,V=quat_spin(*q),quat_spin(*p)
    close(mul(U,dagger(U)),I)
    determinant=U[0][0]*U[1][1]-U[0][1]*U[1][0]
    assert abs(determinant-1)<1e-10
    close(mul(U,V),quat_spin(*quat_mul(q,p)))
    checks+=1

# Bloch vectors, projective identification, phase invariance and action equivariance.
for _ in range(500):
    z1=complex(rng.randint(-5,5),rng.randint(-5,5))
    z2=complex(rng.randint(-5,5),rng.randint(-5,5))
    if z1==z2==0: continue
    r=sqrt(abs(z1)**2+abs(z2)**2)
    z1,z2=z1/r,z2/r
    w=(z1.conjugate()*z2)
    b=(2*w.real,2*w.imag,abs(z1)**2-abs(z2)**2)
    assert abs(sum(x*x for x in b)-1)<1e-10
    proj=((abs(z1)**2,z1*z2.conjugate()),(z2*z1.conjugate(),abs(z2)**2))
    close(proj,scale(.5,add(I,add(add(scale(b[0],s1),scale(b[1],s2)),scale(b[2],s3)))))
    angle=rng.randint(-50,50)*pi/37
    phase=exp(1j*angle)
    zp=(phase*z1,phase*z2)
    close(proj,((abs(zp[0])**2,zp[0]*zp[1].conjugate()),
                (zp[1]*zp[0].conjugate(),abs(zp[1])**2)))
    q=tuple(x/sqrt(30) for x in (1,2,3,4))
    U=quat_spin(*q)
    zprime=(U[0][0]*z1+U[0][1]*z2,U[1][0]*z1+U[1][1]*z2)
    pp=mul(mul(U,proj),dagger(U))
    close(pp,((abs(zprime[0])**2,zprime[0]*zprime[1].conjugate()),
              (zprime[1]*zprime[0].conjugate(),abs(zprime[1])**2)))
    checks+=1

# Exact central character: spin lifts ±1 act oppositely on spinors but identically on vectors.
close(quat_spin(1,0,0,0),I)
close(quat_spin(-1,0,0,0),scale(-1,I))
print(f"Pauli/Spin/Bloch regression checks: {checks} PASS")
