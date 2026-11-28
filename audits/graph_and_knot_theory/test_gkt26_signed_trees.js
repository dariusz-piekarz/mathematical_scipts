// GKT-26-SIGNED-TREES-01: exhaustive signed multigraphs on three vertices.
const assert = require('node:assert/strict');
const edges = [[0,1],[0,1],[1,2],[0,2],[0,0],[2,2]];
let count=0;
for(let mask=0;mask<729;mask++){
 let z=mask; const w=edges.map(()=>{const a=z%3-1;z=Math.floor(z/3);return a;});
 const L=Array.from({length:3},()=>[0,0,0]);
 edges.forEach(([u,v],i)=>{if(u!==v){L[u][u]+=w[i];L[v][v]+=w[i];L[u][v]-=w[i];L[v][u]-=w[i];}});
 let p=0,q=0;
 for(let i=0;i<edges.length;i++)for(let j=i+1;j<edges.length;j++){
  if(!w[i]||!w[j])continue;
  const [a,b]=edges[i], [c,d]=edges[j];
  if(a===b||c===d||new Set([a,b,c,d]).size!==3)continue;
  if(w[i]*w[j]===1)p++;else q++;
 }
 for(let r=0;r<3;r++){
  const [a,b]=[0,1,2].filter(i=>i!==r);
  const det=L[a][a]*L[b][b]-L[a][b]*L[b][a];
  assert.equal(det,p-q);assert.equal(Math.abs(det)===p+q,p*q===0);count++;
 }
}
console.log('GKT-26-SIGNED-TREES-01 PASS',count);
