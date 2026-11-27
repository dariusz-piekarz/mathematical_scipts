"""MTG-001–003: global terminology and notation source regressions."""
import re
import unittest
from test_measure_theory_book_integrity import corpus, without_comments

# Strip only machine identifiers, not visible titles of hyperlinks.
IDENTIFIER = re.compile(r"\\(?:label|ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\{[^{}]+\}|\\hyperref\[[^\]]+\]")
FORBIDDEN = re.compile(
    r"\\(?:mathbf|mathbb|mathds|mathbbm)\s*\{\s*1\s*\}"
    r"|\\(?:mathds|mathbbm)\s+1\b"
    r"|\bindykator\w*|\bsekwenc\w*|\bzwartościowan\w*"
    r"|\b(?:pierwszo|drugo)[ -]?przeliczaln\w*|\bdual\b"
    r"|\btensorowan\w*|\bzbieżnoś[ćc]\w*\s+zwart\w*|\bseskwilini\w*",
    re.IGNORECASE,
)

class MeasureTheoryGlobal(unittest.TestCase):
    def test_mtg_001_terminology_and_characteristic_functions(self):
        sources = corpus()
        self.assertEqual(len(sources), 34)
        for path, body in sources.items():
            visible = IDENTIFIER.sub("", body)
            with self.subTest(file=path.name):
                self.assertIsNone(FORBIDDEN.search(visible))

    def test_mtg_002_machine_ids_are_not_prose(self):
        body = r"\label{def:dual-lp-15} \ref{def:dual-lp-15} \hyperref[def:dual-lp-15]{Dualność}"
        self.assertIsNone(FORBIDDEN.search(IDENTIFIER.sub("", body)))
        for body in (r"\mathbf{1}_A",r"\mathbb { 1 }", "dual ilorazu",
                     "sekwencja", "drugoprzeliczalna", "tensorowanie",
                     "zbieżność zwarta", "seskwiliniowa", "zwartościowanie",
                     "indykator"):
            self.assertIsNotNone(FORBIDDEN.search(body), body)
        self.assertIsNone(FORBIDDEN.search(r"\chi_A, przestrzeń dualna, ciąg, uzwarcenie"))

    def test_mtg_003_glossary_measure_types(self):
        sources = corpus()
        body = next(s for p,s in sources.items() if p.name == "spis_oznaczen.tex")
        for phrase in (r"Miara zewnętrzna na $\mathcal P(X)$",
                       "mierzalnych w sensie Carathéodory'ego jest miarą",
                       "Miara zewnętrzna Hausdorffa przy ograniczeniu średnic",
                       "ta ostatnia jest miarą na zbiorach borelowskich",
                       r"$\|\nu\|_{\mathrm{sv}}(A)$"):
            self.assertIn(phrase,body)


    def test_mtg_004_reference_dependency_inventory(self):
        # Reference links are candidates, not a formal proof dependency graph.
        sources = {int(p.name[:2]): s for p,s in corpus().items()
                   if re.match(r"\d{2}-",p.name)}
        labels = {m.group(1): (ch,m.start()) for ch,s in sources.items()
                  for m in re.finditer(r"\\label\{([^{}]+)\}",s)}
        token = re.compile(r"\\(begin|end)\{(proof)\}|\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\*?\{([^{}]+)\}")
        edges, forward, unknown = set(), [], []
        for ch,s in sources.items():
            depth=0
            for m in token.finditer(s):
                if m.group(1):
                    depth += 1 if m.group(1)=="begin" else -1
                    continue
                for label in m.group(3).split(","):
                    label=label.strip()
                    if label not in labels:
                        unknown.append((ch,label))
                        continue
                    target,pos=labels[label]
                    if target==ch:
                        continue
                    edges.add((ch,target))
                    if target>ch:
                        line=s.count("\n",0,m.start())+1
                        context=" ".join(s[max(0,m.start()-130):m.end()+100].split())
                        forward.append((ch,target,depth>0,line,label,context))
            self.assertEqual(depth,0)
        self.assertEqual(unknown,[])
        print("MTG dependency inventory:",len(labels),"labels;",len(edges),"distinct cross-chapter edges")
        for row in sorted(forward):
            print("MTG FORWARD",row)
        # Reviewed in CLII: the single proof-context forward link explicitly\n        # rejects using the later additivity theorem; it is not a dependency.\n        self.assertEqual({(ch,target,label) for ch,target,in_proof,line,label,context in forward if in_proof},\n                         {(7,8,"ch:twierdzenia-graniczne")})
        self.assertEqual(len(sources),32)

    def test_mtg_005_title_collision_inventory(self):
        # Equal headings may be deliberate variants; report rather than merge.
        titles={}
        for path,s in corpus().items():
            if not re.match(r"\d{2}-",path.name):
                continue
            for m in re.finditer(r"\\begin\{(definicja|twierdzenie|lemat|wniosek)\}\[([^\n\]]+)\]",s):
                key=(m.group(1)," ".join(m.group(2).split()).casefold())
                titles.setdefault(key,[]).append((path.name[:2],s.count("\n",0,m.start())+1))
        for (kind,title),locations in sorted(titles.items()):
            if len({ch for ch,_ in locations})>1:
                print("MTG TITLE COLLISION",kind,title,locations)
        self.assertGreater(len(titles),300)


    def test_mtg_006_complete_index(self):
        sources=corpus()
        kinds={"definicja":"Definicje","twierdzenie":"Twierdzenia",
               "lemat":"Lematy","wniosek":"Wnioski"}
        expected={}
        for p,s in sources.items():
            if not re.match(r"\d{2}-",p.name):
                continue
            for m in re.finditer(r"\\begin\{(definicja|twierdzenie|lemat|wniosek)\}(?:\[([^\]]*)\])?([\s\S]*?)\\end\{\1\}",s):
                kind,title,body=m.groups()
                label=re.search(r"\\label\{([^}]+)\}",body)
                self.assertIsNotNone(label,(p.name,title))
                self.assertNotIn(label.group(1),expected)
                expected[label.group(1)]=(kinds[kind]," ".join((title or "").split()))
        index=next(s for p,s in sources.items() if p.name=="indeks_definicji_i_twierdzen.tex")
        actual={}
        section=None
        for line in index.splitlines():
            h=re.match(r"\\section\*\{([^}]+)\}",line)
            if h:
                section=h.group(1)
            m=re.match(r"\\hyperref\[([^\]]+)\]\{(.*?)\}\s*&\s*\\ref\*\{([^}]+)\}\s*&\s*\\pageref\*\{([^}]+)\}",line)
            if m:
                lab,title,num,page=m.groups()
                self.assertEqual((lab,lab),(num,page))
                self.assertNotIn(lab,actual)
                actual[lab]=(section," ".join(title.split()))
        self.assertEqual(set(expected),set(actual),
                         (sorted(set(expected)-set(actual)),sorted(set(actual)-set(expected))))
        for lab,(kind,title) in expected.items():
            self.assertEqual(actual[lab][0],kind,lab)
            if title:
                self.assertEqual(actual[lab][1],title,lab)
        self.assertEqual(len(actual),534)

if __name__ == "__main__":
    unittest.main()
