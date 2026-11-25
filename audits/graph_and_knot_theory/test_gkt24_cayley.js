// GKT-24-CAYLEY-01: finite cyclic Cayley quotients and reduced words in free groups.
function run(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 let cyclic=0,edges=0,vertices=0,disconnected=0,wordVertices=0,wordSteps=0;
 for(let n=2;n<=14;n++){
  const mod=x=>(x%n+n)%n,orbits=[];for(let x=1;x<n;x++)if(x<=mod(-x))orbits.push([...new Set([x,mod(-x)])]);
  for(let mask=0;mask<2**orbits.length;mask++){
   let S=orbits.flatMap((o,i)=>mask&(1<<i)?o:[]),E=new Set(),A=Array.from({length:n},()=>new Set());
   for(let g=0;g<n;g++)for(let s of S){let h=mod(g+s);assert(g!==h,"no loop");A[g].add(h);E.add([g,h].sort((a,b)=>a-b).join(","))}
   assert(A.every(a=>a.size===S.length),"degree");assert(2*E.size===n*S.length,"undirected count");
   let Q=[0],seen=new Set(Q);while(Q.length)for(let h of A[Q.pop()])if(!seen.has(h)){seen.add(h);Q.push(h)}
   const gcd=(a,b)=>b?gcd(b,a%b):a,d=S.reduce(gcd,n);
   assert(seen.size===n/d,"generated subgroup");if(d>1)disconnected++;
   for(let g=0;g<n;g++)for(let h of A[g])assert(A[mod(g+1)].has(mod(h+1)),"translation");
   cyclic++;edges+=E.size;vertices+=n;
  }
 }
 const reduce=(w,s)=>w.length&&w[w.length-1]===-s?w.slice(0,-1):[...w,s];
 for(let r=1;r<=4;r++){
  let S=Array.from({length:r},(_,i)=>[i+1,-i-1]).flat(),Q=[[]];
  for(let k=0;k<=4;k++){
   assert(Q.length===(k===0?1:2*r*(2*r-1)**(k-1)),"sphere count");
   assert(new Set(Q.map(w=>w.join(","))).size===Q.length,"distinct reduced words");
   let next=[];for(let w of Q){let N=S.map(s=>reduce(w,s));assert(new Set(N.map(v=>v.join(","))).size===2*r,"degree");
    assert(N.filter(v=>v.length===k-1).length===(k?1:0),"unique predecessor");
    for(let i=0;i<S.length;i++)assert(reduce(N[i],-S[i]).join(",")===w.join(","),"inverse");
    wordVertices++;wordSteps+=S.length;next.push(...N.filter(v=>v.length===k+1));
   }Q=next;
  }
 }
 return {cyclic,vertices,edges,disconnected,wordVertices,wordSteps};
}
console.log(JSON.stringify(run()));
