// GKT-19-RANK-01: F2 incidence rank and kernel cardinality, independent of forest enumeration.
// Run from root: node audits/graph_and_knot_theory/test_gkt19_rank.js
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 let graphs=0,subsets=0,zero=0,kernels=0,loops=0,parallel=0;
 function inspect(n,E){
 graphs++;loops+=E.some(([u,v])=>u===v);parallel+=new Set(E.map(e=>e.join(","))).size<E.length;
 for(let a=0;a<2**E.length;a++){
 const S=E.filter((_,i)=>a>>i&1),cols=S.map(([u,v])=>(1<<u)^(1<<v));
 const adj=Array.from({length:n},()=>[]);for(let [u,v] of S){adj[u].push(v);adj[v].push(u)}
 let seen=new Set(),k=0;for(let i=0;i<n;i++)if(!seen.has(i)){k++;let stack=[i];seen.add(i);while(stack.length)for(let v of adj[stack.pop()])if(!seen.has(v)){seen.add(v);stack.push(v)}}
 let basis=Array(n).fill(0),rank=0;for(let col of cols){let z=col;for(let b=n-1;b>=0;b--)if(z>>b&1){if(basis[b])z^=basis[b];else{basis[b]=z;rank++;break}}}
 assert(rank===n-k,"rank over F2");let nullity=S.length-rank;assert(nullity===S.length-n+k,"nullity");
 let count=0;for(let b=0;b<2**S.length;b++){let z=0;for(let i=0;i<S.length;i++)if(b>>i&1)z^=cols[i];if(!z)count++}
 assert(count===2**nullity,"kernel size");
 // A forest has no loops/parallel edges and each connected component is a tree.
 let simple=new Set(),forest=true;for(let [u,v] of S){let key=u+","+v;if(u===v||simple.has(key))forest=false;simple.add(key)}
 // Independently detect a cycle by asking whether any nonloop edge can be bypassed.
 for(let i=0;i<S.length&&forest;i++){let [u,v]=S[i],reach=new Set([u]),stack=[u];while(stack.length){let w=stack.pop();for(let j=0;j<S.length;j++)if(j!==i){let [x,y]=S[j],t=x===w?y:y===w?x:-1;if(t>=0&&!reach.has(t)){reach.add(t);stack.push(t)}}}if(reach.has(v))forest=false}
 assert((nullity===0)===forest,"zero nullity iff forest");
 zero+=forest;kernels+=count;subsets++;
 }
 }
 for(let n=0;n<=4;n++){let es=[];for(let u=0;u<n;u++)for(let v=u;v<n;v++)es.push([u,v]);function go(E,i){inspect(n,E);if(E.length===5)return;for(let j=i;j<es.length;j++)go([...E,es[j]],j)}go([],0)}
 assert(graphs===3528&&subsets===89217,"coverage");return {graphs,subsets,zero,kernels,loops,parallel};
}
console.log(JSON.stringify(run()));
