// GKT-18-DUAL-LIN-01: exact F2 incidence regression, not a proof.
function controlDualLinear(){
 const assert=(p,msg)=>{if(!p)throw Error(msg)};
 function cycles(p){let ids=Array(p.length).fill(-1),count=0;for(let i=0;i<p.length;i++)if(ids[i]<0){let j=i;do{ids[j]=count;j=p[j]}while(j!==i);count++}return [count,ids]}
 function rank(rows,m){const basis=Array(m).fill(0);let r=0;for(let x of rows){for(let j=m-1;j>=0&&x;j--)if(x&(1<<j)){if(basis[j])x^=basis[j];else{basis[j]=x;r++;break}}}return r}
 const parity=x=>{let k=0;for(;x;x&=x-1)k^=1;return k};
 let connected=0,sphere=0,higher=0,orth=0,zero=0;
 let genera={};
 function inspect(p,m){const [n,V]=cycles(p),[f,F]=cycles(p.map((_,i)=>p[i^1]));let B=Array(n).fill(0),C=Array(f).fill(0);for(let i=0;i<m;i++){B[V[2*i]]^=1<<i;B[V[2*i+1]]^=1<<i;C[F[2*i]]^=1<<i;C[F[2*i+1]]^=1<<i}if(rank(B,m)!==n-1)return;connected++;
  assert(rank(C,m)===f-1,"dual rank");
  const g=(2-n+m-f)/2;assert(Number.isInteger(g)&&g>=0,"genus");genera[g]=(genera[g]||0)+1;if(g===0)sphere++;else higher++;
  for(const b of B)for(const c of C){orth++;assert(parity(b&c)===0,"boundary of boundary")}
  const dim=m-rank(B,m)-rank(C,m);assert(dim===2*g,"homology dimension");
  // On a sphere, the row space of dual incidence equals primal cycle space.
  if(g===0){let span=new Set([0]);for(const c of C)for(const x of [...span])span.add(x^c);for(let x=0;x<(1<<m);x++){zero++;assert(span.has(x)===B.every(b=>parity(b&x)===0),"dual cut/primal cycle equality")}}
 }
 for(let m=1;m<=4;m++){let p=Array.from({length:2*m},(_,i)=>i);function perm(k){if(k===p.length){inspect(p,m);return}for(let j=k;j<p.length;j++){[p[k],p[j]]=[p[j],p[k]];perm(k+1);[p[k],p[j]]=[p[j],p[k]]}}perm(0)}
 // One vertex and no edges: the sphere has one face, both spaces vanish.
 assert(rank([0],0)===0,"empty graph incidence");
 return {connected,sphere,higher,orth,zero,genera,zeroEdgeCase:1};
}
console.log('PASS GKT-18-DUAL-LIN-01', controlDualLinear());
