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


def transcript(*, token=TOKEN, name="theorem_x", constants=("Nat.zero", "Eq")):
    lines = [f"{token} BEGIN {name} {len(constants)}"]
    lines.extend(f"{token} CONST {name} {dep}" for dep in constants)
    lines.append(f"{token} END {name}")
    return "Inspect.lean:45:0: info: " + ("\nInspect.lean:45:0: info: ".join(lines))


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
            valid + f"\\n{TOKEN} END {a}",
            valid + f"\\n{TOKEN} BEGIN foreign 0",
            valid.replace(f"{TOKEN} CONST {a} Eq", f"{TOKEN} CONST {b} Eq"),
        )
        for log in broken:
            with self.subTest(log=log[-75:]), self.assertRaises(ValueError):
                inspection.parse_inspection(log, TOKEN, [a, b])

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
                         ("e1","LST-01","theorem","P",1,3,0,len(SOURCE)))
        self.con.execute("INSERT INTO labels VALUES(?,?,?)",("t:x","e1",8))
        self.con.commit()
        self.ready={"ready":True,"lake_available":True,
                    "memory_limit_mb":None,"total_memory_limit_mb":None}
        self.original=self.leanfile.read_bytes()
        self.fingerprint={"source_document_sha256":self.digest,
                          "lean_sha256":hashlib.sha256(self.original).hexdigest(),
                          "toolchain_sha256":"c"*64}

    def execute(self, *args, result=(0,transcript(),False), fingerprint=None, ready=None):
        with patch.dict(os.environ,{"MATLIB_LEAN_RUN":"1"}), \
             patch.object(inspection.lean,"availability",return_value=ready or self.ready), \
             patch.object(inspection.lean_results,"fingerprint",
                          side_effect=fingerprint or (lambda *unused:self.fingerprint)), \
             patch.object(inspection.secrets,"token_hex",return_value=TOKEN), \
             patch.object(inspection.lean_process,"execute_registered",
                          return_value=result) as spawn:
            output=inspection.inspect(self.con,"mapping",lean_root=self.root)
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
