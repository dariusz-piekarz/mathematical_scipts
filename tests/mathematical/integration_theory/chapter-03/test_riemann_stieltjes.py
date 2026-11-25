from fractions import Fraction as F
import unittest


def variation(values):
    return sum(abs(v-u) for u,v in zip(values,values[1:]))


class RiemannStieltjes03(unittest.TestCase):
    def test_summation_by_parts_arbitrary_bv_samples(self):
        f=list(map(F,[2,-1,4,3,-2]))
        a=list(map(F,[0,3,-2,5,1]))
        left=sum(u*(v2-v1) for u,v1,v2 in zip(f,a,a[1:]))
        right=sum(v*(u2-u1) for v,u1,u2 in zip(a[1:],f,f[1:]))
        self.assertEqual(left+right,f[-1]*a[-1]-f[0]*a[0])

    def test_refinement_bound(self):
        f=list(map(F,[0,3,-1,2,4,-2,1]))
        a=list(map(F,[1,-1,2,2,5,1,0]))
        coarse=[0,3,6]
        tags=[1,5]
        fine=sum(f[j]*(a[j+1]-a[j]) for j in range(6))
        initial=sum(f[t]*(a[v]-a[u]) for u,v,t in zip(coarse,coarse[1:],tags))
        bound=sum((max(f[u:v+1])-min(f[u:v+1]))*variation(a[u:v+1])
                  for u,v in zip(coarse,coarse[1:]))
        self.assertLessEqual(abs(initial-fine),bound)

    def test_disjoint_jumps(self):
        # Distinct jumps: f at 1/3, alpha at 2/3, so f=2 near
        # the alpha jump and alpha=0 near the f jump.
        for n in (6,12,24):
            x=[F(k,n) for k in range(n+1)]
            f=lambda t: F(2) if t>=F(1,3) else F(0)
            a=lambda t: F(3) if t>=F(2,3) else F(0)
            for side in (0,1):
                sf=sum(f((u,v)[side])*(a(v)-a(u)) for u,v in zip(x,x[1:]))
                sa=sum(a((u,v)[side])*(f(v)-f(u)) for u,v in zip(x,x[1:]))
                self.assertEqual(sf,6)
                self.assertEqual(sa,0)

    def test_gluing_failure_despite_local_integrability(self):
        c=F(1,2)
        f=lambda x:F(x>c)
        alpha=lambda x:F(x>=c)
        for n in (4,8,16):
            x=[F(k,n) for k in range(n+1)]
            # Both pieces are integrable: f=0 on the left,
            # alpha is constant on the right.
            self.assertEqual(sum(f(v)*(alpha(v)-alpha(u)) for u,v in zip(x,x[1:])),0)
            u,v=c-F(1,n),c+F(1,n)
            self.assertEqual(f(u)*(alpha(v)-alpha(u)),0)
            self.assertEqual(f(v)*(alpha(v)-alpha(u)),1)

    def test_cut_cell_error_identity(self):
        u,c,v=F(1,4),F(1,2),F(3,4)
        f=lambda x:x*x
        alpha=lambda x:3*x-x*x
        for t in (u,c,v):
            before=f(t)*(alpha(v)-alpha(u))
            after=f(c)*(alpha(c)-alpha(u))+f(c)*(alpha(v)-alpha(c))
            self.assertEqual(before-after,(f(t)-f(c))*(alpha(v)-alpha(u)))

    def test_shared_jump_requires_care(self):
        c=F(1,2)
        f=lambda x:F(x>=c)
        a=f
        for n in (4,8,16):
            x=[F(k,n) for k in range(n+1)]
            left=sum(f(u)*(a(v)-a(u)) for u,v in zip(x,x[1:]))
            right=sum(f(v)*(a(v)-a(u)) for u,v in zip(x,x[1:]))
            self.assertEqual((left,right),(0,1))


    def test_smooth_integrator_uniform_error(self):
        # alpha=x^2-x, derivative=2x-1; f need not be continuous.
        alpha=lambda x:x*x-x
        f=lambda x:F(1) if x<F(1,3) else F(-2)
        for n in (1,3,9,17,64):
            grid=[F(i,n) for i in range(n+1)]
            for tags in (grid[:-1],grid[1:],
                         [(u+v)/2 for u,v in zip(grid,grid[1:])]):
                rs=sum(f(t)*(alpha(v)-alpha(u))
                       for u,v,t in zip(grid,grid[1:],tags))
                ri=sum(f(t)*(2*t-1)*(v-u)
                       for u,v,t in zip(grid,grid[1:],tags))
                self.assertLessEqual(abs(rs-ri),F(4,n))

    def test_variation_split_and_signed_scaling(self):
        values=list(map(F,[1,-3,0,8,2,-1]))
        for k in range(len(values)):
            self.assertEqual(variation(values),
                             variation(values[:k+1])+variation(values[k:]))
        self.assertEqual(variation([-3*v for v in values]),3*variation(values))

    def test_plateau_reparametrization_and_asymmetric_reverse_tags(self):
        grid=[F(i,8) for i in range(9)]
        tags=[(2*u+v)/3 for u,v in zip(grid,grid[1:])]
        alpha=lambda x:x-2*int(x>=F(1,2))
        f=lambda x:x*x
        phi=lambda t:max(F(0),2*t-1)
        def total(points,ts,g,a):
            return sum(g(t)*(a(v)-a(u))
                       for u,v,t in zip(points,points[1:],ts))
        image=[(phi(u),phi(v),phi(t))
               for u,v,t in zip(grid,grid[1:],tags) if phi(u)!=phi(v)]
        expected=sum(f(t)*(alpha(v)-alpha(u)) for u,v,t in image)
        self.assertEqual(total(grid,tags,lambda t:f(phi(t)),lambda t:alpha(phi(t))),expected)
        rev_points=[1-x for x in reversed(grid)]
        rev_tags=[1-t for t in reversed(tags)]
        self.assertEqual(total(grid,tags,lambda t:f(1-t),lambda t:alpha(1-t)),
                         -total(rev_points,rev_tags,f,alpha))


if __name__=="__main__":
    unittest.main()
