"""Chapter 31: finite models and source regressions, not proof certification."""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "chapters/pl/measure_theory/31-dzety-od-geometrii-rozniczkowej-do-teorii-miary.tex"

class Chapter31(unittest.TestCase):
    def test_mt31_001_monomial_count(self):
        for n in range(1,5):
            for k in range(6):
                self.assertEqual(sum(sum(a)<=k for a in product(range(k+1), repeat=n)),comb(n+k,k))

    def test_mt31_002_taylor_integral_coefficient(self):
        # Integral t^r(1-t)^k equals r!k!/(r+k+1)!.
        for k in range(7):
            for r in range(5):
                integral = sum(Q((-1)**j*comb(k,j),r+j+1) for j in range(k+1))
                self.assertEqual(integral,Q(factorial(r)*factorial(k),factorial(r+k+1)))
                if r == 0:
                    self.assertEqual((k+1)*integral,1)

    def test_mt31_003_second_jet_affine_change(self):
        # y=x+x^2, at 0: d/dy=d/dx, d²/dy²=d²/dx²-2d/dx.
        for p,a,b in product(range(-3,4),repeat=3):
            self.assertEqual((a-2*p)-(b-2*p),a-b)
        self.assertEqual(0-2*1,-2)

    def test_mt31_004_density_cone_intersection_bound(self):
        # Finite probability model: P(C ∩ A) >= P(C)-P(A^c).
        for c in range(1,9):
            for missing in range(9):
                for overlap in range(max(0,c+missing-8),min(c,missing)+1):
                    self.assertGreaterEqual(c-overlap,c-missing)

    def test_mt31_005_labels_and_source(self):
        s = SOURCE.read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}",s)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(labels),30)
        self.assertIn("thm:dzety-whitney-extension",labels)
        flat = " ".join(s.split())
        for step in ("przedstawicieli kiełków", "resztą całkową",
                     "czynnik niezróżniczkowany", "drugi aksjomat przeliczalności",
                     "Działanie jest wolne i przechodnie", "dopełnienia $A-x$"):
            self.assertIn(step,flat)
        self.assertNotRegex(s,r"\\(?:mathbf|mathbb)\{1\}_")


    def test_mt31_006_whitney_intervals(self):
        # K={0}, dyadic intervals on the positive half-line.
        # Scaling and reflection reduce the check to integer indices.
        for m in range(8,16):
            for j in range(-4,5):
                ell = Q(2)**j
                lo,hi = m*ell,(m+1)*ell
                parent_lo = 2*(m//2)*ell
                self.assertGreaterEqual(lo,8*ell)
                self.assertLess(parent_lo,16*ell)
                self.assertLess(lo,18*ell)
                self.assertGreaterEqual(lo-ell/8,7*ell)
                self.assertLessEqual(hi+ell/8,20*ell)

    def test_mt31_007_whitney_polynomial_recenter(self):
        # Exact scalar polynomials with coefficients of x^i.
        def deriv(c,b,r):
            return sum(c[i]*factorial(i)//factorial(i-r)*b**(i-r)
                       for i in range(r,len(c)))
        for c in product(range(-2,3),repeat=4):
            for b in (-2,0,3):
                for z in (-1,1,4):
                    for r in range(4):
                        actual = deriv(c,z,r)
                        recentered = sum(Q(deriv(c,b,r+j),factorial(j))*(z-b)**j
                                         for j in range(4-r))
                        self.assertEqual(actual,recentered)

    def test_mt31_008_whitney_derivative_bounds_and_gluing(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for term in ("parami rozłącznych wnętrzach, których suma",
                     "pokrycie powiększeniami jest lokalnie skończone",
                     "Traktując $a$ jako ustalony punkt podczas różniczkowania",
                     "dla dowolnego kierunku zbliżania",
                     "Wektor $(H_"):
            self.assertIn(term,s)
        for expr in (r"7\sqrt n\,\ell(Q)",r"20\sqrt n\,\ell(Q)",
                     r"D^\alpha(S^{-1})",r"z\in\overline{Q^*}",
                     r"r^{k-|\beta|+|\gamma|}"):
            self.assertIn(expr,s)


    def test_mt31_009_angular_moment_symmetries(self):
        # Symmetric finite angular model: signed permutations of coordinate axes.
        for n in range(1,9):
            directions = [tuple(sign if i==j else 0 for i in range(n))
                          for j in range(n) for sign in (-1,1)]
            for i,j in product(range(n),repeat=2):
                moment = sum(Q(v[i]*v[j],len(directions)) for v in directions)
                self.assertEqual(moment,Q(int(i==j),n))

    def test_mt31_010_whitney_lusin_overlap_and_remainder(self):
        for n in range(1,21):
            self.assertGreater(Q(3,2)**n,2*Q(1,4)**n)
        for x,y,z,gx,gy,fx,fy,fz in product((-1,0,1),repeat=8):
            rx=fz-fx-gx*(z-x)
            ry=fz-fy-gy*(z-y)
            self.assertEqual(fy-fx-gx*(y-x),rx-ry+(gx-gy)*(z-y))
        for j in range(1,11):
            self.assertLess(sum(Q(1,2**i) for i in range(1,j+1)),1)

    def test_mt31_011_measurability_and_higher_jet_source(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for term in ("Wartość $f(x)$ w punkcie bazowym pozostawiamy niezmienioną",
                     "przesunięciem zbioru miary zero",
                     "mierzalność samego zbioru $D$",
                     "supremum po wszystkich promieniach",
                     "do $A\\cap D_0$ zamiast $A$",
                     "otwarty względnie w $K_0$",
                     "dążą jednostajnie do zera również bez obcięcia"):
            self.assertIn(term,s)
        self.assertIn(r"\bigcap_{j\ge1}\bigcap_{q\ge1}",s)
        self.assertIn(r"\max_{|\alpha|\le k}\min(1,V_{\alpha,l})",s)


    def test_mt31_012_contact_and_symbol_transformation(self):
        # x'=a*x, u'=b*u+c*x: first contact form transforms by b.
        for a,b,c,p,dx,du in product((-2,-1,1,2),repeat=6):
            pt=Q(b*p+c,a)
            self.assertEqual(b*du+c*dx-pt*a*dx,b*(du-p*dx))
        # Second-order scalar symbol under a two-dimensional shear.
        for t,xi,eta in product(range(-3,4),repeat=3):
            self.assertEqual((xi+t*eta)**2+eta**2,
                             xi**2+2*t*xi*eta+(t*t+1)*eta**2)

    def test_mt31_013_bv_jump_and_localization(self):
        # Distributional derivative of the half-line indicator:
        # integral of derivative of a compactly supported piecewise linear test.
        for v0,v1,v2 in product(range(-3,4),repeat=3):
            self.assertEqual(-((v1-v0)+(v2-v1)+(0-v2)),v0)
        # Partition a finite model of a weighted fibre into disjoint pieces.
        weights=(Q(1,2),Q(3,2),Q(0),Q(2))
        for owners in product(range(3),repeat=4):
            self.assertEqual(sum(sum(w for w,o in zip(weights,owners) if o==i)
                                 for i in range(3)),sum(weights))

    def test_mt31_014_geometry_measure_source(self):
        s = " ".join(SOURCE.read_text(encoding="utf-8").split())
        for term in ("ich wspólne jądro jest niezależne od trywializacji",
                     "Odwrotna zmiana współrzędnych",
                     "konwencji bez czynnika",
                     "stałą razy $\\chi_K$",
                     "kolumny są granicami",
                     "lokalnie skończoną miarą wektorową",
                     "rozcinając pokrycie na rozłączne zbiory borelowskie",
                     "kres górny sum po jego skończonych podzbiorach"):
            self.assertIn(term,s)
        for label in ("thm:rademacher-28","thm:BV-measure-29",
                      "thm:lipschitz-area-coarea-28"):
            self.assertIn(r"\ref{"+label+"}",s)


    def test_mt31_015_finite_jet_interpolation(self):
        # Cubic Hermite interpolation at 0 and 1.
        for v0,d0,v1,d1 in product(range(-2,3),repeat=4):
            a,b=v0,d0
            c=3*(v1-v0)-2*d0-d1
            d=2*(v0-v1)+d0+d1
            self.assertEqual((a,b,a+b+c+d,b+2*c+3*d),(v0,d0,v1,d1))

    def test_mt31_016_density_and_equivalence(self):
        for j in range(2,15):
            r=Q(1,2**j)
            tail=Q(8,7)*r**3
            self.assertEqual(tail/(2*r),Q(4,7)*r**2)
        s=" ".join(SOURCE.read_text(encoding="utf-8").split())
        for term in ("Warunek przynależności jest istotny",
                     "relacją równoważności na",
                     "Chińskie twierdzenie o resztach",
                     "wielomianem. Istotnie",
                     "zbiór ich nierówności jest otwarty"):
            self.assertIn(term,s)
        self.assertIn(r"\ref{cor:lebesgue-density-25}",s)

if __name__ == "__main__":
    unittest.main()
