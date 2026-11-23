"""Measure theory R06: finite exact regressions and source consistency checks.

Finite regressions are independent diagnostics, not proofs of general claims.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import math
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters/pl/measure_theory"
NAMES = (
    "01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex",
    "02-miary-i-ich-podstawowe-wlasnosci.tex",
    "03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex",
    "04-miara-lebesguea-na-przestrzeni-euklidesowej.tex",
    "05-struktura-przestrzeni-mierzalnych.tex",
    "06-funkcje-mierzalne-i-ich-aproksymacja.tex",
)


def quantize_nonnegative(value, n):
    truncated = n if value == math.inf else min(value, n)
    return Fraction(math.floor(truncated * (2**n)), 2**n)


def check_simple_approximation():
    values = [Fraction(0), Fraction(1, 3), Fraction(1, 2),
              Fraction(2, 3), Fraction(5, 2), Fraction(24), math.inf]
    checks = 0
    for v in values:
        previous = Fraction(0)
        for n in range(1, 13):
            s = quantize_nonnegative(v, n)
            assert 0 <= previous <= s <= v
            if v != math.inf and n > v:
                assert Fraction(0) <= v-s < Fraction(1, 2**n)
            if v == math.inf:
                assert s == n
            previous = s
            checks += 1
    assert checks == 84
    print(f"PASS R06 canonical simple approximation: {checks} exact stages")


def check_signed_quantization():
    vals = [Fraction(-5, 2), Fraction(-1, 3), Fraction(-1, 4),
            Fraction(0), Fraction(1, 3), Fraction(2), Fraction(7, 4)]
    checks = 0
    for v in vals:
        for n in range(1, 13):
            s = Fraction(math.floor(v * 2**n), 2**n)
            assert 0 <= v-s < Fraction(1, 2**n)
            checks += 1
    assert checks == 84
    print(f"PASS R06 signed simple approximation: {checks} exact stages")


def check_extended_halfline_tests():
    vals = (-math.inf, Fraction(-2), Fraction(0),
            Fraction(1, 2), math.inf)
    cuts = (-3, -1, Fraction(1, 4), 1, 2)
    checked = 0
    for triple in product(vals, repeat=3):
        signatures = [
            tuple(v < q for q in cuts) for v in triple
        ]
        # Every distinct extended-real value is separated by one rational
        # cut. Therefore all its fibers lie in the generated sigma algebra.
        for i in range(3):
            for j in range(3):
                assert (triple[i] == triple[j]) == (signatures[i] == signatures[j])
                checked += 1
    assert checked == 1125
    print(f"PASS R06 rational half-line generators: {checked} finite comparisons")


def check_typewriter():
    checked = 0
    for level in range(1, 9):
        width = Fraction(1, 2**level)
        for m in range(256):
            x = Fraction(m, 256)
            active = sum(
                Fraction(j, 2**level) <= x < Fraction(j+1, 2**level)
                for j in range(2**level)
            )
            assert active == 1
            checked += 1
        assert width == Fraction(1, 2**level)
    assert checked == 2048
    print(f"PASS R06 typewriter moving supports: {checked} dyadic checks")


def check_incomplete_measure_counterexample():
    x = frozenset((0, 1, 2))
    sigma = {frozenset(), frozenset((0, 1)), frozenset((2,)), x}
    null_set = frozenset((0, 1))
    nonmeasurable = frozenset((0,))
    assert null_set in sigma and nonmeasurable not in sigma
    # mu(B)=1 iff 2 belongs to B; mu(null_set)=0.
    mu = lambda b: int(2 in b)
    assert mu(null_set) == 0 and mu(x) == 1
    # f=0 and g=chi_{0}; their difference is contained in null_set.
    f_preimage_one, g_preimage_one = frozenset(), nonmeasurable
    assert f_preimage_one in sigma and g_preimage_one not in sigma
    print("PASS R06 noncomplete null-set modification: 1 concrete counterexample")


def check_source():
    docs = [(CHAPTERS / name).read_text(encoding="utf-8") for name in NAMES]
    source = docs[-1]
    labels = [m.group(1) for doc in docs
              for m in re.finditer(r"\\label\{([^}]+)\}", doc)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)]
    assert len(labels) == len(set(labels)), "duplicate labels R01-R06"
    assert set(refs) <= set(labels), f"unresolved source refs: {set(refs)-set(labels)}"
    stack = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
        if kind == "begin":
            stack.append(name)
        else:
            assert stack and stack.pop() == name, f"unbalanced environment {name}"
    assert not stack, f"unclosed environments {stack}"
    forbidden = ("drugoprzeliczal", "pierwszoprzeliczal", "unia zbiorów",
                 "zbieżność zdominowana", r"\mathbf{1}", r"\mathbb{1}",
                 r"\mathds{1}")
    assert all(x not in source for x in forbidden)
    assert "Niech $(X,\\mathcal F,\\mu)$ będzie przestrzenią z miarą,\na $(f_n)_{n\\ge1}$" in source
    assert "na mocy twierdzenia\n\\ref{thm:composition-measurable}" in source
    assert "Niech $(X,\\mathcal F)$ będzie przestrzenią mierzalną.\nJeżeli $(f_n)_{n\\ge1}$" in source
    print(f"PASS R06 source: {len(refs)} refs, TeX environments, terminology")


if __name__ == "__main__":
    check_simple_approximation()
    check_signed_quantization()
    check_extended_halfline_tests()
    check_typewriter()
    check_incomplete_measure_counterexample()
    check_source()
