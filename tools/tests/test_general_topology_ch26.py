#!/usr/bin/env python3
"""Chapter 26 finite-chain, short-excursion and TeX regression checks."""
from itertools import product
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/26-twierdzenie-hahna-mazurkiewicza.tex"

def chain_models():
    tests=0
    for n in (3,7,17):
        xs=[k/(n-1) for k in range(n)]
        delta=1.01/(n-1)
        for a,b in product(range(n),repeat=2):
            inds=list(range(a,b+1)) if a<=b else list(range(a,b-1,-1))
            if a==b: inds=[a,b]
            assert all(abs(xs[inds[j]]-xs[inds[j-1]])<delta for j in range(1,len(inds)))
            tests+=1
    return tests

def path(knots,t):
    if t<=knots[0][0]:return knots[0][1]
    for (a,x),(b,y) in zip(knots,knots[1:]):
        if t<=b:return x+(y-x)*(t-a)/(b-a)
    return knots[-1][1]

def excursion_model():
    old=[(0.,0.),(1.,1.)]
    new=[(0.,0.),(.48,.48),(.50,.50),(.505,.56),(.510,.50),(.52,.52),(1.,1.)]
    assert new[0]==old[0] and new[-1]==old[-1]
    assert .56 in [v for _,v in new]
    for k in range(2001):
        t=k/2000
        assert abs(path(new,t)-path(old,t))<.12
    return 2001

def dyadic_nets():
    tested=0
    for n in range(1,9):
        net=[k/2**n for k in range(2**n+1)]
        old=[k/2**(n-1) for k in range(2**(n-1)+1)]
        for x in net:
            assert min(abs(x-y) for y in old)<=2**(-n)
            tested+=1
    return tested

def integration():
    chapter=(ROOT/CH).read_text(encoding="utf-8")
    entry=(ROOT/"books/pl/general_topology_ch26.tex").read_text(encoding="utf-8")
    book=(ROOT/"books/pl/general_topology.tex").read_text(encoding="utf-8")
    cat=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    chapters=next(b["chapters"] for b in cat["books"] if b["id"]=="general_topology")
    assert len(chapters)>=26 and chapters[25]==CH
    assert r"\input{../../"+CH+"}" in entry
    assert r"\input{../../"+CH+"}" in book
    assert r"\setcounter{chapter}{25}" in entry
    assert "rozdziały 01–25 stabilne" in book
    for i in ("08","10","25"):
        assert rf"\externaldocument{{general_topology_ch{i}}}" in entry
    own=set(re.findall(r"\\label\{([^}]+)\}",chapter))
    assert len(own)>=20
    for key in ("lem:topog26-uniform-local-connected","lem:topog26-chain",
                "thm:topog26-small-paths","lem:topog26-excursion",
                "thm:topog26-hm-sufficient","lem:topog26-image-second-countable",
                "lem:topog26-image-locally-connected",
                "thm:topog26-hahn-mazurkiewicz"):
        assert key in own,key
    all_tex="\n".join((ROOT/p).read_text(encoding="utf-8") for p in chapters)
    labels=re.findall(r"\\label\{([^}]+)\}",all_tex)
    refs=re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",all_tex)
    assert len(labels)==len(set(labels)),"duplicate labels"
    assert set(refs)<=set(labels), sorted(set(refs)-set(labels))
    for env in ("lemat","twierdzenie","stwierdzenie","wniosek",
                "definicja","uwaga","przyklad","proof","figure",
                "tikzpicture","enumerate"):
        assert chapter.count(r"\begin{"+env+"}")==chapter.count(r"\end{"+env+"}"),env
    for bad in (r"\bunia\b",r"zwartościowani\w*",r"pierwszoprzeliczaln\w*",
                r"drugoprzeliczaln\w*",r"sekwencyjn\w*"):
        assert not re.search(bad,chapter,re.I),bad
    assert re.search(r"niepusty spójny\s+podzbiór", chapter)
    assert "przestrzenią" in chapter
    return len(own),len(refs)

if __name__=="__main__":
    a=chain_models();b=excursion_model();c=dyadic_nets()
    labs,refs=integration()
    print(f"PASS ch26: {a} chain checks, {b} excursion samples, "
          f"{c} dyadic-net checks; {labs} labels, {refs} references")
