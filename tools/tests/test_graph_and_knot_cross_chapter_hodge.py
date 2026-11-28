"""Cross-chapter exact regressions; no third-party dependencies."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "chapters/pl/graph_and_knot_theory"


def rank(rows, width):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for j in range(width):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        a[r] = [x / v for x in a[r]]
        for i in range(r + 1, len(a)):
            v = a[i][j]
            if v:
                a[i] = [x - v * z for x, z in zip(a[i], a[r])]
        r += 1
    return r


def run():
    count = regular = 0
    for n in range(1, 6):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [e for j, e in enumerate(possible) if mask >> j & 1]
            m = len(edges)
            b = [[int(v == y) - int(v == x) for x, y in edges]
                 for v in range(n)]
            adj = [[int((min(u, v), max(u, v)) in edges)
                    for v in range(n)] for u in range(n)]
            deg = [sum(row) for row in adj]
            unseen = set(range(n))
            c = 0
            while unseen:
                c += 1
                todo = [unseen.pop()]
                while todo:
                    u = todo.pop()
                    reached = {v for v in unseen if adj[u][v]}
                    unseen -= reached
                    todo.extend(reached)
            bt = [[b[v][j] for v in range(n)] for j in range(m)]
            l0 = [[sum(x*y for x, y in zip(b[u], b[v]))
                   for v in range(n)] for u in range(n)]
            l1 = [[sum(x*y for x, y in zip(bt[i], bt[j]))
                   for j in range(m)] for i in range(m)]
            assert rank(b, m) == rank(bt, n) == n-c
            assert m-rank(b, m) == m-rank(l1, m) == m-n+c
            assert n-rank(l0, n) == c
            assert l0 == [[(deg[u] if u == v else 0)-adj[u][v]
                           for v in range(n)] for u in range(n)]
            if deg[0] > 0 and len(set(deg)) == 1:
                d = deg[0]
                norm = [[Fraction(int(u == v))-Fraction(adj[u][v], d)
                         for v in range(n)] for u in range(n)]
                assert [[d*x for x in row] for row in norm] == l0
                regular += 1
            count += 1
    assert count == 1099
    # C3 oriented cyclically: boundary of the 2-simplex has all +1.
    b = [[-1,0,1],[1,-1,0],[0,1,-1]]
    d0 = [list(col) for col in zip(*b)]
    d1 = [[1,1,1]]
    assert all(sum(d0[i][j] for i in range(3)) == 0 for j in range(3))
    assert 3-rank(d0, 3) == 1
    assert 3-rank(d1, 3)-rank(d0, 3) == 0
    s6 = next(CH.glob("06-*.tex")).read_text(encoding="utf-8")
    s8 = next(CH.glob("08-*.tex")).read_text(encoding="utf-8")
    s16 = next(CH.glob("16-*.tex")).read_text(encoding="utf-8")
    s43 = next(CH.glob("43-*.tex")).read_text(encoding="utf-8")
    assert r"\dim\ker B=m-n+c" in s6
    assert r"\dim\operatorname{im}B^T=\operatorname{rank}B^T" in s6
    assert r"\lambda_j(L_G)=d\lambda_j(\mathcal L)" in s8
    assert r"\dim\ker d_1=2" in s16
    assert r"\mathcal L=d^{-1}L_G" in s43
    assert r"$a^0=1$ także dla $a=0$" in s43
    print(f"PASS: {count} labelled simple graphs, {regular} positive-degree regular graphs, C3 and filled triangle, source conventions")


if __name__ == "__main__":
    run()
