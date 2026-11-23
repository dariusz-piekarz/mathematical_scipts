"""Chapter 11: exact finite parameter-integral and source regressions.

Finite atomic tests validate examples and edge cases, not the general theorems.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import cmath
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


def integrate(vals, masses):
    return sum((a*w for a, w in zip(vals, masses)), Q(0))


def test_uniform_parameter():
    count = 0
    masses = (Q(0), Q(1), Q(3))
    for t in (Q(-2), Q(-1), Q(0), Q(1), Q(2)):
        for n in range(1, 26):
            base = [Q(i+1) + t*Q(i-2) for i in range(3)]
            new = [b + Q((i+1), n)*t for i, b in enumerate(base)]
            h = [Q(2*(i+1), n) for i in range(3)]
            actual = abs(integrate(new, masses)-integrate(base, masses))
            assert actual <= integrate(h, masses)
            count += 1
    assert count == 125
    print(f"PASS R11 uniform parameter majorants: {count} exact tests")


def test_differentiation():
    count = 0
    for masses in product((Q(0), Q(1), Q(3)), repeat=3):
        for t in (Q(-1), Q(0), Q(2)):
            coefficients = [(Q(i), Q(i+1), Q(i-2)) for i in range(3)]
            value = lambda x: integrate(
                [a+b*x+c*x*x for a,b,c in coefficients], masses
            )
            exact = integrate(
                [b+2*c*t for a,b,c in coefficients], masses
            )
            for n in (5,10,25,50):
                h = Q(1,n)
                secant = (value(t+h)-value(t))/h
                quadratic_error = h*integrate([c for _,_,c in coefficients],masses)
                assert secant-exact == quadratic_error
                count += 1
    assert count == 324
    print(f"PASS R11 differentiating atomic integrals: {count} exact quotients")


def test_moving_domains():
    count = 0
    xs = (Q(0),Q(1),Q(2),Q(3))
    masses = (Q(0),Q(1),Q(2),Q(3))
    for t0 in (Q(1,2),Q(3,2),Q(5,2)):
        base = integrate([Q(i+1) if x<t0 else Q(0)
                          for i,x in enumerate(xs)],masses)
        for n in range(2,55):
            for sign in (-1,1):
                t=t0+Q(sign,4*n)
                moving = integrate([Q(i+1) if x<t else Q(0)
                                    for i,x in enumerate(xs)],masses)
                assert moving == base
                count += 1
    assert count == 318
    print(f"PASS R11 locally fixed moving domains: {count} exact checks")


def test_uniform_tails():
    count=0
    for N in range(1,21):
        bound=Q(1,2**N)
        for t in (Q(-2),Q(-1),Q(0),Q(1),Q(2)):
            tail=sum((abs(t)*Q(1,2**n) for n in range(N+1,65)),Q(0))
            assert tail <= 2*bound
            if abs(t)<=1:
                assert tail<=bound
            count+=1
    assert count==100
    print(f"PASS R11 uniform geometric tails: {count} tests")


def test_laplace():
    count=0
    for t in (Q(1,2),Q(1),Q(2),Q(3)):
        previous = None
        for denominator in (10,20,40,80,160):
            h=1/denominator
            approx=h/math.expm1(float(t)*h)  # right-endpoint sum of exp(-tx)
            exact=1/float(t)
            assert 0 < exact-approx < h, (t,denominator,approx)
            if previous is not None:
                assert approx > previous
            previous=approx
            count+=1
    assert count==20
    for z in (complex(1,1),complex(2,-.5),complex(.75,.25)):
        # Exact Laplace integral for h(x)=e^{-x}: L(z)=1/(z+1).
        w=complex(1e-5,1e-5)
        difference = (1/(z+w+1)-1/(z+1))/w
        assert abs(difference + 1/(z+1)**2) < 1e-4
        count+=1
    assert count==23
    print(f"PASS R11 Laplace real and complex examples: {count} checks")


def test_sources():
    docs = [(BASE / name).read_text(encoding="utf-8") for name in NAMES]
    src = docs[10]
    labels = [m.group(1) for d in docs for m in
              re.finditer(r"\\label\{([^}]+)\}", d)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", src)]
    assert len(labels)==len(set(labels)), "duplicate labels R01-R12"
    assert set(refs)<=set(labels), f"missing references {set(refs)-set(labels)}"
    stack=[]
    for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",src):
        if kind=="begin":
            stack.append(env)
        else:
            assert stack and stack.pop()==env, f"unbalanced environment {env}"
    assert not stack, f"open environments {stack}"
    # Search whole words only: "konsekwencji" contains "sekwencji"
    # as a substring, but is correct Polish and must not be flagged.
    assert not re.search(r"\bsekwencj\w*", src, flags=re.UNICODE)
    for disallowed in (
        "unia zbiorów", "zbieżność zdominowana",
        "pierwszoprzeliczal", "drugoprzeliczal",
        r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}",
    ):
        assert disallowed not in src, f"bad terminology: {disallowed}"
    for required in (
        r"\label{thm:uniform-parameter-11}",
        r"\label{thm:local-differentiation-11}",
        r"\label{thm:higher-differentiation-11}",
        r"\label{thm:laplace-holo-11}",
        r"g_0:X\to[0,\infty)",
        r"Na wspólnym mierzalnym zbiorze wyjątkowym",
        r"Niech $(X,\mathcal F,\mu)$ będzie przestrzenią z miarą",
    ):
        assert required in src, required
    print(f"PASS R11 source: {len(refs)} cross-references and TeX structure")


if __name__ == "__main__":
    test_uniform_parameter()
    test_differentiation()
    test_moving_domains()
    test_uniform_tails()
    test_laplace()
    test_sources()
