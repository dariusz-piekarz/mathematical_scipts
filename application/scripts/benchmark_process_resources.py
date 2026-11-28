"""Isolated generation benchmark (POSIX): wall time, child CPU and peak RSS.

Diagnostic only: timeout terminates the child; no production resource limit is installed.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CHILD = r'''
import json, resource, sqlite3, sys, time
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from backend.generator import project_files, zip_project
path, n = Path(sys.argv[2]), int(sys.argv[3])
con = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
con.row_factory = sqlite3.Row
try:
    ids = [row[0] for row in con.execute('SELECT id FROM documents ORDER BY id LIMIT ?', (n,))]
    if len(ids) != n: raise ValueError('insufficient modules')
    start = time.perf_counter()
    files, manifest = project_files(con, ids, [], 'Process benchmark', closure_depth=0)
    archive = zip_project(files)
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(json.dumps({'generation_wall_s': round(time.perf_counter()-start, 5),
      'cpu_user_s': round(usage.ru_utime, 5), 'cpu_system_s': round(usage.ru_stime, 5),
      'maxrss_kib_linux': usage.ru_maxrss, 'zip_bytes': len(archive), 'files': len(files),
      'external_targets': len(manifest['external_targets'])}))
finally:
    con.close()
'''

def benchmark(db_path, sizes=(1, 5, 15), timeout=30):
    if sys.platform != 'linux':
        raise RuntimeError('RSS unit is Linux-specific; benchmark requires Linux')
    if not sizes or any(type(n) is not int or n < 1 or n > 75 for n in sizes):
        raise ValueError('sizes must be integers in [1,75]')
    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or not 1 <= timeout <= 300:
        raise ValueError('timeout must be in [1,300] seconds')
    results = []
    for n in sizes:
        start = time.perf_counter()
        try:
            p = subprocess.run([sys.executable, '-c', CHILD, str(ROOT), str(db_path), str(n)],
                               cwd=ROOT, capture_output=True, text=True, timeout=timeout, check=False)
            row = {'modules': n, 'elapsed_wall_s': round(time.perf_counter()-start, 5), 'exit_code': p.returncode}
            if p.returncode == 0:
                row.update(json.loads(p.stdout))
            else:
                row['error_tail'] = p.stderr[-1000:]
        except subprocess.TimeoutExpired:
            row = {'modules': n, 'elapsed_wall_s': round(time.perf_counter()-start, 5),
                   'status': 'timeout', 'timeout_s': timeout}
        results.append(row)
    return {'method': 'separate Python child per size; Linux resource.getrusage(RUSAGE_SELF); no HTTP',
            'rss_note': 'ru_maxrss in KiB on Linux; peak includes interpreter and imports',
            'timeout_s': timeout, 'results': results}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=Path, default=ROOT/'data'/'biblioteka.db')
    parser.add_argument('--sizes', nargs='+', type=int, default=[1,5,15])
    parser.add_argument('--timeout', type=float, default=30)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = benchmark(args.db, args.sizes, args.timeout)
    output = json.dumps(result, indent=2, ensure_ascii=False)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding='utf-8')
    print(output)