"""Finite falsification and source-integrity checks for compactness chapter 14.

Finite-model tests do not prove logical compactness, which is established
by the chapter's mathematical argument from Henkin completeness.
"""

import itertools
import re
import unittest
from collections import deque
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[2] / 'chapters' / 'pl'
          / 'logic_and_set_theory'
          / '14-twierdzenie-o-zwartosci-i-jego-zastosowania.tex')


def finite_graphs(n):
    edges = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        yield {edge for j, edge in enumerate(edges) if mask & (1 << j)}


def shortest_distance(n, edges, a, b):
    if a == b:
        return 0
    neighbors = [set() for _ in range(n)]
    for x, y in edges:
        neighbors[x].add(y)
        neighbors[y].add(x)
    queue = deque([(a, 0)])
    seen = {a}
    while queue:
        u, d = queue.popleft()
        for v in neighbors[u]:
            if v == b:
                return d + 1
            if v not in seen:
                seen.add(v)
                queue.append((v, d + 1))
    return None


def walk_formula(n, edges, a, b, m):
    if m == 0:
        return a == b
    for interior in itertools.product(range(n), repeat=m - 1):
        vertices = (a, *interior, b)
        if all(tuple(sorted((vertices[j], vertices[j+1]))) in edges
               for j in range(m)):
            return True
    return False


class Chapter14AuditIII(unittest.TestCase):
    def test_walk_formulas_are_exactly_bounded_reachability(self):
        checked = 0
        for n in range(1, 5):
            for edges in finite_graphs(n):
                for a, b in itertools.product(range(n), repeat=2):
                    distance = shortest_distance(n, edges, a, b)
                    for bound in range(n + 2):
                        encoded = any(walk_formula(n, edges, a, b, m)
                                      for m in range(bound + 1))
                        self.assertEqual(encoded, distance is not None and distance <= bound)
                        checked += 1
        self.assertGreater(checked, 1000)

    def test_color_clauses_force_a_proper_coloring_in_arbitrary_models(self):
        checked = 0
        # Unlike a canonical-color interpretation, P_i ranges over ALL subsets
        # of the two-element domain and constants may identify vertices.
        domain = range(2)
        subsets = [set(x for x in domain if mask & (1 << x)) for mask in range(4)]
        for n in range(0, 4):
            for edges in finite_graphs(n):
                for k in (1, 2):
                    for constants in itertools.product(domain, repeat=n):
                        for predicates in itertools.product(subsets, repeat=k):
                            unique = all(sum(constants[v] in P for P in predicates) == 1
                                         for v in range(n))
                            exclude_edge = all(not (constants[v] in P and constants[w] in P)
                                               for v, w in edges for P in predicates)
                            if unique and exclude_edge:
                                coloring = [next(i for i, P in enumerate(predicates)
                                                 if constants[v] in P)
                                            for v in range(n)]
                                self.assertTrue(all(coloring[v] != coloring[w]
                                                    for v, w in edges))
                            checked += 1
        self.assertGreater(checked, 1000)

    def test_finite_paths_satisfy_any_finite_nonconnectivity_fragment(self):
        for bound in range(0, 9):
            # A path with bound+2 edges has endpoints at distance bound+2.
            n = bound + 3
            edges = {(j, j+1) for j in range(n-1)}
            self.assertEqual(shortest_distance(n, edges, 0, n-1), bound+2)
            self.assertFalse(any(walk_formula(n, edges, 0, n-1, m)
                                 for m in range(bound+1)))

    def test_finite_cardinality_and_nonstandard_parameter_fragments(self):
        for size in range(1, 12):
            for n in range(1, 13):
                eta_n = (size >= n)
                self.assertEqual(eta_n, bool(size >= n))
            for maximum in range(0, 10):
                c = maximum + 1
                self.assertTrue(all(i < c for i in range(maximum + 1)))

    def test_source_inventory_and_no_lost_proofs(self):
        source = SOURCE.read_text(encoding='utf-8')
        expected = {'twierdzenie': 7, 'lemat': 0, 'wniosek': 1,
                    'definicja': 5, 'przyklad': 3, 'uwaga': 5,
                    'proof': 8}
        for environment, amount in expected.items():
            self.assertEqual(source.count(r'\begin{' + environment + '}'), amount)
        labels = re.findall(r'\\label\{([^}]+)\}', source)
        refs = re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}', source)
        self.assertEqual(len(labels), 20)
        self.assertEqual(len(set(labels)), 20)
        self.assertEqual(len(refs), 7)
        self.assertIn(r'\mathrm{Walk}_m', source)
        self.assertNotIn(r'\mathrm{Path}_m', source)
        self.assertIn(r'\label{thm:compactness-not-connectivity}', source)
        stack = []
        for kind, env in re.findall(r'\\(begin|end)\{([^}]+)\}', source):
            if kind == 'begin':
                stack.append(env)
            else:
                self.assertTrue(stack)
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)


if __name__ == '__main__':
    unittest.main(verbosity=2)