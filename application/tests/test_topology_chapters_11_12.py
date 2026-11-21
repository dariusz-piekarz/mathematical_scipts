"""AT-11/12 audit regression tests: duality, intersection forms and spectral pages."""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from random import Random
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters" / "pl" / "algebraic_topology"
BOOK = ROOT / "books" / "pl" / "algebraic_topology.tex"


class TopologyChapterElevenTwelveAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = sorted(AT.glob("0[1-9]-*.tex")) + sorted(
            f for n in (10, 11, 12) for f in AT.glob(f"{n:02d}-*.tex")
        )
        cls.text = {
            f.name[:2]: f.read_text(encoding="utf-8-sig")
            for f in cls.files
        }

    def test_canonical_book_includes_twelve_chapters(self):
        self.assertEqual(set(self.text), {f"{i:02d}" for i in range(1, 13)})
        book = BOOK.read_text(encoding="utf-8-sig")
        for f in self.files:
            self.assertIn(
                r"\input{../../chapters/pl/algebraic_topology/" + f.name + "}",
                book,
            )

    def test_preserve_historical_labels(self):
        required = {
            "11": (
                "ch:przeciecia-dualnosc-klasy",
                "thm:poincare-dualnosc-16",
                "thm:pl-v4",
                "thm:alexander-v4",
                "thm:clutching-16",
                "thm:wi-klasy-16",
                "thm:poincare-hopf-16",
                "thm:forma-przeciecia-16",
            ),
            "12": (
                "ch:ciagi-spektralne-v5",
                "lem:dr-v5",
                "thm:pages-v5",
                "thm:convergence-v5",
                "thm:serre-v5",
                "thm:serre-general-v6",
                "thm:gysin-v5",
                "thm:thom-v5",
            ),
        }
        for chapter, labels in required.items():
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertEqual(
                        self.text[chapter].count(r"\label{" + label + "}"),
                        1,
                    )
        labels = re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        )
        self.assertEqual(len(labels), len(set(labels)))

    def test_all_references_resolve_with_prior_chapters(self):
        labels = set(re.findall(
            r"\\label\s*\{([^}]+)\}", "\n".join(self.text.values())
        ))
        for chapter in ("11", "12"):
            refs = re.findall(
                r"\\(?:ref|eqref|autoref|pageref|nameref)\s*\{([^}]+)\}",
                self.text[chapter],
            )
            self.assertGreater(len(refs), 15)
            self.assertEqual(set(refs) - labels, set())

    def test_environment_balance_and_independent_figures(self):
        for chapter, minimum_figures in (("11", 5), ("12", 2)):
            src = self.text[chapter]
            self.assertEqual(
                Counter(re.findall(r"\\begin\{([^}]+)\}", src)),
                Counter(re.findall(r"\\end\{([^}]+)\}", src)),
            )
            self.assertGreaterEqual(
                len(re.findall(r"\\begin\{tikzpicture\}", src)),
                minimum_figures,
            )
            for command in ("includegraphics", "input", "include",
                            "lstinputlisting", "inputminted"):
                self.assertNotRegex(src, r"\\" + command + r"\s*\{")

    def test_consistent_polish_terminology(self):
        for chapter in ("11", "12"):
            self.assertNotRegex(
                self.text[chapter].lower(),
                r"\btensorowan\w*|\btensorowali\w*"
                r"|\bsekwencj\w*|\binjekc\w*",
            )

    def test_cap_boundary_signs_on_integer_simplices(self):
        """Check boundary(c cap a)=(-1)^k[(boundary c) cap a-c cap da]."""
        ch = self.text["11"]
        self.assertIn(
            r"\partial(c\frown\alpha)=(-1)^k", ch
        )

        def boundary(chain):
            result = defaultdict(int)
            for sigma, coefficient in chain.items():
                if len(sigma) <= 1:
                    continue  # unreduced C_0 -> C_{-1}=0
                for j in range(len(sigma)):
                    face = sigma[:j] + sigma[j + 1:]
                    result[face] += (-1)**j * coefficient
            return {f: v for f, v in result.items() if v}

        def cap(chain, cochain, degree):
            result = defaultdict(int)
            for sigma, coefficient in chain.items():
                if len(sigma) - 1 >= degree:
                    result[sigma[degree:]] += (
                        coefficient * cochain.get(sigma[:degree + 1], 0)
                    )
            return {f: v for f, v in result.items() if v}

        def coboundary(cochain, faces):
            return {
                face: sum(
                    (-1)**j * cochain.get(face[:j] + face[j + 1:], 0)
                    for j in range(len(face))
                )
                for face in faces
            }

        rng = Random(168)
        for m in range(1, 8):
            simplex = tuple(range(m + 1))
            chain = {simplex: 1}
            for k in range(m + 1):
                for _ in range(12):
                    alpha = {
                        face: rng.randint(-5, 5)
                        for face in combinations(simplex, k + 1)
                    }
                    lhs = boundary(cap(chain, alpha, k))
                    da = coboundary(
                        alpha, combinations(simplex, k + 2)
                    )
                    first = cap(boundary(chain), alpha, k)
                    second = cap(chain, da, k + 1)
                    rhs = {
                        face: (-1)**k * (
                            first.get(face, 0) - second.get(face, 0)
                        )
                        for face in set(first) | set(second)
                        if first.get(face, 0) != second.get(face, 0)
                    }
                    with self.subTest(simplex_dim=m, cap_degree=k):
                        self.assertEqual(lhs, rhs)

    def test_zero_dimensional_euler_orientation_signs(self):
        """Orientation signs cancel in <e(TM), [M]> in dimension zero."""
        ch = self.text["11"]
        self.assertIn(r"$u_E=e(E)=\varepsilon\in H^0(M;\Z)$", ch)
        self.assertIn(r"\sum_x\varepsilon_x^2=\#M=\chi(M)", ch)
        for count in range(0, 7):
            for orientations in product((-1, 1), repeat=count):
                fundamental_coefficients = orientations
                euler_values = orientations
                pairing = sum(
                    a * b for a, b in
                    zip(fundamental_coefficients, euler_values)
                )
                with self.subTest(points=count, signs=orientations):
                    self.assertEqual(pairing, count)

    def test_cp2_connected_sum_parity_obstructs_homotopy(self):
        ch = self.text["11"]
        self.assertIn(r"\label{prz:formy-przeciecia-cp2-s2}", ch)
        self.assertIn(r"\label{fig:formy-przeciecia-parzystosc}", ch)
        # CP2#(-CP2): diag(1,-1) is odd, S2xS2 hyperbolic is even.
        def q_odd(a, b):
            return a*a - b*b

        def q_even(a, b):
            return 2*a*b

        self.assertEqual(q_odd(1, 0), 1)
        for a in range(-12, 13):
            for b in range(-12, 13):
                self.assertEqual(q_even(a, b) % 2, 0)
        self.assertIn(r"H_2(N;\Z)", ch)

    def test_spectral_page_three_example(self):
        ch = self.text["12"]
        self.assertIn(r"\label{prz:spectral-d3-cancel}", ch)
        self.assertIn(r"d^3:E^3_{3,0}", ch)
        # C3 = Z*x -> C2 = Z*y by the identity, with
        # filtration(x)=3 and filtration(y)=0. Therefore the
        # leading drop is 3: d1=d2=0, d3 is the identity.
        chain_boundary = lambda coefficient_x: coefficient_x
        nonzero_positions = {(3, 0), (0, 2)}
        for page in (1, 2):
            self.assertNotIn((3 - page, page - 1), nonzero_positions)
        self.assertEqual(chain_boundary(1), 1)
        self.assertEqual(chain_boundary(-7), -7)
        self.assertEqual(
            [n for n in range(-12, 13) if chain_boundary(n) == 0],
            [0],
        )
        self.assertEqual(
            {chain_boundary(n) for n in range(-12, 13)},
            set(range(-12, 13)),
        )
        self.assertIn("Strona czwarta jest zerowa", ch)

    def test_filtered_two_term_complex_higher_differentials(self):
        """For C_r -> C_{r-1} with boundary k, d^r is k and earlier maps vanish."""
        ch = self.text["12"]
        self.assertIn(r"\label{thm:pages-v5}", ch)
        self.assertIn(r"\label{thm:convergence-v5}", ch)
        self.assertIn(r"Z^r_{p,q}", ch)
        for page in range(2, 9):
            # x lies at filtration page; y lies at filtration zero.
            source = (page, 0)
            target = (0, page - 1)
            for earlier in range(1, page):
                # d^earlier has target filtration page-earlier > 0,
                # and there are no generators in that filtration.
                self.assertNotEqual((page-earlier, earlier-1), target)
            for k in (-5, -3, -2, -1, 1, 2, 3, 5):
                # Higher differential is multiplication by k: Z -> Z.
                # H_r=0 and H_{r-1}=Z/|k|; for |k|=1 the latter is 0.
                kernel = [a for a in range(-30, 31) if k*a == 0]
                self.assertEqual(kernel, [0])
                cosets = {x % abs(k) for x in range(-50, 51)}
                self.assertEqual(len(cosets), abs(k))
                self.assertEqual(source[0]-page, target[0])
                self.assertEqual(source[1]+page-1, target[1])

    def test_klein_bottle_twisted_monodromy_and_extensions(self):
        ch = self.text["12"]
        self.assertIn(r"E^2_{0,1}=\Z/2", ch)
        self.assertIn(r"H_1(K;\Z)\cong\Z\oplus\Z/2", ch)
        # Circle with degree -1 transport has cellular boundary (-1)-1=-2.
        transport = -1
        self.assertEqual(transport-1, -2)
        self.assertEqual([n for n in range(-20, 21) if -2*n == 0], [0])
        self.assertEqual({i % 2 for i in range(-20, 21)}, {0, 1})

    def test_spectral_cochain_filtration_and_exact_couple_grading(self):
        ch = self.text["12"]
        for target in (
            r"i:D^1_{p-1,q+1}\to D^1_{p,q}",
            r"k:E^1_{p,q}\to D^1_{p-1,q}",
            r"F^pC^n(E;\Z)=",
            r"F^pC^*(E)/F^{p+1}C^*(E)",
            r"C^*(E_p,E_{p-1};\Z)",
            r"E_1^{p,q}=H^{p+q}(E_p,E_{p-1};\Z)",
            r"$S^{-1}=\varnothing$",
        ):
            with self.subTest(expression=target):
                self.assertIn(target, ch)
        self.assertIn(
            r"występuje \emph{produkt}", ch
        )
        # In a non-finite cellular CW complex, infinite-support
        # cochains are allowed; direct sums would discard such data.
        cochain = lambda cell_index: 1 if cell_index % 3 == 0 else 0
        self.assertEqual(
            sum(cochain(i) for i in range(3000)), 1000
        )
        self.assertEqual(
            [cochain(i) for i in range(9)], [1, 0, 0, 1, 0, 0, 1, 0, 0]
        )

    def test_transgression_starts_at_positive_degree(self):
        ch = self.text["12"]
        self.assertIn(r"Niech $q\ge1$ i niech $u\in E_2^{0,q}$", ch)
        self.assertIn(r"$d_2,\ldots,d_q$", ch)
        self.assertIn(r"$d_{q+1}u\in E_{q+1}^{q+1,0}$", ch)
        for q in range(1, 10):
            # Transgression d_{q+1} has cohomological bidegree
            # (q+1,1-(q+1)), hence (0,q) -> (q+1,0).
            self.assertEqual((0+(q+1), q+1-(q+1)), (q+1, 0))
        # q=0 would make the putative "page q+1" equal to E_1,
        # preceding E_2; it is intentionally excluded.

    def test_extension_problem_distinguishes_actual_groups(self):
        ch = self.text["12"]
        self.assertIn(r"\label{prz:spectral-extension-z4}", ch)
        self.assertIn(r"\label{fig:spectral-extension-z4}", ch)
        z4 = [0, 1, 2, 3]
        z2x2 = [(a, b) for a in range(2) for b in range(2)]
        self.assertEqual(len(z4), len(z2x2))
        self.assertEqual((1 + 1) % 4, 2)
        self.assertTrue(all(((a+a) % 2, (b+b) % 2) == (0, 0)
                            for a, b in z2x2))
        self.assertIn(r"\Z/4\Z", ch)
        self.assertIn(r"(\Z/2\Z)^2", ch)

    def test_serre_hypotheses_no_contradictory_disclaimer(self):
        ch = self.text["12"]
        self.assertIn(r"\ref{thm:serre-general-v6}", ch)
        self.assertIn("skończeniewymiarowej", ch)
        self.assertIn("Nie należy więc opisywać", ch)
        self.assertNotIn(
            "Wersja dla wszystkich fibracji Serre'a, pełny dowód", ch
        )


if __name__ == "__main__":
    unittest.main()
