from fractions import Fraction as F
from math import sin, cos, tan, pi, hypot
from pathlib import Path
import unittest


class Chapter33(unittest.TestCase):
    def test_area_squeezed_by_rectangles(self):
        for n in (2,4,10,50):
            p=[F(i,n) for i in range(n+1)]
            inner=sum(max(F(0),a-b*b)*(b-a) for a,b in zip(p,p[1:]))
            outer=sum((b-a*a)*(b-a) for a,b in zip(p,p[1:]))
            self.assertLessEqual(inner,F(1,6))
            self.assertLessEqual(F(1,6),outer)
            self.assertLessEqual(outer-inner,F(2,n))

    def test_inner_rectangle_figure(self):
        a,b=F(48,100),F(55,100)
        lower=b*b
        upper=a
        self.assertGreater(upper,lower)
        for i in range(11):
            x=a+(b-a)*F(i,10)
            self.assertTrue(x*x<=lower<=upper<=x)

    def test_crossing_graphs_area(self):
        # y=x and y=-x, [-1,1].
        signed=F(1)**2-F(-1)**2
        area=(F(0)**2-F(1)**2)*(-1)+(F(1)**2-F(0)**2)
        self.assertEqual(signed,0)
        self.assertEqual(area,2)

    def test_polygonal_length_refinement(self):
        for n in (3,5,10,20):
            def polygon(k):
                p=[(cos(2*pi*i/k),sin(2*pi*i/k)) for i in range(k+1)]
                return sum(hypot(b[0]-a[0],b[1]-a[1]) for a,b in zip(p,p[1:]))
            self.assertLessEqual(polygon(n),polygon(2*n))
            self.assertLessEqual(polygon(2*n),2*pi)
        self.assertAlmostEqual(2*10000*sin(pi/10000),2*pi,places=6)

    def test_vector_increment_error(self):
        # gamma(t)=(t,t^2), derivative=(1,2t).
        for n in (2,5,10,100):
            for i in range(n):
                a,b=F(i,n),F(i+1,n)
                for t in (a,(a+b)/2,b):
                    err=b*b-a*a-2*t*(b-a)
                    self.assertLessEqual(abs(err),(b-a)**2)

    def test_length_repeated_traversal(self):
        for r in (1,2,5):
            self.assertAlmostEqual(r*4*pi,2*r*2*pi)
            for t in (0.,.3,1.4,2.):
                self.assertAlmostEqual(hypot(-r*sin(t),r*cos(t)),r)

    def test_washer_squeeze(self):
        # u=x, v=x+1, [0,1], normalized volume V/pi=2.
        for n in (2,4,10,50):
            p=[F(i,n) for i in range(n+1)]
            low=sum(max(F(0),(a+1)**2-b*b)*(b-a) for a,b in zip(p,p[1:]))
            high=sum(((b+1)**2-a*a)*(b-a) for a,b in zip(p,p[1:]))
            self.assertLessEqual(low,2)
            self.assertLessEqual(2,high)
            self.assertLessEqual(high-low,F(4,n))

    def test_sphere_volume(self):
        for r in map(F,(1,2,5)):
            H=lambda x:r*r*x-x**3/3
            self.assertEqual(H(r)-H(-r),F(4,3)*r**3)

    def test_frustum_formula(self):
        for p,q,l in ((F(1),F(3),F(5)),(F(0),F(2),F(3)),(F(4),F(2),F(6))):
            small,large=sorted((p,q))
            l1=l*small/(large-small)
            l2=l*large/(large-small)
            self.assertEqual(l2-l1,l)
            self.assertEqual(large*l2-small*l1,(p+q)*l)

    def test_surface_frusta_sphere(self):
        def area(n):
            p=[(cos(pi*i/n),sin(pi*i/n)) for i in range(n+1)]
            return pi*sum((a[1]+b[1])*hypot(a[0]-b[0],a[1]-b[1]) for a,b in zip(p,p[1:]))
        self.assertLess(abs(area(100)-4*pi),abs(area(10)-4*pi))
        self.assertAlmostEqual(area(10000),4*pi,places=6)

    def test_sector_polygon_bounds(self):
        for angle in (.3,pi,2*pi):
            for n in (4,10,100):
                d=angle/n
                self.assertLessEqual(n*sin(d)/2,angle/2)
                self.assertLessEqual(angle/2,n*tan(d/2))
            self.assertAlmostEqual(100000*sin(angle/100000)/2,angle/2,places=7)

    def test_polar_speed(self):
        for t in (0.,.4,pi,4.):
            r=1+cos(t)
            dr=-sin(t)
            dx=dr*cos(t)-r*sin(t)
            dy=dr*sin(t)+r*cos(t)
            self.assertAlmostEqual(dx*dx+dy*dy,dr*dr+r*r)

    def test_cardioid_area(self):
        for n in (8,16,32):
            total=sum((1+cos(2*pi*i/n))**2 for i in range(n))*pi/n
            self.assertAlmostEqual(total,3*pi/2)

    def test_triangle_centroid_moments(self):
        A=F(1,2)
        Mx=F(1,2)*F(1,3)
        My=F(1,3)
        self.assertEqual((My/A,Mx/A),(F(2,3),F(1,3)))
        self.assertEqual(F(1,3)*F(1,4),F(1,12))
        self.assertEqual(F(1,4),F(1,4))

    def test_pappus_volume_torus(self):
        for R,r in ((F(3),F(1)),(F(5),F(2))):
            for w in (F(0),r/2,r):
                u,v=R-w,R+w
                self.assertEqual(v*v-u*u,2*R*(v-u))
            # V/pi^2 as inferred from centroid and disk area.
            self.assertEqual(2*R*r*r,2*R*r**2)

    def test_torus_surface(self):
        R,r=3.,1.
        for n in (8,16,32):
            self.assertAlmostEqual(2*pi*r*sum(R+r*sin(2*pi*i/n) for i in range(n))*2*pi/n,4*pi*pi*R*r)

    def test_figure_sources(self):
        s=(Path(__file__).resolve().parents[4] /
           "chapters/pl/mathematical_analysis_i/33-zastosowania-rachunku-calkowego.tex").read_text(encoding="utf8")
        for token in (r"(.48,{.55*.55}) rectangle (.55,.48)",r"ellipse (.29 and 1.45)",r"(1+cos(\x))*cos(\x)"):
            self.assertIn(token,s)


if __name__=="__main__":
    unittest.main()
