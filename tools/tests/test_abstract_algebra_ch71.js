// AA-71-DIM-01: aa:lem:weyl-alternant-order, aa:tw:weyl-dimension.
// Exact moments of independently enumerated regular Weyl orbits.
// All inner products are multiplied by one common positive scale per system.
const assert=(b,m)=>{if(!b)throw Error(m)};
const key=v=>v.join(",");
const specs=[
 ["A1",[[2]],[1],2,1],["A2",[[2,-1],[-1,2]],[1,1],6,3],
 ["B2",[[2,-2],[-1,2]],[1,2],8,4],["G2",[[2,-3],[-1,2]],[1,3],12,6],
 ["A1xA1",[[2,0],[0,2]],[1,2],4,2],
 ["A3",[[2,-1,0],[-1,2,-1],[0,-1,2]],[1,1,1],24,6],
 ["B3",[[2,-1,0],[-1,2,-2],[0,-1,2]],[1,1,2],48,9],
 ["C3",[[2,-1,0],[-1,2,-1],[0,-2,2]],[2,2,1],48,9],
 ["D4",[[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]],[1,1,1,1],192,12]
];
const rows=n=>{const out=[];for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)out.push([...Array(i).fill(1),...Array(j).fill(2),...Array(n-i-j).fill(3)]);return out};
function tableaux(a,b){let n=0n;for(const t of rows(a+b))for(const u of rows(b))if(u.every((x,i)=>x>t[i]))n++;return n}
let systems=0,models=0,moments=0,orbitTerms=0,dimensionChecks=0,independentDimensions=0,adjoints=0;
for(const [name,C,d,order,N] of specs){
 const r=C.length,rho=Array(r).fill(1),unit=i=>Array.from({length:r},(_,j)=>+(i===j));
 const wt=v=>C.map(row=>row.reduce((s,c,j)=>s+c*v[j],0));
 for(let i=0;i<r;i++)for(let j=0;j<r;j++)assert(d[i]*C[i][j]===d[j]*C[j][i],name+" symmetrization");
 const roots=Array.from({length:r},(_,i)=>unit(i)),seen=new Set(roots.map(key));
 for(let k=0;k<roots.length;k++)for(let i=0;i<r;i++){
  const v=[...roots[k]];v[i]-=wt(v)[i];
  if(!seen.has(key(v))){seen.add(key(v));roots.push(v)}
 }
 const pos=roots.filter(v=>v.every(x=>x>=0));
 assert(pos.length===N&&roots.length===2*N,name+" root count");
 const sum=pos.reduce((u,v)=>u.map((x,i)=>x+v[i]),Array(r).fill(0));
 assert(wt(sum).every(x=>x===2),name+" rho");
 // Pairings with a simple root are d_i times the i-th weight coordinate.
 const pair=(v,root)=>BigInt(root.reduce((s,x,i)=>s+x*d[i]*v[i],0));
 const prod=v=>pos.reduce((p,b)=>p*(2n*pair(v,b)),1n);
 const denom=prod(rho);
 const factorial=Array.from({length:N},(_,i)=>BigInt(i+1)).reduce((p,x)=>p*x,1n);
 function dim(lambda,independent){
  const v=lambda.map(x=>x+1),q=[{v,s:1n}],orbit=new Map([[key(v),1n]]);
  for(let k=0;k<q.length;k++)for(let i=0;i<r;i++){
   const u=q[k].v.map((x,j)=>x-q[k].v[i]*C[j][i]),s=-q[k].s;
   if(orbit.has(key(u)))assert(orbit.get(key(u))===s,name+" sign");
   else{orbit.set(key(u),s);q.push({v:u,s})}
  }
  assert(q.length===order,name+" orbit order");
  const M=Array(N+1).fill(0n);
  // Exponent is 2*(w(mu),rho), using 2*rho=sum of positive roots.
  for(const {v:u,s} of q){const z=pair(u,sum);let power=1n;for(let k=0;k<=N;k++){M[k]+=s*power;power*=z}orbitTerms++}
  assert(M.slice(0,N).every(x=>x===0n),name+" vanishing lower moments");
  assert(M[N]===factorial*prod(v)&&M[N]>0n,name+" leading moment");
  moments+=N+1;
  assert(prod(v)%denom===0n,name+" integral dimension");
  const answer=prod(v)/denom;
  if(independent!==undefined){assert(answer===BigInt(independent),name+" dimension model");independentDimensions++}
  dimensionChecks++;models++;return answer;
 }
 const grid=[];function fill(v){if(v.length===r){grid.push(v);return}for(let i=0;i<=3;i++)fill([...v,i])}fill([]);
 for(const lambda of grid){
  let expected;
  if(name==="A1")expected=lambda[0]+1;
  if(name==="A1xA1")expected=(lambda[0]+1)*(lambda[1]+1);
  if(name==="A2")expected=tableaux(...lambda);
  dim(lambda,expected);
 }
 if(name!=="A1xA1"){
  const highest=pos.reduce((u,v)=>u.reduce((a,b)=>a+b,0)>=v.reduce((a,b)=>a+b,0)?u:v);
  const lambda=wt(highest);assert(lambda.every(x=>x>=0),name+" dominant highest root");
  dim(lambda,2*N+r);adjoints++;
 }
 if(name==="B2")for(const [a,b,n] of [[1,0,4],[0,1,5],[2,0,10]])dim([a,b],n);
 if(name==="G2")for(const [a,b,n] of [[1,0,7],[0,1,14],[2,0,27]])dim([a,b],n);
 systems++;
}
console.log("AA-71-DIM-01: PASS",{systems,models,moments,orbitTerms,dimensionChecks,independentDimensions,adjoints});
