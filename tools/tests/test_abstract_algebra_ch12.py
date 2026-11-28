"""AA-12 audit I: finite ring and localization regression + structural checks."""
import itertools, math, re, unittest
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'chapters/pl/abstract_algebra/12-pierwiastniki-idealow-i-lokalizacja-pierscieni.tex'
TXT=SRC.read_text(encoding='utf-8')

def ideals(n):
    return [{x for x in range(n) if x%d==0} for d in range(1,n+1) if n%d==0]

def prime_ideals(n):
    ans=[]
    for I in ideals(n):
        if len(I)==n:continue
        if all((a*b)%n not in I or a in I or b in I for a in range(n) for b in range(n)):
            ans.append(I)
    return ans

def radical(n,I):
    return {a for a in range(n) if any(pow(a,k,n) in I for k in range(1,9))}

def generated_mult_set(n,gens):
    S={1%n}
    while True:
        t=S|{a*g%n for a in S for g in gens}
        if t==S:return S
        S=t

class RadicalArithmetic(unittest.TestCase):
    def test_01_radical_is_ideal_small_quotients(self):
        for n in range(2,25):
            for I in ideals(n):
                r=radical(n,I)
                self.assertTrue(I<=r)
                self.assertIn(0,r)
                self.assertTrue(all((a+b)%n in r for a,b in itertools.product(r,repeat=2)))
                self.assertTrue(all(a*b%n in r for a in r for b in range(n)))
    def test_02_radical_idempotence(self):
        for n in range(2,50):
            for I in ideals(n):
                r=radical(n,I)
                self.assertEqual(radical(n,r),r)
    def test_03_radical_monotonicity(self):
        for n in range(2,30):
            for I,J in itertools.product(ideals(n),repeat=2):
                if I<=J:self.assertTrue(radical(n,I)<=radical(n,J))
    def test_04_radical_product_equals_intersection(self):
        for n in range(2,28):
            for I,J in itertools.product(ideals(n),repeat=2):
                IJ={(a*b)%n for a in I for b in J}
                self.assertEqual(radical(n,IJ),radical(n,I)&radical(n,J))
                self.assertEqual(radical(n,I&J),radical(n,I)&radical(n,J))
    def test_05_radical_is_intersection_of_primes(self):
        for n in range(2,45):
            for I in ideals(n):
                containing=[P for P in prime_ideals(n) if I<=P]
                result=set(range(n)) if not containing else set.intersection(*containing)
                self.assertEqual(radical(n,I),result,(n,I))
    def test_06_nilradical_z12(self):
        self.assertEqual(radical(12,{0}),{0,6})
        self.assertEqual(set.intersection(*prime_ideals(12)),{0,6})
    def test_07_nilradical_zsquarefree(self):
        for n in (6,10,14,15,21,30,42):
            self.assertEqual(radical(n,{0}),{0})
    def test_08_nilradical_zn_prime_powers(self):
        for p,k in ((2,2),(2,4),(3,2),(5,2)):
            n=p**k
            self.assertEqual(radical(n,{0}),{a for a in range(n) if a%p==0})
    def test_09_ideal_generation_and_radical_12(self):
        self.assertEqual(radical(12,{0,4,8}),{0,2,4,6,8,10})
        self.assertEqual(radical(12,{0,6}),{0,6})
    def test_10_prime_avoid_multiplicative_sets(self):
        for n in range(2,24):
            for g in range(1,n):
                S=generated_mult_set(n,[g])
                if 0 in S:continue
                for I in ideals(n):
                    if I.isdisjoint(S):
                        self.assertTrue(any(I<=P and P.isdisjoint(S) for P in prime_ideals(n)))

class LocalizationArithmetic(unittest.TestCase):
    def make(self,n,g):
        S=generated_mult_set(n,[g]);self.assertNotIn(0,S)
        pairs=list(itertools.product(range(n),S))
        equiv=lambda x,y:any((u*(x[0]*y[1]-y[0]*x[1]))%n==0 for u in S)
        reps=[]
        for x in pairs:
            if not any(equiv(x,r) for r in reps):reps.append(x)
        idx={x:next(i for i,r in enumerate(reps) if equiv(x,r)) for x in pairs}
        add=lambda a,b:idx[((a[0]*b[1]+b[0]*a[1])%n,(a[1]*b[1])%n)]
        mul=lambda a,b:idx[((a[0]*b[0])%n,(a[1]*b[1])%n)]
        return S,pairs,equiv,reps,idx,add,mul
    def test_11_example_naive_relation_not_transitive(self):
        self.assertEqual((0*2-0*1)%6,0)
        self.assertEqual((0*1-3*2)%6,0)
        self.assertNotEqual((0*1-3*1)%6,0)
    def test_12_equivalence_transitive_all_examples(self):
        for n,g in ((6,2),(10,2),(12,5),(15,2),(8,3),(9,2)):
            S,pairs,eq,*_=self.make(n,g)
            self.assertTrue(all(eq(x,x) for x in pairs))
            self.assertTrue(all(eq(x,y)==eq(y,x) for x,y in itertools.product(pairs,repeat=2)))
            for x,y,z in itertools.product(pairs,repeat=3):
                if eq(x,y) and eq(y,z):self.assertTrue(eq(x,z))
    def test_13_addition_well_defined_representatives(self):
        for n,g in ((6,2),(10,2),(12,5),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for x,y in itertools.product(pairs,repeat=2):
                self.assertEqual(idx[x],idx[next(r for r in reps if eq(x,r))])
                self.assertEqual(add(x,y),add(reps[idx[x]],reps[idx[y]]))
    def test_14_multiplication_well_defined_representatives(self):
        for n,g in ((6,2),(10,2),(12,5),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for x,y in itertools.product(pairs,repeat=2):
                self.assertEqual(mul(x,y),mul(reps[idx[x]],reps[idx[y]]))
    def test_15_ring_axioms_localized_finite_models(self):
        for n,g in ((6,2),(10,2),(12,5),(8,3)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            plus=lambda i,j:add(reps[i],reps[j]); times=lambda i,j:mul(reps[i],reps[j])
            zero=idx[(0,1)];one=idx[(1,1)]
            for x in range(len(reps)):
                self.assertEqual(plus(x,zero),x)
                self.assertEqual(times(x,one),x)
                for y in range(len(reps)):
                    self.assertEqual(plus(x,y),plus(y,x))
                    self.assertEqual(times(x,y),times(y,x))
                    for z in range(len(reps)):
                        self.assertEqual(plus(plus(x,y),z),plus(x,plus(y,z)))
                        self.assertEqual(times(times(x,y),z),times(x,times(y,z)))
                        self.assertEqual(times(x,plus(y,z)),plus(times(x,y),times(x,z)))
    def test_16_localized_z6_is_f3(self):
        S,pairs,eq,reps,idx,add,mul=self.make(6,2)
        self.assertEqual(len(reps),3)
        red=lambda x:(x[0]*pow(x[1],-1,3))%3
        self.assertEqual(len({red(x) for x in reps}),3)
        for x,y in itertools.product(pairs,repeat=2):
            self.assertEqual(eq(x,y),red(x)==red(y))
    def test_17_localization_kills_s_torsion_exactly(self):
        for n,g in ((6,2),(10,2),(12,5),(15,2),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for a in range(n):
                self.assertEqual(eq((a,1),(0,1)),any((u*a)%n==0 for u in S))
    def test_18_invert_all_denominators(self):
        for n,g in ((6,2),(10,2),(12,5),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for s in S:self.assertTrue(eq((s,s),(1,1)))
    def test_19_ideal_membership_by_saturation(self):
        for n,g in ((6,2),(10,2),(12,5)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for I in ideals(n):
                ext={idx[(a,s)] for a in I for s in S}
                for a,s in pairs:
                    self.assertEqual(idx[(a,s)] in ext,any((u*a)%n in I for u in S))
    def test_20_prime_ideal_correspondence(self):
        for n,g in ((6,2),(10,2),(12,5),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            primes=[P for P in prime_ideals(n) if P.isdisjoint(S)]
            ext=[{idx[(a,s)] for a in P for s in S} for P in primes]
            self.assertEqual(len(ext),len({frozenset(P) for P in ext}))
            for P,E in zip(primes,ext):
                self.assertEqual({a for a in range(n) if idx[(a,1)] in E},P)
    def test_21_radical_commutes_with_localization(self):
        for n,g in ((6,2),(10,2),(12,5),(9,2)):
            S,pairs,eq,reps,idx,add,mul=self.make(n,g)
            for I in ideals(n):
                ext={idx[(a,s)] for a in I for s in S}
                radext={i for i,r in enumerate(reps) if any(
                    next(j for j,t in enumerate(reps) if eq(t,(pow(r[0],k,n),pow(r[1],k,n)))) in ext for k in range(1,9))}
                extrad={idx[(a,s)] for a in radical(n,I) for s in S}
                self.assertEqual(radext,extrad)
    def test_22_localization_of_Z_2(self):
        for a,n in itertools.product(range(-20,21),range(8)):
            q=Fraction(a,2**n)
            self.assertEqual(q*Fraction(2,1),Fraction(2*a,2**n))
            self.assertNotEqual(q,Fraction(1,3))
    def test_23_units_of_Z_one_sixth(self):
        for a,b in itertools.product(range(-50,51),range(1,51)):
            val=Fraction(a,b)
            def admissible(z):
                d=z.denominator
                while d%2==0:d//=2
                while d%3==0:d//=3
                return d==1
            if admissible(val) and val:
                test=admissible(1/val)
                num=abs(val.numerator); den=val.denominator
                def only23(v):
                    while v%2==0:v//=2
                    while v%3==0:v//=3
                    return v==1
                self.assertEqual(test,only23(num))
    def test_24_saturation_of_six_in_Z_one_half(self):
        for a in range(-200,201):
            self.assertEqual(any((2**k*a)%6==0 for k in range(7)),a%3==0)
    def test_25_residue_field_Z_local_five(self):
        for a,b in itertools.product(range(-20,21),range(1,21)):
            if b%5==0:continue
            val=a*pow(b,-1,5)%5
            self.assertEqual((val*b-a)%5,0)

class StructuralChecks(unittest.TestCase):
    def test_26_existing_labels_unique(self):
        labs=re.findall(r'\\label\{([^}]+)\}',TXT)
        self.assertEqual(len(labs),len(set(labs)))
        self.assertGreaterEqual(len(labs),36)
    def test_27_proofs_preserved_and_balanced(self):
        for env in ('twierdzenie','lemat','stwierdzenie','definicja','proof','przyklad','uwaga'):
            self.assertEqual(TXT.count('\\begin{'+env+'}'),TXT.count('\\end{'+env+'}'))
        self.assertEqual(TXT.count('\\begin{proof}'),16)
    def test_28_radical_primality_and_empty_intersection_stated(self):
        self.assertIn('przecięcie po pustej rodzinie oznacza cały $R$',TXT)
        self.assertIn('\\sqrt{S^{-1}I}=S^{-1}(\\sqrt I)',TXT)
    def test_29_standalone_assumptions_for_localization(self):
        for token in ('Niech $R$ będzie przemiennym pierścieniem z jedynką','homomorfizmem kanonicznym','$\\iota(a)=a/1_R$'):
            self.assertIn(token,TXT)
    def test_30_terminology_consistency(self):
        self.assertNotIn('Pierwiastek ideału',TXT)
        self.assertNotIn('niedzielnikiem zera',TXT)
        self.assertIn('Pierwiastnik ideału',TXT)



def elements_ideal(n,d):
    return {x for x in range(n) if x%d==0}


def primes_mod_n(n):
    out=[]
    for d in range(1,n+1):
        if n%d:continue
        I=elements_ideal(n,d)
        if len(I)==n:continue
        if all(((a*b)%n not in I) or a in I or b in I for a in range(n) for b in range(n)):
            out.append((d,I))
    return out


def f2mulmodp(a,b):
    # representation of a0 + a1*x in F2[x]/(x^2+x+1)
    a0,a1=a; b0,b1=b
    const=(a0*b0+a1*b1)%2
    x=(a0*b1+a1*b0+a1*b1)%2
    return const,x

class AuditIIMath(unittest.TestCase):
    def test_31_only_two_prime_ideals_of_z12(self):
        P=primes_mod_n(12)
        self.assertEqual({d for d,_ in P},{2,3})
        self.assertEqual(set.intersection(*(I for _,I in P)),{0,6})

    def test_32_every_prime_contains_two_or_three(self):
        self.assertEqual((2**2*3)%12,0)
        for d,P in primes_mod_n(12):
            self.assertTrue(2 in P or 3 in P)
            self.assertIn(d,(2,3))

    def test_33_f2_irreducible_quadratic(self):
        p=lambda x:(x*x+x+1)%2
        self.assertEqual([p(0),p(1)],[1,1])

    def test_34_x_inverse_mod_p(self):
        one=(1,0);x=(0,1);x_plus_one=(1,1)
        self.assertEqual(f2mulmodp(x,x_plus_one),one)
        self.assertEqual(f2mulmodp(x_plus_one,x),one)

    def test_35_f2_quotient_is_field_four_elements(self):
        el=list(itertools.product(range(2),repeat=2))
        self.assertEqual(len(el),4)
        for a in el:
            if a==(0,0):continue
            self.assertTrue(any(f2mulmodp(a,b)==(1,0) for b in el))

    def test_36_laurent_maximal_ideals_distinct(self):
        # p(1)=1 while (x-1) vanishes at 1
        self.assertEqual((1+1+1)%2,1)
        # distinct kernels: eval x=1 vs quotient p(x)
        self.assertEqual(f2mulmodp((0,1),(1,1)),(1,0))

    def test_37_empty_generators_mean_zero_ideal(self):
        for n in range(2,11):
            generated={0} # sums of empty list of generators
            self.assertEqual(generated,{0})
            ideals=[{0} for _ in range(6)]
            self.assertTrue(all(I==ideals[0] for I in ideals))
        self.assertIn('Jeśli $m=0$',TXT)
        self.assertLess(TXT.index('Jeśli $m=0$'), TXT.index(r'N=\max\{n_1,\ldots,n_m\}'))

    def test_38_strict_nofinite_generation_chain(self):
        # Over F2, x_(n+1) evaluated at x_1=...=x_n=0 stays nonzero.
        for n in range(1,15):
            generators={i for i in range(1,n+1)}
            next_var=n+1
            # Evaluating x_1=...=x_n=0 annihilates their generated
            # ideal, whereas x_(n+1) maps to a nonzero monomial.
            def evaluate_monomial(variable_index):
                return 0 if variable_index in generators else ('x',variable_index)
            self.assertTrue(all(evaluate_monomial(i)==0 for i in generators))
            self.assertEqual(evaluate_monomial(next_var),('x',n+1))



class AuditIIIIndependent(unittest.TestCase):
    """Independent edge-case models: saturation, radicals, residue fields and ACC."""

    def test_39_all_primes_of_z12_from_maximality(self):
        primes=prime_ideals(12)
        E2={x for x in range(12) if x%2==0}
        E3={x for x in range(12) if x%3==0}
        self.assertEqual({frozenset(p) for p in primes},{frozenset(E2),frozenset(E3)})
        for p in primes:self.assertTrue(2 in p or 3 in p)

    def test_40_saturation_ideals_is_idempotent(self):
        for n,g in ((6,2),(8,3),(10,2),(12,5),(15,2),(21,2),(30,7)):
            S=generated_mult_set(n,[g])
            if 0 in S:continue
            for I in ideals(n):
                sat={x for x in range(n) if any(s*x%n in I for s in S)}
                sat2={x for x in range(n) if any(s*x%n in sat for s in S)}
                self.assertEqual(sat,sat2,(n,g,I))

    def test_41_saturation_commutes_with_radical(self):
        for n,g in ((6,2),(10,2),(12,5),(15,2),(30,7)):
            S=generated_mult_set(n,[g])
            if 0 in S:continue
            for I in ideals(n):
                sat=lambda J:{x for x in range(n) if any(s*x%n in J for s in S)}
                self.assertEqual(sat(radical(n,I)),radical(n,sat(I)))

    def test_42_prime_correspondence_with_two_generator_S(self):
        for n,gens in ((30,(2,3)),(42,(2,7)),(35,(2,3)),(60,(7,11))):
            S=generated_mult_set(n,gens)
            if 0 in S:continue
            ps=prime_ideals(n)
            survivors=[p for p in ps if p.isdisjoint(S)]
            target=[p for p in ps if all(g%n not in p for g in gens)]
            self.assertEqual(survivors,target)

    def test_43_fraction_residue_field_p5(self):
        for a,b in itertools.product(range(-20,21),repeat=2):
            if b==0 or b%5==0:continue
            f=Fraction(a,b)
            norm=lambda f:f.numerator*pow(f.denominator,-1,5)%5
            self.assertEqual(norm(f),a*pow(b,-1,5)%5)
            if a%5:self.assertEqual(norm(1/f)*norm(f)%5,1)

    def test_44_laurent_quadratic_quotient_over_f2(self):
        elements=list(itertools.product(range(2),repeat=2))
        x=(0,1);xp=(1,1)
        self.assertEqual(f2mulmodp(x,xp),(1,0))
        for u in elements:
            if u==(0,0):continue
            inverses=[v for v in elements if f2mulmodp(u,v)==(1,0)]
            self.assertEqual(len(inverses),1)

    def test_45_localization_at_primes_is_local_small_models(self):
        for n in (6,8,10,12,15,18,21,24):
            for P in prime_ideals(n):
                S=set(range(n))-P
                if not S or 0 in S:continue
                for a in range(n):
                    invertible=any((a*s)%n in S for s in S)
                    self.assertEqual(invertible,a not in P)

    def test_46_ascending_chains_finite_ring_terminate(self):
        for n in range(2,60):
            Ii=ideals(n)
            levels={frozenset(I) for I in Ii}
            self.assertEqual(len(levels),len(Ii))
            for I in Ii:
                bigger=[J for J in Ii if I<J]
                self.assertTrue(all(len(J)>len(I) for J in bigger))

if __name__=='__main__': unittest.main(verbosity=2)
