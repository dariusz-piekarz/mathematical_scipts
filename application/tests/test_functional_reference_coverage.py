"""Catalog-wide FA coverage: test the actual parser and exact label resolver."""
import json
from pathlib import Path
import unittest

from backend.label_registry import Owner, qualified_occurrence, resolve
from backend.latex_parser import module_id, parse_document

ROOT = Path(__file__).resolve().parents[2]


class FunctionalReferenceCoverageTest(unittest.TestCase):
    def test_all_fa_chapters_have_resolvable_cross_volume_reading_links(self):
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

        fa_ids = {mid for mid in paths if mid.startswith("FA-")}
        self.assertGreaterEqual(len(fa_ids), 35)
        count = 0
        for mid in sorted(fa_ids):
            doc = load(mid)
            refs = [r for r in doc.references if r.command == "atlasref"]
            self.assertTrue(refs, f"{mid}: missing thematic reading link")
            cross_targets = set()
            cross_volume = 0
            for r in refs:
                with self.subTest(source=mid, line=r.line, label=r.target):
                    qualified = qualified_occurrence(r.target)
                    self.assertIsNotNone(qualified, "FA links must have explicit chapter ownership")
                    target, label = qualified
                    target_doc = load(target)
                    owners = [Owner(target_doc.id, item.name, item.entity_id)
                              for item in target_doc.labels if item.name == label]
                    self.assertEqual(len(owners), 1, "missing or ambiguous target")
                    decision = resolve(mid, r.target, owners)
                    self.assertEqual(decision.status, "external_resolved")
                    self.assertEqual(decision.owner, owners[0])
                    self.assertIsNotNone(decision.owner.entity_id)
                    if not target.startswith("FA-"):
                        cross_volume += 1
                        cross_targets.add(r.target)
            self.assertGreater(cross_volume, 0, f"{mid}: no cross-volume reading link")
            count += len(cross_targets)
        # Coverage may grow; the audited baseline must not silently shrink.
        self.assertGreaterEqual(count, 77)
