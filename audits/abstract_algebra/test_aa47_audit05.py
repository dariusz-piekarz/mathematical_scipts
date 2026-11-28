"""Independent AA-47 algebraic identities; not a substitute for full repository CI."""
from fractions import Fraction
import sympy as S

x,z=S.symbols('x z')

def test(name, condition):
    assert condition, name
    print('PASS',name)

# SymPy route: rational integration and Rothstein--Trager
f=2*x+3/(x-1)**3+5/(x-1)
R=x**2-S.Rational(3,2)/(x-1)**2
test('Hermite decomposition', S.cancel(f-S.diff(R,x)-5/(x-1))==0)
test('nonzero rational residue',S.residue(f,x,1)==5)
A=x+2; B=x**2-1
T=S.resultant(B,A-z*S.diff(B,x),x)
roots=[S.cancel(A.subs(x,a)/S.diff(B,x).subs(x,a)) for a in [-1,1]]
test('RT resultant roots',S.expand(T-S.prod(S.diff(B,x).subs(x,a)*(r-z) for a,r in zip([-1,1],roots)))==0)
test('RT reconstruction',S.cancel(A/B-sum(r/(x-a) for a,r in zip([-1,1],roots)))==0)
# Polynomial differential equation r' + h r = s, both positive and obstruction
h=x; r=x**2+1; s=S.expand(S.diff(r,x)+h*r)
test('polynomial differential solution',S.expand(S.diff(r,x)+h*r-s)==0)
test('constant h telescoping',S.expand(S.diff(x**3-3*x**2+6*x-6,x)+(x**3-3*x**2+6*x-6)-x**3)==0)
# Riccati examples, including algebraic counterexample
for name,r,q in [('riccati base',x,x*x+1),('riccati rational',x+1/x,x*x+3),('riccati algebraic',S.sqrt(x)-1/(4*x),x+S.Rational(5,16)/x**2)]:
    test(name,S.simplify(S.diff(r,x)+r*r-q)==0)
# Independent Fraction route: exact rational evaluation of two identities
for v in [Fraction(2),Fraction(3,2),Fraction(-2)]:
    test('Fraction Riccati at '+str(v),(1-1/v**2)+(v+1/v)**2==v*v+3)
    test('Fraction Hermite at '+str(v),2*v+3/(v-1)**3+5/(v-1)==(2*v+3/(v-1)**3)+5/(v-1))
