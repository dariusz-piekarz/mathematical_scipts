"""Chapter 15: geometric Lp, duality and weak-convergence regressions.

Checks finite examples and LaTeX integrity. They do not prove functional
analytic assertions for arbitrary measure spaces.
"""
import cmath
import math
import re
from fractions import Fraction
from itertools import product
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "chapters/pl/measure_theory"
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
    "13-zamiana-zmiennych-w-calce-lebesguea.tex",
    "14-przestrzenie-lp-i-ich-podstawowe-wlasnosci.tex",
    "15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex",
)


def lp(x, weights, p):
    return sum(w * abs(z)**p for z, w in zip(x, weights))**(1/p)


def approx_le(a, b):
    return a <= b + 5e-11 * max(1, abs(a), abs(b))


def midpoint_inequalities():
    # Deterministic complex-valued two-atom models; zero weights included.
    complex_values = [complex(re, im) for re, im in
                      product((-1, 0, 1), repeat=2)]
    vectors = list(product(complex_values, repeat=2))
    count = 0
    for weights in product((0, 1, 3), repeat=2):
        for p in (1.25, 1.5, 1.9, 2, 3, 5):
            for f in vectors:
                # Distinct second vector from cyclic shifts: 4,374 checks.
                for shift in (0, 7, 19, 43):
                    h = vectors[(vectors.index(f)+shift) % len(vectors)]
                    m = tuple((a+b)/2 for a, b in zip(f, h))
                    v = tuple((a-b)/2 for a, b in zip(f, h))
                    a, b = lp(f, weights, p), lp(h, weights, p)
                    nm, nv = lp(m, weights, p), lp(v, weights, p)
                    if p >= 2:
                        assert approx_le(nm**p+nv**p, (a**p+b**p)/2)
                    elif a+b > 0:
                        lower = p*(p-1)/2 * nv**2 / (a+b)**(2-p)
                        assert approx_le(lower, (a**p+b**p)/2-nm**p)
                    else:
                        assert nm == nv == 0
                    count += 1
    assert count == 17496, count
    print(f"PASS R15 midpoint Clarkson inequalities: {count} complex atomic models")


def dual_norming_and_energy():
    count = 0
    for weights in product((0, 1, 4), repeat=2):
        for g in product((complex(0), complex(1), complex(-1),
                          complex(0,1), complex(1,1)), repeat=2):
            for p in (1.5, 2, 3, 4):
                q = p/(p-1)
                gnorm = lp(g, weights, q)
                if not gnorm:
                    continue
                f = tuple((z.conjugate()*abs(z)**(q-2)
                           if z else complex(0)) for z in g)
                fnorm = lp(f, weights, p)
                functional = sum(w*a*z for w,a,z in zip(weights,f,g))
                assert abs(functional.imag) < 1e-10
                assert abs(functional.real-gnorm**q) < 1e-9
                assert abs(fnorm-gnorm**(q-1)) < 1e-9
                # Explicit minimizer of alpha ||f||^p / p - Re int(fg).
                for alpha in (0.5, 1, 3):
                    minimizer = tuple(alpha**(-1/(p-1))*z for z in f)
                    def energy(v):
                        return alpha*lp(v, weights, p)**p/p - sum(
                            w*(a*b).real for a,b,w in zip(v,g,weights))
                    opt = energy(minimizer)
                    for delta in (-.5, 0, .5):
                        z = tuple(v+delta*(1+1j) for v in minimizer)
                        assert approx_le(opt, energy(z))
                        count += 1
    assert count > 4500
    print(f"PASS R15 norming functional and strict convex energy: {count} tests")


def dual_l1_atomic():
    count = 0
    for masses in product((0, 1, 3), repeat=3):
        for g in product((-2, -1, 0, 1, 3), repeat=3):
            M = max((abs(z) for z, w in zip(g,masses) if w > 0),
                    default=0)
            for i, w in enumerate(masses):
                if w == 0: continue
                f = [0]*3
                f[i] = 1/w if g[i] >= 0 else -1/w
                assert sum(abs(a)*b for a,b in zip(f,masses)) == 1
                integral = sum(a*b*c for a,b,c in zip(f,g,masses))
                assert abs(integral) <= M
                count += 1
    assert count > 7000
    print(f"PASS R15 finite-atom L1 dual bound: {count} tests")


def weak_rademacher_dyadic():
    count=0
    for n in range(2,10):
        values=[1 if k%2 == 0 else -1 for k in range(2**(n+1))]
        for m in range(0,n):
            # Integral of r_n over every dyadic interval of rank m is 0.
            span=2**(n+1-m)
            for interval in range(2**m):
                partial=sum(values[interval*span:(interval+1)*span])
                assert partial == 0
                count += 1
    assert count > 3000
    print(f"PASS R15 Rademacher weak cancellation: {count} dyadic intervals")


def structure():
    docs=[(BASE/n).read_text(encoding="utf-8") for n in NAMES]
    src=docs[-1]
    labels=[m.group(1) for d in docs for m in re.finditer(r"\\label\{([^}]+)\}",d)]
    refs=[m.group(1) for m in re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",src)]
    assert len(labels)==len(set(labels)), "duplicate labels R01-R15"
    assert set(refs)<=set(labels), f"unresolved references {set(refs)-set(labels)}"
    stack=[]
    for action,env in re.findall(r"\\(begin|end)\{([^}]+)\}",src):
        if action=="begin":stack.append(env)
        else:assert stack and stack.pop()==env, f"unmatched {env}"
    assert not stack, f"open environments {stack}"
    assert not re.search(r"\bsekwencj\w*",src)
    for forbidden in ("unia zbiorów","zbieżność zdominowana","indykator",
                      r"\mathbf{1}",r"\mathbb{1}",r"\mathds{1}"):
        assert forbidden not in src, forbidden
    required=(
        r"\label{thm:dual-lp-15}",r"\label{thm:dual-l1-15}",
        r"\label{thm:reflexive-lp-15}",r"\label{thm:uniform-convexity-15}",
        r"\label{thm:weak-subseq-15}",r"\label{lem:midpoint-lp-15}",
        r"\label{cor:holder-sharp-15}",
        r"stałe na",r"przedziałach dyadycznych",
    )
    for needle in required:assert needle in src, needle
    assert src.count(r"\begin{proof}") == 12
    print(f"PASS R15 LaTeX structure: {len(refs)} refs and 12 proofs")


if __name__ == "__main__":
    midpoint_inequalities()
    dual_norming_and_energy()
    dual_l1_atomic()
    weak_rademacher_dyadic()
    structure()
