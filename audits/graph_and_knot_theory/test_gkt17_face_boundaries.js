// GKT-17-FACES-01. Run: node audits/graph_and_knot_theory/test_gkt17_face_boundaries.js
// Exhaustive connected labelled simple graphs on 3..5 vertices and cyclic rotation systems.
// Spherical rotation systems selected by Euler characteristic 2 (orientable ribbon surface).
// Tests bridge/face equivalence and simple facial walks in 2-connected graphs.
// Finite combinatorial test, not verification of local straightening or Jordan-Schoenflies.
function run(){
 const stats={graphs:0,rotations:0,planeEmbeddings:0,biconnectedEmbeddings:0,faces:0,bridgeChecks:0,repeatedFaces:0};
 function assert(p,msg){if(!p)throw Error(msg)}
 function perms(a){if(!a.length)return [[]];return a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p]))}
 for(let n=3;n<=5;n++){
  const pairs=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)pairs.push([i,j]);
  for(let mask=0;mask<1<<pairs.length;mask++){
   const adj=Array.from({length:n},()=>[]),es=[];
   for(let i=0;i<pairs.length;i++)if(mask>>i&1){let [a,b]=pairs[i];adj[a].push(b);adj[b].push(a);es.push([a,b])}
   function conn(remove=-1,skip=[]){let start=Array.from({length:n},(_,i)=>i).find(i=>i!==remove),seen=new Set([start]),todo=[start];while(todo.length){let a=todo.pop();for(let b of adj[a])if(b!==remove&&!seen.has(b)&&!(skip.includes(a)&&skip.includes(b))){seen.add(b);todo.push(b)}}return seen.size===n-(remove>=0?1:0)}
   if(!conn())continue;
   stats.graphs++;
   let two=Array.from({length:n},(_,i)=>i).every(i=>conn(i)),bridges=es.map(e=>!conn(-1,e));
   let orders=adj.map(ns=>perms(ns.slice(1)).map(p=>[ns[0],...p]));
   function inspect(rot){
    stats.rotations++;let visited=new Map(),faces=[];
    const code=(a,b)=>a*n+b;
    for(let [a,b] of es)for(let [u,v] of [[a,b],[b,a]]){
     let initial=code(u,v);if(visited.has(initial))continue;
     let face=[],k=initial;
     do{
      assert(!visited.has(k),"darts do not partition into cycles");visited.set(k,faces.length);
      let x=Math.floor(k/n),y=k%n;face.push(x);
      let ns=rot[y],z=ns[(ns.indexOf(x)+1)%ns.length];k=code(y,z);
     }while(k!==initial);
     faces.push(face);
    }
    assert(visited.size===2*es.length,"dart count");
    if(n-es.length+faces.length!==2)return;
    stats.planeEmbeddings++;
    if(two)stats.biconnectedEmbeddings++;
    stats.faces+=faces.length;
    for(let i=0;i<es.length;i++){let [x,y]=es[i];assert((visited.get(code(x,y))===visited.get(code(y,x)))===bridges[i],"bridge-face equivalence");stats.bridgeChecks++}
    for(let face of faces){
     if(new Set(face).size!==face.length)stats.repeatedFaces++;
     if(two)assert(face.length>=3&&new Set(face).size===face.length,"non-simple face in 2-connected spherical rotation");
    }
   }
   function choose(i,rot){if(i===n){inspect(rot);return}for(let order of orders[i])choose(i+1,[...rot,order])}
   choose(0,[]);
  }
 }
 assert(stats.biconnectedEmbeddings>0&&stats.repeatedFaces>0,"missing positive or negative examples");
 return stats;
}
console.log(JSON.stringify(run()));
