#!/usr/bin/env python3
"""Chapter 16 structural and finite-model regression tests."""
import json
import re
from pathlib import Path
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex"

def test_initial_topology():
    cases = 0
    for f in product((0,1), repeat=3):
        for g in product((0,1), repeat=3):
            basis = [frozenset(i for i in range(3) if h[i]==v)
                     for h in (f,g) for v in (0,1)]
            topology = {frozenset(),frozenset(range(3)),*basis}
            for _ in range(6):
                topology |= {a & b for a in topology for b in topology}
                topology |= {a | b for a in topology for b in topology}
            assert set(basis) <= topology
            assert all(a & b in topology and a | b in topology
                       for a in topology for b in topology)
            cases += 1
    return cases

def test_sources():
    text = (ROOT/CH).read_text(encoding="utf-8")
    book = (ROOT/"books/pl/general_topology.tex").read_text(encoding="utf-8")
    standalone = (ROOT/"books/pl/general_topology_ch16.tex").read_text(encoding="utf-8")
    assert r"\input{../../"+CH+"}" in book
    assert r"\input{../../"+CH+"}" in standalone
    assert r"\setcounter{chapter}{15}" in standalone
    for name in (
        "def:topog-uzwarcenia-topologia-poczatkowa",
        "prop:topog-uzwarcenia-poczatkowa-ciaglosc",
        "thm:topog-uzwarcenia-funkcyjny-opis",
        "def:topog-uzwarcenia-uzwarcenie",
        "thm:topog-uzwarcenia-istnienie",
        "def:topog-uzwarcenia-rownowaznosc",
        "prop:topog-uzwarcenia-homeomorfizm-jednoznaczny",
        "prop:topog-uzwarcenia-zwarta",
        "def:topog-uzwarcenia-porzadek",
        "prop:topog-uzwarcenia-porzadek-klasy",
        "ex:topog-uzwarcenia-dwa-przedzialu",
        "ex:topog-uzwarcenia-ciag-zbiezny",
    ):
        assert r"\label{"+name+"}" in text, name
    assert r"p\circ e_1=e_2" in text
    assert r"q\circ p=\mathrm{id}_{K_1}" in text
    assert r"(S^1,e_2)\preccurlyeq([0,1],e_1)" in text
    for env in ("definicja","twierdzenie","stwierdzenie","przyklad","uwaga","proof","enumerate"):
        assert text.count(r"\begin{"+env+"}") == text.count(r"\end{"+env+"}")
    books = json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))["books"]
    chapters = next(b["chapters"] for b in books if b["id"]=="general_topology")
    assert len(chapters)==16 and chapters[15]==CH
    merged="\n".join((ROOT/p).read_text(encoding="utf-8") for p in chapters)
    labels=re.findall(r"\\label\{([^}]+)\}",merged)
    refs=re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",merged)
    assert len(labels)==len(set(labels))
    assert set(refs)<=set(labels), sorted(set(refs)-set(labels))
    assert not re.search(r"zwartościowani|zbieżności\s+zwartej",text,re.I)
    return len(labels),len(refs)

if __name__=="__main__":
    cases=test_initial_topology()
    labels,refs=test_sources()
    print(f"PASS initial-topology models={cases}; labels={labels}; refs={refs}")
