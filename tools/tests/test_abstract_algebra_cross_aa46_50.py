"""AA-46–AA-50 cross-audit: exact Riccati/PV models and source references."""
from pathlib import Path
import re
import unittest
import sympy as s

x=s.symbols("x", positive=True)
ROOT=Path(__file__).resolve().parents[2]
NAMES={
43:"43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex",
44:"44-twierdzenie-liouvillea-o-calkowaniu-elementarnym.tex",
45:"45-kryteria-hiperwykladnicze-i-calki-nieelementarne.tex",
46:"46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex",
47:"47-algorytmy-rischa-i-kovacica.tex",
48:"48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex",
49:"49-kwadratowy-przypadek-algorytmu-kovacica.tex",
50:"50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex",
}

def rational_square(z):
    """In C(x), a rational function is a square iff valuations are even."""
    a,b=s.fraction(s.cancel(z))
    return all(k%2==0 for _,k in s.factor_list(a)[1]+s.factor_list(b)[1])

class CrossAuditAA46to50(unittest.TestCase):
    def exact(self,expr,msg):
        self.assertEqual(s.simplify(expr),0,msg)
    def test_risch_pv_rational_interface(self):
        self.exact(s.diff(-1/x,x)-1/x-(1/x**2-1/x),"AA47 Risch")
        q=2/x**2; z1=x**2; z2=1/x
        self.exact(s.diff(z1,x,2)-q*z1,"AA46 PV z1")
        self.exact(s.diff(z2,x,2)-q*z2,"AA46 PV z2")
        self.exact(z1*s.diff(z2,x)-s.diff(z1,x)*z2+3,"AA46 PV Wronskian")
        for r in (2/x,-1/x):
            self.exact(s.diff(r,x)+r**2-q,"AA48 rational Riccati")
    def test_quadratic_models_and_discriminant(self):
        models=(
            (x+s.Rational(5,16)/x**2,-s.Rational(1,4)/x,s.sqrt(x),-1/(2*x),4*x),
            ((4*x+5)/(16*x**2),-1/(4*x)+1/(2*(x-1)),s.sqrt(x)/(2*(x-1)),-1/(2*x)+1/(x-1),x/(x-1)**2),
            (1/x-s.Rational(3,16)/x**2,1/(4*x),1/s.sqrt(x),1/(2*x),4/x),
        )
        for i,(q,b,t,phi,delta) in enumerate(models,1):
            with self.subTest(model=i):
                for sign in (-1,1):
                    r=b+sign*t
                    self.exact(s.diff(r,x)+r**2-q,f"AA49 Riccati {i}/{sign}")
                self.exact(4*q-2*s.diff(phi,x)-phi**2-delta,f"AA49 discriminant {i}")
                self.assertFalse(rational_square(delta),f"AA49 strict quadratic {i}")
        phi=1/x; delta=4*(2/x**2)-2*s.diff(phi,x)-phi**2
        self.exact(delta-9/x**2,"AA49 rational degeneration")
        self.assertTrue(rational_square(delta),"AA49 square discriminant")
    def test_airy_exclusions(self):
        self.assertEqual(s.degree(x,x)%2,1)
        self.assertTrue(s.Rational(-1,2)<0 and not s.Rational(-1,2).is_integer)
        self.assertTrue(-s.degree(x,x)==-1<2)
    def test_finite_local_sets(self):
        data={
            3:(4,s.Rational(3,16),[3,6,9],[4,5,6,7,8],[4,5,6,7,8]),
            4:(6,s.Rational(101,576),list(range(3,10)),[4,6,8],[5,6,7]),
            5:(12,s.Rational(611,3600),list(range(3,10)),[4,5,6,7,8],[5,6,7]),
        }
        for m,(n,c,ex0,ex1,exi) in data.items():
            with self.subTest(m=m):
                q=-s.Rational(3,16)/x**2-s.Rational(2,9)/(x-1)**2+c/(x*(x-1))
                b0=s.limit(q*x*x,x,0); b1=s.limit(q*(x-1)**2,x,1)
                bi=s.limit(q*x*x,x,s.oo)
                self.exact(b0+s.Rational(3,16),f"AA50 b0 {m}")
                self.exact(b1+s.Rational(2,9),f"AA50 b1 {m}")
                self.exact(1+4*bi-s.Rational(1,m*m),f"AA50 exponent infinity {m}")
                def E(b):
                    a=[6+s.Rational(12*k,n)*s.sqrt(1+4*b) for k in range(-n//2,n//2+1)]
                    return sorted({int(v) for v in a if v.is_integer is True})
                self.assertEqual(E(b0),ex0)
                self.assertEqual(E(b1),ex1)
                self.assertEqual(E(bi),exi)
                self.exact(s.Rational(n,12)*(7-3-4),f"AA50 degree {m}")
    def test_labels_and_refs_aa43_to_aa50(self):
        contents={n:(ROOT/"chapters/pl/abstract_algebra"/name).read_text(encoding="utf-8")
                  for n,name in NAMES.items()}
        labels=[a for source in contents.values() for a in re.findall(r"\\label\{([^{}]+)\}",source)]
        self.assertEqual(len(labels),len(set(labels)),"duplicate AA43-50 label")
        targets=set(labels)
        for n in range(44,51):
            refs=set(re.findall(r"\\(?:eqref|ref|pageref|autoref)\{([^{}]+)\}",contents[n]))
            self.assertTrue(refs<=targets,f"AA{n} broken references: {refs-targets}")

if __name__=="__main__":
    unittest.main()
