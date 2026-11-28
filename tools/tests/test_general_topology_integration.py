#!/usr/bin/env python3
"""Independent finite-model and LaTeX reference checks for general topology, ch. 01."""
from itertools import combinations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / 'chapters/pl/general_topology/01-przestrzenie-topologiczne.tex'
BOOK = ROOT / 'books/pl/general_topology.tex'

def power(items):
    items = list(items)
    return [frozenset(items[i] for i in range(len(items)) if mask & (1 << i))
            for mask in range(1 << len(items))]

def topological(t, x):
    p = set(power(x))
    return (set(t) <= p and frozenset() in t and x in t
            and all(a | b in t and a & b in t for a in t for b in t))

def generated(subbase, x):
    intersections = {x}
    for s in subbase:
        intersections.update({b & s for b in tuple(intersections)})
    sums = {frozenset()}
    for b in intersections:
        sums.update({u | b for u in tuple(sums)})
    return frozenset(sums)

def base_ok(base, x):
    return (frozenset().union(*base) == x and
            all(any(p in c and c <= a & b for c in base)
                for a in base for b in base for p in a & b))

for n, count in enumerate((1, 1, 4, 29)):
    x = frozenset(range(n))
    subsets = power(x)
    topologies = [frozenset(t) for t in power(subsets)
                  if topological(frozenset(t), x)]
    assert len(topologies) == count, (n, len(topologies))
    for subbase in power(subsets):
        tau = generated(subbase, x)
        assert topological(tau, x)
        assert tau == frozenset.intersection(*(
            t for t in topologies if all(b in t for b in subbase)))
        b = frozenset(subbase)
        assert base_ok(b, x) == any(
            b <= t and all(any(p in c and c <= u for c in b)
                           for u in t for p in u) for t in topologies)
    for tau in topologies:
        closed = frozenset(x - u for u in tau)
        assert all(frozenset.intersection(*family) in closed
                   for family in power(closed) if family)
        assert all(a | b in closed for a in closed for b in closed)
    print(f'PASS topology n={n}: {count} topologies, subbases, bases, closed families')

src = CH.read_text(encoding='utf-8')
book = BOOK.read_text(encoding='utf-8')
labels = re.findall(r'\\label\{([^}]+)\}', src)
refs = re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', src)
assert len(set(labels)) == len(labels)
assert set(refs) <= set(labels), set(refs) - set(labels)
assert r'\input{../../chapters/pl/general_topology/01-przestrzenie-topologiczne.tex}' in book
assert 'topologia koskończona' in src.lower()
assert not re.search(r'\b(kofinita|unia)\b', re.sub(r'\\label\{[^}]+\}', '', src), re.I)
for env in ('twierdzenie','stwierdzenie','definicja','przyklad','uwaga','proof','figure'):
    assert src.count(r'\begin{' + env + '}') == src.count(r'\end{' + env + '}')
print(f'PASS LaTeX: {len(labels)} unique labels; {len(refs)} references; terms and environments')
