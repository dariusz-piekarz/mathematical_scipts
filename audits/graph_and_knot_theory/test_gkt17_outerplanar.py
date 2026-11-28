"""GKT-17-OUTER-01: finite regression for outerplanar polygon graphs.

Run: python audits/graph_and_knot_theory/test_gkt17_outerplanar.py
Source: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex
Checks only combinatorial instances; not a proof or PDF check.
"""
from itertools import combinations

def run():
    count = ears = steps = 0
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        cross = [(i, j) for i, (a, b) in enumerate(edges)
                 for j, (c, d) in enumerate(edges)
                 if a < c < b < d]
        def components(es, removed=None):
            unseen = set(range(n)) - {removed}
            k = 0
            while unseen:
                k += 1
                todo = [unseen.pop()]
                while todo:
                    u = todo.pop()
                    for a, b in es:
                        v = b if a == u else a if b == u else None
                        if v in unseen:
                            unseen.remove(v)
                            todo.append(v)
            return k
        for mask in range(1 << len(edges)):
            if any(mask >> i & 1 and mask >> j & 1 for i,j in cross):
                continue
            es = [e for i,e in enumerate(edges) if mask >> i & 1]
            count += 1
            deg = [sum(v in e for e in es) for v in range(n)]
            assert len(es) <= 2*n-3 and min(deg) <= 2, (n, es)
            if len(es) == 2*n-3:
                assert deg.count(2) >= 2, (n, es)
                ears += 1
            if components(es) == 1:
                cs = [components(es, v) for v in range(n)]
                # A missing polygon side can be added without crossings.
                # If it joins two components after deletion, potential drops.
                for a,b in [(i,i+1) for i in range(n-1)]+[(0,n-1)]:
                    if (a,b) in es:
                        continue
                    new = [components(es+[(a,b)],v) for v in range(n)]
                    assert all(x <= y for x,y in zip(new,cs))
                    if new != cs:
                        assert sum(new) < sum(cs)
                        steps += 1
    print(f"PASS graphs={count}, triangulations={ears}, potential_drops={steps}")

if __name__ == "__main__":
    run()
