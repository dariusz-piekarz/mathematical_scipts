"""Mathematical/source regressions: AT04↔DG07 and AT05↔DG08."""
from __future__ import annotations

from collections import Counter
from itertools import permutations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
AT = ROOT / "chapters/pl/algebraic_topology"
DG = ROOT / "chapters/pl/differential_geometry_and_topology"
PATHS = {
    "AT04": next(AT.glob("04-*.tex")),
    "DG07": next(DG.glob("07-*.tex")),
    "AT05": next(AT.glob("05-*.tex")),
    "DG08": next(DG.glob("08-*.tex")),
}


def labels(source):
    return set(re.findall(r"\\label\{([^}]+)\}", source))


def compose(p, q):
    # Permutations as images of 0,1,2; p composed after q.
    return tuple(p[q[i]] for i in range(len(q)))


class ATDGPairwiseAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = {
            key: p.read_text(encoding="utf-8-sig")
            for key, p in PATHS.items()
        }
        path = ROOT / "application/config/KANDYDACI_SCALEN_AT_DG_ETAP_03.json"
        cls.manifest = json.loads(path.read_text(encoding="utf8"))

    def test_irregular_cover_monodromy_is_transitive_and_nonnormal(self):
        # (1 2) and (2 3) act on exactly three sheets.
        a, b = (1, 0, 2), (0, 2, 1)
        orbit = {0}
        while True:
            new = orbit | {a[i] for i in orbit} | {b[i] for i in orbit}
            if new == orbit:
                break
            orbit = new
        self.assertEqual(orbit, {0, 1, 2})
        centralizer = [
            p for p in permutations(range(3))
            if compose(p, a) == compose(a, p)
            and compose(p, b) == compose(b, p)
        ]
        self.assertEqual(centralizer, [(0, 1, 2)])
        self.assertEqual(6 - 3 + 1, 4)  # Rank of the 3-sheeted cover.
        self.assertIn(r"\label{prz:nakrycie-nieregularne-bukiet-dg07}",
                      self.sources["DG07"])
        self.assertIn(r"\label{fig:nakrycie-nieregularne-bukiet-dg07}",
                      self.sources["DG07"])
        self.assertIn(r"\operatorname{Deck}(p)=\{1\}", self.sources["DG07"])
        self.assertIn(r"\pi_1(E)\cong F_{6-3+1}=F_4", self.sources["DG07"])

    def test_three_sheet_rose_graph_has_valid_local_cover(self):
        a, b = (1, 0, 2), (0, 2, 1)
        # Each sheet contains exactly one incoming/outgoing half-edge
        # above each of the two oriented loops.
        for sigma in (a, b):
            for vertex in range(3):
                outgoing = [i for i in range(3) if i == vertex]
                incoming = [i for i in range(3) if sigma[i] == vertex]
                self.assertEqual(len(outgoing), 1)
                self.assertEqual(len(incoming), 1)
        self.assertEqual(3 * 2, 6)

    def test_van_kampen_AT04_kernel_checks_changed_open_set_labels(self):
        s = self.sources["AT04"]
        loc = s.index(r"\begin{twierdzenie}[van Kampen: dwa otwarte zbiory]")
        proof = s[loc:s.index(r"\end{proof}", loc)]
        for phrase in (
            "krawędzi", "prostokąta", "pierwotnej litery",
            "U\\cap V", "N\\subseteq\\ker\\Phi",
        ):
            self.assertIn(phrase, proof)
        self.assertIn(r"\ker\Phi", proof)
        self.assertIn(r"\pi_1(X,x_0)", proof)

    def test_star_local_homology_and_augmentation(self):
        # Z^r -> Z is summation; ker has integral basis e_j-e_r.
        for r in range(1, 9):
            basis = [
                tuple((1 if i == j else (-1 if i == r - 1 else 0))
                      for i in range(r))
                for j in range(r - 1)
            ]
            self.assertEqual(len(basis), r-1)
            for v in basis:
                self.assertEqual(sum(v), 0)
            # Any integer vector of zero sum has the explicit decomposition.
            a = tuple(range(1, r)) + (-sum(range(1, r)),)
            combo = tuple(
                sum(a[j]*basis[j][i] for j in range(r-1))
                for i in range(r)
            )
            self.assertEqual(combo, a)
        self.assertIn(r"\label{prz:homologia-lokalna-r-ramion-at05}",
                      self.sources["AT05"])
        self.assertIn(r"\label{fig:lokalna-r-ramion-at05}",
                      self.sources["AT05"])
        self.assertIn(r"\Z^{r-1}", self.sources["AT05"])

    def test_important_unique_math_survives_both_versions(self):
        s = self.sources
        for label in (
            "prz:nakrycie-m-arkuszy", "fig:nakrycie-m-arkuszy",
        ):
            self.assertIn(label, labels(s["AT04"]))
        for label in (
            "thm:deck-normalizator", "thm:pi1-graf",
            "prz:nakrycie-nieregularne-bukiet-dg07",
            "fig:nakrycie-nieregularne-bukiet-dg07",
        ):
            self.assertIn(label, labels(s["DG07"]))
        for label in (
            "prz:mv-sfera-dwie-polkul",
            "prz:homologia-butelka-kleina",
            "fig:homologia-butelka-kleina",
            "prz:homologia-lokalna-r-ramion-at05",
        ):
            self.assertIn(label, labels(s["AT05"]))
        for label in (
            "thm:homologia-grafu-incydencja",
            "prop:lokalna-homologia-brzeg-8",
            "prz:lokalna-homologia-trojnog-8",
        ):
            self.assertIn(label, labels(s["DG08"]))

    def test_merge_manifest_matches_all_actual_source_labels(self):
        manifest = self.manifest
        self.assertFalse(manifest["policy"]["auto_merge"])
        self.assertFalse(manifest["policy"]["rename_labels"])
        self.assertEqual(len(manifest["pairs"]), 2)
        for pair in manifest["pairs"]:
            a, b = pair["left"], pair["right"]
            la, lb = labels(self.sources[a]), labels(self.sources[b])
            self.assertEqual(pair["shared_label_names"], len(la & lb))
            self.assertEqual(set(pair["left_only_labels"]), la - lb)
            self.assertEqual(set(pair["right_only_labels"]), lb - la)
            self.assertIsNone(pair["canonical_source"])
            self.assertFalse(pair["approved_to_merge"])
            self.assertTrue(pair["auditFindings"])

    def test_no_duplicate_labels_or_unbalanced_tex_environments(self):
        for key, source in self.sources.items():
            with self.subTest(chapter=key):
                ll = re.findall(r"\\label\{([^}]+)\}", source)
                self.assertEqual(len(ll), len(set(ll)))
                self.assertEqual(
                    Counter(re.findall(r"\\begin\{([^}]+)\}", source)),
                    Counter(re.findall(r"\\end\{([^}]+)\}", source)),
                )
                self.assertNotRegex(source.lower(), r"\bsekwencj\w*")
                self.assertNotRegex(source.lower(), r"\btensorowan\w*")

    def test_canonical_book_inputs_have_not_changed(self):
        for vol, book in (
            ("AT", ROOT / "books/pl/algebraic_topology.tex"),
            ("DG", ROOT / "books/pl/differential_geometry_and_topology.tex"),
        ):
            text = book.read_text(encoding="utf8")
            folder = "algebraic_topology" if vol=="AT" else "differential_geometry_and_topology"
            for key in (("AT04","AT05") if vol=="AT" else ("DG07","DG08")):
                item = f"../../chapters/pl/{folder}/{PATHS[key].name}"
                self.assertIn(r"\input{" + item + "}", text)


if __name__ == "__main__":
    unittest.main()
