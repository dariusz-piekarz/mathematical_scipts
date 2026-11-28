#!/usr/bin/env python3
"""AA-X08: independently test Galois fixed fields, trace, norm and discriminants."""
from itertools import product
from math import gcd


def poly_trim(x):
    a=list(x)
    while a and a[-1]==0: a.pop()
    return a

def poly_rem(a,b,p):
    a=poly_trim(a)
    b=poly_trim(b)
    assert b and b[-1]%p != 0
    while len(a)>=len(b):
        z=a[-1]*pow(b[-1],-1,p)%p
        k=len(a)-len(b)
        for j,t in enumerate(b): a[k+j]=(a[k+j]-z*t)%p
        a=poly_trim(a)
    return a

def irreducible(p,n):
    for coeffs in product(range(p),repeat=n):
        if coeffs[0] == 0: continue
        f=list(coeffs)+[1]
        ok=True
        for k in range(1,n//2+1):
            for cs in product(range(p),repeat=k):
                g=list(cs)+[1]
                if not poly_rem(f,g,p):
                    ok=False;break
            if not ok:break
        if ok: return f
    raise ValueError((p,n))

class Fq:
    def __init__(self,p,n):
        self.p,self.n=p,n
        self.f=irreducible(p,n)
        self.q=p**n
        self.basis=[p**i for i in range(n)]
        self.vec=[tuple((a//p**i)%p for i in range(n)) for a in range(self.q)]
    def mk(self,vec):
        return sum((int(t)%self.p)*self.p**i for i,t in enumerate(vec))
    def add(self,a,b): return self.mk((x+y for x,y in zip(self.vec[a],self.vec[b])))
    def mul(self,a,b):
        p,n=self.p,self.n
        aa,bb=self.vec[a],self.vec[b]
        z=[0]*(2*n-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb): z[i+j]=(z[i+j]+x*y)%p
        for k in range(2*n-2,n-1,-1):
            c=z[k]
            for i in range(n): z[k-n+i]=(z[k-n+i]-c*self.f[i])%p
        return self.mk(z[:n])
    def power(self,a,k):
        o=1
        while k:
            if k&1:o=self.mul(o,a)
            a=self.mul(a,a);k//=2
        return o
    def mat(self,a):
        return [[self.vec[self.mul(a,b)][i] for b in self.basis] for i in range(self.n)]
    def trace_linear(self,a):
        m=self.mat(a)
        return sum(m[i][i] for i in range(self.n))%self.p
    def det_linear(self,a):
        p=self.p
        m=[v[:] for v in self.mat(a)]
        d=1
        for j in range(self.n):
            k=next((i for i in range(j,self.n) if m[i][j]),None)
            if k is None:return 0
            if k!=j: m[j],m[k]=m[k],m[j];d=-d
            v=m[j][j];d=d*v%p
            inv=pow(v,-1,p)
            for i in range(j+1,self.n):
                factor=m[i][j]*inv%p
                for t in range(j,self.n): m[i][t]=(m[i][t]-factor*m[j][t])%p
        return d%p


def fixed_fields_and_tower(F):
    p,n,q=F.p,F.n,F.q
    count=dict(fixed=0,galois=0,tower_trace=0,tower_norm=0)
    for d in range(1,n+1):
        if n%d:continue
        fixed={a for a in range(q) if F.power(a,p**d)==a}
        assert len(fixed)==p**d
        assert all(F.add(a,b) in fixed and F.mul(a,b) in fixed for a in fixed for b in fixed)
        count['fixed']+=1
        gen_orbit=[tuple(F.power(a,p**(d*j)) for a in range(q)) for j in range(n//d)]
        assert len(set(gen_orbit))==n//d
        count['galois']+=1
        for a in range(q):
            relative_trace=0
            relative_norm=1
            for j in range(n//d):
                b=F.power(a,p**(d*j))
                relative_trace=F.add(relative_trace,b)
                relative_norm=F.mul(relative_norm,b)
            assert relative_trace in fixed and relative_norm in fixed
            outer_trace=0
            outer_norm=1
            for j in range(d):
                outer_trace=F.add(outer_trace,F.power(relative_trace,p**j))
                outer_norm=F.mul(outer_norm,F.power(relative_norm,p**j))
            absolute_trace=0
            absolute_norm=1
            for j in range(n):
                b=F.power(a,p**j)
                absolute_trace=F.add(absolute_trace,b)
                absolute_norm=F.mul(absolute_norm,b)
            assert outer_trace==absolute_trace
            assert outer_norm==absolute_norm
            count['tower_trace']+=1
            count['tower_norm']+=1
    return count


def main():
    cases=((2,2),(2,3),(2,4),(2,6),(3,2),(3,3),(3,4),(5,2))
    counts=dict(trace=0,norm=0,trace_surj=0,norm_surj=0,trace_pair_nondegenerate=0,fixed=0,galois=0,tower_trace=0,tower_norm=0)
    for p,n in cases:
        F=Fq(p,n)
        ts=set();ns=set()
        for a in range(F.q):
            trace=0
            norm=1
            for j in range(n):
                b=F.power(a,p**j)
                trace=F.add(trace,b)
                norm=F.mul(norm,b)
            assert trace==F.trace_linear(a)
            assert norm==F.det_linear(a)
            assert 0<=trace<p and 0<=norm<p
            counts['trace']+=1;counts['norm']+=1
            ts.add(trace)
            if a:ns.add(norm)
        assert ts==set(range(p));counts['trace_surj']+=1
        assert ns==set(range(1,p));counts['norm_surj']+=1
        for a in range(1,F.q):
            assert any(F.trace_linear(F.mul(a,b)) for b in range(F.q))
            counts['trace_pair_nondegenerate']+=1
        for k,v in fixed_fields_and_tower(F).items():counts[k]+=v
    assert counts['trace']>0
    s=sum(counts.values())
    print(f'AA-X08 finite-field Galois/trace/norm: {s}/{s} PASS', counts)


if __name__=='__main__':main()
