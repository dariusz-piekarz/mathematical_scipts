#!/usr/bin/env python3
"""Chapter 24 finite-model and LaTeX integration regressions.

Finite models test group and quotient identities, not topological generality.
"""
from itertools import permutations, product
from pathlib import Path
import json
import math
import re

ROOT = Path(__file__).resolve().parents[2]
CH = "chapters/pl/general_topology/24-grupy-topologiczne-i-przestrzenie-jednorodne.tex"


def op(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    return tuple(a.index(i) for i in range(len(a)))


def model_s3():
    g = list(permutations(range(3)))
    e = (0, 1, 2)
    even = frozenset(p for p in g if sum(
        p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 == 0)
    h = frozenset([e, (1, 0, 2)])
    assert len(even) == 3 and len(h) == 2
    assert all(op(x, inv(x)) == e for x in g)
    assert all(op(x, op(y, inv(x))) in even for x in g for y in even)
    assert any(op(x, op(y, inv(x))) not in h for x in g for y in h)
    # The induced left action on cosets is transitive; stabilizer of H is H.
    for x, y in product(g, repeat=2):
        mover = op(y, inv(x))
        assert frozenset(op(op(mover, x), z) for z in h) == (
            frozenset(op(y, z) for z in h))
    assert {x for x in g if frozenset(op(x, z) for z in h) == h} == set(h)

    def coset(x, subgroup):
        return frozenset(op(x, z) for z in subgroup)

    for sub, count in [(h, 3), (even, 2)]:
        cs = {coset(x, sub) for x in g}
        assert len(cs) == count
        assert frozenset().union(*cs) == frozenset(g)
        assert all(len(a & v) in (0, len(sub)) for a in cs for v in cs)

    tests = 0
    for a, b, x, y in product(g, repeat=4):
        if coset(a, even) == coset(x, even) and coset(b, even) == coset(y, even):
            assert coset(op(a, b), even) == coset(op(x, y), even)
            tests += 1
    return tests


def model_cyclic():
    count = 0
    for n in (2, 3, 4, 6, 8, 12):
        g = range(n)
        for d in range(1, n + 1):
            if n % d:
                continue
            h = {a for a in g if a % d == 0}
            cosets = {frozenset((a + v) % n for v in h) for a in g}
            assert len(cosets) == d
            for a, b, x, y in product(g, repeat=4):
                if (a-x) % n in h and (b-y) % n in h:
                    assert (a+b-x-y) % n in h
                    count += 1
    return count


def model_circle():
    count = 0
    for k in range(-8, 9):
        for t in (0., .125, .3333, .5, .8):
            a = [math.cos(2*math.pi*t), math.sin(2*math.pi*t)]
            v = [math.cos(2*math.pi*(t+k)), math.sin(2*math.pi*(t+k))]
            assert math.dist(a, v) < 1e-11
            count += 1
    return count



def model_birkhoff_kakutani():
    """Finite weighted word distances model the chain construction."""
    tests = 0
    for n in (4, 8, 12):
        subgroup = {0, n//2}
        u = [set(range(n)), subgroup, {0}, {0}]
        assert all({(a+b+c) % n for a in u[k+1]
                    for b in u[k+1] for c in u[k+1]} <= u[k]
                   for k in range(3))
        rho = [0. if g == 0 else (.5 if g in subgroup else 1.)
               for g in range(n)]
        d = [[rho[(y-x) % n] for y in range(n)]
             for x in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        for x, y, z in product(range(n), repeat=3):
            assert d[x][y] >= 0
            assert (d[x][y] == 0) == (x == y)
            assert abs(d[x][y] - d[y][x]) < 1e-10
            assert d[x][z] <= d[x][y] + d[y][z] + 1e-10
            assert abs(d[(x+z) % n][(y+z) % n] - d[x][y]) < 1e-10
            tests += 1
        for k in (0, 1, 2):
            ball = {g for g in range(n) if d[0][g] < 2**(-k)}
            assert u[k+1] <= ball <= u[k]
    return tests

def test_source():
    chapter = (ROOT / CH).read_text(encoding="utf-8")
    entry = (ROOT / "books/pl/general_topology_ch24.tex").read_text(encoding="utf-8")
    book = (ROOT / "books/pl/general_topology.tex").read_text(encoding="utf-8")
    cat = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
    chapters = next(x["chapters"] for x in cat["books"] if x["id"] == "general_topology")
    assert len(chapters) >= 24 and chapters[23] == CH
    assert r"\input{../../" + CH + "}" in entry
    assert r"\input{../../" + CH + "}" in book
    assert r"\setcounter{chapter}{23}" in entry
    assert "rozdziały 01–24 stabilne" in book
    labels = re.findall(r"\\label\{([^}]+)\}", chapter)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", chapter)
    assert len(labels) == len(set(labels)) and len(labels) >= 30
    assert set(refs) <= set(labels), sorted(set(refs)-set(labels))
    for label in ("thm:topog24-difference", "lem:topog24-closure",
                  "thm:topog24-regular", "thm:topog24-subgroup-closure",
                  "thm:topog24-open-quotient", "thm:topog24-coset-action",
                  "thm:topog24-coset-hausdorff",
                  "thm:topog24-normal-quotient", "thm:topog24-isomorphism",
                  "thm:topog24-coset-compact", "thm:topog24-identity-component",
                  "thm:topog24-uniformities", "thm:topog24-birkhoff-kakutani",
                  "cor:topog24-right-metric"):
        assert rf"\label{{{label}}}" in chapter
    for env in ("definicja", "twierdzenie", "stwierdzenie", "wniosek",
                "lemat", "uwaga", "przyklad", "proof", "figure", "tikzpicture",
                "enumerate"):
        assert len(re.findall(r"\\begin\{" + env + r"\}", chapter)) == len(
            re.findall(r"\\end\{" + env + r"\}", chapter)), env
    for bad in (r"\bunia\b", r"zwartościowani\w*", r"pierwszoprzeliczaln\w*",
                r"drugoprzeliczaln\w*", r"sekwencyjn\w*"):
        assert not re.search(bad, chapter, re.IGNORECASE), bad
    assert "miary Haara" in chapter
    return len(labels), len(refs)


if __name__ == "__main__":
    n = model_s3()
    c = model_cyclic()
    t = model_circle()
    bk = model_birkhoff_kakutani()
    labels, refs = test_source()
    print(f"PASS ch24: {n} S3 quotient checks, {c} cyclic checks, "
          f"{t} circle checks, {bk} BK chain checks, "
          f"{labels} labels, {refs} local refs")
