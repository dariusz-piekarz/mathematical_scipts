// GKT-02-04-06-CUT-BFS-01; independent finite models, not a proof or Lean.
function verifyCutBfs(){
 const check=(ok,msg)=>{if(!ok)throw Error(msg)};
 let graphs=0, roots=0, distances=0, cuts=0, removals=0, pairs=0, connected=0;
 for(let n=1;n<=5;n++){
  const E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([u,v]);
  const full=(1<<n)-1;
  function parts(mask){const p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};E.forEach(([u,v],i)=>{if(mask&(1<<i))p[root(u)]=root(v)});return p.map((_,i)=>root(i))}
  const pop=x=>{let k=0;while(x){x&=x-1;k++}return k};
  for(let mask=0;mask<(1<<E.length);mask++){
   graphs++;
   const A=Array.from({length:n},()=>[]), D=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?0:Infinity));
   E.forEach(([u,v],i)=>{if(mask&(1<<i)){A[u].push(v);A[v].push(u);D[u][v]=D[v][u]=1}});
   for(let k=0;k<n;k++)for(let i=0;i<n;i++)for(let j=0;j<n;j++)D[i][j]=Math.min(D[i][j],D[i][k]+D[k][j]);
   for(const reverse of [false,true])for(let s=0;s<n;s++){
    roots++;const d=Array(n).fill(Infinity),p=Array(n).fill(-1),q=[s];d[s]=0;
    let last=-1;
    for(let i=0;i<q.length;i++){
     const u=q[i];check(d[u]>=last,"dequeue order");last=d[u];
     const neighbors=reverse?[...A[u]].reverse():A[u];
     for(const v of neighbors)if(d[v]===Infinity){d[v]=d[u]+1;p[v]=u;q.push(v)}
     for(let j=i+2;j<q.length;j++)check(d[q[j-1]]<=d[q[j]],"queue order");
     if(i+1<q.length)check(d[q[q.length-1]]-d[q[i+1]]<=1,"queue width");
    }
    check(new Set(q).size===q.length,"repeated queue vertex");
    for(let v=0;v<n;v++){distances++;check(d[v]===D[s][v],"distance");if(!Number.isFinite(d[v])||v===s){check(p[v]===-1,"unexpected parent");continue}let u=v;for(let k=d[v];k>0;k--){check(p[u]>=0&&A[u].includes(p[u])&&d[p[u]]===k-1,"parent chain");u=p[u]}check(u===s,"chain root")}
   }
   const comp=parts(mask), isConnected=new Set(comp).size===1;if(isConnected)connected++;
   const byCut=Array.from({length:n},()=>Array(n).fill(Infinity)),byRemoval=Array.from({length:n},()=>Array(n).fill(Infinity));
   let globalCut=Infinity,globalRemoval=Infinity;
   for(let S=1;S<full;S++){
    cuts++;let boundary=0;E.forEach(([u,v],i)=>{if((mask&(1<<i))&&Boolean(S&(1<<u))!==Boolean(S&(1<<v)))boundary|=1<<i});
    const size=pop(boundary);globalCut=Math.min(globalCut,size);const rest=parts(mask^boundary);
    for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)if(Boolean(S&(1<<u))!==Boolean(S&(1<<v))){check(rest[u]!==rest[v],"cut does not separate");byCut[u][v]=Math.min(byCut[u][v],size)}
    if(isConnected)check(size>0,"empty proper cut in connected graph");
   }
   for(let F=mask;;F=(F-1)&mask){
    removals++;const p=parts(mask^F),size=pop(F);if(new Set(p).size>1)globalRemoval=Math.min(globalRemoval,size);
    for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)if(p[u]!==p[v])byRemoval[u][v]=Math.min(byRemoval[u][v],size);
    if(F===0)break;
   }
   for(let u=0;u<n;u++)for(let v=u+1;v<n;v++){pairs++;check(byCut[u][v]===byRemoval[u][v],"minimum s,t separator")}
   if(n>=2){check(globalCut===globalRemoval,"global minimum cut");if(isConnected)check(globalCut<=Math.min(...A.map(a=>a.length)),"degree upper bound")}
  }
 }
 return {graphs,connected,roots,distances,cuts,removals,pairs};
}
console.log('PASS GKT-02-04-06-CUT-BFS-01', verifyCutBfs());
