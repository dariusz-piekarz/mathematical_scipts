"""Regression and finite-model checks for functional analysis chapter 12."""
import cmath
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
SOURCE = CHAPTERS / "12-klasyczne-przestrzenie-banacha-i-ich-duale.tex"


class Chapter12Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_proofs_definitions_and_examples_balanced(self):
        expected = {"proof": 10, "definicja": 4, "stwierdzenie": 2,
                    "twierdzenie": 5, "lemat": 3, "przyklad": 2, "uwaga": 2}
        for environment, count in expected.items():
            self.assertEqual(
                self.source.count(r"\begin{" + environment + "}"), count,
                environment,
            )
            self.assertEqual(
                self.source.count(r"\end{" + environment + "}"), count,
                environment,
            )

    def test_unique_labels_and_resolved_refs_across_01_12(self):
        chapters = [
            next(CHAPTERS.glob(f"{n:02d}-*.tex")).read_text(encoding="utf-8")
            for n in range(1, 13)
        ]
        labels = [
            key for chapter in chapters
            for key in re.findall(r"\\label\{([^}]+)\}", chapter)
        ]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(re.findall(r"\\label\{([^}]+)\}", self.source)), 19)
        refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        refs += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertEqual(len(refs), 5)
        self.assertEqual(sorted(set(refs) - set(labels)), [])

    def test_conjugate_space_terminology_and_characteristic_functions(self):
        self.assertIn("przestrzenie sprzężone", self.source)
        self.assertNotRegex(self.source, r"\bdualn\w*|\bwskaźnik\w*")
        self.assertNotRegex(self.source, r"\\(?:mathbf|mathbb)\s*(?:\{1\}|1)")
        self.assertIn(r"\nu(A)=F(\chi_A)", self.source)
        self.assertIn(r"\nu(A)=F(\chi_A)", self.source)
        self.assertIn(r"\Phi(\chi_{A_n})=0", self.source)
        self.assertIn(r"T(\chi_K)", self.source)

    def test_operator_norm_and_completion_hypotheses(self):
        self.assertIn(r"\mathcal L(E,F)", self.source)
        self.assertIn(r"\|T_n-T\|\to0", self.source)
        self.assertIn("nawet gdy $E$ nie jest zupełna", self.source)

    def test_holder_sequence_finite_example(self):
        x = (1.0, -2.0, 3.0, 0.5)
        y = (-3.0, 2.0, 0.0, -1.0)
        for p in (1.5, 2.0, 3.0, 4.0):
            q = p / (p - 1)
            lhs = sum(abs(a*b) for a, b in zip(x, y))
            rhs = sum(abs(a)**p for a in x)**(1/p) * sum(abs(v)**q for v in y)**(1/q)
            self.assertLessEqual(lhs, rhs + 1e-10)
        self.assertLessEqual(sum(abs(a*b) for a, b in zip(x, y)),
                             sum(abs(a) for a in x) * max(abs(b) for b in y))

    def test_lp_dual_witness_for_finite_sequences(self):
        a = (complex(1, 2), complex(-2, 1), complex(0, 0))
        for p in (1.5, 2.0, 3.0):
            q = p / (p - 1)
            s = sum(abs(v)**q for v in a)
            witness = [
                (v.conjugate() * abs(v)**(q-2) / s**(1/p)) if v else 0
                for v in a
            ]
            self.assertAlmostEqual(sum(abs(v)**p for v in witness)**(1/p), 1)
            functional = sum(v*w for v, w in zip(a, witness))
            self.assertAlmostEqual(functional.real, s**(1/q))
            self.assertAlmostEqual(functional.imag, 0)

    def test_c0_dual_sign_witness(self):
        a = (complex(1, 1), complex(0, -2), complex(2, -3))
        witness = [v.conjugate()/abs(v) if v != 0 else 0 for v in a]
        value = sum(v*w for v, w in zip(a, witness))
        self.assertAlmostEqual(value.real, sum(abs(v) for v in a))
        self.assertAlmostEqual(value.imag, 0)

    def test_nonrepresentable_limit_functional(self):
        self.assertIn(r"\widetilde L(e_n)=0", self.source)
        self.assertIn(r"\widetilde L(u)=1", self.source)
        self.assertIn("u=(1,1,\\ldots)", self.source)

    def test_lp_holder_finite_measure(self):
        weights = (0.25, 0.5, 0.25)
        f = (1.0, -2.0, 4.0)
        g = (-1.0, 3.0, 2.0)
        p = q = 2.0
        left = sum(w*abs(x*y) for w, x, y in zip(weights, f, g))
        right = (sum(w*abs(x)**p for w, x in zip(weights, f))**(1/p)
                 * sum(w*abs(y)**q for w, y in zip(weights, g))**(1/q))
        self.assertLessEqual(left, right + 1e-10)

    def test_finite_measure_variation_bound(self):
        # nu(A)=F(chi_A), for finite atomic measure norm(chi_{union}) <= mu(K)^(1/p).
        weights = [0.1, 0.2, 0.3, 0.4]
        values = [complex(2, 1), complex(-3, 2), complex(1, -1), complex(-1, -2)]
        variation = sum(w*abs(v) for w, v in zip(weights, values))
        lhs = abs(sum(w*v for w, v in zip(weights, values)))
        self.assertLessEqual(lhs, variation + 1e-10)
        self.assertIn(r"\nu(A)=F(\chi_A)", self.source)

    def test_radon_nikodym_extremal_test_with_weighted_atoms(self):
        # For p=q=2 choose f proportional to conjugate of g.
        weights = [0.25, 0.25, 0.5]
        g = [complex(1, 2), complex(-1, 0), complex(2, -2)]
        norm = math.sqrt(sum(w*abs(v)**2 for w, v in zip(weights, g)))
        f = [v.conjugate()/norm for v in g]
        lhs = sum(w*x*y for w, x, y in zip(weights, f, g))
        self.assertAlmostEqual(lhs.real, norm)
        self.assertAlmostEqual(lhs.imag, 0)

    def test_linfty_dual_non_integral_functional(self):
        self.assertIn(r"\Phi(\chi_A)=1", self.source)
        self.assertIn(r"\Phi(\chi_{A_n})=0", self.source)
        self.assertIn(r"\sum_n\Phi(\chi_{A_n})=0", self.source)

    def test_riesz_outer_measure_matches_open_content(self):
        self.assertIn(r"\mu^*(U)=m(U)", self.source)
        self.assertIn(r"\mu^*(K)=m(K)=T(\chi_K)", self.source)
        self.assertIn(r"\mu_T=\mu^*|_{\mathcal B(K)}", self.source)

    def test_layer_cake_partition_of_unity_identity(self):
        # h_j = clip((f-j*delta)/delta, 0, 1): f=delta*sum_j h_j.
        delta = 0.1
        count = 100
        for value in (0.0, 0.05, 0.11, 0.31, 1.99, 8.25):
            h = [min(1, max(0, (value-j*delta)/delta)) for j in range(count)]
            self.assertAlmostEqual(value, delta*sum(h), places=9)

    def test_positive_functional_norm_is_mass(self):
        # Finite compact space with positive masses.
        mu = (0.3, 0.2, 0.5)
        values = (1.0, -2.0, 0.5)
        value = sum(w*x for w, x in zip(mu, values))
        self.assertLessEqual(abs(value), sum(mu)*max(abs(v) for v in values))
        self.assertAlmostEqual(sum(mu), 1.0)
        self.assertIn(r"m(K)=T(\chi_K)", self.source)

    def test_complex_variation_norm_discrete_model(self):
        mu = (complex(1, 2), complex(-2, -1), complex(1, 0))
        f = [v.conjugate()/abs(v) if v != 0 else 0 for v in mu]
        self.assertAlmostEqual(abs(sum(v*w for v, w in zip(mu, f))),
                               sum(abs(v) for v in mu))
        self.assertIn(r"|\nu|(K)", self.source)

    def test_dirac_evaluation(self):
        self.assertIn(r"\delta_{x_0}", self.source)
        self.assertIn(r"F_{x_0}(f)=f(x_0)", self.source)
        self.assertIn("ma normę $1$", self.source)


if __name__ == "__main__":
    unittest.main()
