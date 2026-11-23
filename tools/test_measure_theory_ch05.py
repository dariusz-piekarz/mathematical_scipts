"""Finite regressions and LaTeX source checks for measure theory, chapter 05.

Finite models illustrate, but do not prove, the general statements.
"""
from itertools import product
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters/pl/measure_theory"
NAMES = (
    "01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex",
    "02-miary-i-ich-podstawowe-wlasnosci.tex",
    "03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex",
    "04-miara-lebesguea-na-przestrzeni-euklidesowej.tex",
    "05-struktura-przestrzeni-mierzalnych.tex",
)


def powerset(points):
    return [
        frozenset(x for i, x in enumerate(points) if mask & (1 << i))
        for mask in range(1 << len(points))
    ]


def generated_sigma(points, generators):
    """Finite sigma algebra from atoms of the generator-membership partition."""
    atoms = {}
    for point in points:
        signature = tuple(point in item for item in generators)
        atoms.setdefault(signature, set()).add(point)
    cells = list(atoms.values())
    return {
        frozenset(x for i, cell in enumerate(cells)
                  if mask & (1 << i) for x in cell)
        for mask in range(1 << len(cells))
    }


def check_trace():
    x = tuple(range(3))
    all_subsets = powerset(x)
    cases = 0
    for family_mask in range(1 << len(all_subsets)):
        generators = [
            e for i, e in enumerate(all_subsets) if family_mask & (1 << i)
        ]
        sigma = generated_sigma(x, generators)
        for a in all_subsets:
            left = {b & a for b in sigma}
            right = generated_sigma(tuple(sorted(a)), [b & a for b in generators])
            assert left == right
            cases += 1
    assert cases == 2048
    print(f"PASS R05 trace and generation: {cases} exhaustive finite cases")


def check_initial_sigma():
    x = tuple(range(3))
    y = tuple(range(3))
    subsets_x, subsets_y = powerset(x), powerset(y)
    cases = 0
    for values in product(y, repeat=len(x)):
        inverse_images = [
            frozenset(i for i, value in enumerate(values) if value in b)
            for b in subsets_y
        ]
        initial = set(inverse_images)
        assert initial == generated_sigma(x, inverse_images)
        for fm in range(1 << len(subsets_x)):
            sigma_x = generated_sigma(
                x, [a for i, a in enumerate(subsets_x) if fm & (1 << i)]
            )
            is_measurable = all(a in sigma_x for a in inverse_images)
            assert is_measurable == (initial <= sigma_x)
            cases += 1
    assert cases == 6912
    print(f"PASS R05 initial sigma/minimality: {cases} finite cases")


def check_product_projections():
    x, y = (0, 1), (0, 1, 2)
    xy = tuple(product(x, y))
    sigma_x = {frozenset(x), frozenset(), frozenset({0}), frozenset({1})}
    sigma_y = {frozenset(y), frozenset(),
               frozenset({0}), frozenset({1}), frozenset({2})}
    # Enumerate all sub-sigma-algebras of the full powersets.
    def all_sigmas(points):
        subsets = powerset(points)
        return {frozenset(generated_sigma(
            points, [s for i, s in enumerate(subsets) if mask & (1 << i)]
        )) for mask in range(1 << len(subsets))}
    count = 0
    for fx in all_sigmas(x):
        for gy in all_sigmas(y):
            rectangles = [
                frozenset((a, b) for a, b in xy if a in aa and b in bb)
                for aa in fx for bb in gy
            ]
            strips = [
                frozenset((a, b) for a, b in xy if a in aa) for aa in fx
            ] + [
                frozenset((a, b) for a, b in xy if b in bb) for bb in gy
            ]
            assert generated_sigma(xy, rectangles) == generated_sigma(xy, strips)
            count += 1
    assert count == 10
    print(f"PASS R05 products and projections: {count} sigma-algebra pairs")


def check_pushforward():
    weights = (2, 0, 3)
    x, y, z = tuple(range(3)), tuple(range(2)), tuple(range(3))
    cases = 0
    for fv in product(y, repeat=len(x)):
        pushed_y = tuple(
            sum(weights[i] for i in x if fv[i] == j) for j in y
        )
        for gv in product(z, repeat=len(y)):
            for c in powerset(z):
                lhs = sum(weights[i] for i in x if gv[fv[i]] in c)
                rhs = sum(pushed_y[j] for j in y if gv[j] in c)
                assert lhs == rhs
                cases += 1
    assert cases == 648
    print(f"PASS R05 functorial pushforward: {cases} cases")
    assert all(
        (7 if 1 in b else 0) == sum((7,) if 1 in b else ())
        for b in powerset(y)
    )


def check_latex_sources():
    docs = [(CHAPTERS / name).read_text(encoding="utf-8") for name in NAMES]
    source = docs[-1]
    labels = [m.group(1) for doc in docs
              for m in re.finditer(r"\\label\{([^}]+)\}", doc)]
    refs = [m.group(1) for m in
            re.finditer(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", source)]
    assert len(labels) == len(set(labels)), "duplicate labels in R01-R05"
    assert set(refs) <= set(labels), f"unresolved: {set(refs)-set(labels)}"
    stack = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
        if kind == "begin":
            stack.append(name)
        else:
            assert stack and stack.pop() == name, f"unbalanced: {name}"
    assert not stack, f"unclosed environments: {stack}"
    for forbidden in (
        "drugoprzeliczal", "pierwszoprzeliczal", "unia zbiorów",
        "zbieżność zdominowana", r"\mathbf{1}", r"\mathbb{1}", r"\mathds{1}",
    ):
        assert forbidden not in source, f"forbidden text: {forbidden}"
    assert "przestrzeni spełniających drugi aksjomat przeliczalności" in source
    assert "Dla każdego $B\\in\\mathcal G$ mamy $(f_\\#\\mu)(B)" in source
    print(f"PASS R05 source: {len(refs)} resolved references and TeX structure")


if __name__ == "__main__":
    check_trace()
    check_initial_sigma()
    check_product_projections()
    check_pushforward()
    check_latex_sources()
