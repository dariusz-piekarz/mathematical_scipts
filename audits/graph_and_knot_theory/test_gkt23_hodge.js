// GKT-23-HODGE-01: exact integer-scaled weighted adjoints and harmonic decomposition.
function run(){
 const assert=(v,m)=>{if(!v)throw Error(m)},Z=(r,c)=>Array.from({length:r},()=>Array(c).fill(0n)),I=n=>Z(n,n).map((r,i)=>r.map((_,j)=>i===j?1n:0n)),T=A=>A[0].map((_,j)=>A.map(r=>r[j])),M=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0n))),S=(A,k)=>A.map(r=>r.map(x=>x*k)),A=(X,Y)=>X.map((r,i)=>r.map((x,j)=>x+Y[i][j])),eq=(X,Y)=>X.length===Y.length&&X.every((r,i)=>r.length===Y[i].length&&r.every((x,j)=>x===Y[i][j]));
 const B=[[-1n,0n,1n],[1n,-1n,0n],[0n,1n,-1n]],D0=T(B),D1=[[1n,1n,1n]];
 const det=X=>X.length===1?X[0][0]:X[0].reduce((s,x,j)=>s+(j%2?-1n:1n)*x*det(X.slice(1).map(r=>r.filter((_,k)=>k!==j))),0n);
 function adj(X){if(X.length===1)return [[1n]];return X.map((r,i)=>r.map((_,j)=>(i+j)%2?-det(X.filter((_,k)=>k!==j).map(r=>r.filter((_,k)=>k!==i))):det(X.filter((_,k)=>k!==j).map(r=>r.filter((_,k)=>k!==i)))))}
 let models=0,nonstandard=0,harmonic=0,filled=0;
 for(let k=-3;k<=3;k++)for(let l=-3;l<=3;l++)for(let m=1;m<=4;m++){
  let U=[[1n,BigInt(k),0n],[0n,1n,BigInt(l)],[0n,0n,1n]],V=[[1n,0n,BigInt(l)],[BigInt(k),1n,0n],[0n,0n,1n]];
  let G0=M(T(U),U),G1=S(M(T(V),V),BigInt(m)),G2=[[BigInt(m+1)]],q0=det(G0),q1=det(G1);
  let E0=M(M(adj(G0),T(D0)),G1),E1=M(M(adj(G1),T(D1)),G2);
  assert(eq(M(G0,E0),S(M(T(D0),G1),q0)),"adjoint d0");assert(eq(M(G1,E1),S(M(T(D1),G2),q1)),"adjoint d1");
  if(!eq(E0,S(T(D0),q0))||!eq(E1,S(T(D1),q1)))nonstandard++;
  assert(eq(M(D1,D0),[[0n,0n,0n]]),"cochain identity");
  let L=M(D0,E0),Lf=A(S(L,q1),S(M(E1,D1),q0));
  assert(eq(M(G1,L),T(M(G1,L)))&&eq(M(G1,Lf),T(M(G1,Lf))),"weighted self-adjointness");
  // h=G1^{-1}(1,1,1)^T up to nonzero scalar; kernel of d0*.
  let h=M(adj(G1),[[1n],[1n],[1n]]);assert(eq(M(L,h),[[0n],[0n],[0n]])&&h.some(r=>r[0]!==0n),"harmonic cycle");
  assert(det(L)===0n&&L.some((r,i)=>r.some((_,j)=>det(L.filter((_,a)=>a!==i).map(r=>r.filter((_,b)=>b!==j)))!==0n)),"rank two");
  assert(det(Lf)!==0n,"filled triangle invertible");
  models++;harmonic++;filled++;
 }
 assert(eq(A(M(D0,T(D0)),M(T(D1),D1)),S(I(3),3n)),"unweighted filled Laplacian");return {models,nonstandard,harmonic,filled};
}
console.log(JSON.stringify(run()));
