"""Finite regression checks; not a proof of the infinite-dimensional results."""
import cmath
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PDE = ROOT / "chapters/pl/partial_differential_equations"
SOURCE = PDE / "12-operatory-nieograniczone-i-teoria-spektralna.tex"


class SpectralChecks(unittest.TestCase):
    def test_source_structure(self):
        source = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(labels), 33)
        self.assertEqual(len(re.findall(r"\\section\{", source)), 9)
        stack = []
        for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", source):
            if kind == "begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), name)
        self.assertFalse(stack)
        self.assertNotRegex(source, r"\\mathrm d\\lambda_[12d](?![\w(])")
        self.assertNotIn(r"\frac{\mathrm d}{\mathrm d\lambda", source)

    def test_reference_targets(self):
        source = SOURCE.read_text(encoding="utf-8")
        refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", source))
        paths = [p for p in PDE.glob("*.tex")
                 if p.name[:2] in {"05", "06", "07", "08", "09", "10", "11", "12", "15"}]
        labels = [label for p in paths for label in re.findall(
            r"\\label\{([^}]+)\}", p.read_text(encoding="utf-8"))]
        for label in refs:
            with self.subTest(label=label):
                self.assertEqual(labels.count(label), 1)

    def test_resolvent(self):
        for lam in (1, 4, 9, 16):
            for z in (-1, 2j, 3+2j):
                for w in (-2, -1j, 5+1j):
                    rz, rw = 1/(lam-z), 1/(lam-w)
                    self.assertAlmostEqual(abs(rz-rw-(z-w)*rz*rw), 0)
                    self.assertAlmostEqual(abs((1-(1+z)/(lam+1))*(lam+1)-(lam-z)), 0)

    def test_form_and_minmax_diagonal(self):
        eigen = (1, 4, 9, 16)
        for k, lam in enumerate(eigen, 1):
            coeff = [complex(j+1, j-1) for j in range(k)]
            rq = sum(x*abs(a)**2 for x, a in zip(eigen, coeff))/sum(abs(a)**2 for a in coeff)
            self.assertLessEqual(rq, lam)
            self.assertEqual(max(eigen[:k]), min(eigen[k-1:]))

    def test_heat_generator_and_smoothing(self):
        for lam in (1, 4, 9, 25):
            self.assertAlmostEqual(math.expm1(-lam*1e-8)/1e-8, -lam, delta=4e-6)
            for m in (1, 2, 3, 5):
                for t in (.01, .1, 1, 10):
                    self.assertLessEqual(lam**m*math.exp(-t*lam),
                                         (m/(math.e*t))**m*(1+1e-12))

    def test_duhamel(self):
        for lam in (1, 4, 9, 25):
            for t in (.01, .2, 1, 2):
                f = t/lam + math.expm1(-lam*t)/lam**2
                fp = -math.expm1(-lam*t)/lam
                self.assertAlmostEqual(fp+lam*f, t)

    def test_duhamel_counterexample_support(self):
        ls = [8*4**n for n in range(12)]
        for a, b in zip(ls, ls[1:]):
            self.assertLess(2/b, 1/a)
        # The modal coefficient is C_eta/(sqrt(n)*L_n).
        # Weighted squares therefore produce the harmonic series.
        for n, lam in enumerate(ls, 1):
            self.assertAlmostEqual(lam**2*(1/(math.sqrt(n)*lam))**2, 1/n)

    def test_wave_energy(self):
        for lam in (1, 4, 9, 25):
            for c in (.5, 1, 3):
                w = c*math.sqrt(lam)
                a, b = .7+.2j, -1.3+.4j
                e0 = w*w*abs(a)**2+abs(b)**2
                for t in (-2, 0, .7, 3):
                    u = a*math.cos(w*t)+b*math.sin(w*t)/w
                    p = -w*a*math.sin(w*t)+b*math.cos(w*t)
                    self.assertAlmostEqual(abs(p)**2+w*w*abs(u)**2, e0, delta=1e-10)

    def test_unitary_dynamics(self):
        for lam in (1, 4, 9, 25):
            for t in (-2, 0, .7, 3):
                z = cmath.exp(-1j*t*lam)
                self.assertAlmostEqual(abs(z), 1)
                self.assertAlmostEqual(abs(z.conjugate()*z-1), 0)
                for m in (1, 2, 3):
                    self.assertAlmostEqual(abs(lam**m*z)/lam**m, 1)

    def test_rectangle_multiplicity(self):
        eigen = sorted(m*m+n*n for m in range(1, 9) for n in range(1, 9))
        self.assertEqual(eigen[:3], [2, 5, 5])


if __name__ == "__main__":
    unittest.main()
