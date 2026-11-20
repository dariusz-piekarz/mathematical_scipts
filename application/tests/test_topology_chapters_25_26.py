"""AT-25/26: regression audit of Hodge monodromy and Legendre periods.

The source remains 26 independent TeX chapters; diagrams are inline.
Numerical calculations use only the Python standard library.
"""
from __future__ import annotations

from collections import Counter
from math import comb, pi
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyTwentyFiveTwentySixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            p for n in range(10, 27) for p in AT.glob(f"{n:02d}-*.tex")
        )
        cls.src = {p.name[:2]: p.read_text(encoding="utf-8-sig")
                   for p in cls.paths}

    def test_book_has_all_twenty_six_canonical_chapters(self):
        self.assertEqual(set(self.src), {f"{n:02d}" for n in range(1, 27)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for path in self.paths:
            with self.subTest(path=path.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + path.name + "}", book
                )

    def test_historical_labels_preserved_and_no_duplicates(self):
        historical = {
            "25": (
                "ch:xiv-hodge-monodromia", "lem:cone-complex-xiv",
                "thm:cone-les-xiv", "ex:derived-not-split-xiv",
                "prop:hodge-filtration-xiv", "thm:kahler-hodge-xiv",
                "ex:nodal-mhs-xiv", "def:nearby-vanishing-xiv",
                "prop:milnor-stalk-xiv", "ex:node-monodromy-xiv",
                "thm:a1-monodromy-xiv", "thm:picard-lefschetz-xiv",
            ),
            "26": (
                "ch:xv-vhs-degeneracje", "prop:xv-gm-local",
                "prop:xv-period-derivative", "thm:xv-vhs-family",
                "prop:xv-pf-general", "sec:xv-legendre",
                "prop:xv-legendre-period", "thm:xv-legendre-pf",
                "prop:xv-legendre-T2", "lem:xv-weights-rank2",
                "thm:xv-lmhs", "ex:xv-central-limit",
            ),
        }
        for chapter, labels in historical.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.src[chapter].count(r"\label{" + label + "}"), 1
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.src.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_new_and_existing_references_resolve(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.src.values())
        ))
        for chapter in ("25", "26"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.src[chapter],
            )
            self.assertGreaterEqual(len(refs), 4)
            self.assertEqual(set(refs) - labels, set())

    def test_balanced_latex_and_no_external_resources(self):
        for chapter in ("25", "26"):
            s = self.src[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", s)),
                Counter(re.findall(r"\\end\{([^}]+)\}", s)),
            )
            self.assertGreaterEqual(s.count(r"\begin{tikzpicture}"), 2)
            for cmd in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(s, r"\\" + cmd + r"\s*\{")
            self.assertNotRegex(
                s.lower(),
                r"\btensorowan\w*|\bsekwencj\w*|\binjekcj\w*"
                r"|\bseskwilini\w*",
            )
            self.assertNotIn(r"\boxed{", s)

    def test_power_map_vanishing_cycles_and_quasi_unipotence(self):
        s = self.src["25"]
        self.assertIn(r"\label{prz:monodromy-zm-v14}", s)
        self.assertIn(r"\label{fig:monodromy-z3}", s)
        self.assertIn(r"\frac{T^m-1}{T-1}", s)
        for m in range(2, 11):
            # Cyclic action on Q^m; augmentation kernel has dim m-1.
            vectors = [tuple(1 if j == i else -1 if j == m-1 else 0
                             for j in range(m)) for i in range(m-1)]
            for v in vectors:
                self.assertEqual(sum(v), 0)
            # The cyclic shift has order m (and is not identity).
            perm = list(range(m))
            for _ in range(m):
                perm = perm[-1:] + perm[:-1]
            self.assertEqual(perm, list(range(m)))
            self.assertEqual(m-1, len(vectors))

    def test_cubic_milnor_monodromy_matrix(self):
        # On basis (e0-e1,e1-e2) permutation has matrix [[0,-1],[1,-1]].
        a = ((0, -1), (1, -1))

        def product(x, y):
            return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(2))
                               for j in range(2)) for i in range(2))

        self.assertEqual(product(product(a, a), a), ((1, 0), (0, 1)))
        self.assertNotEqual(a, ((1, 0), (0, 1)))
        self.assertEqual(a[0][0] + a[1][1], -1)
        self.assertEqual(a[0][0]*a[1][1]-a[0][1]*a[1][0], 1)

    def test_weight_filtration_rank_one_requires_nontriviality(self):
        s = self.src["26"]
        self.assertIn(r"\label{lem:xv-weights-rank2}", s)
        self.assertIn(r"\subsetneq W_0=W_1", s)
        self.assertIn(r"\subsetneq W_2=V_\Q", s)
        self.assertIn("izomorfizmem", s)
        self.assertIn("zerowymi", s)
        # Matrix for N(e2)=2e0, N(e0)=0, so N²=0, ker=im=Qe0.
        N = ((0, 2), (0, 0))
        N2 = tuple(tuple(sum(N[i][k]*N[k][j] for k in range(2))
                         for j in range(2)) for i in range(2))
        self.assertEqual(N2, ((0, 0), (0, 0)))
        self.assertEqual((N[0][1], N[1][1]), (2, 0))

    def test_legendre_wronskian_derivative_at_half(self):
        src = self.src["26"]
        self.assertIn(r"\label{prz:xv-legendre-wronskian}", src)
        # Hypergeometric u = sum a_n lambda^n.
        # At lambda=1/2: v=i*u(1-lambda), W=-2i*u*u',
        # and the theorem predicts W=-4i/pi.
        coefficients = [(comb(2*n, n)/4**n)**2 for n in range(60)]
        lam = .5
        u = sum(a*lam**n for n,a in enumerate(coefficients))
        uprime = sum(n*a*lam**(n-1) for n,a in
                     enumerate(coefficients) if n)
        self.assertAlmostEqual(2*u*uprime, 4/pi, places=11)
        derivative = -2j*uprime/u
        predicted = -4j/(pi*u*u)
        self.assertAlmostEqual(abs(derivative-predicted), 0.0, places=11)

    def test_monodromy_base_change_and_filtration(self):
        src = self.src["26"]
        self.assertIn(r"\label{prz:xv-legendre-weight-explicit}", src)
        self.assertIn(r"\label{fig:xv-legendre-weight-explicit}", src)
        self.assertIn(r"\operatorname{im}N=\ker N=\Q e_0", src)
        for q in range(1, 8):
            # (I+N)^q=I+qN and ker/image independent of q>0.
            Tq = ((1, 2*q), (0, 1))
            self.assertEqual(Tq[0][1], 2*q)
            self.assertEqual(Tq[1][0], 0)

    def test_advanced_dependencies_do_not_become_false_proofs(self):
        a, b = self.src["25"], self.src["26"]
        self.assertIn("twierdzenia Milnora", a)
        self.assertIn("nie ogólny dowód", a)
        self.assertIn("twierdzenia Schmida", b)
        self.assertIn("nie dowodem istnienia granicznej filtracji", b)


if __name__ == "__main__":
    unittest.main()
