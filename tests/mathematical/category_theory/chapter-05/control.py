from itertools import product
from collections import Counter

counts = Counter()

# CAT-05-002/008: all relations between sets of size at most three.
def rel(n, m):
    pairs = list(product(range(n), range(m)))
    for mask in range(1 << len(pairs)):
        yield frozenset(p for i,p in enumerate(pairs) if mask >> i & 1)

def compose(s, r):
    return frozenset((a,c) for a,b in r for bb,c in s if b == bb)

for n,m in product(range(4), repeat=2):
    out, inc = list(rel(0,m)), list(rel(n,0))
    assert len(out) == len(inc) == 1
    z = compose(out[0],inc[0])
    assert z == frozenset()
    counts['zero_factorization'] += 1
    for r in rel(n,m):
        assert compose(frozenset(),r) == frozenset()
        assert compose(r,frozenset()) == frozenset()
        counts['relation_absorption'] += 1
    assert (frozenset((i,i) for i in range(n)) == z) == (n == 0)
    counts['zero_identity'] += 1

# CAT-05-007: split monos from singleton in finite Set.
for n in range(1,7):
    for a in range(n):
        f=(a,)
        r=(0,)*n
        assert tuple(r[i] for i in f) == (0,)
        counts['split_mono'] += 1

# CAT-05-008/009: linear maps over F2, product functor V -> V x V.
def apply(a,n,m,x):
    return tuple(sum(a[i*n+j]*x[j] for j in range(n))%2 for i in range(m))
def zero(n,m,x):
    return apply((0,)*(n*m),n,m,x)
for n,m in product(range(4),repeat=2):
    for a in product(range(2),repeat=n*m):
        for x in product(range(2),repeat=n):
            assert apply(a,n,m,zero(n,n,x)) == zero(n,m,x)
            assert zero(m,m,apply(a,n,m,x)) == zero(n,m,x)
            counts['linear_absorption'] += 1
    for x,y in product(product(range(2),repeat=n),repeat=2):
        assert zero(n,m,x)+zero(n,m,y) == zero(2*n,2*m,x+y)
        counts['product_functor_zero'] += 1

print(dict(counts))
print('Total:',sum(counts.values()))
