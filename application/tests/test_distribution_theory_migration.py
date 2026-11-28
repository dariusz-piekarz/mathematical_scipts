"""Guard the DT migration against lost labels and partial catalog activation."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8-sig"))


def labels(path):
    return re.findall(r"\\label\s*\{([^{}]+)\}",
                      (ROOT / path).read_text(encoding="utf-8-sig"))


def alias_key(entry):
    return tuple(entry[k] for k in
                 ("old_document", "old_label", "target_document", "target_label"))


class DistributionTheoryMigrationTest(unittest.TestCase):
    def test_preservation_and_atomic_catalog_switch(self):
        migration = read_json("catalog/distribution_theory_migration.json")
        chapters = migration["chapters"]
        aliases = migration["qualified_label_aliases"]
        catalog = read_json("catalog/books.json")
        registered = [p for book in catalog["books"] for p in book["chapters"]]
        targets = {c["target_path"] for c in chapters}
        staged = {c["staged_path"] for c in chapters}
        active = targets.intersection(registered)
        self.assertIn(len(active), (0, len(targets)), "partial DT activation")
        self.assertFalse(staged.intersection(registered))
        self.assertEqual(len(targets), 19)
        self.assertEqual([c["id"] for c in chapters],
                         [f"DT-{i:02d}" for i in range(1, 20)])

        owners = {}
        for chapter in chapters:
            path = chapter["target_path"] if active else chapter["staged_path"]
            actual = labels(path)
            self.assertEqual(len(actual), len(set(actual)), path)
            if active:
                self.assertLessEqual(set(chapter["labels"]), set(actual), path)
            else:
                self.assertCountEqual(chapter["labels"], actual, path)
            for label in actual:
                self.assertNotIn(label, owners, f"duplicate DT label: {label}")
                owners[label] = chapter["id"]
        self.assertGreaterEqual(len(owners), 265)

        old_ids = {f"FA-{i:02d}" for i in range(17, 26)}
        self.assertEqual({a["old_document"] for a in aliases}, old_ids)
        keys = {(a["old_document"], a["old_label"]) for a in aliases}
        self.assertEqual(len(keys), len(aliases))
        self.assertEqual(len(keys), 211)
        for a in aliases:
            self.assertEqual(a["old_label"], a["target_label"])
            self.assertEqual(owners.get(a["target_label"]), a["target_document"])

        originals = {}
        for path in registered:
            match = re.fullmatch(r"chapters/pl/functional_analysis/(1[789]|2[0-5])-[^/]+\.tex", path)
            if match:
                old_id = "FA-" + match.group(1)
                self.assertNotIn(old_id, originals)
                originals[old_id] = path

        if active:
            self.assertFalse(originals, "old FA copies still registered")
            config = read_json("application/config/ALIASY_PO_SCALENIACH.json")
            configured = {alias_key(a) for a in config["qualified_label_aliases"]}
            self.assertLessEqual({alias_key(a) for a in aliases}, configured)
            dt = [b for b in catalog["books"] if targets.intersection(b["chapters"])]
            self.assertEqual(len(dt), 1)
            self.assertLessEqual(targets, set(dt[0]["chapters"]))
        else:
            self.assertEqual(set(originals), old_ids)
            old_labels = [(mid, label) for mid, path in originals.items()
                          for label in labels(path)]
            self.assertCountEqual(old_labels, list(keys))


if __name__ == "__main__":
    unittest.main()
