"""Chapter 14 audit: Frechet/Gateaux differentiability, examples and TeX contracts."""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "chapters/pl/functional_analysis"
SOURCE = CHAPTERS / "14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex"


def not_frechet_example(x, y):
    return x**3*y/(x**4+y*y) if x or y else 0.0


def discontinuous_directional_example(x, y):
    return x**3*y/(x**6+y*y) if x or y else 0.0


def nonlinear_directional_example(x, y):
    return x**3/(x*x+y*y) if x or y else 0.0


class Chapter14Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_environment_balancing(self):
        counts = {
            "proof": 12, "twierdzenie": 7, "stwierdzenie": 4,
            "lemat": 1, "definicja": 6, "przyklad": 8, "uwaga": 4,
            "tikzpicture": 1,
        }
        for name, count in counts.items():
            self.assertEqual(self.source.count(r"\begin{" + name + "}"), count, name)
            self.assertEqual(self.source.count(r"\end{" + name + "}"), count, name)

    def test_14_references_across_complete_context(self):
        texts = [
            next(CHAPTERS.glob(f"{i:02d}-*.tex")).read_text(encoding="utf-8")
            for i in range(1, 15)
        ]
        labels = [
            item for text in texts
            for item in re.findall(r"\\label\{([^}]+)\}", text)
        ]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(re.findall(r"\\label\{([^}]+)\}", self.source)), 29)
        refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", self.source)
        refs += re.findall(r"\\hyperref\[([^\]]+)\]", self.source)
        self.assertEqual(len(refs), 4)
        self.assertEqual(set(refs) - set(labels), set())

    def test_polish_terminology(self):
        self.assertNotRegex(self.source, r"\bdualn\w*|\binjektywn\w*")
        self.assertNotRegex(self.source, r"\bsekwencj\w*|\bsekwencyjn\w*")
        self.assertNotRegex(self.source, r"\bwskaźnik\w*|\btensorowani\w*")
        self.assertNotRegex(self.source, r"\\(?:mathbf|mathbb)\s*(?:\{1\}|1)")

    def test_inline_math_balanced_by_paragraph(self):
        text = "\n".join(line.split("%", 1)[0] for line in self.source.splitlines())
        for i, paragraph in enumerate(re.split(r"\n\s*\n", text), 1):
            self.assertEqual(
                len(re.findall(r"(?<!\\)\$", paragraph)) % 2, 0,
                f"Unbalanced inline math in paragraph {i}",
            )

    def test_definitions_and_quantifiers(self):
        for marker in (
            r"\label{def:directional14}", r"\label{def:gateaux14}",
            r"\label{def:frechet14}", r"\label{def:c1-14}",
            r"\label{def:gradient14}", r"\label{def:complex-differentiability14}",
        ):
            self.assertIn(marker, self.source)
        self.assertIn(r"\mathcal L(E,F)", self.source)

    def test_frechet_implies_directional_in_smooth_scalar(self):
        # For F(x,y)=x^2+3xy, the derivative at (1,-1) is (-1,3).
        x, y, a, b = 1.0, -1.0, 2.0, -1.0
        fun = lambda u, v: u*u+3*u*v
        exact = (2*x+3*y)*a + 3*x*b
        for t in (1e-2, 1e-3, 1e-4):
            approximation = (fun(x+t*a, y+t*b)-fun(x,y))/t
            self.assertLess(abs(approximation-exact), 8*t)

    def test_discontinuous_all_directional_derivatives_zero(self):
        for a, b in ((1.0,0.0),(2.0,1.0),(-1.0,2.0),(0.0,1.0)):
            values = [
                discontinuous_directional_example(t*a,t*b)/t
                for t in (1e-3,1e-4,1e-5)
            ]
            self.assertLess(abs(values[-1]), 2e-4)
        for x in (0.1,0.01,0.001):
            self.assertAlmostEqual(discontinuous_directional_example(x,x**3),0.5)

    def test_continuous_gateaux_not_frechet(self):
        for a, b in ((1.0,0.0),(1.0,2.0),(0.0,1.0)):
            self.assertLess(
                abs(not_frechet_example(1e-5*a,1e-5*b)/1e-5),1e-4
            )
        for x in (1e-2,1e-3,1e-4):
            f = not_frechet_example(x,x*x)
            ratio = abs(f)/math.hypot(x,x*x)
            self.assertAlmostEqual(ratio,1/(2*math.sqrt(1+x*x)),places=10)

    def test_directional_derivative_not_additive(self):
        def dq(a,b):
            return nonlinear_directional_example(a,b)
        self.assertAlmostEqual(dq(1,0)+dq(0,1),1)
        self.assertAlmostEqual(dq(1,1),0.5)
        for a,b in ((1,0),(1,1),(-2,1)):
            for t in (0.01,-0.01):
                self.assertAlmostEqual(
                    nonlinear_directional_example(t*a,t*b)/t,dq(a,b)
                )

    def test_gateaux_chain_rule_counterexample(self):
        gamma = lambda t:(t,t*t)
        for t in (0.1,0.01,-0.01):
            x,y = gamma(t)
            self.assertAlmostEqual(not_frechet_example(x,y)/t,0.5)

    def test_l1_norm_gateaux_but_not_frechet(self):
        x = [2.0**(-n) for n in range(1,15)]
        h = [(-1)**n*2.0**(-n) for n in range(1,15)]
        for t in (1e-3,1e-4,1e-5):
            if all(abs(t*v)<abs(a) for a,v in zip(x,h)):
                quotient = (sum(abs(a+t*v) for a,v in zip(x,h)) -
                            sum(abs(a) for a in x))/t
                self.assertAlmostEqual(quotient,sum(h),places=8)
        for k in range(len(x)):
            v = x.copy()
            v[k] = -x[k]
            delta = 2*abs(x[k])
            linear = -2*abs(x[k])
            self.assertAlmostEqual(
                abs(sum(abs(z) for z in v)-sum(abs(z) for z in x)-linear)/delta,
                1.0,
            )

    def test_bilinear_chain_rule_hypothesis_complete(self):
        self.assertIn(
            r"Niech $E,E_1,E_2,G$ będą rzeczywistymi przestrzeniami Banacha",
            self.source,
        )
        self.assertIn(r"\label{thm:bilinear14}", self.source)

    def test_bilinear_product_derivative(self):
        # B(x,y)=xy in R, derivative at (2,3) along (u,v) is 3u+2v.
        x,y,du,dv=2.0,3.0,4.0,-2.0
        for t in (1e-2,1e-3,1e-4):
            quotient=((x+t*du)*(y+t*dv)-x*y)/t
            self.assertLess(abs(quotient-(du*y+x*dv)), 10*t)

    def test_hilbert_quadratic_gradient(self):
        # J(x)=1/2 <Ax,x> - <x,b> with A=diag(2,3).
        x,b,h=[1.0,-2.0],[2.0,1.0],[0.5,-1.0]
        val=lambda z: (2*z[0]**2+3*z[1]**2)/2 - z[0]*b[0]-z[1]*b[1]
        derivative=(2*x[0]-b[0])*h[0]+(3*x[1]-b[1])*h[1]
        for t in (1e-2,1e-3,1e-4):
            remainder=val([a+t*v for a,v in zip(x,h)])-val(x)-t*derivative
            self.assertAlmostEqual(remainder,t*t*(2*h[0]**2+3*h[1]**2)/2)

    def test_mean_value_theorem_vector_curve(self):
        # gamma(t)=(t^2, t^3), integral gamma' on [0,1]=(1,1).
        n=10000
        integral=[
            sum((2*(k+0.5)/n)/n for k in range(n)),
            sum((3*((k+0.5)/n)**2)/n for k in range(n)),
        ]
        self.assertAlmostEqual(integral[0],1,places=7)
        self.assertAlmostEqual(integral[1],1,places=7)

    def test_continuous_gateaux_sufficient_condition_documented(self):
        self.assertIn(r"\label{thm:continuous-gateaux14}",self.source)
        self.assertIn(r"D_Gf:U\to\mathcal L(E,F)",self.source)
        self.assertIn(r"\sup_{0\le t\le1}",self.source)

    def test_discontinuous_derivative_example(self):
        # f(t)=t^2 sin(1/t^2) is differentiable with f'(0)=0.
        f=lambda t:t*t*math.sin(1/(t*t)) if t else 0.0
        for t in (1e-2,1e-3,1e-4):
            self.assertLessEqual(abs(f(t)/t),abs(t))
        self.assertIn(r"2x^{-1}\cos(1/x^2)",self.source)

    def test_real_differentiability_of_norm(self):
        x,y,h,k=2.0,3.0,-0.5,1.0
        radial=(x*h+y*k)/math.hypot(x,y)
        n=lambda t:math.hypot(x+t*h,y+t*k)
        for t in (1e-3,1e-4,1e-5):
            self.assertLess(abs((n(t)-n(0))/t-radial),t)

    def test_complex_conjugation_not_complex_linear(self):
        conj=lambda z:z.conjugate()
        self.assertNotEqual(conj(1j),1j*conj(1))
        self.assertIn(r"D_{\R}f(z)h=\overline h",self.source)
        self.assertIn("nie może być liniowy nad",self.source)

    def test_complex_abs_squared_at_origin(self):
        f=lambda z:abs(z)**2
        for h in (complex(1e-4,1e-4),complex(1e-5,-1e-5)):
            self.assertLess(abs(f(h))/abs(h),2e-4)
        self.assertIn(r"|h|^2=o(|h|)",self.source)

    def test_tikz_curve_and_caption(self):
        self.assertIn(r"\begin{tikzpicture}",self.source)
        self.assertIn(r"plot (\x,{\x*\x})",self.source)
        self.assertIn("kierunki stałe",self.source)


if __name__ == "__main__":
    unittest.main()
