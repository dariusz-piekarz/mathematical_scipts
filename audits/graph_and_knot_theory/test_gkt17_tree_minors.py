"""GKT-17-TREE-01: finite tests of labelled trees and minor models.
Run with Python and NetworkX. Not a formal proof.
"""
from itertools import combinations, product
import networkx as nx


def tree_checks():
    total = stars = splits = 0
    for n in range(1, 9):
        trees = [nx.empty_graph(1)] if n == 1 else nx.nonisomorphic_trees(n)
        for t in trees:
            paths = dict(nx.all_pairs_shortest_path(t))
            for k in (3, 4):
                for labels in product(t.nodes, repeat=k):
                    total += 1
                    star = any(all(set(paths[z][a]) & set(paths[z][b]) == {z}
                                   for a, b in combinations(labels, 2)) for z in t)
                    split = False
                    if k == 4:
                        for a, b in t.edges:
                            if sum(b not in paths[u][a] for u in labels) == 2:
                                split = True
                                break
                    assert star != split, (t.edges, labels)
                    stars += star
                    splits += split
    print(f'PASS assignments={total}, stars={stars}, splits={splits}')


def reachable(g, h):
    if len(g) < len(h) or g.number_of_edges() < h.number_of_edges():
        return False
    if len(g) == len(h):
        return nx.algorithms.isomorphism.GraphMatcher(g, h).subgraph_is_monomorphic()
    return (any(reachable(g.subgraph(set(g)-{v}).copy(), h) for v in g)
            or any(reachable(nx.contracted_nodes(g, a, b, self_loops=False), h)
                   for a, b in g.edges))


def model(g, h):
    hs = list(h)
    for assignment in product(range(-1, len(h)), repeat=len(g)):
        blocks = [{v for v, i in zip(g, assignment) if i == j} for j in range(len(h))]
        if not all(b and nx.is_connected(g.subgraph(b)) for b in blocks):
            continue
        if all(any(g.has_edge(u, v) for u in blocks[hs.index(a)] for v in blocks[hs.index(b)])
               for a, b in h.edges):
            return True
    return False


def model_checks():
    gs = [g for g in nx.graph_atlas_g() if len(g) <= 4]
    total = yes = 0
    for g in gs:
        for h in gs:
            a, b = reachable(g, h), model(g, h)
            assert a == b, (g.edges, h.edges)
            total += 1
            yes += a
    print(f'PASS minor_pairs={total}, positive={yes}, negative={total-yes}')


if __name__ == '__main__':
    tree_checks()
    model_checks()
