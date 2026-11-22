"""Tests for opt-in, provenance-bound Lean constant-expression inspection.

Simulated executions are NOT actual Lean/kernel verification.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from fastapi import HTTPException
from backend import lean_introspection as inspection

SOURCE = "\\begin{twierdzenie}\\label{t:x}\nP.\n\\end{twierdzenie}\n"
TOKEN = "a" * 32
LABEL_OFFSET = SOURCE.index("\\label{t:x}")


def transcript(*, token=TOKEN, name="theorem_x", constants=("Nat.zero", "Eq")):
    lines = [f"{token} BEGIN {name} {len(constants)}"]
    lines.extend(f"{token} CONST {name} {dep}" for dep in constants)
    lines.append(f"{token} END {name}")
    return "Inspect.lean:45:0: info: " + ("\nInspect.lean:45:0: info: ".join(lines))


def classified_transcript():
    events = [
        f"{TOKEN} BEGIN theorem_x 2",
        f"{TOKEN} CONST theorem_x Nat.zero",
        f"{TOKEN} CONST theorem_x Eq",
        f"{TOKEN} END theorem_x",
        f"{TOKEN} TYPE_BEGIN theorem_x 1",
        f"{TOKEN} TYPE_CONST theorem_x Eq",
        f"{TOKEN} TYPE_END theorem_x",
        f"{TOKEN} VALUE_BEGIN theorem_x 1",
        f"{TOKEN} VALUE_CONST theorem_x Nat.zero",
        f"{TOKEN} VALUE_END theorem_x",
    ]
    return "\n".join("Inspect.lean:15:0: info: " + e for e in events)


class ParsingTests(unittest.TestCase):
    def test_fixed_commands_include_actual_metaprogram_introspection(self):
        code = inspection.make_instrumentation(["theorem_x"], TOKEN)
        self.assertIn("run_meta do", code)
        self.assertIn("open Lean Meta", code)
        self.assertIn("getConstInfo "+chr(96)+"theorem_x", code)
        self.assertIn("getUsedConstantsAsSet", code)
        self.assertIn(TOKEN+" BEGIN theorem_x", code)
        with self.assertRaises(ValueError):
            inspection.make_instrumentation(["bad; #eval IO.println"], TOKEN)
        with self.assertRaises(ValueError):
            inspection.make_instrumentation(["theorem_x", "theorem_x"], TOKEN)

    def test_parser_rejects_empty_duplicate_and_invalid_expected_declarations(self):
        # An empty expected set used to produce an apparently complete result
        # from an empty log, without any actual Lean declaration evidence.
        for names in ([], ["theorem_x", "theorem_x"],
                      ["theorem_x", "foreign; #eval"],
                      ["theorem_x"] * (inspection.MAX_THEOREMS + 1)):
            with self.subTest(names=names), self.assertRaises(ValueError):
                inspection.parse_inspection("", TOKEN, names)
        with self.assertRaises(ValueError):
            inspection.parse_inspection(transcript(), TOKEN, [])

    def test_classified_instrumentation_uses_actual_type_and_value_expressions(self):
        code = inspection.make_instrumentation(["theorem_x"], TOKEN, classified=True)
        self.assertIn("info.type.getUsedConstantsAsSet.toList", code)
        self.assertIn("info.value? true", code)
        self.assertIn(f"{TOKEN} TYPE_BEGIN theorem_x", code)
        self.assertIn(f"{TOKEN} VALUE_BEGIN theorem_x", code)

    def test_classified_parser_requires_complete_consistent_origin_protocol(self):
        valid = classified_transcript()
        result = inspection.parse_classified_inspection(valid, TOKEN, ["theorem_x"])
        self.assertEqual(result["constants"], {"theorem_x": ["Eq", "Nat.zero"]})
        self.assertEqual(result["type_constants"], {"theorem_x": ["Eq"]})
        self.assertEqual(result["value_constants"], {"theorem_x": ["Nat.zero"]})
        self.assertEqual(result["reference_edges"], [
            {"declaration": "theorem_x", "constant": "Eq", "origin": "type"},
            {"declaration": "theorem_x", "constant": "Nat.zero", "origin": "value"},
        ])
        for broken in (
            valid.replace(f"{TOKEN} TYPE_END theorem_x", ""),
            valid.replace(f"{TOKEN} VALUE_END theorem_x", ""),
            valid.replace(f"{TOKEN} TYPE_BEGIN theorem_x 1",
                          f"{TOKEN} TYPE_BEGIN theorem_x 3"),
            valid.replace(f"{TOKEN} VALUE_CONST theorem_x Nat.zero",
                          f"{TOKEN} VALUE_CONST theorem_x Nat.succ"),
            valid + f"\n{TOKEN} VALUE_END theorem_x",
            valid + f"\n{TOKEN} OTHER theorem_x 0",
            valid + f"\n{TOKEN} TYPE_BEGIN foreign 0",
            valid.replace(f"{TOKEN} CONST theorem_x Nat.zero", ""),
        ):
            with self.subTest(log=broken[-100:]), self.assertRaises(ValueError):
                inspection.parse_classified_inspection(broken, TOKEN, ["theorem_x"])

    def test_classified_two_declarations_interleaved_with_shared_and_empty_values(self):
        a, b = "theorem_x", "theorem_y"
        # The same constant can be referenced by both type and proof. A
        # declaration without a readable value still needs BEGIN 0 / END.
        events = [
            f"{TOKEN} BEGIN {b} 1",
            f"{TOKEN} BEGIN {a} 2",
            f"{TOKEN} CONST {a} Eq",
            f"{TOKEN} CONST {b} Eq",
            f"{TOKEN} CONST {a} Nat.zero",
            f"{TOKEN} END {a}",
            f"{TOKEN} END {b}",
            f"{TOKEN} TYPE_BEGIN {a} 2",
            f"{TOKEN} TYPE_BEGIN {b} 1",
            f"{TOKEN} TYPE_CONST {b} Eq",
            f"{TOKEN} TYPE_CONST {a} Eq",
            f"{TOKEN} TYPE_CONST {a} Nat.zero",
            f"{TOKEN} TYPE_END {b}",
            f"{TOKEN} TYPE_END {a}",
            f"{TOKEN} VALUE_BEGIN {b} 0",
            f"{TOKEN} VALUE_END {b}",
            f"{TOKEN} VALUE_BEGIN {a} 1",
            f"{TOKEN} VALUE_CONST {a} Eq",
            f"{TOKEN} VALUE_END {a}",
        ]
        log = "\n".join("Inspect.lean:24:0: info: " + event for event in events)
        data = inspection.parse_classified_inspection(log, TOKEN, [a, b])
        self.assertEqual(data["constants"][a], ["Eq", "Nat.zero"])
        self.assertEqual(data["constants"][b], ["Eq"])
        self.assertEqual(data["value_constants"][a], ["Eq"])
        self.assertEqual(data["value_constants"][b], [])
        self.assertEqual(data["type_constants"][b], ["Eq"])
        edges = data["reference_edges"]
        self.assertIn({"declaration": a, "constant": "Eq", "origin": "type"}, edges)
        self.assertIn({"declaration": a, "constant": "Eq", "origin": "value"}, edges)
        self.assertNotIn({"declaration": b, "constant": "Eq", "origin": "value"}, edges)
        self.assertEqual(len(edges), 4)

    def test_classified_multi_declaration_protocol_fails_closed_on_partial_evidence(self):
        names = ["theorem_x", "theorem_y"]
        logs = []
        for name in names:
            logs.extend([
                f"{TOKEN} BEGIN {name} 1",
                f"{TOKEN} CONST {name} Eq",
                f"{TOKEN} END {name}",
                f"{TOKEN} TYPE_BEGIN {name} 1",
                f"{TOKEN} TYPE_CONST {name} Eq",
                f"{TOKEN} TYPE_END {name}",
                f"{TOKEN} VALUE_BEGIN {name} 0",
                f"{TOKEN} VALUE_END {name}",
            ])
        valid = "\n".join(logs)
        inspection.parse_classified_inspection(valid, TOKEN, names)
        for broken in (
            valid.replace(f"{TOKEN} VALUE_END theorem_y", ""),
            valid.replace(f"{TOKEN} TYPE_CONST theorem_y Eq", ""),
            valid.replace(f"{TOKEN} TYPE_BEGIN theorem_y 1",
                          f"{TOKEN} TYPE_BEGIN theorem_y 0"),
            valid.replace(f"{TOKEN} VALUE_BEGIN theorem_y 0",
                          f"{TOKEN} VALUE_BEGIN theorem_x 0"),
            valid + "\n" + f"{TOKEN} TYPE_END theorem_x",
            valid.replace(f"{TOKEN} CONST theorem_y Eq", ""),
        ):
            with self.subTest(last=broken[-100:]), self.assertRaises(ValueError):
                inspection.parse_classified_inspection(broken, TOKEN, names)

    def test_complete_output_is_sorted_and_bound_to_declaration(self):
        result = inspection.parse_inspection(transcript(), TOKEN, ["theorem_x"])
        self.assertEqual(result, {"theorem_x": ["Eq", "Nat.zero"]})

    def test_missing_end_duplicate_or_forged_names_are_rejected(self):
        valid = transcript()
        for bad in (
            valid.replace(TOKEN+" END theorem_x", ""),
            valid + "\n" + TOKEN + " CONST theorem_x Nat.one",
            valid.replace("BEGIN theorem_x 2", "BEGIN theorem_x 3"),
            valid.replace("CONST theorem_x Eq", "CONST foreign Eq"),
            valid.replace("CONST theorem_x Eq", "CONST theorem_x <script>"),
            valid.replace("CONST theorem_x Eq", "CONST theorem_x Nat.zero"),
        ):
            with self.subTest(bad=bad[:80]), self.assertRaises(ValueError):
                inspection.parse_inspection(bad, TOKEN, ["theorem_x"])

    def test_two_declarations_interleaved_and_reversed_are_complete(self):
        a, b = "theorem_x", "theorem_y"
        events = [
            f"{TOKEN} BEGIN {b} 1",
            f"{TOKEN} BEGIN {a} 2",
            f"{TOKEN} CONST {a} Nat.zero",
            f"{TOKEN} CONST {b} Eq",
            f"{TOKEN} CONST {a} Nat.succ",
            f"{TOKEN} END {b}",
            f"{TOKEN} END {a}",
        ]
        output = "\n".join("Inspect.lean:8:0: info: " + e for e in events)
        self.assertEqual(inspection.parse_inspection(output, TOKEN, [a, b]),
                         {a: ["Nat.succ", "Nat.zero"], b: ["Eq"]})

    def test_two_declarations_fail_closed_on_missing_or_extra_events(self):
        a, b = "theorem_x", "theorem_y"
        valid = "\n".join([
            f"{TOKEN} BEGIN {a} 1", f"{TOKEN} CONST {a} Eq",
            f"{TOKEN} END {a}", f"{TOKEN} BEGIN {b} 0",
            f"{TOKEN} END {b}",
        ])
        self.assertEqual(inspection.parse_inspection(valid, TOKEN, [a, b]),
                         {a: ["Eq"], b: []})
        broken = (
            valid.replace(f"{TOKEN} END {b}", ""),
            valid.replace(f"{TOKEN} BEGIN {b} 0", f"{TOKEN} BEGIN {b} 1"),
            valid + f"\n{TOKEN} END {a}",
            valid + f"\n{TOKEN} BEGIN foreign 0",
            valid.replace(f"{TOKEN} CONST {a} Eq", f"{TOKEN} CONST {b} Eq"),
        )
        for log in broken:
            with self.subTest(log=log[-75:]), self.assertRaises(ValueError):
                inspection.parse_inspection(log, TOKEN, [a, b])

    def test_rolling_log_saturation_rejects_apparently_complete_events(self):
        complete = transcript()
        capacity = inspection.MAX_OUTPUT_BYTES
        # A truncated subprocess log can end with a complete-looking protocol.
        # Equality with capture capacity must never count as verified output.
        saturated = ("X" * (capacity - len(complete.encode("utf-8")) - 1)
                     + "\n" + complete)
        self.assertEqual(len(saturated.encode("utf-8")), capacity)
        with self.assertRaisesRegex(ValueError, "saturated"):
            inspection.parse_inspection(saturated, TOKEN, ["theorem_x"])
        unsaturated = saturated[1:]
        self.assertEqual(inspection.parse_inspection(
            unsaturated, TOKEN, ["theorem_x"]), {"theorem_x": ["Eq", "Nat.zero"]})

    def test_count_bound_and_truncated_output_fail_closed(self):
        with self.assertRaises(ValueError):
            inspection.parse_inspection(f"{TOKEN} BEGIN theorem_x 999\n", TOKEN, ["theorem_x"])
        with self.assertRaises(ValueError):
            inspection.parse_inspection("x" * (inspection.MAX_OUTPUT_BYTES+1),
                                        TOKEN, ["theorem_x"])


class InspectionExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "application" / "lean"
        (self.root / "src").mkdir(parents=True)
        self.leanfile = self.root / "src" / "T.lean"
        self.leanfile.write_text(
            "import Mathlib\ntheorem theorem_x (p : Prop) : p → p := by exact id\n",
            encoding="utf-8")
        self.digest = hashlib.sha256(SOURCE.encode("utf-8")).hexdigest()
        entry = {"id":"mapping","source_module":"LST-01","source_label":"t:x",
                 "source_document_sha256":self.digest,"statement_status":"approved",
                 "lean_file":"src/T.lean","lean_theorem":"theorem_x"}
        (self.root / "manifest.json").write_text(
            json.dumps({"schema_version":1,"items":[entry]}),encoding="utf-8")
        self.con=sqlite3.connect(":memory:")
        self.addCleanup(self.con.close)
        self.con.row_factory=sqlite3.Row
        self.con.executescript("""
          CREATE TABLE documents(id TEXT, title TEXT, sha256 TEXT, content TEXT);
          CREATE TABLE entities(id TEXT, document_id TEXT, kind TEXT, title TEXT,
            start_line INTEGER, end_line INTEGER, start_offset INTEGER, end_offset INTEGER);
          CREATE TABLE labels(name TEXT, entity_id TEXT, offset INTEGER);
        """)
        self.con.execute("INSERT INTO documents VALUES(?,?,?,?)",
                         ("LST-01","Logic",self.digest,SOURCE))
        self.con.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
                         ("e1","LST-01","theorem","P",1,3,0,len(SOURCE) - 1))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)",("t:x","e1",LABEL_OFFSET))
        self.con.commit()
        self.ready={"ready":True,"lake_available":True,
                    "memory_limit_mb":None,"total_memory_limit_mb":None}
        self.original=self.leanfile.read_bytes()
        self.fingerprint={"source_document_sha256":self.digest,
                          "lean_sha256":hashlib.sha256(self.original).hexdigest(),
                          "toolchain_sha256":"c"*64}

    def execute(self, *args, result=(0,transcript(),False), fingerprint=None, ready=None, process=None, classified=False):
        with patch.dict(os.environ,{"MATLIB_LEAN_RUN":"1"}), \
             patch.object(inspection.lean,"availability",return_value=ready or self.ready), \
             patch.object(inspection.lean_results,"fingerprint",
                          side_effect=fingerprint or (lambda *unused:self.fingerprint)), \
             patch.object(inspection.secrets,"token_hex",return_value=TOKEN), \
             patch.object(inspection.lean_process,"execute_registered",
                          return_value=result, side_effect=process) as spawn:
            output=inspection.inspect(self.con,"mapping",lean_root=self.root,classified=classified)
        return output,spawn

    def test_success_requires_real_subprocess_interface_but_never_certificate(self):
        outcome,spawn=self.execute()
        self.assertEqual(outcome["inspection_status"],"complete")
        self.assertEqual(outcome["constants"],{"theorem_x":["Eq","Nat.zero"]})
        self.assertFalse(outcome["certificate"])
        command,root=spawn.call_args.args[:2]
        self.assertEqual(command[:3],["lake","env","lean"])
        self.assertEqual(root,self.root)
        # Temporary instrumented source is gone after the run.
        self.assertFalse(Path(command[3]).exists())
        self.assertEqual(self.leanfile.read_bytes(),self.original)
        self.assertNotIn("proof_status",outcome)

    def test_classified_inspection_preserves_total_and_never_certifies(self):
        response, spawned = self.execute(
            result=(0, classified_transcript(), False), classified=True)
        spawned.assert_called_once()
        self.assertEqual(response["inspection_status"], "complete")
        self.assertEqual(response["constants"], {"theorem_x": ["Eq", "Nat.zero"]})
        self.assertEqual(response["type_constants"], {"theorem_x": ["Eq"]})
        self.assertEqual(response["value_constants"], {"theorem_x": ["Nat.zero"]})
        self.assertEqual(len(response["reference_edges"]), 2)
        self.assertFalse(response["certificate"])
        self.assertNotIn("proof_status", response)

    def test_disabled_and_stale_sources_never_launch(self):
        with patch.dict(os.environ,{"MATLIB_LEAN_RUN":"0"}), \
             patch.object(inspection.lean_process,"execute_registered") as spawn:
            blocked=inspection.inspect(self.con,"mapping",lean_root=self.root)
        self.assertEqual(blocked["inspection_status"],"blocked")
        spawn.assert_not_called()
        changed=SOURCE+"% edit\n"
        self.con.execute("UPDATE documents SET content=?,sha256=?",
                         (changed,hashlib.sha256(changed.encode()).hexdigest()))
        self.con.commit()
        blocked,spawn=self.execute()
        self.assertEqual(blocked["inspection_status"],"blocked")
        spawn.assert_not_called()

    def test_failure_timeout_and_missing_output_are_not_evidence(self):
        for exitcode,output,timeout,status in (
            (1,"error",False,"failed"),
            (None,"",True,"timeout"),
            (0,f"{TOKEN} BEGIN theorem_x 2",False,"blocked")
        ):
            with self.subTest(status=status):
                response,_=self.execute(result=(exitcode,output,timeout))
                self.assertEqual(response["inspection_status"],status)
                self.assertFalse(response["certificate"])
                self.assertEqual(response["constants"],{})

    def test_full_diagnostic_tail_never_returns_complete(self):
        complete = transcript()
        limit = inspection.MAX_OUTPUT_BYTES
        saturated = ("Z" * (limit - len(complete.encode("utf-8")) - 1)
                     + "\n" + complete)
        response, spawn = self.execute(result=(0, saturated, False))
        spawn.assert_called_once()
        self.assertEqual(response["inspection_status"], "blocked")
        self.assertEqual(response["constants"], {})
        self.assertFalse(response["certificate"])

    def test_index_rebuild_during_lean_execution_blocks_stale_evidence(self):
        for mode in ("reindexed", "corrupted"):
            with self.subTest(mode=mode):
                def mutate_index(*args, **kwargs):
                    changed = SOURCE + "% reindexed\\n"
                    new_digest = hashlib.sha256(changed.encode("utf-8")).hexdigest()
                    self.con.execute(
                        "UPDATE documents SET content=?,sha256=? WHERE id=?",
                        (changed, new_digest if mode == "reindexed" else self.digest,
                         "LST-01"))
                    self.con.commit()
                    return 0, transcript(), False

                result, spawned = self.execute(process=mutate_index)
                spawned.assert_called_once()
                self.assertEqual(result["inspection_status"], "blocked")
                self.assertEqual(result["constants"], {})
                self.assertFalse(result["certificate"])
                self.con.execute("UPDATE documents SET content=?,sha256=? WHERE id=?",
                                 (SOURCE, self.digest, "LST-01"))
                self.con.commit()

    def test_manifest_binding_changed_before_lock_blocks_wrong_source(self):
        # The in-memory registry entry may be read before another process
        # rewrites the manifest. Do not use old source info with a new catalog.
        baseline = inspection.lean_catalog.list_formalizations(
            self.con, lean_root=self.root)["items"][0]
        for field, altered in (
            ("source_module", "LST-02"),
            ("source_label", "t:other"),
            ("lean_file", "src/Elsewhere.lean"),
            ("lean_theorems", ["other_declaration"]),
        ):
            with self.subTest(field=field):
                changed = {**baseline, field: altered}
                with patch.object(inspection.lean_catalog, "list_formalizations",
                                  return_value={"items": [changed]}):
                    result, spawned = self.execute()
                spawned.assert_not_called()
                self.assertEqual(result["inspection_status"], "blocked")
                self.assertEqual(result["constants"], {})
                self.assertFalse(result["certificate"])

    def test_label_binding_rebuilt_during_execution_never_returns_complete(self):
        # The document hash stays unchanged, but its label becomes unlinked
        # or is moved to a different theorem entity during the Lean process.
        self.con.execute(
            "INSERT INTO entities VALUES(?,?,?,?,?,?,?,?)",
            ("e2", "LST-01", "theorem", "P duplicate", 1, 3, 0, len(SOURCE) - 1))
        self.con.commit()
        for mode in ("unlinked", "moved"):
            with self.subTest(mode=mode):
                def mutate_labels(*args, **kwargs):
                    if mode == "unlinked":
                        self.con.execute("DELETE FROM labels WHERE name=?", ("t:x",))
                    else:
                        self.con.execute(
                            "UPDATE labels SET entity_id=? WHERE name=?", ("e2", "t:x"))
                    self.con.commit()
                    return 0, transcript(), False

                try:
                    response, spawned = self.execute(process=mutate_labels)
                    spawned.assert_called_once()
                    self.assertEqual(response["inspection_status"], "blocked")
                    self.assertEqual(response["constants"], {})
                    self.assertFalse(response["certificate"])
                finally:
                    self.con.execute("DELETE FROM labels WHERE name=?", ("t:x",))
                    self.con.execute(
                        "INSERT INTO labels VALUES(?,?,?)", ("t:x", "e1", LABEL_OFFSET))
                    self.con.commit()

    def test_indexed_entity_metadata_change_during_run_blocks_completion(self):
        # A reindex may retain the same document SHA and entity ID, changing
        # offsets or the mathematical-object type. All must invalidate output.
        mutations = (
            ("kind", "UPDATE entities SET kind='section' WHERE id='e1'"),
            ("title", "UPDATE entities SET title='Other theorem' WHERE id='e1'"),
            ("start_line", "UPDATE entities SET start_line=2 WHERE id='e1'"),
            ("end_line", "UPDATE entities SET end_line=2 WHERE id='e1'"),
            ("start_offset", "UPDATE entities SET start_offset=1 WHERE id='e1'"),
            ("end_offset", "UPDATE entities SET end_offset=3 WHERE id='e1'"),
            ("label_offset", f"UPDATE labels SET offset={LABEL_OFFSET + 1} WHERE name='t:x'"),
        )
        for field, sql in mutations:
            with self.subTest(field=field):
                def mutate(*args, **kwargs):
                    self.con.execute(sql)
                    self.con.commit()
                    return 0, transcript(), False
                try:
                    outcome, spawn = self.execute(process=mutate)
                    spawn.assert_called_once()
                    self.assertEqual(outcome["inspection_status"], "blocked")
                    self.assertEqual(outcome["constants"], {})
                    self.assertFalse(outcome["certificate"])
                finally:
                    self.con.execute(
                        "UPDATE entities SET kind='theorem', title='P', "
                        "start_line=1, end_line=3, start_offset=0, end_offset=? "
                        "WHERE id='e1'", (len(SOURCE) - 1,))
                    self.con.execute(
                        f"UPDATE labels SET offset={LABEL_OFFSET} WHERE name='t:x'")
                    self.con.commit()

    def test_duplicate_label_on_same_entity_rejected_before_compiler(self):
        # Catalog deliberately uses DISTINCT entity IDs, so two identical
        # label records need a separate fail-closed guard.
        self.con.execute("INSERT INTO labels VALUES(?,?,?)", ("t:x", "e1", LABEL_OFFSET + 3))
        self.con.commit()
        response, spawn = self.execute()
        spawn.assert_not_called()
        self.assertEqual(response["inspection_status"], "blocked")
        self.assertFalse(response["certificate"])

    def test_preexisting_corrupt_entity_bounds_and_label_positions_never_spawn(self):
        # These records are already malformed before the request; a before/after
        # comparison alone would accept the unchanged corruption.
        invalid = (
            ("wrong_label_offset", "UPDATE labels SET offset=0 WHERE name='t:x'"),
            ("label_instead_of_command", f"UPDATE labels SET offset={LABEL_OFFSET + 1} WHERE name='t:x'"),
            ("out_of_bounds_entity", "UPDATE entities SET end_offset=9999 WHERE id='e1'"),
            ("label_outside_entity", f"UPDATE entities SET end_offset={LABEL_OFFSET} WHERE id='e1'"),
            ("wrong_start_line", "UPDATE entities SET start_line=2, end_line=3 WHERE id='e1'"),
            ("wrong_end_line", "UPDATE entities SET start_line=1, end_line=2 WHERE id='e1'"),
            ("reversed_lines", "UPDATE entities SET start_line=5, end_line=2 WHERE id='e1'"),
            ("negative_start", "UPDATE entities SET start_offset=-1 WHERE id='e1'"),
        )
        for reason, sql in invalid:
            with self.subTest(reason=reason):
                self.con.execute(sql)
                self.con.commit()
                try:
                    result, spawned = self.execute()
                    spawned.assert_not_called()
                    self.assertEqual(result["inspection_status"], "blocked")
                    self.assertEqual(result["constants"], {})
                    self.assertFalse(result["certificate"])
                finally:
                    self.con.execute(
                        "UPDATE entities SET start_offset=0, end_offset=?, "
                        "start_line=1, end_line=3 WHERE id='e1'", (len(SOURCE) - 1,))
                    self.con.execute(
                        "UPDATE labels SET offset=? WHERE name='t:x'", (LABEL_OFFSET,))
                    self.con.commit()

    def test_dependency_change_after_process_refuses_stale_results(self):
        call=[0]
        def fingerprint(*args):
            call[0]+=1
            fresh=dict(self.fingerprint)
            if call[0]==2:
                fresh["lean_sha256"]="f"*64
            return fresh
        output,_=self.execute(fingerprint=fingerprint)
        self.assertEqual(output["inspection_status"],"blocked")

    def test_missing_toolchain_and_invalid_identifiers(self):
        with patch.dict(os.environ,{"MATLIB_LEAN_RUN":"1"}), \
             patch.object(inspection.lean,"availability",
                          return_value={**self.ready,"lake_available":False}):
            result=inspection.inspect(self.con,"mapping",lean_root=self.root)
        self.assertEqual(result["inspection_status"],"toolchain_unavailable")
        with self.assertRaises(HTTPException) as exc:
            inspection.inspect(self.con,"../../etc",lean_root=self.root)
        self.assertEqual(exc.exception.status_code,400)
        with self.assertRaises(HTTPException) as exc:
            inspection.inspect(self.con,"unknown",lean_root=self.root)
        self.assertEqual(exc.exception.status_code,404)


if __name__=="__main__":
    unittest.main()
