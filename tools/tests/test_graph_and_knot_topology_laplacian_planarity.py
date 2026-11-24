#!/usr/bin/env python3
"""Global graph/knot audit: historical chapters 07--09 (exact finite models).

Independent checks for finite graph coverings, homotopy ranks, Kirchhoff's
matrix-tree theorem (weighted/unweighted), spectral determinant identity,
resistance and Dirichlet energy, planar rotation systems and face coloring.
No external dependencies, no random sampling, exact Fraction arithmetic.
These tests complement and DO NOT replace proofs for arbitrary finite graphs.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[2]


def edge_pairs(n):
    return tuple(combinations(range(n),2))


def components(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen=set()
    groups=[]
    for root in range(n):
        if root in seen:
            continue
        current={root}
        queue=[root]
        seen.add(root)
        for u in queue:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);current.add(v);queue.append(v)
        groups.append(current)
    return groups


def is_connected(n,edges):
    return n>=1 and len(components(n,edges))==1


def exact_determinant(matrix):
    """Rational elimination, preserving exactness and pivot signs."""
    n=len(matrix)
    if n==0:
        return Fraction(1)
    a=[[Fraction(x) for x in row] for row in matrix]
    out=Fraction(1)
    for col in range(n):
        pivot=next((r for r in range(col,n) if a[r][col]!=0),None)
        if pivot is None:
            return Fraction(0)
        if pivot!=col:
            a[col],a[pivot]=a[pivot],a[col]
            out=-out
        pivot_val=a[col][col]
        out*=pivot_val
        for i in range(col+1,n):
            if a[i][col]!=0:
                scale=a[i][col]/pivot_val
                for j in range(col+1,n):
                    a[i][j]-=scale*a[col][j]
                a[i][col]=0
    return out


def solve(matrix,rhs):
    """Independent Gaussian elimination over rational numbers."""
    n=len(rhs)
    if not n:
        return []
    a=[[Fraction(x) for x in row]+[Fraction(rhs[i])]
       for i,row in enumerate(matrix)]
    for col in range(n):
        piv=next((r for r in range(col,n) if a[r][col]),None)
        assert piv is not None, "Dirichlet system unexpectedly singular"
        a[col],a[piv]=a[piv],a[col]
        div=a[col][col]
        a[col]=[x/div for x in a[col]]
        for row in range(n):
            if row!=col:
                mult=a[row][col]
                if mult:
                    a[row]=[x-mult*y for x,y in zip(a[row],a[col])]
    return [a[i][-1] for i in range(n)]


def laplacian(n,edges,weights):
    L=[[Fraction(0) for j in range(n)] for i in range(n)]
    for (u,v),w in zip(edges,weights):
        L[u][u]+=w
        L[v][v]+=w
        L[u][v]-=w
        L[v][u]-=w
    return L


def tree_weight(n,edges,weights):
    if not n:
        return Fraction(0)
    if n==1:
        return Fraction(1)
    result=Fraction(0)
    for idx in combinations(range(len(edges)),n-1):
        selected=[edges[i] for i in idx]
        if is_connected(n,selected):
            term=Fraction(1)
            for i in idx:
                term*=weights[i]
            result+=term
    return result


def audit_kirchhoff(n,edges):
    m=len(edges)
    for weights in ([1]*m,[(i%3)+1 for i in range(m)]):
        L=laplacian(n,edges,weights)
        cofactor=exact_determinant([row[:-1] for row in L[:-1]])
        expected=tree_weight(n,edges,weights)
        assert cofactor==expected,(n,edges,weights,cofactor,expected)
        if is_connected(n,edges):
            # det(L+11^T/n) = n det(L_reduced), independently.
            shifted=[[L[i][j]+Fraction(1,n)
                      for j in range(n)] for i in range(n)]
            assert exact_determinant(shifted)==n*expected
    if n>=2 and is_connected(n,edges):
        weights=[(i%3)+1 for i in range(m)]
        L=laplacian(n,edges,weights)
        # Unit current source at 0, sink n-1, normalized f(n-1)=0.
        b=[Fraction(int(i==0)-int(i==n-1)) for i in range(n)]
        f=solve([row[:-1] for row in L[:-1]],b[:-1])+[Fraction(0)]
        current=[w*(f[u]-f[v]) for (u,v),w in zip(edges,weights)]
        assert all(
            sum(L[v][u]*f[u] for u in range(n))==b[v]
            for v in range(n)
        )
        resistance=f[0]-f[-1]
        assert resistance>0
        assert resistance==sum((j*j/Fraction(w) for j,w in zip(current,weights)),
                               Fraction(0))
        assert resistance==sum(
            (weights[i]*(f[u]-f[v])**2 for i,(u,v) in enumerate(edges)),
            Fraction(0)
        )
        # Dirichlet conditions f(0)=0, f(n-1)=1.
        boundary={0:Fraction(0),n-1:Fraction(1)}
        interior=list(range(1,n-1))
        x=solve([[L[u][v] for v in interior] for u in interior],
                [-sum(L[u][b]*value for b,value in boundary.items())
                 for u in interior])
        h=[boundary.get(v) for v in range(n)]
        for v,value in zip(interior,x):
            h[v]=value
        assert all(sum(L[u][v]*h[v] for v in range(n))==0 for u in interior)
        assert min(h)>=0 and max(h)<=1
        energy=lambda values:sum(
            (Fraction(w)*(values[u]-values[v])**2
             for (u,v),w in zip(edges,weights)),Fraction(0))
        baseline=energy(h)
        for u in interior:
            for offset in (-1,1):
                g=h[:];g[u]+=offset
                assert energy(g)>baseline
    return True


def graph_cover(n,base_edges,d,shifts):
    """Construct finite d-cover of simple base via voltage assignments mod d."""
    N=n*d
    lifted=[]
    for (u,v),shift in zip(base_edges,shifts):
        for sheet in range(d):
            lifted.append((d*u+sheet,d*v+(sheet+shift)%d))
    assert len(lifted)==d*len(base_edges)
    assert N==d*n
    # At each lifted vertex, one and only one incidence over each
    # base incidence is present (local graph-covering condition).
    for u in range(n):
        base_neigh={v for e in base_edges for v in e if u in e and v!=u}
        for sheet in range(d):
            incident=[(x,y) for x,y in lifted if d*u+sheet in (x,y)]
            assert len(incident)==len(base_neigh)
            images={((x if y==d*u+sheet else y)//d) for x,y in incident}
            assert images==base_neigh
    groups=components(N,lifted)
    beta=len(lifted)-N+len(groups)
    base_beta=len(base_edges)-n+1
    assert beta==d*(base_beta-1)+len(groups)
    if len(groups)==1:
        assert beta==1+d*(base_beta-1)
    return len(groups)==1


def audit_covers():
    total=connected_cases=0
    for n in range(1,5):
        all_e=edge_pairs(n)
        for mask in range(1<<len(all_e)):
            edges=[e for i,e in enumerate(all_e) if mask>>i &1]
            if not is_connected(n,edges):
                continue
            for d in (2,3):
                for shifts in product(range(d),repeat=len(edges)):
                    total+=1
                    if graph_cover(n,edges,d,shifts):
                        connected_cases+=1
    return total,connected_cases


def audit_permutation_covers():
    """TG07-PERM-01: all pairs of sheet permutations, degrees 1 through 4."""
    cases=connected=automorphisms=0
    for d in range(1,5):
        perms=list(permutations(range(d)))
        for sigmas in product(perms,repeat=2):
            # Base: two triangles meeting at root 0. The two chords
            # are the only edges with nonidentity sheet transport.
            base=[(0,1),(1,2),(0,3),(3,4),(2,0),(4,0)]
            transports=[tuple(range(d))]*4+list(sigmas)
            lifted=[(d*u+i,d*v+p[i])
                    for (u,v),p in zip(base,transports) for i in range(d)]
            groups=components(5*d,lifted)
            roots=[{v%d for v in group if v//d==0} for group in groups]
            unseen=set(range(d))
            orbits=[]
            while unseen:
                orbit={min(unseen)}
                queue=list(orbit)
                for i in queue:
                    for p in sigmas:
                        j=p[i]
                        if j not in orbit:
                            orbit.add(j)
                            queue.append(j)
                orbits.append(orbit)
                unseen-=orbit
            assert {frozenset(g) for g in roots}=={frozenset(g) for g in orbits}
            assert all(len(group)==5*len(root) for group,root in zip(groups,roots))
            # Independently compare the actual lifted edge set with its
            # image under simultaneous sheet relabeling.
            edge_set=set(lifted)
            deck=[]
            for rho in perms:
                image={(d*(u//d)+rho[u%d],d*(v//d)+rho[v%d])
                       for u,v in lifted}
                is_deck=image==edge_set
                commutes=all(rho[p[i]]==p[rho[i]] for p in sigmas for i in range(d))
                assert is_deck==commutes
                if is_deck:
                    deck.append(rho)
                # Conjugate the permutations and compare lifted graphs.
                inv=tuple(rho.index(i) for i in range(d))
                taus=[tuple(rho[p[inv[i]]] for i in range(d)) for p in sigmas]
                relabeled={(d*u+i,d*v+p[i])
                           for (u,v),p in zip(base,[tuple(range(d))]*4+taus)
                           for i in range(d)}
                assert image==relabeled
            if len(groups)==1:
                connected+=1
                assert all(rho==tuple(range(d)) or all(rho[i]!=i for i in range(d))
                           for rho in deck)
                assert len(lifted)-5*d+1==d+1
            automorphisms+=len(deck)
            cases+=1
    # A transitive, noncyclic monodromy with trivial deck group.
    p,q=(1,0,2),(0,2,1)
    assert [rho for rho in permutations(range(3))
            if all(rho[s[i]]==s[rho[i]] for s in (p,q) for i in range(3))]==[(0,1,2)]
    return cases,connected,automorphisms


def audit_universal_cover_prefixes():
    """TG07-UC-01: exact truncated universal covers, including loops and parallel edges."""
    graphs=roots=vertices=incidences=0
    for n in range(1,4):
        types=list(combinations(range(n),2))+[(v,v) for v in range(n)]
        for multiplicities in product(range(3),repeat=len(types)):
            E=[e for e,k in zip(types,multiplicities) for _ in range(k)]
            if len(E)>5 or not is_connected(n,E):
                continue
            graphs+=1
            outgoing=[[] for _ in range(n)]
            for j,(u,v) in enumerate(E,1):
                outgoing[u].append((j,v))
                outgoing[v].append((-j,u))
            for root in range(n):
                roots+=1
                depth=4
                endpoint={():root}
                layer=[()]
                for _ in range(depth):
                    new=[]
                    for w in layer:
                        for step,v in outgoing[endpoint[w]]:
                            if w and step==-w[-1]:
                                continue
                            z=w+(step,)
                            assert z not in endpoint
                            endpoint[z]=v
                            new.append(z)
                    layer=new
                vertices+=len(endpoint)
                assert len(endpoint)-1==sum(bool(w) for w in endpoint)
                for w,v in endpoint.items():
                    if len(w)==depth:
                        continue
                    neighbors=[]
                    for step,target in outgoing[v]:
                        z=w[:-1] if w and step==-w[-1] else w+(step,)
                        assert z in endpoint and endpoint[z]==target
                        neighbors.append(z)
                        incidences+=1
                    assert len(set(neighbors))==len(outgoing[v])
                    assert sum(len(z)<len(w) for z in neighbors)==bool(w)
                if len(E)==n-1:
                    assert len(endpoint)==n
                else:
                    assert layer  # a cycle permits arbitrarily long reduced walks
    return graphs,roots,vertices,incidences


def audit_radial_contraction():
    """TG07-RAD-01: exact common-prefix distance in a rooted tree."""
    checks=0
    # a,b are distances to root; c is length of shared initial arc.
    # Include points in edge interiors and both contraction regimes.
    for a,b in product((Fraction(i,2) for i in range(11)),repeat=2):
        for c in (Fraction(i,2) for i in range(11) if Fraction(i,2)<=min(a,b)):
            for s in (Fraction(i,8) for i in range(9)):
                before=a+b-2*c
                after=s*(a+b)-2*min(c,s*a,s*b)
                assert 0<=after<=before
                checks+=1
    return checks


def audit_length_metric():
    """TG07-MET-01: unit-edge metric at quarter points, including loops."""
    graphs=points=distances=0
    for n in range(1,4):
        types=list(combinations(range(n),2))+[(v,v) for v in range(n)]
        for multiplicities in product(range(3),repeat=len(types)):
            E=[e for e,k in zip(types,multiplicities) for _ in range(k)]
            if len(E)>4 or not is_connected(n,E):
                continue
            # Each unit edge subdivided into four equal parts.
            N=n+3*len(E)
            adj=[[] for _ in range(N)]
            for j,(u,v) in enumerate(E):
                path=[u,n+3*j,n+3*j+1,n+3*j+2,v]
                for x,y in zip(path,path[1:]):
                    adj[x].append(y)
                    adj[y].append(x)
            D=[]
            for x in range(N):
                row=[None]*N
                row[x]=0
                queue=[x]
                for u in queue:
                    for v in adj[u]:
                        if row[v] is None:
                            row[v]=row[u]+1
                            queue.append(v)
                D.append(row)
            B=[[0 if u==v else n+1 for v in range(n)] for u in range(n)]
            for u,v in E:
                if u!=v:
                    B[u][v]=B[v][u]=1
            for k in range(n):
                for u in range(n):
                    for v in range(n):
                        B[u][v]=min(B[u][v],B[u][k]+B[k][v])
            assert all(D[u][v]==4*B[u][v] for u in range(n) for v in range(n))
            def ends(x):
                if x<n:
                    return [(x,0)]
                j,t=divmod(x-n,3)
                u,v=E[j]
                return [(u,t+1),(v,3-t)]
            for x in range(N):
                for y in range(N):
                    expected=min(a+4*B[u][v]+b for u,a in ends(x) for v,b in ends(y))
                    if x>=n and y>=n and (x-n)//3==(y-n)//3:
                        expected=min(expected,abs(x-y))
                    assert D[x][y]==expected
                    assert (D[x][y]==0)==(x==y)
                    assert D[x][y]==D[y][x]
                    distances+=1
            points+=N
            graphs+=1
    return graphs,points,distances


def audit_cover_tree_normalization():
    """TG07-NORM-01: normalize arbitrary sheet labels along a spanning tree."""
    # Two tree edges with opposite traversal signs, a chord and a loop.
    E=[(0,1),(2,1),(0,2),(1,1)]
    cases=connected=edges_checked=0
    for d in range(1,4):
        identity=tuple(range(d))
        perms=list(permutations(identity))
        for p in product(perms,repeat=len(E)):
            # g[v][i] is the old label of new sheet i over v.
            g=[identity,p[0],tuple(p[1].index(p[0][i]) for i in identity)]
            q=[tuple(g[v].index(sigma[g[u][i]]) for i in identity)
               for (u,v),sigma in zip(E,p)]
            assert q[0]==q[1]==identity
            original={(j,u*d+i,v*d+p[j][i])
                      for j,(u,v) in enumerate(E) for i in identity}
            normalized={(j,u*d+i,v*d+q[j][i])
                        for j,(u,v) in enumerate(E) for i in identity}
            transported={(j,u*d+g[u][i],v*d+g[v][q[j][i]])
                         for j,(u,v) in enumerate(E) for i in identity}
            assert transported==original
            old_components=components(3*d,[(u,v) for _,u,v in original])
            new_components=components(3*d,[(u,v) for _,u,v in normalized])
            old_partition={frozenset(C) for C in old_components}
            new_partition={frozenset((x//d)*d+g[x//d][x%d] for x in C)
                           for C in new_components}
            assert old_partition==new_partition
            # For each named base edge, both directed incidences occur once
            # above each of its ends, even if that edge is a loop.
            for j,(u,v) in enumerate(E):
                for i in identity:
                    assert sum(k==j and x==u*d+i for k,x,y in original)==1
                    assert sum(k==j and y==v*d+i for k,x,y in original)==1
                    edges_checked+=2
            cases+=1
            connected+=int(len(old_components)==1)
    return cases,connected,edges_checked


def audit_rooted_forests():
    """TG08-FOREST-01: all principal minors and weighted forest polynomials."""
    graphs=minors=polynomials=resistances=0
    for n in range(1,5):
        es=edge_pairs(n)
        for mask in range(1<<len(es)):
            E=[e for i,e in enumerate(es) if mask>>i&1]
            for weights in ([1]*len(E),[(i%3)+1 for i in range(len(E))]):
                L=laplacian(n,E,weights)
                forests=[]
                for subset in range(1<<len(E)):
                    selected=[j for j in range(len(E)) if subset>>j&1]
                    C=components(n,[E[j] for j in selected])
                    if len(selected)!=n-len(C):
                        continue
                    weight=1
                    for j in selected:
                        weight*=weights[j]
                    forests.append((C,weight))
                for S_mask in range(1,1<<n):
                    S={v for v in range(n) if S_mask>>v&1}
                    I=[v for v in range(n) if v not in S]
                    expected=sum(w for C,w in forests if all(len(c&S)==1 for c in C))
                    assert exact_determinant([[L[u][v] for v in I] for u in I])==expected
                    minors+=1
                # Compare polynomial evaluations at n+1 distinct integers.
                for t in range(-1,n):
                    expected=0
                    for C,w in forests:
                        root_choices=1
                        for c in C:
                            root_choices*=len(c)
                        expected+=t**len(C)*root_choices*w
                    assert exact_determinant([[L[u][v]+t*int(u==v) for v in range(n)]
                                              for u in range(n)])==expected
                    polynomials+=1
                if is_connected(n,E):
                    tree_sum=sum(w for C,w in forests if len(C)==1)
                    for s,t in combinations(range(n),2):
                        J=[v for v in range(n) if v!=t]
                        f=solve([[L[u][v] for v in J] for u in J],
                                [Fraction(int(u==s)) for u in J])
                        expected=sum(w for C,w in forests
                                     if len(C)==2 and all(len(c&{s,t})==1 for c in C))
                        assert f[J.index(s)]==Fraction(expected,tree_sum)
                        resistances+=1
                graphs+=1
    return graphs,minors,polynomials,resistances


def audit_rayleigh_equality():
    """TG08-RAY-01: exact equality criteria for weight changes and added edges."""
    graphs=terminal_pairs=changes=equal_changes=additions=equal_additions=0
    def potential(n, E, weights, s, t):
        L=laplacian(n,E,weights)
        J=[v for v in range(n) if v!=t]
        sol=solve([[L[u][v] for v in J] for u in J],
                  [Fraction(int(u==s)) for u in J])
        f=[Fraction(0)]*n
        for u,x in zip(J,sol):
            f[u]=x
        return f
    for n in range(2,5):
        es=edge_pairs(n)
        for mask in range(1<<len(es)):
            E=[e for i,e in enumerate(es) if mask>>i&1]
            if not is_connected(n,E):
                continue
            for weights in ([1]*len(E),[(i%3)+1 for i in range(len(E))]):
                graphs+=1
                for s,t in combinations(range(n),2):
                    terminal_pairs+=1
                    f=potential(n,E,weights,s,t)
                    R=f[s]
                    # Increase each nonempty subset of conductances.
                    for subset in range(1,1<<len(E)):
                        changed=[j for j in range(len(E)) if subset>>j&1]
                        w2=[w+int(j in changed) for j,w in enumerate(weights)]
                        R2=potential(n,E,w2,s,t)[s]
                        assert R2<=R
                        assert (R2==R)==all(f[E[j][0]]==f[E[j][1]] for j in changed)
                        changes+=1
                        equal_changes+=int(R2==R)
                    for u,v in es:
                        if (u,v) in E:
                            continue
                        R2=potential(n,E+[(u,v)],weights+[2],s,t)[s]
                        assert R2<=R
                        assert (R2==R)==(f[u]==f[v])
                        additions+=1
                        equal_additions+=int(R2==R)
    assert equal_changes and equal_changes<changes
    assert equal_additions and equal_additions<additions
    return graphs,terminal_pairs,changes,equal_changes,additions,equal_additions


def audit_dirichlet_boundary():
    """TG08-DIR-01: all boundary sets, including missed components."""
    graphs=boundaries=singular=solutions=0
    for n in range(1,5):
        es=edge_pairs(n)
        for mask in range(1<<len(es)):
            E=[e for i,e in enumerate(es) if mask>>i&1]
            C=components(n,E)
            for weights in ([1]*len(E),[(i%3)+1 for i in range(len(E))]):
                L=laplacian(n,E,weights)
                graphs+=1
                for mask_s in range(1<<n):
                    S={v for v in range(n) if mask_s>>v&1}
                    I=[v for v in range(n) if v not in S]
                    missed=[c for c in C if not c&S]
                    A=[[L[u][v] for v in I] for u in I]
                    assert (exact_determinant(A)==0)==bool(missed)
                    boundaries+=1
                    singular+=int(bool(missed))
                    # Ground one extra vertex in every missed component.
                    T=S|{min(c) for c in missed}
                    J=[v for v in range(n) if v not in T]
                    f=[Fraction(v-1) if v in S else Fraction(0) for v in range(n)]
                    sol=solve([[L[u][v] for v in J] for u in J],
                              [-sum(L[u][v]*f[v] for v in T) for u in J])
                    for u,x in zip(J,sol):
                        f[u]=x
                    assert all(sum(L[u][v]*f[v] for v in range(n))==0 for u in I)
                    assert all(f[v]==v-1 for v in S)
                    for c in C:
                        if c&S:
                            assert all(min(f[v] for v in c&S)<=f[u]<=max(f[v] for v in c&S) for u in c)
                    for c in missed:
                        h=[f[v]+int(v in c) for v in range(n)]
                        assert all(sum(L[u][v]*(h[v]-f[v]) for v in range(n))==0 for u in range(n))
                        assert all(h[v]==f[v] for v in S)
                    solutions+=1
    return graphs,boundaries,singular,solutions


def audit_hodge_spectra():
    """TG08-SPEC-01: weighted Gram spectra via exact determinant identities."""
    graphs=evaluations=0
    for n in range(1,5):
        es=edge_pairs(n)
        for mask in range(1<<len(es)):
            E=[e for i,e in enumerate(es) if mask>>i&1]
            m=len(E)
            # Integer square-root weights; both Gram matrices are integral.
            D=[[((j%3)+1)*(int(v==b)-int(v==a))
                for j,(a,b) in enumerate(E)] for v in range(n)]
            P=[[sum(D[u][j]*D[v][j] for j in range(m))
                for v in range(n)] for u in range(n)]
            Q=[[sum(D[v][i]*D[v][j] for v in range(n))
                for j in range(m)] for i in range(m)]
            assert P==laplacian(n,E,[((j%3)+1)**2 for j in range(m)])
            # Equality of characteristic polynomials after padding the
            # smaller Gram matrix with zero eigenvalues, including m=0.
            for t in range(max(n,m)+1):
                p=exact_determinant([[t*int(u==v)-P[u][v]
                                      for v in range(n)] for u in range(n)])
                q=exact_determinant([[t*int(i==j)-Q[i][j]
                                      for j in range(m)] for i in range(m)])
                assert t**max(0,m-n)*p==t**max(0,n-m)*q
                evaluations+=1
            graphs+=1
    return graphs,evaluations


def planar_rotation(n,edges):
    """Exhaustive oriented sphere-embedding search via cyclic edge orders.

    A rotation system determines faces as orbits of the
    (u->v) => (v->next_after_u_at_v) dart permutation.
    Connected orientable genus 0 iff n - m + face_count == 2.
    """
    assert is_connected(n,edges)
    if not edges:
        return [()],{}
    nbr=[[] for _ in range(n)]
    for u,v in edges:
        nbr[u].append(v);nbr[v].append(u)
    options=[]
    for neighbors in nbr:
        a=tuple(sorted(neighbors))
        options.append(tuple((a[0],)+p for p in permutations(a[1:])))
    for rotations in product(*options):
        next_dart={}
        for v in range(n):
            neigh=rotations[v]
            for i,u in enumerate(neigh):
                next_dart[(u,v)]=(v,neigh[(i+1)%len(neigh)])
        darts=set(next_dart)
        faces=[];face_of={}
        while darts:
            first=min(darts);cur=first;orbit=[]
            while cur in darts:
                darts.remove(cur)
                face_of[cur]=len(faces)
                orbit.append(cur)
                cur=next_dart[cur]
            assert cur==first
            faces.append(tuple(orbit))
        if n-len(edges)+len(faces)==2:
            return faces,face_of
    return None,None


def dual_faces_two_color(edges,nfaces,face_of):
    dual=[set() for _ in range(nfaces)]
    for u,v in edges:
        a=face_of[(u,v)];b=face_of[(v,u)]
        if a==b:
            return False
        dual[a].add(b);dual[b].add(a)
    colors={}
    for root in range(nfaces):
        if root in colors:
            continue
        colors[root]=0;todo=[root]
        for f in todo:
            for g in dual[f]:
                if g not in colors:
                    colors[g]=1-colors[f];todo.append(g)
                elif colors[g]==colors[f]:
                    return False
    return True


def audit_planarity():
    count=connected_count=planar_count=0
    for n in range(1,6):
        all_e=edge_pairs(n)
        for mask in range(1<<len(all_e)):
            edges=[e for i,e in enumerate(all_e) if mask>>i&1]
            count+=1
            if not is_connected(n,edges):
                continue
            connected_count+=1
            faces,face_of=planar_rotation(n,edges)
            if faces is None:
                assert n>=5
                continue
            planar_count+=1
            m=len(edges)
            assert n-m+len(faces)==2
            if n>=3:
                assert m<=3*n-6,(n,edges,"planar bound")
            adj=[set() for _ in range(n)]
            for u,v in edges:adj[u].add(v);adj[v].add(u)
            # Exhaustive vertex bipartitions, rather than relying on a BFS oracle.
            is_bip=any(all(colors[u]!=colors[v] for u,v in edges)
                       for colors in product((0,1),repeat=n))
            if is_bip and n>=3:
                assert m<=2*n-4,(n,edges,"bipartite planar bound")
            eulerian=all(len(row)%2==0 for row in adj)
            face_two_color=dual_faces_two_color(edges,len(faces),face_of)
            assert face_two_color==eulerian,(
                n,edges,eulerian,face_two_color,"face coloring"
            )
    assert planar_rotation(5,edge_pairs(5))[0] is None
    assert planar_rotation(5,edge_pairs(5)[:-1])[0] is not None
    k33=[(i,j) for i in range(3) for j in range(3,6)]
    assert planar_rotation(6,k33)[0] is None
    # Two triangles meeting at a vertex: Eulerian, two-colorable faces.
    butterfly=[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)]
    faces,face_of=planar_rotation(5,butterfly)
    assert faces is not None and dual_faces_two_color(butterfly,len(faces),face_of)
    return count,connected_count,planar_count


def source_integration():
    c=json.loads((ROOT/"catalog/books.json").read_text(encoding="utf-8"))
    book=next(x for x in c["books"] if x["id"]=="graph_and_knot_theory")
    assert len(book["chapters"])==44
    source={
        i:(ROOT/next(p for p in book["chapters"] if Path(p).name.startswith(i+"-")))
        .read_text(encoding="utf-8")
        for i in ("05","07","08","09","12","19")
    }
    assert r"\tau_V(G)" in source["05"] and r"\tau(G)" not in source["05"]
    assert r"\tau(G)" in source["08"] and r"\tau(G)" in source["12"]
    assert r"rem:tg-laplacian-conventions" in source["08"]
    for i in ("07","08","09"):
        assert source[i].count(r"\begin{proof}")==source[i].count(r"\end{proof}")
        assert source[i].count(r"\begin{tikzpicture}")==source[i].count(r"\end{tikzpicture}")
    assert r"thm:tg-free-pi1" in source["07"]
    assert r"thm:tg-kirchhoff" in source["08"]
    assert r"thm:tg-euler-plane" in source["09"]
    assert "Dwukolorowanie ścian bez dwudzielności grafu" in source["09"]


if __name__=="__main__":
    source_integration()
    graph_count=0
    for n in range(1,6):
        e=edge_pairs(n)
        for mask in range(1<<len(e)):
            edges=[edge for i,edge in enumerate(e) if mask>>i&1]
            audit_kirchhoff(n,edges)
            graph_count+=1
    print("PASS 07: covers, Euler characteristic, Nielsen-Schreier:",audit_covers())
    print("PASS TG07-PERM-01 cases, connected, deck automorphisms:",audit_permutation_covers())
    print("PASS TG07-UC-01 graphs, roots, vertices, incidences:",audit_universal_cover_prefixes())
    print("PASS TG07-RAD-01 exact radial contraction checks:",audit_radial_contraction())
    print("PASS TG07-MET-01 graphs, points, distances:",audit_length_metric())
    print("PASS TG07-NORM-01 cases, connected, incidences:",audit_cover_tree_normalization())
    print("PASS 08: exact Kirchhoff/Dirichlet/Thomson models:",graph_count)
    print("PASS TG08-FOREST-01 weighted graphs, minors, polynomial values, resistances:",audit_rooted_forests())
    print("PASS TG08-RAY-01 graphs, pairs, changes, equal, additions, equal:",audit_rayleigh_equality())
    print("PASS TG08-DIR-01 graphs, boundaries, singular, solutions:",audit_dirichlet_boundary())
    print("PASS TG08-SPEC-01 graphs, polynomial evaluations:",audit_hodge_spectra())
    print("PASS 09: exhaustive rotations, planar faces and coloring:",audit_planarity())
    print("PASS source conventions, notation and 44-chapter catalog")
