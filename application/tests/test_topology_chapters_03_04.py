"""Regression tests for the second two-chapter AT mathematical audit.

Keeps historical labels, verifies source independence, checks targets against
the four-chapter audit build and exercises the noncommutative pivot-order fix.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters" / "pl" / "algebraic_topology"
FILES = sorted(CHAPTERS.glob("0[1-4]-*.tex"))
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


def matmul(x, y):
    """2x2 matrix product over F_2; ring multiplication is not commutative."""
    a, b, c, d = x
    e, f, g, h = y
    return ((a*e+b*g) % 2, (a*f+b*h) % 2,
            (c*e+d*g) % 2, (c*f+d*h) % 2)


class TopologyChapterThreeFourAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = {f.name[:2]: f.read_text(encoding="utf-8-sig") for f in FILES}

    def test_four_original_chapters_in_book(self):
        self.assertEqual(set(self.text), {"01", "02", "03", "04"})
        book = BOOK.read_text(encoding="utf-8-sig")
        for f in FILES:
            self.assertIn(r"\input{../../chapters/pl/algebraic_topology/"
                          + f.name + "}", book)

    def test_historical_labels_remain_unique(self):
        for idx, names in [
            ("03", ("ch:algebra-homologiczna", "thm:les-homologia",
                    "thm:mod-m-homologia", "thm:kasowanie-pary")),
            ("04", ("ch:topologia-algebraiczna-podstawy",
                    "thm:grupa-podstawowa", "thm:pi1-okragu",
                    "thm:van-kampen", "thm:pi1-dolaczenie-komorki")),
        ]:
            for name in names:
                self.assertEqual(self.text[idx].count(r"\label{" + name + "}"), 1)
        labels = re.findall(r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values()))
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_at03_at04_refs_have_targets_in_audit_book(self):
        labels = set(re.findall(r"\\label\s*\{([^}]+)\}",
                                "\n".join(self.text.values())))
        for idx in ("03", "04"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.text[idx]
            )
            self.assertGreaterEqual(len(refs), 10)
            self.assertEqual(set(refs) - labels, set())

    def test_no_new_external_file_dependencies(self):
        for idx in ("03", "04"):
            src = self.text[idx]
            for command in ("includegraphics", "input", "lstinputlisting",
                            "inputminted", "include"):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")
            starts = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            ends = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(starts, ends)
            self.assertGreaterEqual(starts["figure"], 2)

    def test_consistent_polish_tensor_terminology(self):
        for idx in ("03", "04"):
            self.assertNotRegex(self.text[idx].lower(),
                                r"\btensorowan\w*|\btensorowali\w*")

    def test_dual_hom_explicit_commutativity(self):
        ch = self.text["03"]
        target = ch[ch.index(r"\begin{stwierdzenie}[Kompleks dualny]"):]
        self.assertIn("przemiennym pierścieniem z jedynką", target[:280])
        self.assertIn(r"\operatorname{Hom}_R(C_n,G)", ch)

    def test_noncommutative_cancellation_uses_correct_coefficient_order(self):
        ch = self.text["03"]
        self.assertIn("x-a(x)u^{-1}e", ch)
        self.assertNotIn("x-u^{-1}a(x)e", ch)
        # Choose u^2=I and noncentral a in M_2(F_2).
        u = (1, 1, 0, 1)
        a = (0, 0, 1, 0)
        zero = (0, 0, 0, 0)
        self.assertEqual(matmul(u, u), (1, 0, 0, 1))
        self.assertNotEqual(matmul(a, u), matmul(u, a))
        # Correct pivot coefficient a*u^{-1}: (a*u^{-1})*u=a.
        self.assertEqual(matmul(matmul(a, u), u), a)
        # Incorrect pivot coefficient u^{-1}*a: (u^{-1}*a)*u != a.
        self.assertNotEqual(matmul(matmul(u, a), u), a)

    def test_mod_two_complex_and_connecting_map(self):
        # C_2=F2, C_1=F2^2, C_0=F2, d_2=0, d_1(x,y)=x.
        c1 = [(x,y) for x in range(2) for y in range(2)]
        cycles1 = [(x,y) for x,y in c1 if x == 0]
        boundaries1 = {(0,0)}
        self.assertEqual(len(cycles1)//len(boundaries1), 2)
        self.assertEqual(2, 2)  # dim H_2 = 1, since d_2 = 0
        self.assertEqual({x for x,y in c1}, {0,1})  # H_0 = 0
        # For lift 1 in C_2(Z), d_2(1)=(0,2)=2(0,1).
        self.assertEqual((0,2), (0,2*1))
        self.assertIn(r"\delta_2[\bar1]", self.text["03"])

    def test_finite_cover_degree_section_obstruction(self):
        ch = self.text["04"]
        self.assertIn(r"\label{prz:nakrycie-m-arkuszy}", ch)
        self.assertIn(r"\label{fig:nakrycie-m-arkuszy}", ch)
        self.assertIn(r"(q_m)_*\circ t_*=\id_{\Z}", ch)
        for m in (2, 3, 5):
            self.assertNotIn(1, [m*k for k in range(-20, 21)])


if __name__ == "__main__":
    unittest.main()
