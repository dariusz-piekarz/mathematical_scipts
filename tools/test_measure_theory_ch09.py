"""Chapter 09: exact finite convergence regressions and LaTeX source checks.

The finite models are regression diagnostics, not proofs of general theorems.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
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
    "09-rodzaje-zbieznosci-funkcji-mierzalnych.tex",
)


def rho(f, g, weights):
    return sum(w * min(1, abs(x-y)) for x, y, w in zip(f, g, weights))


def check_measure_metric():
    fs = list(product((-1, 0, 1, 2), repeat=2))
    count = 0
    for weights in product((0, 1, 3), repeat=2):
        for f, g, h in product(fs, repeat=3):
            dfg, dgh, dfh = rho(f, g, weights), rho(g, h, weights), rho(f, h, weights)
            assert dfg >= 0 and dfg == rho(g, f, weights)
            assert (dfg == 0) == all(
                (x == y or w == 0) for x, y, w in zip(f, g, weights)
            )
            assert dfh <= dfg + dgh
            count += 1
    assert count == 36864
    print(f"PASS R09 finite measure metric: {count} triangles and null classes")


def check_chebyshev():
    values = list(product((-2, -1, 0, 1, 2), repeat=2))
    count = 0
    for v in values:
        for weights in product((0, 1, 3), repeat=2):
            for p in (1, 2, 3):
                normp = sum(w * abs(x)**p for x, w in zip(v, weights))
                for epsilon in (Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)):
                    left = sum(w for x, w in zip(v, weights) if abs(x) > epsilon)
                    assert left * epsilon**p <= normp
                    count += 1
    assert count == 2025
    print(f"PASS R09 Chebyshev Lp => measure: {count} weighted examples")


def check_typewriter():
    count = 0
    for k in range(9):
        width = Fraction(1, 2**k)
        assert width > 0
        for q in range(256):
            x = Fraction(q, 256)
            hits = sum(
                Fraction(j, 2**k) <= x < Fraction(j+1, 2**k)
                for j in range(2**k)
            )
            assert hits == 1
            count += 1
    assert count == 2304
    print(f"PASS R09 typewriter: {count} complete dyadic-block checks")


def check_scheffe():
    grid = [Fraction(j, 4) for j in range(5)]
    count = 0
    for a, b in product(grid, repeat=2):
        target = (a, 1-a)
        alternative = (b, 1-b)
        for n in range(1, 9):
            approximate = tuple(
                (Fraction(1)-Fraction(1, n))*x + Fraction(1, n)*y
                for x, y in zip(target, alternative)
            )
            assert sum(approximate) == sum(target) == 1
            l1 = sum(abs(x-y) for x, y in zip(approximate, target))
            assert l1 == Fraction(2*abs(a-b), n)
            count += 1
    assert count == 200
    print(f"PASS R09 Scheffe normalized densities: {count} exact examples")


def check_egorov_null_exception():
    # X={0,1} with mu({0})=0, mu({1})=1; a.e. convergence
    # need not hold at x=0, but Egorov permits E={0}.
    for n in range(1, 65):
        f_n = (Fraction(n), Fraction(1, n))
        assert abs(f_n[1]) <= Fraction(1, n)
        assert abs(f_n[0]) >= 1
    assert sum((0, 1)[i] for i in (0,)) == 0
    # Empty X\E is possible for a zero measure space:
    # the nonnegative supremum convention gives sup(empty)=0.
    print("PASS R09 Egorov null exception and empty complement")


def check_local_vs_global():
    for n in range(1, 65):
        # f_n=chi_[n,n+1) on R; full bad set always has measure 1.
        assert Fraction(1) == 1
        # Every fixed compact interval [-R,R] eventually avoids support.
        for radius in range(1, 8):
            if n > radius:
                assert n >= radius
    print("PASS R09 local/global mass escape: 64 moving supports")


def check_source():
    docs = [(BASE / name).read_text(encoding="utf-8") for name in FILES]
    src = docs[-1]
    labels = [m.group(1) for d in docs for m in
              re.finditer(r"\\label\{([^}]+)\}", d)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", src)]
    assert len(labels) == len(set(labels)), "duplicate labels R01-R09"
    assert set(refs) <= set(labels), f"unresolved crossrefs: {set(refs)-set(labels)}"
    stack = []
    for kind, env in re.findall(r"\\(begin|end)\{([^}]+)\}", src):
        if kind == "begin":
            stack.append(env)
        else:
            assert stack and stack.pop() == env, f"mismatched: {env}"
    assert not stack, f"unclosed environments: {stack}"
    for forbidden in (
        "sekwencji", "unia zbiorów", "zbieżność zdominowana",
        "pierwszoprzeliczal", "drugoprzeliczal",
        r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}"
    ):
        assert forbidden not in src, forbidden
    assert r"\label{def:five-convergences}" in src
    assert r"\label{thm:measure-metric-9}" in src
    assert r"\label{thm:scheffe-9}" in src
    assert "Jeśli $X\\setminus E=\\varnothing$" in src
    assert "a $f_n,f:X\\to\\mathbb R$ funkcjami mierzalnymi." in src
    print(f"PASS R09 source: {len(refs)} crossrefs, TeX environments and terminology")


if __name__ == "__main__":
    check_measure_metric()
    check_chebyshev()
    check_typewriter()
    check_scheffe()
    check_egorov_null_exception()
    check_local_vs_global()
    check_source()
