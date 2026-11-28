// GKT-18-TC-01: finite orientable rotation systems, duality and integral tree-cotree reduction.
// All permutations for 2,4,6 darts, deterministic samples for 8–18 darts; fixed pairing d^1.
// Run with Node.js. Finite tests, not formal proof.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 function cycles(p){let seen=new Set(),cs=[];for(let i=0;i<p.length;i++)if(!seen.has(i)){let c=[],j=i;do{assert(!seen.has(j),"permutation");seen.add(j);c.push(j);j=p[j]}while(j!==i);cs.push(c)}return cs}
 function index(cs,n){let x=Array(n);cs.forEach((c,i)=>c.forEach(d=>x[d]=i));return x}
 function tree(n,edges,order){let p=Array.from({length:n},(_,i)=>i);function root(x){while(p[x]!==x)x=p[x];return x}let T=[];for(let e of order){let [u,v]=edges[e],a=root(u),b=root(v);if(a!==b){p[a]=b;T.push(e)}}return T}
 let total=0,connected=0,positiveGenus=0,loops=0,parallel=0,oneFace=0,decomps=0,basis=0,relations=0;
 function inspect(sigma){
   total++;let m=sigma.length/2,D=2*m,vs=cycles(sigma),v=index(vs,D),phi=sigma.map((_,d)=>sigma[d^1]),fs=cycles(phi),f=index(fs,D);
   let E=Array.from({length:m},(_,e)=>[v[2*e],v[2*e+1]]),F=Array.from({length:m},(_,e)=>[f[2*e],f[2*e+1]]),order=Array.from({length:m},(_,i)=>i);
   let T0=tree(vs.length,E,order);if(T0.length!==vs.length-1)return;
   connected++;let g=(2-vs.length+m-fs.length)/2;assert(g>=0&&Number.isInteger(g),"genus");
   positiveGenus+=g>0;loops+=E.some(([u,w])=>u===w);parallel+=new Set(E.map(([u,w])=>[Math.min(u,w),Math.max(u,w)].join(","))).size<m;oneFace+=fs.length===1;
   assert(phi.every((_,d)=>phi[d^1]===sigma[d]),"double dual");
   let boundary=a=>F.map(([i,j])=>a[i]-a[j]);
   let divergence=z=>{let d=Array(vs.length).fill(0);E.forEach(([u,w],e)=>{d[u]-=z[e];d[w]+=z[e]});return d};
   for(let i=0;i<fs.length;i++){let a=Array(fs.length).fill(0);a[i]=1;assert(divergence(boundary(a)).every(x=>x===0),"boundary squared")}
   for(let ord of [order,order.slice().reverse()]){
     let T=tree(vs.length,E,ord),off=ord.filter(e=>!T.includes(e)),B=tree(fs.length,F,off),L=off.filter(e=>!B.includes(e));
     assert(T.length===vs.length-1&&B.length===fs.length-1&&L.length===2*g,"tree-cotree");
     decomps++;
     let adj=Array.from({length:vs.length},()=>[]);for(let e of T){let[u,w]=E[e];adj[u].push([w,e,1]);adj[w].push([u,e,-1])}
     function fundamental(e){let[u,w]=E[e],z=Array(m).fill(0);z[e]=1;function path(x,prev){if(x===u)return true;for(let[y,k,sign]of adj[x])if(y!==prev&&path(y,x)){z[k]=sign;return true}return false}assert(path(w,-1),"tree path");return z}
     let zs=off.map(fundamental);
     zs.forEach((z,i)=>{assert(divergence(z).every(x=>!x),"fundamental cycle");assert(off.every((e,j)=>z[e]===(i===j?1:0)),"coordinate basis")});
     let dualAdj=Array.from({length:fs.length},()=>[]);for(let e of B){let[i,j]=F[e];dualAdj[i].push([j,e,-1]);dualAdj[j].push([i,e,1])}
     function potential(b){let a=Array(fs.length).fill(null);a[0]=0;let q=[0];for(let i of q)for(let[j,e,sgn]of dualAdj[i])if(a[j]===null){a[j]=a[i]+sgn*b[e];q.push(j)}assert(a.every(x=>x!==null),"dual tree connectivity");assert(B.every(e=>a[F[e][0]]-a[F[e][1]]===b[e]),"integer solve");return a}
     function normal(z){let b=boundary(potential(z));assert(B.every(e=>z[e]===b[e]),"elimination");return L.map(e=>z[e]-b[e])}
     for(let i=0;i<fs.length;i++){let a=Array(fs.length).fill(0);a[i]=1;assert(normal(boundary(a)).every(x=>x===0),"boundary killed");relations++}
     for(let i=0;i<L.length;i++){let z=fundamental(L[i]);assert(normal(z).every((x,j)=>x===(i===j?1:0)),"integral quotient basis");basis++}
     let z=Array(m).fill(0);zs.forEach((w,i)=>w.forEach((x,j)=>z[j]+=(i%5-2)*x));let b=boundary(potential(z)),rest=z.map((x,i)=>x-b[i]);let coeff=normal(z),reconstructed=Array(m).fill(0);L.forEach((e,i)=>fundamental(e).forEach((x,j)=>reconstructed[j]+=coeff[i]*x));
     assert(rest.every((x,i)=>x===reconstructed[i]),"integral reconstruction");
   }
 }
 function perm(a,k){if(k===a.length){inspect(a.slice());return}for(let j=k;j<a.length;j++){[a[k],a[j]]=[a[j],a[k]];perm(a,k+1);[a[k],a[j]]=[a[j],a[k]]}}
 for(let m=1;m<=3;m++)perm(Array.from({length:2*m},(_,i)=>i),0);
 let state=172;function rnd(n){state=(Math.imul(state,1664525)+1013904223)>>>0;return state%n}
 for(let m=4;m<=9;m++)for(let i=0;i<300;i++){let a=Array.from({length:2*m},(_,j)=>j);for(let j=a.length-1;j>0;j--){let k=rnd(j+1);[a[j],a[k]]=[a[k],a[j]]}inspect(a)}
 assert(positiveGenus&&loops&&parallel&&oneFace&&basis,"coverage");
 return {total,connected,positiveGenus,loops,parallel,oneFace,decomps,basis,relations};
}
console.log(JSON.stringify(run()));
