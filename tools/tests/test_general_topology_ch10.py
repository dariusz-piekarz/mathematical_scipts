#!/usr/bin/env python3
"""Chapter 10: finite-topology and explicit metric construction checks.

Finite spaces cannot establish Urysohn's theorem in its infinite form;
this script checks its finite implications and the concrete formulas.
The infinite examples require the separate written mathematical audit.
"""
from __future__ import annotations
from itertools import product
from pathlib import Path
import re

from test_general_topology_ch07 import all_topologies

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'chapters/pl/general_topology/10-metryzowalnosc.tex'
BOOK=ROOT/'books/pl/general_topology.tex'
STANDALONE=ROOT/'books/pl/general_topology_ch10.tex'


def t1(tau,n):
    X=(1<<n)-1
    return all((X^(1<<x)) in tau for x in range(n))


def is_regular(tau,n):
    X=(1<<n)-1
    for F in range(1<<n):
        if X^F not in tau:
            continue
        for x in range(n):
            if F&(1<<x):
                continue
            if not any((u&(1<<x)) and (v&F)==F and (u&v)==0
                       for u in tau for v in tau):
                return False
    return True


def is_normal(tau,n):
    X=(1<<n)-1
    closed=[X^u for u in tau]
    for F in closed:
        for G in closed:
            if F&G:
                continue
            if not any((u&F)==F and (v&G)==G and not(u&v)
                       for u in tau for v in tau):
                return False
    return True


def finite_axiom_checks():
    counts={'topologies':0,'regular_lindelof_normal':0,'t3_iff_discrete':0,'hausdorff_iff_discrete':0}
    for n in range(5):
        full=frozenset(range(1<<n))
        for tau in all_topologies(n):
            tau=frozenset(tau)
            counts['topologies']+=1
            X=(1<<n)-1
            reg=is_regular(tau,n)
            normal=is_normal(tau,n)
            # Every finite topological space is Lindelof.
            assert not reg or normal, ('regular nonnormal finite topology',n,tau)
            counts['regular_lindelof_normal']+=1
            # In finite spaces, T1 is equivalent to discreteness.
            assert (reg and t1(tau,n)) == (tau==full)
            counts['t3_iff_discrete']+=1
            # Hausdorff finite -> each singleton open, conversely evident.
            hausdorff=all(any((u&(1<<x)) and (v&(1<<y)) and not(u&v)
                               for u in tau for v in tau)
                           for x in range(n) for y in range(n) if x!=y)
            assert hausdorff==(tau==full)
            counts['hausdorff_iff_discrete']+=1
    assert counts['topologies']==390
    return counts


def explicit_metrics():
    cases=0; triangles=0
    # Discrete finite spaces: separating continuous coordinate functions.
    for m in range(2,9):
        fs=[lambda x,k=k: 0 if x==k else 1 for k in range(m)]
        d=lambda x,y: sum(2.0**(-(n+1))*abs(f(x)-f(y))
                          for n,f in enumerate(fs))
        for x in range(m):
            assert d(x,x)==0
            for y in range(m):
                assert (d(x,y)>0)==(x!=y)
                assert abs(d(x,y)-d(y,x))<1e-13
                for z in range(m):
                    assert d(x,z)<=d(x,y)+d(y,z)+1e-13
                    triangles+=1
        mind=min(d(x,y) for x in range(m) for y in range(m) if x!=y)
        assert all(tuple(y for y in range(m) if d(x,y)<mind/2)==(x,)
                   for x in range(m))
        cases+=1
    return cases,triangles


def bounded_metric_and_products():
    cases=0; triangles=0
    for digits in range(1,5):
        points=list(product(range(3),repeat=digits))
        rho=lambda a,b: sum(2**(-(k+1))*min(1,abs(a[k]-b[k]))
                            for k in range(digits))
        for a in points:
            assert rho(a,a)==0
            for b in points:
                assert rho(a,b)==rho(b,a)
                assert (rho(a,b)>0)==(a!=b)
                for c in points:
                    assert rho(a,c)<=rho(a,b)+rho(b,c)+1e-14
                    triangles+=1
        assert all(any(rho(a,b)>0 for b in points if b!=a) for a in points) if len(points)>1 else True
        cases+=1
    # The lower-limit topology's nonmetrizability cannot be shown
    # by a finite grid; it is checked from the written proof.
    return cases,triangles


def lint():
    src=SRC.read_text(encoding='utf8')
    book=BOOK.read_text(encoding='utf8')
    standalone=STANDALONE.read_text(encoding='utf8')
    assert src.startswith(r'\chapter{Metryzowalność przestrzeni topologicznych}')
    assert r'\input{../../chapters/pl/general_topology/10-metryzowalnosc.tex}' in book
    assert r'\setcounter{chapter}{9}' in standalone
    assert r'\input{../../chapters/pl/general_topology/10-metryzowalnosc.tex}' in standalone
    for expected in [
        'def:topog-pseudometryka-metryka',
        'prop:topog-metryka-t3-pierwszy',
        'lem:topog-t3-lindelof-normalna',
        'thm:topog-urysohn-metryzowalnosc',
        'cor:topog-urysohn-kostka-hilberta',
        'thm:topog-metryka-kostka-przeliczalna',
        'thm:topog-przeliczalny-iloczyn-metryzowalny',
        'cor:topog-zwarta-hausdorff-metryzowalna',
        'ex:topog-sorgenfrey-niemetryzowalna',
        'ex:topog-kostka-nieprzeliczalna',
        'ex:topog-iloraz-dwa-poczatki',
    ]:
        assert '\\label{'+expected+'}' in src,expected
    for env in ('twierdzenie','lemat','stwierdzenie','wniosek','definicja','przyklad','uwaga','proof','figure','tikzpicture'):
        assert src.count('\\begin{'+env+'}')==src.count('\\end{'+env+'}'),env
    texfiles=list((ROOT/'chapters/pl/general_topology').glob('*.tex'))
    labels=[];refs=[]
    for path in texfiles:
        s=path.read_text(encoding='utf8')
        labels+=re.findall(r'\\label\{([^}]+)\}',s)
        refs+=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',s)
        s=re.sub(r'\\(?:label|ref|eqref|pageref)\{[^}]+\}','',s)
        assert not re.search(r'\b(?:pierwszo\s+przeliczaln\w*|drugoprzeliczaln\w*|pierwsz\w*\s+przeliczalno\w*|drug\w*\s+przeliczalno\w*)',s,re.I),path
    assert len(labels)==len(set(labels)), 'duplicate labels'
    assert set(refs)<=set(labels), f'broken references: {set(refs)-set(labels)}'
    no_labels=re.sub(r'\\label\{[^}]+\}', '',src)
    assert not re.search(r'\b(kofinita|unia|sekwencj\w*|tensorowanie)\b',no_labels,re.I)
    assert 'quasi-składow' not in no_labels.lower()
    assert r'\clearpage' in src and 'ex:topog-iloraz-dwa-poczatki' in src
    assert 'Wykażmy teraz otwartość całej kuli' in src
    # Audit 2: a discrete topology does not have a unique basis.
    assert 'jego jedyna baza' not in src
    assert r'Dla każdej bazy $\mathcal A$' in src
    assert r'$x\in A\subseteq\{x\}$' in src
    assert 'Kula jest więc otwarta w topologii iloczynu' in src
    assert r'\varepsilon-D(x,z)' in src
    assert r'\arctan\colon\R\to(-\pi/2,\pi/2)' in src
    return len(labels),len(refs)


if __name__=='__main__':
    counts=finite_axiom_checks()
    u,tr=explicit_metrics()
    p,tp=bounded_metric_and_products()
    labels,refs=lint()
    print(f'PASS Chapter 10: finite={counts}; separating-metrics={u},'
          f' metric-triples={tr}; products={p}, product-triples={tp};'
          f' labels={labels}, refs={refs}')
