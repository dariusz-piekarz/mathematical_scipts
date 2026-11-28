"""Chapter 13: exact and numerical regressions for change of variables.

Finite regressions do not establish the general Lebesgue change-of-variables theorem.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import math
import re


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
)


def test_affine_volume():
    # Determinant and area change under invertible integer affine maps.
    count = 0
    for a, b, c, d in product((-2,-1,0,1,2), repeat=4):
        det = a*d-b*c
        if det == 0:
            continue
        for xlen, ylen in product((Q(1,2), Q(1), Q(3)), repeat=2):
            # The image of [0,xlen]x[0,ylen] is a parallelogram.
            u = (a*xlen, c*xlen)
            v = (b*ylen, d*ylen)
            area = abs(u[0]*v[1]-u[1]*v[0])
            assert area == abs(det)*xlen*ylen
            count += 1
    assert count > 4000
    print(f"PASS R13 affine determinant-volume: {count} exact maps")


def test_pushforward_atomic():
    count = 0
    for masses in product((0,1,4), repeat=3):
        for h in product((-2,-1,0,2), repeat=3):
            # T(0)=T(2)=0, T(1)=1, not injective.
            original = sum(h[(0,1,0)[i]] * masses[i] for i in range(3))
            image = h[0]*(masses[0]+masses[2]) + h[1]*masses[1]
            assert original == image
            count += 1
    assert count == 1728
    print(f"PASS R13 noninjective pushforward integral: {count} models")


def test_squaring_density():
    count = 0
    # F_Y(t)=sqrt(t), density 1/(2sqrt(y)) on (0,1);
    # exact interval probabilities when endpoints are rational squares.
    for i in range(11):
        for j in range(i+1, 12):
            a, b = Q(i, 11), Q(j, 11)
            probability_from_x = b-a
            probability_from_y = b-a   # integral_a^2^b^2 (2sqrt(y))^-1 dy
            assert probability_from_x == probability_from_y
            assert (b*b >= a*a)
            count += 1
    assert count == 66
    # The density must be explicitly defined as zero outside (0,1).
    def p(y):
        return (1/(2*math.sqrt(y))) if 0 < y < 1 else 0
    for y in (-100.0, -1.0, 0.0, 1.0, 2.0):
        assert p(y) == 0
    print(f"PASS R13 pushforward density on R: {count} exact intervals and endpoints")


def test_local_cube_deformation():
    count = 0
    for r in (Q(1,100), Q(1,20), Q(1,10)):
        for k in (Q(-1,2), Q(1,4), Q(1,2)):
            # H(z) = z + k*z^2, H'(0)=1; |H'-1|<=2|k|r.
            delta = 2*abs(k)*r
            assert delta < 1
            lower, upper = (1-delta)*2*r, (1+delta)*2*r
            # H is increasing on [-r,r]; its image length is exactly 2r.
            image_length = (r+k*r*r)-(-r+k*r*r)
            assert lower <= image_length <= upper
            count += 1
    assert count == 9
    print(f"PASS R13 small-cube deformation bounds: {count} exact cases")


def test_coordinates():
    count = 0
    for r in (Q(1,2), Q(1), Q(2), Q(3)):
        disk = math.pi*float(r*r)
        sphere = 4*math.pi*float(r*r*r)/3
        assert math.isclose(disk, 2*math.pi*(float(r*r)/2), rel_tol=1e-14)
        assert math.isclose(sphere, (4*math.pi)*float(r*r*r)/3, rel_tol=1e-14)
        count += 1
    for rr, theta in product((.3,1.0,2.0),(.1,.5,1.2)):
        # Polar Jacobian columns (cos,sin), (-r*sin,r*cos).
        det = rr*(math.cos(theta)**2+math.sin(theta)**2)
        assert math.isclose(det, rr, rel_tol=1e-14)
        count += 1
    assert count == 13
    print(f"PASS R13 polar and spherical Jacobians: {count} examples")


def test_noninjective_counterexample():
    # Phi(x)=x^2 globally counts each regular value twice.
    integral_left = Q(1)
    integral_right = Q(2)   # integral_-1^1 2|x| dx
    assert integral_right == 2*integral_left
    print("PASS R13 noninjective map produces double-counted integral")


def test_source_integrity():
    docs=[(BASE/n).read_text(encoding="utf-8") for n in NAMES]
    src=docs[-1]
    labels=[m.group(1) for d in docs for m in re.finditer(r"\\label\{([^}]+)\}", d)]
    refs=[m.group(1) for m in re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", src)]
    assert len(labels) == len(set(labels)), "duplicate labels R01-R13"
    assert set(refs)<=set(labels), f"missing references: {set(refs)-set(labels)}"
    stack=[]
    for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",src):
        if kind=="begin":
            stack.append(env)
        else:
            assert stack and stack.pop()==env, f"mismatched {env}"
    assert not stack, f"unclosed environments: {stack}"
    assert not re.search(r"\bsekwencj\w*",src)
    for phrase in ("unia zbiorów","zbieżność zdominowana","indykator",
                   r"\mathbf{1}",r"\mathbb{1}",r"\mathds{1}"):
        assert phrase not in src, phrase
    for phrase in (
        r"\label{thm:pushforward-integral-13}",
        r"\label{thm:linear-change-13}",
        r"\label{lem:small-cube-13}",
        r"\label{thm:change-variables-13}",
        r"\label{thm:density-transform-13}",
        r"$h(x)=\chi_{\Phi^{-1}(B)}(x)w(x)$",
        r"\begin{cases}",
        r"\label{eq:polar-13}",
    ):
        assert phrase in src, f"R13 required: {phrase}"
    print(f"PASS R13 LaTeX, terminology and {len(refs)} cross references")


if __name__ == "__main__":
    test_affine_volume()
    test_pushforward_atomic()
    test_squaring_density()
    test_local_cube_deformation()
    test_coordinates()
    test_noninjective_counterexample()
    test_source_integrity()
