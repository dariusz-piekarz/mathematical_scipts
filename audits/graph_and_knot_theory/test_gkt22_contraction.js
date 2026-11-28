// GKT-22-CONTRACTION-01: exact BigInt verification of elementary chain contraction maps.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},Z=(r,c)=>Array.from({length:r},()=>Array(c).fill(0n)),I=n=>Z(n,n).map((r,i)=>r.map((_,j)=>i===j?1n:0n));
 const mul=(A,B)=>A.map(r=>Array.from({length:B[0].length},(_,j)=>r.reduce((s,v,k)=>s+v*B[k][j],0n)));
 const add=(A,B,sign=1n)=>A.map((r,i)=>r.map((v,j)=>v+sign*B[i][j]));
 const eq=(A,B)=>A.length===B.length&&A.every((r,i)=>r.length===B[i].length&&r.every((v,j)=>v===B[i][j]));
 let seed=209;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 let trials=0,degreeChecks=0,unitNeg=0,nontrivial=0,torsionBlocks=0;
 for(let trial=0;trial<240;trial++){
  const n=5,N=4,p=trial%(n-1),D=Array.from({length:n},()=>Z(N,N));
  for(let k=1;k<n;k++){D[k][1][0]=k===p+1?(trial%2?1n:-1n):BigInt(rnd(7)-3);D[k][3][2]=BigInt(2+rnd(8));torsionBlocks++}
  // Conjugate the chain complex by unimodular changes of basis.
  for(let k=0;k<n;k++)for(let t=0;t<7;t++){
    let a=rnd(N),b=rnd(N-1);if(b>=a)b++;let c=BigInt(rnd(7)-3);let U=I(N),Ui=I(N);U[a][b]=c;Ui[a][b]=-c;
    if(k>0)D[k]=mul(D[k],U);
    if(k+1<n)D[k+1]=mul(Ui,D[k+1]);
  }
  for(let k=2;k<n;k++)assert(eq(mul(D[k-1],D[k]),Z(N,N)),"original chain");
  let choices=[];for(let i=0;i<N;i++)for(let j=0;j<N;j++)if(D[p+1][i][j]===1n||D[p+1][i][j]===-1n)choices.push([i,j]);
  if(!choices.length)continue;
  let [a,b]=choices[rnd(choices.length)],l=D[p+1][a][b];if(l===-1n)unitNeg++;
  let sizes=Array(n).fill(N);sizes[p]--;sizes[p+1]--;
  let J=[],P=[],H=Array.from({length:n-1},()=>Z(N,N));
  for(let k=0;k<n;k++){
   if(k!==p&&k!==p+1){J.push(I(N));P.push(I(N));continue}
   let rem=Array.from({length:N},(_,i)=>i).filter(i=>i!==(k===p?a:b)),j=Z(N,N-1),q=Z(N-1,N);
   rem.forEach((v,i)=>{j[v][i]=1n;q[i][v]=1n;if(k===p){q[i][a]=-D[p+1][v][b]/l}else{j[b][i]=-D[p+1][a][v]/l}});
   J.push(j);P.push(q);
  }
  H[p][b][a]=1n/l;
  if(P[p].some(r=>r[a]!==0n)||J[p+1][b].some(x=>x!==0n))nontrivial++;
  let R=[null];for(let k=1;k<n;k++)R.push(mul(mul(P[k-1],D[k]),J[k]));
  for(let k=0;k<n;k++){
   assert(eq(mul(P[k],J[k]),I(sizes[k])),"pi i");
   let left=add(I(N),mul(J[k],P[k]),-1n),right=Z(N,N);
   if(k+1<n)right=add(right,mul(D[k+1],H[k]));
   if(k>0)right=add(right,mul(H[k-1],D[k]));
   assert(eq(left,right),"id-i pi = dh+hd");
   if(k>0){assert(eq(mul(D[k],J[k]),mul(J[k-1],R[k])),"i chain map");assert(eq(mul(P[k-1],D[k]),mul(R[k],P[k])),"pi chain map")}
   if(k>1)assert(eq(mul(R[k-1],R[k]),Z(sizes[k-2],sizes[k])),"reduced chain");
   degreeChecks++;
  }
  // Directly compare the Schur block and adjacent restrictions with the reduced matrices.
  const rows=Array.from({length:N},(_,i)=>i).filter(i=>i!==a),cols=Array.from({length:N},(_,i)=>i).filter(i=>i!==b);
  assert(eq(R[p+1],rows.map(i=>cols.map(j=>D[p+1][i][j]-D[p+1][i][b]*D[p+1][a][j]/l))),"Schur");
  if(p>0)assert(eq(R[p],D[p].map(r=>rows.map(j=>r[j]))),"lower restriction");
  if(p+2<n)assert(eq(R[p+2],cols.map(i=>D[p+2][i])),"upper restriction");
  trials++;
 }
 assert(trials>100&&unitNeg>0&&nontrivial>0,"coverage");return {generated:240,trials,degreeChecks,unitNeg,nontrivial,torsionBlocks};
}
console.log(JSON.stringify(run()));
