"""Regression gates for the detailed mathematical audit of AT-01 and AT-02.

These protect specific checked mathematical examples, label identities,
source independence and terminology. They do not replace PDF compilation.
"""
from __future__ import annotations

from collections import Counter
from math import gcd
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
CH1 = AT / "01-jezyk-i-podstawowe-konstrukcje-topologiczne.tex"
CH2 = AT / "02-podstawy-algebry-abstrakcyjnej-grupy-pierscienie-i-moduly.tex"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


def compose(p, q):
    """Composition p after q for a four-vertex permutation."""
    return tuple(p[q[i]] for i in range(4))


class AuditedAlgebraicTopologyChapters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = CH1.read_text(encoding="utf-8-sig")
        cls.b = CH2.read_text(encoding="utf-8-sig")

    def test_registered_in_existing_modular_book(self):
        main = BOOK.read_text(encoding="utf-8-sig")
        for source in (CH1, CH2):
            self.assertIn(r"\input{../../chapters/pl/algebraic_topology/" +
                          source.name + "}", main)

    def test_original_label_identifiers_survive(self):
        for text, names in [
            (self.a, ("ch:wstep-topologia", "def:topologia-ilorazowa")),
            (self.b, ("ch:algebra-abstrakcyjna-v5",
                      "thm:izo-grupy-v5", "sec:tensor-algebra-v5",
                      "thm:tensor-uni-v5")),
        ]:
            for name in names:
                self.assertEqual(text.count(r"\label{" + name + "}"), 1)

    def test_local_label_occurrences_are_unique(self):
        labels = re.findall(r"\\label\s*\{([^}]+)\}", self.a + "\n" + self.b)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertGreaterEqual(len(labels), 12)

    def test_inline_figures_and_balanced_environments(self):
        for text in (self.a, self.b):
            starts = Counter(re.findall(r"\\begin\{([^}]+)\}", text))
            ends = Counter(re.findall(r"\\end\{([^}]+)\}", text))
            self.assertEqual(starts, ends)
            self.assertGreaterEqual(starts["figure"], 1)
            self.assertNotIn(r"\includegraphics", text)
            self.assertNotIn(r"\input{", text)
            self.assertNotIn(r"\lstinputlisting", text)

    def test_no_disallowed_polish_terminology(self):
        self.assertIsNone(re.search(r"\btensorowan\w*", self.a + "\n" + self.b,
                                    re.IGNORECASE))

    def test_quotient_and_projective_examples_have_proofs(self):
        for label in (
            "lem:zwarta-hausdorff-top-intro",
            "prz:iloraz-okragu-torusa-top-intro",
            "uw:iloraz-niehausdorff-top-intro",
            "prz:rzutowe-wymiar-jeden-top-intro",
            "prz:sinus-topologa-top-intro",
        ):
            self.assertIn(r"\label{" + label + "}", self.a)
        self.assertIn(r"$\C P^1\cong S^2$", self.a)

    def test_ring_assumptions_and_tor_definition(self):
        self.assertIn(r"pierścieniem z jedynką", self.b)
        self.assertIn(r"pierścieniem z jedynką. Pozwala to", self.b)
        self.assertIn(r"\operatorname{Tor}_1^\Z(A,B)", self.b)
        self.assertIn(r"\operatorname{Ext}^1_\Z(A,B)", self.b)

    def test_dihedral_group_example(self):
        identity = (0, 1, 2, 3)
        r = (1, 2, 3, 0)
        s = (1, 0, 3, 2)
        powers = [identity]
        for _ in range(3):
            powers.append(compose(powers[-1], r))
        elements = set(powers + [compose(p, s) for p in powers])
        self.assertEqual(len(elements), 8)
        self.assertEqual(compose(s, compose(r, s)), powers[3])
        self.assertEqual(len({p[0] for p in elements}), 4)
        self.assertEqual(sum(p[0] == 0 for p in elements), 2)

    def test_cyclic_tor_ext_examples(self):
        for m, n in [(2, 3), (12, 18), (4, 6), (1, 7)]:
            kernel_count = sum((m * x) % n == 0 for x in range(n))
            subgroup = {(m * x) % n for x in range(n)}
            ext_quotient_size = n // len(subgroup)
            self.assertEqual(kernel_count, gcd(m, n))
            self.assertEqual(ext_quotient_size, gcd(m, n))


if __name__ == "__main__":
    unittest.main()
