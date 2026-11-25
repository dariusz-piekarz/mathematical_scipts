// GKT-20-LINK-MOVES-01: exhaustive small pure 2-complexes and local Pachner moves.
// Run from root: node audits/graph_and_knot_theory/test_gkt20_link_moves.js
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},key=x=>[...x].sort((a,b)=>a-b).join(","),tri=x=>[...new Set(x.map(key))].sort().join(";");
 function data(T){
 let V=new Set(),E=new Map(),L=new Map();for(let i=0;i<T.length;i++){const t=T[i];assert(new Set(t).size===3,"degenerate triangle");for(let v of t){V.add(v);if(!L.has(v))L.set(v,[]);L.get(v).push(t.filter(x=>x!==v))}for(let j=0;j<3;j++){let k=key(t.filter((_,l)=>l!==j));if(!E.has(k))E.set(k,[]);E.get(k).push(i)}}
 return {V,E,L,chi:V.size-E.size+T.length};
 }
 function components(V,edges){let adj=new Map([...V].map(v=>[v,[]]));for(let [a,b] of edges){adj.get(a).push(b);adj.get(b).push(a)}let seen=new Set(),k=0;for(let v of V)if(!seen.has(v)){k++;let S=[v];seen.add(v);while(S.length)for(let w of adj.get(S.pop()))if(!seen.has(w)){seen.add(w);S.push(w)}}return k}
 function links(D){return [...D.L.values()].every(es=>{let vs=new Set(es.flat());let deg=new Map([...vs].map(v=>[v,0]));for(let [a,b] of es){deg.set(a,deg.get(a)+1);deg.set(b,deg.get(b)+1)}return [...deg.values()].every(x=>x===2)&&components(vs,es)===1})}
 function verify(T){let D=data(T);assert(links(D),"link condition");assert([...D.E.values()].every(x=>x.length===2),"edge incidence");let dual=[...D.E.values()];assert(new Set(dual.map(key)).size===dual.length,"dual simplicity");assert(components(new Set(T.map((_,i)=>i)),dual)===1,"dual connectivity");assert(3*T.length===2*D.E.size,"double count");return D}
 let examined=0,surfaces=0,subdivisions=0,flips=0,blocked=0,reverseBlocked=0,edgeSub=0,pinches=0;
 function inspect(T){examined++;let D=data(T);if(!T.length)return;let all2=[...D.E.values()].every(x=>x.length===2);let connected=components(D.V,[...D.E.keys()].map(k=>k.split(",").map(Number)))===1;
 if(all2&&connected&&!links(D))pinches++;
 if(!links(D)||!connected)return;surfaces++;verify(T);let x=Math.max(...D.V)+1;
 for(let i=0;i<T.length;i++){let [a,b,c]=T[i],rest=T.filter((_,j)=>i!==j),U=[...rest,[a,b,x],[b,c,x],[c,a,x]],A=verify(U);assert(A.chi===D.chi,"1-3 Euler");assert(!U.some(t=>key(t)===key([a,b,c])),"3-1 target absent");assert(tri([...U.filter(t=>!t.includes(x)),[a,b,c]])===tri(T),"3-1 inverse");subdivisions++}
 for(let v of D.V){let ts=T.filter(t=>t.includes(v));if(ts.length===3){let abc=[...new Set(ts.flat().filter(w=>w!==v))];if(T.some(t=>key(t)===key(abc)))reverseBlocked++;else{let U=[...T.filter(t=>!t.includes(v)),abc];assert(verify(U).chi===D.chi,"3-1 Euler")}}}
 for(let [e,ids] of D.E){let [a,b]=e.split(",").map(Number),[i,j]=ids,c=T[i].find(v=>v!==a&&v!==b),d=T[j].find(v=>v!==a&&v!==b);assert(c!==d,"opposite vertices");let rest=T.filter((_,h)=>h!==i&&h!==j);
 if(D.E.has(key([c,d])))blocked++;else{let U=[...rest,[a,c,d],[b,c,d]],A=verify(U);assert(A.chi===D.chi&&!A.E.has(e),"2-2 flip");flips++}
 let U=[...rest,[a,b,x],[b,c,x],[c,a,x],T[j]],A=verify(U);assert(!A.E.has(key([x,d])),"new diagonal");let W=[...rest,[a,x,c],[b,x,c],[a,x,d],[b,x,d]],B=verify(W);assert(B.chi===D.chi&&B.V.size===D.V.size+1&&B.E.size===D.E.size+3&&W.length===T.length+2&&!B.E.has(e),"edge subdivision");edgeSub++;
 }
 }
 // All subsets of triangles on <=5 labelled vertices; isolated vertices are omitted.
 for(let n=3;n<=5;n++){let ts=[];for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)for(let c=b+1;c<n;c++)ts.push([a,b,c]);for(let m=0;m<2**ts.length;m++)inspect(ts.filter((_,i)=>m>>i&1))}
 // Two tetrahedral spheres glued at one vertex: all edges have degree two, link disconnected.
 const sphere=a=>[[a[0],a[1],a[2]],[a[0],a[1],a[3]],[a[0],a[2],a[3]],[a[1],a[2],a[3]]];inspect([...sphere([0,1,2,3]),...sphere([0,4,5,6])]);
 // Octahedral sphere: flips exist (opposite vertices not joined).
 let oct=[];for(let a of [0,1])for(let b of [2,3])for(let c of [4,5])oct.push([a,b,c]);inspect(oct);
 assert(surfaces>0&&flips>0&&blocked>0&&reverseBlocked>0&&pinches>0,"coverage");return {examined,surfaces,subdivisions,flips,blocked,reverseBlocked,edgeSub,pinches};
}
console.log(JSON.stringify(run()));
