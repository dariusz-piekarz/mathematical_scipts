// AA-67: rank-one quotients and exact cyclic highest-weight modules of type A2.
function verma67(){
 const A=(v,m)=>{if(!v)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 let rankOne=0,relations=0,singular=0,models=0,dimensions=0,weights=0,weylChecks=0,highest=0;
 for(let m=0;m<=20;m++){for(let k=0;k<=m;k++){
  const e=BigInt(k*(m-k+1)),ef=BigInt((k+1)*(m-k)),h=BigInt(m-2*k);
  A(ef-e===h,"sl2 commutation");relations++;
  A((k===0)===(e===0n),"raising kernel");singular++;
 }A((m+1)*(m-(m+1)+1)===0,"singular vector");rankOne++;}
 for(let a=0;a<=4;a++)for(let b=0;b<=4-a;b++){
  const n=a+b,d=3**n,bs=Array.from({length:d},(_,k)=>Array.from({length:n},(_,j)=>Math.floor(k/3**j)%3)),wt=[[1,0],[-1,1],[0,-1]];
  const weight=k=>bs[k].reduce((w,x,j)=>w.map((y,i)=>y+(j<a?1:-1)*wt[x][i]),[0,0]);
  const act=(v,i,raise)=>{let out=Array(d).fill(0n);for(let k=0;k<d;k++)if(v[k])for(let j=0;j<n;j++){const dual=j>=a,from=(raise!==dual)?i+1:i,to=(raise!==dual)?i:i+1;if(bs[k][j]===from)out[k+(to-from)*3**j]+=v[k]*(dual?-1n:1n);}return out;};
  const spaces=new Map(),queue=[];
  const add=(w,v)=>{const key=w.join(",");let rows=spaces.get(key)||[];v=v.slice();for(const [p,u] of rows){if(!v[p])continue;const s=u[p],t=v[p];v=v.map((x,j)=>s*x-t*u[j]);const g=v.reduce(gcd,0n);if(g)v=v.map(x=>x/g);}const p=v.findIndex(x=>x!==0n);if(p<0)return;A(v.every((x,k)=>!x||weight(k).join(",")===key),"homogeneous");rows.push([p,v]);spaces.set(key,rows);queue.push([w,v]);};
  let k=0;for(let j=a;j<n;j++)k+=2*3**j;let v=Array(d).fill(0n);v[k]=1n;add([a,b],v);
  for(let i=0;i<2;i++){A(act(v,i,true).every(x=>!x),"highest");let u=v;for(let j=0;j<=[a,b][i];j++)u=act(u,i,false);A(u.every(x=>!x),"singular quotient relation");highest++;}
  for(let t=0;t<queue.length;t++){const [w,u]=queue[t];for(let i=0;i<2;i++){let z=w.map((x,j)=>x-(i===j?2:-1));add(z,act(u,i,false));}}
  A(queue.length===(a+1)*(b+1)*(a+b+2)/2,"A2 dimension");A(spaces.get(`${a},${b}`).length===1,"top line");
  for(const [key,rows] of spaces){const w=key.split(",").map(Number),delta=[a-w[0],b-w[1]],n1=(2*delta[0]+delta[1])/3,n2=(delta[0]+2*delta[1])/3;A(Number.isInteger(n1)&&Number.isInteger(n2)&&n1>=0&&n2>=0,"root cone");
   for(let i=0;i<2;i++){const s=w.map((x,j)=>x-w[i]*(i===j?2:-1));A(spaces.get(s.join(","))?.length===rows.length,"Weyl symmetry");weylChecks++;}
   weights++;
  }models++;dimensions+=queue.length;
 }
 return {rankOne,relations,singular,models,dimensions,weights,weylChecks,highest};
}
console.log('AA-67 highest weight quotients: PASS',verma67());

// AA-67-QW-01: aa:lem:verma-integrable, weight projections descend to Q.
// Finite supports in the rank-one Verma module; Q kills degrees > m.
// Exact scaled Lagrange projectors, including singleton and zero quotients of weights.
function quotientWeights67(){
 let supports=0,projections=0,coordinates=0;
 for(let m=0;m<=8;m++)for(let n=0;n<=8;n++){
  const h=Array.from({length:n+1},(_,k)=>BigInt(m-2*k));
  const v=h.map((_,k)=>BigInt((k+1)*(-1)**k));
  const q=w=>w.slice(0,m+1);
  let sum=v.map(()=>0n);
  for(let j=0;j<h.length;j++){
   let den=1n;
   for(let k=0;k<h.length;k++)if(k!==j)den*=h[j]-h[k];
   const p=w=>w.map((x,i)=>{
    let num=x;
    for(let k=0;k<h.length;k++)if(k!==j)num*=h[i]-h[k];
    if(num%den!==0n)throw Error("nonintegral projection");
    return num/den;
   });
   const w=p(v),left=q(w),right=p(q(v));
   if(left.length!==right.length||left.some((x,i)=>x!==right[i]))throw Error("projection does not descend");
   w.forEach((x,i)=>{if(x!==(i===j?v[i]:0n))throw Error("wrong weight component");sum[i]+=x;coordinates++;});
   if(j>m&&left.some(x=>x!==0n))throw Error("discarded weight survives");
   projections++;
  }
  if(sum.some((x,i)=>x!==v[i]))throw Error("weight components do not sum to original vector");
  supports++;
 }
 return {supports,projections,coordinates};
}
console.log("AA-67-QW-01: PASS",quotientWeights67());
