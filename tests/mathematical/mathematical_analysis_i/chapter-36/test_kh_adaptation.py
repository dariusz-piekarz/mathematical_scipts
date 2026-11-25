from pathlib import Path
from fractions import Fraction as F
import re
import unittest


ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "chapters/pl/mathematical_analysis_i/36-calka-kurzweila-henstocka.tex"
MAP = ROOT / "audits/mathematical_analysis_i/ch36_source_map.md"


class Chapter36(unittest.TestCase):
    def test_label_uniqueness_and_local_references(self):
        source=SOURCE.read_text(encoding="utf8")
        labels=re.findall(r"\\label\{([^}]+)\}",source)
        self.assertEqual(len(labels),len(set(labels)))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",source):
            if ref.startswith("ma1:kh:"):
                self.assertIn(ref,labels)

    def test_external_local_references(self):
        source=SOURCE.read_text(encoding="utf8")
        all_sources="\n".join(p.read_text(encoding="utf8") for p in
            (ROOT/"chapters/pl/mathematical_analysis_i").glob("*.tex"))
        labels=set(re.findall(r"\\label\{([^}]+)\}",all_sources))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",source):
            self.assertIn(ref,labels)

    def test_book_and_catalog_integration(self):
        import json
        rel="chapters/pl/mathematical_analysis_i/36-calka-kurzweila-henstocka.tex"
        book=(ROOT/"books/pl/mathematical_analysis_i.tex").read_text(encoding="utf8")
        self.assertEqual(book.count("\\input{../../"+rel+"}"),1)
        self.assertLess(book.index("35-kwadratury-numeryczne.tex"),book.index(rel))
        catalog=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf8"))
        chapters=[c for b in catalog["books"] for c in b.get("chapters",[])]
        self.assertEqual(chapters.count(rel),1)

    def test_weighted_regularity_budget(self):
        eps,eta,h=F(1,10),F(1,100),F(1,3)
        for m in (1,5,20):
            weights=[F(1,3*2**abs(k)) for k in range(-m,m+1)]
            self.assertEqual(sum(weights),1-F(2,3*2**m))
            errors=[w*min(eta/2,eps/(6*(1+abs(k*h)+h)))
                    for k,w in zip(range(-m,m+1),weights)]
            self.assertLess(sum(errors),eta/2)
            self.assertLess(sum((abs(k*h)+h)*e for k,e in
                                zip(range(-m,m+1),errors)),eps/6)

    def test_source_label_map(self):
        mapping=re.findall(r"^\| ([^| ]+) \| (ma1:kh:[^| ]+) \|$",MAP.read_text(encoding="utf8"),re.M)
        self.assertGreaterEqual(len(mapping),29)
        source=SOURCE.read_text(encoding="utf8")
        originals="\n".join(p.read_text(encoding="utf8") for p in
            (ROOT/"chapters/pl/integration_theory").glob("*.tex"))
        for old,new in mapping:
            self.assertIn("\\label{"+old+"}",originals)
            self.assertIn("\\label{"+new+"}",source)
            self.assertNotIn("\\label{"+old+"}",source)

    def test_gauge_diagram_enclosure(self):
        # Coordinates of the three cells in the TikZ example.
        cells=[(F(0),F(2),F(1),F(6,5)),
               (F(2),F(24,5),F(16,5),F(17,10)),
               (F(24,5),F(7),F(6),F(7,5))]
        for u,v,t,d in cells:
            self.assertTrue(t-d<u<=t<=v<t+d)

    def test_repeated_tags_at_shared_endpoint(self):
        t=F(1,2)
        intervals=[(F(3,8),t),(t,F(5,8))]
        d=F(1,5)
        self.assertTrue(all(t-d<u<=t<=v<t+d for u,v in intervals))
        self.assertLess(sum(v-u for u,v in intervals),2*d)

    def test_dyadic_example_partial_cell(self):
        for n in range(1,10):
            a=F((-1)**(n+1),n)
            u,v=F(1,2**n),F(1,2**(n-1))
            for c in (u,(u+v)/2,v):
                self.assertLessEqual(abs(2**n*a*(v-c)),abs(a))
            self.assertEqual(2**n*a*(v-u),a)

    def test_stieltjes_summation_by_parts(self):
        x=[F(0),F(1,4),F(1,2),F(1)]
        fun=lambda t:t*t
        g=lambda t:F(1) if t>=F(1,2) else F(0)
        left=sum(g(u)*(fun(v)-fun(u)) for u,v in zip(x,x[1:]))
        right=sum(fun(v)*(g(v)-g(u)) for u,v in zip(x,x[1:]))
        self.assertEqual(left+right,fun(x[-1])*g(x[-1])-fun(x[0])*g(x[0]))

    def test_decreasing_substitution_sign(self):
        # Simpson is exact for the transformed polynomial - (1-t)^2.
        f=lambda x:x*x
        phi=lambda t:1-t
        q=lambda t:-f(phi(t))
        transformed=(q(F(0))+4*q(F(1,2))+q(F(1)))/6
        original=(f(F(0))+4*f(F(1,2))+f(F(1)))/6
        self.assertEqual(transformed,-original)
        self.assertEqual(original,F(1,3))

    def test_oscillatory_threshold_witnesses(self):
        # On [k*pi,(k+1)*pi], integral t*sin(t) equals
        # (-1)^k (2*k+1)*pi, and the bound is 2*k*pi.
        from math import pi
        for k in range(1,12):
            exact=abs((-1)**k*(2*k+1)*pi)
            self.assertGreaterEqual(exact,2*k*pi)
        # For -1 <= beta < 0, (k+1)^beta >= 1/(k+1).
        for beta in (-1,-0.75,-0.5,-0.25):
            for k in range(1,50):
                self.assertGreaterEqual((k+1)**beta,1/(k+1))

    def test_derivative_remainder_telescope(self):
        endpoints=[F(0),F(1,5),F(1,2),F(1)]
        tags=[F(1,10),F(1,3),F(3,4)]
        errors=[]
        for u,v,t in zip(endpoints,endpoints[1:],tags):
            errors.append(2*t*(v-u)-(v*v-u*u))
            self.assertLessEqual(abs(errors[-1]),(v-u)**2)
        self.assertEqual(sum(errors),sum(2*t*(v-u)
                         for u,v,t in zip(endpoints,endpoints[1:],tags))-1)


if __name__=="__main__":
    unittest.main()
