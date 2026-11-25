// GKT-23-HARMONIC-MIN-01: exact weighted harmonic representatives and norm minimization on C3.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),mv=(A,x)=>A.map(r=>dot(r,x)),trans=A=>A[0].map((_,j)=>A.map(r=>r[j])),mul=(A,B)=>A.map(r=>trans(B).map(c=>dot(r,c))),norm=(G,x)=>dot(x,mv(G,x)),det=A=>A.length===1?A[0][0]:A[0].reduce((s,x,j)=>s+((j%2)?-1n:1n)*x*det(A.slice(1).map(r=>r.filter((_,k)=>k!==j))),0n),adj=A=>A.map((r,i)=>r.map((_,j)=>((i+j)%2?-1n:1n)*det(A.filter((_,k)=>k!==j).map(r=>r.filter((_,k)=>k!==i)))));
 let metrics=0,representatives=0,strict=0,zero=0;
 const one=[1n,1n,1n];
 for(let k=-3;k<=3;k++)for(let l=-3;l<=3;l++)for(let m=1;m<=4;m++){
  let U=[[BigInt(m),BigInt(k),0n],[0n,1n,BigInt(l)],[0n,0n,1n]],G=mul(trans(U),U),h=mv(adj(G),one),den=dot(one,h);
  assert(den>0n,"positive harmonic normalizer");
  let Gh=mv(G,h);assert(Gh.every(x=>x===det(G)),"harmonic adjoint");
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++){
   let z=[BigInt(a),BigInt(b),BigInt(c)],v=z.map(x=>x*den),H=h.map(x=>x*dot(one,z)),e=v.map((x,i)=>x-H[i]);
   assert(dot(one,e)===0n,"same cohomology class");
   // d0(u)=(u_b-u_a,u_c-u_b,u_a-u_c); solve exact difference.
   let u=[0n,e[0],e[0]+e[1]];assert(e[2]===u[0]-u[2],"exact difference");
   assert(dot(H,mv(G,e))===0n,"orthogonality");
   assert(norm(G,v)===norm(G,H)+norm(G,e),"Pythagorean identity");
   if(e.some(x=>x!==0n)){assert(norm(G,v)>norm(G,H),"strict norm minimization");strict++}else zero++;
   representatives++;
  }metrics++;
 }return {metrics,representatives,strict,zero};
}
console.log(JSON.stringify(run()));
