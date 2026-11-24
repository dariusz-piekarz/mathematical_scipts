// AA-64: Fitting decomposition over F_101, conjugated nilpotent/invertible blocks.
function fitting64(){
 const p=101,mod=x=>((x%p)+p)%p,assert=(v,m)=>{if(!v)throw Error(m)};
 const inv=x=>{for(let y=1;y<p;y++)if(mod(x*y)===1)return y;throw Error("inverse")};
 const id=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>+(i===j)));
 const mul=(A,B)=>A.map(r=>B[0].map((_,j)=>mod(r.reduce((s,x,k)=>s+x*B[k][j],0))));
 function reduce(A){let a=A.map(r=>r.map(mod)),r=0,piv=[];for(let j=0;j<a[0].length&&r<a.length;j++){let k=a.findIndex((row,i)=>i>=r&&row[j]);if(k<0)continue;[a[r],a[k]]=[a[k],a[r]];let u=inv(a[r][j]);a[r]=a[r].map(x=>mod(x*u));for(let i=0;i<a.length;i++)if(i!==r){let c=a[i][j];a[i]=a[i].map((x,l)=>mod(x-c*a[r][l]));}piv.push(j);r++;}return [a,piv];}
 const rank=A=>reduce(A)[1].length;
 const nullspace=A=>{let [R,piv]=reduce(A),n=A[0].length;return Array.from({length:n},(_,i)=>i).filter(i=>!piv.includes(i)).map(j=>Array.from({length:n},(_,i)=>i===j?1:piv.includes(i)?mod(-R[piv.indexOf(i)][j]):0));};
 const trans=A=>A[0].map((_,j)=>A.map(r=>r[j]));
 let models=0,powers=0,strict=0;
 for(let n=1;n<=9;n++)for(let k=0;k<=n;k++)for(let trial=0;trial<3;trial++){
  let A=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i<k&&j<k?+(j===i+1):i>=k&&j>=k?(i===j?trial+1:j===i+1?2:0):0));
  let U=id(n),V=id(n);for(let i=0;i<n-1;i++){let E=id(n),Ei=id(n);E[i+1][i]=trial+2;Ei[i+1][i]=mod(-trial-2);U=mul(E,U);V=mul(V,Ei);}A=mul(mul(U,A),V);
  let B=id(n);for(let i=0;i<n;i++){let C=mul(A,B);assert(rank(C)<=rank(B),"monotonic");powers++;B=C;}
  assert(rank(B)===n-k,"stable rank");assert(rank(mul(A,B))===n-k,"image stable");
  const K=nullspace(B);assert(K.length===k,"nullity");
  const cols=[...trans(B),...K];assert(rank(trans(cols))===n,"direct decomposition");
  assert(rank(mul(B,B))===rank(B),"intersection");
  if(k>=2){assert(rank(A)>rank(B),"ordinary vs generalized null");strict++;}
  models++;
 }
 return {models,powers,strict};
}
console.log('AA-64 Fitting decomposition: PASS',fitting64());
