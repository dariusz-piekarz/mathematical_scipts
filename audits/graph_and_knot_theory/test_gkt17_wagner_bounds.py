"""GKT-17-WAGNER-01: finite minor and edge-bound regression.
Requires NetworkX. Checks atlas graphs up to six vertices; not a proof.
"""
from functools import lru_cache
from itertools import combinations
import networkx as nx


def key(g):
    g = nx.convert_node_labels_to_integers(g, ordering='sorted')
    return len(g), tuple(sorted(tuple(sorted(e)) for e in g.edges))


def minor_checker(target):
    @lru_cache(None)
    def has(n, edges):
        if n < len(target) or len(edges) < target.number_of_edges():
            return False
        g = nx.Graph()
        g.add_nodes_from(range(n))
        g.add_edges_from(edges)
        if n == len(target):
            return nx.algorithms.isomorphism.GraphMatcher(g, target).subgraph_is_monomorphic()
        return (any(has(*key(g.subgraph(set(g) - {v}))) for v in g)
                or any(has(*key(nx.contracted_nodes(g, u, v, self_loops=False)))
                       for u, v in g.edges))
    return lambda g: has(*key(g))


def run():
    k4 = minor_checker(nx.complete_graph(4))
    k23 = minor_checker(nx.complete_bipartite_graph(2, 3))
    k5 = minor_checker(nx.complete_graph(5))
    k33 = minor_checker(nx.complete_bipartite_graph(3, 3))
    total = planar = outer = bound = bipartite = outer_bound = equality = 0
    for g in nx.graph_atlas_g():
        n, m = len(g), g.number_of_edges()
        if n > 6:
            continue
        total += 1
        p = nx.check_planarity(g)[0]
        assert p == (not k5(g) and not k33(g)), g.edges
        planar += p
        cone = g.copy()
        cone.add_node(n)
        cone.add_edges_from((n, v) for v in g)
        o = nx.check_planarity(cone)[0]
        assert o == (not k4(g) and not k23(g)), g.edges
        outer += o
        if p and n >= 3:
            assert m <= 3*n - 6
            bound += 1
            if nx.is_bipartite(g):
                assert m <= 2*n - 4
                bipartite += 1
        if o and n >= 2:
            assert m <= 2*n - 3
            outer_bound += 1
            if n >= 3 and m == 2*n - 3:
                assert nx.is_biconnected(g)
                equality += 1
        if p and n:
            assert min(dict(g.degree()).values()) <= 5
        if o and n:
            assert min(dict(g.degree()).values()) <= 2
    print(f'PASS atlas={total}, planar={planar}, outer={outer}, planar_bound={bound}, bipartite_bound={bipartite}, outer_bound={outer_bound}, equality={equality}')


if __name__ == '__main__':
    run()
