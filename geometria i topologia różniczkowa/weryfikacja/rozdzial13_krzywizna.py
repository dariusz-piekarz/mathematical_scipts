"""Niezależna kontrola rachunków rozdziału 13.

Uruchomienie: uv run --with sympy python weryfikacja/rozdzial13_krzywizna.py
Wymaga Python 3 i SymPy. Nie zapisuje plików ani nie zmienia źródła książki.
Wyprowadza krzywiznę z metryki, sprawdza pełną tabelę Kerra i kontrakcję,
a następnie kontroluje normalizację czterowymiarowego Pfaffianu.
"""
import sympy as s
from functools import lru_cache
from itertools import combinations
r,x,a,M=s.symbols('r x a M',real=True)
S=r*r+a*a*x*x; D=r*r-2*M*r+a*a; q=1-x*x
g=s.Matrix([[-1+2*M*r/S,0,0,-2*M*r*a*q/S],
 [0,S/D,0,0],[0,0,S/q,0],
 [-2*M*r*a*q/S,0,0,q*(r*r+a*a+2*M*r*a*a*q/S)]])
gi=g.inv().applyfunc(s.factor)
def simp(f): return s.factor(f)
def diff(f,i): return s.diff(f,(r,x)[i-1]) if i in (1,2) else s.S.Zero
@lru_cache(None)
def G(k,i,j):
 return simp(sum(gi[k,l]*(diff(g[l,j],i)+diff(g[l,i],j)-diff(g[i,j],l))/2 for l in range(4)))
@lru_cache(None)
def R(k,b,i,j):
 if i==j:return s.S.Zero
 if i>j:return -R(k,b,j,i)
 return simp(diff(G(k,j,b),i)-diff(G(k,i,b),j)+sum(G(k,i,l)*G(l,j,b)-G(k,j,l)*G(l,i,b) for l in range(4)))
for i in range(4):
 for j in range(i,4):
  value=simp(sum(R(k,j,k,i) for k in range(4)))
  assert value==0,(i,j,value)
 print('Ricci row',i,'OK',flush=True)
# Orthogonal vectors F_0,F_1,F_2,F_3; E_2 points toward increasing theta.
F=s.Matrix([[r*r+a*a,0,0,a*q],[0,1,0,0],[0,0,-1,0],[a,0,0,1]])
N=[-S*D,S/D,S/q,S*q]
assert (F.T*g*F-s.diag(*N)).applyfunc(simp)==s.zeros(4)
@lru_cache(None)
def low(i,j,k,l):return simp(sum(g[l,z]*R(z,k,i,j) for z in range(4)))
pair=list(combinations(range(4),2))
B=s.zeros(6)
for pi,(i,j) in enumerate(pair):
 for pk,(k,l) in enumerate(pair[pi:],pi):
  z=simp(sum(F[ii,i]*F[jj,j]*F[kk,k]*F[ll,l]*low(ii,jj,kk,ll)
   for ii in range(4) if F[ii,i]!=0 for jj in range(4) if F[jj,j]!=0
   for kk in range(4) if F[kk,k]!=0 for ll in range(4) if F[ll,l]!=0))
  B[pi,pk]=B[pk,pi]=z
  if z!=0: print('B',i,j,k,l,':',z,flush=True)
 print('Curvature row',pi,'OK',flush=True)
K=simp(4*sum(B[i,j]**2/(N[pair[i][0]]*N[pair[i][1]]*N[pair[j][0]]*N[pair[j][1]]) for i in range(6) for j in range(6)))
expected=48*M*M*(r**6-15*a*a*r**4*x*x+15*a**4*r*r*x**4-a**6*x**6)/S**6
assert simp(K-expected)==0
print('FULL SYMBOLIC KERR CONTRACTION OK',flush=True)

# Porównanie wszystkich 36 pozycji tabeli z niezależnym rachunkiem.
alpha=M*r*(r*r-3*a*a*x*x)/S**3
beta=M*a*x*(3*r*r-a*a*x*x)/S**3
table=s.diag(2*alpha,-alpha,-alpha,alpha,alpha,-2*alpha)
table[0,5]=table[5,0]=-2*beta
table[1,4]=table[4,1]=-beta
table[2,3]=table[3,2]=beta
for i,(ii,jj) in enumerate(pair):
 for j,(kk,ll) in enumerate(pair):
  if i==j:
   denominator=N[ii]*N[jj]*(-1 if ii==0 else 1)
  elif len({ii,jj,kk,ll})==4:
   denominator=S**2
  else:
   assert B[i,j]==0
   continue
  assert simp(B[i,j]-table[i,j]*denominator)==0,(i,j)
print('KERR: all 36 table entries OK')

# Usunięcie mianownika Delta przez współrzędne wpadające (v,r,x,psi).
change=s.eye(4)
change[0,1]=-(r*r+a*a)/D
change[3,1]=-a/D
ingoing=(change.T*g*change).applyfunc(simp)
expected_ingoing=s.Matrix([
 [-1+2*M*r/S,1,0,-2*M*r*a*q/S],
 [1,0,0,-a*q],
 [0,0,S/q,0],
 [-2*M*r*a*q/S,-a*q,0,q*(r*r+a*a+2*M*r*a*a*q/S)]])
assert (ingoing-expected_ingoing).applyfunc(simp)==s.zeros(4)
assert simp(ingoing.det()+S*S)==0  # x=cos(theta); w theta mnożymy przez sin^2(theta).
print('KERR: horizon coordinate extension and determinant OK')

# Ogólny algebraiczny tensor krzywizny w 4D: iloczyny Kulkarni--Nomizu.
# Bierzemy dokładne macierze całkowitoliczbowe, także z elementami mieszanymi.
from itertools import product, permutations
from random import Random
rng=Random(1304)
indices=list(product(range(4),repeat=4))
perms=list(permutations(range(4)))
def eps(p):
 return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
for trial in range(5):
 tensor={idx:0 for idx in indices}
 for term in range(4):
  h=s.zeros(4);k=s.zeros(4)
  for i in range(4):
   for j in range(i,4):
    h[i,j]=h[j,i]=rng.randrange(-3,4)
    k[i,j]=k[j,i]=rng.randrange(-3,4)
  for i,j,z,w in indices:
   tensor[i,j,z,w]+=h[i,w]*k[j,z]+h[j,z]*k[i,w]-h[i,z]*k[j,w]-h[j,w]*k[i,z]
 def T(i,j,z,w):return tensor[i,j,z,w]
 for i,j,z,w in indices:
  assert T(i,j,z,w)+T(j,z,i,w)+T(z,i,j,w)==0
 ric=s.Matrix(4,4,lambda i,j:sum(T(k,i,j,k) for k in range(4)))
 norm=sum(v*v for v in tensor.values())
 combo=norm-4*sum(v*v for v in ric)+s.trace(ric)**2
 double_eps=sum(eps(ijkl)*eps(abcd)*T(*abcd[:2],ijkl[1],ijkl[0])*T(*abcd[2:],ijkl[3],ijkl[2]) for ijkl in perms for abcd in perms)
 assert double_eps==4*combo
 # Direct wedge products in Pf(Omega)=O12 O34-O13 O24+O14 O23.
 def wedge(i,j,k,l):
  return sum(eps(abcd)*T(*abcd[:2],j,i)*T(*abcd[2:],l,k) for abcd in perms)/4
 pf=wedge(0,1,2,3)-wedge(0,2,1,3)+wedge(0,3,1,2)
 assert pf==combo/8
print('PFAFFIAN: five non-diagonal algebraic curvature tests OK')
