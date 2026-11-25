// GKT-22-CANCEL-01: simplicial chain cancellation over Z, check mod p homology.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)}, pop=x=>{let n=0;while(x){n+=x&1;x>>=1}return n};
 let seed=20261125;function rnd(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n}
 function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){let j=rnd(i+1);[a[i],a[j]]=[a[j],a[i]]}return a}
 function rank(A,p){if(!A.length)return 0;let M=A.map(r=>r.map(x=>(x%p+p)%p)),r=0;for(let j=0;j<M[0].length&&r<M.length;j++){let i=M.findIndex((a,i)=>i>=r&&a[j]!==0);if(i<0)continue;[M[i],M[r]]=[M[r],M[i]];let inv=1;while(M[r][j]*inv%p!==1)inv++;M[r]=M[r].map(x=>x*inv%p);for(let i=r+1;i<M.length;i++){let a=M[i][j];M[i]=M[i].map((x,k)=>(x-a*M[r][k]%p+p)%p)}r++}return r}
 function betti(C,D,p){return C.map((c,d)=>c.length-(d?rank(D[d],p):0)-(d+1<C.length?rank(D[d+1],p):0))}
 function square(C,D){for(let d=2;d<C.length;d++)for(let i=0;i<C[d-2].length;i++)for(let j=0;j<C[d].length;j++)assert(D[d-1][i].reduce((s,x,k)=>s+x*D[d][k][j],0)===0,"boundary square")}
 function acyclic(S,inc,P){let m=new Set(P.map(e=>e.join(","))),A=new Map(S.map(x=>[x,[]])),I=new Map(S.map(x=>[x,0]));for(let [a,b] of inc){if(m.has([a,b].join(",")))[a,b]=[b,a];A.get(a).push(b);I.set(b,I.get(b)+1)}let Q=S.filter(x=>!I.get(x)),n=0;while(Q.length){let x=Q.pop();n++;for(let y of A.get(x)){I.set(y,I.get(y)-1);if(!I.get(y))Q.push(y)}}return n===S.length}
 let complexes=0,eliminations=0,adjacent=0,changed=0,fieldChecks=0;
 for(let trial=0;trial<240;trial++){
  let n=3+trial%4, S0=new Set();for(let x=1;x<1<<n;x++)if(rnd(100)<(trial%5===0?5:20)){for(let y=x;y;y=(y-1)&x)S0.add(y)}
  let S=[...S0].sort((a,b)=>a-b),C0=Array.from({length:n},(_,d)=>S.filter(x=>pop(x)===d+1)),inc=[];for(let b of S)if(pop(b)>1)for(let a of S)if((a&b)===a&&pop(a)+1===pop(b))inc.push([a,b]);
  let P=[],used=new Set();for(let [a,b] of shuffle(inc))if(!used.has(a)&&!used.has(b)&&acyclic(S,inc,[...P,[a,b]])){P.push([a,b]);used.add(a);used.add(b)}
  let D0=C0.map((c,d)=>d?C0[d-1].map(a=>c.map(b=>{if((a&b)!==a)return 0;let removed=b^a;return (-1)**pop(b&(removed-1))})):[]);
  square(C0,D0);let dims=[...new Set(P.map(([a])=>pop(a)-1))];if(dims.some(d=>dims.includes(d+1)))adjacent++;
  for(let order of [dims.sort((a,b)=>a-b),[...dims].reverse()]){
   let C=C0.map(x=>[...x]),D=D0.map(A=>A.map(r=>[...r])),left=[...P];
   for(let d of order){let group=left.filter(([a])=>pop(a)-1===d);
    while(group.length){let index=group.findIndex(([a,b])=>group.every(([x,y])=>x===a||D[d+1][C[d].indexOf(a)][C[d+1].indexOf(y)]===0));assert(index>=0,"topological first pair");
     let [a,b]=group.splice(index,1)[0],i=C[d].indexOf(a),j=C[d+1].indexOf(b),A=D[d+1],l=A[i][j];assert(Math.abs(l)===1,"unit pivot");
     let rest=left.filter(([x,y])=>x!==a||y!==b);let old=rest.map(([x,y])=>{let e=pop(x)-1;return D[e+1][C[e].indexOf(x)][C[e+1].indexOf(y)]});
     D[d+1]=A.filter((_,k)=>k!==i).map((row,k)=>row.flatMap((v,h)=>{if(h===j)return [];let w=v-row[j]*A[i][h]/l;if(w!==v)changed++;return [w]}));
     if(d>0)D[d]=D[d].map(row=>row.filter((_,k)=>k!==i));if(d+2<n)D[d+2]=D[d+2].filter((_,k)=>k!==j);C[d].splice(i,1);C[d+1].splice(j,1);
     rest.forEach(([x,y],k)=>{let e=pop(x)-1;assert(D[e+1][C[e].indexOf(x)][C[e+1].indexOf(y)]===old[k],"other matched pivots unchanged")});left=rest;square(C,D);eliminations++;
    }
   }
   assert(C.every((c,d)=>c.join(",")===C0[d].filter(x=>!used.has(x)).join(",")),"critical basis");
   for(let p of [2,3,5,7]){assert(betti(C,D,p).join(",")===betti(C0,D0,p).join(","),"homology");fieldChecks++}
  }complexes++;
 }
 assert(adjacent>0&&changed>0,"coverage");return {complexes,adjacent,eliminations,changed,fieldChecks};
}
console.log(JSON.stringify(run()));
