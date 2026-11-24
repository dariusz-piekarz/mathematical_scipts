"""GKT-17-FACE-01: finite facial-walk and gluing regression.
Requires NetworkX. Tests combinatorial instances, not topological proofs.
"""
from itertools import combinations
import networkx as nx


def run():
    graphs = faces = darts = 0
    for g in nx.graph_atlas_g():
        if len(g) < 3 or not nx.is_biconnected(g):
            continue
        ok, emb = nx.check_planarity(g)
        if not ok:
            continue
        graphs += 1
        seen = set()
        count = 0
        for u, v in emb.edges():
            if (u, v) in seen:
                continue
            walk = emb.traverse_face(u, v, seen)
            assert len(walk) >= 3 and len(set(walk)) == len(walk)
            count += 1
        assert len(seen) == 2 * g.number_of_edges()
        assert len(g) - g.number_of_edges() + count == 2
        faces += count
        darts += len(seen)
    small = [g for g in nx.graph_atlas_g() if 1 <= len(g) <= 4]
    vertex = edge = 0
    for g in small:
        for h in small:
            for a in g:
                for b in h:
                    j = nx.compose(nx.relabel_nodes(g, lambda u: 0 if u == a else (1, u)),
                                   nx.relabel_nodes(h, lambda u: 0 if u == b else (2, u)))
                    assert nx.check_planarity(j)[0]
                    vertex += 1
            for a, b in combinations(g, 2):
                for c, d in combinations(h, 2):
                    j = nx.compose(nx.relabel_nodes(g, lambda u: 0 if u == a else 1 if u == b else (1, u)),
                                   nx.relabel_nodes(h, lambda u: 0 if u == c else 1 if u == d else (2, u)))
                    j.add_edge(0, 1)
                    assert nx.check_planarity(j)[0]
                    j.remove_edge(0, 1)
                    assert nx.check_planarity(j)[0]
                    edge += 1
    print(f'PASS biconnected={graphs}, faces={faces}, darts={darts}, vertex_glues={vertex}, edge_glues={edge}')


if __name__ == '__main__':
    run()
