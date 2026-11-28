"""Exercise the actual Atlas resolver on all historical DT aliases before activation."""
import json
from contextlib import closing
from pathlib import Path
import re
import shutil
import sqlite3
import tempfile
import unittest

from backend.graph_coverage import graph_coverage, reading_reference_issues
from backend.latex_parser import build_database
from distribution_graph_migration import structure_plan, successor_source

ROOT = Path(__file__).resolve().parents[2]


class DistributionRestructureGraphTest(unittest.TestCase):
    def test_all_historical_targets_resolve_in_successor_index(self):
        plan = structure_plan()
        aliases = plan["planned_qualified_aliases"]
        key = "target_path" if plan["status"] == "active" else "candidate_path"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pl"
            for row in plan["chapters"]:
                if not row.get(key):
                    continue
                src = ROOT / row[key]
                dest = root / "distribution_theory" / src.name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dest)

            # Use explicit synthetic reading links; no live source is modified.
            probe = root / "measure_theory" / "99-dt-alias-probe.tex"
            probe.parent.mkdir(parents=True)
            probe.write_text(
                r"\section{Kontrola aliasów DT}" + "\n" +
                "\n".join(r"\atlasref{" + a["old_document"] + "::" +
                          a["old_label"] + "}{Kontrola}" for a in aliases),
                encoding="utf-8")
            alias_path = Path(tmp) / "aliases.json"
            alias_path.write_text(json.dumps({"qualified_label_aliases": aliases}),
                                  encoding="utf-8")
            db = Path(tmp) / "index.db"
            build_database(root, db, alias_path, recursive=True)
            with closing(sqlite3.connect(db)) as con, con:
                rows = con.execute(
                    "SELECT target_label,status,target_document,target_entity "
                    "FROM references_tex WHERE source_document='ME-99' "
                    "AND command='atlasref'").fetchall()
                self.assertEqual(len(rows), len(aliases))
                actual = {r[0]: r[1:] for r in rows}
                self.assertEqual(len(actual), len(aliases))
                for a in aliases:
                    old = a["old_document"] + "::" + a["old_label"]
                    with self.subTest(alias=old):
                        status, owner, entity = actual[old]
                        self.assertEqual(status, "alias_resolved")
                        self.assertEqual(owner, a["target_document"])
                        self.assertIsNotNone(entity)
                        self.assertEqual(con.execute(
                            "SELECT entity_id FROM label_occurrences "
                            "WHERE document_id=? AND name=?",
                            (owner, a["target_label"])).fetchall(), [(entity,)])
                audit = reading_reference_issues(con)
                # The isolated index intentionally excludes external volumes.
                # Only the probe's references must be valid in this test.
                probe_issues = [x for x in audit["issues"]
                                if x.get("source_document", x.get("source")) == "ME-99"]
                self.assertFalse(probe_issues, probe_issues)
                expected = {a["target_document"] for a in aliases}
                edges = {e["target"] for e in graph_coverage(con)["edges"]
                         if e["source"] == "ME-99" and e["reading"] > 0}
                self.assertEqual(edges, expected)

    def test_inherited_outgoing_links_follow_the_split(self):
        plan = structure_plan()
        baseline = plan["historical_outgoing_links"]["by_document"]
        migration = json.loads((ROOT / "catalog/distribution_theory_migration.json")
                               .read_text(encoding="utf-8"))
        self.assertEqual(set(baseline), {c["id"] for c in migration["chapters"]})
        key = "target_path" if plan["status"] == "active" else "candidate_path"
        # The baseline was extracted from the pre-activation revision.
        # It remains independently checkable after removing obsolete files.
        for chapter in migration["chapters"]:
            old_id = chapter["id"]
            links = set(baseline[old_id])
            if plan["status"] != "active":
                text = (ROOT / chapter["target_path"]).read_text(encoding="utf-8")
                self.assertEqual(links, set(re.findall(r"\\atlasref\{([^}]+)\}", text)),
                                 old_id)
            successors = [r for r in plan["chapters"]
                          if old_id in r["source_modules"] and r.get(key)]
            self.assertTrue(successors, old_id)
            combined = "\n".join((ROOT / r[key]).read_text(encoding="utf-8")
                                 for r in successors)
            self.assertLessEqual(links, set(re.findall(r"\\atlasref\{([^}]+)\}", combined)),
                                 old_id)
        for old, qualified, new in (
            ("DT-01", "PDE-08::thm:pde8-inversion", "DT-09"),
            ("DT-04", "PDE-07::def:pde7-derivative", "DT-05"),
            ("DT-05", "PDE-07::thm:pde7-mollify", "DT-07"),
            ("DT-07", "PDE-08::def:pde8-distFT", "DT-10"),
            ("DT-08", "GT-07::thm:topog-zwartosc-sieci", "DT-17"),
            ("DT-09", "AA-18::aa:tw:tensor-universal", "DT-18"),
            ("DT-10", "LA-10::thm:lin10-istnienie", "DT-19"),
            ("DT-11", "KAT-09::cat:ex:tensor-rep", "DT-20"),
        ):
            self.assertEqual(successor_source(old, qualified), new)


if __name__ == "__main__":
    unittest.main()
