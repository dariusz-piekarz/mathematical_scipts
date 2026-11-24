// AA-67: Weyl averaging bound, including nonsymmetric Cartan matrices and reducible systems.
function bound67(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const I=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1:0));
 const mul=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0)));
 const mv=(A,v)=>A.map(r=>r.reduce((s,x,k)=>s+x*v[k],0));
 const det=A=>A.length===1?A[0][0]:A[0].reduce((s,x,j)=>s+(-1)**j*x*det(A.slice(1).map(r=>r.filter((_,k)=>k!==j))),0);
 function solve(A,v){const d=det(A);return A.map((_,j)=>det(A.map((r,i)=>r.map((x,k)=>k===j?v[i]:x)))/d);}
 function tuples(n,max){if(!n)return [[]];return Array.from({length:max+1},(_,i)=>tuples(n-1,max).map(t=>[i,...t])).flat();}
 let groups=0,groupElements=0,dominants=0,orbitMembers=0,accepted=0,rejected=0,componentChecks=0;
 for(const [A,size] of [[[[2]],2],[[[2,-1],[-1,2]],6],[[[2,-2],[-1,2]],8],[[[2,-3],[-1,2]],12],[[[2,0],[0,2]],4],[[[2,-1,0],[-1,2,-1],[0,-1,2]],24],[[[2,-1,0],[-1,2,-2],[0,-1,2]],48]]){
  const n=A.length,gens=I(n).map((_,i)=>I(n).map((r,j)=>r.map((x,k)=>x-(k===i?A[j][i]:0))));
  const list=[I(n)],seen=new Set([JSON.stringify(list[0])]);
  for(let i=0;i<list.length;i++)for(const s of gens){const t=mul(s,list[i]),k=JSON.stringify(t);if(!seen.has(k)){seen.add(k);list.push(t);assert(list.length<=size,"group size upper bound");}}
  assert(list.length===size,"group size");groups++;groupElements+=size;
  for(const l of tuples(n,3)){
   const b=solve(A,l.map(x=>x*size));assert(b.every(x=>Number.isInteger(x)&&x>=0),"integer nonnegative average bound");dominants++;
   const avg=Array(n).fill(0);for(const w of list){const v=mv(w,l);v.forEach((x,j)=>avg[j]+=x);let diff=solve(A,l.map((x,j)=>x-v[j]));assert(diff.every((x,j)=>Number.isInteger(x)&&x>=0&&x<=b[j]),"highest orbit in cone and bound");orbitMembers++;}
   assert(avg.every(x=>x===0),"Weyl average");
   for(const k of tuples(n,6)){
    const v=mv(A,k),mu=l.map((x,j)=>x-v[j]);let sums=Array(n).fill(0),ok=true;
    for(const w of list){const wm=mv(w,mu),q=solve(A,l.map((x,j)=>x-wm[j]));assert(q.every(Number.isInteger),"root lattice congruence");if(q.some(x=>x<0))ok=false;q.forEach((x,j)=>sums[j]+=x);}
    assert(sums.every((x,j)=>x===b[j]),"sum of orbit differences");
    if(ok){assert(k.every((x,j)=>x<=b[j]),"finite box");accepted++;}else rejected++;
    componentChecks+=n;
   }
  }
 }
 return {groups,groupElements,dominants,orbitMembers,accepted,rejected,componentChecks};
}
console.log('AA-67 Weyl averaging: PASS',bound67());
