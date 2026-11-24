// AA-63: exact conjugated Cartan models in sl_n.
function conjugacy63(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const z=n=>Array.from({length:n},()=>Array(n).fill(0n));
 const add=(a,b)=>a.map((r,i)=>r.map((v,j)=>v+b[i][j]));
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,v,k)=>s+v*b[k][j],0n)));
 const sc=(a,c)=>a.map(r=>r.map(v=>v*c));const br=(a,b)=>add(mul(a,b),sc(mul(b,a),-1n));
 const eq=(a,b)=>a.every((r,i)=>r.every((v,j)=>v===b[i][j]));
 const I=n=>z(n).map((r,i)=>r.map((v,j)=>i===j?1n:0n));
 const unit=(n,i,j)=>{const a=z(n);a[i][j]=1n;return a;};
 const diag=v=>v.map((x,i)=>v.map((_,j)=>i===j?x:0n));
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
 const rank=ms=>{let rows=[];for(const M of ms){let v=M.flat();for(const [p,w] of rows){if(!v[p])continue;const a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);const d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}const p=v.findIndex(x=>x!==0n);if(p>=0)rows.push([p,v]);}return rows.length};
 let models=0,jacobians=0,centralizers=0,rootchecks=0,expchecks=0;
 for(let n=2;n<=6;n++){
  const D=Array.from({length:n-1},(_,i)=>add(unit(n,i,i),sc(unit(n,n-1,n-1),-1n)));
  const R=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)R.push([i,j,unit(n,i,j)]);
  for(let trial=0;trial<3;trial++){
   let U=I(n),V=I(n);for(let k=0;k<n+2;k++){const i=k%n,j=(i+trial+1)%n;if(i===j)continue;let X=unit(n,i,j),c=BigInt(k+1);U=mul(add(I(n),sc(X,c)),U);V=mul(V,add(I(n),sc(X,-c)));}
   assert(eq(mul(U,V),I(n)),"inverse");
   const conj=X=>mul(mul(U,X),V);
   const vals=Array.from({length:n},(_,i)=>BigInt(2*i-n+1)),t=conj(diag(vals)),H=D.map(conj),roots=R.map(([i,j,X])=>[i,j,conj(X)]);
   const base=[...H,...roots.map(r=>r[2])];assert(rank(base)===n*n-1,"basis");
   const deriv=roots.map(([i,j,X])=>{assert(eq(br(X,t),sc(X,vals[j]-vals[i])),"root direction");rootchecks++;return br(X,t)});
   assert(rank([...H,...deriv])===n*n-1,"Jacobian rank");jacobians++;
   assert(rank(base.map(X=>br(t,X)))===n*n-n,"centralizer dimension");assert(H.every(X=>eq(br(t,X),z(n))),"centralizer");centralizers++;
   for(const [i,j,X] of roots){let c=3n;const E=add(I(n),sc(X,c)),Ei=add(I(n),sc(X,-c));const ad=br(X,t),ad2=br(X,ad);
    assert(eq(br(X,ad2),z(n)),"nilpotence on t");assert(eq(mul(mul(E,t),Ei),add(add(t,sc(ad,c)),sc(ad2,c*c/2n))),"exponential");expchecks++;}
   models++;
  }
 }
 return {models,jacobians,centralizers,rootchecks,expchecks};
}
console.log('AA-63 conjugacy models: PASS',conjugacy63());
