"use strict";
function control(){
  const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  const maps=(n,m)=>{let a=[[]];for(let i=0;i<n;i++)a=a.flatMap(x=>Array.from({length:m},(_,j)=>[...x,j]));return a};
  const comp=(g,f)=>f.map(i=>g[i]);
  const assert=(b)=>{if(!b)throw Error("control failure")};
  let squares=0, parallel=0, negative=0, recurrence=0;
  // Square indexed by [1]x[1]: compare direct compatible quadruples with two nested limits.
  for(let a=0;a<=2;a++)for(let b=0;b<=2;b++)for(let c=0;c<=2;c++)for(let d=0;d<=2;d++)
  for(const f of maps(a,b))for(const g of maps(a,c))for(const h of maps(b,d))for(const k of maps(c,d)){
    if(!eq(comp(h,f),comp(k,g)))continue;
    let direct=[],horizontal=[],vertical=[];
    for(let x=0;x<a;x++)for(let y=0;y<b;y++)for(let z=0;z<c;z++)for(let w=0;w<d;w++)
      if(f[x]===y&&g[x]===z&&h[y]===w&&k[z]===w)direct.push([x,y,z,w]);
    for(let x=0;x<a;x++)for(let z=0;z<c;z++)if(g[x]===z&&h[f[x]]===k[z])horizontal.push([x,f[x],z,k[z]]);
    for(let x=0;x<a;x++)for(let y=0;y<b;y++)if(f[x]===y&&k[g[x]]===h[y])vertical.push([x,y,g[x],h[y]]);
    assert(eq(direct,horizontal)&&eq(direct,vertical));squares++;
  }
  // Non-thin filtered category 0 => 1 -> 2, terminal 2. Check equivalence
  // closure on tagged elements by graph reachability versus common-target equality.
  for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)for(let c=0;c<=3;c++)
  for(const f of maps(a,b))for(const g of maps(a,b))for(const h of maps(b,c)){
    if(!eq(comp(h,f),comp(h,g)))continue;
    const n=a+b+c, adj=Array.from({length:n},()=>[]);
    const link=(x,y)=>{adj[x].push(y);adj[y].push(x)};
    for(let i=0;i<a;i++){link(i,a+f[i]);link(i,a+g[i])}
    for(let i=0;i<b;i++)link(a+i,a+b+h[i]);
    const final=[...comp(h,f),...h,...Array.from({length:c},(_,i)=>i)];
    for(let i=0;i<n;i++){let seen=new Set([i]),todo=[i];while(todo.length){for(const j of adj[todo.pop()])if(!seen.has(j)){seen.add(j);todo.push(j)}}
      for(let j=0;j<n;j++){assert(seen.has(j)===(final[i]===final[j]));parallel++}}
  }
  // Nonfiltered parallel arrows from singleton to two points: quotient identifies
  // distinct target elements, but target object has only its identity out of it.
  for(const f of maps(1,2))for(const g of maps(1,2))if(!eq(f,g)){
    const closure=new Set([f[0],g[0]]);
    assert(closure.size===2&&f[0]!==g[0]);negative++;
  }
  // Solve finite truncations of a_n-u_n(a_{n+1})=b_n for all cyclic
  // surjective transition maps (not only identities).
  for(let m=2;m<=9;m++)for(let r=0;r<m;r++){
    const u=Array.from({length:m},(_,x)=>(r*x)%m);if(new Set(u).size!==m)continue;
    for(const b of maps(3,m)){let a=0;for(const v of b){const next=u.indexOf((a-v+m)%m);assert(next>=0&&(a-u[next]+m)%m===v);a=next}recurrence++}
  }
  return {squares,parallel,negative,recurrence,total:squares+parallel+negative+recurrence}
}
console.log(JSON.stringify(control()));
