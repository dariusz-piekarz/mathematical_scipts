"""GKT-17-KUR-01: finite regressions for the cyclic obstruction and contraction lemmas.
Run: python audits/graph_and_knot_theory/test_gkt17_kuratowski.py
Requires networkx for the graph-atlas part; no claim of formal proof.
"""
from itertools import combinations, product
import networkx as nx


def cyclic_checks():
    total = insert = common = alternating = 0
    for n in range(3, 9):
        for flags in product(range(4), repeat=n):
            x = {i for i, f in enumerate(flags) if f & 1}
            y = {i for i, f in enumerate(flags) if f & 2}
            if min(len(x), len(y)) < 2:
                continue
            total += 1
            xs = sorted(x)
            arcs = []
            for a, b in zip(xs, xs[1:] + xs[:1]):
                arcs.append({(a + j) % n for j in range((b-a) % n + 1)})
            if any(y <= arc for arc in arcs):
                insert += 1
                continue
            if len(x & y) >= 3:
                common += 1
                continue
            alternating += 1
            assert any((a in y and b in x and c in y and d in x) or
                       (a in x and b in y and c in x and d in y)
                       for a, b, c, d in combinations(range(n), 4)), (n, x, y)
    print(f'PASS cyclic={total}, insertion={insert}, common={common}, alternating={alternating}')


def contraction_checks():
    graphs = edges = good = bad = 0
    for g in nx.graph_atlas_g():
        if len(g) < 5 or nx.node_connectivity(g) < 3:
            continue
        graphs += 1
        found = False
        for u, v in g.edges:
            edges += 1
            h = nx.contracted_nodes(g, u, v, self_loops=False)
            contractible = nx.node_connectivity(h) >= 3
            separating = any(nx.number_connected_components(g.subgraph(set(g) - {u, v, w})) > 1
                             for w in set(g) - {u, v})
            assert contractible == (not separating), (g.edges, u, v)
            found |= contractible
            good += contractible
            bad += not contractible
        assert found, g.edges
    print(f'PASS three_connected={graphs}, edges={edges}, contractible={good}, noncontractible={bad}')


if __name__ == '__main__':
    cyclic_checks()
    contraction_checks()
