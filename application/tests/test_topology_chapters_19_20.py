"""AT-19/20 rigorous audit regressions: Lefschetz, Morse compactification.

Keep original labels, compare dependency chain and cross-volume references,
check actual matrix and explicit ODE/Green calculations. The independent
two-pass LaTeX workflow validates the PDF and diagrams.
"""
from __future__ import annotations

from collections import Counter
from math import atan, cos, exp, sin, pi, sqrt
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyNineteenTwentyAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 21)
            for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.texts = {
            f.name[:2]: f.read_text(encoding="utf-8-sig")
            for f in cls.files
        }

    def test_canonical_book_loads_all_twenty_chapters(self):
        self.assertEqual(
            set(self.texts), {f"{i:02d}" for i in range(1, 21)}
        )
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(file=file.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_historical_labels_survive_with_no_duplicates(self):
        historical = {
            "19": (
                "ch:lefschetz-v10", "lem:hopf-trace-v10",
                "thm:lefschetz-v10", "def:fixed-index-v10",
                "thm:lefschetz-hopf-v10",
            ),
            "20": (
                "ch:morse-analytic-v11",
                "lem:morse-energy-analytic-v11",
                "lem:morse-transit-v11", "def:broken-morse-v11",
                "thm:morse-broken-compact-v11",
                "cor:morse-rigid-finite-v11",
                "lem:morse-exponential-v11",
                "thm:morse-gluing-v11", "prop:morse-d2-analytic-v11",
            ),
        }
        for ch, labels in historical.items():
            for label in labels:
                with self.subTest(ch=ch, label=label):
                    self.assertEqual(
                        self.texts[ch].count(r"\label{" + label + "}"), 1
                    )
        all_labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        )
        self.assertEqual(len(all_labels), len(set(all_labels)))

    def test_at19_and_20_references_resolve_with_prior_chapters(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.texts.values())
        ))
        for ch in ("19", "20"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.texts[ch],
            )
            self.assertGreaterEqual(len(refs), 3)
            self.assertEqual(set(refs) - labels, set())

    def test_diagrams_and_environments_are_independent(self):
        for ch in ("19", "20"):
            source = self.texts[ch]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", source)),
                Counter(re.findall(r"\\end\{([^}]+)\}", source)),
            )
            self.assertGreaterEqual(
                source.count(r"\begin{tikzpicture}"), 2
            )
            for command in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(
                    source, r"\\" + command + r"\s*\{"
                )

    def test_correct_polish_mathematical_terms(self):
        for ch in ("19", "20"):
            self.assertNotRegex(
                self.texts[ch].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekcj\w*",
            )

    def test_real_dg_exterior_power_and_morse_sources(self):
        tensor_source = (
            DG / "03-algebra-tensorowa-i-zewnetrzna.tex"
        ).read_text(encoding="utf-8-sig")
        morse_source = (
            DG / "18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex"
        ).read_text(encoding="utf-8-sig")
        for label in ("thm:potega-zewn-operatora", "thm:minory-lambda"):
            self.assertIn(r"\label{" + label + "}", tensor_source)
            self.assertIn(label, self.texts["19"])
        self.assertIn(r"\label{ch:teoria-morsea}", morse_source)
        self.assertIn("18-teoria-morse-a-punkty-krytyczne-", self.texts["20"])

    def test_lefschetz_torus_two_fixed_points_and_indices(self):
        ch = self.texts["19"]
        self.assertIn(r"\label{prz:lefschetz-torus-dwa-indeksy}", ch)
        self.assertIn(r"\label{fig:lefschetz-torus-dwa-indeksy}", ch)
        A = ((2, 1), (1, 0))
        det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        trace_A = A[0][0] + A[1][1]
        det_I_minus_A = (
            (1-A[0][0])*(1-A[1][1]) - A[0][1]*A[1][0]
        )
        self.assertEqual((det_A, trace_A, det_I_minus_A), (-1, 2, -2))
        self.assertEqual(1 - trace_A + det_A, det_I_minus_A)
        fixed = ((0, 0), (0.5, 0.5))
        for x, y in fixed:
            with self.subTest(x=x, y=y):
                self.assertEqual((A[0][0]-1)*x + A[0][1]*y, int(
                    (A[0][0]-1)*x + A[0][1]*y
                ))
                self.assertEqual(A[1][0]*x + (A[1][1]-1)*y, int(
                    A[1][0]*x + (A[1][1]-1)*y
                ))
        # Same parity of (m+n,m-n) means index exactly 2 in Z².
        self.assertEqual(
            {(m+n) % 2 == (m-n) % 2
             for m in range(-4, 5) for n in range(-4, 5)},
            {True},
        )
        self.assertEqual(sum([-1, -1]), det_I_minus_A)

    def test_scalar_hyperbolic_green_inverse_is_uniform(self):
        ch = self.texts["20"]
        self.assertIn(r"\label{lem:morse-scalar-green}", ch)
        for lam in (-4.0, -1.5, 0.4, 2.0):
            # Unique bounded solution to u' + lam*u = sin(t).
            # Inverse Fourier multiplier: u=(lam sin(t)-cos(t))/(lam²+1).
            def u(t):
                return (lam*sin(t) - cos(t)) / (1+lam*lam)

            def du(t):
                return (lam*cos(t) + sin(t)) / (1+lam*lam)

            for t in (-4.3, -0.4, 0.0, 0.7, 2.5):
                with self.subTest(lam=lam, t=t):
                    self.assertAlmostEqual(
                        du(t) + lam*u(t), sin(t), places=12
                    )
                    self.assertLessEqual(
                        abs(u(t)), 1/abs(lam)+1e-12
                    )

    def test_torus_odes_and_smooth_gluing_parameter(self):
        ch = self.texts["20"]
        self.assertIn(r"\label{prz:morse-torus-gluing-explicit}", ch)
        self.assertIn(r"\label{fig:morse-torus-gluing-explicit}", ch)
        self.assertIn(r"s=b-a", ch)
        self.assertIn(r"\rho_+=e^{-s}", ch)
        self.assertIn(r"\rho_-=e^{s}", ch)

        def angle(t, a, sign):
            return 2*sign*atan(exp(t-a))

        for sign in (-1, 1):
            for a in (-1.0, 0.5):
                for t in (-2.0, 0, 3.0):
                    h = 1e-6
                    numerical_derivative = (
                        angle(t+h, a, sign) -
                        angle(t-h, a, sign)
                    ) / (2*h)
                    with self.subTest(sign=sign, a=a, t=t):
                        self.assertAlmostEqual(
                            numerical_derivative,
                            sin(angle(t, a, sign)),
                            places=8,
                        )
        for s in (5.0, 10.0):
            rho = exp(-s)
            u = 0.2
            # On the theta-transition window, the second angle
            # is given exactly by 2*atan(rho*e^u).
            self.assertAlmostEqual(
                angle(-s/2+u, s/2, 1),
                2*atan(rho*exp(u)),
                places=12,
            )

    def test_general_gluing_gap_is_still_explicit(self):
        ch = self.texts["20"]
        self.assertIn(r"o prawym odwrotnym", ch)
        self.assertIn("nie zastępuje ogólnego lematu", ch)
        self.assertIn(r"\mathcal D_T", ch)
        self.assertIn("jednostajny", ch)
        self.assertIn("pozostaje odrębnym krokiem", ch)


if __name__ == "__main__":
    unittest.main()
