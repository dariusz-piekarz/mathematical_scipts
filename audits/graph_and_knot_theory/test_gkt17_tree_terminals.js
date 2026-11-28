// GKT-17-TREE-01. Run: node audits/graph_and_knot_theory/test_gkt17_tree_terminals.js
// Exhaustive labelled trees via Prüfer codes, n<=6, terminal multisets of size 3 or 4.
// Checks actual path intersections and 2+2 cuts independently. Not a formal proof.
function run(){
 let trees=0,cases=0,star=0,split=0,repeated=0;
 for(let n=1;n<=6;n++){
  function inspect(seq){
   let adj=Array.from({length:n},()=>[]),deg=Array(n).fill(1),edges=[];
   function edge(a,b){adj[a].push(b);adj[b].push(a);edges.push([a,b])}
   for(let u of seq)deg[u]++;
   for(let u of seq){let v=deg.indexOf(1);edge(u,v);deg[u]--;deg[v]--}
   if(n>1){let rem=deg.flatMap((d,i)=>d===1?[i]:[]);edge(...rem)}
   trees++;
   let paths=Array.from({length:n},()=>Array(n).fill(0));
   for(let z=0;z<n;z++){function dfs(v,p,m){paths[z][v]=m|(1<<v);for(let w of adj[v])if(w!==p)dfs(w,v,paths[z][v])}dfs(z,-1,0)}
   let sides=edges.map(([a,b])=>{let m=0;for(let v=0;v<n;v++)if(!(paths[a][v]&(1<<b)))m|=1<<v;return m});
   function check(t,k){cases++;if(new Set(t).size<k)repeated++;
    let center=false;
    for(let z=0;z<n;z++){let good=true,used=0;for(let v of t){let p=paths[z][v]&~(1<<z);if(used&p){good=false;break}used|=p}if(good){center=true;break}}
    let cut=k===4&&sides.some(m=>t.reduce((s,v)=>s+((m>>v)&1),0)===2);
    if(center===cut)throw Error(JSON.stringify({n,edges,t,center,cut}));
    if(center)star++;else split++;
   }
   for(let k of [3,4]){function gen(t,min){if(t.length===k){check(t,k);return}for(let v=min;v<n;v++)gen([...t,v],v)}gen([],0)}
  }
  function prufer(seq){if(seq.length===Math.max(0,n-2)){inspect(seq);return}for(let i=0;i<n;i++)prufer([...seq,i])}prufer([])
 }
 if(!split||!repeated)throw Error("missing cases");
 return {trees,cases,star,split,repeated};
}
console.log(JSON.stringify(run()));
