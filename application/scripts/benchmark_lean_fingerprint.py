"""Read-only, real-environment timings of the three Lean provenance checkpoints.

The tool does not run Lean, update history, validate mathematical equivalence,
or represent a proof certificate. Run only from a trusted checkout.
Example: python scripts/benchmark_lean_fingerprint.py --samples 3
"""
from __future__ import annotations

import argparse
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys
import time
from unittest.mock import patch

APPLICATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APPLICATION))
from backend import lean_results


def _registered_inputs(lean_root: Path) -> tuple[Path, str]:
    manifest = json.loads((lean_root / "manifest.json").read_text(encoding="utf-8"))
    items = manifest.get("items") if isinstance(manifest, dict) else None
    if not isinstance(items, list) or not items or not isinstance(items[0], dict):
        raise ValueError("No registered Lean source to benchmark")
    entry = items[0]
    rel, sha = entry.get("lean_file"), entry.get("source_document_sha256")
    if (not isinstance(rel, str) or not rel.startswith("src/")
            or "\\" in rel or ".." in Path(rel).parts
            or not rel.endswith(".lean")
            or not isinstance(sha, str) or not lean_results.HEX_DIGEST.fullmatch(sha)):
        raise ValueError("Malformed registered Lean benchmark source")
    src = (lean_root / "src").resolve()
    file = (lean_root / rel).resolve()
    if not file.is_relative_to(src) or not file.is_file():
        raise ValueError("Registered Lean source is missing or outside src")
    return file, sha



# Instrument the original digest calls rather than independently measuring
# them: an independent second pass would not explain the full fingerprint time.
# Keep instrumentation only in this diagnostic process. Production code is
# not patched and every original SHA256 calculation still runs in full.
COMPONENTS = (
    ("local_sources", lean_results, "_project_sources_sha256"),
    ("external_packages", lean_results.lean_environment, "external_packages_sha256"),
    ("olean_artifacts", lean_results.lean_environment, "compiled_artifacts_sha256"),
    ("tool_executables", lean_results.lean_environment, "executable_toolchain_sha256"),
)



# These probes wrap the *real* calls used by compiled_artifacts_sha256.
# No second walk, synthetic hash, skipped file or persistent cache is introduced.
# Instrumentation is process-local, single-threaded and MUST NOT be used in the
# server/runner; unittest.mock.patch is restored even when a digest raises.
OLEAN_TIME_BUCKETS = (
    "directory_scan", "metadata", "file_open", "content_read",
    "hashing_sorting_and_other",
)
OLEAN_IO_COUNTERS = (
    "directories_visited", "walk_files_seen", "olean_name_candidates",
    "non_olean_names_skipped", "stat_calls", "lstat_calls", "fstat_calls",
    "olean_files_opened", "content_read_calls", "content_bytes_read",
)


class _ObservedOleanStream:
    def __init__(self, stream, timings: dict[str, float],
                 counters: dict[str, int]):
        self.stream = stream
        self.timings = timings
        self.counters = counters

    def __enter__(self):
        self.stream.__enter__()
        return self

    def __exit__(self, exc_type, exc, tb):
        return self.stream.__exit__(exc_type, exc, tb)

    def read(self, *args, **kwargs):
        started = time.perf_counter()
        try:
            data = self.stream.read(*args, **kwargs)
        finally:
            self.timings["content_read"] += time.perf_counter() - started
        self.counters["content_read_calls"] += 1
        self.counters["content_bytes_read"] += len(data)
        return data

    def fileno(self):
        return self.stream.fileno()

    def __getattr__(self, name):
        return getattr(self.stream, name)


def _profile_olean_substeps(original, *args, **kwargs) -> tuple[str, dict]:
    """Observe the original Lake .olean digest, including its original limits.

    directory_scan is time spent advancing os.walk; metadata covers Path
    stat/lstat and os.fstat; file_open covers opening .olean file handles;
    content_read covers read() calls, not hashlib.update. The residual also
    contains sorting, SHA256 updates, Python loops and probe overhead. Timings
    are diagnostic approximations, not independent security attestations.
    """
    timings = {label: 0.0 for label in OLEAN_TIME_BUCKETS}
    counters = {label: 0 for label in OLEAN_IO_COUNTERS}
    raw_walk = os.walk
    raw_fstat = os.fstat
    raw_stat, raw_lstat, raw_open = Path.stat, Path.lstat, Path.open
    metadata_depth = 0

    def timed_metadata(original, counter_key, *call_args, **call_kwargs):
        # In CPython 3.13 Path.lstat delegates to Path.stat. Count both API
        # calls, but charge wall-clock time only to the outermost operation.
        nonlocal metadata_depth
        started = time.perf_counter()
        metadata_depth += 1
        try:
            return original(*call_args, **call_kwargs)
        finally:
            elapsed = time.perf_counter() - started
            metadata_depth -= 1
            if metadata_depth == 0:
                timings["metadata"] += elapsed
            counters[counter_key] += 1

    def observed_walk(*walk_args, **walk_kwargs):
        source = raw_walk(*walk_args, **walk_kwargs)

        def advance():
            while True:
                started = time.perf_counter()
                try:
                    item = next(source)
                except StopIteration:
                    timings["directory_scan"] += time.perf_counter() - started
                    return
                except BaseException:
                    timings["directory_scan"] += time.perf_counter() - started
                    raise
                timings["directory_scan"] += time.perf_counter() - started
                counters["directories_visited"] += 1
                # Derive name counts from this original os.walk result only.
                # The exact name '.olean' has no Path suffix.
                names = item[2]
                candidates = sum(name.endswith(".olean") and name != ".olean"
                                 for name in names)
                counters["walk_files_seen"] += len(names)
                counters["olean_name_candidates"] += candidates
                counters["non_olean_names_skipped"] += len(names) - candidates
                yield item

        return advance()

    def observed_stat(path, *stat_args, **stat_kwargs):
        return timed_metadata(raw_stat, "stat_calls", path, *stat_args, **stat_kwargs)

    def observed_lstat(path, *stat_args, **stat_kwargs):
        return timed_metadata(raw_lstat, "lstat_calls", path, *stat_args, **stat_kwargs)

    def observed_fstat(*stat_args, **stat_kwargs):
        return timed_metadata(raw_fstat, "fstat_calls", *stat_args, **stat_kwargs)

    def observed_open(path, *open_args, **open_kwargs):
        mode = open_args[0] if open_args else open_kwargs.get("mode", "r")
        if path.suffix != ".olean" or mode != "rb":
            return raw_open(path, *open_args, **open_kwargs)
        started = time.perf_counter()
        try:
            stream = raw_open(path, *open_args, **open_kwargs)
        finally:
            timings["file_open"] += time.perf_counter() - started
        counters["olean_files_opened"] += 1
        return _ObservedOleanStream(stream, timings, counters)

    with ExitStack() as stack:
        stack.enter_context(patch.object(os, "walk", observed_walk))
        stack.enter_context(patch.object(os, "fstat", observed_fstat))
        stack.enter_context(patch.object(Path, "stat", observed_stat))
        stack.enter_context(patch.object(Path, "lstat", observed_lstat))
        stack.enter_context(patch.object(Path, "open", observed_open))
        started = time.perf_counter()
        result = original(*args, **kwargs)
        elapsed = time.perf_counter() - started
    timings["hashing_sorting_and_other"] = max(
        0.0, elapsed - sum(timings[name] for name in OLEAN_TIME_BUCKETS[:-1]))
    return result, {"total_seconds": elapsed, "seconds": timings, "counts": counters}


def _profile_once(document_sha: str, file: Path, lean_root: Path,
                  binding_sha: str) -> tuple[dict[str, str], float, dict[str, float], dict]:
    parts: dict[str, float] = {}
    olean_breakdown: dict = {}
    with ExitStack() as stack:
        for label, module, attribute in COMPONENTS:
            original = getattr(module, attribute)

            def measure(*args, _original=original, _label=label, **kwargs):
                t0 = time.perf_counter()
                try:
                    if _label == "olean_artifacts":
                        value, details = _profile_olean_substeps(_original, *args, **kwargs)
                        olean_breakdown.update(details)
                        return value
                    return _original(*args, **kwargs)
                finally:
                    parts[_label] = time.perf_counter() - t0

            stack.enter_context(patch.object(module, attribute, measure))
        started = time.perf_counter()
        fingerprint = lean_results.fingerprint(
            document_sha, file, lean_root, binding_sha)
        elapsed = time.perf_counter() - started
    if set(parts) != {name for name, _, _ in COMPONENTS} or not olean_breakdown:
        raise RuntimeError("Incomplete fingerprint timing instrumentation")
    return fingerprint, elapsed, parts, olean_breakdown


def benchmark(lean_root: Path, *, samples: int = 3) -> dict:
    """Measure actual fingerprint calls; refuse dependency changes mid-benchmark."""
    if type(samples) is not int or not 1 <= samples <= 6:
        raise ValueError("samples must be an integer between 1 and 6")
    file, document_sha = _registered_inputs(lean_root)
    # Benchmark only: never save or expose this artificial binding as evidence.
    dummy_binding = hashlib.sha256(b"benchmark-only-not-an-indexed-source").hexdigest()
    durations: list[float] = []
    measurements = {name: [] for name, _, _ in COMPONENTS}
    unclassified: list[float] = []
    olean_timings = {name: [] for name in OLEAN_TIME_BUCKETS}
    olean_counts: list[dict[str, int]] = []
    olean_totals: list[float] = []
    first: dict[str, str] | None = None
    for _ in range(samples):
        measured, elapsed, parts, olean = _profile_once(
            document_sha, file, lean_root, dummy_binding)
        if first is not None and measured != first:
            raise RuntimeError("Dependencies changed during the fingerprint benchmark")
        first = measured
        durations.append(elapsed)
        olean_totals.append(olean["total_seconds"])
        olean_counts.append(olean["counts"])
        for name in OLEAN_TIME_BUCKETS:
            olean_timings[name].append(olean["seconds"][name])
        for name, value in parts.items():
            measurements[name].append(value)
        # Includes selected .lean bytes, Lake/manifest metadata, and Python
        # bookkeeping. It is not an independent hash of any dependency.
        unclassified.append(max(0.0, elapsed - sum(parts.values())))
    return {
        "purpose": "timing_only_not_a_formalization_result",
        "certificate": False,
        "real_fingerprint_calls": samples,
        "samples_seconds": [round(v, 6) for v in durations],
        "median_seconds": round(statistics.median(durations), 6),
        "total_seconds": round(sum(durations), 6),
        "max_seconds": round(max(durations), 6),
        "component_samples_seconds": {
            name: [round(v, 6) for v in values]
            for name, values in measurements.items()
        },
        "component_median_seconds": {
            name: round(statistics.median(values), 6)
            for name, values in measurements.items()
        },
        "other_work_samples_seconds": [round(v, 6) for v in unclassified],
        "olean_breakdown_samples_seconds": {
            name: [round(v, 6) for v in values]
            for name, values in olean_timings.items()
        },
        "olean_breakdown_median_seconds": {
            name: round(statistics.median(values), 6)
            for name, values in olean_timings.items()
        },
        "olean_subprofile_total_seconds": [round(v, 6) for v in olean_totals],
        "olean_io_samples": olean_counts,
        "olean_method": (
            "single original digest pass: os.walk advancement, Path.stat/lstat "
            "and os.fstat, .olean open/read; filename counters reuse os.walk " 
            "results to count paths avoided; remainder includes SHA256, sorting, "
            "Python and probe overhead; no content or metadata checks bypassed"
        ),
        "method": "perf_counter around original digest calls inside full fingerprint; no caching",
        "stability": "all fingerprint dictionaries identical during benchmark",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean-root", type=Path, default=APPLICATION / "lean")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = benchmark(args.lean_root, samples=args.samples)
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
