// GKT-28-JSJ-GRAPH-01: exhaustive multigraph gluing combinatorics.
function graphControl(){
const ck=(x,m)=>{if(!x)throw Error(m)};
let graphs=0,connected=0,edgeChecks=0,trees=0,orders=0,loops=0,parallel=0;
for(let n=1;n<=4;n++){
const types=[];for(let i=0;i<n;i++)for(let j=i;j<n;j++)types.push([i,j]);
function components(E){const p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};let count=n;for(const [u,v] of E){let a=root(u),b=root(v);if(a!==b){p[b]=a;count--}}return count}
function check(E){graphs++;if(components(E)!==1)return;connected++;if(E.some(([a,b])=>a===b))loops++;if(new Set(E.map(x=>x.join(","))).size<E.length)parallel++;
let bridge=E.map((_,i)=>components(E.filter((_,j)=>i!==j))>1);
const allTrees=[];for(let mask=0;mask<(1<<E.length);mask++){let I=E.map((_,i)=>i).filter(i=>mask>>i&1);if(I.length!==n-1||components(I.map(i=>E[i]))!==1)continue;allTrees.push(I);trees++;for(const J of [I,[...I].reverse()]){const partial=[];for(const i of J){const b=components(partial);partial.push(E[i]);ck(components(partial)===b-1,"tree glue");orders++}ck(components(partial)===1,"tree connected");let remaining=E.map((_,i)=>i).filter(i=>!I.includes(i));ck(remaining.length===E.length-n+1,"HNN count");for(const i of remaining){partial.push(E[i]);ck(components(partial)===1,"HNN glue");orders++}}}
ck(allTrees.length>0,"spanning tree exists");
for(let i=0;i<E.length;i++){ck(bridge[i]===allTrees.every(T=>T.includes(i)),"bridge iff all trees");ck(components(E.filter((_,j)=>i!==j))===(bridge[i]?2:1),"cut components");edgeChecks++}}
function generate(E,start){check(E);if(E.length===6)return;for(let i=start;i<types.length;i++)generate([...E,types[i]],i)}generate([],0)
}return {graphs,connected,edgeChecks,trees,orders,loops,parallel}}
console.log('PASS GKT-28-JSJ-GRAPH-01', graphControl());
