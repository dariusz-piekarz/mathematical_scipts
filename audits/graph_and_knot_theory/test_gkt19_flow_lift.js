// GKT-19-LIFT-01: signed face differences and constructive lifting via complementary trees.
// Exhaustive rotation systems with at most three edges, including composite moduli.
// Run from repo root: node audits/graph_and_knot_theory/test_gkt19_flow_lift.js
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 function cycles(p){let ids=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(ids[i]<0){let d=i;do{ids[d]=n;d=p[d]}while(d!==i);n++}return {ids,n}}
 let models=0,orientationChecks=0,faceColumns=0,lifts=0,compositeLifts=0;
 function inspect(n,f,E,F){
 const m=E.length,p=Array.from({length:n},(_,i)=>i),T=new Set();function root(x){while(p[x]!==x)x=p[x];return x}
 for(let e=0;e<m;e++){let [u,v]=E[e],a=root(u),b=root(v);if(a!==b){p[a]=b;T.add(e)}}
 if(T.size!==n-1||n-m+f!==2)return;
 models++;
 for(let flip=0;flip<2**m;flip++){
 const edges=E.map(([u,v],i)=>flip>>i&1?[v,u]:[u,v]);
 const faces=F.map(([r,l],i)=>flip>>i&1?[l,r]:[r,l]);
 const adj=Array.from({length:f},()=>[]);
 for(let e=0;e<m;e++)if(!T.has(e)){let [r,l]=faces[e];assert(r!==l,"dual tree loop");adj[l].push([r,e,1]);adj[r].push([l,e,-1])}
 const parent=Array(f).fill(-1),order=[0];parent[0]=0;
 for(let i=0;i<order.length;i++)for(let [v] of adj[order[i]])if(parent[v]<0){parent[v]=order[i];order.push(v)}
 assert(order.length===f&&m-T.size===f-1,"complementary tree");
 function boundary(j){let b=Array(n).fill(0);edges.forEach(([u,v],i)=>{b[u]-=j[i];b[v]+=j[i]});return b}
 for(let h=0;h<f;h++){let j=faces.map(([r,l])=>Number(r===h)-Number(l===h));assert(boundary(j).every(x=>x===0),"signed face column");faceColumns++}
 orientationChecks++;
 for(let q of [2,3,4,6]){
 const mod=x=>((x%q)+q)%q,j=Array(m).fill(0);
 function enumerate(i){
 if(i<m){for(let x=0;x<q;x++){j[i]=x;enumerate(i+1)}return}
 if(!boundary(j).every(x=>mod(x)===0))return;
 const c=Array(f).fill(null);c[0]=0;
 for(let u of order)for(let [v,e,sgn] of adj[u])if(c[v]===null)c[v]=mod(c[u]+sgn*j[e]);
 assert(faces.every(([r,l],e)=>mod(c[r]-c[l])===j[e]),"flow reconstruction");
 for(let a=0;a<q;a++)assert(faces.every(([r,l],e)=>mod(mod(c[r]+a)-mod(c[l]+a))===j[e]),"constant shift");
 lifts++;compositeLifts+=q===4||q===6;
 }
 enumerate(0);
 }
 }
 }
 inspect(1,1,[],[]);
 function perm(s,k){if(k===s.length){let v=cycles(s),f=cycles(s.map((_,d)=>s[d^1]));let E=[],F=[];for(let i=0;i<s.length;i+=2){E.push([v.ids[i],v.ids[i+1]]);F.push([f.ids[i],f.ids[i+1]])}inspect(v.n,f.n,E,F);return}for(let i=k;i<s.length;i++){[s[k],s[i]]=[s[i],s[k]];perm(s,k+1);[s[k],s[i]]=[s[i],s[k]]}}
 for(let m=1;m<=3;m++)perm(Array.from({length:2*m},(_,i)=>i),0);
 assert(models===453&&compositeLifts>0,"coverage");
 return {models,orientationChecks,faceColumns,lifts,compositeLifts};
}
console.log(JSON.stringify(run()));
