"""AT-17/18 audit regressions: Pontriagin–Thom, bordism and Morse homology.

Checks canonical source and theorem labels, tensor-algebra cross-volume links,
calculations of Stiefel–Whitney numbers and RP2 Morse differentials,
LaTeX environments and independence of local image/code resources.
Separate CI compiles the dependent AT-01–18 volume twice.
"""
from __future__ import annotations

from collections import Counter
from math import exp
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
DG = ROOT / "chapters" / "pl" / "differential_geometry_and_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologySeventeenEighteenAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in range(10, 19) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.text = {
            file.name[:2]: file.read_text(encoding="utf-8-sig")
            for file in cls.files
        }

    def test_book_loads_exactly_the_eighteen_prerequisites(self):
        self.assertEqual(set(self.text), {f"{i:02d}" for i in range(1, 19)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for file in self.files:
            with self.subTest(path=file.name):
                self.assertIn(
                    r"\input{../../chapters/pl/algebraic_topology/"
                    + file.name + "}", book
                )

    def test_preserve_historical_labels_and_no_duplicates(self):
        historical = {
            "17": (
                "ch:pt-v9", "lem:pt-regular-v9", "lem:pt-collapse-v9",
                "thm:pt-framed-v9", "cor:pt-stable-v9",
                "thm:pt-pd-v9", "cor:euler-zero-v9",
                "prop:bordism-group-v9", "ex:bordism-low-v9",
                "thm:sw-bdy-v9", "thm:omega2-v9",
                "prop:normal-class-v9", "thm:pt-MO-v9",
                "lem:thom-transversal-v9-audyt",
            ),
            "18": (
                "ch:morse-v10", "thm:morse-lemma-v10",
                "lem:morse-energy-v10", "prop:morse-dimension-v10",
                "thm:morse-compact-v10", "def:morse-complex-v10",
                "thm:morse-d2-v10", "thm:morse-handle-v10",
                "lem:morse-same-level-audit", "thm:morse-singular-v10",
                "thm:morse-inequalities-v10",
            ),
        }
        for chapter, names in historical.items():
            for label in names:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.text[chapter].count(r"\label{" + label + "}"), 1
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_references_resolve_inside_at_volume(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        ))
        for chapter in ("17", "18"):
            refs = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{([^}]+)\}",
                self.text[chapter],
            )
            self.assertGreater(len(refs), 4)
            self.assertFalse(set(refs) - labels, set(refs) - labels)

    def test_real_geometry_tensor_chapter_and_canonical_label_reused(self):
        source = (
            DG / "03-algebra-tensorowa-i-zewnetrzna.tex"
        ).read_text(encoding="utf-8-sig")
        for label in (
            "ch:algebra-tensorowa",
            "sec:iloczyn-tensorowy",
            "thm:tensor-hom",
        ):
            self.assertIn(r"\label{" + label + "}", source)
        for chapter in ("17", "18"):
            self.assertIn("03-algebra-tensorowa-i-zewnetrzna.tex", self.text[chapter])
            self.assertIn(r"\href{https://github.com/", self.text[chapter])
        self.assertIn(r"thm:tensor-hom", self.text["17"])
        self.assertIn(r"sec:iloczyn-tensorowy", self.text["18"])
        morse = (
            DG / "18-teoria-morse-a-punkty-krytyczne-uchwyty-i-przeplyw.tex"
        ).read_text(encoding="utf-8-sig")
        cobordism = (
            DG / "19-kobordyzmy-i-rachunek-uchwytow.tex"
        ).read_text(encoding="utf-8-sig")
        self.assertIn(r"\label{ch:teoria-morsea}", morse)
        self.assertIn(r"\label{ch:rachunek-uchwytow}", cobordism)

    def test_no_external_graphic_or_source_dependencies(self):
        for chapter, min_figs in (("17", 2), ("18", 2)):
            src = self.text[chapter]
            begin = Counter(re.findall(r"\\begin\{([^}]+)\}", src))
            end = Counter(re.findall(r"\\end\{([^}]+)\}", src))
            self.assertEqual(begin, end)
            self.assertGreaterEqual(begin["tikzpicture"], min_figs)
            for cmd in (
                "includegraphics", "input", "include",
                "lstinputlisting", "inputminted",
            ):
                self.assertNotRegex(src, r"\\" + cmd + r"\s*\{")

    def test_approved_polish_terms(self):
        for chapter in ("17", "18"):
            self.assertNotRegex(
                self.text[chapter].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekcj\w*|\bseskwilini\w*",
            )

    def test_pontriagin_thom_mapping_grammar_regressions(self):
        """Prevent malformed inflections caused by replacing 'mapa' with 'odwzorowanie'."""
        source = self.text["17"]
        for forbidden in (
            r"odwzorowań[ęą]",
            r"\bmapami\b",
            r"otrzymana odwzorowanie",
            r"przybliżona odwzorowanie",
            r"odwzorowanie pozostaje zatem niezmieniona",
            r"odwzorowanie .* jest homotopijna",
        ):
            with self.subTest(pattern=forbidden):
                self.assertNotRegex(source, forbidden)
        self.assertIn("ciągłym (a nawet gładkim) odwzorowaniem", source)
        self.assertIn("przestrzenią docelową jest", source)
        self.assertIn("homotopijne z odwzorowaniem stałym", source)

    def test_product_of_projective_planes_is_nonneutral_in_bordism(self):
        chapter = self.text["17"]
        self.assertIn(r"\label{prz:bordism-rp2-product}", chapter)
        self.assertIn(r"\label{fig:bordism-rp2-product}", chapter)
        self.assertIn(r"\langle w_2(TX)^2,[X]_2\rangle=1", chapter)
        self.assertIn(r"\langle w_4(TX),[X]_2\rangle=1", chapter)
        # Multiply w2=a²+ab+b² with itself in F2[a,b]/(a³,b³).
        w2 = {(2, 0), (1, 1), (0, 2)}
        square = set()
        for i, j in w2:
            for k, l in w2:
                mon = (i + k, j + l)
                if mon[0] >= 3 or mon[1] >= 3:
                    continue
                if mon in square:
                    square.remove(mon)
                else:
                    square.add(mon)
        self.assertEqual(square, {(2, 2)})
        self.assertIn(r"2[X]=0", chapter)

    def test_rp4_has_same_euler_parity_but_distinct_bordism(self):
        chapter = self.text["17"]
        self.assertIn(r"\label{prz:bordism-rp4-versus-rp2-square}", chapter)
        self.assertIn(r"w(TY)=(1+t)^5=1+t+t^4", chapter)
        # Two SW-number vectors (w2²,w4) are linearly independent over F2.
        x = (1, 1)
        y = (0, 1)
        self.assertEqual((x[0]*y[1] - x[1]*y[0]) % 2, 1)
        self.assertEqual(sum([1, -1, 1]), 1)  # chi(RP4)=1
        self.assertEqual(1 * 1, 1)  # chi(RP2×RP2)=1

    def test_pt_basepoint_and_relative_transversality_are_justified(self):
        source = self.text["17"]
        for token in (
            r"$Q_+\to S^k$",
            r"punktowaną sferą $(S^{n+k},\infty)$",
            "w zmiennej czasu na kołnierzach końców",
            r"$\{\infty\}\times[0,1]$",
            "produktowym przy obu końcach",
            r"\label{thm:pt-framed-v9}",
        ):
            with self.subTest(token=token):
                self.assertIn(token, source)
        self.assertNotIn("Iteracja X, rozdział XVIII", source)

    def test_projective_tangent_characteristic_numbers_in_low_dimensions(self):
        """w(T RP^n)=(1+t)^(n+1), with degree truncated at n."""
        from math import comb
        source = self.text["17"]
        self.assertIn(r"w(T\R P^2)=(1+t)^3=1+t+t^2", source)
        self.assertIn(r"w(TY)=(1+t)^5=1+t+t^4", source)
        for n in range(1, 33):
            top_stiefel_whitney = comb(n+1, n) % 2
            cell_euler_characteristic = sum((-1)**j for j in range(n+1))
            with self.subTest(dimension=n):
                self.assertEqual(
                    top_stiefel_whitney, cell_euler_characteristic % 2
                )
        # In RP^4, compute w2 and w4 from (1+t)^5.
        w_rp4 = [comb(5, i) % 2 for i in range(5)]
        rp4 = (w_rp4[2] ** 2 % 2, w_rp4[4])
        self.assertEqual(rp4, (0, 1))

        # In RP^2 x RP^2, compute the homogeneous w2 and w4
        # from (1+a)^3(1+b)^3 modulo (a^3,b^3).
        def poly_degree(d):
            return {
                (i, d-i): (comb(3, i) * comb(3, d-i)) % 2
                for i in range(3) if 0 <= d-i <= 2
            }
        w2 = poly_degree(2)
        w4 = poly_degree(4)
        square = 0
        for (i,j), first in w2.items():
            for (u,v), second in w2.items():
                if i+u == 2 and j+v == 2:
                    square ^= first * second
        product = (square, w4[(2,2)])
        self.assertEqual(product, (1, 1))
        self.assertEqual(
            (product[0]*rp4[1] - product[1]*rp4[0]) % 2, 1
        )

    def test_pt_euler_zeros_dimensions_and_exact_references(self):
        source = self.text["17"]
        for fragment in (
            r"Niech $m\ge1$ i $1\le k\le m$.",
            r"Dla $k>m$ zbiór $Z(s)$ jest pusty",
            r"$e(\xi)=0$ w $H^k(Q;\Z)$",
            r"$n\ge0$, $k\ge1$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, source)
        self.assertNotRegex(
            source,
            r"\bmapa\b|\bmapy\b|\bmapę\b|\bmapą\b",
        )
        for chapter in ("17", "18"):
            src = self.text[chapter]
            starts = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{", src
            )
            closed = re.findall(
                r"\\(?:ref|eqref|pageref|autoref|nameref)\s*\{[^{}\n]+\}",
                src,
            )
            self.assertEqual(
                len(starts), len(closed),
                f"Malformed reference in TOP-{chapter}",
            )

    def test_projective_morse_quadratic_flow_is_descending(self):
        chapter = self.text["18"]
        self.assertIn(r"\label{prz:morse-rp2-torsja}", chapter)
        self.assertIn(r"\label{fig:morse-rp2-torsja}", chapter)
        lambdas = (-1.0, 0.0, 3.0)
        x = (0.3, -0.5, 0.8)

        def value(time):
            weights = [exp(-4 * l * time) * y*y
                       for l, y in zip(lambdas, x)]
            return sum(l * w for l, w in zip(lambdas, weights)) / sum(weights)

        self.assertLess(value(0.5), value(0))
        self.assertLess(value(0), value(-0.5))
        self.assertIn(r"\lambda(p_i)=i", chapter)

    def test_morse_compactification_quantifiers_and_handle_extremes(self):
        chapter = self.text["18"]
        for fragment in (
            r"$p,q,r\in\operatorname{Crit}(f)$",
            r"$\lambda(a)-\lambda(b)-1\ge0$",
            "dokładnie jeden punkt pośredni",
            r"$D^0=\{*\}$ i $S^{-1}=\varnothing$",
            r"Dla $k=0$ dołącza się więc nową składową",
            r"o wymiarze $n\ge0$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, chapter)
        for total_index_drop in (1, 2):
            middle = [
                index for index in range(11)
                if 10 > index > 10-total_index_drop
            ]
            self.assertEqual(
                middle, [] if total_index_drop == 1 else [9]
            )

    def test_morse_theorem_hypotheses_are_self_contained(self):
        """Critical points, dimensions and flow parameters are explicit in statements."""
        chapter = self.text["18"]
        for fragment in (
            r"o wymiarze $n\ge0$",
            r"$\lambda\in\{0,\ldots,n\}$",
            r"$\Phi$ przepływem",
            r"Dla każdego $p\in\operatorname{Crit}(f)$",
            r"Jeśli $p,q\in\operatorname{Crit}(f)$",
            r"Dla różnych $p,q\in\operatorname{Crit}(f)$",
            r"$\mathcal M(p,q)=(W^u(p)\cap W^s(q))/\R$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, chapter)

    def test_morse_projective_trajectory_orientation_at_two_intersections(self):
        """Independent signs at both intersections with f=c in RP^2."""
        import math
        chapter = self.text["18"]
        self.assertIn(r"n(p_2,p_1)=-2", chapter)
        self.assertIn(r"n(p_1,p_0)=0", chapter)
        for eigenvalues in ((-1.0, 0.0, 3.0), (1.0, 5.0, 9.0),
                            (-8.0, -3.0, -1.0)):
            l0,l1,l2 = eigenvalues
            for step in range(1, 40):
                c = l1 + (l2-l1)*step/40
                radius = math.sqrt((l2-c)/(c-l1))
                signs = []
                for v in (-radius, radius):
                    # Flow increases v when u=0: v_dot > 0 for v>0.
                    # Positive transversal for orientation
                    # (flow, transversal) on W^u(p2) is -sgn(v) du.
                    transverse_u = -1 if v > 0 else 1
                    # The oriented normal to W^s(p1) is da=du/v.
                    orientation = transverse_u / v
                    signs.append(-1 if orientation < 0 else 1)
                self.assertEqual(signs, [-1,-1])
                self.assertEqual(sum(signs), -2)

    def test_morse_rational_inequality_polynomials(self):
        """m(t)-b(t) = (1+t)Q(t) for three concrete chain complexes."""
        # S^2 height: C0=Z, C1=0, C2=Z; all boundaries zero.
        # RP^2:    C0=C1=C2=Z; d2=2, d1=0 (rational rank 1).
        # S^1 with four critical points: C0=C1=Z^2, rank d1=1.
        examples = [
            ((1,0,1), (1,0,1), (0,0,0)),
            ((1,1,1), (1,0,0), (0,1,0)),
            ((2,2,0), (1,1,0), (1,0,0)),
        ]
        for m,b,quotient in examples:
            with self.subTest(m=m):
                reconstructed = [
                    quotient[k] + (quotient[k-1] if k else 0)
                    for k in range(len(m))
                ]
                self.assertEqual(
                    list(map(lambda ab: ab[0]-ab[1], zip(m,b))),
                    reconstructed,
                )
                self.assertEqual(
                    sum((-1)**k*m[k] for k in range(len(m))),
                    sum((-1)**k*b[k] for k in range(len(b))),
                )

    def test_morse_orientations_are_in_definition_and_terms_are_standard(self):
        chapter = self.text["18"]
        for fragment in (
            r"orientację $W^u(p)$",
            r"Dla $k\in\Z$ niech $CM_k(f,g)$",
            "pustą grupą dla indeksów niewystępujących",
            "dla wszystkich $k\in\Z$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, chapter)
        self.assertNotRegex(
            chapter,
            r"\bmapa\b|\bmapy\b|\bmapą\b|\bmapę\b"
            r"|\bsekwencj\w*|\btensorowan\w*",
        )
        self.assertNotIn("Iteracja X, rozdział XIX", chapter)

    def test_morse_rp2_integral_torsion_calculation(self):
        chapter = self.text["18"]
        self.assertIn(r"\partial_2=2", chapter)
        self.assertIn(r"\partial_1=0", chapter)
        self.assertRegex(chapter, r"HM_1=[^\n]*\\cong\\Z/2\\Z")
        # 0 -> Z --2--> Z --0--> Z -> 0 gives H2=0, H1=Z/2, H0=Z.
        kernel_d2 = [n for n in range(-50, 51) if 2*n == 0]
        self.assertEqual(kernel_d2, [0])
        self.assertEqual({2*k for k in range(-50, 51)} & {1, 3, 5}, set())
        self.assertEqual({(2*k) % 2 for k in range(-50, 51)}, {0})

    def test_morse_rationalization_is_explicit_and_nonredundant(self):
        chapter = self.text["18"]
        self.assertIn(r"CM_*(f,g)\otimes_{\Z}\Q", chapter)
        self.assertIn(r"\Q$ jest płaskim $\Z$-modułem", chapter)
        self.assertIn(r"HM_k(f,g)\otimes_{\Z}\Q", chapter)
        self.assertNotIn("Tensorujmy", chapter)


if __name__ == "__main__":
    unittest.main()
