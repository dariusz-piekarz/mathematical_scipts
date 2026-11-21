"""Chapter 18 regression tests: arithmetization, finite traces, diagonal notation.

Finite computations supplement but never replace formal mathematical proofs.
"""
import math
import re
import unittest
from itertools import product
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SOURCE = (ROOT/'chapters/pl/logic_and_set_theory/18-reprezentowalnosc-i-diagonalizacja.tex').read_text(encoding='utf8')
PREV = ''.join((ROOT/'chapters/pl/logic_and_set_theory'/n).read_text(encoding='utf8') for n in (
 '16-algorytmy-obliczalnosc-i-nierozstrzygalnosc.tex',
 '17-arytmetyka-formalna-i-kodowanie-skladni.tex'))
S=SOURCE
P=PREV

def beta(a, b, i):
    return a % (1 + (i + 1) * b)


def crt_audit2(remainders, moduli):
    p = math.prod(moduli)
    ans = sum(c * (p // m) * pow(p // m, -1, m)
              for c, m in zip(remainders, moduli) if m > 1) % p
    return ans


def pack(u, v):
    return (u + v) ** 2 + u


def encode_audit2(xs):
    s = len(xs) - 1
    b = math.factorial(s + 1) * (1 + max(xs))
    mods = [1 + (i + 1) * b for i in range(len(xs))]
    return crt_audit2(xs, mods), b


class TestLogic18AuditIIOnIII(unittest.TestCase):
    def test_crt_many_coprime_moduli(self):
        count = 0
        for mods in ((3, 5), (3, 4, 5), (5, 7, 8), (7, 9, 10)):
            for rems in product(*(range(min(3, m)) for m in mods)):
                ans = crt_audit2(rems, mods)
                self.assertTrue(all(ans % m == c for c, m in zip(rems, mods)))
                self.assertLess(ans, math.prod(mods))
                count += 1
        self.assertGreater(count, 80)

    def test_beta_traces(self):
        count = 0
        for n in (1, 2, 3, 4):
            for xs in product(range(3), repeat=n):
                a, b = encode_audit2(xs)
                self.assertEqual(tuple(beta(a, b, i) for i in range(n)), xs)
                count += 1
        self.assertEqual(count, 120)

    def test_beta_b_bound_and_uniqueness(self):
        for a in range(18):
            for m in range(1, 8):
                answers = [(q, v) for q in range(a + 1) for v in range(m)
                           if a == q * m + v]
                self.assertEqual(len(answers), 1, (a, m))
                self.assertEqual(answers[0][1], a % m)

    def test_three_case_trace_semantics(self):
        # Deterministic program: on state 0 increment r_0; state 1 halt.
        # A valid standard trace has first halting time 1.
        def is_transition(u, v):
            return u[0] == 0 and v == (1, u[1] + 1)

        def halts(u):
            return u[0] == 1

        def c_trace(xs, t, y):
            if len(xs) != t + 1 or xs[0] != (0, 2):
                return False
            if any(halts(xs[i]) or not is_transition(xs[i], xs[i + 1])
                   for i in range(t)):
                return False
            return halts(xs[t]) and xs[t][1] == y

        self.assertTrue(c_trace([(0, 2), (1, 3)], 1, 3))
        self.assertFalse(c_trace([(0, 2)], 0, 2))
        self.assertFalse(c_trace([(0, 2), (1, 3), (1, 3)], 2, 3))
        self.assertFalse(c_trace([(0, 2), (1, 3)], 1, 4))
        # β encodes the state and register rows independently.
        state_code = encode_audit2([0, 1])
        register_code = encode_audit2([2, 3])
        self.assertEqual(tuple(beta(*state_code, i) for i in (0, 1)), (0, 1))
        self.assertEqual(tuple(beta(*register_code, i) for i in (0, 1)), (2, 3))

    def test_D_t_on_standard_times(self):
        D = lambda t: all(j < t for u in range(t + 1) for j in range(u))
        self.assertTrue(all(D(t) for t in range(80)))

    def test_packing_component_bounds(self):
        seen = set()
        for a, b in product(range(50), repeat=2):
            p = pack(a, b)
            self.assertNotIn(p, seen)
            seen.add(p)
            self.assertGreaterEqual(p, max(a, b))

    def test_proof_three_cases_and_numerals(self):
        self.assertIn(r't<\overline s', SOURCE)
        self.assertIn(r't=\overline s', SOURCE)
        self.assertIn(r'\overline s<t', SOURCE)
        self.assertIn(r'B_j(\overline{u^{(j)}})', SOURCE)
        self.assertIn(r'\neg H_e(\overline{u^{(s)}})', SOURCE)
        self.assertIn(r'\forall y\,(\varphi_f(\overline{\vec n},y)\leftrightarrow y=\overline m)', SOURCE)

    def test_proof_predicate_bounded_and_code_distinction(self):
        self.assertIn(r'\operatorname{Pack}(p;d,t,\vec a,\vec b)', SOURCE)
        self.assertIn('ustalonych długościach krotek', SOURCE)
        self.assertIn(r'\operatorname{Prf}_T(p,x)', SOURCE)
        self.assertIn('formula $\\Delta_0$', SOURCE.replace('formuła', 'formula'))
        self.assertIn(r'Q\vdash G\leftrightarrow\psi(\overline g)', SOURCE)
        self.assertNotIn(r'\psi(\ulcorner G\urcorner)', SOURCE)

    def test_no_unjustified_new_environments_and_refs(self):
        counts = {'twierdzenie': 2, 'lemat': 5, 'proof': 7,
                  'definicja': 3, 'przyklad': 4, 'uwaga': 3}
        for env, n in counts.items():
            self.assertEqual(SOURCE.count(r'\begin{' + env + '}'), n, env)
        stack = []
        for kind, env in re.findall(r'\\(begin|end)\{([^}]+)\}', SOURCE):
            if kind == 'begin':
                stack.append(env)
            else:
                self.assertEqual(stack.pop(), env)
        self.assertFalse(stack)
        own_labels = re.findall(r'\\label\{([^}]+)\}', SOURCE)
        self.assertEqual(len(own_labels), 13)
        self.assertEqual(len(set(own_labels)), 13)
        all_labels = set(own_labels) | set(re.findall(r'\\label\{([^}]+)\}', PREV))
        refs = re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}', SOURCE)
        self.assertEqual(len(refs), 29)
        self.assertEqual(set(refs) - all_labels, set())



def beta(a,b,i): return a%(1+(i+1)*b)
def pair(a,b): return (a+b)*(a+b)+a

def crt(vals):
    s=len(vals)-1
    b=math.factorial(s+1)*(max(vals)+1)
    mods=[1+(i+1)*b for i in range(len(vals))]
    M=math.prod(mods)
    # Algorithmic bounded minimization, not a recipe for practical large instances.
    A=sum(c * (M//m) * (pow(M//m, -1, m) if m>1 else 0)
          for c,m in zip(vals,mods))%M
    return A,b,mods

class TestLogic18AuditIII(unittest.TestCase):
    def test_beta_CRT_many_values(self):
        count=0
        for length in range(1,5):
            for vals in product(range(4),repeat=length):
                a,b,mods=crt(vals)
                self.assertEqual(tuple(beta(a,b,i) for i in range(length)),vals)
                self.assertTrue(all(math.gcd(x,y)==1 for i,x in enumerate(mods) for y in mods[i+1:]))
                self.assertTrue(all(c<m for c,m in zip(vals,mods)))
                count+=1
        self.assertEqual(count,340)
    def test_beta_bound_uniqueness_including_zero_code(self):
        for a in range(65):
            for b in range(5):
                for i in range(4):
                    m=1+(i+1)*b
                    W=[(q,r) for q in range(a+1) for r in range(m) if a==q*m+r]
                    self.assertEqual(len(W),1)
                    self.assertEqual(W[0][1],beta(a,b,i))
    def test_successor_time_order(self):
        for t in range(61):
            for j in range(61):
                self.assertEqual(not (j<t) or (j+1<=t),True)
                if j<t:
                    witnesses=[z for z in range(t+1) if z+(j+1)==t]
                    self.assertEqual(len(witnesses),1)
                    z=witnesses[0]
                    self.assertEqual(t,j+1 if z==0 else (j+2)+(z-1))
    def test_program_traces_with_first_halt(self):
        # inc(register), halt, and a machine that starts in Halt.
        def accept(initial,trace,t,y):
            if not trace or trace[0]!=initial or len(trace)!=t+1:return False
            for before,after in zip(trace,trace[1:]):
                if before[0]!=0 or after!=(1,before[1]+1): return False
            return trace[-1][0]==1 and trace[-1][1]==y
        self.assertTrue(accept((0,2),[(0,2),(1,3)],1,3))
        self.assertFalse(accept((0,2),[(0,2)],0,2))
        self.assertFalse(accept((0,2),[(0,2),(1,3),(1,3)],2,3))
        self.assertFalse(accept((0,2),[(0,2),(1,3)],1,4))
        self.assertTrue(accept((1,2),[(1,2)],0,2))
    def test_pack_injective_and_bounded(self):
        seen=set()
        for a,b in product(range(35),repeat=2):
            p=pair(a,b)
            self.assertNotIn(p,seen)
            seen.add(p)
            self.assertGreaterEqual(p,max(a,b))
            self.assertGreaterEqual(pair(p,a),max(p,a))
    def test_numerals_and_Q_case_proof(self):
        self.assertIn(r'C_{V_T}(d,x,\overline1,t,\vec a,\vec b)',S)
        self.assertNotIn(r'C_{V_T}(d,x,1,t,\vec a,\vec b)',S)
        self.assertIn(r'(\overline j<t)\to(\overline{j+1}\le t)',S)
        self.assertIn('z (Q8) otrzymujemy',S)
        self.assertIn('a (Q3)',S)
        self.assertIn(r'$t=\overline{j+1}$',S)
        self.assertIn(r'$\overline{j+1}<t$',S)
        self.assertIn(r'U(\vec a,\vec b,t)',S)
        self.assertIn(r'D(t)',S)
    def test_diagonal_substitution_is_numeral(self):
        self.assertIn(r'Q\vdash G\leftrightarrow\psi(\overline g)',S)
        self.assertIn(r'\varphi_d(\overline m,y)',S)
        self.assertNotIn(r'\psi(\ulcorner G\urcorner)',S)
    def test_environments_labels_refs(self):
        expected={'twierdzenie':2,'lemat':5,'proof':7,'definicja':3,'przyklad':4,'uwaga':3}
        for env,c in expected.items():
            self.assertEqual(S.count('\\begin{'+env+'}'),c)
        labels=re.findall(r'\\label\{([^}]+)\}',S)
        self.assertEqual(len(labels),13)
        self.assertEqual(len(set(labels)),13)
        refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',S)
        self.assertEqual(len(refs),29)
        self.assertFalse(set(refs)-set(labels)-set(re.findall(r'\\label\{([^}]+)\}',P)))
        stack=[]
        for x,env in re.findall(r'\\(begin|end)\{([^}]+)\}',S):
            if x=='begin':stack.append(env)
            else:self.assertEqual(stack.pop(),env)
        self.assertFalse(stack)


if __name__=='__main__': unittest.main()