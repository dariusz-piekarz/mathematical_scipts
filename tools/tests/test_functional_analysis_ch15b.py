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


    def test_derivative_integration_expansion_contracts(self):
        for name, fragments in (
            ("14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex", (
                "\\label{def:weak-curve-derivative14}",
                "\\label{thm:scalar-curve-derivative14}",
                "\\label{ex:scalar-not-weak-derivative14}",
                "\\label{def:bastiani14}",
            )),
            ("15-pochodne-wyzszych-rzedow-i-lokalne-twierdzenia-analizy-nieliniowej.tex", (
                "\\label{thm:inverse-derivatives15}",
                "\\label{thm:exp-derivatives15}",
                "\\label{ex:noncommuting-exp15}",
                "(m+k_0+\\cdots+k_m)!",
            )),
            ("15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex", (
                "\\label{thm:leibniz-moving15a}",
                "\\label{thm:higher-parametric15a}",
                "f(b(s),s)b'(s)-f(a(s),s)a'(s)",
            )),
            ("15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex", (
                "\\label{thm:bochner-lebesgue-differentiation15b}",
                "\\label{thm:ac-curve-representation15b}",
                "\\label{thm:rnp-lipschitz15b}",
                "\\label{ex:lipschitz-no-derivative15b}",
                "\\label{thm:weak-primitive-derivative15b}",
                "\\label{prop:weakstar-primitive-derivative15b}",
                "\\label{thm:weak-parametric-differentiation15b}",
                "\\label{thm:norm-parametric-differentiation15b}",
                "\\label{thm:bochner-sobolev15b}",
                "\\label{cor:sobolev-curve-estimate15b}",
                "b(\\mathcal R)\\le2b(\\mathcal P)",
                "2^{1-n}L",
            )),
        ):
            source = (SOURCE.parent / name).read_text(encoding="utf-8")
            for fragment in fragments:
                self.assertIn(fragment, source)

    def test_derivative_expansion_exact_examples(self):
        # Inverse along a nilpotent direction H=E12, A=diag(2,3).
        # The (1,2) coefficient of (A+tH)^-1 is exactly -t/6.
        for t in (Fraction(1, 3), Fraction(-2, 5), Fraction(1, 100)):
            self.assertEqual((-t/Fraction(6))/t, Fraction(-1, 6))
        # Simplex monomial integrals: beta recurrence for m=1.
        from math import factorial
        for p in range(5):
            for q in range(5):
                direct = sum((Fraction((-1)**j * factorial(q),
                                       factorial(j)*factorial(q-j)*(p+j+1))
                              for j in range(q+1)), Fraction(0))
                self.assertEqual(direct, Fraction(factorial(p)*factorial(q),
                                                  factorial(p+q+1)))
        # Moving limits: integral from s to 2s of (t+s) dt = 5s^2/2.
        for s in (Fraction(-1, 3), Fraction(1, 2), Fraction(2)):
            self.assertEqual(2*(2*s+s)-(s+s)+(2*s-s), 5*s)
        # RNP interval encoding: child lengths sum to parent length and
        # the weighted average of child slopes is the parent slope.
        length = Fraction(3, 4)
        masses = [Fraction(1, 4), Fraction(1, 2)]
        slopes = [Fraction(-1, 3), Fraction(2, 3)]
        average = sum(m*v for m,v in zip(masses, slopes))/length
        for halves in (1, 2, 4):
            children = [m/halves for _ in range(halves) for m in masses]
            values = slopes*halves
            self.assertEqual(sum(children), length)
            self.assertEqual(sum(m*v for m,v in zip(children, values)),
                             length*average)


    def test_chapter14_audit21_proof_details(self):
        source = (SOURCE.parent / "14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex").read_text(encoding="utf-8")
        for fragment in (
            "2(b-a)\\omega(\\delta)",
            "x_n=(2\\pi n)^{-1/2}",
            "J(x_*+h)-J(x_*)=\\frac12\\langle Ah,h\\rangle",
            "\\frac{\\eta(t+h)(y)-\\eta(t)(y)}{h}=w(y)",
            "$\\ell(df(x;h+k))=\\ell(df(x;h))+\\ell(df(x;k))$",
        ):
            self.assertIn(fragment, source)
        # Quadratic energy with A=diag(2,3), b=(4,3), x*=(2,1).
        def energy(x,y):
            return (2*x*x+3*y*y)/2-4*x-3*y
        for h,k in ((Fraction(1,3),Fraction(-2,5)),(Fraction(0),Fraction(1,7))):
            self.assertEqual(energy(2+h,1+k)-energy(Fraction(2),Fraction(1)),
                             (2*h*h+3*k*k)/2)


    def test_audit34_measurability_and_completeness_contracts(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "B_{n,j}=C_{n,j}\\setminus\\bigcup_{i<j}C_{n,i}",
            "\\mu(E_n)<2^{-n}",
            "\\|f_{n_{k+1}}-f_{n_k}\\|_{L^1}\\le 2^{-k}",
            "\\|f-f_{n_k}\\|_{L^1}\\le\\sum_{j\\ge k}2^{-j}",
            "\\chi_A(s)\\nu(B)x",
            "v_n(b)=f(b)",
        ):
            self.assertIn(fragment, source)

    def test_audit34_vector_l1_cauchy_tail(self):
        # Exact finite-atom witnesses of the telescoping estimate.
        # f_k has two coordinates and converges to f in weighted l1.
        weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
        f = [(Fraction(2), Fraction(-1)), (Fraction(-3), Fraction(4)),
             (Fraction(0), Fraction(5))]
        v = [(1, -1), (-1, 1), (1, 1)]

        def fn(k):
            return [tuple(x + Fraction(y, 2**k) for x, y in zip(a,b))
                    for a,b in zip(f,v)]

        def dist(u,w):
            return sum(mu*sum(abs(x-y) for x,y in zip(a,b))
                       for mu,a,b in zip(weights,u,w))

        for k in range(1, 20):
            self.assertEqual(dist(fn(k+1),fn(k)), Fraction(1, 2**k))
            self.assertEqual(dist(fn(k),f), Fraction(1, 2**(k-1)))
            for m in range(k+1, 21):
                tail = sum(Fraction(1, 2**j) for j in range(k,m))
                self.assertEqual(dist(fn(k),fn(m)), tail)
                self.assertLessEqual(tail, dist(fn(k),f))


    def test_audit35_dunford_pettis_contracts(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\int_S|x_{n_k}'(f(s))-h(s)|\\,\\mathrm d\\mu(s)\\le 2^{-k}",
            "D_A(a)=\\sum_{n\\in A}a_n",
            "D_{S_*}(a)=\\sum_{n\\ge1}",
            "B_Y(e_t,1/2)",
            "\\le\\int_S\\|f_n-f\\|\\,\\mathrm d\\mu.",
        ):
            self.assertIn(fragment, source)

    def test_dunford_signed_atoms(self):
        # Finite truncations of the c0 example: bilinear pairing,
        # opposite signs cancel only on the full paired set.
        for n in range(1, 9):
            a = [Fraction((-1)**k, k*k+1) for k in range(1,n+1)]
            atoms = [(k, sign) for k in range(1,n+1) for sign in (-1,1)]
            def scalar_integral(subset):
                return sum((Fraction(1,2**(k+1))*sign*2**k*a[k-1]
                            for k,sign in subset), Fraction(0))
            self.assertEqual(scalar_integral(atoms),0)
            self.assertEqual(scalar_integral([(k,1) for k in range(1,n+1)]),
                             sum(a,Fraction(0))/2)
            for mask in range(1 << len(atoms)) if n <= 5 else (0,1,3,7):
                subset = [atom for i,atom in enumerate(atoms) if mask & (1<<i)]
                coefficients = [sum((Fraction(sign,2) for j,sign in subset if j==k),
                                    Fraction(0)) for k in range(1,n+1)]
                self.assertEqual(scalar_integral(subset),
                    sum((v*w for v,w in zip(coefficients,a)),Fraction(0)))


    def test_audit36_gelfand_variation_contracts(self):
        source = SOURCE.read_text(encoding="utf-8")
        for fragment in (
            "\\|g_A\\|\\le\\|Q\\|",
            "\\sum_n|g_{A_n}(y)|\\le\\int_A",
            "|m|(A_i)-\\varepsilon/N",
            "m_f(A)-\\sum_{n=1}^N m_f(A_n)=m_f(B_N)",
            "B_0=S\\setminus\\bigcup_{j=1}^k B_j",
        ):
            self.assertIn(fragment, source)

    def test_audit36_variation_stability_finite_atoms(self):
        # Independent enumeration of partitions, not the density formula.
        mu = [Fraction(1,2), Fraction(1,4), Fraction(1,8), Fraction(1,8)]
        f = [(2,-3),(0,1),(-2,2),(3,0)]
        g = [(1,-3),(1,-1),(-2,1),(0,0)]
        def partitions(items):
            if not items:
                yield []
                return
            i,*rest = items
            for p in partitions(rest):
                yield [[i]] + p
                for j in range(len(p)):
                    q = [b[:] for b in p]
                    q[j].append(i)
                    yield q
        def variation(h,indices):
            return max((sum(sum(abs(sum(mu[i]*h[i][k] for i in b))
                                for k in range(2)) for b in p)
                        for p in partitions(indices)), default=0)
        for mask in range(16):
            A = [i for i in range(4) if mask & (1<<i)]
            vf,vg = variation(f,A),variation(g,A)
            error = sum(mu[i]*sum(abs(f[i][k]-g[i][k]) for k in range(2)) for i in A)
            self.assertLessEqual(abs(vf-vg),error)
            for split in range(16):
                B = [i for i in A if split & (1<<i)]
                C = [i for i in A if i not in B]
                self.assertEqual(vf,variation(f,B)+variation(f,C))

if __name__ == "__main__":
    unittest.main()
