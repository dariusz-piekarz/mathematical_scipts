from itertools import product, permutations
from collections import Counter

counts = Counter()

# CAT-04-008: three independent coordinate-selection transformations.
# The source is a 2 x 2 x 2 array, each target axis has length 3.
selectors = list(product(range(2), repeat=3))
for a,b,c in product(selectors, repeat=3):
    for x in product(range(2), repeat=8):
        X = tuple(tuple(tuple(x[4*i+2*j+k] for k in range(2)) for j in range(2)) for i in range(2))
        left = tuple(tuple(tuple(X[i][j][k] for k in a) for j in b) for i in c)
        inner = tuple(tuple(tuple(X[i][j][k] for k in a) for j in b) for i in range(2))
        right = tuple(inner[i] for i in c)
        assert left == right
        counts['horizontal_assoc'] += 1

# CAT-04-001: noncommuting transformations on a one-object group category.
# Conjugation functors F_a, natural transformation F_a -> F_b by b a^-1.
G = list(permutations(range(3)))
e = (0,1,2)
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a): return tuple(a.index(i) for i in range(3))
def conj(a,x): return mul(mul(a,x),inv(a))
def nat(a,b): return mul(b,inv(a))
def hor(a,b,c,d): return mul(nat(c,d),conj(c,nat(a,b)))
for a,b,c,d,p,q in product(G, repeat=6):
    assert hor(a,c,d,q) == mul(hor(b,c,p,q),hor(a,b,d,p))
    counts['interchange'] += 1
for a,b,c,d,h in product(G, repeat=5):
    eta = hor(a,b,c,d)
    assert mul(conj(mul(d,b),h),eta) == mul(eta,conj(mul(c,a),h))
    counts['horizontal_naturality'] += 1

# CAT-04-010: short exact sequence of two-term complexes over F3.
# B1=A1+C1, B0=A0+C0; dB has upper-right entry t.
# dA=dC=0; delta(c)=t*c; chain-map condition is u*t=t2*v.
for t,t2,u,v,s,c,a in product(range(3),repeat=7):
    if (u*t-t2*v)%3: continue
    b=(a,c)
    fb=((u*b[0]+s*b[1])%3,v*b[1]%3)
    assert (t2*fb[1])%3 == (u*t*c)%3
    counts['connecting_naturality'] += 1
print(dict(counts))
print('Total:',sum(counts.values()))
