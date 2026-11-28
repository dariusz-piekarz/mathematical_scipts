"""AA-X16: exact S3 group algebra, Maschke and character projector checks."""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[2]
S3=list(permutations(range(3)))
IDENT=(0,1,2)
def multiply(g,h):
    return tuple(g[h[i]] for i in range(3))
def inverse(g):
    return tuple(g.index(i) for i in range(3))
def parity(g):
    return (-1)**sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))
def kind(g):
    if g==IDENT:return "e"
    if parity(g)==-1:return "t"
    return "c"
CHARS={
    "trivial":{"e":1,"t":1,"c":1},
    "sign":{"e":1,"t":-1,"c":1},
    "standard":{"e":2,"t":0,"c":-1},
}
DIMS={"trivial":1,"sign":1,"standard":2}

def element(terms=()):
    a={g:Q(0) for g in S3}
    for g,v in terms:a[g]+=Q(v)
    return a
def add(a,b):
    return {g:a[g]+b[g] for g in S3}
def prod(a,b):
    out=element()
    for g in S3:
        for h in S3:out[multiply(g,h)]+=a[g]*b[h]
    return out
ONE=element([(IDENT,1)])
ZERO=element()
def projector(chi):
    return element((g,Q(DIMS[chi]*CHARS[chi][kind(inverse(g))],len(S3))) for g in S3)

def matrix_rep(g):
    # Action on the 2D sum-zero subspace of Q^3 in basis (1,-1,0), (0,1,-1).
    b1=(1,-1,0)
    b2=(0,1,-1)
    v1=tuple(b1[g.index(i)] for i in range(3))
    v2=tuple(b2[g.index(i)] for i in range(3))
    return ((Q(v1[0]),Q(v2[0])),(Q(-v1[2]),Q(-v2[2])))
def mmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mfrom_group_algebra(a):
    return tuple(tuple(sum(a[g]*matrix_rep(g)[i][j] for g in S3) for j in range(2)) for i in range(2))
I2=((Q(1),Q(0)),(Q(0),Q(1)))
Z2=((Q(0),Q(0)),(Q(0),Q(0)))

def rank(a):
    a=[list(row) for row in a]
    n=len(a)
    piv=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(piv,n) if a[i][col]),None)
        if pivot is None:continue
        a[piv],a[pivot]=a[pivot],a[piv]
        d=a[piv][col]
        a[piv]=[x/d for x in a[piv]]
        for i in range(n):
            if i!=piv:
                f=a[i][col]
                a[i]=[a[i][j]-f*a[piv][j] for j in range(len(a[i]))]
        piv+=1
        if piv==n:break
    return piv

class GroupAlgebraRepresentationInterface(unittest.TestCase):
    def test_s3_exact_representation_and_universal_extension(self):
        self.assertEqual(len(S3),6)
        for g in S3:
            self.assertEqual(multiply(g,inverse(g)),IDENT)
            self.assertEqual(mmul(matrix_rep(g),matrix_rep(inverse(g))),I2)
            for h in S3:
                self.assertEqual(mmul(matrix_rep(g),matrix_rep(h)),matrix_rep(multiply(g,h)))
                ag=element([(g,1)])
                bh=element([(h,1)])
                self.assertEqual(mfrom_group_algebra(prod(ag,bh)),
                                 mmul(mfrom_group_algebra(ag),mfrom_group_algebra(bh)))
    def test_class_table_and_character_orthogonality(self):
        classes={c:[g for g in S3 if kind(g)==c] for c in ("e","t","c")}
        self.assertEqual([len(classes[c]) for c in ("e","t","c")],[1,3,2])
        self.assertEqual(sum(d*d for d in DIMS.values()),6)
        for a in CHARS:
            for b in CHARS:
                q=sum(len(classes[c])*CHARS[a][c]*CHARS[b][c] for c in classes)
                self.assertEqual(q,6*int(a==b))
        for c in classes:
            for k in classes:
                q=sum(CHARS[a][c]*CHARS[a][k] for a in CHARS)
                self.assertEqual(q,6//len(classes[c]) if c==k else 0)
    def test_primitive_central_idempotents(self):
        es={name:projector(name) for name in CHARS}
        self.assertEqual(add(add(es["trivial"],es["sign"]),es["standard"]),ONE)
        for a,ea in es.items():
            self.assertEqual(prod(ea,ea),ea)
            for b,eb in es.items():
                if a!=b:self.assertEqual(prod(ea,eb),ZERO)
            for g in S3:
                basis=element([(g,1)])
                self.assertEqual(prod(ea,basis),prod(basis,ea))
    def test_projectors_on_simple_modules(self):
        for name in CHARS:
            e=projector(name)
            for rep in CHARS:
                scalar=sum(e[g]*CHARS[rep][kind(g)] for g in S3)
                if rep in ("trivial","sign"):
                    self.assertEqual(scalar,Q(1) if rep==name else Q(0))
            self.assertEqual(mfrom_group_algebra(e),I2 if name=="standard" else Z2)
    def test_regular_module_multiplicities(self):
        for name in CHARS:
            e=projector(name)
            mult=[[e[multiply(g,inverse(h))] for h in S3] for g in S3]
            trace=sum(mult[i][i] for i in range(6))
            expected=DIMS[name]**2
            self.assertEqual(trace,expected)
            self.assertEqual(rank(mult),expected)
    def test_modular_obstruction_f2c2(self):
        def f2mul(a,b):
            return ((a[0]*b[0]+a[1]*b[1])%2,(a[0]*b[1]+a[1]*b[0])%2)
        one=(1,0); g=(0,1); u=(1,1)
        self.assertNotEqual(u,(0,0))
        self.assertEqual(f2mul(u,u),(0,0))
        self.assertEqual(f2mul(g,u),u)
        # The only 1D invariant submodule in F2[C2] is span((1,1)).
        vectors=[(1,0),(0,1),(1,1)]
        invariant=[v for v in vectors if f2mul(g,v)==v]
        self.assertEqual(invariant,[u])
        self.assertEqual(2%2,0)
        self.assertNotEqual(prod(element([(IDENT,1),(S3[1],-1)]),
                                 element([(IDENT,1),(S3[1],-1)])),ZERO)
    def test_source_definitions_and_links(self):
        files=[
          "15-pierscienie-nieprzemienne-i-algebry-grupowe.tex",
          "41-reprezentacje-grup-i-twierdzenie-maschkego.tex",
          "42-lemat-schura-charaktery-i-ortogonalnosc.tex",
        ]
        sources=[(ROOT/"chapters/pl/abstract_algebra"/f).read_text(encoding="utf-8") for f in files]
        labels=[z for a in sources for z in re.findall(r"\\label\{([^{}]+)\}",a)]
        refs=[z for a in sources for z in re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}",a)]
        self.assertEqual(len(labels),65)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertTrue(set(refs)<=set(labels),set(refs)-set(labels))
        for label in ("aa:def:nc-group-ring","aa:tw:nc-group-ring-universal",
                      "aa:prop:rep-modules","aa:tw:maschke",
                      "aa:tw:regular-character","aa:prop:isotypic-projector"):
            self.assertIn(label,labels)

if __name__=="__main__":
    unittest.main()
