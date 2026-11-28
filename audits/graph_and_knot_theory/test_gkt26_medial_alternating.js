// GKT-26-MEDIAL-ALT-01: enumerate four-valent spherical maps and crossing choices.
function auditMedial(){
 const assert=(b,m)=>{if(!b)throw Error(m)};
 const cycles=p=>{let ids=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(ids[i]<0){let j=i;do{ids[j]=n;j=p[j]}while(j!==i);n++}return[n,ids]};
 let connected=0,planar=0,assignments=0,alternating=0,uniform=0,oneComponent=0,oneComponentAlternating=0,faceEdges=0;
 for(let n=1;n<=3;n++){
 const N=4*n,rot=Array.from({length:N},(_,i)=>4*Math.floor(i/4)+(i+1)%4),a=Array(N).fill(-1);
 function inspect(){let seen=new Set([0]),q=[0];for(let i=0;i<q.length;i++)for(let j of [rot[q[i]],a[q[i]]])if(!seen.has(j)){seen.add(j);q.push(j)}if(seen.size!==N)return;connected++;
 const [f,F]=cycles(a.map(x=>rot[x]));if(n-2*n+f!==2)return;planar++;
 const adj=Array.from({length:f},()=>new Set);for(let d=0;d<N;d++){adj[F[d]].add(F[a[d]]);faceEdges++}let color=Array(f).fill(-1),Q=[0];color[0]=0;for(let i=0;i<Q.length;i++)for(let j of adj[Q[i]]){if(color[j]<0){color[j]=1-color[Q[i]];Q.push(j)}assert(color[j]!==color[Q[i]],"checkerboard")}assert(Q.length===f,"dual connected");
 for(let d=0;d<N;d++)assert(color[F[d]]===color[F[rot[rot[d]]]],"opposite sectors");
 const [orientedComponents]=cycles(a.map(x=>rot[rot[x]]));assert(orientedComponents%2===0,"oriented cycles");if(orientedComponents===2)oneComponent++;
 let localAlternating=0;for(let mask=0;mask<(1<<n);mask++){assignments++;const over=d=>(d%2)===((mask>>Math.floor(d/4))&1);let alt=true;for(let d=0;d<N;d++)if(over(d)===over(a[d]))alt=false;
 const cols=Array.from({length:n},(_,i)=>color[F[4*i+((mask>>i)&1)]]);const uni=cols.every(x=>x===cols[0]);assert(alt===uni,"alternating iff same A color");if(alt){alternating++;localAlternating++;if(orientedComponents===2)oneComponentAlternating++}if(uni)uniform++}
 assert(localAlternating===2,"two assignments");
 }
 function pair(){let i=a.indexOf(-1);if(i<0){inspect();return}for(let j=i+1;j<N;j++)if(a[j]<0){a[i]=j;a[j]=i;pair();a[i]=a[j]=-1}}
 pair();
 }
 return {connected,planar,assignments,alternating,uniform,oneComponent,oneComponentAlternating,faceEdges};
}
console.log('PASS GKT-26-MEDIAL-ALT-01', auditMedial());
