"""Catalog-wide FA coverage: test the actual parser and exact label resolver."""
import json
from pathlib import Path
import unittest

from backend.label_registry import Owner, qualified_occurrence, resolve
from backend.latex_parser import module_id, parse_document

from distribution_graph_migration import active, restructured, structure_plan

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
        groups = [{mid} for mid in sorted(fa_ids)]
        if active(catalog):
            self.assertGreaterEqual(len(fa_ids), 26)
            inherited = {f"DT-{n:02d}" for n in (1, 2, 3, 4, 5, 7, 8, 9, 10, 11)}
            if restructured():
                plan = structure_plan()
                for old in sorted(inherited):
                    successors = {f"DT-{r['number']:02d}"
                                  for r in plan["chapters"]
                                  if old in r["source_modules"] and r.get("target_path")}
                    self.assertTrue(successors, old)
                    self.assertLessEqual(successors, paths.keys())
                    groups.append(successors)
            else:
                self.assertLessEqual(inherited, paths.keys())
                groups.extend({mid} for mid in sorted(inherited))
        else:
            self.assertGreaterEqual(len(fa_ids), 35)

        config = json.loads((ROOT / "application/config/ALIASY_PO_SCALENIACH.json")
                            .read_text(encoding="utf-8"))
        aliases = {(a["old_document"], a["old_label"]):
                   (a["target_document"], a["target_label"])
                   for a in config["qualified_label_aliases"]}

        count = 0
        for group in groups:
            cross_targets = set()
            for mid in sorted(group):
                doc = load(mid)
                refs = [r for r in doc.references if r.command == "atlasref"]
                for r in refs:
                    with self.subTest(source=mid, line=r.line, label=r.target):
                        qualified = qualified_occurrence(r.target)
                        self.assertIsNotNone(qualified, "FA links must have explicit chapter ownership")
                        target, label = qualified
                        # Direct ownership has priority; otherwise follow the
                        # exact historical pair, not a global label-name search.
                        direct = load(target) if target in paths else None
                        if direct is None or not any(x.name == label for x in direct.labels):
                            target, label = aliases.get((target, label), (target, label))
                        target_doc = load(target)
                        owners = [Owner(target_doc.id, item.name, item.entity_id)
                                  for item in target_doc.labels if item.name == label]
                        self.assertEqual(len(owners), 1, "missing or ambiguous target")
                        decision = resolve(mid, target + "::" + label, owners)
                        self.assertEqual(decision.status, "external_resolved")
                        self.assertEqual(decision.owner, owners[0])
                        self.assertIsNotNone(decision.owner.entity_id)
                        if target.split("-", 1)[0] != mid.split("-", 1)[0]:
                            cross_targets.add((target, label))
            self.assertTrue(cross_targets, f"{group}: no cross-volume reading link")
            count += len(cross_targets)
        # Coverage may grow; the audited baseline must not silently shrink.
        self.assertGreaterEqual(count, 77)
