import unittest
from pathlib import Path
from fractions import Fraction

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex"

class TestChapter15B(unittest.TestCase):
    def test_latex_relations(self):
        source = SOURCE.read_text(encoding="utf-8")
        for relation in (r"u_n\to f", r"s_n\to f", r"f(s)\ne0"):
            self.assertIn(relation, source)
        self.assertNotIn("u_n\t" + "o f", source)
        self.assertNotIn("s_n\t" + "o f", source)
        self.assertNotIn("f(s)\n" + "e0", source)

    def test_diagonal_error_budget(self):
        for n in range(1, 20):
            tail = sum((Fraction(1, 2**k) for k in range(n, 40)), Fraction(0))
            self.assertLess(tail, Fraction(1, 2**(n-1)))
        self.assertIn("Borela--Cantellego daje", SOURCE.read_text(encoding="utf-8"))


    def test_fubini_rectangular_vector_integral(self):
        # Exact finite-atomic Bochner integral on a product space.
        mu = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        nu = [Fraction(2, 5), Fraction(3, 5)]
        f = [
            [(Fraction(1, 3), Fraction(-2, 5)), (Fraction(-1), Fraction(3))],
            [(Fraction(2), Fraction(1, 4)), (Fraction(-3, 2), Fraction(2))],
            [(Fraction(-2, 7), Fraction(1)), (Fraction(1, 3), Fraction(-1))],
        ]

        def vecsum(weighted):
            weighted = tuple(weighted)
            return tuple(sum((w * v[k] for w, v in weighted), Fraction(0))
                         for k in range(2))

        by_s = vecsum(
            (mu[i], vecsum((nu[j], f[i][j]) for j in range(len(nu))))
            for i in range(len(mu))
        )
        by_t = vecsum(
            (nu[j], vecsum((mu[i], f[i][j]) for i in range(len(mu))))
            for j in range(len(nu))
        )
        product = vecsum(
            (mu[i] * nu[j], f[i][j])
            for i in range(len(mu)) for j in range(len(nu))
        )
        self.assertEqual(product, (Fraction(-53, 210), Fraction(61, 50)))
        self.assertEqual(by_s, product)
        self.assertEqual(by_t, product)

    def test_vector_measure_variation_on_finite_atoms(self):
        # X=R^2 with l1 norm; variation of a Bochner density.
        mu = [Fraction(1, 2), Fraction(1, 4),
              Fraction(1, 8), Fraction(1, 8)]
        f = [(Fraction(3), Fraction(-4)),
             (Fraction(-1), Fraction(1, 2)),
             (Fraction(2), Fraction(0)),
             (Fraction(0), Fraction(-6))]

        def norm(v):
            return abs(v[0]) + abs(v[1])

        def m(indices):
            return tuple(sum((mu[i] * f[i][k] for i in indices), Fraction(0))
                         for k in range(2))

        def partitions(items):
            if not items:
                yield []
                return
            x, *rest = items
            for partition in partitions(rest):
                yield [[x]] + partition
                for j in range(len(partition)):
                    new = [block[:] for block in partition]
                    new[j].append(x)
                    yield new

        for mask in range(1 << len(mu)):
            atoms = [i for i in range(len(mu)) if mask & (1 << i)]
            value = max(
                (sum((norm(m(block)) for block in partition), Fraction(0))
                 for partition in partitions(atoms)),
                default=Fraction(0),
            )
            integral_norm = sum((mu[i] * norm(f[i]) for i in atoms), Fraction(0))
            self.assertEqual(value, integral_norm)

    def test_variation_lemma_and_fubini_cross_sections_present(self):
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn(r"\label{prop:variation-measure15b}", source)
        self.assertIn("przekroje\n$N$ mają miarę zero", source)
        self.assertIn(r"\int_S\sum_{n=1}^\infty", source)


    def test_dunford_and_gelfand_theorems_are_self_contained(self):
        source = SOURCE.read_text(encoding="utf-8")
        for label, symbols in (
            ("thm:dunford-closedgraph15b", ("$f:S", "$x'\circ f", "$D_A(x')", r"\in X''")),
            ("thm:gelfand-exists15b", ("$f:S", "$g_A(y)", "$Y'$", r"\sigma(Y',Y)")),
        ):
            start = source.index(r"\label{" + label + "}")
            end = source.index(r"\end{twierdzenie}", start)
            statement = source[start:end]
            self.assertIn(r"$(S,\Sigma,\mu)$", statement)
            self.assertIn(r"$\K\in\{\R,\C\}$", statement)
            for symbol in symbols:
                self.assertIn(symbol, statement)
        self.assertNotIn("Przy założeniach powyższej definicji", source)
        self.assertNotIn("Przy założeniach definicji", source)
        self.assertIn(r"Całka Dunforda w $X''$ poza $J_X(X)$", source)


    def test_audit06_proof_details(self):
        # Source contracts, not a formal proof of the general theorems.
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            r"Jeżeli $Y=\{0\}$",
            "więc jest silnie mierzalna",
            "rozłączne prostokąty",
            "malejące",
            "Twierdzenie o klasie",
            r"$q_n<s<r_n$",
            r"$f(s)(s)=0$ i $f(s)(s)=1$",
        ):
            self.assertIn(fragment, source)


    def test_audit07_representative_and_counterexamples(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\bigcap_{k\\ge1}\\bigcup_{M\\ge1}\\bigcap_{i,j\\ge M}",
            "Jeżeli $X\\ne\\{0\\}$",
            "sumę Riemanna równą $x_0$",
            "$D_A\\in J_X(X)$ dla każdego $A\\in\\Sigma$",
            "g_S-\\sum_{n=1}^N g_{\\{n\\}}=g_{A_{N+1}}",
            "$\\mu$. Dla parami rozłącznych $A_n$ zachodzi",
            "addytywność przeliczalną w normie. Zatem $m$ jest miarą",
        ):
            self.assertIn(fragment, source)


    def test_audit08_explicit_hypotheses(self):
        source = SOURCE.read_text(encoding="utf-8")
        for label in (
            "thm:pettis-meas15b", "thm:bochner-criterion15b",
            "thm:bochner-dct15b", "thm:bochner-fubini15b",
            "prop:riemann-bochner15b", "thm:dunford-closedgraph15b",
            "thm:hierarchy-integrals15b", "thm:pettis-convergence15b",
            "thm:gelfand-exists15b", "prop:variation-measure15b",
            "thm:bochner-measure15b",
        ):
            start = source.index(r"\label{" + label + "}")
            end = source.index(r"\end{", start)
            self.assertIn(r"\K\in\{\R,\C\}", source[start:end])


    def test_audit09_definitions_and_construction(self):
        source = SOURCE.read_text(encoding="utf-8")
        for label in (
            "def:measurability15b", "def:bochner15b", "def:dunford-pettis15b",
            "def:gelfand15b", "def:vector-measure15b", "def:rnp15b",
        ):
            start = source.index(r"\label{" + label + "}")
            end = source.index(r"\end{definicja}", start)
            self.assertIn(r"\K\in\{\R,\C\}", source[start:end])
        for fragment in (
            "J_X(x)(x')=x'(x)",
            "nie klasy równoważności",
            "niezależność tej sumy od przedstawienia",
            "nazywamy całkowalną w sensie Dunforda",
            "jednoznacznie wyznaczony",
            "Całka Pettisa jest liniowa",
            "miara wektorowa $m$ rozszerza się na uzupełnienie",
            "$|\\bar m|(S)=|m|(S)<\\infty$",
        ):
            self.assertIn(fragment, source)


    def test_audit10_completion_and_total_integral(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "$D_{S_*}=0\\in J_{c_0}(c_0)$",
            "$D_A=(1/2,1/2,\\ldots)\\notin J_{c_0}(c_0)$",
            "C_j=B_j\\setminus\\bigcup_{i<j}B_i",
            "$\\bar m(\\bigcup_j A_j)=\\sum_j m(C_j)=\\sum_j\\bar m(A_j)$",
            "$|\\bar m|(S)=|m|(S)<\\infty$",
            "względem pierwotnej miary",
            "a silna mierzalność $Tf$ wynika",
        ):
            self.assertIn(fragment, source)


    def test_strongly_measurable_pettis_not_bochner(self):
        source = SOURCE.read_text(encoding="utf-8")
        start = source.index(r"\label{ex:pettis-strong-not-bochner15b}")
        end = source.index(r"\end{przyklad}", start)
        example = source[start:end]
        for fragment in (
            "f(n)=\\frac{2^n}{n}e_n",
            "s_N(k)=f(k)",
            "\\sum_{n=1}^{\\infty}\\frac{|a_n|}{n}",
            "v_A=(\\chi_A(n)/n)_{n\\ge1}",
            "\\langle v_A,a\\rangle=x'(v_A)",
            "\\sum_{n=1}^{\\infty}\\frac1n=\\infty",
        ):
            self.assertIn(fragment, example)
        # Finite truncations: verify the representing vector coordinatewise.
        for subset in (set(), {1, 3, 7}, set(range(1, 33))):
            a = [Fraction((-1)**n, n + 1) for n in range(1, 33)]
            scalar_integral = sum(
                (Fraction(1, 2**n) * Fraction(2**n, n) * a[n-1]
                 for n in subset), Fraction(0))
            v = [Fraction(1, n) if n in subset else Fraction(0)
                 for n in range(1, 33)]
            self.assertEqual(scalar_integral,
                             sum((x*y for x, y in zip(v, a)), Fraction(0)))
        # Dyadic blocks separate the harmonic and square-summable series.
        for k in range(1, 9):
            block = range(2**k, 2**(k+1))
            self.assertGreaterEqual(sum(Fraction(1, n) for n in block),
                                    Fraction(1, 2))
            self.assertLessEqual(sum(Fraction(1, n*n) for n in block),
                                 Fraction(1, 2**k))


    def test_pettis_vector_measure_infinite_variation(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\label{ex:pettis-infinite-variation15b}",
            "\\hyperref[ex:pettis-strong-not-bochner15b]",
            "\\sum_{n=1}^{\\infty}\\frac{\\chi_{B_N}(n)}{n^2}",
            "|m|(A)=\\sum_{n\\in A}\\frac1n",
            "|m|(S)=\\sum_{n\\ge1}1/n=\\infty",
        ):
            self.assertIn(fragment, source)
        # On finite sets the singleton partition attains the upper bound.
        # Compare squared norms to avoid irrational arithmetic.
        for mask in range(1 << 8):
            atoms = [n for n in range(1, 9) if mask & (1 << (n-1))]
            singleton_sum = sum((Fraction(1, n) for n in atoms), Fraction(0))
            norm_squared = sum((Fraction(1, n*n) for n in atoms), Fraction(0))
            self.assertLessEqual(norm_squared, singleton_sum**2)
            for cut in range(9):
                first = [n for n in atoms if n <= cut]
                tail = [n for n in atoms if n > cut]
                self.assertEqual(
                    norm_squared,
                    sum((Fraction(1, n*n) for n in first + tail), Fraction(0)))
                self.assertEqual(
                    singleton_sum,
                    sum((Fraction(1, n) for n in first + tail), Fraction(0)))
        # Every dyadic block contributes at least 1/2 to variation,
        # but its squared norm contributes at most 2**(-k).
        for k in range(1, 9):
            block = range(2**k, 2**(k+1))
            self.assertGreaterEqual(sum(Fraction(1, n) for n in block),
                                    Fraction(1, 2))
            self.assertLessEqual(sum(Fraction(1, n*n) for n in block),
                                 Fraction(1, 2**k))


    def test_extended_vector_integral_properties(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\label{thm:vector-integral-multipliers15b}",
            "D_A(Tf)=T''D_A(f)",
            "G_A(R'h)=R'G_A(h)",
            "\\sigma(X'',X')",
            "\\label{thm:orlicz-pettis15b}",
            "\\|\\sum_{n\\in H}u_n\\|\\le2\\varepsilon/3",
            "\\label{thm:pettis-vector-measure15b}",
            "\\|m_f\\|_{\\mathrm{sv}}(A)=q_f(A)",
            "q_f(A)\\le4p(A)",
            "\\mu(A_n\\triangle A)\\to0",
            "G_A(h)=J_Y' D_A(h)",
            "\\Phi(e_n)=0",
            "\\Phi((1,1,\\ldots))=1",
        ):
            self.assertIn(fragment, source)
        # For the atomic ell2 example, the squared semivariation of
        # a finite set A equals sum_{n in A} 1/n^2 by Cauchy-Schwarz.
        # The unit-ball extremizer is proportional to (chi_A(n)/n).
        for atoms in ({1}, {2, 3, 7}, set(range(1, 17))):
            squared = sum((Fraction(1, n*n) for n in atoms), Fraction(0))
            pairing = sum((Fraction(1, n)*Fraction(1, n)
                           for n in atoms), Fraction(0))
            self.assertEqual(pairing**2 / squared, squared)
            self.assertLessEqual(squared,
                sum((Fraction(1, n) for n in atoms), Fraction(0))**2)
            for cut in range(1, 17):
                tail = sum((Fraction(1, n*n) for n in atoms if n > cut),
                           Fraction(0))
                self.assertLessEqual(tail, Fraction(1, cut))
        # A weak-star sum in ell-infinity need not converge in norm.
        for size in range(2, 20):
            prefix = [1]*(size-1) + [0]
            self.assertEqual(max(abs(1-v) for v in prefix), 1)


    def test_vector_integral_convergence_distinctions(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\label{thm:vector-integral-convergence15b}",
            "q_{f_n-f}(S)\\to0",
            "r_{h_n-h}(S)\\to0",
            "\\|e_n\\|=1",
            "=\\left(\\sum_{n\\in A}\\frac1{n^2}\\right)^{1/2}",
        ):
            self.assertIn(fragment, source)
        # For constant functions on a one-atom probability space,
        # scalar evaluations of e_n tend to zero but norm is one.
        for n in range(1, 65):
            coefficient = Fraction(1, n*n)
            self.assertEqual(coefficient, Fraction(1, n)**2)
            self.assertLessEqual(coefficient, Fraction(1, n))
            self.assertEqual(sum(int(j == n) for j in range(1, 65)), 1)


    def test_weak_fubini_section_conditions(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\label{thm:gelfand-fubini15b}",
            "\\label{thm:dunford-fubini15b}",
            "\\label{thm:pettis-fubini15b}",
            "\\label{prop:weak-fubini-separable15b}",
            "\\label{ex:weak-fubini-failure15b}",
            "\\int_A^{\\mathrm G}U_B\\,\\mathrm d\\mu",
            "D_C(F_B)=D_{C\\times B}(f)",
            "f(s,t)=k(t)e_s",
            "C_a\\times T",
            "\\int_T k\\,\\mathrm d\\lambda=\\infty",
        ):
            self.assertIn(fragment, source)
        # Finite atomic scalarization: both iterated sums agree.
        mu = [Fraction(1, 3), Fraction(2, 3)]
        nu = [Fraction(1, 4), Fraction(3, 4)]
        f = [[Fraction(1, 2), Fraction(-2)],
             [Fraction(3), Fraction(4, 3)]]
        direct = sum(mu[i]*nu[j]*f[i][j]
                     for i in range(2) for j in range(2))
        self.assertEqual(direct, sum(mu[i]*sum(nu[j]*f[i][j]
                           for j in range(2)) for i in range(2)))
        self.assertEqual(direct, sum(nu[j]*sum(mu[i]*f[i][j]
                           for i in range(2)) for j in range(2)))
        # For k(t)=1/t every dyadic interval contributes at
        # least 1/2 to its integral: length times minimum.
        for n in range(12):
            length = Fraction(1, 2**(n+1))
            minimum = 2**n
            self.assertEqual(length*minimum, Fraction(1, 2))


    def test_audit18_common_exception_and_norm_measurability(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\|h(s,t)\\|=\\sup_k|h(s,t)(y_k)|",
            "\\|y_{k_j}-y/\\|y\\|\\|<1/j",
            "h(s,t)(x')=x'(f(s,t))",
            "$4\\varepsilon/3$",
            "przedstawiciela klasy",
            "mierzalnym zbiorze miary zero. Twierdzenie Tonellego",
        ):
            self.assertIn(fragment, source)


    def test_vitali_weak_and_uniform_conditions(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\label{def:uniform-integrability15b}",
            "\\label{lem:scalar-vitali15b}",
            "\\label{thm:weak-vitali15b}",
            "\\label{thm:uniform-vitali15b}",
            "q_{f_n-f}(S)\\to0",
            "2M(E_{n,x'})+\\eta\\mu(S)",
            "D_A(f)\\in J_X(X)",
            "\\label{cor:bochner-vitali15b}",
            "\\sup_{\\|x'\\|\\le1}\\mu(\\{|x'(f_n)|>1/2\\})=1",
            "\\mu(A)=2^{-k}\\to0",
        ):
            self.assertIn(fragment, source)
        # In c0 the scalar-integrability tail does not vanish
        # uniformly on the dual unit ball: each singleton contributes 1.
        for k in range(1, 21):
            self.assertEqual(Fraction(1, 2**k)*2**k, 1)
        # Uniform scalar absolute continuity without a common integrable
        # majorant is possible: disjoint atoms of masses 2^-k,
        # with integrals 1/k for the individual functions.
        for k in range(1, 21):
            self.assertEqual(Fraction(1, 2**k)*Fraction(2**k, k),
                             Fraction(1, k))

if __name__ == "__main__":
    unittest.main()
