// AA-60 independent exact extension and root-string checks.
function independentAA60(){
 const check=(v,msg)=>{if(!v)throw Error(msg)};
 const zero=(m,n)=>Array.from({length:m},()=>Array(n).fill(0n));
 const add=(a,b)=>a.map((r,i)=>r.map((x,j)=>x+b[i][j]));
 const scale=(a,c)=>a.map(r=>r.map(x=>c*x));
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0n)));
 const sub=(a,b)=>add(a,scale(b,-1n));
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 function rank(cols){
  if(!cols.length)return 0;
  const A=cols[0].map((_,i)=>cols.map(c=>c[i]));let r=0;
  for(let j=0;j<cols.length&&r<A.length;j++){
   let k=r;while(k<A.length&&A[k][j]===0n)k++;
   if(k===A.length)continue;
   [A[k],A[r]]=[A[r],A[k]];
   for(let i=r+1;i<A.length;i++){
    if(!A[i][j])continue;
    const p=A[r][j],q=A[i][j],d=gcd(p,q);
    A[i]=A[i].map((x,l)=>(p/d)*x-(q/d)*A[r][l]);
    const g=A[i].reduce(gcd,0n);if(g)A[i]=A[i].map(x=>x/g);
   }r++;
  }return r;
 }
 // Use the unscaled monomial basis, distinct from the main test's normalized basis.
 function mod(m){
  const H=zero(m+1,m+1),E=zero(m+1,m+1),F=zero(m+1,m+1);
  for(let j=0;j<=m;j++){
   H[j][j]=BigInt(m-2*j);
   if(j>0)E[j-1][j]=BigInt(j);
   if(j<m)F[j+1][j]=BigInt(m-j);
  }return [H,E,F];
 }
 let extensions=0,equal=0,variables=0;
 for(let a=0;a<=4;a++)for(let b=0;b<=4;b++){
  const [H,E,F]=mod(a),[h,e,f]=mod(b),d=(a+1)*(b+1);
  const action=(A,X,B)=>sub(mul(A,X),mul(X,B));
  // Off-diagonal blocks X,Y,Z of H,E,F. The three linear equations
  // are exactly the off-diagonal parts of [H,E]=2E, [H,F]=-2F, [E,F]=H.
  const residual=(X,Y,Z)=>[
   sub(sub(action(H,Y,h),action(E,X,e)),scale(Y,2n)),
   add(sub(action(H,Z,h),action(F,X,f)),scale(Z,2n)),
   sub(sub(action(E,Z,e),action(F,Y,f)),X)
  ].flat(2);
  const cols=[],cob=[];
  for(let i=0;i<=a;i++)for(let j=0;j<=b;j++){
   const T=zero(a+1,b+1);T[i][j]=1n;
   const O=zero(a+1,b+1);
   cols.push(residual(T,O,O),residual(O,T,O),residual(O,O,T));
   const v=[action(H,T,h),action(E,T,e),action(F,T,f)];
   check(residual(...v).every(x=>x===0n),"coboundary not cocycle");
   cob.push(v.flat(2));
  }
  const rk=rank(cols),rb=rank(cob);
  check(rb===d-(a===b?1:0),"intertwiner dimension");
  check(3*d-rk===rb,"nonsplit extension detected");
  extensions++;if(a===b)equal++;variables+=3*d;
 }
 const systems=[];
 function classical(type,n){
  const roots=[];
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(const s of [-1,1])for(const t of [-1,1]){
   const r=Array(n).fill(0);r[i]=s;r[j]=t;roots.push(r);
  }
  if(type!=="D")for(let i=0;i<n;i++)for(const s of [-1,1]){
   const r=Array(n).fill(0);r[i]=type==="C"?2*s:s;roots.push(r);
  }return roots;
 }
 for(let n=2;n<=5;n++)for(const t of ["B","C"])systems.push([t+n,classical(t,n)]);
 for(let n=4;n<=5;n++)systems.push(["D"+n,classical("D",n)]);
 const F4=classical("B",4).map(r=>r.map(x=>2*x));
 for(let k=0;k<16;k++)F4.push(Array.from({length:4},(_,i)=>(k>>i)&1?1:-1));
 systems.push(["F4",F4]);
 const G2=[];
 for(let i=0;i<3;i++){
  for(let j=0;j<3;j++)if(i!==j){const r=[0,0,0];r[i]=1;r[j]=-1;G2.push(r);}
  for(const s of [-1,1]){const r=Array(3).fill(-s);r[i]=2*s;G2.push(r);}
 }
 systems.push(["G2",G2]);
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
 let pairs=0,strings=0,maxLength=0;const lengths={};
 for(const [name,R] of systems){
  const keys=new Set(R.map(r=>r.join(",")));check(keys.size===R.length,"duplicates");
  let longest=0;
  for(const a of R)for(const b of R){
   const aa=dot(a,a),bb=dot(b,b),ab=dot(a,b);
   check((2*ab)%aa===0,"nonintegral Cartan");
   const c=2*ab/aa;
   check(keys.has(b.map((x,i)=>x-c*a[i]).join(",")),"reflection");
   pairs++;
   if(ab*ab===aa*bb){check(b.every((x,i)=>x===a[i])||b.every((x,i)=>x===-a[i]),"not reduced");continue;}
   // Exhaust all possible k: every root on the line determines k from one nonzero coordinate.
   const i=a.findIndex(x=>x!==0),ks=[];
   for(const r of R){const k=(r[i]-b[i])/a[i];if(Number.isInteger(k)&&r.every((x,j)=>x===b[j]+k*a[j]))ks.push(k);}
   ks.sort((x,y)=>x-y);const p=-ks[0],q=ks[ks.length-1];
   check(ks.length===p+q+1&&ks.every((k,j)=>k===j-p),"gap in root string");
   check(p-q===c,"wrong root-string sign");
   longest=Math.max(longest,ks.length);strings++;
  }
  lengths[name]=longest;maxLength=Math.max(maxLength,longest);
 }
 check(maxLength===4&&lengths.G2===4,"missing long string");
 return {extensions,equal,variables,systems:systems.length,pairs,strings,lengths};
}
console.log('AA-60 independent exact checks: PASS', independentAA60());
