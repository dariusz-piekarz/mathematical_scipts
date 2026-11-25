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
