"""Niezależne kontrole znaków rozdziału 16. Uruchom: python ten_plik.py.

Sprawdza tożsamości na wszystkich bazowych kołańcuchach małych
sympleksów oraz formułę przekątnej na torusach przez porównanie
rachunku algebry zewnętrznej z wyznacznikiem I-A.
Nie zastępuje dowodów dualności ani twierdzenia Thoma.
Nie wymaga dodatkowych bibliotek i nie zapisuje plików.
"""
from collections import defaultdict
from itertools import combinations, permutations
from random import Random


def boundary(simplex):
    if len(simplex) < 2:
        return []
    return [(simplex[:i] + simplex[i + 1 :], (-1) ** i)
            for i in range(len(simplex))]


def differential(cochain, simplex):
    return sum(sign * cochain(face) for face, sign in boundary(simplex))


def cup(alpha, beta, degree, simplex):
    return alpha(simplex[:degree + 1]) * beta(simplex[degree:])


def add(chain, simplex, coefficient):
    chain[simplex] += coefficient
    if not chain[simplex]:
        del chain[simplex]


def check_cup():
    count = 0
    for p in range(4):
        for q in range(4):
            simplex = tuple(range(p + q + 2))
            for af in combinations(simplex, p + 1):
                for bf in combinations(simplex, q + 1):
                    alpha = lambda face: int(face == af)
                    beta = lambda face: int(face == bf)
                    lhs = differential(lambda face: cup(alpha, beta, p, face), simplex)
                    rhs = (cup(lambda face: differential(alpha, face), beta, p + 1, simplex)
                           + (-1) ** p * cup(alpha, lambda face: differential(beta, face), p, simplex))
                    assert lhs == rhs, (p, q, af, bf, lhs, rhs)
                    count += 1
    print(f'Leibniz: {count} par bazowych kołańcuchów — OK')


def check_cap():
    count = 0
    for m in range(7):
        simplex = tuple(range(m + 1))
        for k in range(m + 1):
            for af in combinations(simplex, k + 1):
                alpha = lambda face: int(face == af)
                lhs, rhs = defaultdict(int), defaultdict(int)
                for face, sign in boundary(simplex[k:]):
                    add(lhs, face, sign * alpha(simplex[:k + 1]))
                if k < m:
                    for face, sign in boundary(simplex):
                        add(rhs, face[k:], (-1) ** k * sign * alpha(face[:k + 1]))
                    add(rhs, simplex[k + 1:], (-1) ** (k + 1)
                        * differential(alpha, simplex[:k + 2]))
                assert lhs == rhs, (m, k, af, dict(lhs), dict(rhs))
                count += 1
    print(f'Brzeg iloczynu kapowego: {count} przypadków bazowych — OK')


def permutation_sign(sequence):
    return (-1) ** sum(x > y for i, x in enumerate(sequence) for y in sequence[i + 1:])


def determinant(matrix):
    n = len(matrix)
    result = 0
    for perm in permutations(range(n)):
        product = permutation_sign(perm)
        for i, j in enumerate(perm):
            product *= matrix[i][j]
        result += product
    return result


def wedge(a, b):
    result = defaultdict(int)
    for I, x in a.items():
        for J, y in b.items():
            if set(I).intersection(J):
                continue
            add(result, tuple(sorted(I + J)), x * y * permutation_sign(I + J))
    return dict(result)


def check_diagonal():
    rng = Random(16016)
    count = 0
    for n in range(1, 5):
        indices = tuple(range(n))
        matrices = [[[int(i == j) for j in indices] for i in indices],
                    [[0 for j in indices] for i in indices]]
        matrices += [[[rng.randrange(-2, 3) for j in indices] for i in indices]
                     for _ in range(30)]
        for A in matrices:
            evaluation = 0
            for k in range(n + 1):
                for I in combinations(indices, k):
                    J = tuple(j for j in indices if j not in I)
                    # a_I wedge b_I is the positive top form.
                    b_I = {J: permutation_sign(I + J)}
                    pullback = {(): 1}
                    for i in I:
                        pullback = wedge(pullback, {(j,): A[i][j] for j in indices})
                    term = wedge(b_I, pullback)
                    evaluation += (-1) ** (n * k) * term.get(indices, 0)
            expected = determinant([[int(i == j) - A[i][j] for j in indices] for i in indices])
            assert evaluation == expected, (n, A, evaluation, expected)
            count += 1
    print(f'Klasa przekątnej / lokalny znak Lefschetza: {count} macierzy — OK')


if __name__ == '__main__':
    check_cup()
    check_cap()
    check_diagonal()
