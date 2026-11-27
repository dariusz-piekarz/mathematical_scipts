"""Finite regression witnesses for Daniell--Stone constructions with and without a unit."""
from fractions import Fraction as Q
import json
from pathlib import Path
import re
import unittest


class DaniellStone12(unittest.TestCase):
    def test_cover_residual(self):
        u=Q(1)
        h=[Q(1,2**k) for k in range(1,13)]
        residual=[max(u-sum(h[:n]),0) for n in range(1,13)]
        self.assertEqual(residual,[Q(1,2**n) for n in range(1,13)])
        self.assertTrue(all(a>b for a,b in zip(residual,residual[1:])))

    def test_lattice_cutoff_split(self):
        xs=[Q(-1),Q(0),Q(1,3),Q(1),Q(2)]
        h=[Q(2),Q(5),Q(1),Q(3),Q(7)]
        v=[min(1,max(x,0)) for x in xs]
        b=[min(y,7*z) for y,z in zip(h,v)]
        a=[y-z for y,z in zip(h,b)]
        self.assertTrue(all(x>=0 for x in a+b))
        self.assertEqual([x+y for x,y in zip(a,b)],h)
        self.assertEqual(b[:2],[0,0])
        self.assertEqual(a[-2:],[0,0])

    def test_level_ramp_telescoping(self):
        for x in (Q(-1),Q(0),Q(1,7),Q(2)):
            vals=[min(1,n*max(x,0)) for n in range(1,15)]
            diffs=[vals[0]]+[b-a for a,b in zip(vals,vals[1:])]
            self.assertTrue(all(d>=0 for d in diffs))
            self.assertEqual(sum(diffs),int(x>0))

    def test_threshold_bounds_and_exact_ramp_identity(self):
        d=Q(1,4)
        m=8
        for x in [Q(j,24) for j in range(49)]:
            lower=d*sum(x>k*d for k in range(1,m+1))
            upper=d*sum(x>k*d for k in range(m))
            ramps=d*sum(min(1,max(x-k*d,0)/d) for k in range(m))
            self.assertTrue(lower<=x<=upper)
            self.assertLessEqual(upper-lower,d)
            self.assertEqual(ramps,x)

    def test_weighted_representation_squeeze(self):
        xs=[Q(0),Q(1,3),Q(1),Q(5,3)]
        w=[Q(2),Q(1,2),Q(0),Q(4)]
        d=Q(1,5)
        m=10
        integral=lambda f:sum(a*b for a,b in zip(w,f))
        L=[d*sum(x>k*d for k in range(1,m+1)) for x in xs]
        U=[d*sum(x>k*d for k in range(m)) for x in xs]
        self.assertTrue(integral(L)<=integral(xs)<=integral(U))
        self.assertLessEqual(integral(U)-integral(L),d*sum(w))

    def test_dyadic_layers_gap(self):
        for k in range(12):
            self.assertGreater(Q(1,2**(k+1))-Q(1,2**(k+2)),0)

    def test_atomic_weights_no_mass_at_limit(self):
        for n in (1,3,10):
            weights={Q(1,k):Q(1,2**k) for k in range(1,n+1)}
            self.assertEqual(weights.get(Q(0),0),0)
            self.assertEqual(sum(weights.values()),1-Q(1,2**n))

    def test_boundary_evaluation_lacks_order_continuity(self):
        for t in (Q(1),Q(1,5),Q(1,10)):
            seq=[max(1-n*t,0) for n in range(1,15)]
            self.assertEqual(seq[-1],0)
            self.assertEqual(seq,sorted(seq,reverse=True))
        self.assertTrue(all(max(1-n*0,0)==1 for n in range(1,15)))


    def test_split_first_increment_without_unit(self):
        # The zero-level set may have infinite mass in the general proof.
        for delta in (Q(1,3), Q(1,7)):
            m=12
            for j in range(3*m+1):
                x=j*delta/3
                lower=delta*sum(x>k*delta for k in range(1,m+1))
                first=min(x,delta)
                rest=delta*sum(min(1,max(x-k*delta,0)/delta)
                               for k in range(1,m))
                self.assertEqual(first+rest,x)
                self.assertLessEqual(rest,lower)
                self.assertLessEqual(lower,x)

    def test_cover_truncation_l1_error(self):
        w=[Q(2),Q(3),Q(1),Q(4)]
        indicator=[Q(1),Q(0),Q(1),Q(0)]
        hs=[[Q(1,3),Q(1,100),Q(1,2),Q(0)],
            [Q(2,3),Q(0),Q(1,2),Q(1,200)]]
        integral=lambda f:sum(a*b for a,b in zip(w,f))
        total=[sum(row) for row in zip(*hs)]
        v=[min(1,x) for x in total]
        self.assertTrue(all(a<=b<=c for a,b,c in zip(indicator,v,total)))
        error=integral([abs(a-b) for a,b in zip(v,indicator)])
        budget=sum(integral(h) for h in hs)-integral(indicator)
        self.assertLessEqual(error,budget)
        partial=[min(1,x) for x in hs[0]]
        self.assertLessEqual(
            integral([abs(a-b) for a,b in zip(partial,indicator)]),
            integral([a-b for a,b in zip(v,partial)])+error)

    def test_positive_threshold_cover(self):
        h=[Q(0),Q(1,4),Q(2),Q(3)]
        w=[Q(3),Q(1),Q(5),Q(2)]
        ih=sum(a*b for a,b in zip(h,w))
        for t in (Q(1,4),Q(1),Q(2),Q(4)):
            mass=sum(a for a,x in zip(w,h) if x>t)
            self.assertLessEqual(t*mass,ih)



class DaniellStoneMigration(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[2]
    CANONICAL = "chapters/pl/measure_theory/32-calka-daniella-stone-a.tex"
    LEGACY = "12-calka-daniella-stone-a.tex"
    # Freeze the original labels independently of the retired CAL source.
    LEGACY_LABELS = {
        "it:def:daniell-lattice",
        "it:def:daniell-functional",
        "it:lem:daniell-monotone-extension",
        "it:lem:daniell-cover-domination",
        "it:def:daniell-outer",
        "it:eq:daniell-outer",
        "it:lem:daniell-outer",
        "it:lem:daniell-separated",
        "it:lem:daniell-measurability",
        "it:lem:daniell-level",
        "it:thm:daniell-stone",
        "it:cor:daniell-completion",
        "it:cor:daniell-necessity",
        "it:thm:daniell-l1-density",
        "it:cor:daniell-continuous-extension",
        "it:thm:daniell-unbounded-unit",
        "it:thm:daniell-stone-general",
        "it:cor:daniell-general-density",
        "it:ex:daniell-nonunique",
        "it:ex:daniell-without-stone",
        "it:ex:daniell-cc",
        "prz:daniel-koniecznosc",
        "prz:daniell-atoms",
    }

    def test_original_labels_survive_in_me32(self):
        source = (self.ROOT / self.CANONICAL).read_text(encoding="utf-8")
        labels = re.findall(r"\\label\{([^}]+)\}", source)
        self.assertTrue(self.LEGACY_LABELS <= set(labels),
                        self.LEGACY_LABELS - set(labels))
        self.assertEqual(len(labels), len(set(labels)))

    def test_me32_in_book_and_catalog(self):
        catalog = json.loads((self.ROOT / "catalog/books.json").read_text(
            encoding="utf-8"))
        book = next(b for b in catalog["books"] if b["id"] == "measure_theory")
        self.assertEqual(book["chapters"].count(self.CANONICAL), 1)
        entry = self.ROOT / book["entrypoint"]
        text = entry.read_text(encoding="utf-8")
        includes = re.findall(r"\\input\{([^}]+)\}", text)
        resolved = [(entry.parent / name).resolve() for name in includes]
        self.assertEqual(resolved.count((self.ROOT / self.CANONICAL).resolve()), 1)

    def test_remaining_cal_references_use_canonical_target(self):
        canonical = (self.ROOT / self.CANONICAL).read_text(encoding="utf-8")
        labels = set(re.findall(r"\\label\{([^}]+)\}", canonical))
        # The old book may disappear entirely after migration.
        for path in (self.ROOT / "chapters/pl/integration_theory").glob("*.tex"):
            if path.name == self.LEGACY:
                continue
            text = path.read_text(encoding="utf-8")
            local_refs = set(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", text))
            self.assertFalse(local_refs & self.LEGACY_LABELS, path.name)
            for target in re.findall(r"\\atlasref\{ME-32::([^}]+)\}", text):
                self.assertIn(target, labels, path.name)



if __name__=="__main__":
    unittest.main()
