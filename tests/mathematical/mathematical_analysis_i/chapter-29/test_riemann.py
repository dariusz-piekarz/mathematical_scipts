from fractions import Fraction as F
from pathlib import Path
import unittest


def sums(p, extrema):
    intervals=zip(p,p[1:])
    lower=upper=F(0)
    for a,b in intervals:
        m,M=extrema(a,b)
        lower+=m*(b-a)
        upper+=M*(b-a)
    return lower,upper


def mesh(p):
    return max(b-a for a,b in zip(p,p[1:]))


def square_extrema(a,b):
    return min(a*a,b*b) if a*b>0 else F(0),max(a*a,b*b)


class Chapter29(unittest.TestCase):
    def test_refinement_and_common_refinement(self):
        p=list(map(F,(-2,-1,1,3)))
        r=list(map(F,(-2,0,2,3)))
        q=sorted(set(p+r))
        lp,up=sums(p,square_extrema)
        lr,ur=sums(r,square_extrema)
        lq,uq=sums(q,square_extrema)
        self.assertTrue(lp<=lq<=uq<=up)
        self.assertTrue(lr<=lq<=uq<=ur)
        self.assertLessEqual(lp,ur)
        self.assertLessEqual(lr,up)

    def test_square_darboux_sums(self):
        for n in (1,2,4,8,17):
            p=[F(i,n) for i in range(n+1)]
            l,u=sums(p,square_extrema)
            self.assertEqual(u-l,F(1,n))
            self.assertLessEqual(l,F(1,3))
            self.assertLessEqual(F(1,3),u)
            self.assertEqual(u,F(n*(n+1)*(2*n+1),6*n**3))

    def test_bad_intervals_refinement_bound(self):
        p0=[F(0),F(1,3),F(2,3),F(1)]
        k=len(p0)-2
        for n in (1,2,3,4,5,8,13):
            p=[F(i,n) for i in range(n+1)]
            q=sorted(set(p+p0))
            bad=[(a,b) for a,b in zip(p,p[1:])
                 if any(a<t<b for t in p0[1:-1])]
            self.assertLessEqual(len(bad),k)
            self.assertLessEqual(sum(b-a for a,b in bad),k*mesh(p))
            l,u=sums(p,square_extrema)
            lq,uq=sums(q,square_extrema)
            self.assertTrue(0<=u-uq<=2*k*mesh(p))
            self.assertTrue(0<=lq-l<=2*k*mesh(p))

    def test_nonattained_extrema_and_approximate_tags(self):
        def f(x):
            return x if 0<x<1 else F(1,2)
        for n in (2,4,8,32):
            p=[F(i,n) for i in range(n+1)]
            def extrema(a,b):
                # At outer endpoints the changed value 1/2 may enlarge the range.
                return (min(a,F(1,2)) if b==1 else a,
                        max(b,F(1,2)) if a==0 else b)
            l,u=sums(p,extrema)
            eta=F(1,10*n)
            # Interior tags can approach the unattained extrema of the full interval.
            self.assertEqual(sums([F(0),F(1)],extrema),(F(0),F(1)))
            self.assertEqual(f(eta),eta)
            self.assertTrue(1-2*eta<f(1-eta)<1)
            self.assertLessEqual(l,F(1,2))
            self.assertLessEqual(F(1,2),u)
        self.assertEqual(f(F(0)),F(1,2))
        self.assertEqual(f(F(1)),F(1,2))

    def test_isolating_discontinuities_including_endpoints(self):
        a,b=F(0),F(1)
        points=[a,F(1,3),F(2,3),b]
        B,eps=F(3),F(1,10)
        rho=eps/(16*B*len(points))
        intervals=[(max(a,d-rho),min(b,d+rho)) for d in points]
        self.assertTrue(all(u<v for u,v in intervals))
        self.assertTrue(all(v<w for (_,v),(w,_) in zip(intervals,intervals[1:])))
        total=sum(v-u for u,v in intervals)
        self.assertLess(2*B*total,eps/2)
        self.assertEqual(intervals[0][0],a)
        self.assertEqual(intervals[-1][1],b)
        for (u,v),(w,z) in zip(intervals,intervals[1:]):
            self.assertTrue(all(not v<=d<=w for d in points))

    def test_tagged_sums_squeezed(self):
        p=[F(0),F(1,7),F(1,2),F(1)]
        l,u=sums(p,square_extrema)
        for t in (F(0),F(1,3),F(1,2),F(1)):
            s=sum(((1-t)*a+t*b)**2*(b-a) for a,b in zip(p,p[1:]))
            self.assertTrue(l<=s<=u)

    def test_monotone_telescope(self):
        p=[F(-2),F(-1,2),F(1,3),F(2)]
        for sign in (1,-1):
            f=lambda x:sign*x**3
            ex=lambda a,b:(min(f(a),f(b)),max(f(a),f(b)))
            l,u=sums(p,ex)
            self.assertLessEqual(u-l,mesh(p)*abs(f(p[-1])-f(p[0])))

    def test_finite_discontinuities_step(self):
        c=F(1,2)
        ex=lambda a,b:(int(a>=c),int(b>=c))
        for n in (4,8,16,32):
            p=[F(i,n) for i in range(n+1)]
            l,u=sums(p,ex)
            self.assertEqual(l,F(1,2))
            self.assertEqual(u-l,F(1,n))
            self.assertTrue(l<=F(1,2)<=u)

    def test_dirichlet_extrema(self):
        # Every nontrivial interval has both rational and irrational points.
        for n in (1,3,9,17):
            p=[F(i,n) for i in range(n+1)]
            self.assertEqual(sums(p,lambda a,b:(F(0),F(1))),(F(0),F(1)))

    def test_linearity_of_tagged_sums(self):
        p=[F(-1),F(0),F(1,3),F(2)]
        tags=[(a+b)/2 for a,b in zip(p,p[1:])]
        s=lambda f:sum(f(t)*(b-a) for a,b,t in zip(p,p[1:],tags))
        for alpha,beta in ((F(0),F(0)),(F(3),F(-2)),(F(-1),F(0))):
            self.assertEqual(s(lambda x:alpha*x+beta*x*x),
                             alpha*s(lambda x:x)+beta*s(lambda x:x*x))

    def test_product_and_absolute_oscillation_bounds(self):
        grid=[F(i,8) for i in range(-8,9)]
        for i in range(len(grid)-1):
            pts=grid[i:]
            f=[x for x in pts]
            g=[x*x for x in pts]
            osc=lambda v:max(v)-min(v)
            self.assertLessEqual(osc([a*b for a,b in zip(f,g)]),osc(f)+osc(g))
            self.assertLessEqual(osc([abs(a) for a in f]),osc(f))

    def test_finite_changes_at_partition_endpoints(self):
        for n in (2,4,8,16):
            p=[F(i,n) for i in range(n+1)]
            changed={F(0),F(1,2),F(1)}
            bad=[(a,b) for a,b in zip(p,p[1:]) if any(a<=t<=b for t in changed)]
            self.assertLessEqual(len(bad),2*len(changed))
            for t in (F(0),F(1),F(1,2)):
                s=sum((b-a)*int((1-t)*a+t*b in changed) for a,b in zip(p,p[1:]))
                self.assertLessEqual(s,2*len(changed)*mesh(p))

    def test_oriented_additivity_and_order(self):
        primitive=lambda x:x**3/3
        integ=lambda a,b:primitive(b)-primitive(a)
        from itertools import permutations
        for a,b,c in permutations(map(F,(-2,0,3))):
            self.assertEqual(integ(a,b)+integ(b,c),integ(a,c))
            self.assertEqual(integ(a,b),-integ(b,a))
        self.assertEqual(integ(F(2),F(2)),0)

    def test_weighted_mean_value(self):
        # f(x)=x, g(x)=x on [0,1]: xi=(1/3)/(1/2)=2/3.
        a,b=F(1,3),F(1,2)
        xi=a/b
        self.assertTrue(0<=xi<=1)
        self.assertEqual(xi*b,a)
        self.assertEqual(F(0)*xi,0)

    def test_fundamental_difference_quotient(self):
        for x in (F(-2),F(0),F(1,3),F(1)):
            for h in (F(-1,10),F(1,10),F(1,100)):
                q=((x+h)**3-x**3)/(3*h)
                self.assertEqual(q-x*x,x*h+h*h/3)
                self.assertLessEqual(abs(q-x*x),abs(x*h)+h*h/3)

    def test_newton_leibniz_telescoping(self):
        p=list(map(F,(-2,-1,0,1,3)))
        G=lambda x:x*x
        tags=[(a+b)/2 for a,b in zip(p,p[1:])]
        s=sum(2*t*(b-a) for a,b,t in zip(p,p[1:],tags))
        self.assertEqual(s,G(p[-1])-G(p[0]))

    def test_thomae_labels_preserve_original_and_distinguish_riemann_example(self):
        root = Path(__file__).resolve().parents[4]
        chapters = root / "chapters/pl/mathematical_analysis_i"
        original = r"\label{ma1:ex:thomae}"
        riemann = r"\label{ma1:ex:thomae-riemann}"
        owners = {original: [], riemann: []}
        for path in sorted(chapters.glob("*.tex")):
            source = path.read_text(encoding="utf8")
            for label in owners:
                owners[label].extend([path.name] * source.count(label))
        self.assertEqual(owners[original], ["19-funkcje-patologiczne.tex"])
        self.assertEqual(owners[riemann], ["29-calka-riemanna.tex"])
        source = (chapters / owners[riemann][0]).read_text(encoding="utf8")
        self.assertIn(r"\ref{ma1:ex:thomae-riemann}", source)

    def test_figure_source(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/29-calka-riemanna.tex").read_text(encoding="utf8")
        for token in (r"plot (\x,{\x*\x})",r"\foreach \i in {0,1,2,3}",
                      r"\fill[blue!18]",r"\fill[orange!30]"):
            self.assertIn(token,s)
        p=[F(i,4) for i in range(5)]
        self.assertEqual(sums(p,square_extrema),(F(7,32),F(15,32)))


if __name__=="__main__":
    unittest.main()
