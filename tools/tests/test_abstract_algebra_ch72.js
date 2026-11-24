// AA-72-KMF-01: aa:lem:kostant-partition-recursion, aa:lem:kostant-generating,
// aa:tw:kostant-multiplicity, aa:cor:kostant-coset.
// Exact root lattice conversion, orbit enumeration, memoized partition recursion,
// independent A1 strings, A2 tableaux, adjoint and external tensor product models.
const assert=(b,m)=>{if(!b)throw Error(m)},key=v=>v.join(","),parse=s=>s.split(",").map(Number);
const add=(F,v,c=1n)=>{const k=key(v);F.set(k,(F.get(k)||0n)+c)};
const det=M=>M.length===0?1n:M[0].reduce((s,x,j)=>s+(j%2?-1n:1n)*BigInt(x)*det(M.slice(1).map(row=>row.filter((_,i)=>i!==j))),0n);
const rows=n=>{let out=[];for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)out.push([...Array(i).fill(1),...Array(j).fill(2),...Array(n-i-j).fill(3)]);return out};
function tableaux(a,b){const F=new Map();for(const t of rows(a+b))for(const u of rows(b)){if(u.some((x,i)=>x<=t[i]))continue;const n=[0,0,0];for(const x of [...t,...u])n[x-1]++;add(F,[n[0]-n[1],n[1]-n[2]])}return F}
const specs=[
 ["A1",[[2]],2,1],["A2",[[2,-1],[-1,2]],6,3],["B2",[[2,-2],[-1,2]],8,4],["G2",[[2,-3],[-1,2]],12,6],
 ["A3",[[2,-1,0],[-1,2,-1],[0,-1,2]],24,6],
 ["A1xA2",[[2,0,0],[0,2,-1],[0,-1,2]],12,4]
];
let systems=0,models=0,weights=0,absent=0,wrongCoset=0,cancellations=0,partitionChecks=0,orbitTerms=0;
for(const [name,C,order,N] of specs){
 const r=C.length,zero=Array(r).fill(0),rho=Array(r).fill(1),unit=i=>zero.map((_,j)=>+(i===j));
 const wt=v=>C.map(row=>row.reduce((s,c,j)=>s+c*v[j],0));
 const D=det(C);assert(D!==0n,name+" invertible");
 const inv=Array.from({length:r},(_,i)=>Array.from({length:r},(_,j)=>((i+j)%2?-1n:1n)*det(C.filter((_,k)=>k!==j).map(row=>row.filter((_,k)=>k!==i)))));
 function rootCoords(v){const nums=inv.map(row=>row.reduce((s,c,j)=>s+c*BigInt(v[j]),0n));if(nums.some(x=>x%D!==0n))return null;return nums.map(x=>Number(x/D))}
 const roots=Array.from({length:r},(_,i)=>unit(i)),seen=new Set(roots.map(key));
 for(let k=0;k<roots.length;k++)for(let i=0;i<r;i++){const v=[...roots[k]];v[i]-=wt(v)[i];if(!seen.has(key(v))){seen.add(key(v));roots.push(v)}}
 const pos=roots.filter(v=>v.every(x=>x>=0));assert(pos.length===N&&roots.length===2*N,name+" root count");
 const memo=new Map();
 function part(j,v){if(!v||v.some(x=>x<0))return 0n;if(!j)return v.every(x=>x===0)?1n:0n;const k=j+":"+key(v);if(memo.has(k))return memo.get(k);const z=part(j-1,v)+part(j,v.map((x,i)=>x-pos[j-1][i]));memo.set(k,z);return z}
 // Independent bounded enumeration of multiplicity families.
 function brute(j,v){if(j===N)return v.every(x=>x===0)?1n:0n;let total=0n,u=[...v];while(u.every(x=>x>=0)){total+=brute(j+1,u);u=u.map((x,i)=>x-pos[j][i])}return total}
 function grid(lo,hi,fn,v=[]){if(v.length===r){fn(v);return}for(let i=lo;i<=hi;i++)grid(lo,hi,fn,[...v,i])}
 grid(0,4,v=>{assert(part(N,v)===brute(0,v),name+" partition families");assert(key(rootCoords(wt(v)))===key(v),name+" root conversion");partitionChecks++});
 function check(lambda,F,bound){
  const v=lambda.map(x=>x+1),q=[{v,s:1n}],orbit=new Map([[key(v),1n]]);
  for(let k=0;k<q.length;k++)for(let i=0;i<r;i++){const u=q[k].v.map((x,j)=>x-q[k].v[i]*C[j][i]),s=-q[k].s;if(orbit.has(key(u)))assert(orbit.get(key(u))===s,name+" orbit sign");else{orbit.set(key(u),s);q.push({v:u,s})}}
  assert(q.length===order,name+" orbit order");
  const candidates=new Map();grid(-bound,bound,mu=>candidates.set(key(mu),mu));for(const k of F.keys())candidates.set(k,parse(k));
  for(const [k,mu] of candidates){
   let m=0n,negative=false,positive=false;const inCoset=rootCoords(lambda.map((x,i)=>x-mu[i]))!==null;
   for(const {v:u,s} of q){const arg=rootCoords(u.map((x,i)=>x-mu[i]-rho[i]));const count=part(N,arg);m+=s*count;if(count>0n){if(s<0n)negative=true;else positive=true}orbitTerms++}
   const expected=F.get(k)||0n;assert(m===expected,name+" multiplicity "+key(lambda)+" at "+k);assert(m>=0n,name+" positivity");
   if(!inCoset){assert(m===0n,name+" root coset");wrongCoset++}
   if(!expected)absent++;if(negative&&positive)cancellations++;weights++;
  }
  models++;
 }
 if(name==="A1"){for(let m=0;m<=16;m++){const F=new Map();for(let j=0;j<=m;j++)add(F,[m-2*j]);check([m],F,m+3)}}
 else if(name==="A2"){for(let a=0;a<=6;a++)for(let b=0;b<=6-a;b++)check([a,b],tableaux(a,b),a+b+2)}
 else if(name==="A1xA2"){for(let m=0;m<=3;m++)for(let a=0;a<=3;a++)for(let b=0;b<=3-a;b++){const F=new Map();for(let j=0;j<=m;j++)for(const [k,c] of tableaux(a,b))add(F,[m-2*j,...parse(k)],c);check([m,a,b],F,Math.max(m,a+b)+1)}}
 else {const F=new Map([[key(zero),BigInt(r)]]);for(const v of roots)add(F,wt(v));const high=pos.reduce((a,b)=>a.reduce((s,x)=>s+x,0)>=b.reduce((s,x)=>s+x,0)?a:b);check(wt(high),F,4)}
 systems++;
}
assert(wrongCoset>0&&cancellations>0,"boundary coverage");
console.log("AA-72-KMF-01: PASS",{systems,models,weights,absent,wrongCoset,cancellations,partitionChecks,orbitTerms});
