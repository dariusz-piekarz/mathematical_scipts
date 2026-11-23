"""AA-X22: independent exact links AA-29 finite fields, AA-32 discriminant, AA-35 Frobenius.

No probabilistic factorization or floating arithmetic; every test is exact.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import re
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
X = sp.symbols("X")
EXAMPLES = (
    X**3 - X - 1, X**3 - 3*X + 1, X**4 - 2,
    X**4 - X - 1, X**2 - 5, (X**2 - 2)*(X - 3),
)
PRIMES = (2, 3, 5, 7, 11)


def frobenius_power_mod(h, p, k):
    """X^(p^k) in F_p[X]/(h), by binary exponentiation."""
    z = sp.Poly(1, X, modulus=p)
    b = sp.Poly(X, X, modulus=p).rem(h)
    e = p**k
    while e:
        if e % 2:
            z = (z*b).rem(h)
        b = (b*b).rem(h)
        e //= 2
    return z


def factor_degrees(poly, p):
    """Return degree with multiplicities, not silently removing repeated factors."""
    coeff, fac = sp.factor_list(sp.Poly(poly, X, modulus=p))
    return tuple(sorted(deg for f, multiplicity in fac
                        for deg in [f.degree()]
                        for _ in range(multiplicity)))


def monic_remainder(f, g, p):
    """Polynomial remainder over F_p, increasing coefficient order; g monic."""
    r = list(f)
    g = list(g)
    while len(r) >= len(g):
        c = r[-1] % p
        if c:
            for i in range(len(g)):
                r[len(r)-len(g)+i] = (r[len(r)-len(g)+i]-c*g[i]) % p
        r.pop()
    return r


def irreducible_brute(coeff, p):
    """Trial all monic divisors of degree <= floor(deg f/2)."""
    n = len(coeff)-1
    for k in range(1,n//2+1):
        for prefix in product(range(p), repeat=k):
            divisor = (*prefix, 1)
            if not any(monic_remainder(coeff, divisor, p)):
                return False
    return True


class FrobeniusReductionInterface(unittest.TestCase):
    def test_good_reduction_iff_squarefree(self):
        for f in EXAMPLES:
            disc = int(sp.discriminant(f, X))
            self.assertNotEqual(disc, 0)
            for p in (*PRIMES, 23, 59):
                with self.subTest(f=str(f), p=p):
                    poly = sp.Poly(f, X, modulus=p)
                    squarefree = poly.gcd(poly.diff()).degree() == 0
                    self.assertEqual(squarefree, disc % p != 0)
                    degrees = factor_degrees(f, p)
                    self.assertEqual(sum(degrees), sp.degree(f,X))
                    # Equal degrees may come from distinct factors;
                    # multiplicity is verified by the squarefree gcd above.

    def test_frobenius_fixed_root_counts_via_gcd(self):
        for f in EXAMPLES:
            n = sp.degree(f, X)
            disc = int(sp.discriminant(f, X))
            for p in PRIMES:
                if disc % p == 0:
                    continue
                with self.subTest(f=str(f), p=p):
                    h = sp.Poly(f, X, modulus=p)
                    degrees = Counter(factor_degrees(f,p))
                    for k in range(1,n+1):
                        power = frobenius_power_mod(h,p,k)
                        fixed = h.gcd(power - sp.Poly(X,X,modulus=p)).degree()
                        self.assertEqual(fixed, sum(d*v for d,v in degrees.items()
                                                    if k%d==0))
                        # Mobius inversion recovers the number of k-cycles
                        # from independently computed fixed-root counts.
                        fixed_divisors = [
                            (int(d), h.gcd(frobenius_power_mod(h,p,int(d)) -
                                     sp.Poly(X,X,modulus=p)).degree())
                            for d in sp.divisors(k)
                        ]
                        recovered = sum(int(sp.mobius(k//d))*count
                                        for d,count in fixed_divisors)
                        self.assertEqual(recovered, k*degrees.get(k,0))

    def test_irreducible_mobius_formula_by_full_enumeration(self):
        for p in (2,3,5):
            for n in (1,2,3,4):
                with self.subTest(p=p,n=n):
                    count = sum(irreducible_brute((*a,1),p)
                                for a in product(range(p),repeat=n))
                    predicted = sum(int(sp.mobius(d))*p**(n//d)
                                    for d in sp.divisors(n))//n
                    self.assertEqual(count,predicted)
                    self.assertGreater(count,0)

    def test_exact_cubic_frobenius_patterns_and_bad_prime(self):
        f=X**3-X-1
        patterns={2:(3,),5:(1,2),23:(1,1,1),59:(1,1,1)}
        for p,expected in patterns.items():
            with self.subTest(p=p):
                self.assertEqual(factor_degrees(f,p),expected)
                poly=sp.Poly(f,X,modulus=p)
                good=(poly.gcd(poly.diff()).degree()==0)
                self.assertEqual(good,p!=23)
                if p==23:
                    self.assertEqual(poly.eval(10)%p,0)
                    self.assertEqual(poly.diff().eval(10)%p,0)
                else:
                    self.assertEqual(sum(expected),3)

    def test_parity_equals_quadratic_character_of_discriminant(self):
        # For odd good p, Frobenius sign = Legendre(disc mod p).
        # This is stronger than merely checking whether the sign is odd.
        for f in EXAMPLES:
            n=sp.degree(f,X)
            D=int(sp.discriminant(f,X))
            for p in (3,5,7,11,13,17,19,31):
                if D%p==0:
                    continue
                with self.subTest(f=str(f),p=p):
                    s=len(factor_degrees(f,p))
                    sign=(-1)**(n-s)
                    quadratic_character=pow(D%p,(p-1)//2,p)
                    self.assertEqual(quadratic_character,1 if sign==1 else p-1)
        # In F_2 the Legendre-symbol criterion cannot be applied.
        f=X**3-X-1
        self.assertEqual(factor_degrees(f,2),(3,))
        self.assertEqual(int(sp.discriminant(f,X))%2,1)

    def test_source_labels_references_and_required_assumptions(self):
        folder=ROOT/"chapters/pl/abstract_algebra"
        files=sorted(folder.glob("[0-9][0-9]-*.tex"))
        self.assertEqual(len(files),50)
        contents={p.name:p.read_text(encoding="utf8") for p in files}
        all_labels=[z for text in contents.values()
                    for z in re.findall(r"\\label\{([^{}]+)\}",text)]
        self.assertEqual(len(all_labels),len(set(all_labels)))
        focus=(
            "29-struktura-cial-skonczonych-i-wielomiany-nierozkladalne.tex",
            "32-wyroznik-i-grupa-galois.tex",
            "35-redukcja-modulo-p-i-cykle-frobeniusa.tex",
        )
        self.assertEqual(sum(len(re.findall(r"\\label\{", contents[f]))
                             for f in focus),32)
        refs=[z for f in focus for z in re.findall(
            r"\\(?:ref|pageref|eqref|autoref)\{([^{}]+)\}", contents[f])]
        self.assertEqual(len(refs),24)
        self.assertFalse(set(refs)-set(all_labels),set(refs)-set(all_labels))
        for label in (
            "aa:tw:finite-frobenius-roots","aa:tw:finite-irreducible-count",
            "aa:tw:disc-separable","aa:tw:frob-cycles",
            "aa:tw:dedekind-cycle","aa:wn:frob-parity",
        ):
            self.assertIn(label,all_labels)
        self.assertIn("p\\nmid\\operatorname{disc}(f)",
                      contents[focus[2]])

if __name__=="__main__":
    unittest.main()
