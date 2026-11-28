// GKT-26-TAIT-STATES-01: exact local smoothing and Laurent polynomial regression.
function controlTaitStates(){
 const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
 const cycles=p=>{let id=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(id[i]<0){let j=i;do{id[j]=n;j=p[j]}while(j!==i);n++}return [n,id]};
 const dsu=n=>{let p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};return {join:(u,v)=>{p[root(u)]=root(v)},count:()=>new Set(p.map((_,i)=>root(i))).size}};
 const pop=x=>{let c=0;for(;x;x&=x-1)c++;return c};
 const multiply=(P,Q)=>{let R=new Map;for(const [a,x] of P)for(const [b,y] of Q)R.set(a+b,(R.get(a+b)||0n)+x*y);return R};
 const pow=(P,k)=>{assert(k>=0,"negative exponent");let R=new Map([[0,1n]]);while(k--)R=multiply(R,P);return R};
 const add=(P,Q,shift)=>{for(const [i,x] of Q)P.set(i+shift,(P.get(i+shift)||0n)+x)};
 const delta=new Map([[2,-1n],[-2,-1n]]), xm=new Map([[-4,-1n],[0,-1n]]),ym=new Map([[4,-1n],[0,-1n]]);
 let maps=0,states=0,coeffs=0,loops=0,parallel=0;
 function inspect(p,m){const [v,V]=cycles(p),[f]=cycles(p.map((_,i)=>p[i^1]));const conn=dsu(v),E=[];for(let i=0;i<m;i++){E.push([V[2*i],V[2*i+1]]);conn.join(...E[i])}if(conn.count()!==1||v-m+f!==2)return;maps++;if(E.some(([a,b])=>a===b))loops++;if(new Set(E.map(e=>[...e].sort((a,b)=>a-b).join(","))).size<m)parallel++;
  let bracket=new Map,T=new Map;
  for(let mask=0;mask<(1<<m);mask++){states++;let C=dsu(v);for(let i=0;i<m;i++)if(mask&(1<<i))C.join(...E[i]);const k=C.count(),a=pop(mask);
   // Independently glue the local two smoothings on the medial diagram.
   let S=dsu(4*m);for(let d=0;d<2*m;d++)S.join(2*d+1,2*p[d]);
   for(let i=0;i<m;i++){let d=2*i,e=d+1;if(mask&(1<<i)){S.join(2*d,2*e+1);S.join(2*d+1,2*e)}else{S.join(2*d,2*d+1);S.join(2*e,2*e+1)}}
   const b=S.count();assert(b===2*k-v+a,"state circles");assert(b>=1,"nonempty state");
   add(bracket,pow(delta,b-1),2*a-m);
   add(T,multiply(pow(xm,k-1),pow(ym,a-v+k)),2*v-m-2);
  }
  for(const i of new Set([...bracket.keys(),...T.keys()])){coeffs++;assert((bracket.get(i)||0n)===(T.get(i)||0n),"Laurent coefficient")}
 }
 for(let m=1;m<=3;m++){let p=Array.from({length:2*m},(_,i)=>i);function perm(k){if(k===p.length){inspect(p,m);return}for(let j=k;j<p.length;j++){[p[k],p[j]]=[p[j],p[k]];perm(k+1);[p[k],p[j]]=[p[j],p[k]]}}perm(0)}
 return {maps,states,coeffs,loops,parallel};
}
console.log('PASS GKT-26-TAIT-STATES-01', controlTaitStates());
