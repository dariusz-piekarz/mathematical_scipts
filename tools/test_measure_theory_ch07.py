"""Regression checks for chapter 07 (Lebesgue integral construction).

Finite atomic models are diagnostics, not substitutes for general proofs.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import math
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters/pl/measure_theory"
NAMES = (
    "01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex",
    "02-miary-i-ich-podstawowe-wlasnosci.tex",
    "03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex",
    "04-miara-lebesguea-na-przestrzeni-euklidesowej.tex",
    "05-struktura-przestrzeni-mierzalnych.tex",
    "06-funkcje-mierzalne-i-ich-aproksymacja.tex",
    "07-konstrukcja-calki-lebesguea.tex",
)


def term(a, weight):
    """Product in [0,infinity], with 0 * infinity = 0."""
    return 0 if a == 0 or weight == 0 else a * weight


def integral(values, weights):
    return sum(term(a, w) for a, w in zip(values, weights))


def check_simple_properties():
    count = 0
    for weights in product((0, 1, math.inf), repeat=3):
        for s in product((0, 1, 2), repeat=3):
            value = integral(s, weights)
            # Canonical level-set formula versus atom refinement.
            levels = set(s)
            canonical = sum(
                term(level, sum(weights[i] for i in range(3) if s[i] == level))
                for level in levels
            )
            assert value == canonical
            for c in (0, 1, 3):
                assert integral([c * v for v in s], weights) == term(c, value)
            for t in product((0, 1, 2), repeat=3):
                other = integral(t, weights)
                assert integral([a + b for a, b in zip(s, t)], weights) == value + other
                if all(a <= b for a, b in zip(s, t)):
                    assert value <= other
                count += 1
    assert count == 19683
    print(f"PASS R07 atomic simple integrals and additivity: {count} finite triples")


def check_discrete_infinity():
    count = 0
    levels = (0, 2, math.inf)
    weights = (0, 1, math.inf)
    for f in product(levels, repeat=3):
        for w in product(weights, repeat=3):
            true_integral = integral(f, w)
            truncated = []
            for M in (1, 2, 3, 5, 10, 100):
                fn = [min(value, M) for value in f]
                approximation = integral(fn, w)
                assert approximation <= true_integral
                truncated.append(approximation)
            assert all(a <= b for a, b in zip(truncated, truncated[1:]))
            # For a finite integral the truncation is already exact at M=2.
            if math.isfinite(true_integral):
                assert truncated[1] == true_integral
            # f(n)=infinity and w_n>0 forces the integral to infinity.
            if any(a == math.inf and weight > 0 for a, weight in zip(f, w)):
                assert true_integral == math.inf
            count += 1
    assert count == 729
    print(f"PASS R07 discrete truncated minorants incl infinity: {count} cases")


def check_disjoint_partition():
    """Closed boundaries at -1,+1 belong to exactly one indicated interval."""
    count = 0
    for j in range(-80, 81):
        x = Fraction(j, 8)
        central = int(-1 < x < 1)
        right = sum(
            int(n <= x < n + 1) for n in range(1, 12)
        )
        left = sum(
            int(-n - 1 < x <= -n) for n in range(1, 12)
        )
        assert central + right + left == 1, (x, central, right, left)
        count += 1
    assert count == 161
    print(f"PASS R07 real-line partition: {count} dyadic/rational endpoints")


def check_divergence():
    for n in range(1, 35):
        terms = [Fraction(2**j, 2**(j+1)) for j in range(n)]
        assert sum(terms) == Fraction(n, 2)
    print("PASS R07 1/x divergent minorants: 34 exact partial sums")


def check_sources():
    files = [(BASE / name).read_text(encoding="utf8") for name in NAMES]
    source = files[-1]
    labels = [m.group(1) for f in files
              for m in re.finditer(r"\\label\{([^}]+)\}", f)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)]
    assert len(labels) == len(set(labels)), "duplicate labels R01-R07"
    assert set(refs).issubset(set(labels)), f"missing refs: {set(refs)-set(labels)}"
    stack = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
        if kind == "begin":
            stack.append(name)
        else:
            assert stack and stack.pop() == name, f"bad environment {name}"
    assert not stack, f"unclosed environments: {stack}"
    for forbidden in (
        "sekwencji", "drugoprzeliczal", "zbieżność zdominowana",
        "unia zbiorów", r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}"
    ):
        assert forbidden not in source, f"terminology: {forbidden}"
    assert "lista wartości jest pusta" in source
    assert "s_{N,M}(n)=" in source
    assert "parami rozłączne przedziały\n$(-1,1)$" in source
    print(f"PASS R07 TeX source and {len(refs)} cross-references")


if __name__ == "__main__":
    check_simple_properties()
    check_discrete_infinity()
    check_disjoint_partition()
    check_divergence()
    check_sources()
