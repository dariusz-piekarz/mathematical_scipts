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
        for row in plan["chapters"]:
            path = row.get("candidate_path")
            if not path:
                self.assertFalse(row["labels"])
                continue
            self.assertNotIn(path, canonical)
            text = (ROOT / path).read_text(encoding="utf-8")
            labels = re.findall(r"\\label\{([^}]+)\}", text)
            self.assertEqual(sorted(labels), sorted(row["labels"]), path)
            self.assertEqual(len(labels), len(set(labels)), path)
            self.assertEqual(len(re.findall(r"(?m)^\\section\{", text)), 1, path)
            self.assertNotRegex(text, r"(?m)^\\setcounter\{section\}", path)
            for label in labels:
                self.assertNotIn(label, actual)
                actual[label] = row["number"]
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
        self.assertEqual(set(actual), set(historical))
        external = set(migration["external_unqualified_labels"])
        for n, label, path in all_refs:
            if label not in external:
                self.assertIn(label, actual, path)
                self.assertLessEqual(actual[label], n, (path, label))

    def test_candidate_master_exact_order(self):
        plan = json.loads(PLAN.read_text(encoding="utf-8"))
        master = (ROOT / plan["candidate_master"]["path"]).read_text(
            encoding="utf-8")
        rows = [r for r in plan["chapters"] if r.get("candidate_path")]
        actual = re.findall(
            r"\\setcounter\{section\}\{(\d+)\}\s*\\input\{\.\./\.\./([^}]+)\}",
            master)
        self.assertEqual([(int(n) + 1, path) for n, path in actual],
                         [(r["number"], r["candidate_path"]) for r in rows])
        self.assertEqual(master.count(r"\input{"), len(rows))
        self.assertEqual(master.count(r"\begin{document}"), 1)
        self.assertEqual(master.count(r"\end{document}"), 1)


if __name__ == "__main__":
    unittest.main()
