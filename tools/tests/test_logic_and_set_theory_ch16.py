"""Chapter 16 regression checks: finite falsification / source checks, not proofs."""
from itertools import product
from pathlib import Path
import os
import re
import unittest

SOURCE = Path(os.environ.get('LOGIC16_SOURCE', str(Path(__file__).resolve().parents[2] / 'chapters/pl/logic_and_set_theory/16-algorytmy-obliczalnosc-i-nierozstrzygalnosc.tex')))

def pair_encode(u, v):
    return '0' * len(u) + '1' + u + v

def pair_decode(s):
    if not set(s) <= {'0', '1'}:
        return None
    i = s.find('1')
    if i < 0 or len(s) < 2 * i + 1:
        return None
    return s[i+1:i+1+i], s[i+1+i:]

def encode_word(digits, base):
    return sum(v * base ** i for i, v in enumerate(digits))

class Chapter16Tests(unittest.TestCase):
    def test_pair_encoding_injective(self):
        words = [''.join(x) for n in range(5) for x in product('01', repeat=n)]
        codes = [pair_encode(u, v) for u in words for v in words]
        self.assertEqual(len(codes), len(set(codes)))
        for u, v in product(words, repeat=2):
            self.assertEqual(pair_decode(pair_encode(u, v)), (u, v))

    def test_pair_decoder_rejects_bad_prefixes(self):
        for n in range(10):
            for symbols in product('01', repeat=n):
                s = ''.join(symbols)
                dec = pair_decode(s)
                if dec is not None:
                    self.assertEqual(pair_encode(*dec), s)
        self.assertIsNone(pair_decode('00000'))
        self.assertIsNone(pair_decode('0011'))

    def test_head_move_right_arithmetic(self):
        cases = 0
        for base in (2, 3, 4):
            for left_len in range(3):
                for right_len in range(3):
                    for left in product(range(base), repeat=left_len):
                        for right in product(range(base), repeat=right_len):
                            for symbol in range(base):
                                L, R = encode_word(left, base), encode_word(right, base)
                                L2 = symbol + base*L
                                R2 = R // base if right_len else 0
                                symbol2 = R % base if right_len else 0
                                self.assertEqual(L2, encode_word((symbol,) + left, base))
                                self.assertEqual(R2, encode_word(right[1:] if right_len else (), base))
                                self.assertEqual(symbol2, right[0] if right_len else 0)
                                cases += 1
        self.assertGreater(cases, 900)

    def test_head_move_left_symmetry(self):
        for base in (2, 3):
            for length in range(4):
                for left in product(range(base), repeat=length):
                    L = encode_word(left, base)
                    for current in range(base):
                        self.assertEqual(current + base*L, encode_word((current,)+left, base))
                        if length:
                            self.assertEqual((L % base, L//base), (left[0], encode_word(left[1:], base)))

    def test_dovetailing_one_recognizer_accepts(self):
        # One of two semideciders must accept for a fixed input; simulated finite traces.
        for accept_at in (0,1,2,5,10):
            for owner in (0,1):
                accepted = None
                for step in range(accept_at+2):
                    if step == accept_at:
                        accepted = owner
                        break
                self.assertEqual(accepted, owner)

    def test_diagonal_reversal(self):
        # If D predicts halt, constructed K loops; otherwise K halts.
        for predicts_halt in (False, True):
            k_halts = not predicts_halt
            self.assertNotEqual(k_halts, predicts_halt)

    def test_source_hypotheses_and_inventories(self):
        t = SOURCE.read_text(encoding='utf-8')
        self.assertIn(r'q_0\notin\{q_{\mathrm{tak}},q_{\mathrm{nie}}\}', t)
        self.assertIn(r'\operatorname{code}(k,k)', t)
        self.assertIn('szczególną klasą funkcji', t)
        self.assertNotIn('Nie jest to inny rodzaj obliczalności', t)
        self.assertIn(r'\label{fig:computability-diagonal}', t)
        expected = {'twierdzenie':5,'lemat':2,'wniosek':1,'proof':8,'definicja':5,'przyklad':6,'uwaga':4,'figure':1}
        for env, count in expected.items():
            self.assertEqual(t.count(r'\begin{'+env+'}'), count, env)
            self.assertEqual(t.count(r'\end{'+env+'}'), count, env)
        labels = re.findall(r'\\label\{([^}]+)\}', t)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(labels),13)


def encode(digits, base):
    return sum(d * (base ** i) for i,d in enumerate(digits))

def encoded_transition(L, left_len, a, R, right_len, written, motion, base):
    if motion == 'P':
        new_left = written + base * L
        if right_len:
            return new_left, left_len + 1, R % base, R // base, right_len - 1
        return new_left, left_len + 1, 0, 0, 0
    if motion == 'L':
        new_right = written + base * R
        if left_len:
            return L // base, left_len - 1, L % base, new_right, right_len + 1
        return 0, 0, 0, new_right, right_len + 1
    if motion == 'S':
        return L, left_len, written, R, right_len
    raise ValueError(motion)

def explicit_transition(left, a, right, written, motion):
    if motion == 'P':
        return (written, *left), right[0] if right else 0, right[1:]
    if motion == 'L':
        return left[1:], left[0] if left else 0, (written, *right)
    return left, written, right

class AuditII(unittest.TestCase):
    def test_two_sided_tape_after_writing_not_reading(self):
        count = 0
        for base in (2,3):
            words = [tuple(x) for length in range(3) for x in product(range(base), repeat=length)]
            for left in words:
                for right in words:
                    for read, written, motion in product(range(base), range(base), 'LPS'):
                        got = encoded_transition(encode(left,base),len(left),read,encode(right,base),len(right),written,motion,base)
                        a,b,c = explicit_transition(left,read,right,written,motion)
                        expect = encode(a,base),len(a),b,encode(c,base),len(c)
                        self.assertEqual(got,expect,(left,read,right,written,motion))
                        count += 1
        self.assertGreater(count,5000)
    def test_transitions_are_not_using_old_symbol_if_written_differs(self):
        base=3
        left=(1,2); right=(2,1)
        for motion in 'LP':
            got = encoded_transition(encode(left,base),len(left),0,encode(right,base),len(right),2,motion,base)
            bad = encoded_transition(encode(left,base),len(left),0,encode(right,base),len(right),0,motion,base)
            self.assertNotEqual(got,bad)
        txt=SOURCE.read_text()
        self.assertIn("L'=c+BL",txt)
        self.assertIn("R'=c+BR",txt)
        self.assertNotIn(r"L'=a+bL",txt)
    def test_binary_input_scope_and_invalid_proof_codes(self):
        txt=SOURCE.read_text()
        self.assertIn(r'w\in\{0,1\}^*',txt)
        self.assertIn('alfabecie wejściowym $\\{0,1\\}$',txt)
        self.assertIn('w przeciwnym razie go odrzucamy',txt)
    def test_source_inventory_and_links(self):
        txt=SOURCE.read_text()
        expected={'twierdzenie':5,'lemat':2,'wniosek':1,'proof':8,'definicja':5,'przyklad':6,'uwaga':4,'figure':1}
        for env,n in expected.items():
            self.assertEqual(txt.count(r'\begin{'+env+'}'),n)
            self.assertEqual(txt.count(r'\end{'+env+'}'),n)
        labels=re.findall(r'\\label\{([^}]+)\}',txt)
        self.assertEqual(len(labels),13)
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(len(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',txt)),9)

class AuditIII(unittest.TestCase):
    def test_explicit_effectivity_of_language(self):
        t=SOURCE.read_text(encoding='utf-8')
        for required in (
           'poprawność kodów symboli, ich rodzaje i arności',
           'poprawność można sprawdzać',
           'skończone słowa',
           'pozostałe kontrole wynikają z jawnych założeń',
           'niepustym podzbiorem symboli wejściowych',
           'Jeśli kod pary lub maszyny jest błędny'):
            self.assertIn(required,t)
        self.assertNotIn('Wypisujemy kolejno wszystkie skończone napisy\nmogące kodować drzewa',t)

    def test_signed_head_position_multistep(self):
        from itertools import product
        import random
        rng=random.Random(32016)
        checked=0
        for B in (2,3,5):
            for _ in range(350):
                left=tuple(rng.randrange(B) for i in range(rng.randrange(4)))
                right=tuple(rng.randrange(B) for i in range(rng.randrange(4)))
                a=rng.randrange(B);h=rng.randrange(-3,4)
                tape={h:a}
                for j,val in enumerate(left): tape[h-j-1]=val
                for j,val in enumerate(right): tape[h+j+1]=val
                L=encode(left,B);R=encode(right,B);ell=len(left);r=len(right)
                for _ in range(8):
                    written=rng.randrange(B);move=rng.choice('LPS')
                    tape[h]=written
                    h+=(1 if move=='P' else -1 if move=='L' else 0)
                    L,ell,a,R,r=encoded_transition(L,ell,a,R,r,written,move,B)
                    self.assertEqual(a,tape.get(h,0))
                    self.assertEqual(L,encode([tape.get(h-j-1,0) for j in range(ell)],B))
                    self.assertEqual(R,encode([tape.get(h+j+1,0) for j in range(r)],B))
                    checked+=1
        self.assertEqual(checked,8400)

if __name__ == '__main__':
    unittest.main()