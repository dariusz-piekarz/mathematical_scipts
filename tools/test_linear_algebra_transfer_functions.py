"""Exact checks for chapter 28: transfer functions and forced systems."""
from fractions import Fraction as F
import itertools

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def matpow(a,n):
    out=[[F(int(i==j)) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out=matmul(out,a)
    return out

def markov(a,b,c,n):
    return [matmul(matmul(c,matpow(a,k)),b)[0][0] for k in range(n)]

def check_companion(a0,a1,b0,b1):
    a=[[F(0),F(1)],[-F(a0),-F(a1)]]
    b=[[F(0)],[F(1)]]
    c=[[F(b0),F(b1)]]
    vals=markov(a,b,c,6)
    # The Laurent coefficient recursion:
    # H0=b1, H1=b0-a1*b1, H_{k+2}=-a1 H_{k+1}-a0 H_k.
    assert vals[0]==b1
    assert vals[1]==b0-a1*b1
    for k in range(4):
        assert vals[k+2]==-a1*vals[k+1]-a0*vals[k]
    # The Kalman controllability matrix [B,AB] is always invertible.
    ab=matmul(a,b)
    assert b[0][0]*ab[1][0]-ab[0][0]*b[1][0]==-1

for a0,a1,b0,b1 in itertools.product(range(-2,3),repeat=4):
    check_companion(a0,a1,b0,b1)
print("Chapter 28: 625 exact companion/Markov recurrences: PASS")

# Check non-minimal hidden unstable mode.
a=[[F(1),F(0)],[F(0),F(-1)]]
b=[[F(0)],[F(1)]]
c=[[F(0),F(1)]]
assert markov(a,b,c,12)==[F((-1)**k) for k in range(12)]
print("Hidden unstable mode elimination: PASS")

# Discrete forced response: pulse and recursion agree.
a=[[F(0),F(1)],[F(-2),F(-3)]]
b=[[F(0)],[F(1)]]
c=[[F(3),F(2)]]
d=F(2)
for u in itertools.product([F(-1),F(0),F(1)],repeat=5):
    x=[[F(4)],[F(-3)]]
    outputs=[]
    for uk in u:
        outputs.append(matmul(c,x)[0][0]+d*uk)
        x=matmul(a,x)
        x[0][0]+=b[0][0]*uk
        x[1][0]+=b[1][0]*uk
    h=markov(a,b,c,5)
    state=[[F(4)],[F(-3)]]
    for k in range(5):
        predicted=matmul(c,matmul(matpow(a,k),state))[0][0]+d*u[k]
        predicted+=sum(h[k-1-j]*u[j] for j in range(k))
        assert predicted==outputs[k]
print("243 discrete forced-system exact tests: PASS")
