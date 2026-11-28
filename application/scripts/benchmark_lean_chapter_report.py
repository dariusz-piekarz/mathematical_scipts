"""Paired full chapter-report benchmark on a read-only indexed checkout.

Legacy mode removes only the catalogue module filter, restoring pre-L1.4.3
work. Both paths use the same real report, registry and provenance checks.
No Lean execution, history, fingerprint or certificate is produced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import statistics
import sys
import time
from unittest.mock import patch

APPLICATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION))

from backend import lean_catalog, lean_chapter_report
from backend import lean_formalization as lean, lean_source_provenance


def benchmark(db_path: Path, *, lean_root: Path = APPLICATION / "lean",
              samples: int = 6) -> dict:
    if type(samples) is not int or not 2 <= samples <= 20:
        raise ValueError("samples must be between 2 and 20")
    registry = lean._registry(lean_root)
    if not registry or len(registry) > lean_catalog.MAX_ENTRIES:
        raise ValueError("Expected nonempty bounded real registry")
    modules = sorted({item["source_module"] for item in registry})
    original = lean_catalog.list_formalizations

    def legacy(con, *, lean_root, module_id=None):
        return original(con, lean_root=lean_root)

    con = sqlite3.connect(db_path.resolve().as_uri() + "?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        indexed_chapters = con.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        results = []
        for module in modules:
            def run(mode):
                with patch.object(lean_catalog, "list_formalizations",
                                  legacy if mode == "legacy" else original):
                    started = time.perf_counter()
                    report = lean_chapter_report.chapter_report(
                        con, module, lean_root=lean_root)
                    return report, time.perf_counter() - started

            baseline, _ = run("legacy")  # warm both paths before timing
            warm, _ = run("scoped")
            if baseline != warm or baseline["certificate"] is not False:
                raise RuntimeError("Report equality/certificate check failed")
            if baseline["source_index_status"] != "ok" or not baseline["total"]:
                raise RuntimeError("Missing or corrupt real indexed module")
            seconds = {"legacy": [], "scoped": []}
            for n in range(samples):
                for mode in (("legacy", "scoped") if n % 2 == 0
                             else ("scoped", "legacy")):
                    report, elapsed = run(mode)
                    if report != baseline:
                        raise RuntimeError("Report changed during paired timing")
                    seconds[mode].append(elapsed)
            counts = {}
            # Instrument a separate untimed pair; wrappers call the real functions.
            for mode in ("legacy", "scoped"):
                with patch.object(lean_source_provenance, "owner_status",
                                  wraps=lean_source_provenance.owner_status) as owners, \
                     patch.object(lean, "_source_file_current",
                                  wraps=lean._source_file_current) as files:
                    report, _ = run(mode)
                if report != baseline:
                    raise RuntimeError("Instrumented report changed")
                counts[mode] = {
                    "owner_checks": owners.call_count,
                    "canonical_checks": files.call_count,
                    "other_module_owner_checks": sum(
                        call.args[1] != module for call in owners.call_args_list),
                    "other_module_canonical_checks": sum(
                        call.args[0]["source_module"] != module
                        for call in files.call_args_list),
                }
            if (counts["scoped"]["other_module_owner_checks"]
                    or counts["scoped"]["other_module_canonical_checks"]):
                raise RuntimeError("Scoped report checked unrelated modules")
            results.append({
                "module": module,
                "registered_entries": baseline["total"],
                "ready": baseline["ready"], "draft": baseline["draft"],
                "stale": baseline["stale"],
                "report_sha256": hashlib.sha256(json.dumps(
                    baseline, sort_keys=True, ensure_ascii=False,
                    separators=(",", ":")).encode("utf-8")).hexdigest(),
                "samples_seconds": seconds,
                "median_seconds": {k: statistics.median(v)
                                   for k, v in seconds.items()},
                "operation_counts": counts,
                "reports_equal": True,
            })
        return {
            "purpose": "paired_chapter_report_benchmark_not_formalization_result",
            "certificate": False, "samples_per_method": samples,
            "indexed_chapters": indexed_chapters,
            "registry_entries": len(registry), "registry_modules": len(modules),
            "method": "read-only same index and checkout; warmup then alternating "
                      "full report calls; separate untimed real operation counts",
            "scope": "host-specific warm timings; no Lean/Mathlib execution; "
                     "no synthetic registry scaling or semantic certificate",
            "results": results,
        }
    finally:
        con.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=APPLICATION / "data/biblioteka.db")
    parser.add_argument("--lean-root", type=Path, default=APPLICATION / "lean")
    parser.add_argument("--samples", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = benchmark(args.db, lean_root=args.lean_root, samples=args.samples)
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(encoded)
