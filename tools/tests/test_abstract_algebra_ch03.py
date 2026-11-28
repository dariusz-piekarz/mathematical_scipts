"""Audited AA-03: structure and independent finite models for group actions."""
from itertools import permutations, product
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
PARTS = [ROOT / f"chapters/pl/abstract_algebra/{name}" for name in (
    "01-grupy-podgrupy-i-grupy-cykliczne.tex",
    "02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex",
    "03-dzialania-grup-orbity-i-rownanie-klas.tex",
)]

def mul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    return tuple(a.index(i) for i in range(len(a)))

def conj(x,g):
    return mul(mul(g,x),inv(g))

def gen(*generators):
    e=tuple(range(len(generators[0])))
    elements={e}
    while True:
        new=elements|{mul(x,g) for x in elements for g in generators}|{mul(g,x) for x in elements for g in generators}
        if new==elements:return tuple(sorted(elements))
        elements=new

def coset(g,h):
    return frozenset(mul(g,x) for x in h)

def orbits(group,points,action):
    return {frozenset(action(g,x) for g in group) for x in points}

class AbstractAlgebraAA03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources=[p.read_text('utf8') for p in PARTS]
        cls.s3=tuple(permutations(range(3)))
        cls.d4=gen((1,2,3,0),(0,3,2,1))

    def test_structure_labels_refs(self):
        s=self.sources[-1]
        labels=re.findall(r'\\label\{([^}]+)\}',s)
        refs=re.findall(r'\\(?:ref|eqref|autoref|pageref|nameref)\{([^}]+)\}',s)
        all_labels=set(re.findall(r'\\label\{([^}]+)\}','\n'.join(self.sources)))
        self.assertEqual(len(labels),21)
        self.assertEqual(len(set(labels)),21)
        self.assertTrue(all(x.startswith('aa:') for x in labels))
        self.assertTrue(set(refs)<=all_labels)
        self.assertEqual(s.count(r'\begin{proof}'),11)
        self.assertEqual(s.count(r'\end{proof}'),11)
        for env in ('lemat','twierdzenie','definicja','przyklad','uwaga'):
            self.assertEqual(s.count('\\begin{'+env+'}'),s.count('\\end{'+env+'}'))

    def test_orbit_stabilizer_s4(self):
        g=tuple(permutations(range(4)))
        for x in range(4):
            stab={p for p in g if p[x]==x}
            self.assertEqual(len(stab),6)
            self.assertEqual(len({p[x] for p in g}),4)

    def test_s3_cosets_and_core(self):
        g=self.s3;e=(0,1,2);h={e,(0,2,1)}
        cs={coset(x,h) for x in g}
        kernel={x for x in g if all(coset(mul(x,a),h)==c for c in cs for a in c)}
        core=set.intersection(*({conj(x,a) for x in h} for a in g))
        self.assertEqual(kernel,{e})
        self.assertEqual(core,kernel)
        self.assertEqual(len(cs),3)

    def test_conjugacy_classes(self):
        for g in (self.s3,self.d4):
            cs=orbits(g,g,lambda a,x:conj(x,a))
            z={x for x in g if all(mul(x,a)==mul(a,x) for a in g)}
            self.assertEqual(sum(map(len,cs)),len(g))
            self.assertEqual(len(z),sum(len(c) for c in cs if len(c)==1))
            for x in g:
                cent={a for a in g if mul(x,a)==mul(a,x)}
                self.assertEqual(len({conj(x,a) for a in g}),len(g)//len(cent))

    def test_normalizers_d4(self):
        g=self.d4;e=(0,1,2,3)
        sub=[]
        for mask in range(1,1<<len(g)):
            h=frozenset(x for i,x in enumerate(g) if mask>>i&1)
            if e in h and all(mul(a,inv(b)) in h for a in h for b in h):sub.append(h)
        self.assertEqual(len(sub),10)
        for h in sub:
            normalizer={a for a in g if {conj(x,a) for x in h}==set(h)}
            self.assertTrue(set(h)<=normalizer)
            self.assertTrue(all(conj(x,a) in h for a in normalizer for x in h))
            self.assertTrue(all(mul(a,inv(b)) in normalizer for a in normalizer for b in normalizer))

    def test_burnside_square_colors(self):
        g=self.d4
        for k,expected in ((2,6),(3,21)):
            colors=tuple(product(range(k),repeat=4))
            def act(a,c):
                ia=inv(a);return tuple(c[ia[i]] for i in range(4))
            fixed=sum(sum(act(a,c)==c for c in colors) for a in g)
            self.assertEqual(fixed,expected*len(g))
            self.assertEqual(len(orbits(g,colors,act)),expected)

    def test_affine_group_five_points(self):
        g=tuple((a,b) for a in range(1,5) for b in range(5))
        def multiply(x,y):
            a,b=x;c,d=y;return (a*c%5,(a*d+b)%5)
        def action(x,y):
            a,b=x;return (a*y+b)%5
        self.assertEqual(len(g),20)
        self.assertEqual({x for x in g if all(action(x,y)==y for y in range(5))},{(1,0)})
        for y in range(5):
            self.assertEqual(len({action(x,y) for x in g}),5)
            self.assertEqual(len({x for x in g if action(x,y)==y}),4)
        for x in g:
            for y in g:
                for z in range(5):
                    self.assertEqual(action(multiply(x,y),z),action(x,action(y,z)))

if __name__=='__main__':
    unittest.main()
