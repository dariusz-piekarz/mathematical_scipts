"""CAT-00 regression criteria. Finite models do not replace semantic proofs."""
import itertools
import re
import unittest
from pathlib import Path

CHAPTER = Path(__file__).resolve().parents[2] / "chapters/pl/category_theory/00-po-co-teoria-kategorii.tex"

class CategoryTheoryCh00(unittest.TestCase):
    def test_CAT_00_001_product(self):
        # sec:motywacja: existence and uniqueness in finite cyclic groups.
        for a, b in itertools.product(range(2), range(4)):
            h = tuple((a*x % 2, b*x % 4) for x in range(4))
            for x, y in itertools.product(range(4), repeat=2):
                self.assertEqual(h[(x+y)%4], ((h[x][0]+h[y][0])%2, (h[x][1]+h[y][1])%4))
            candidates = [u for u in itertools.product(itertools.product(range(2), range(4)), repeat=4)
                          if all(u[x][0] == a*x%2 and u[x][1] == b*x%4 for x in range(4))]
            self.assertEqual(candidates, [h])

    def test_CAT_00_002_meet(self):
        # cat:ex:motywacja-porzadek: intersection is a meet.
        for a,b,x in itertools.product(range(8), repeat=3):
            self.assertEqual((x&a == x and x&b == x), x&(a&b) == x)

    def test_CAT_00_003_no_terminal_injections(self):
        # cat:ex:motywacja-morfizmy: singleton and doubleton obstruction.
        for n in range(6):
            self.assertFalse(len(list(itertools.permutations(range(n),1))) == 1 and
                             len(list(itertools.permutations(range(n),2))) == 1)

    def test_CAT_00_004_structure(self):
        s = CHAPTER.read_text(encoding="utf-8")
        for label in ("sec:motywacja","cat:ex:motywacja-porzadek","cat:ex:motywacja-morfizmy"):
            self.assertEqual(s.count(r"\label{" + label + "}"),1)
        stack = []
        for cmd,name in re.findall(r"\\(begin|end)\{([^}]+)\}",s):
            if cmd == "begin":
                stack.append(name)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(),name)
        self.assertFalse(stack)
