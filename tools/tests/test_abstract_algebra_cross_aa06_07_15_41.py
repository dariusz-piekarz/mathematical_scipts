"""AA-X21: dihedral presentations, noncommutative group algebras and modules.

All finite-group and matrix computations are exact and dependency-free.
"""
from itertools import product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
I2 = ((1, 0), (0, 1))


def group(n):
    """D_(2n): (i,j) represents r**i s**j."""
    return tuple(product(range(n), range(2)))


def compose(n, a, b):
    i, j = a
    k, l = b
    return ((i + ((-1) ** j) * k) % n, (j + l) % 2)


def action(n, g, x):
    i, j = g
    return (i + ((-1) ** j) * x) % n


def basis(n, element):
    return tuple(int(g == element) for g in group(n))


def alg_mul(n, a, b, p=None):
    gg = group(n)
    positions = {g: i for i, g in enumerate(gg)}
    out = [0] * len(gg)
    for i, g in enumerate(gg):
        for j, h in enumerate(gg):
            k = positions[compose(n, g, h)]
            out[k] += a[i] * b[j]
    if p is not None:
        out = [x % p for x in out]
    return tuple(out)


def matmul(a, b, p=None):
    result = tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                         for j in range(2)) for i in range(2))
    if p is not None:
        result = tuple(tuple(x % p for x in row) for row in result)
    return result


def power(a, k, p=None):
    out = I2
    for _ in range(k):
        out = matmul(out, a, p)
    return out


def matrix_words(n, R, S, p=None):
    return { (i, j): matmul(power(R, i, p), power(S, j, p), p)
             for i, j in group(n) }


class PresentationGroupAlgebraInterface(unittest.TestCase):
    def test_dihedral_group_laws_and_normal_forms(self):
        for n in (3, 4, 5, 6):
            with self.subTest(n=n):
                gg = group(n)
                e, r, s = (0, 0), (1, 0), (0, 1)
                self.assertEqual(len(gg), 2*n)
                self.assertEqual(len(set(gg)), 2*n)
                for a in gg:
                    self.assertEqual(compose(n, e, a), a)
                    self.assertEqual(compose(n, a, e), a)
                    for b in gg:
                        for c in gg:
                            self.assertEqual(
                                compose(n, compose(n, a, b), c),
                                compose(n, a, compose(n, b, c)))
                self.assertEqual(compose(n, s, r), compose(n, (n-1,0), s))

    def test_faithful_vertex_permutation_representation(self):
        for n in (3, 4, 5, 6):
            with self.subTest(n=n):
                gg = group(n)
                perms = [tuple(action(n, g, v) for v in range(n)) for g in gg]
                self.assertEqual(len(set(perms)), 2*n)
                for a in gg:
                    for b in gg:
                        ab = compose(n, a, b)
                        self.assertEqual(
                            tuple(action(n, ab, v) for v in range(n)),
                            tuple(action(n, a, action(n, b, v))
                                  for v in range(n)))

    def test_dihedral_group_algebra_relations_and_independent_basis(self):
        for n in (3, 4, 5):
            with self.subTest(n=n):
                one, r, s = (basis(n, (0,0)), basis(n, (1,0)),
                             basis(n, (0,1)))
                z = one
                for _ in range(n):
                    z = alg_mul(n,z,r)
                self.assertEqual(z,one)
                self.assertEqual(alg_mul(n,s,s),one)
                self.assertEqual(alg_mul(n,s,r),
                                 alg_mul(n,basis(n,(n-1,0)),s))
                # All 2n normal monomials u**i v**j are distinct basis vectors.
                normal_forms = [
                    alg_mul(n,basis(n,(i,0)),basis(n,(0,j)))
                    for i,j in group(n)]
                self.assertEqual(len(set(normal_forms)),2*n)
                self.assertEqual(set(normal_forms),
                                 {basis(n,g) for g in group(n)})
                # (Sum a_g[g])(Sum b_h[h]) matches the semidirect multiplication.
                a=tuple(2*i-3 for i in range(2*n))
                b=tuple(3-i for i in range(2*n))
                c=tuple((-1)**i for i in range(2*n))
                self.assertEqual(alg_mul(n,alg_mul(n,a,b),c),
                                 alg_mul(n,a,alg_mul(n,b,c)))

    def test_regular_module_is_faithful_and_respects_relators(self):
        for n in (3, 4, 5):
            with self.subTest(n=n):
                gg = group(n)
                e=basis(n,(0,0))
                for g in gg:
                    for h in gg:
                        self.assertEqual(
                            alg_mul(n,basis(n,g),basis(n,h)),
                            basis(n,compose(n,g,h)))
                    self.assertEqual(alg_mul(n,basis(n,g),e),basis(n,g))
                # The free K-span of group elements is visibly 2n dimensional.
                self.assertEqual(len({alg_mul(n,basis(n,g),e) for g in gg}),2*n)

    def test_small_exact_matrix_representations(self):
        models=(
            (3, ((0,-1),(1,-1)), ((-1,1),(0,1))),
            (4, ((0,-1),(1,0)), ((1,0),(0,-1))),
        )
        for n,R,S in models:
            with self.subTest(n=n):
                self.assertEqual(power(R,n),I2)
                self.assertEqual(power(S,2),I2)
                self.assertEqual(matmul(S,R),
                                 matmul(power(R,n-1),S))
                images=matrix_words(n,R,S)
                self.assertEqual(len(set(images.values())),2*n)
                for a in group(n):
                    for b in group(n):
                        self.assertEqual(
                            matmul(images[a],images[b]),
                            images[compose(n,a,b)])

    def test_characteristic_two_relators_do_not_ensure_faithfulness(self):
        # D8's planar integral 2x2 matrices degenerate mod 2,
        # but the group algebra's regular module remains faithful over F2.
        n=4
        R=((0,-1),(1,0))
        S=((1,0),(0,-1))
        images=matrix_words(n,R,S,p=2)
        self.assertEqual(len(set(images.values())),2)
        self.assertEqual(images[(0,1)],I2)
        self.assertEqual(power(R,4,p=2),I2)
        self.assertEqual(power(S,2,p=2),I2)
        self.assertEqual(matmul(S,R,p=2),matmul(power(R,3,p=2),S,p=2))
        self.assertEqual(len({alg_mul(n,basis(n,g),basis(n,(0,0)),p=2)
                              for g in group(n)}),8)
        # In contrast, the S3 standard 2x2 integral matrices stay faithful
        # in both F2 and F3 (although neither characteristic is semisimple).
        R3=((0,-1),(1,-1))
        S3=((-1,1),(0,1))
        for p in (2,3):
            image=matrix_words(3,R3,S3,p=p)
            self.assertEqual(len(set(image.values())),6)
            self.assertEqual(power(R3,3,p),I2)
            self.assertEqual(power(S3,2,p),I2)

    def test_one_dimensional_characters_and_abelianization(self):
        for n in (3,4,5,6):
            with self.subTest(n=n):
                chars=[]
                for rr,ss in product((-1,1),repeat=2):
                    if rr**n!=1 or ss**2!=1 or ss*rr!=rr**(n-1)*ss:
                        continue
                    chi={g:rr**g[0]*ss**g[1] for g in group(n)}
                    self.assertTrue(all(
                        chi[compose(n,g,h)]==chi[g]*chi[h]
                        for g in group(n) for h in group(n)))
                    chars.append(chi)
                self.assertEqual(len(chars),2 if n%2 else 4)
                # Commutator quotient is C2 for n odd, C2 x C2 for n even.
                # In characteristic 2 the signs coincide, not the group elements.
                self.assertEqual(len({tuple(v%2 for v in chi.values())
                                      for chi in chars}),1)

    def test_source_references_and_compatibility(self):
        folder=ROOT/"chapters/pl/abstract_algebra"
        paths=sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(paths),50)
        source={p.name:p.read_text(encoding="utf-8") for p in paths}
        labels=[m for s in source.values()
                for m in re.findall(r"\\label\{([^{}]+)\}",s)]
        self.assertEqual(len(labels),len(set(labels)))
        focus=(
          "06-iloczyny-proste-polproste-i-rozszerzenia-grup.tex",
          "07-grupy-wolne-prezentacje-i-twierdzenie-nielsena-schreiera.tex",
          "15-pierscienie-nieprzemienne-i-algebry-grupowe.tex",
          "41-reprezentacje-grup-i-twierdzenie-maschkego.tex",
        )
        self.assertEqual(sum(len(re.findall(r"\\label\{",source[p]))
                             for p in focus),93)
        refs=[m for p in focus for m in re.findall(
            r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}",source[p])]
        self.assertEqual(len(refs),41)
        self.assertFalse(set(refs)-set(labels),set(refs)-set(labels))
        for item in (
            "aa:tw:presentation-universal","aa:prz:presentations-basic",
            "aa:prz:dihedral-semidirect","aa:prz:s3-semidirect",
            "aa:tw:nc-group-ring-universal","aa:tw:nc-free-universal",
            "aa:prop:rep-modules",
        ):
            self.assertIn(item,labels)


if __name__=="__main__":
    unittest.main()
