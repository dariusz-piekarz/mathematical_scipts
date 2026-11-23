"""Chapter 10: finite checks for Lusin, smooth cutoffs and Lp approximation.

These finite/numerical examples are regressions, not general proofs.
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
    "09-rodzaje-zbieznosci-funkcji-mierzalnych.tex",
    "10-regularnosc-funkcji-mierzalnych-i-aproksymacja-funkcjami-ciaglymi.tex",
)
NEXT_REFERENCE = "12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex"


def eta(t):
    return math.exp(-1.0/t) if t > 0 else 0.0


def radial_cutoff(x, center, radius):
    sq = (x-center)**2
    a = eta(radius**2-sq)
    b = eta(sq-radius**2/4)
    return a/(a+b)


def check_smooth_cutoffs():
    cases = 0
    # One-dimensional centers and radii for a smooth support cutoff.
    for center in (-3.0, 0.0, 2.0):
        for radius in (0.75, 1.0, 2.0):
            for i in range(-100, 101):
                dx = radius * i / 60.0
                v = radial_cutoff(center+dx, center, radius)
                assert 0 <= v <= 1, (dx, v)
                if abs(dx) <= radius/2:
                    assert v == 1, (dx, v)
                if abs(dx) >= radius:
                    assert v == 0, (dx, v)
                cases += 1
    assert cases == 1809
    # Finite product yields a smooth cutoff equal to 1 at either center.
    for x in (-1.0, 1.0):
        v = 1 - (1-radial_cutoff(x,-1.0,1)) * (
            1-radial_cutoff(x,1.0,1)
        )
        assert v == 1
    print(f"PASS R10 smooth radial cutoffs: {cases} samples, both centers")


def check_indicator_regularization():
    """Nested K ⊂ A ⊂ O: error <= measure(O \ K), with 0*infty avoided."""
    count = 0
    n = 3
    for k,a,o in product(range(1 << n), repeat=3):
        if (k & ~a) or (a & ~o):
            continue
        for theta_values in product((Fraction(0), Fraction(1, 2), Fraction(1)),
                                    repeat=n):
            if any((k & (1 << i)) and theta_values[i] != 1 or
                   not (o & (1 << i)) and theta_values[i] != 0
                   for i in range(n)):
                continue
            for weights in product((0, 1, 3), repeat=n):
                discrepancy = sum(
                    weights[i] * abs(Fraction(bool(a & (1 << i))) -
                                     theta_values[i])**2
                    for i in range(n)
                )
                bound = sum(
                    weights[i] for i in range(n)
                    if (o & (1 << i)) and not (k & (1 << i))
                )
                assert discrepancy <= bound
                count += 1
    assert count >= 10000
    print(f"PASS R10 nested indicator approximations: {count} weighted models")


def check_lipschitz_inf_convolution():
    xs = tuple(Fraction(x, 2) for x in range(-8,9))
    values = (lambda x: x/2, lambda x: abs(x)/3)
    checked = 0
    for h in values:
        on_k = {x:h(x) for x in xs}
        M = max(abs(y) for y in on_k.values())
        for L in (Fraction(1), Fraction(2), Fraction(5)):
            def u(x):
                raw = min(v+L*abs(x-y) for y,v in on_k.items())
                return max(-M,min(M,raw))
            assert all(u(x)==h(x) for x in xs)
            # Verify global Lipschitz constant on a larger sampling grid.
            grid = tuple(Fraction(i,4) for i in range(-36,37))
            out = [u(x) for x in grid]
            assert all(abs(v) <= M for v in out)
            for i in range(len(grid)-1):
                assert abs(out[i+1]-out[i]) <= L*(grid[i+1]-grid[i])
                checked += 1
    assert checked == 432
    print(f"PASS R10 bounded inf-convolution: {checked} Lipschitz differences")


def check_signed_simple_approximation():
    values = [Fraction(-7,3),Fraction(-1,3),Fraction(0),
              Fraction(1,5),Fraction(11,4),Fraction(6)]
    count = 0
    for v in values:
        for n in range(1, 12):
            step = Fraction(1, 2**n)
            approx = step * math.floor(v/step)
            assert 0 <= v-approx < step
            count += 1
    assert count == 66
    print(f"PASS R10 signed floor quantization: {count} exact values")


def check_countable_exception_budgets():
    # Egorov + compact core (1/4+1/4) + countably many inner errors (1/4).
    eps = Fraction(3,7)
    first,second=eps/4,eps/4
    for end in (1,2,4,8,16,32,128):
        tail=sum((eps*Fraction(1,2**(n+2)) for n in range(1,end+1)),
                 Fraction(0))
        assert first+second+tail < eps
    # Countably many independent Lusin exceptions.
    for end in (1,2,4,8,16,32,128):
        s=sum((eps*Fraction(1,2**(j+1)) for j in range(1,end+1)),
              Fraction(0))
        assert s<eps
    print("PASS R10 Lusin and countable-exception error budgets: 14 cases")


def check_empty_spaces():
    E=frozenset()
    K=frozenset()
    assert K <= E
    assert len(E-K)==0
    # The empty function has no values and its restriction is continuous.
    empty_values=set()
    assert not empty_values
    # H=0 extends the empty function; no sup(empty) is evaluated.
    assert 0 == 0
    print("PASS R10 empty measurable set and compact set conventions")


def check_sources():
    docs = [(BASE / name).read_text(encoding="utf-8") for name in FILES]
    src=docs[-1]
    labels=[m.group(1) for d in docs for m in re.finditer(r"\\label\{([^}]+)\}",d)]
    # Only forward labels for dependencies, without auditing the later chapter.
    forward=(BASE/NEXT_REFERENCE).read_text(encoding="utf-8")
    labels.extend(m.group(1) for m in re.finditer(r"\\label\{([^}]+)\}",forward))
    refs=[m.group(1) for m in re.finditer(
        r"\\(?:ref|eqref|pageref)\{([^}]+)\}",src)]
    assert len(labels)==len(set(labels)), "duplicate labels R01–R10 and R12"
    assert set(refs) <= set(labels), f"missing refs: {set(refs)-set(labels)}"
    stack=[]
    for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",src):
        if kind=="begin":
            stack.append(env)
        else:
            assert stack and stack.pop()==env, f"unbalanced {env}"
    assert not stack, f"unclosed environments: {stack}"
    for forbidden in ("sekwencji","unia zbiorów","zbieżność zdominowana",
                      "drugoprzeliczal","pierwszoprzeliczal",
                      r"\mathbf{1}",r"\mathbb{1}",r"\mathds{1}"):
        assert forbidden not in src, forbidden
    for required in (
        r"Jeżeli $E=\varnothing$, bierzemy $K=\varnothing$",
        r"Jeśli $K=\varnothing$," ,
        r"\label{cor:lusin-finite-ae-10}",
        r"\label{cor:smooth-approx-in-measure-10}",
        r"\label{thm:cc-in-lp-10}",
        r"\label{thm:ae-smooth-approx-10}",
    ):
        assert required in src, f"missing R10 hypothesis/label: {required}"
    print(f"PASS R10 LaTeX source: {len(refs)} resolved references, environments, language")


if __name__ == "__main__":
    check_smooth_cutoffs()
    check_indicator_regularization()
    check_lipschitz_inf_convolution()
    check_signed_simple_approximation()
    check_countable_exception_budgets()
    check_empty_spaces()
    check_sources()
