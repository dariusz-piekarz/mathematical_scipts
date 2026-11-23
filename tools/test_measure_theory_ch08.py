"""Chapter 08: independent finite regressions for Lebesgue limit theorems.

Finite atomic models are regressions; general theorems require the proofs in TeX.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import math
import re


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters/pl/measure_theory"
FILES = (
    "01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex",
    "02-miary-i-ich-podstawowe-wlasnosci.tex",
    "03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex",
    "04-miara-lebesguea-na-przestrzeni-euklidesowej.tex",
    "05-struktura-przestrzeni-mierzalnych.tex",
    "06-funkcje-mierzalne-i-ich-aproksymacja.tex",
    "07-konstrukcja-calki-lebesguea.tex",
    "08-twierdzenia-graniczne-dla-calki-lebesguea.tex",
)


def nonnegative_term(value, mass):
    return 0 if value == 0 or mass == 0 else value * mass


def integrate_nonnegative(values, masses):
    return sum(nonnegative_term(f, w) for f, w in zip(values, masses))


def test_monotone_convergence():
    stages = [(a, b, c) for a, b, c in
              product((0, 1, 2, math.inf), repeat=3) if a <= b <= c]
    count = 0
    for ax, ay in product(stages, repeat=2):
        terms = tuple((ax[n], ay[n]) for n in range(3))
        for weights in product((0, 2, math.inf), repeat=2):
            ints = [integrate_nonnegative(f, weights) for f in terms]
            assert ints[0] <= ints[1] <= ints[2]
            assert ints[-1] == integrate_nonnegative(
                (max(ax), max(ay)), weights
            )
            count += 1
    assert count == 3600
    print(f"PASS R08 Beppo Levi finite stabilization: {count} models")


def test_fatou():
    # A periodic infinite sequence of three nonnegative functions has
    # liminf equal to its coordinatewise minimum.
    values = tuple(product((0, 1, 2, math.inf), repeat=2))
    count = 0
    for a, b, c in product(values, repeat=3):
        lower = tuple(min(a[i], b[i], c[i]) for i in range(2))
        for weights in product((0, 1, math.inf), repeat=2):
            lhs = integrate_nonnegative(lower, weights)
            rhs = min(integrate_nonnegative(v, weights) for v in (a, b, c))
            assert lhs <= rhs
            count += 1
    assert count == 36864
    print(f"PASS R08 Fatou periodic sequences: {count} models")


def test_dominated_convergence():
    count = 0
    for values in product((-2, -1, 0, 1, 2), repeat=2):
        for masses in product((0, 1, 3), repeat=2):
            true_integral = sum(f * w for f, w in zip(values, masses))
            majorant = sum(abs(f) * w for f, w in zip(values, masses))
            for n in range(1, 9):
                approx = [
                    Fraction(n-1, n) * x for x in values
                ]
                difference = sum(abs(x-y)*w for x, y, w in zip(
                    approx, values, masses
                ))
                assert difference <= Fraction(majorant, n)
                assert sum(x*w for x, w in zip(approx, masses)) == (
                    Fraction(n-1, n) * true_integral
                )
                count += 1
    assert count == 1800
    print(f"PASS R08 dominated convergence L1: {count} models")


def test_layer_cake_and_abs_integrability():
    count = 0
    for values in product((0, 1, 2, 4), repeat=2):
        for masses in product((0, 1, 3, math.inf), repeat=2):
            lhs = integrate_nonnegative(values, masses)
            # Layer-cake formula is a sum of the measures of {f>t}
            # over successive unit-length intervals.
            rhs = sum(
                integrate_nonnegative(
                    (int(a > t) for a in values), masses
                ) for t in range(4)
            )
            assert lhs == rhs
            count += 1
    assert count == 256
    print(f"PASS R08 layer cake with infinite masses: {count} models")


def test_source_structure():
    docs = [(BASE / name).read_text(encoding="utf-8") for name in FILES]
    source = docs[-1]
    labels = [m.group(1) for data in docs for m in
              re.finditer(r"\\label\{([^}]+)\}", data)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)]
    assert len(labels) == len(set(labels)), "duplicate label R01–R08"
    assert set(refs) <= set(labels), f"undefined reference {set(refs)-set(labels)}"
    environments = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
        if kind == "begin":
            environments.append(name)
        else:
            assert environments and environments.pop() == name, name
    assert not environments, environments
    forbidden = (
        "sekwencji", "unia zbiorów", "zbieżność zdominowana",
        "pierwszoprzeliczal", "drugoprzeliczal",
        r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}"
    )
    for phrase in forbidden:
        assert phrase not in source, phrase
    assert "\\emph{niepustą} rodziną" in source
    assert "M\\in[0,\\infty)" in source
    assert "na wspólnym mierzalnym zbiorze wyjątkowym" in source
    assert "\\lambda_1(O)<b-a" in source
    assert "Niech $(X,\\mathcal F,\\mu)$ będzie przestrzenią z miarą." in source
    print(f"PASS R08 source/terminology: {len(refs)} resolved references")


if __name__ == "__main__":
    test_monotone_convergence()
    test_fatou()
    test_dominated_convergence()
    test_layer_cake_and_abs_integrability()
    test_source_structure()
