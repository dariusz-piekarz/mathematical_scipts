"""Verify the candidate layout without activating it in the Atlas catalog."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "catalog/distribution_theory_structure_plan.json"
MIGRATION = ROOT / "catalog/distribution_theory_migration.json"


class DistributionRestructureTest(unittest.TestCase):
    def test_candidate_coverage_and_reference_order(self):
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        migration = json.loads(MIGRATION.read_text(encoding="utf-8"))
        historical = {label: row["id"] for row in migration["chapters"]
                      for label in row["labels"]}
        mapping = {row["label"]: row for row in plan["label_map"]}
        self.assertEqual(len(mapping), len(plan["label_map"]))
        self.assertEqual(set(mapping), set(historical))
        actual = {}
        all_refs = []
        active = json.loads((ROOT / "catalog/books.json").read_text(
            encoding="utf-8"))["books"]
        canonical = {p for book in active for p in book["chapters"]}
        switched = plan["status"] == "active"
        key = "target_path" if switched else "candidate_path"
        for row in plan["chapters"]:
            path = row.get(key)
            if not path:
                self.assertFalse(row["labels"])
                continue
            if switched:
                self.assertIn(path, canonical)
            else:
                self.assertNotIn(path, canonical)
            text = (ROOT / path).read_text(encoding="utf-8")
            labels = re.findall(r"\\label\{([^}]+)\}", text)
            self.assertLessEqual(set(row["labels"]), set(labels), path)
            if not switched:
                self.assertEqual(sorted(labels), sorted(row["labels"]), path)
            self.assertEqual(len(labels), len(set(labels)), path)
            self.assertEqual(len(re.findall(r"(?m)^\\section\{", text)), 1, path)
            self.assertNotRegex(text, r"(?m)^\\setcounter\{section\}", path)
            prose = "\n".join(line for line in text.splitlines()
                              if not line.lstrip().startswith("%"))
            self.assertNotRegex(
                prose, r"rozdzia[łl][a-ząćęłńóśźż]*[~ ]+\d", path)
            for label in labels:
                self.assertNotIn(label, actual)
                actual[label] = row["number"]
                if label in mapping:
                    self.assertEqual(mapping[label]["old_document"], historical[label])
                    self.assertEqual(mapping[label]["planned_chapter"], row["number"])
            for hit in re.finditer(
                r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]",
                text
            ):
                all_refs.append((row["number"], hit.group(1) or hit.group(2), path))
            stack = []
            for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
                if match[1] == "begin":
                    stack.append(match[2])
                else:
                    self.assertTrue(stack, path)
                    self.assertEqual(stack.pop(), match[2], path)
            self.assertFalse(stack, path)
        self.assertLessEqual(set(historical), set(actual))
        if not switched:
            self.assertEqual(set(actual), set(historical))
        external = set(migration["external_unqualified_labels"])
        for n, label, path in all_refs:
            if label not in external:
                self.assertIn(label, actual, path)
                self.assertLessEqual(actual[label], n, (path, label))

    def test_planned_aliases_are_flat_and_exact(self):
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        migration = json.loads(MIGRATION.read_text(encoding="utf-8"))
        config = json.loads((ROOT / "application/config/ALIASY_PO_SCALENIACH.json")
                            .read_text(encoding="utf-8"))
        owners = {label: f"DT-{row['number']:02d}"
                  for row in plan["chapters"] for label in row["labels"]}
        canonical = {(owner, label) for label, owner in owners.items()}
        expected = {}
        for row in migration["qualified_label_aliases"]:
            expected[row["old_document"], row["old_label"]] = (
                owners[row["target_label"]], row["target_label"])
        for row in plan["label_map"]:
            label = row["label"]
            if row["old_document"] != owners[label]:
                expected[row["old_document"], label] = (owners[label], label)
        actual = {}
        for row in plan["planned_qualified_aliases"]:
            key = row["old_document"], row["old_label"]
            target = row["target_document"], row["target_label"]
            self.assertNotIn(key, actual)
            self.assertNotIn(key, canonical)
            self.assertIn(target, canonical)
            self.assertEqual(key[1], target[1])
            actual[key] = target
        self.assertEqual(actual, expected)
        self.assertFalse(set(actual).intersection(actual.values()),
                         "aliases must point directly to canonical labels")
        self.assertEqual(sum(k[0].startswith("FA-") for k in actual), 211)
        self.assertEqual(sum(k[0].startswith("DT-") for k in actual), 224)
        unrelated = {(a["old_document"], a["old_label"])
                     for a in config["qualified_label_aliases"]
                     if not a["target_document"].startswith("DT-")}
        self.assertFalse(unrelated.intersection(actual))
        # During staging, the live FA aliases still point at the old DT owners.
        installed = {(a["old_document"], a["old_label"],
                      a["target_document"], a["target_label"])
                     for a in config["qualified_label_aliases"]}
        self.assertTrue(all((a["old_document"], a["old_label"],
                             a["target_document"], a["target_label"]) in installed
                            for a in (plan["planned_qualified_aliases"]
                                      if plan["status"] == "active"
                                      else migration["qualified_label_aliases"])))

    def test_candidate_master_exact_order(self):
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        switched = plan["status"] == "active"
        master_path = "books/pl/distribution_theory.tex" if switched else plan["candidate_master"]["path"]
        key = "target_path" if switched else "candidate_path"
        master = (ROOT / master_path).read_text(encoding="utf-8")
        rows = [r for r in plan["chapters"] if r.get(key)]
        actual = re.findall(
            r"\\setcounter\{section\}\{(\d+)\}\s*\\input\{\.\./\.\./([^}]+)\}",
            master)
        self.assertEqual([(int(n) + 1, path) for n, path in actual],
                         [(r["number"], r[key]) for r in rows])
        self.assertEqual(master.count(r"\input{"), len(rows))
        self.assertEqual(master.count(r"\begin{document}"), 1)
        self.assertEqual(master.count(r"\end{document}"), 1)


if __name__ == "__main__":
    unittest.main()
