// GKT-21-GLUE-01: directed band graphs with arbitrary choices and regular cuts.
function run(){
 const assert=(v,m)=>{if(!v)throw Error(m)};let models=0,connected=0,cuts=0,parallel=0,bypass=0;
 function check(V,E){
  let adj=V.map(()=>[]);for(let [a,b] of E){assert(a<b,"height");adj[a].push(b);adj[b].push(a)}
  let seen=new Set(),k=0;for(let i=0;i<V.length;i++)if(!seen.has(i)){k++;let S=[i];seen.add(i);while(S.length)for(let j of adj[S.pop()])if(!seen.has(j)){seen.add(j);S.push(j)}}
  let beta=E.length-V.length+k,chi=V.reduce((a,v)=>a+(v===0||v===3?1:-1),0);
  assert(beta===k-chi/2,"Euler");assert(adj.every((a,i)=>a.length===(V[i]===0||V[i]===3?1:3)),"degree");
  // Insert a regular vertex at every intervening critical height, independently on each edge.
  let edges=[],aux=new Set(),h=V.map((_,i)=>i);
  for(let [a,b] of E){let x=a;for(let t=a+1;t<b;t++){let z=h.length;h.push(t);aux.add(z);edges.push([x,z]);x=z}edges.push([x,b])}
  cuts+=aux.size;assert(edges.length-h.length+k===beta,"subdivision rank");if(aux.size)bypass++;
  for(let z of aux){let ins=edges.filter(e=>e[1]===z),outs=edges.filter(e=>e[0]===z);assert(ins.length===1&&outs.length===1,"regular degree");let a=ins[0][0],b=outs[0][1];assert(h[a]<h[z]&&h[z]<h[b],"monotone suppression");edges=edges.filter(e=>!e.includes(z));edges.push([a,b])}
  let key=es=>es.map(e=>e.join(",")).sort().join(";");assert(key(edges)===key(E),"edge multiset recovered");
  models++;if(k===1)connected++;if(new Set(E.map(e=>e.join(","))).size<E.length)parallel++;
 }
 function visit(V,E,L){
  if(V.length&&L.length===0)check(V,E);if(V.length===7)return;
  let id=V.length;visit([...V,0],E,[...L,id]);
  // Equivalent choices of identical open ends are skipped, but different sources are all tried.
  for(let i=0;i<L.length;i++){if(L.indexOf(L[i])!==i)continue;let rest=L.filter((_,j)=>j!==i);
   visit([...V,1],[...E,[L[i],id]],[...rest,id,id]);visit([...V,3],[...E,[L[i],id]],rest);
   let used=new Set();for(let j=i+1;j<L.length;j++){let pair=[L[i],L[j]].sort().join(",");if(used.has(pair))continue;used.add(pair);visit([...V,2],[...E,[L[i],id],[L[j],id]],[...L.filter((_,k)=>k!==i&&k!==j),id])}
  }
 }
 visit([],[],[]);assert(connected&&parallel&&bypass,"coverage");return {models,connected,cuts,parallel,bypass};
}
console.log(JSON.stringify(run()));
