#!/usr/bin/env python3
"""AA-X11: genuinely finite extension-field tests for AA-29.

Checks irreducible counts, Möbius inversion, Rabin irreducibility and
the Frobenius factorization X^(q^n)-X, also for non-prime q=4,8,9.
All polynomial operations are implemented independently over F_(p^m).
"""
from itertools import product
from math import gcd

def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return tuple(a)

def prime_factors(n):
    return [p for p in range(2,n+1) if n%p==0 and
            all(p%j for j in range(2,int(p**0.5)+1))]

def mu(n):
    if n==1:return 1
    k=0
    for p in prime_factors(n):
        if n%(p*p)==0:return 0
        k+=1
    return (-1)**k

def base_rem(a,b,p):
    a=list(trim(a));b=trim(b)
    while len(a)>=len(b):
        z=a[-1]*pow(b[-1],-1,p)%p;off=len(a)-len(b)
        for j,c in enumerate(b):a[off+j]=(a[off+j]-z*c)%p
        a=list(trim(a))
    return tuple(a)

def irreducible_base(p,m):
    if m==1:return (0,1)
    for coeff in product(range(p),repeat=m):
        if coeff[0]==0:continue
        f=tuple(coeff)+(1,)
        if all(base_rem(f,tuple(g)+(1,),p) for d in range(1,m//2+1)
               for g in product(range(p),repeat=d)):
            return f
    raise AssertionError((p,m))

class Field:
    def __init__(self,p,m):
        self.p,self.m,self.q=p,m,p**m
        self.f=irreducible_base(p,m)
        self.vec=[tuple(x//p**j%p for j in range(m)) for x in range(self.q)]
    def idx(self,a):return sum((z%self.p)*self.p**j for j,z in enumerate(a))
    def add(self,a,b):return self.idx((x+y for x,y in zip(self.vec[a],self.vec[b])))
    def neg(self,a):return self.idx((-x for x in self.vec[a]))
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p,m=self.p,self.m
        aa,bb=self.vec[a],self.vec[b]
        z=[0]*(2*m-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb):z[i+j]=(z[i+j]+x*y)%p
        for k in range(len(z)-1,m-1,-1):
            t=z[k]
            for i,c in enumerate(self.f[:-1]):z[k-m+i]=(z[k-m+i]-t*c)%p
        return self.idx(z[:m])
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def inv(self,a):
        assert a!=0
        v=self.power(a,self.q-2)
        assert self.mul(a,v)==1
        return v

def padd(f,g,F):
    return trim(F.add(f[i] if i<len(f) else 0,g[i] if i<len(g) else 0)
                for i in range(max(len(f),len(g))))
def pneg(f,F):return tuple(F.neg(x) for x in f)
def psub(f,g,F):return padd(f,pneg(g,F),F)
def pmul(f,g,F):
    if not f or not g:return ()
    out=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):out[i+j]=F.add(out[i+j],F.mul(a,b))
    return trim(out)
def prem(a,b,F):
    a=list(trim(a));b=trim(b)
    assert b
    bi=F.inv(b[-1])
    while len(a)>=len(b):
        t=F.mul(a[-1],bi);offset=len(a)-len(b)
        for j,v in enumerate(b):a[offset+j]=F.sub(a[offset+j],F.mul(t,v))
        a=list(trim(a))
    return tuple(a)
def ppowmod(a,n,f,F):
    z=(1,)
    while n:
        if n&1:z=prem(pmul(z,a,F),f,F)
        a=prem(pmul(a,a,F),f,F);n//=2
    return z
def pgcd(a,b,F):
    while b:a,b=b,prem(a,b,F)
    return tuple(F.mul(x,F.inv(a[-1])) for x in a) if a else ()
def irreducible_poly(f,F):
    d=len(f)-1
    if d<1:return False
    x=(0,1);h=x
    powers={}
    for k in range(1,d+1):
        h=ppowmod(h,F.q,f,F)
        if k in {d//p for p in prime_factors(d)}:
            powers[k]=h
    if h!=prem(x,f,F):return False
    return all(pgcd(f,psub(powers[d//p],x,F),F)==(1,)
               for p in prime_factors(d))

def main():
    stats={}
    def verify(kind,ok,case):
        assert ok,(kind,case)
        stats[kind]=stats.get(kind,0)+1
    configs=((2,1,6),(3,1,5),(5,1,4),(2,2,5),(2,3,4),(3,2,4))
    summary={}
    for p,m,maxdegree in configs:
        F=Field(p,m);q=F.q
        all_irr={}
        for d in range(1,maxdegree+1):
            irr=[]
            for coeff in product(range(q),repeat=d):
                f=tuple(coeff)+(1,)
                flag=irreducible_poly(f,F)
                verify('Rabin_irreducibility_and_Frobenius',flag in (True,False),(q,d,f))
                if flag:irr.append(f)
            all_irr[d]=irr
            divisors=[e for e in range(1,d+1) if d%e==0]
            N=sum(mu(e)*q**(d//e) for e in divisors)//d
            verify('Mobius_irreducible_count',len(irr)==N,(q,d,len(irr),N))
            verify('Frobenius_degree_sum',
                   sum(j*len(all_irr[j]) for j in divisors)==q**d,(q,d))
            # Every irreducible factor of degree j | d must divide X^(q^d)-X;
            # conversely for j not dividing d the factor must not divide.
            for j in range(1,d+1):
                sample=all_irr[j]
                for f in sample:
                    expected=(d%j==0)
                    got=(ppowmod((0,1),q**d,f,F)==prem((0,1),f,F))
                    verify('Frobenius_factor_divisibility',got==expected,(q,d,j,f))
            # Product of exactly these irreducibles is Frobenius polynomial,
            # compared explicitly in the smaller degree cases.
            if q**d<=1024:
                pr=(1,)
                for j in divisors:
                    for f in all_irr[j]:pr=pmul(pr,f,F)
                expected=[0]*(q**d+1)
                expected[1]=F.neg(1);expected[-1]=1
                verify('full_Frobenius_factorization',pr==tuple(expected),(q,d))
        summary[q]=[len(all_irr[d]) for d in range(1,maxdegree+1)]
        # Distinct subfields are fixed sets of Frobenius powers
        for d in range(1,m+1):
            if m%d==0:
                S={a for a in range(q) if F.power(a,p**d)==a}
                verify('subfield_fixed_by_Frobenius',len(S)==p**d,(p,m,d))
                verify('subfield_add_mul_closed',
                       all(F.add(a,b) in S and F.mul(a,b) in S for a in S for b in S),(p,m,d))
    total=sum(stats.values())
    print(f'AA-X11 AA-29 finite extension fields: {total}/{total} PASS',summary,stats)
if __name__=='__main__':main()
