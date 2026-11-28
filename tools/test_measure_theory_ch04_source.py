"""Static regression checks for chapter 04, including the Cantor TikZ figure.

Not a replacement for an actual LaTeX compile or visual PDF inspection.
"""
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters/pl/measure_theory"
NAMES = (
    "01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex",
    "02-miary-i-ich-podstawowe-wlasnosci.tex",
    "03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex",
    "04-miara-lebesguea-na-przestrzeni-euklidesowej.tex",
)
contents = [(CHAPTERS / name).read_text(encoding="utf-8") for name in NAMES]
source = contents[-1]

labels = [
    label
    for doc in contents
    for label in re.findall(r"\\label\{([^}]+)\}", doc)
]
assert len(labels) == len(set(labels)), "duplicate label in R01-R04"
references = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)
missing = sorted(set(references) - set(labels))
assert not missing, f"unresolved references in R04: {missing}"

stack = []
for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
    if kind == "begin":
        stack.append(name)
    else:
        assert stack and stack.pop() == name, f"unbalanced environment: {name}"
assert not stack, f"unclosed environments: {stack}"

assert "Jeśli $a=b$, to $\\Gamma_f$ jest singletonem" in source, (
    "the zero-length Lipschitz graph case is not justified"
)
assert "Niech $a,b\\in\\mathbb R$, $a\\le b$, $L\\ge0$" in source, (
    "explicit Lipschitz graph hypotheses are missing"
)

for forbidden in (
    r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}",
    "zbieżność zdominowana", "unia zbiorów",
):
    assert forbidden not in source, f"forbidden notation: {forbidden}"

figure = re.search(
    r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
    source, re.DOTALL,
)
assert figure is not None
assert len(re.findall(r"\\begin\{tikzpicture\}", source)) == 1
assert re.search(
    r"\\end\{tikzpicture\}\s*\\par\\smallskip\s*"
    r"\\emph\{Pierwsze cztery etapy",
    source,
), "Cantor caption must begin its own paragraph below the diagram"

blocks = re.findall(r"\\foreach \\a/\\b in \{([^}]*)\}", figure.group())
assert len(blocks) == 3, f"expected 3 loop-drawn Cantor stages, got {len(blocks)}"
expected = [(Fraction(0), Fraction(1))]
checked_endpoints = 0
tolerance = Fraction(1, 10**6)  # TikZ specifies six decimal places
for n, block in enumerate(blocks, start=1):
    intervals = [
        tuple(Fraction(value) for value in item.split("/"))
        for item in block.split(",")
    ]
    expected = [
        part
        for a, b in expected
        for part in (
            (a, a + (b-a)/3),
            (b - (b-a)/3, b),
        )
    ]
    assert len(intervals) == len(expected) == 2**n
    for (a, b), (want_a, want_b) in zip(intervals, expected):
        assert abs(a - want_a) <= tolerance, (n, a, want_a)
        assert abs(b - want_b) <= tolerance, (n, b, want_b)
        checked_endpoints += 2
assert checked_endpoints == 28

print(
    f"PASS R04: {len(labels)} labels in R01-R04, "
    f"{len(references)} resolved references, "
    f"paired TeX environments, 28 Cantor endpoints and caption"
)
