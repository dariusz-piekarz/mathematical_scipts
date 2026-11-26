"""CAT-28: finite comonad and comparison models, not formal proofs."""
import itertools
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/pl/category_theory/28-monady-komonady-i-twierdzenie-becka.tex"


class CategoryTheoryCh28(unittest.TestCase):
    def test_CAT_28_001_product_comonad_coalgebras(self):
        for e,n in itertools.product(range(3),repeat=2):
            pairs = list(itertools.product(range(e),range(n)))
            coalgebras = []
            for c in itertools.product(pairs,repeat=n):
                if all(c[x][1]==x and (c[x][0],c[x]) ==
                       (c[x][0],c[c[x][1]]) for x in range(n)):
                    coalgebras.append(c)
            self.assertEqual(set(coalgebras),
                             {tuple(zip(p,range(n)))
                              for p in itertools.product(range(e),repeat=n)})
            for c in coalgebras:
                for m in range(3):
                    # Cofree target (E x M, diagonal): transpose a map
                    # h:X->E x M to its second coordinate.
                    target = list(itertools.product(range(e),range(m)))
                    compatible = {h for h in itertools.product(target,repeat=n)
                                  if all(h[x][0]==c[x][0] for x in range(n))}
                    induced = {tuple((c[x][0],f[x]) for x in range(n))
                               for f in itertools.product(range(m),repeat=n)}
                    self.assertEqual(compatible,induced)

    def test_CAT_28_002_structure(self):
        source=CHAPTER.read_text(encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",source)
        self.assertEqual(len(labels),len(set(labels)))
        all_labels=[]
        for p in CHAPTER.parent.glob("*.tex"):
            all_labels.extend(re.findall(r"\\label\{([^}]+)\}",
                                         p.read_text(encoding="utf-8")))
        for ref in re.findall(r"\\(?:ref|eqref)\{([^}]+)\}",source):
            self.assertEqual(all_labels.count(ref),1,ref)
        stack=[]
        for kind,env in re.findall(r"\\(begin|end)\{([^}]+)\}",source):
            if kind=="begin":
                stack.append(env)
            else:
                self.assertTrue(stack,env)
                self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)
        for m in re.finditer(r"\\end\{(twierdzenie|stwierdzenie|lemat|wniosek)\}",source):
            self.assertTrue(source[m.end():].lstrip().startswith(r"\begin{proof}"))
        self.assertIn(CHAPTER.relative_to(ROOT).as_posix(),
                      (ROOT/"books/pl/category_theory.tex").read_text(encoding="utf-8"))
