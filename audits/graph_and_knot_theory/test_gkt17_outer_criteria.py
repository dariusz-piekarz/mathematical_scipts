"""GKT-17-OUTER-02: independent finite outerplanarity checks.
Run: python audits/graph_and_knot_theory/test_gkt17_outer_criteria.py
Requires networkx. Atlas graphs up to six vertices; not a proof.
"""
from functools import lru_cache
from itertools import combinations, permutations
import networkx as nx


def circular(g):
    if len(g) <= 2:
        return True
    vertices = list(g)
    for tail in permutations(vertices[1:]):
        pos = {v: i for i, v in enumerate((vertices[0],) + tail)}
        es = [tuple(sorted((pos[a], pos[b]))) for a, b in g.edges]
        if not any(a < c < b < d or c < a < d < b
                   for (a, b), (c, d) in combinations(es, 2)):
            return True
    return False


def signature(g):
    ix = {v: i for i, v in enumerate(sorted(g))}
    return len(g), tuple(sorted(tuple(sorted((ix[a], ix[b]))) for a, b in g.edges))


@lru_cache(None)
def forbidden(n, es):
    g = nx.Graph()
    g.add_nodes_from(range(n))
    g.add_edges_from(es)
    if any(all(g.has_edge(a, b) for a, b in combinations(s, 2))
           for s in combinations(g, 4)):
        return True
    if any(len(set(g[a]) & set(g[b])) >= 3 for a, b in combinations(g, 2)):
        return True
    if n <= 4:
        return False
    for a, b in g.edges:
        h = nx.contracted_nodes(g, a, b, self_loops=False)
        if forbidden(*signature(h)):
            return True
    return False


def run():
    total = outer = connected = equality = maximal_checks = 0
    for g in nx.graph_atlas_g():
        n = len(g)
        if n > 6:
            continue
        total += 1
        cone = g.copy()
        cone.add_node(n)
        cone.add_edges_from((n, v) for v in g)
        planar_cone = nx.check_planarity(cone)[0]
        circular_test = circular(g)
        minor_test = not forbidden(*signature(g))
        assert planar_cone == circular_test == minor_test, signature(g)
        if not circular_test:
            continue
        outer += 1
        h = g.copy()
        order = []
        while h:
            v = min(h, key=lambda u: h.degree(u))
            assert h.degree(v) <= 2
            order.append(v)
            h.remove_node(v)
        colors = {}
        for v in reversed(order):
            colors[v] = next(c for c in range(3) if c not in {colors[u] for u in g[v] if u in colors})
        assert all(colors[a] != colors[b] for a, b in g.edges)
        if n >= 3 and nx.is_connected(g):
            connected += 1
            m = g.number_of_edges()
            assert m <= 2*n-3
            maximal = True
            for a, b in nx.non_edges(g):
                extended = g.copy()
                extended.add_edge(a, b)
                maximal_checks += 1
                if circular(extended):
                    maximal = False
            assert maximal == (m == 2*n-3), signature(g)
            if maximal:
                equality += 1
                assert nx.is_biconnected(g)
                assert sum(1 for u in g if g.degree(u) == 2) >= 2
    assert equality and total > outer
    print(f'PASS graphs={total}, outer={outer}, connected_n_ge_3={connected}, equality={equality}, extra_edge_checks={maximal_checks}')


if __name__ == '__main__':
    run()
