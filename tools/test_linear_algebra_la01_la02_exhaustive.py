#!/usr/bin/env python3
"""Independent exhaustive finite-field checks for LA01/LA02, 2026-11-22."""
from itertools import combinations, product
from collections import Counter
from hashlib import sha256
from pathlib import Path

counts = Counter()

def add(u, v, p):
    return tuple((a+b) % p for a,b in zip(u,v))

def mul(a, v, p):
    return tuple((a*x) % p for x in v)

def span(gens, p, n):
    ans = { (0,)*n }
    for v in gens:
        ans = {add(x, mul(a, v, p), p) for x in ans for a in range(p)}
    return frozenset(ans)

def indep(gens, p, n):
    return len(span(gens, p, n)) == p**len(gens)

def all_subspaces(p, n):
    vectors = list(product(range(p), repeat=n))
    nonzero = [v for v in vectors if any(v)]
    seen = {frozenset({(0,)*n}): tuple()}
    for k in range(1, n+1):
        for generators in combinations(nonzero, k):
            if indep(generators, p, n):
                sp = span(generators,p,n)
                if sp not in seen:
                    seen[sp] = generators
    return seen

def check(condition, key):
    counts[key] += 1
    if not condition:
        raise AssertionError(f"FAILED {key}, at count {counts[key]}")

for p,n in [(2,2), (2,3), (2,4), (3,2), (3,3)]:
    subspaces = all_subspaces(p,n)
    V = frozenset(product(range(p), repeat=n))
    check(V in subspaces, 'full_space_enumerated')
    check(len(subspaces[frozenset({(0,)*n})])==0, 'zero_basis')
    for U,basis_U in subspaces.items():
        dU = len(basis_U)
        check(len(U)==p**dU, 'basis_dimension')
        # Finite Hamel basis extension inside any spanning set (choose full V as S)
        B = list(basis_U)
        for v in V:
            if v not in span(B,p,n):
                B.append(v)
        check(indep(B,p,n) and span(B,p,n)==V and len(B)==n, 'basis_extension')
        # All quotient cosets, well-defined quotient operations and |V/U|=p^(n-dim U)
        cosets = {frozenset(add(v,u,p) for u in U) for v in V}
        check(len(cosets)==p**(n-dU), 'quotient_cardinality')
        check(all(len(c)==len(U) for c in cosets), 'coset_equipotence')
        check(all((c1==c2)==(len(c1.intersection(c2))>0) for c1 in cosets for c2 in cosets), 'coset_partition')
        for W,basis_W in subspaces.items():
            dW = len(basis_W)
            inter = U.intersection(W)
            plus = frozenset(add(u,w,p) for u in U for w in W)
            check(plus in subspaces, 'sum_is_subspace')
            check(inter in subspaces, 'intersection_is_subspace')
            dI = len(subspaces[inter]); dS = len(subspaces[plus])
            check(dS+dI==dU+dW, 'dimension_formula')
            check((dI==0)==(len(U)*len(W)==len(plus)), 'direct_sum_criterion')
            check(len(U)*len(W)//len(inter)==len(plus), 'second_iso_cardinality')
            # Map U/(U∩W) -> (U+W)/W: well defined and bijective.
            domain_cosets = {frozenset(add(u,t,p) for t in inter) for u in U}
            target_cosets = {frozenset(add(x,w,p) for w in W) for x in plus}
            rel = {}
            for u in U:
                source = frozenset(add(u,t,p) for t in inter)
                target = frozenset(add(u,w,p) for w in W)
                if source in rel:
                    check(rel[source]==target, 'second_iso_well_defined')
                rel[source]=target
            check(len(rel)==len(domain_cosets)==len(target_cosets) and set(rel.values())==target_cosets, 'second_iso_bijection')

# Three proper lines cover F_2^2: finite field assumption is essential.
lines = [S for S in all_subspaces(2,2) if len(S)==2]
check(len(lines)==3 and frozenset().union(*lines)==frozenset(product(range(2),repeat=2)), 'finite_field_union_counterexample')

# A property guaranteed by linear independence: no basis element belongs to span of other basis elements.
for p,n in [(2,4),(3,3)]:
    for U,basis_U in all_subspaces(p,n).items():
        for i,v in enumerate(basis_U):
            check(v not in span(basis_U[:i]+basis_U[i+1:],p,n), 'independent_coordinate_uniqueness')

print('EXHAUSTIVE TESTS OF ALL SUBSPACE PAIRS')
for p,n in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
    print(f'F_{p}^{n}: {len(all_subspaces(p,n))} subspaces')
print('ASSERTIONS PER FAMILY')
for k, v in sorted(counts.items()):
    print(f'{k}: {v}')
print('TOTAL PASS:', sum(counts.values()))
print('SHA256:', sha256(Path(__file__).read_bytes()).hexdigest())
