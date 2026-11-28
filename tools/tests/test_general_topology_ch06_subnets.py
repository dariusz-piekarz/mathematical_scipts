from itertools import product

def powerset(X):
    return [frozenset(i for i in X if mask & (1<<i)) for mask in range(1<<len(X))]

def topologies(n):
    X=frozenset(range(n)); ps=powerset(tuple(X))
    for membership in product((False,True),repeat=len(ps)):
        tau={u for u,b in zip(ps,membership) if b}
        if frozenset() not in tau or X not in tau: continue
        if any((a|b) not in tau or (a&b) not in tau for a in tau for b in tau):continue
        yield tau

def preorders(n):
    D=range(n)
    for bits in range(1<<(n*n)):
        R={(i,j) for i in D for j in D if bits>>(i*n+j)&1}
        if any((i,i) not in R for i in D):continue
        if any((i,k) not in R for i,j in R for j2,k in R if j==j2):continue
        if any(not any((i,k) in R and (j,k) in R for k in D) for i in D for j in D):continue
        yield R

nchecks=0
for dn in (1,2,3):
  for R in preorders(dn):
    D=range(dn)
    for n in (1,2,3):
      X=set(range(n))
      for tau in topologies(n):
        for seq in product(range(n),repeat=dn):
          for x in X:
            neighborhood=[U for U in tau if x in U]
            cluster=all(any((d0,d) in R and seq[d] in U for d in D) for U in neighborhood for d0 in D)
            E=[(d,U) for d in D for U in neighborhood if seq[d] in U]
            if cluster:
              assert E
              ER=lambda a,b:(a[0],b[0]) in R and b[1]<=a[1]
              assert all(ER(a,a) for a in E)
              assert all(ER(a,c) for a in E for b in E for c in E if ER(a,b) and ER(b,c))
              assert all(any(ER(a,c) and ER(b,c) for c in E) for a in E for b in E)
              assert all(any(all(ER(e0,e) <= ((d0,e[0]) in R) for e in E) for e0 in E) for d0 in D)
              assert all(any(all(ER(e0,e) <= (seq[e[0]] in U) for e in E) for e0 in E) for U in neighborhood)
            nchecks+=1
print('PASS independent finite directed-preorder/subnet-construction cases:',nchecks)
