"""Repeatable local benchmark; read-only against the indexed library.

Run from project root: python scripts/benchmark_generation.py --output data/benchmark_v16.json
The numbers describe this machine only, not an enforced server budget.
"""
import argparse
import json
import sqlite3
import statistics
import sys
import time
import tracemalloc
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.generator import project_files, zip_project


def benchmark(db_path: Path, sizes=(1, 5, 15, 30), repetitions=3, measure_memory=True):
    if repetitions < 1 or any(n < 1 or n > 75 for n in sizes):
        raise ValueError('Invalid benchmark parameters')
    con = sqlite3.connect(f'file:{db_path}?mode=ro', uri=True)
    con.row_factory = sqlite3.Row
    try:
        ids = [r[0] for r in con.execute('SELECT id FROM documents ORDER BY id')]
        results = []
        for n in sizes:
            if n > len(ids):
                raise ValueError('Not enough modules in database')
            measurements = []
            for _ in range(repetitions):
                if measure_memory:
                    tracemalloc.start()
                start = time.perf_counter()
                files, manifest = project_files(con, ids[:n], [], 'Benchmark', closure_depth=0)
                generated = time.perf_counter()
                archive = zip_project(files)
                finished = time.perf_counter()
                if measure_memory:
                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                else:
                    peak = None
                measurements.append({'generate_s': round(generated-start, 4),
                                     'zip_s': round(finished-generated, 4),
                                     'total_s': round(finished-start, 4),
                                     'tracemalloc_peak_bytes': peak,
                                     'zip_bytes': len(archive),
                                     'files': len(files),
                                     'external_targets': len(manifest['external_targets'])})
            results.append({'modules': n, 'runs': measurements,
                            'median_total_s': statistics.median(x['total_s'] for x in measurements),
                            'max_peak_bytes': max(x['tracemalloc_peak_bytes'] for x in measurements) if measure_memory else None})
        return {'repetitions': repetitions, 'module_selection': 'first N module IDs ordered lexicographically',
                'closure_depth': 0, 'method': 'perf_counter' + (' + tracemalloc' if measure_memory else '') + '; in-process, no HTTP',
                'memory_tracing': measure_memory,
                'results': results}
    finally:
        con.close()


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--db', type=Path, default=ROOT/'data'/'biblioteka.db')
    p.add_argument('--output', type=Path)
    p.add_argument('--repetitions', type=int, default=3)
    p.add_argument('--sizes', type=int, nargs='+', default=[1, 5, 15, 30])
    p.add_argument('--no-memory-tracing', action='store_true')
    a = p.parse_args()
    result = benchmark(a.db, sizes=a.sizes, repetitions=a.repetitions, measure_memory=not a.no_memory_tracing)
    encoded = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(encoded, encoding='utf-8')
    print(encoded)