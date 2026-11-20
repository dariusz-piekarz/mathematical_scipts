"""In-process ASGI concurrency diagnostic; not a network or production load test."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import statistics
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient
from backend.api import app


def benchmark(levels=(1, 2, 4), requests_per_level=4, modules=('ALG-09',)):
    if not levels or any(not isinstance(n, int) or isinstance(n, bool) or n < 1 or n > 16 for n in levels):
        raise ValueError('Concurrency levels must be integers between 1 and 16')
    if not isinstance(requests_per_level, int) or not 1 <= requests_per_level <= 64:
        raise ValueError('Invalid request count')
    if not modules or len(modules) > 75:
        raise ValueError('Invalid module selection')
    rows = []
    with TestClient(app) as client:
        def request(_):
            start = time.perf_counter()
            response = client.post('/api/generate', json={'modules':list(modules), 'closure_depth':0})
            elapsed = time.perf_counter()-start
            return {'status':response.status_code,'seconds':round(elapsed,5), 'bytes':len(response.content)}
        for level in levels:
            started = time.perf_counter()
            with ThreadPoolExecutor(max_workers=level) as pool:
                results = list(pool.map(request, range(requests_per_level)))
            wall = time.perf_counter()-started
            rows.append({'concurrency':level,'requests':results,'wall_seconds':round(wall,5),
                         'median_latency_seconds':round(statistics.median(r['seconds'] for r in results),5),
                         'successes':sum(r['status']==200 for r in results)})
    return {'method':'in-process FastAPI TestClient; concurrent threads; no network, no process memory measurement',
            'modules':list(modules),'requests_per_level':requests_per_level,'results':rows}


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--levels',type=int,nargs='+',default=[1,2,4])
    p.add_argument('--requests',type=int,default=4)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    result=benchmark(a.levels,a.requests)
    encoded=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(encoded,encoding='utf-8')
    print(encoded)