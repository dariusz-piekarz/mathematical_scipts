"""Independent AA-34 mathematical checks. Run: python -m unittest AA-34-audyt-I-testy.py -v"""
from __future__ import annotations
import itertools, re, unittest
from pathlib import Path
import sympy as sp

SOURCE=Path(__file__).resolve().parents[2] / 'chapters/pl/abstract_algebra/34-rezolwenta-szescienna-i-grupy-galois-stopnia-czwartego.tex'
src=SOURCE.read_text(encoding='utf8')
x,Y=sp.symbols('x Y')
a,b,c,d=sp.symbols('a b c d')
root_syms=sp.symbols('r1 r2 r3 r4')
parts=(frozenset((frozenset((0,1)),frozenset((2,3)))),
       frozenset((frozenset((0,2)),frozenset((1,3)))),
       frozenset((frozenset((0,3)),frozenset((1,2)))))

def action(perm):
    return tuple(parts.index(frozenset(frozenset(perm[i] for i in pair) for pair in part)) for part in parts)

def compose(p,q): return tuple(p[q[i]] for i in range(len(q)))

def betas(rs):
    t,u,v,w=rs
    return (t*u+v*w,t*v+u*w,t*w+u*v)

def symmetric_coefficients(rs):
    return [sum(sp.prod(comb) for comb in itertools.combinations(rs,k)) for k in range(1,5)]

def resolvent_from_coeffs(aa,bb,cc,dd):
    return sp.expand(Y**3-bb*Y**2+(aa*cc-4*dd)*Y-(aa**2*dd+cc**2-4*bb*dd))

def discriminant_from_roots(rs):
    return sp.prod((rs[i]-rs[j])**2 for i in range(len(rs)) for j in range(i+1,len(rs)))

class StructuralTests(unittest.TestCase):
    def test_source_present(self): self.assertGreater(len(src),14000)
    def test_unique_labels(self):
        labs=re.findall(r'\\label\{([^}]+)\}',src)
        self.assertEqual(len(labs),len(set(labs)))
    def test_local_refs(self):
        labs=set(re.findall(r'\\label\{([^}]+)\}',src))
        refs=set(re.findall(r'\\ref\{([^}]+)\}',src))
        external={'aa:tw:vieta-general','aa:tw:disc-alternating','aa:wn:res-sym','aa:tw:disc-separable','aa:tw:cyclotomic-galois'}
        self.assertEqual(refs-labs,external)
    def test_c4_example(self): self.assertIn(r'\label{aa:prz:quartic-c4}',src)
    def test_discriminant_corollary(self): self.assertIn(r'\label{aa:wn:quartic-resolvent-disc}',src)
    def test_factorization_corollary(self): self.assertIn(r'\label{aa:wn:quartic-resolvent-factorization}',src)
    def test_no_old_monom(self): self.assertNotIn('monomów',src)
    def test_quartic_hypotheses(self): self.assertIn('monicznym, nierozkładalnym i rozdzielczym',src)
    def test_no_unclosed_environments(self):
        for env in ('twierdzenie','wniosek','przyklad','proof','definicja','uwaga','enumerate','tikzpicture'):
            self.assertEqual(len(re.findall(r'\\begin\{'+env+r'\}',src)),len(re.findall(r'\\end\{'+env+r'\}',src)),env)

class ActionTests(unittest.TestCase):
    def test_surjectivity(self): self.assertEqual(len({action(p) for p in itertools.permutations(range(4))}),6)
    def test_kernel_V4(self):
        self.assertEqual({p for p in itertools.permutations(range(4)) if action(p)==(0,1,2)},
                         {(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)})
    def test_kernel_normal(self):
        elems=list(itertools.permutations(range(4)))
        ker={p for p in elems if action(p)==(0,1,2)}
        for g in elems:
            inv=tuple(g.index(i) for i in range(4))
            for h in ker: self.assertIn(compose(g,compose(h,inv)),ker)

class FormulaTests(unittest.TestCase):
    def test_betas_sum(self):
        e=symmetric_coefficients(root_syms)
        self.assertEqual(sp.expand(sum(betas(root_syms))-e[1]),0)
    def test_betas_pairwise_products(self):
        t=betas(root_syms);e=symmetric_coefficients(root_syms)
        self.assertEqual(sp.expand(sum(t[i]*t[j] for i,j in ((0,1),(0,2),(1,2)))-(e[0]*e[2]-4*e[3])),0)
    def test_betas_triple_product(self):
        t=betas(root_syms);e=symmetric_coefficients(root_syms)
        self.assertEqual(sp.expand(sp.prod(t)-(e[0]**2*e[3]+e[2]**2-4*e[1]*e[3])),0)
    def test_equal_discriminants_symbolic(self):
        e=symmetric_coefficients(root_syms)
        r=resolvent_from_coeffs(-e[0],e[1],-e[2],e[3])
        self.assertEqual(sp.expand(sp.discriminant(r,Y)-discriminant_from_roots(root_syms)),0)
    def test_formula_pure_polynomial(self):
        e=symmetric_coefficients(root_syms)
        r=resolvent_from_coeffs(-e[0],e[1],-e[2],e[3]); b=betas(root_syms)
        self.assertEqual(sp.expand(r-sp.prod(Y-v for v in b)),0)

class ExampleTests(unittest.TestCase):
    examples=(
        ('S4',x**4-x-1,24,Y**3+4*Y-1),
        ('D4',x**4-2,8,Y**3+8*Y),
        ('V4',x**4-10*x**2+1,4,Y**3+10*Y**2-4*Y-40),
        ('C4',x**4+x**3+x**2+x+1,4,Y**3-Y**2-3*Y+2),
    )
    def test_cyclotomic_shift(self): self.assertEqual(sp.expand((x+1)**4+(x+1)**3+(x+1)**2+(x+1)+1),x**4+5*x**3+10*x**2+10*x+5)
    def test_cyclotomic_quadratic_factor(self): self.assertEqual(sp.expand((Y-2)*(Y**2+Y-1)),Y**3-Y**2-3*Y+2)
    def test_v4_field(self): self.assertEqual(sp.expand((x**2-5)**2-24),x**4-10*x**2+1)
    def test_s4_discriminant(self): self.assertEqual(sp.discriminant(x**4-x-1,x),-283)
    def test_c4_discriminant(self): self.assertEqual(sp.discriminant(x**4+x**3+x**2+x+1,x),125)
    def test_resolvent_discriminant_s4(self): self.assertEqual(sp.discriminant(Y**3+4*Y-1,Y),-283)
    def test_resolvent_discriminant_c4(self): self.assertEqual(sp.discriminant(Y**3-Y**2-3*Y+2,Y),125)
    def test_cyclotomic_irreducible(self): self.assertTrue(sp.Poly(x**4+x**3+x**2+x+1,x,domain='QQ').is_irreducible)
    def test_discriminant_quartic_special(self):
        for cc,dd in [(-1,-1),(3,1),(0,-2),(2,3)]:
            self.assertEqual(sp.discriminant(x**4+cc*x+dd,x),256*dd**3-27*cc**4)


def make_example_case(name,poly,order,resol):
    def test(self):
        P=sp.Poly(poly,x,domain='QQ');aa,bb,cc,dd=P.all_coeffs()[1:]
        self.assertEqual(resolvent_from_coeffs(aa,bb,cc,dd),resol)
        self.assertTrue(P.is_irreducible)
        group,_=sp.polys.numberfields.galois_group(poly,x)
        self.assertEqual(group.order(),order)
        self.assertEqual(sp.discriminant(resol,Y),sp.discriminant(poly,x))
        roots_count=len(sp.factor_list(resol)[1]);self.assertGreaterEqual(roots_count,1)
    test.__name__='test_example_'+name.lower()
    return test
for name,poly,order,resol in ExampleTests.examples: setattr(ExampleTests,'test_example_'+name.lower(),make_example_case(name,poly,order,resol))

# 24 separately counted tests verify the homomorphism law for one left argument against all right arguments.
perms=list(itertools.permutations(range(4)))
for idx,p in enumerate(perms):
    def f(self,p=p):
        for q in perms: self.assertEqual(action(compose(p,q)),compose(action(p),action(q)))
    setattr(ActionTests,f'test_homomorphism_left_{idx:02d}',f)

# 12 numerical and modular identity tests. Repeated roots are intentionally included.
cases=[(0,1,2,3),(-2,-1,1,4),(0,0,1,3),(-1,2,2,2),(1,1,1,1),
       (-3,-2,-1,2),(2,3,4,5),(0,1,1,2),(0,0,0,2),(0,0,0,0),
       (1,2,3,7),(-2,0,3,8)]
for idx,rs in enumerate(cases):
    def numeric(self,rs=rs):
        t=betas(rs); e=symmetric_coefficients(rs)
        r=resolvent_from_coeffs(-e[0],e[1],-e[2],e[3])
        self.assertEqual(sp.expand(r-sp.prod(Y-z for z in t)),0)
        self.assertEqual(sp.discriminant(r,Y),discriminant_from_roots(rs))
        for p in (2,3,5,7):
            self.assertEqual(int(sp.discriminant(r,Y))%p,int(discriminant_from_roots(rs))%p)
    setattr(FormulaTests,f'test_values_{idx:02d}',numeric)

# 16 finite-characteristic checks, verify direct root identities over all roots reduced mod p.
for p in (2,3,5,7):
    for idx,rs in enumerate(cases[:4]):
        def modular(self,p=p,rs=rs):
            rr=tuple(v%p for v in rs);be=betas(rr);e=symmetric_coefficients(rr)
            r=resolvent_from_coeffs(-e[0],e[1],-e[2],e[3])
            delta=discriminant_from_roots(rr)
            self.assertTrue(all(int(z)%p==0 for z in sp.Poly(sp.expand(r-sp.prod(Y-v for v in be)),Y).all_coeffs()))
            self.assertEqual(int(sp.discriminant(r,Y)-delta)%p,0)
        setattr(FormulaTests,f'test_gf{p}_roots{idx}',modular)

if __name__=='__main__': unittest.main(verbosity=2)
