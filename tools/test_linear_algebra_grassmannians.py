"""Exact tests for Gr(2,4) charts and Pluecker coordinates."""
from fractions import Fraction as F
from itertools import product

def det2(row1, row2):
    return row1[0]*row2[1]-row1[1]*row2[0]

tested = 0
for tup in product((-2,-1,0,1,2), repeat=8):
    a = [[F(tup[2*i+j]) for j in range(2)] for i in range(4)]
    d = det2(a[0],a[1])
    if d == 0:
        continue
    p = {(i,j): det2(a[i],a[j])
         for i in range(4) for j in range(i+1,4)}
    assert p[0,1]*p[2,3]-p[0,2]*p[1,3]+p[0,3]*p[1,2] == 0
    inv = [[a[1][1]/d, -a[0][1]/d],
           [-a[1][0]/d, a[0][0]/d]]
    graph = [
        [sum(a[i][k]*inv[k][j] for k in range(2)) for j in range(2)]
        for i in range(4)
    ]
    assert graph[0] == [F(1),F(0)]
    assert graph[1] == [F(0),F(1)]
    for i in (2,3):
        assert graph[i][0] == -p[1,i]/d
        assert graph[i][1] == p[0,i]/d
    # Determinant of this basis change is 1.
    t = [[F(1),F(1)],[F(1),F(2)]]
    other = [[sum(a[i][k]*t[k][j] for k in range(2))
              for j in range(2)] for i in range(4)]
    for i in range(4):
        for j in range(i+1,4):
            assert det2(other[i],other[j]) == p[i,j]
    tested += 1
    if tested >= 500:
        break
assert tested == 500
print(f"Grassmann charts and Pluecker relation: {tested} exact PASS")
