"""Small finite-model falsification checks for chapter 15; not general proofs."""
from itertools import product, combinations, permutations
from pathlib import Path
import unittest

SRC = (Path(__file__).resolve().parents[2]
       / 'chapters/pl/logic_and_set_theory/15-homomorfizmy-izomorfizmy-i-elementarnosc-struktur.tex')

def models(n):
    universe=tuple(range(n))
    for c in universe:
        for values in product(universe, repeat=n):
            for mask in range(1<<n):
                yield {'A':universe,'c':c,'f':dict(zip(universe,values)),
                       'R':{i for i in universe if mask & (1<<i)}}

def tval(t,m,s):
    if t[0]=='v':return s[t[1]]
    if t[0]=='c':return m['c']
    return m['f'][tval(t[1],m,s)]

def sat(phi,m,s):
    k=phi[0]
    if k=='eq':return tval(phi[1],m,s)==tval(phi[2],m,s)
    if k=='R':return tval(phi[1],m,s) in m['R']
    if k=='not':return not sat(phi[1],m,s)
    if k=='and':return sat(phi[1],m,s) and sat(phi[2],m,s)
    if k=='or':return sat(phi[1],m,s) or sat(phi[2],m,s)
    if k=='imp':return not sat(phi[1],m,s) or sat(phi[2],m,s)
    if k in ('ex','all'):
        vals=[sat(phi[2],m,tuple(a if i==phi[1] else v for i,v in enumerate(s))) for a in m['A']]
        return any(vals) if k=='ex' else all(vals)
    raise AssertionError(k)

def homo(a,b,h,reflect=False):
    if h[a['c']] != b['c']:return False
    if any(h[a['f'][x]]!=b['f'][h[x]] for x in a['A']):return False
    if any(x in a['R'] and h[x] not in b['R'] for x in a['A']):return False
    if reflect:
        return len(set(h.values()))==len(h) and all((x in a['R'])==(h[x] in b['R']) for x in a['A'])
    return True

X=('v',0);Y=('v',1);F=('f',X);C=('c',)
FORMULAS=(('R',X),('eq',F,Y),('not',('R',X)),
          ('or',('R',Y),('eq',X,C)),
          ('and',('R',X),('eq',F,Y)),
          ('imp',('R',X),('R',F)),
          ('ex',0,('and',('R',X),('eq',F,Y))),
          ('all',0,('or',('R',X),('eq',F,Y))),
          ('not',('ex',1,('eq',X,Y))),
          ('all',1,('ex',0,('eq',('f',X),Y))))

class Chapter15Tests(unittest.TestCase):
    def test_homomorphism_terms_and_positive_existential(self):
        terms=(X,Y,C,F,('f',F),('f',C))
        positives=(('R',X),('eq',F,Y),('and',('R',X),('eq',X,Y)),
                   ('or',('R',Y),('eq',F,C)),
                   ('ex',0,('R',X)),
                   ('ex',0,('and',('R',X),('eq',('f',X),Y))))
        count=0
        for n,m in product((1,2),repeat=2):
            for a in models(n):
                for b in models(m):
                    for vals in product(b['A'],repeat=n):
                        h=dict(zip(a['A'],vals))
                        if not homo(a,b,h):continue
                        for s in product(a['A'],repeat=2):
                            ss=tuple(h[x] for x in s)
                            for t in terms:self.assertEqual(h[tval(t,a,s)],tval(t,b,ss))
                            for phi in positives:
                                if sat(phi,a,s):self.assertTrue(sat(phi,b,ss))
                            count+=1
        self.assertGreater(count,40)

    def test_isomorphism_preserves_all_connectives_and_quantifiers(self):
        count=0
        for n in (1,2):
            for a in models(n):
                for dest in permutations(a['A']):
                    h=dict(zip(a['A'],dest))
                    inv={v:k for k,v in h.items()}
                    b={'A':a['A'],'c':h[a['c']],
                       'f':{v:h[a['f'][inv[v]]] for v in a['A']},
                       'R':{h[v] for v in a['R']}}
                    self.assertTrue(homo(a,b,h,reflect=True))
                    for s in product(a['A'],repeat=2):
                        for phi in FORMULAS:
                            self.assertEqual(sat(phi,a,s),sat(phi,b,tuple(h[x] for x in s)))
                            count+=1
        self.assertGreater(count,100)

    def test_substructures_preserve_quantifier_free_and_universal(self):
        count=0
        B=(0,1,2)
        for b in models(3):
            for k in (1,2):
                for sub in combinations(B,k):
                    A=set(sub)
                    if b['c'] not in A or any(b['f'][i] not in A for i in A):continue
                    a={'A':sub,'c':b['c'],'f':{i:b['f'][i] for i in A},'R':b['R']&A}
                    for s in product(sub,repeat=2):
                        for phi in FORMULAS[:6]:
                            self.assertEqual(sat(phi,a,s),sat(phi,b,s))
                            count+=1
                    # finite proper substructures cannot be elementary:
                    # B |= exists x (x != each named element of A), A does not.
                    assert len(A)<len(B)
                    self.assertTrue(any(z not in A for z in B))
                    self.assertFalse(any(z not in A for z in sub))
        self.assertGreater(count,100)

    def test_countermodels_negation_universal_and_non_elementarity(self):
        a={'A':(0,),'c':0,'f':{0:0},'R':set()}
        b={'A':(0,),'c':0,'f':{0:0},'R':{0}}
        h={0:0}
        self.assertTrue(homo(a,b,h))
        self.assertTrue(sat(('not',('R',X)),a,(0,0)))
        self.assertFalse(sat(('not',('R',X)),b,(0,0)))
        b2={'A':(0,1),'c':0,'f':{0:0,1:1},'R':{0}}
        a2={'A':(0,),'c':0,'f':{0:0},'R':{0}}
        self.assertTrue(homo(a2,b2,{0:0},reflect=True))
        self.assertTrue(sat(('all',0,('R',X)),a2,(0,0)))
        self.assertFalse(sat(('all',0,('R',X)),b2,(0,0)))
        self.assertTrue(sat(('ex',0,('not',('eq',X,Y))),b2,(0,0)))
        self.assertFalse(sat(('ex',0,('not',('eq',X,Y))),a2,(0,0)))

    def test_source_inventory_and_reference_integrity(self):
        import re
        src=SRC.read_text()
        inv={'definicja':7,'lemat':1,'twierdzenie':5,'proof':6,'przyklad':7,'uwaga':4}
        for e,num in inv.items():self.assertEqual(src.count(r'\begin{'+e+'}'),num)
        labels=re.findall(r'\\label\{([^}]+)\}',src)
        self.assertEqual(len(labels),14)
        self.assertEqual(len(set(labels)),14)
        self.assertIn('dwuargumentowym symbolem relacyjnym $R$',src)
        self.assertIn(r'\mathfrak A,s\models\neg R(x)',src)
        self.assertIn(r'\label{thm:model-tarski-vaught}',src)
        self.assertNotIn('W $\\mathfrak A$ formuła $\\neg R(a)$',src)



class Chapter15TarskiVaughtWitnessTests(unittest.TestCase):
    def test_proper_finite_substructures_fail_witness_condition(self):
        # In a finite proper induced substructure A of B,
        # the formula exists x (x != a1 and ... and x != ak)
        # is witnessed in B but not in A. Parameters a_i come from A.
        witnessed=0
        for b in models(3):
            B=b['A']
            for k in (1,2):
                for sub in combinations(B,k):
                    A=set(sub)
                    if b['c'] not in A or any(b['f'][v] not in A for v in A):
                        continue
                    a={'A':sub,'c':b['c'],
                       'f':{i:b['f'][i] for i in A},'R':b['R']&A}
                    neq=[('not',('eq',('v',0),('v',i+1))) for i in range(k)]
                    body=neq[0]
                    for formula in neq[1:]:body=('and',body,formula)
                    exists=('ex',0,body)
                    assignment=(sub[0],sub[0],sub[-1])
                    self.assertTrue(sat(exists,b,assignment))
                    self.assertFalse(sat(exists,a,assignment))
                    witnessed+=1
        self.assertGreater(witnessed,200)

    def test_source_has_explicit_variable_hygiene_and_general_theory(self):
        src=SRC.read_text(encoding='utf-8')
        self.assertIn(r'Twierdzenia~\ref{thm:sem-alpha-renaming-xlv}', src)
        self.assertIn(r'\operatorname{Th}(\mathfrak C)', src)
        self.assertIn('gdzie $k$ jest arnością symbolu $R$',src)
        self.assertIn(r'zmienne $x_1,\ldots,x_n$ są parami różne',src)


    def test_expanded_constant_not_used_as_reduct_symbol(self):
        src=SRC.read_text(encoding='utf-8')
        self.assertIn(r'\mathfrak M=\mathfrak M^+\upharpoonright\mathcal L_{\mathrm{ar}}',src)
        self.assertIn(r'a:=c^{\mathfrak M^+}',src)
        self.assertNotIn(r'c^{\mathfrak M}',src)
        self.assertIn(r'\mathfrak M\models\neg\sigma',src)
        self.assertIn(r'\overline m^{\mathfrak M}<^{\mathfrak M}a',src)

if __name__=='__main__':unittest.main()