"""GKT-17-SEP-01: finite regression of separator and descent lemmas.
Run with Python and NetworkX; not a formal proof.
"""
from itertools import combinations
import networkx as nx


def run():
    graphs = cuts = incidences = descents = outside = 0
    for g in nx.graph_atlas_g():
        if len(g) < 5 or nx.node_connectivity(g) < 3:
            continue
        graphs += 1
        separators = {}
        for s in combinations(g, 3):
            parts = list(nx.connected_components(g.subgraph(set(g)-set(s))))
            if len(parts) < 2:
                continue
            separators[frozenset(s)] = parts
            cuts += 1
            for u in s:
                for c in parts:
                    assert set(g[u]) & c, (g.edges, s, u, c)
                    incidences += 1
        for s, parts in separators.items():
            for x, y in combinations(s, 2):
                if not g.has_edge(x, y):
                    continue
                z, = s - {x, y}
                for c in parts:
                    for w in set(g[z]) & c:
                        for t in set(g) - {z, w}:
                            q = frozenset({z, w, t})
                            if q not in separators:
                                continue
                            candidates = [d for d in separators[q] if not d & {x, y}]
                            assert candidates, (g.edges, s, q)
                            for d in candidates:
                                assert set(g[w]) & d
                                assert d < c, (g.edges, s, q, c, d)
                                assert t in c | {x, y}, (g.edges, s, q, c, d)
                                outside += t in {x, y}
                                descents += 1
    assert cuts and descents and outside
    print(f'PASS graphs={graphs}, separators={cuts}, incidences={incidences}, descents={descents}, t_xy={outside}')


if __name__ == '__main__':
    run()
