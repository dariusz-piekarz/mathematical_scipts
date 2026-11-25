// GKT-19-KIRCH-01: compare weighted simple-tree count, multigraph tree count,
// and each exact Laplacian cofactor. Run from root: node audits/graph_and_knot_theory/test_gkt19_kirchhoff.js
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 function det(M){if(!M.length)return 1n;let d=0n;for(let j=0;j<M.length;j++){let C=M.slice(1).map(r=>r.filter((_,i)=>i!==j));d+=(j%2?-1n:1n)*M[0][j]*det(C)}return d}
 function trees(n,E,weighted){let ans=0n;for(let mask=0;mask<2**E.length;mask++){let p=Array.from({length:n},(_,i)=>i),k=n,prod=1n;function root(x){while(p[x]!==x)x=p[x];return x}let ok=true;for(let i=0;i<E.length;i++)if(mask>>i&1){let [u,v,w]=E[i],a=root(u),b=root(v);if(a===b){ok=false;break}p[a]=b;k--;prod*=weighted?BigInt(w):1n}if(ok&&k===1)ans+=prod}return ans}
 let graphs=0,connected=0,cofactors=0,loops=0,parallel=0;
 function inspect(n,E){graphs++;let a=trees(n,E,false);if(!a)return;connected++;
 loops+=E.some(([u,v])=>u===v);const W=new Map();for(let [u,v] of E)if(u!==v){let key=u+","+v;W.set(key,(W.get(key)||0)+1)}
 let F=[...W].map(([k,w])=>[...k.split(",").map(Number),w]);parallel+=F.some(e=>e[2]>1);assert(a===trees(n,F,true),"weighted enumeration");
 let L=Array.from({length:n},()=>Array(n).fill(0n));for(let [u,v] of E){L[u][u]++;L[v][v]++;L[u][v]--;L[v][u]--}
 let K=Array.from({length:n},()=>Array(n).fill(0n));for(let [u,v,w] of F){let z=BigInt(w);K[u][u]+=z;K[v][v]+=z;K[u][v]-=z;K[v][u]-=z}
 assert(L.every((r,i)=>r.every((v,j)=>v===K[i][j])),"weighted Laplacian");
 for(let r=0;r<n;r++){assert(det(L.filter((_,i)=>i!==r).map(row=>row.filter((_,j)=>j!==r)))===a,"exact cofactor");cofactors++}
 }
 for(let n=1;n<=4;n++){let es=[];for(let u=0;u<n;u++)for(let v=u;v<n;v++)es.push([u,v]);function go(E,k){inspect(n,E);if(E.length===5)return;for(let i=k;i<es.length;i++)go([...E,es[i]],i)}go([],0)}
 assert(loops&&parallel,"coverage");return {graphs,connected,cofactors,loops,parallel};
}
console.log(JSON.stringify(run()));
