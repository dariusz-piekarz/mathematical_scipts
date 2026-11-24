// GKT-18-ORIENT-01: both dual conventions and oriented cellular boundaries.
// Finite rotation models, not a proof of geometric duality.
function run(){
  const assert=(x,m)=>{if(!x)throw Error(m)};
  function inv(p){let q=[];p.forEach((x,i)=>q[x]=i);return q}
  function cycles(p){let idx=Array(p.length).fill(-1),cs=[];for(let i=0;i<p.length;i++)if(idx[i]<0){let d=i,c=[];do{assert(idx[d]<0,"cycle");idx[d]=cs.length;c.push(d);d=p[d]}while(d!==i);cs.push(c)}return {idx,cs}}
  let total=0,connected=0,signChecks=0;
  function inspect(s){
    total++;let D=s.length,m=D/2,V=cycles(s),v=V.idx,phi=s.map((_,d)=>s[d^1]),F=cycles(phi);
    let seen=new Set([0]),q=[0];for(let d of q)for(let x of [s[d],d^1])if(!seen.has(x)){seen.add(x);q.push(x)}if(seen.size!==D)return;connected++;
    let dual=inv(phi),df=dual.map((_,d)=>dual[d^1]),dd=inv(df),dv=cycles(df).idx;
    assert(phi.every((_,d)=>phi[d^1]===s[d]),"reversed dual squared");
    assert(dd.every((x,d)=>x===(s[d^1]^1)),"oriented dual squared");
    for(let a=0;a<D;a++)for(let b=0;b<D;b++)assert((dv[a]===dv[b])===(v[a^1]===v[b^1]),"dual faces");
    for(let i=0;i<F.cs.length;i++){
      let positive=F.cs[i].slice().reverse().map(d=>d^1),coeff=Array(m).fill(0),div=Array(V.cs.length).fill(0);
      positive.forEach((d,j)=>{assert(v[d^1]===v[positive[(j+1)%positive.length]],"positive walk");coeff[d>>1]+=d%2===0?1:-1});
      for(let e=0;e<m;e++){assert(coeff[e]===Number(F.idx[2*e+1]===i)-Number(F.idx[2*e]===i),"positive signs");div[v[2*e]]-=coeff[e];div[v[2*e+1]]+=coeff[e]}
      assert(div.every(x=>x===0),"boundary squared");signChecks++;
    }
  }
  function perm(a,k){if(k===a.length){inspect(a);return}for(let j=k;j<a.length;j++){[a[k],a[j]]=[a[j],a[k]];perm(a,k+1);[a[k],a[j]]=[a[j],a[k]]}}
  for(let m=1;m<=3;m++)perm(Array.from({length:2*m},(_,i)=>i),0);
  let state=172;function rnd(n){state=(Math.imul(state,1664525)+1013904223)>>>0;return state%n}
  for(let m=4;m<=9;m++)for(let i=0;i<300;i++){let a=Array.from({length:2*m},(_,j)=>j);for(let j=a.length-1;j>0;j--){let k=rnd(j+1);[a[j],a[k]]=[a[k],a[j]]}inspect(a)}
  return {total,connected,signChecks};
}
console.log(JSON.stringify(run()));
