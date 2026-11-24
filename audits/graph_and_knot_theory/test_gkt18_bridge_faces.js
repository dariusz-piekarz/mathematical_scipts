// GKT18-BRIDGE-01: every bridge has both darts in the same face.
const assert = require('node:assert/strict');
let count=0;
for(let n=2;n<=5;n++){
 let edges=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)edges.push([i,j]);
 for(let mask=1;mask<2**edges.length;mask++){
  let es=edges.filter((_,i)=>mask>>i&1),adj=Array.from({length:n},()=>[]);
  es.forEach(([a,c],i)=>{adj[a].push(2*i);adj[c].push(2*i+1)});
  function reach(skip){let seen=new Set([0]),q=[0];for(let v of q)for(let d of adj[v])if((d>>1)!==skip){let w=es[d>>1][1-(d%2)];if(!seen.has(w)){seen.add(w);q.push(w)}}return seen.size}
  if(reach(-1)!==n)continue;
  let sig=[];for(let a of adj)a.forEach((d,i)=>sig[d]=a[(i+1)%a.length]);
  let face=[];for(let d=0;d<sig.length;d++)if(face[d]===undefined){let k=d;do{face[k]=d;k=sig[k^1]}while(k!==d)}
  for(let i=0;i<es.length;i++)if(reach(i)!==n){assert.equal(face[2*i],face[2*i+1]);count++}
 }
}
assert.equal(count,1067);console.log('GKT18-BRIDGE-01:',count);
