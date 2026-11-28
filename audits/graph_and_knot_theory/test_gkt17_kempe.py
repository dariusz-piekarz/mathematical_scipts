"""GKT-17-KEMPE-01: finite regression of five-colour extension.
Requires networkx. Run with Python; not a proof of the Jordan theorem.
"""
from itertools import product
import networkx as nx


def run():
    counts = [0, 0]
    planar = 0
    for g in nx.graph_atlas_g():
        ok, embedding = nx.check_planarity(g)
        if not ok:
            continue
        planar += 1
        for v in g:
            if g.degree(v) != 5:
                continue
            ns = list(embedding.neighbors_cw_order(v))
            h = g.copy()
            h.remove_node(v)
            rest = sorted(set(h) - set(ns))
            for colors in product(range(1, 6), repeat=len(rest)):
                c = dict(zip(ns, range(1, 6))) | dict(zip(rest, colors))
                if any(c[a] == c[b] for a, b in h.edges):
                    continue
                def component(i, j):
                    sub = h.subgraph([u for u in h if c[u] in (i, j)])
                    return nx.node_connected_component(sub, ns[i-1])
                k = component(1, 3)
                if ns[2] not in k:
                    i, j = 1, 3
                    counts[0] += 1
                else:
                    i, j = 2, 4
                    k = component(i, j)
                    assert ns[3] not in k
                    counts[1] += 1
                for u in k:
                    c[u] = i + j - c[u]
                assert all(c[a] != c[b] for a, b in h.edges)
                c[v] = i
                assert all(c[a] != c[b] for a, b in g.edges)
    assert all(counts), counts
    print(f'PASS planar={planar}, swap13={counts[0]}, swap24={counts[1]}')


if __name__ == '__main__':
    run()
