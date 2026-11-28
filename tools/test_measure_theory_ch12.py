"""Chapter 12: exact regressions for product measures, Tonelli and Fubini.

All finite tests are diagnostics and do not prove general measure theorems.
"""
from fractions import Fraction as Q
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
    "08-twierdzenia-graniczne-dla-calki-lebesguea.tex",
    "09-rodzaje-zbieznosci-funkcji-mierzalnych.tex",
    "10-regularnosc-funkcji-mierzalnych-i-aproksymacja-funkcjami-ciaglymi.tex",
    "11-calki-zalezne-od-parametru.tex",
    "12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex",
)


def nonnegative_product(a, b):
    if a == 0 or b == 0:
        return 0
    return a * b


def nonnegative_integral(values, weights):
    return sum(nonnegative_product(a, w) for a, w in zip(values, weights))


def tonelli(arr, mu, nu):
    direct = sum(
        nonnegative_product(arr[i][j],
                            nonnegative_product(mu[i], nu[j]))
        for i in range(2) for j in range(2)
    )
    first_y = nonnegative_integral(
        [nonnegative_integral(arr[i], nu) for i in range(2)], mu
    )
    first_x = nonnegative_integral([
        nonnegative_integral([arr[i][j] for i in range(2)], mu)
        for j in range(2)
    ], nu)
    return direct, first_y, first_x


def test_tonelli_including_infinity():
    count = 0
    for vals in product((0, 1, 3, math.inf), repeat=4):
        arr = (vals[:2], vals[2:])
        for weights in product((0, 2, math.inf), repeat=4):
            mu, nu = weights[:2], weights[2:]
            direct, horizontal, vertical = tonelli(arr, mu, nu)
            assert direct == horizontal == vertical, (
                arr, mu, nu, direct, horizontal, vertical
            )
            count += 1
    assert count == 20736
    print(f"PASS R12 Tonelli including 0*infinity and infinity: {count} models")


def test_fubini_signed():
    count = 0
    for vals in product((-2, -1, 0, 1, 2), repeat=4):
        arr = (vals[:2], vals[2:])
        for weights in product((0, 1, 3), repeat=4):
            mu, nu = weights[:2], weights[2:]
            direct = sum(arr[i][j] * mu[i] * nu[j]
                         for i in range(2) for j in range(2))
            horizontal = sum(mu[i] * sum(arr[i][j] * nu[j]
                                        for j in range(2))
                             for i in range(2))
            vertical = sum(nu[j] * sum(arr[i][j] * mu[i]
                                      for i in range(2))
                           for j in range(2))
            bound = sum(abs(arr[i][j]) * mu[i] * nu[j]
                        for i in range(2) for j in range(2))
            assert direct == horizontal == vertical
            assert abs(direct) <= bound
            count += 1
    assert count == 50625
    print(f"PASS R12 signed Fubini on finite products: {count} models")


def test_nonabsolute_counterexample():
    for k in range(1, 61):
        a = lambda m, n: int(n == m) - int(n == m+1)
        # Finite k-by-k square has total 1, whereas
        # summing each infinite row before summing rows gives 0.
        square = sum(a(m, n) for m in range(1, k+1)
                     for n in range(1, k+1))
        assert square == 1
        assert all(a(m, m) + a(m, m+1) == 0
                   for m in range(1, k+1))
        assert sum(a(m, 1) for m in range(1, k+1)) == 1
        for n in range(2, k+1):
            assert sum(a(m, n) for m in range(1, k+1)) == 0
    print("PASS R12 nonabsolute Fubini counterexample: 60 finite cutoffs")


def test_product_rectangles():
    endpoints = (Q(-2), Q(-1), Q(0), Q(1, 2), Q(1), Q(3))
    intervals = [(a, b) for a in endpoints for b in endpoints if a < b]
    count = 0
    for a, b in intervals:
        for c, d in intervals:
            # Two-dimensional rectangle area equals product of lengths,
            # regardless of which coordinate is integrated first.
            x_len, y_len = b-a, d-c
            area = x_len*y_len
            assert area == y_len*x_len
            assert area >= 0
            count += 1
    assert count == 225
    print(f"PASS R12 rational Lebesgue rectangles: {count} exact areas")


def test_null_sections():
    # A product-null set may have a non-null exceptional section.
    # mu({0})=0, mu({1})=1; nu({0})=2, nu({1})=3.
    mu, nu = (0, 1), (2, 3)
    arr = ((1, 1), (0, 0))
    direct, _, _ = tonelli(arr, mu, nu)
    assert direct == 0
    assert nonnegative_integral(arr[0], nu) == 5
    assert nonnegative_integral(arr[1], nu) == 0
    print("PASS R12 product-null exceptional section, 0*infinity semantics")


def test_source_structure():
    docs = [(BASE / name).read_text(encoding="utf-8") for name in NAMES]
    src = docs[-1]
    labels = [m.group(1) for d in docs
              for m in re.finditer(r"\\label\{([^}]+)\}", d)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", src)]
    assert len(labels) == len(set(labels)), "duplicate R01-R12 labels"
    assert set(refs) <= set(labels), f"unresolved R12 refs: {set(refs)-set(labels)}"
    stack = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", src):
        if kind == "begin":
            stack.append(name)
        else:
            assert stack and stack.pop() == name, f"unmatched {name}"
    assert not stack, f"open environments: {stack}"
    for disallowed in (
        "unia zbiorów", "zbieżność zdominowana", "indykator",
        r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}"
    ):
        assert disallowed not in src, f"forbidden terminology: {disallowed}"
    assert not re.search(r"\bsekwencj\w*", src)
    for required in (
        r"\label{thm:product-measure-12}",
        r"\label{thm:tonelli-12}",
        r"\label{thm:fubini-12}",
        r"\label{thm:completed-product-fubini-12}",
        r"\label{cor:null-sections-12}",
        r"\label{cor:practical-fubini-12}",
        "Niezależność dwóch elementów losowych",
        "Niech $(X,\\mathcal F,\\mu)$ i $(Y,\\mathcal G,\\nu)$",
    ):
        assert required in src, f"missing R12 element: {required}"
    print(f"PASS R12 LaTeX, terminology and {len(refs)} cross references")


if __name__ == "__main__":
    test_tonelli_including_infinity()
    test_fubini_signed()
    test_nonabsolute_counterexample()
    test_product_rectangles()
    test_null_sections()
    test_source_structure()
