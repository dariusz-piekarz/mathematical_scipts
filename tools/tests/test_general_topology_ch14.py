#!/usr/bin/env python3
"""Regression tests for relocation of local compactness from 11 to 14."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
P11 = ROOT / "chapters/pl/general_topology/11-zupelnosc-i-twierdzenie-bairea.tex"
P14 = ROOT / "chapters/pl/general_topology/14-zwartosc-lokalna.tex"
BOOK = ROOT / "books/pl/general_topology.tex"
STANDALONE = ROOT / "books/pl/general_topology_ch14.tex"

def test_relocation():
    c11 = P11.read_text(encoding="utf-8")
    c14 = P14.read_text(encoding="utf-8")
    book = BOOK.read_text(encoding="utf-8")
    standalone = STANDALONE.read_text(encoding="utf-8")
    moved_labels = (
        "sec:topog-baire-lokalnie-zwarte",
        "def:topog-baire-lokalna-zwartosc",
        "lem:topog-baire-zwarte-domkniecie",
        "thm:topog-baire-lokalnie-zwarte",
    )
    for label in moved_labels:
        assert rf"\label{{{label}}}" not in c11, label
        assert c14.count(rf"\label{{{label}}}") == 1, label
    assert "lokalnie zwartych" in c11  # forward pointer only
    assert r"\begin{definicja}[Zwartość lokalna]" not in c11
    assert r"\begin{lemat}[Otoczenia o zwartym domknięciu]" in c14
    assert r"\overline W^{\,X}=\overline H^{\,K}" in c14
    assert r"\ref{lem:topog-baire-zwarte-domkniecie}" in c14
    assert r"\begin{twierdzenie}[Twierdzenie Baire'a --- wersja lokalnie zwarta]" in c14
    assert r"\label{thm:topog-baire-metryczne}" in c11
    assert r"\label{prop:topog-lokalna-podprzestrzenie}" in c14
    assert r"\label{prop:topog-lokalna-iloczyny}" in c14
    assert r"\label{thm:topog-lokalna-wyczerpanie}" in c14
    assert r"\label{prop:topog-lokalna-drugi-aksjomat}" in c14
    assert r"\label{ex:topog-lokalna-dyskretna-nie-sigma}" in c14
    assert r"\label{def:topog-lokalna-przeliczalnosc-nieskonczonosc}" in c14
    assert r"\label{def:topog-lokalna-sigma-zwarta}" in c14
    assert "nieprzeliczalnym" in c14
    assert r"\label{ex:topog-lokalna-q-sigma-nieskonczonosc}" in c14
    assert c11.index(r"\label{thm:topog-baire-metryczne}") < c11.index(r"\section{Konsekwencje")
    assert r"\setcounter{chapter}{13}" in standalone
    expected = r"\input{../../chapters/pl/general_topology/14-zwartosc-lokalna.tex}"
    assert expected in book and expected in standalone
    items = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))["books"]
    chapters = next(item["chapters"] for item in items if item["id"]=="general_topology")
    assert chapters[10].endswith("/11-zupelnosc-i-twierdzenie-bairea.tex")
    assert chapters[13].endswith("/14-zwartosc-lokalna.tex")
    assert len(chapters) == 14
    for tex in [c11,c14]:
        for env in ["definicja","lemat","twierdzenie","proof","uwaga"]:
            assert tex.count(r"\begin{"+env+"}") == tex.count(r"\end{"+env+"}")
    all_text = "\n".join((ROOT / ch).read_text(encoding="utf-8") for ch in chapters)
    labels = re.findall(r"\\label\{([^}]+)\}",all_text)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",all_text)
    assert len(labels) == len(set(labels))
    assert set(refs).issubset(set(labels)), sorted(set(refs)-set(labels))
    return len(labels),len(refs)

if __name__ == "__main__":
    labels,refs=test_relocation()
    print(f"PASS local compactness relocated to chapter 14: labels={labels}; references={refs}")
