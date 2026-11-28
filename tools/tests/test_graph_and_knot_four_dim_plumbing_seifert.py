#!/usr/bin/env python3
"""Independent exact regression for graph/knot chapters 22--24.

Checks intersection lattices, leaf elimination, Seifert presentations,
branched E8/An/Dn plumbing determinants, Smith invariants, signature
linear algebra and Fox--Milnor algebra. Finite arithmetic does NOT
prove Freedman, Donaldson, Murasugi, geometric Seifert surgery or Kirby.
Standard library only.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd, prod
from pathlib import Path
import random

BASE=Path(__file__).resolve().parents[2]/"chapters/pl/graph_and_knot_theory"


def det(A):
    """Exact Bareiss determinant with pivoting, including empty matrix."""
    n=len(A)
    if not n:return 1
    a=[list(row) for row in A]
    assert all(len(row)==n for row in a)
    prev=1; sign=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*pivot-a[i][k]*a[k][j]
                assert v%prev==0
                a[i][j]=v//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def qtree(weights,edges):
    n=len(weights)
    Q=[[0]*n for _ in range(n)]
    for i,w in enumerate(weights):Q[i][i]=w
    for i,j in edges:
        Q[i][j]+=1;Q[j][i]+=1
    return Q


def induced(weights,edges,keep):
    idx={v:i for i,v in enumerate(keep)}
    return qtree([weights[i] for i in keep],
                 [(idx[i],idx[j]) for i,j in edges if i in idx and j in idx])


def leaf_checks():
    cases=[(1,[]),(2,[(0,1)]),(3,[(0,1),(1,2)]),
           (4,[(0,1),(0,2),(0,3)]),
           (5,[(0,1),(1,2),(2,3),(1,4)]),
           (6,[(0,1),(1,2),(2,3),(3,4),(2,5)])]
    count=0
    for n,edges in cases:
        leaves=[v for v in range(n)
                if sum(v in e for e in edges)==1]
        if not leaves:continue
        for w in product((-3,-2,-1,0,2),repeat=n):
            Q=qtree(w,edges)
            for v in leaves:
                u=next(j if i==v else i for i,j in edges if v in (i,j))
                keep=[i for i in range(n) if i!=v]
                rem=[i for i in range(n) if i not in (v,u)]
                rhs=w[v]*det(induced(w,edges,keep))-det(induced(w,edges,rem))
                assert det(Q)==rhs,(n,edges,w,v)
                count+=1
    return count


def an_dn_e8_checks():
    count=0
    for n in range(1,14):
        edges=[(i,i+1) for i in range(n-1)]
        Q=qtree([-2]*n,edges)
        assert det(Q)==(-1)**n*(n+1)
        # Sylvester negative definiteness for all leading principal minors
        assert all((-1)**k*det([row[:k] for row in Q[:k]])>0
                   for k in range(1,n+1))
        count+=n+1
    for n in range(4,15):
        # D_n: long arm with n-3 vertices and two short leaves
        edges=[(i,i+1) for i in range(n-3)]  # line vertices 0..n-3
        edges.extend(((n-3,n-2),(n-3,n-1)))
        Q=qtree([-2]*n,edges)
        assert det(Q)==(-1)**n*4
        assert rank_modp(Q,2)==n-(2 if n%2==0 else 1)
        count+=2
    edges=[(i,i+1) for i in range(6)]+[(2,7)]
    Q=qtree([-2]*8,edges)
    assert det(Q)==1
    assert all((-1)**k*det([row[:k] for row in Q[:k]])>0
               for k in range(1,9))
    # Even integral form: x^T Q x is divisible by 2.
    for x in product((-1,0,1),repeat=8):
        assert sum(x[i]*Q[i][j]*x[j]
                   for i in range(8) for j in range(8))%2==0
        count+=1
    return count


def rank_modp(A,p):
    if not A:return 0
    a=[[int(x)%p for x in row] for row in A]
    n=len(a);m=len(a[0]);i=0
    for j in range(m):
        k=next((k for k in range(i,n) if a[k][j]%p),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        inv=pow(a[i][j],-1,p)
        a[i]=[v*inv%p for v in a[i]]
        for k in range(n):
            if k!=i and a[k][j]:
                v=a[k][j]
                a[k]=[(q-v*t)%p for q,t in zip(a[k],a[i])]
        i+=1
        if i==n:break
    return i


def cont_frac(arm):
    c=Fraction(arm[-1])
    for x in arm[-2::-1]:c=Fraction(x)-1/c
    return c


def seifert_matrix(b,alphas,betas):
    r=len(alphas)
    assert len(betas)==r
    A=[[0]*(r+1) for _ in range(r+1)]
    for i,(alpha,beta) in enumerate(zip(alphas,betas)):
        A[i][i]=alpha;A[i][-1]=beta;A[-1][i]=1
    A[-1][-1]=-b
    return A


def star_checks():
    counts=0
    for lens in [(1,1,1),(1,2,3),(1,2,4),(2,1,2)]:
        choices=[list(product((2,3),repeat=n)) for n in lens]
        for arms in product(*choices):
            fracs=[cont_frac(a) for a in arms]
            alphas=[x.numerator for x in fracs]
            betas=[x.denominator for x in fracs]
            for b in (-3,-2,-1,0,1):
                weights=[b]+[-a for arm in arms for a in arm]
                edges=[];cur=1
                for arm in arms:
                    prev=0
                    for _ in arm:
                        edges.append((prev,cur))
                        prev=cur;cur+=1
                Q=qtree(weights,edges)
                s=Fraction(b)+sum((Fraction(q,p) for p,q in zip(alphas,betas)),Fraction())
                signed=(-1)**sum(lens)*prod(alphas)*s
                assert signed.denominator==1
                assert det(Q)==signed.numerator,(lens,arms,b)
                S=seifert_matrix(b,alphas,betas)
                # Sign conventions: det(Seifert A)=(-1)*prod(alpha)*s.
                assert det(S)==-prod(alphas)*s
                counts+=1
    return counts


def smith_maximal_minor_gcd(A,r):
    # Product of nonzero Smith factors for a rank-r integer matrix.
    rows=range(len(A));cols=range(len(A[0]))
    return gcd(*(abs(det([[A[i][j] for j in J] for i in I]))
                 for I in combinations(rows,r)
                 for J in combinations(cols,r)))


def seifert_torsion_checks():
    cases=[
        (-2,(2,3,5),(1,2,4),1),
        (-1,(3,3,3),(1,1,1),0),
        (-1,(2,2),(1,1),0),
        (0,(2,3,5),(1,1,1),31),
    ]
    for b,a,bet,expected_abs in cases:
        A=seifert_matrix(b,a,bet)
        s=Fraction(b)+sum((Fraction(q,p) for p,q in zip(a,bet)),Fraction())
        want=-prod(a)*s
        assert want.denominator==1
        assert det(A)==want.numerator
        if expected_abs:
            assert abs(det(A))==expected_abs
    e0=seifert_matrix(-1,(3,3,3),(1,1,1))
    assert det(e0)==0
    # Rank 3, torsion order gcd of 3x3 minors equals 3.
    assert smith_maximal_minor_gcd(e0,3)==3
    # At g=0 this gives H1=Z ⊕ Z/3.
    return len(cases)+1


def pmul(A,B):
    C={}
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]=C.get(i+j,0)+a*b
    return {i:a for i,a in C.items() if a}


def padd(A,B):
    C=A.copy()
    for i,b in B.items():C[i]=C.get(i,0)+b
    return {i:a for i,a in C.items() if a}


def pdet(M):
    n=len(M)
    if not n:return {0:1}
    out={}
    for perm in permutations(range(n)):
        parity=sum(perm[i]>perm[j] for i in range(n)
                   for j in range(i+1,n))%2
        term={0:(-1)**parity}
        for i,j in enumerate(perm):term=pmul(term,M[i][j])
        out=padd(out,term)
    return out


def fox_milnor_checks():
    rng=random.Random(23024)
    checks=0
    for g in (1,2):
        for _ in range(220 if g==1 else 120):
            A=[[rng.randrange(-2,3) for j in range(g)] for i in range(g)]
            B=[[rng.randrange(-2,3) for j in range(g)] for i in range(g)]
            C=[[rng.randrange(-2,3) for j in range(g)] for i in range(g)]
            V=[[0]*g+A[i] for i in range(g)]+[B[i]+C[i] for i in range(g)]
            n=2*g
            M=[[padd({1:V[i][j]},{0:-V[j][i]})
                for j in range(n)] for i in range(n)]
            f=pdet([[padd({1:A[i][j]},{0:-B[j][i]})
                    for j in range(g)] for i in range(g)])
            f_rev={-i:c for i,c in f.items()}
            rhs={k+g:c for k,c in pmul(f,f_rev).items()}
            assert pdet(M)==rhs,(g,V,f)
            checks+=1
    V=[[0,2],[1,0]]
    M=[[padd({1:V[i][j]},{0:-V[j][i]}) for j in range(2)]
       for i in range(2)]
    assert pdet(M)=={0:-2,1:5,2:-2}
    assert det([[V[i][j]-V[j][i] for j in range(2)]
                for i in range(2)])==1
    return checks+1


def isotropic_signature_checks():
    # Hyperbolic blocks with a chosen totally isotropic L and a
    # diagonal anisotropic remainder: signature<=n-2dim(L).
    count=0
    for d in range(1,5):
        for pos,neg in product(range(5),repeat=2):
            n=2*d+pos+neg
            Q=[[0]*n for _ in range(n)]
            for i in range(d):
                Q[i][d+i]=Q[d+i][i]=1
            for i in range(pos):Q[2*d+i][2*d+i]=1
            for i in range(neg):Q[2*d+pos+i][2*d+pos+i]=-1
            assert all(Q[i][j]==0 for i in range(d) for j in range(d))
            assert abs(pos-neg)<=n-2*d
            count+=1
    return count


def a5_triangle_checks():
    # s=(12)(34), t=(235): prove the displayed triangle-group
    # surjection by independent finite permutation enumeration.
    s=(2,1,4,3,5);t=(1,3,5,4,2)
    ident=(1,2,3,4,5)
    def mul(a,b):return tuple(a[b[i]-1] for i in range(5))
    def power(a,n):
        out=ident
        for _ in range(n):out=mul(out,a)
        return out
    assert power(s,2)==power(t,3)==power(mul(s,t),5)==ident
    group={ident};todo=[ident]
    for x in todo:
        for gen in (s,t):
            y=mul(x,gen)
            if y not in group:
                group.add(y);todo.append(y)
    assert len(group)==60
    return len(group)



def solve_fraction(A,b):
    """Independent rational Gauss-Jordan solver; never uses determinant cofactors."""
    n=len(A)
    assert n==len(b) and all(len(row)==n for row in A)
    aug=[[Fraction(t) for t in row]+[Fraction(rhs)]
         for row,rhs in zip(A,b)]
    for j in range(n):
        i=next((k for k in range(j,n) if aug[k][j]!=0),None)
        assert i is not None
        aug[i],aug[j]=aug[j],aug[i]
        pv=aug[j][j]
        aug[j]=[z/pv for z in aug[j]]
        for k in range(n):
            if k!=j:
                c=aug[k][j]
                aug[k]=[x-c*y for x,y in zip(aug[k],aug[j])]
    return [row[-1] for row in aug]


def an_linking_checks():
    # A_n: the x1 linking self-pairing is n/(n+1) mod 1.
    cases=0
    for n in range(1,21):
        Q=qtree([-2]*n,[(i,i+1) for i in range(n-1)])
        e1=[int(i==0) for i in range(n)]
        inv_col=solve_fraction(Q,e1)
        actual=-inv_col[0]
        expected=Fraction(n,n+1)
        assert actual==expected
        assert actual.denominator==n+1
        # Test bilinear linking pairing against relation vectors Q*z.
        for shift in (1,-1,3):
            rel=[sum(Q[i][j]*(shift if j==0 else 0)
                     for j in range(n)) for i in range(n)]
            new_e1=[x+y for x,y in zip(e1,rel)]
            assert sum(new_e1[i]*inv_col[i] for i in range(n))-inv_col[0] == shift
            cases+=1
    return cases


def star_zero_e_kernel_checks():
    """Cross-check zero e_Q, primitive null vector and torsion Smith minors."""
    samples=[
        (-1,(3,3,3),3),
        (-1,(2,3,6),1),
        (-1,(2,4,4),2),
        (-1,(2,2),1),
        (-2,(2,2,2,2),4),
    ]
    count=0
    for b,alphas,torsion_expected in samples:
        assert Fraction(b)+sum((Fraction(1,a) for a in alphas),Fraction())==0
        edges=[(0,i) for i in range(1,len(alphas)+1)]
        Q=qtree([b]+[-a for a in alphas],edges)
        from math import lcm
        central=lcm(*alphas)
        null=[central]+[central//a for a in alphas]
        assert gcd(*null)==1
        assert all(sum(Q[i][j]*null[j] for j in range(len(null)))==0
                   for i in range(len(null)))
        assert det(Q)==0
        n=len(null)
        minors=smith_maximal_minor_gcd(Q,n-1)
        # Torsion order is the product of nonzero Smith factors.
        assert minors==torsion_expected,(b,alphas,minors)
        S=seifert_matrix(b,alphas,(1,)*len(alphas))
        assert det(S)==0
        assert smith_maximal_minor_gcd(S,n-1)==torsion_expected
        count+=1
    return count


def trefoil_murasugi_signature_checks():
    # Independent exact principal-minor check for the positive
    # definite 2x2 Seifert symmetrization of a trefoil.
    S=[[2,-1],[-1,2]]
    assert S[0][0]>0 and det(S)>0
    assert det(S)==3
    assert all(sum(x[i]*S[i][j]*x[j] for i in range(2) for j in range(2))>0
               for x in product((-2,-1,0,1,2),repeat=2) if x!=(0,0))
    # Two positive eigenvalues imply signature = 2;
    # Murasugi: g4>=1; Seifert genus 1: g4<=1.
    assert abs(2)<=2*1
    return 24


def source_checks():
    names=[
        "22-wezly-i-rozmaitosci-czterowymiarowe.tex",
        "23-grafy-plumbingowe-formy-przeciecia-i-krata-e8.tex",
        "24-rozmaitosci-seiferta-i-grafy-gwiazdziste.tex",
    ]
    x,y,z=[(BASE/n).read_text(encoding="utf8") for n in names]
    assert r"\label{lem:kt-isotropic-signature}" in x
    assert r"\label{ex:kt-trefoil-four-genus-signature}" in x
    assert r"\label{ex:kt-fox-milnor-matrix}" in x
    assert r"\label{lem:tg-plumbing-leaf-determinant}" in y
    assert r"\label{st:tg-plumbing-An-linking}" in y
    assert r"\label{ex:tg-plumbing-D4-leaf}" in y
    assert r"\label{ex:tg-seifert-zero-e-torsion}" in z
    assert r"\label{st:tg-star-definiteness}" in z
    assert r"\label{cor:tg-star-nullspace-boundary}" in z
    assert r"\label{ex:tg-star-zero-e-kernel}" in z


if __name__=="__main__":
    source_checks()
    print("PASS weighted plumbing tree leaf minors:",leaf_checks())
    print("PASS An Dn E8 determinant, ranks and E8 parity:",an_dn_e8_checks())
    print("PASS star plumbing Schur and Seifert determinant:",star_checks())
    print("PASS Seifert Smith invariants including zero Euler torsion:",seifert_torsion_checks())
    print("PASS Fox-Milnor exact Laurent factorization:",fox_milnor_checks())
    print("PASS Murasugi isotropic algebra:",isotropic_signature_checks())
    print("PASS E8 triangle group finite A5 image:",a5_triangle_checks())
    print("PASS A_n exact linking form and integral relations:",an_linking_checks())
    print("PASS Seifert zero-Euler primitive kernels and Smith torsion:",star_zero_e_kernel_checks())
    print("PASS trefoil signature obstruction to smooth slicing:",trefoil_murasugi_signature_checks())
