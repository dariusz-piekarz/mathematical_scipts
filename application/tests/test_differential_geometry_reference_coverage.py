"""Check every canonical DG reading reference with the production parser and resolver."""
from collections import Counter
import json
from pathlib import Path
import unittest

from backend.label_registry import Owner, qualified_occurrence, resolve
from backend.latex_parser import module_id, parse_document

ROOT = Path(__file__).resolve().parents[2]


class DifferentialGeometryReferenceCoverageTest(unittest.TestCase):
    def test_all_existing_dg_reading_links_resolve(self):
        catalog = json.loads((ROOT / "catalog/books.json").read_text(encoding="utf-8"))
        paths = {}
        for book in catalog["books"]:
            for filename in book["chapters"]:
                mid = module_id(Path(filename))
                self.assertNotIn(mid, paths, f"duplicate catalog ID: {mid}")
                paths[mid] = filename

        parsed = {}

        def load(mid):
            if mid not in parsed:
                self.assertIn(mid, paths)
                filename = paths[mid]
                parsed[mid] = parse_document(
                    (ROOT / filename).read_text(encoding="utf-8-sig"), filename)
                self.assertEqual(parsed[mid].id, mid)
            return parsed[mid]

        dg_ids = {mid for mid in paths if mid.startswith("DG-")}
        self.assertTrue({f"DG-{i:02d}" for i in range(1, 21)} <= dg_ids)
        linked = set()
        count = 0
        domains = set()
        for mid in sorted(dg_ids):
            doc = load(mid)
            refs = [r for r in doc.references if r.command == "atlasref"]
            occurrences = Counter(r.target for r in refs)
            for r in refs:
                with self.subTest(source=mid, line=r.line, target=r.target):
                    qualified = qualified_occurrence(r.target)
                    self.assertIsNotNone(qualified)
                    target, label = qualified
                    self.assertEqual(occurrences[r.target], 1)
                    target_doc = load(target)
                    owners = [Owner(target_doc.id, item.name, item.entity_id)
                              for item in target_doc.labels if item.name == label]
                    self.assertEqual(len(owners), 1, "missing or ambiguous target")
                    decision = resolve(mid, r.target, owners)
                    self.assertEqual(decision.status, "external_resolved")
                    self.assertEqual(decision.owner, owners[0])
                    self.assertIsNotNone(decision.owner.entity_id)
                    if not target.startswith("DG-"):
                        linked.add(mid)
                        count += 1
                        domains.add(target.split("-")[0])
        # Preserve the audited baseline without inventing links to meet a quota.
        self.assertTrue({f"DG-{i:02d}" for i in range(1, 21)} <= linked)
        self.assertGreaterEqual(count, 35)
        self.assertTrue({"AA", "FA", "KAT", "LA", "ME", "TOP"} <= domains)

        reciprocal = (
            ("AA-57", "DG-02", "fakt:nawias-wlasnosci"),
            ("FA-14", "DG-12", "def:pochodna-wzdluz-krzywej"),
            ("FA-15", "DG-13", "thm:wspolrzedne-normalne"),
            ("ME-27", "DG-14", "thm:bishop-gromov"),
        )
        for source, target, label in reciprocal:
            with self.subTest(source=source, target=target, label=label):
                ref = target + "::" + label
                self.assertEqual(sum(r.command == "atlasref" and r.target == ref
                                     for r in load(source).references), 1)
                owners = [Owner(target, item.name, item.entity_id)
                          for item in load(target).labels if item.name == label]
                self.assertEqual(len(owners), 1)
                decision = resolve(source, ref, owners)
                self.assertEqual(decision.status, "external_resolved")
                self.assertEqual(decision.owner, owners[0])
                self.assertIsNotNone(decision.owner.entity_id)


if __name__ == "__main__":
    unittest.main()
