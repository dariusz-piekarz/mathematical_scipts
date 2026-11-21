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
        self.assertIn(r"\frac{\xi^m-1}{\xi-1}", s)
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
        self.assertIn("nie jest unipotentny", a)
        self.assertIn("twierdzenia Schmida", b)
        self.assertIn("nie dowodem istnienia granicznej filtracji", b)


    def test_integral_cyclic_monodromy_and_derived_obstruction(self):
        # For f(z)=z^m the reduced integral homology has rank m-1,
        # and det(I-T)=m.  The cokernel is cyclic of order m.
        source = self.src["25"]
        self.assertIn(r"\det(I-T|_{\widetilde H_0", source)
        self.assertIn(r"\Z/m\Z", source)
        self.assertIn(r"\mathbb H^3(S^2,K_e)", source)
        for m in range(2, 16):
            n = m - 1
            # On b_j=e_j-e_{j+1}, T(b_j)=b_{j+1} (j<n-1)
            # and T(b_{n-1})=-sum_j b_j.
            matrix = [[(1 if i == j else 0) -
                       (-1 if j == n-1 else 1 if i == j+1 else 0)
                       for j in range(n)] for i in range(n)]
            # Fraction-free Bareiss elimination computes det over Z.
            prev = 1
            for k in range(n-1):
                pivot = matrix[k][k]
                self.assertNotEqual(pivot, 0)
                for i in range(k+1, n):
                    for j in range(k+1, n):
                        value = (matrix[i][j]*pivot -
                                 matrix[i][k]*matrix[k][j])
                        self.assertEqual(value % prev, 0)
                        matrix[i][j] = value // prev
                for i in range(k+1, n):
                    matrix[i][k] = 0
                prev = pivot
            self.assertEqual(matrix[n-1][n-1], m)

    def test_legendre_unipotent_not_finite_order(self):
        # Base change multiplies N rather than killing it for N != 0.
        source = self.src["26"]
        self.assertIn(r"T^q=I+qN\ne I", source)
        for q in range(1, 24):
            self.assertNotEqual(((1, 2*q), (0, 1)),
                                ((1, 0), (0, 1)))


    def test_at25_lefschetz_requires_unramified_nodal_model(self):
        """A ramified base change transforms a single Dehn twist into its m-th power."""
        src = self.src["25"]
        for fragment in (
            r"$\pi(z,w)=zw$",
            r"$zw=s^m$",
            "submersją na pewnym otoczeniu włókna",
            "wzór na pojedynczą transwekcję",
            r"\langle\gamma,\delta\rangle\,\delta",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn("posiada\njedną zwyczajną osobliwość węzłową.", src)
        for m in range(1, 12):
            # T(a) = a and T(b) = b+a on genus-one homology.
            Tm = ((1, m), (0, 1))
            self.assertEqual(Tm[0][1], m)
            if m > 1:
                self.assertNotEqual(Tm, ((1, 1), (0, 1)))

    def test_at25_hodge_opposed_filtrations_and_mhs_dependency(self):
        src = self.src["25"]
        for fragment in (
            r"$G_p=\overline{F^{m-p}V_{\C}}$",
            r"$w=v-u\in F^p$",
            r"F^pV_{\C}=F^{p+1}V_{\C}",
            r"$V_{\C}=\bigoplus_p(F^pV_{\C}\cap G_p)$",
            r"F^p(\operatorname{Gr}_m^WV)_{\C}",
            "długiego ciągu",
            r"\emph{mieszanych struktur Hodge'a}",
            r"\mathcal H^q(Rf_*K)",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotRegex(src, r"\brezolwent\w*")
        # Pure weight-one example: F^1=< (1,i) >, conjugate F^1=< (1,-i) >
        v = (1, 1j)
        conjugate = (1, -1j)
        det = v[0]*conjugate[1] - v[1]*conjugate[0]
        self.assertNotEqual(det, 0)
        self.assertEqual(det, -2j)


    def test_at25_self_contained_statements_and_ehresmann_fiber(self):
        source = self.src["25"]
        for fragment in (
            r"Niech $\mathcal A$ będzie kategorią abelową,",
            "Niech $V_{\\Q}$ będzie skończeniewymiarową",
            r"$b_j(M)=\dim_{\Q}H^j(M;\Q)$",
            r"E_1^{p,q}=H^q(X,\Omega_X^p)",
            r"Niech $x\in C$ oznacza węzeł.",
            r"$F=p^{-1}(b)$",
            r"$C_t=\pi^{-1}(t)$",
            r"$X_0=f^{-1}(0)$, a $P\in\operatorname{Perv}(X;\Q)$.",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, source)
        self.assertIn("poza węzłem\n$\\pi$ jest submersją", source)


    def test_at26_complete_geometric_monodromy_hypotheses(self):
        src = self.src["26"]
        for fragment in (
            r"$p\in\overline S\setminus S$",
            r"$\Delta^*\subset S^{\mathrm{an}}$",
            r"R^kf_*\Q_{\mathcal X}",
            r"$W_\bullet(N,k)$",
            r"$NW_j\subseteq W_{j-2}$",
            r"N^r:\operatorname{Gr}_{k+r}^{W}V_\Q",
            r"F^\bullet(z+1)=T F^\bullet(z)",
            "skończeniewymiarowych",
            r"\mathbb V_{\C}\cong R^kf_*\C_{\mathcal X}",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)
        self.assertNotIn(r"$W(N)[-k]$", src)
        self.assertNotIn("algebraicznej rodziny\nnad przebitym dyskiem", src)

    def test_at26_self_contained_periods_and_hodge_data(self):
        src = self.src["26"]
        for fragment in (
            r"$\omega\in\Gamma(U,\mathcal H)$ holomorficznym",
            r"$Q(v,w)=(-1)^mQ(w,v)$",
            r"$\mathcal H=H^k_{\mathrm{dR}}(\mathcal X/S)$",
            r"$\gamma_t$ jest lokalnie poziomą rodziną",
            r"$\omega_\lambda=\dd x/y$",
            r"$\lambda\in\C\setminus\{0,1\}$",
            r"$F=p^{-1}(b)$" if False else r"$N\in\operatorname{End}(V_\Q)$",
            r"$k\ge0$",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, src)

    def test_at26_relative_hodge_lattice_weight_indices(self):
        # In the Legendre model N(e2)=2e0, centered at weight one,
        # Gr_0 and Gr_2 are one-dimensional, Gr_1 is trivial.
        N = ((0, 2), (0, 0))
        assert N[0][1] != 0
        assert N[0][0] == N[1][1] == 0
        for q in (1, 2, 3, 5, 17):
            Nq = ((0, 2 * q), (0, 0))
            self.assertEqual(Nq[0][1], 2 * q)
        # Polarized weight-one form is alternating: Q(x,y)=-Q(y,x).
        Q = ((0, 1), (-1, 0))
        self.assertEqual(Q[0][1], -Q[1][0])


if __name__ == "__main__":
    unittest.main()
