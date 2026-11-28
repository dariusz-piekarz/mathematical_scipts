// GKT-12-18-DELTA-01: independent finite regression; not a proof.
function control12and18(){
 const check=(ok,msg)=>{if(!ok)throw Error(msg)};
 let models=[],cutChecks=0,bfsRoots=0;
 for(let h=2;h<=6;h++){
  const m=2**(h+1)-1,n=2*m,A=Array.from({length:n},()=>new Set());
  const add=(u,v)=>{check(u!==v&&!A[u].has(v),"simple");A[u].add(v);A[v].add(u)};
  add(0,m);for(const off of [0,m]){for(let i=1;i<m;i++)add(off+i,off+Math.floor((i-1)/2));const L=2**h-1;for(let i=L;i<m;i++)add(off+i,off+(i===m-1?L:i+1))}
  check(A.every(s=>s.size===3),"degree");
  let diam=0;for(let r=0;r<n;r++){bfsRoots++;let q=[r],d=Array(n).fill(-1);d[r]=0;for(let i=0;i<q.length;i++)for(const v of A[q[i]])if(d[v]===-1){d[v]=d[q[i]]+1;q.push(v)}check(q.length===n,"connected");diam=Math.max(diam,...d)}
  check(diam===2*h+1&&diam===2*Math.log2(n+2)-3,"diameter");
  let bridge=0;for(let u=0;u<m;u++)for(const v of A[u])if(v>=m)bridge++;check(bridge===1,"half cut");
  if(h===2)for(let mask=1;mask<(1<<n);mask++){let k=0,c=0;for(let u=0;u<n;u++)if(mask&(1<<u)){k++;for(const v of A[u])if(!(mask&(1<<v)))c++}if(k<=m){cutChecks++;check(c*m>=k,"conductance lower bound")}}
  models.push({h,n,diam,phi:`1/${3*m}`})
 }
 let maps=0,treePairs=0,dualCuts=0,loopMaps=0,parallelMaps=0,nonSpherical=0;
 const pop=x=>{let r=0;for(;x;x&=x-1)r++;return r};
 function cycles(p){const id=Array(p.length).fill(-1);let count=0;for(let i=0;i<p.length;i++)if(id[i]<0){let j=i;do{id[j]=count;j=p[j]}while(j!==i);count++}return [count,id]}
 function isConnected(n,E,mask){const p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};for(let i=0;i<E.length;i++)if(mask&(1<<i)){let [u,v]=E[i];p[root(u)]=root(v)}return new Set(p.map((_,i)=>root(i))).size===1}
 function process(p,m){
  const [n,V]=cycles(p),[f,F]=cycles(p.map((_,i)=>p[i^1]));const E=[],D=[];for(let i=0;i<m;i++){E.push([V[2*i],V[2*i+1]]);D.push([F[2*i],F[2*i+1]])}
  const all=(1<<m)-1;if(!isConnected(n,E,all))return;if(n-m+f!==2){nonSpherical++;return}maps++;check(isConnected(f,D,all),"dual connected");
  if(E.some(([u,v])=>u===v))loopMaps++;if(new Set(E.map(e=>[...e].sort((a,b)=>a-b).join(","))).size<m)parallelMaps++;
  for(let mask=0;mask<=all;mask++){const t=pop(mask)===n-1&&isConnected(n,E,mask),dt=pop(all^mask)===f-1&&isConnected(f,D,all^mask);check(t===dt,"dual tree bijection");if(t)treePairs++}
  for(let S=1;S<(1<<f)-1;S++){dualCuts++;const parity=Array(n).fill(0);let count=0;D.forEach(([u,v],i)=>{if(Boolean(S&(1<<u))!==Boolean(S&(1<<v))){count++;parity[E[i][0]]^=1;parity[E[i][1]]^=1}});check(count>0&&parity.every(x=>x===0),"dual cut parity")}
 }
 for(let m=1;m<=4;m++){let p=Array.from({length:2*m},(_,i)=>i);function gen(k){if(k===p.length){process(p,m);return}for(let j=k;j<p.length;j++){[p[k],p[j]]=[p[j],p[k]];gen(k+1);[p[k],p[j]]=[p[j],p[k]]}}gen(0)}
 return {models,bfsRoots,cutChecks,maps,treePairs,dualCuts,loopMaps,parallelMaps,nonSpherical};
}
console.log('PASS GKT-12-18-DELTA-01', control12and18());
