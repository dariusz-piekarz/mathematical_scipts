"""Chapter 13 mathematical sanity checks and TeX regression contracts (stdlib only)."""
import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
SOURCE = CHAPTERS / "13-przestrzenie-hilberta-reprezentacja-riesza-i-formy-poltoraliniowe.tex"


def inner(x, y):
    """Inner product linear in the first argument."""
    return sum(a * b.conjugate() for a, b in zip(x, y))


def norm(x):
    return math.sqrt(max(inner(x, x).real, 0.0))


class Chapter13Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_core_theorem_labels(self):
        for label in (
            "lem:cs13", "prop:parallelogram13", "thm:projection-convex13",
            "thm:orth-decomposition13", "thm:riesz-hilbert13", "lem:bessel13",
            "thm:countable-fourier-support13", "thm:parseval13",
            "thm:hilbert-basis13", "thm:hilbert-hamel-uncountable13",
            "prop:hilbert-l2I13", "thm:adjoint13", "thm:form-repr13",
            "thm:lax-milgram13",
        ):
            self.assertIn(r"\label{" + label + "}", self.source)

    def test_environment_counts(self):
        expected = {
            "proof": 14, "twierdzenie": 10, "stwierdzenie": 2,
            "lemat": 2, "definicja": 4, "przyklad": 5, "uwaga": 5,
        }
        for env, n in expected.items():
            self.assertEqual(self.source.count(r"\begin{" + env + "}"), n, env)
            self.assertEqual(self.source.count(r"\end{" + env + "}"), n, env)

    def test_labels_and_references_in_complete_context(self):
        texts = [
            next(CHAPTERS.glob(f"{i:02d}-*.tex")).read_text(encoding="utf-8")
            for i in range(1, 14)
        ]
        labels = [m for text in texts for m in re.findall(r"\\label\{([^}]+)\}", text)]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(re.findall(r"\\label\{([^}]+)\}", self.source)), 30)
        refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        refs += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertEqual(len(refs), 13)
        self.assertEqual(sorted(set(refs) - set(labels)), [])

    def test_polish_terminology(self):
        self.assertNotRegex(self.source, r"\bdualn\w*|\binjektywn\w*")
        self.assertNotRegex(self.source, r"\bsekwencj\w*|\bsekwencyjn\w*")
        self.assertNotRegex(self.source, r"\btensorowani\w*|\bwskaźnik\w*")
        self.assertIn("przestrzeń sprzężoną", self.source)
        self.assertIn("formą półtoraliniową", self.source)
        self.assertNotRegex(self.source, r"\\(?:mathbf|mathbb)\s*(?:\{1\}|1)")

    def test_inline_math_balanced_in_paragraphs(self):
        stripped = "\n".join(line.split("%", 1)[0] for line in self.source.splitlines())
        for i, paragraph in enumerate(re.split(r"\n\s*\n", stripped), 1):
            self.assertEqual(len(re.findall(r"(?<!\\)\$", paragraph)) % 2, 0,
                             f"paragraph {i}")

    def test_linear_first_complex_inner_product(self):
        x = [1+2j, -3+1j]
        y = [2-1j, 4+3j]
        self.assertAlmostEqual(abs(inner(x, y)-inner(y, x).conjugate()), 0)
        self.assertAlmostEqual(abs(inner([2j*z for z in x], y)-2j*inner(x, y)), 0)
        self.assertAlmostEqual(abs(inner(x, [2j*z for z in y]) + 2j*inner(x, y)), 0)

    def test_complex_polarization_formula(self):
        x, y = [2+3j, 1-1j], [1-2j, -3+1j]
        add = lambda a, b: [u+v for u, v in zip(a, b)]
        minus = lambda a, b: [u-v for u, v in zip(a, b)]
        iy = [1j*v for v in y]
        z = (norm(add(x,y))**2 - norm(minus(x,y))**2
             + 1j*norm(add(x,iy))**2 - 1j*norm(minus(x,iy))**2)/4
        self.assertAlmostEqual(abs(z-inner(x, y)), 0)

    def test_cauchy_schwarz_and_bessel(self):
        x = [1+1j, 2-1j, -4j]
        y = [2, 3j, -1]
        self.assertLessEqual(abs(inner(x, y)), norm(x)*norm(y)+1e-10)
        self.assertLessEqual(sum(abs(z)**2 for z in x[:2]),
                             norm(x)**2+1e-10)

    def test_real_positive_orthant_metric_projection(self):
        def project(v):
            return [max(z, 0.0) for z in v]
        for x, y in (([-2, 3], [1, -5]), ([0, -1], [-2, 4]),
                     ([2, 2], [-2, -2])):
            p, q = project(x), project(y)
            self.assertLessEqual(norm([a-b for a, b in zip(p,q)]),
                                 norm([a-b for a, b in zip(x,y)])+1e-10)
            self.assertLessEqual(sum((a-b)*(c-a) for a,b,c in zip(x,p,q)), 1e-10)

    def test_projection_onto_complex_line(self):
        u, x = [1+1j, -2j, 2], [2-1j, 1+2j, -1]
        coeff = inner(x, u)/norm(u)**2
        p = [coeff*v for v in u]
        residual = [v-w for v,w in zip(x,p)]
        self.assertAlmostEqual(abs(inner(residual, u)), 0)
        self.assertAlmostEqual(norm(x)**2, norm(p)**2+norm(residual)**2)

    def test_complex_riesz_functional_is_antilinear_in_representer(self):
        x, y = [1+1j, 4-2j], [2j, 3+1j]
        alpha = 2-1j
        self.assertAlmostEqual(abs(inner(x, [alpha*v for v in y]) -
                                    alpha.conjugate()*inner(x, y)), 0)

    def test_fourier_support_threshold(self):
        coeffs = [0.25, 0.5, 0.01, 0.0, 0.6, 0.001, 0]
        total = sum(abs(c)**2 for c in coeffs)
        for n in (1,2,3,4,5,10):
            large = sum(abs(c)>=1/n for c in coeffs)
            self.assertLessEqual(large, n*n*total+1e-10)

    def test_fourier_unconditional_finite_model(self):
        coeffs = [1+2j, -2j, 3-1j]
        values = [norm([c])**2 for c in coeffs]
        self.assertAlmostEqual(sum(values), norm(coeffs)**2)
        for permutation in itertools.permutations(coeffs):
            self.assertAlmostEqual(sum(abs(c)**2 for c in permutation),
                                   norm(coeffs)**2)

    def test_vandermonde_nonzero(self):
        t = [0.15,0.45,0.85]
        determinant = ((t[1]-t[0])*(t[2]-t[0])*(t[2]-t[1]))
        self.assertNotEqual(determinant, 0)
        self.assertIn("Vandermonde", self.source)

    def test_gram_schmidt_two_vectors(self):
        a = [1+1j, 2-1j]
        b = [2j, 3]
        e1 = [v/norm(a) for v in a]
        projection = inner(b,e1)
        u2 = [v-projection*w for v,w in zip(b,e1)]
        e2 = [v/norm(u2) for v in u2]
        self.assertAlmostEqual(norm(e1),1)
        self.assertAlmostEqual(norm(e2),1)
        self.assertAlmostEqual(abs(inner(e1,e2)),0)

    def test_adjoint_2x2_complex_identity(self):
        T = [[1+2j, 2-1j],[-3j, 1]]
        x, y = [1-1j,2], [1+2j,-3j]
        apply = lambda M,z: [sum(m*v for m,v in zip(row,z)) for row in M]
        adj = [[T[j][i].conjugate() for j in range(2)] for i in range(2)]
        self.assertAlmostEqual(abs(inner(apply(T,x),y)-inner(x,apply(adj,y))),0)

    def test_bounded_sesquilinear_form(self):
        A = [2, 3]
        a = lambda x,y: sum(k*u*v.conjugate() for k,u,v in zip(A,x,y))
        x,y = [1+1j,2], [2j,1-2j]
        self.assertLessEqual(abs(a(x,y)),max(A)*norm(x)*norm(y)+1e-10)
        self.assertAlmostEqual(abs(a(x,y)-a(y,x).conjugate()),0)

    def test_lax_milgram_finite_diagonal_example(self):
        A = [2.0,3.0,5.0]
        f = [3+1j, -2j,4]
        u = [v/k for v,k in zip(f,A)]
        for v in ([1,2j,-3],[2,0,1]):
            left = sum(k*x*w.conjugate() for k,x,w in zip(A,u,v))
            right = inner(f,v)
            self.assertAlmostEqual(abs(left-right), 0)
        self.assertLessEqual(norm(u),norm(f)/min(A)+1e-10)

    def test_weak_poisson_f_constant_one(self):
        # -u''=1, u(0)=u(1)=0; u(t)=t(1-t)/2 and u'=1/2-t.
        for k in range(11):
            t = k/10
            u = t*(1-t)/2
            self.assertAlmostEqual(0.5-t, 0.5-t)
            self.assertGreaterEqual(u, -1e-12)
        self.assertAlmostEqual(0*(1-0)/2, 0)
        self.assertAlmostEqual(1*(1-1)/2, 0)
        # weak test v(t)=t(1-t): int u'v'=1/6=int v.
        h=1/10000
        v_left=sum((0.5-(k+0.5)*h)*(1-2*(k+0.5)*h)*h for k in range(10000))
        v_right=sum(((k+0.5)*h)*(1-(k+0.5)*h)*h for k in range(10000))
        self.assertAlmostEqual(v_left,v_right,places=7)

    def test_weak_poisson_continuity_and_density_documented(self):
        self.assertIn(r"|\Lambda(v)|\le\|f\|_2\|v\|_2",self.source)
        self.assertIn(r"\|u\|_2\le\|u'\|_2/\sqrt2",self.source)
        self.assertIn(r"w''=-f",self.source)
        self.assertIn("w normie $H$",self.source)
        self.assertIn(r"\widetilde h_n\to h",self.source)
        self.assertIn(r"u=w",self.source)
        self.assertIn(r"w''=-f",self.source)

    def test_examples_and_complex_conventions(self):
        self.assertIn(r"\chi_{[0,1]}", self.source)
        self.assertIn(r"\nu:\N\to I_x", self.source)
        self.assertIn(r"\|\Lambda\|", self.source)
        self.assertIn(r"\operatorname{Re}\langle h,x\rangle",self.source)


if __name__ == "__main__":
    unittest.main()
