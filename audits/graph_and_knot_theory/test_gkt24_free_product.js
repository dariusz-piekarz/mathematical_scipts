// GKT-24-FREE-PRODUCT-01: incidence and local tree structure in C2*C3.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},orders=[2,3];
 const key=w=>w.map(([t,j])=>t+":"+j).join(",");
 function append(w,t,j){j=(j%orders[t]+orders[t])%orders[t];if(!j)return w.slice();if(w.length&&w[w.length-1][0]===t){let r=(w[w.length-1][1]+j)%orders[t];return r?[...w.slice(0,-1),[t,r]]:w.slice(0,-1)}return [...w,[t,j]]}
 const coset=(w,t)=>w.length&&w[w.length-1][0]===t?w.slice(0,-1):w.slice();
 const vertex=(w,t)=>t+"|"+key(coset(w,t));
 let words=[[]],all=[[]];for(let n=1;n<=10;n++){words=words.flatMap(w=>[0,1].filter(t=>!w.length||w[w.length-1][0]!==t).flatMap(t=>Array.from({length:orders[t]-1},(_,i)=>append(w,t,i+1))));all.push(...words)}
 let incidences=0,translations=0,vertices=new Map(),E=new Map();
 for(let w of all){
  const o=vertex(w,0),v=vertex(w,1);E.set(key(w),[o,v]);
  for(let t of [0,1]){let base=coset(w,t),vs=vertex(w,t);vertices.set(vs,[base,t]);let reps=Array.from({length:orders[t]},(_,j)=>append(base,t,j));
   assert(new Set(reps.map(key)).size===orders[t],"distinct incident edges");
   assert(reps.every(x=>vertex(x,t)===vs),"coset incidence");
   assert(new Set(reps.map(x=>vertex(x,1-t))).size===orders[t],"distinct neighbors");
   for(let x of reps){for(let j=0;j<orders[t];j++)assert(vertex(append(x,t,j),t)===vs,"coset independence");incidences++}
  }
  for(let t of [0,1])for(let j=1;j<orders[t];j++){
   let left=x=>x.length&&x[0][0]===t?(((j+x[0][1])%orders[t])?[[t,(j+x[0][1])%orders[t]],...x.slice(1)]:x.slice(1)):[[t,j],...x];
   for(let u of [0,1])assert(vertex(left(w),u)===vertex(left(coset(w,u)),u),"left equivariance");translations++;
  }
 }
 // The finite set of edges indexed by words of bounded syllable length is connected and acyclic.
 let adj=new Map();for(let [a,b] of E.values()){if(!adj.has(a))adj.set(a,[]);if(!adj.has(b))adj.set(b,[]);adj.get(a).push(b);adj.get(b).push(a)}
 let Q=["0|"],seen=new Set(Q);while(Q.length)for(let v of adj.get(Q.pop()))if(!seen.has(v)){seen.add(v);Q.push(v)}
 assert(seen.size===adj.size&&E.size===adj.size-1,"finite tree");
 assert(adj.size===vertices.size,"all endpoints");
 return {words:all.length,vertices:adj.size,edges:E.size,incidences,translations};
}
console.log(JSON.stringify(run()));
