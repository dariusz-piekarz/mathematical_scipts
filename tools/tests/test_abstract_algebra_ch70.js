// AA-70-WCF-01: aa:lem:weyl-weight-trace, aa:tw:weyl-character-formula.
// Exact A1 and A2 weights from monomials and semistandard Young tableaux.
const assert=(b,m)=>{if(!b)throw Error(m)};
const key=v=>v.join(","), parse=s=>s.split(",").map(Number);
const add=(f,v,c)=>{const k=key(v),z=(f.get(k)||0n)+c;if(z)f.set(k,z);else f.delete(k)};
const eq=(a,b)=>a.size===b.size&&[...a].every(([k,c])=>b.get(k)===c);
const mult=(a,b)=>{const f=new Map();for(const [s,c] of a)for(const [t,d] of b){const w=parse(t);add(f,parse(s).map((x,i)=>x+w[i]),c*d)}return f};
const rows=n=>{const a=[];for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)a.push([...Array(i).fill(1),...Array(j).fill(2),...Array(n-i-j).fill(3)]);return a};
function tableaux(a,b){const f=new Map();for(const top of rows(a+b))for(const bottom of rows(b)){if(bottom.some((x,i)=>x<=top[i]))continue;const n=[0,0,0];for(const x of [...top,...bottom])n[x-1]++;add(f,[n[0]-n[1],n[1]-n[2]],1n)}return f}
let models=0,weightChecks=0,absent=0,traceChecks=0,eigenChecks=0;
function verify(lambda,F,C,roots,dot,bound){
 const r=lambda.length,rho=Array(r).fill(1),plus=(u,v)=>u.map((x,i)=>x+v[i]);
 const norm=u=>dot(u,u);
 const shifted=plus(lambda,rho), cas=norm(shifted)-norm(rho);
 const R=(v,i)=>v.map((x,j)=>x-v[i]*C[j][i]);
 function alt(v){const q=[{v,s:1n}],seen=new Map([[key(v),1n]]);for(let k=0;k<q.length;k++)for(let i=0;i<r;i++){const w=R(q[k].v,i),s=-q[k].s,t=key(w);if(seen.has(t))assert(seen.get(t)===s,"regular orbit signs");else{seen.set(t,s);q.push({v:w,s})}}return seen}
 let D=new Map([[key(rho),1n]]);
 for(const a of roots){const g=new Map(D);for(const [k,c] of D)add(g,parse(k).map((x,i)=>x-a[i]),-c);D=g}
 assert(eq(D,alt(rho)),"denominator");
 const DF=mult(D,F);assert(eq(DF,alt(shifted)),"character identity");
 for(const k of DF.keys()){assert(norm(parse(k))===norm(shifted),"Casimir eigenvalue");eigenChecks++}
 const points=[];function grid(v){if(v.length===r){points.push(v);return}for(let i=-bound;i<=bound;i++)grid([...v,i])}grid([]);
 for(const mu of points){
  const m=F.get(key(mu))||0n;let total=0n;
  for(const a of roots){
   let T=0n,next=0n;
   // Each model has support within the box. Beyond 2*bound+2 steps no root ray can meet it.
   for(let j=1;j<=2*bound+2;j++){const v=mu.map((x,i)=>x+j*a[i]);const z=dot(v,a)*(F.get(key(v))||0n);T+=z;if(j>1)next+=z}
   const v=plus(mu,a);
   assert(T-next===dot(v,a)*(F.get(key(v))||0n),"trace difference");
   if(!m)assert(T===0n,"trace of zero space");
   total+=T;traceChecks++;
  }
  assert((cas-dot(mu,plus(mu,rho.map(x=>2*x))))*m===2n*total,"Freudenthal trace identity");
  if(!m)absent++;weightChecks++;
 }
 models++;
}
for(let m=0;m<=20;m++){const F=new Map();for(let j=0;j<=m;j++)add(F,[m-2*j],1n);verify([m],F,[[2]],[[2]],(u,v)=>BigInt(u[0]*v[0]),m+2)}
for(let a=0;a<=7;a++)for(let b=0;b<=7-a;b++){const F=tableaux(a,b);verify([a,b],F,[[2,-1],[-1,2]],[[2,-1],[-1,2],[1,1]],(u,v)=>BigInt(2*u[0]*v[0]+u[0]*v[1]+u[1]*v[0]+2*u[1]*v[1]),a+b+2)}
console.log("AA-70-WCF-01: PASS",{models,weightChecks,absent,traceChecks,eigenChecks});

// AA-70-WCF-02: aa:lem:weyl-casimir-eigenvalue, aa:lem:weyl-weight-trace,
// aa:tw:weyl-character-formula. Adjoint models from root spaces and mixed
// simple factors with their relative Killing scales (not Weyl-formula data).
const before70={models,weightChecks,absent,traceChecks,eigenChecks};
let adjointModels=0,mixedModels=0;
for(const [name,C,G,expected] of [
 ["B2",[[2,-2],[-1,2]],[[1,1],[1,2]],8],
 ["G2",[[2,-3],[-1,2]],[[2,3],[3,6]],12]
]){
 const q=[[1,0],[0,1]],seen=new Set(q.map(key));
 for(let k=0;k<q.length;k++)for(let i=0;i<2;i++){
  const v=[...q[k]];v[i]-=C[i].reduce((s,c,j)=>s+c*v[j],0);
  if(!seen.has(key(v))){seen.add(key(v));q.push(v)}
 }
 assert(q.length===expected,name+" root count");
 const wt=v=>C.map(row=>row.reduce((s,c,j)=>s+c*v[j],0));
 const pos=q.filter(v=>v.every(x=>x>=0));
 const highest=pos.reduce((a,b)=>a[0]+a[1]>=b[0]+b[1]?a:b);
 const lambda=wt(highest),F=new Map([[key([0,0]),2n]]);
 assert(lambda.every(x=>x>=0),name+" highest root dominant");
 for(const v of q)add(F,wt(v),1n);
 assert([...F.values()].reduce((a,b)=>a+b,0n)===BigInt(expected+2),name+" adjoint dimension");
 const dot=(u,v)=>BigInt(u.reduce((s,x,i)=>s+x*G[i].reduce((t,c,j)=>t+c*v[j],0),0));
 const bound=Math.max(...q.flatMap(v=>wt(v).map(Math.abs)))+2;
 verify(lambda,F,C,pos.map(wt),dot,bound);adjointModels++;
}
const Cmix=[[2,0,0],[0,2,-1],[0,-1,2]];
const rootsMix=[[2,0,0],[0,2,-1],[0,-1,2],[0,1,1]];
// Actual Killing dual Gram: A1 = 1/8; A2 = [[2,1],[1,2]]/18.
// Multiply the entire direct sum form by 72, preserving relative scales.
const mixDot=(u,v)=>BigInt(9*u[0]*v[0]+4*(2*u[1]*v[1]+u[1]*v[2]+u[2]*v[1]+2*u[2]*v[2]));
for(let m=0;m<=4;m++)for(let a=0;a<=4;a++)for(let b=0;b<=4-a;b++){
 const f=tableaux(a,b),F=new Map();
 for(let j=0;j<=m;j++)for(const [k,c] of f)add(F,[m-2*j,...parse(k)],c);
 verify([m,a,b],F,Cmix,rootsMix,mixDot,Math.max(m,a+b)+2);mixedModels++;
}
console.log("AA-70-WCF-02: PASS",{adjointModels,mixedModels,models:models-before70.models,weightChecks:weightChecks-before70.weightChecks,absent:absent-before70.absent,traceChecks:traceChecks-before70.traceChecks,eigenChecks:eigenChecks-before70.eigenChecks});

// AA-70-WCF-03: aa:lem:weyl-differential-product.
// Arbitrary signed Laurent polynomials, not necessarily W-invariant.
// Verify the lemma after clearing its denominator; no formal infinite series.
function checkProduct70(){
 const specs=[
  ["A1",[[1]],[[2]]],
  ["A2",[[2,1],[1,2]],[[2,-1],[-1,2],[1,1]]],
  ["B2",[[1,1],[1,2]],[[2,-1],[-2,2],[0,1],[2,0]]],
  ["A1xA2",[[9,0,0],[0,8,4],[0,4,8]],[[2,0,0],[0,2,-1],[0,-1,2],[0,1,1]]]
 ];
 let cases=0,coefficients=0,nonInvariant=0,zeroCases=0;
 for(const [name,G,roots] of specs){
  const rank=G.length,rho=Array(rank).fill(1),zero=Array(rank).fill(0);
  const dot=(u,v)=>BigInt(u.reduce((s,x,i)=>s+x*G[i].reduce((t,g,j)=>t+g*v[j],0),0));
  const sum=roots.reduce((v,a)=>v.map((x,i)=>x+a[i]),zero);
  assert(key(sum)===key(rho.map(x=>2*x)),name+" rho");
  const mon=(v,c=1n)=>new Map(c?[[key(v),c]]:[]);
  const factor=a=>{const f=mon(zero);add(f,a.map(x=>-x),-1n);return f};
  function productExcept(except=-1){let f=mon(rho);for(let i=0;i<roots.length;i++)if(i!==except)f=mult(f,factor(roots[i]));return f}
  const D=productExcept();
  const op=(f,fn)=>{const g=new Map();for(const [s,c] of f){const v=parse(s);add(g,v,c*fn(v))}return g};
  const L=f=>op(f,v=>dot(v,v));
  const der=(f,a)=>op(f,v=>dot(a,v));
  assert(eq(L(D),op(D,()=>dot(rho,rho))),name+" denominator eigenvector");
  for(let seed=0;seed<36;seed++){
   const F=new Map();
   if(seed)for(let j=0;j<12;j++){
    const v=Array.from({length:rank},(_,i)=>((seed*(i+3)+j*(2*i+5)+j*j)%9)-4);
    add(F,v,BigInt((seed*3+j*5)%11-5));
   }
   const main=op(F,v=>dot(v,v)+2n*dot(rho,v)+dot(rho,rho));
   const right=mult(D,main);
   for(let i=0;i<roots.length;i++){
    const a=roots[i],term=mult(mult(productExcept(i),mon(a.map(x=>-x))),der(F,a));
    for(const [s,c] of term)add(right,parse(s),2n*c);
   }
   const left=L(mult(D,F));
   assert(eq(left,right),name+" cleared differential product");
   // An arbitrary F need not have invariant coefficients even under -1;
   // this is just a coverage check of signed/asymmetric inputs.
   if([...F].some(([s,c])=>F.get(key(parse(s).map(x=>-x)))!==c))nonInvariant++;
   if(!F.size)zeroCases++;
   coefficients+=left.size;cases++;
  }
 }
 assert(zeroCases===specs.length&&nonInvariant>0,"edge coverage");
 return {systems:specs.length,cases,coefficients,asymmetricInputs:nonInvariant,zeroCases};
}
console.log("AA-70-WCF-03: PASS",checkProduct70());
