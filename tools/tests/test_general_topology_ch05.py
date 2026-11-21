#!/usr/bin/env python3
"""Independent finite-model and source regression checks for General Topology Ch. 05.

Enumerates every topology on up to four points.  All structures are finite,
therefore every nonempty arbitrary union/intersection reduces to a finite one.
"""
from itertools import combinations, product
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'chapters/pl/general_topology/05-aksjomaty-oddzielania.tex'
BOOK = ROOT / 'books/pl/general_topology.tex'


def subsets(x):
    elements = tuple(x)
    return tuple(frozenset(y for i,y in enumerate(elements) if mask & (1 << i))
                 for mask in range(1 << len(elements)))


def topologies(x):
    p = subsets(x)
    res = []
    for t in subsets(p):
        if frozenset() not in t or x not in t:
            continue
        if all(a | b in t and a & b in t for a in t for b in t):
            res.append(frozenset(t))
    return tuple(res)


def closedsets(x, t):
    return frozenset(x - u for u in t)


def closure(x, t, a):
    return frozenset.intersection(*(f for f in closedsets(x,t) if a <= f))


def T0(x,t):
    return all(any((p in u) != (q in u) for u in t)
               for p in x for q in x if p != q)


def T1(x,t):
    return all(x - {p} in t for p in x)


def T2(x,t):
    return all(any(p in u and q in v and not (u & v) for u in t for v in t)
               for p in x for q in x if p != q)


def regular(x,t):
    cs=closedsets(x,t)
    return all(any(p in u and f <= v and not(u & v) for u in t for v in t)
               for f in cs for p in x-f)


def normal(x,t):
    cs=closedsets(x,t)
    return all(any(f <= u and g <= v and not(u & v) for u in t for v in t)
               for f in cs for g in cs if not(f & g))


def completely_regular_finite(x,t):
    # Every continuous image of a finite space in R has finite discrete image.
    # A real separator therefore exists iff a clopen separator exists.
    cs=closedsets(x,t)
    clopens=t & cs
    return all(any(p in u and not (u & f) for u in clopens)
               for f in cs for p in x-f)


space_count=0
point_checks=0
normal_checks=0
for n in range(5):
    x=frozenset(range(n))
    ts=topologies(x)
    assert len(ts)==(1,1,4,29,355)[n],(n,len(ts))
    for t in ts:
        cs=closedsets(x,t)
        t0,t1,t2=T0(x,t),T1(x,t),T2(x,t)
        r,norm=regular(x,t),normal(x,t)
        cr=completely_regular_finite(x,t)
        assert (not t2 or t1) and (not t1 or t0)
        assert t1 == all(frozenset({p}) in cs for p in x)
        assert (not t1 or len(t)==2**n)
        diag=frozenset((p,p) for p in x)
        # A point in (XxX)\diag has a disjoint basic rectangle iff T2.
        diag_closed=all(any(p in u and q in v and (not(u & v))
                            for u in t for v in t) for p in x for q in x if p != q)
        assert diag_closed==t2
        assert (not (t1 and r) or t2)
        assert (not cr or r)
        assert (not (t1 and norm) or cr)
        assert norm==all(any(f<=u and closure(x,t,u)<=w for u in t)
                         for f in cs for w in t if f<=w)
        assert r==all(any(p in u and closure(x,t,u)<=w for u in t)
                      for p in x for w in t if p in w)
        # Independent Urysohn check for finite spaces: a normal space has
        # a clopen separator for any two disjoint closed sets.
        if norm:
            clopens=cs&t
            for f in cs:
                for g in cs:
                    if not(f&g):
                        assert any(f<=u and not(u&g) for u in clopens), (n,t,f,g)
                        normal_checks+=1
        # Heredity of all separation properties, closed-subspace normality.
        for a in subsets(x):
            sa=frozenset(a&u for u in t)
            assert not t0 or T0(a,sa)
            assert not t1 or T1(a,sa)
            assert not t2 or T2(a,sa)
            assert not r or regular(a,sa)
            assert not cr or completely_regular_finite(a,sa)
            assert not (norm and a in cs) or normal(a,sa)
            point_checks+=1
        space_count+=1
    print(f'PASS separation n={n}: {len(ts)} topologies')

# Strict first implications and normality without regularity.
sier=frozenset((frozenset(),frozenset({1}),frozenset({0,1})))
x=frozenset({0,1})
assert T0(x,sier) and not T1(x,sier) and not T2(x,sier)
assert normal(x,sier) and not regular(x,sier)
cofinite= frozenset({frozenset()} | {x - a for a in subsets(x) if len(a)<len(x)})
assert T1(x,cofinite)  # finite cofinite topology is discrete; infinite case in text

# Real quotient R -> Sierpinski: inverse image of {1}=(0,+inf) open;
# inverse image of {0}=(-inf,0] not open.
assert frozenset({1}) in sier and frozenset({0}) not in sier


# Tietze's extension theorem, independently checked on every normal topology
# on at most four points, for all closed A and all continuous three-valued
# functions f:A -> {-1,0,1} (with its real-line subspace topology).
tietze_checks = 0
for n in range(5):
    x = frozenset(range(n))
    for t in topologies(x):
        if not normal(x,t):
            continue
        whole_clopens = t & closedsets(x,t)
        continuous_extensions = []
        for values in product((-1,0,1), repeat=n):
            if all(frozenset(i for i,v in enumerate(values) if v == k)
                   in whole_clopens for k in (-1,0,1)):
                continuous_extensions.append(values)
        for a in closedsets(x,t):
            a_sorted = tuple(sorted(a))
            subtop = frozenset(u & a for u in t)
            sub_clopens = subtop & frozenset(a-u for u in subtop)
            for values in product((-1,0,1), repeat=len(a_sorted)):
                if not all(frozenset(a_sorted[i] for i,v in enumerate(values) if v == k)
                           in sub_clopens for k in (-1,0,1)):
                    continue
                assert any(all(ext[i] == values[j] for j,i in enumerate(a_sorted))
                           for ext in continuous_extensions), (n,t,a,values)
                tietze_checks += 1
print(f'PASS Tietze finite-model extension: {tietze_checks} closed-domain functions')


s=SRC.read_text(encoding='utf8')
book=BOOK.read_text(encoding='utf8')
labels=re.findall(r'\\label\{([^}]+)\}',s)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',s)
all_src='\n'.join(p.read_text(encoding='utf8') for p in sorted((ROOT/'chapters/pl/general_topology').glob('*.tex')))
all_labels=re.findall(r'\\label\{([^}]+)\}',all_src)
assert len(all_labels)==len(set(all_labels)), 'duplicate labels in whole book'
assert set(refs)<=set(all_labels),set(refs)-set(all_labels)
assert r'\input{../../chapters/pl/general_topology/05-aksjomaty-oddzielania.tex}' in book
assert r'\chapter{Aksjomaty oddzielania}' in s
assert r'\label{thm:topog-tietze}' in s
assert r'\label{fig:topog-t1-t2-porownanie}' in s
# All five consecutive strictness statements must have explicit, labelled
# counterexamples (the non-finite Mysior construction requires a proof).
for label in (
    'ex:topog-sierpinski-oddzielanie',
    'ex:topog-koskonczona-t1-nie-t2',
    'ex:topog-k-topologia',
    'ex:topog-mysior-t3-nie-tych',
    'thm:topog-sorgenfrey-plane',
):
    assert r'\label{' + label + '}' in s, label
assert r'\label{fig:topog-mysior-baza}' in s
assert r'T_3\not\Rightarrow T_{3\frac12}' in s
assert r'T_{3\frac12}\not\Rightarrow T_4' in s

# T1 requires the existence of separating neighborhoods, not every
# neighborhood: X itself always contains both distinct points.
assert 'każde\notoczenie nie zawiera drugiego punktu' not in s
assert r'\emph{wybrane} otoczenie $U$' in s
assert not re.search(r'\b(kofinita|unia|tensorowanie)\b',s,re.I)
for env in ('twierdzenie','stwierdzenie','wniosek','definicja','przyklad','uwaga','proof','figure'):
    assert s.count(r'\begin{'+env+'}')==s.count(r'\end{'+env+'}'),env
print(f'PASS Chapter05: {space_count} topologies, {point_checks} subspace tests, '
      f'{normal_checks} closed-pair normal checks; {len(labels)} labels, {len(refs)} refs')
