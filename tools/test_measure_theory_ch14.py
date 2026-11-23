"""Chapter 14: finite regression tests for Lp inequalities and source integrity.

These atomic models are diagnostics, not proofs of the general theorems.
"""
from fractions import Fraction as Q
from itertools import product
from math import inf, isclose, sqrt
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1] / "chapters/pl/measure_theory"
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
    "11-calki-zalezne-od-parametru.tex",
    "12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex",
    "13-zamiana-zmiennych-w-calce-lebesguea.tex",
    "14-przestrzenie-lp-i-ich-podstawowe-wlasnosci.tex",
)


def norm(vec, mass, p):
    if p == inf:
        return max((abs(x) for x, w in zip(vec, mass) if w > 0), default=0)
    return sum(w * abs(x)**p for x, w in zip(vec, mass)) ** (1/p)


def le(a, b):
    return a <= b + 1e-10 * max(1, abs(a), abs(b))


def check_young():
    count=0
    for a,b in product((Q(0),Q(1,4),Q(1),Q(3),Q(8)),repeat=2):
        for p,q in ((2.,2.),(3.,1.5),(4.,4/3)):
            left=float(a*b)
            right=float(a)**p/p+float(b)**q/q
            assert le(left,right), (a,b,p,q)
            count+=1
    assert count==75
    print(f"PASS R14 Young with boundary 0: {count} inequalities")


def check_holder_and_minkowski():
    count=0
    values=list(product((-1,0,1,2),repeat=2))
    for mass in product((0,1,4),repeat=2):
        for f,g in product(values,repeat=2):
            left=sum(w*abs(a*b) for a,b,w in zip(f,g,mass))
            assert le(left,norm(f,mass,2)*norm(g,mass,2))
            assert le(left,norm(f,mass,1)*norm(g,mass,inf))
            for p in (1,2,3,inf):
                h=tuple(a+b for a,b in zip(f,g))
                assert le(norm(h,mass,p),norm(f,mass,p)+norm(g,mass,p))
            count+=1
    assert count==2304
    print(f"PASS R14 Holder/Minkowski incl. zero masses and Linf: {count} pairs")


def check_jensen_and_embeddings():
    count=0
    for masses in product((0,1,3),repeat=3):
        total=sum(masses)
        if total==0:
            continue
        for vals in product((-2,-1,0,1,3),repeat=3):
            mean=Q(sum(w*x for x,w in zip(vals,masses)),total)
            mean_square=Q(sum(w*x*x for x,w in zip(vals,masses)),total)
            assert mean**2 <= mean_square
            n1=norm(vals,masses,1)
            n2=norm(vals,masses,2)
            ninf=norm(vals,masses,inf)
            assert le(n1,sqrt(total)*n2)
            assert le(n2,sqrt(total)*ninf)
            assert le(n2,sqrt(n1*ninf))
            count+=1
    assert count==3250
    print(f"PASS R14 Jensen, finite embeddings, L1-L2-Linf interpolation: {count}")


def check_simple_approximation():
    count=0
    vals=[Q(-11,4),Q(-1,3),Q(0),Q(2,5),Q(9,2)]
    for v in vals:
        for m in (2,3,7,17,41):
            # The floor approximation treats negative and positive values alike.
            scaled=v*m
            approx=Q(scaled.numerator//scaled.denominator,m)
            assert 0 <= v-approx < Q(1,m)
            count+=1
    assert count==25
    print(f"PASS R14 signed simple quantization: {count}")


def check_lp_series_and_translations():
    count=0
    for masses in product((0,1,3),repeat=3):
        vector=(Q(1),Q(-2),Q(3))
        for terms in (1,2,4,8,12):
            # u_n=2^(-n) vector. Triangle estimate for finite and infinite tails.
            finite=sum((Q(1,2**n) for n in range(1,terms+1)),Q(0))
            rest=Q(1,2**terms)
            for p in (1,2,inf):
                assert le(norm(tuple(float(finite*x) for x in vector),masses,p),
                          float(finite)*norm(vector,masses,p))
                assert le(float(rest)*norm(vector,masses,p),
                          sum(2**(-n)*norm(vector,masses,p) for n in range(terms+1,terms+81))
                          + 1e-10)
                count+=1
    assert count==405
    print(f"PASS R14 Lp series and tails: {count}")


def check_structure():
    docs=[(BASE/n).read_text(encoding="utf-8") for n in FILES]
    src=docs[-1]
    labels=[m.group(1) for d in docs for m in re.finditer(r"\\label\{([^}]+)\}", d)]
    refs=[m.group(1) for m in re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",src)]
    assert len(labels)==len(set(labels)), "duplicate R01-R14 labels"
    assert set(refs)<=set(labels), f"missing refs: {set(refs)-set(labels)}"
    stack=[]
    for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",src):
        if kind=="begin":
            stack.append(env)
        else:
            assert stack and stack.pop()==env, f"mismatched {env}"
    assert not stack, stack
    for term in ("unia zbiorów","zbieżność zdominowana","indykator",
                 r"\mathbf{1}",r"\mathbb{1}",r"\mathds{1}"):
        assert term not in src, term
    assert not re.search(r"\bsekwencj\w*",src)
    for label in ("thm:holder-14","thm:minkowski-14","thm:series-lp-14",
                  "thm:riesz-fischer-14","thm:jensen-14",
                  "thm:simple-dense-lp-14","thm:separable-lp-14",
                  "thm:lp-interpolation-14"):
        assert rf"\label{{{label}}}" in src, label
    assert "części dodatniej i ujemnej" in src
    print(f"PASS R14 crossrefs and source structure: {len(refs)} crossrefs")


if __name__=="__main__":
    check_young()
    check_holder_and_minkowski()
    check_jensen_and_embeddings()
    check_simple_approximation()
    check_lp_series_and_translations()
    check_structure()
