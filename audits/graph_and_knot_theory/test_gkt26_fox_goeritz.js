// GKT-26-FOX-GOERITZ-01: independent modular Fox arc vs Goeritz nullity.
function foxGoeritzControl(){
 const ck=(x,m)=>{if(!x)throw Error(m)};
 function cycles(p){let F=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(F[i]<0){let j=i;do{F[j]=n;j=p[j]}while(j!==i);n++}return[n,F]}
 function dsu(n){let p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};return {root,join:(i,j)=>{p[root(i)]=root(j)}}}
 function rank(A,p){let M=A.map(r=>r.map(x=>(x%p+p)%p)),r=0;for(let j=0;j<(M[0]?.length||0)&&r<M.length;j++){let i=r;while(i<M.length&&!M[i][j])i++;if(i===M.length)continue;[M[i],M[r]]=[M[r],M[i]];let inv=1;while(inv*M[r][j]%p!==1)inv++;M[r]=M[r].map(x=>x*inv%p);for(let k=r+1;k<M.length;k++){let c=M[k][j];if(c)M[k]=M[k].map((x,l)=>(x-c*M[r][l]%p+p)%p)}r++}return r}
 let maps=0,choices=0,knots=0,checks=0,oddChecks=0;
 for(let n=1;n<=3;n++){let N=4*n,rot=Array.from({length:N},(_,i)=>4*Math.floor(i/4)+(i+1)%4),a=Array(N).fill(-1);
 function inspect(){let q=[0],seen=new Set(q);for(let i=0;i<q.length;i++)for(const j of [rot[q[i]],a[q[i]]])if(!seen.has(j)){seen.add(j);q.push(j)}if(q.length!==N)return;let [f,F]=cycles(a.map(x=>rot[x]));if(n-2*n+f!==2)return;maps++;let adj=Array.from({length:f},()=>[]);for(let d=0;d<N;d++)adj[F[d]].push(F[a[d]]);let C=Array(f).fill(-1),fq=[0];C[0]=0;for(let i=0;i<fq.length;i++)for(let j of adj[fq[i]]){if(C[j]<0){C[j]=1-C[fq[i]];fq.push(j)}ck(C[j]!==C[fq[i]],"color")}const isKnot=cycles(a.map(x=>rot[rot[x]]))[0]===2;
 for(let mask=0;mask<(1<<n);mask++){choices++;if(isKnot)knots++;let U=dsu(N);for(let d=0;d<N;d++)U.join(d,a[d]);for(let i=0;i<n;i++){let o=(mask>>i)&1;U.join(4*i+o,4*i+o+2)}let ids=[...new Set(Array.from({length:N},(_,i)=>U.root(i)))],arc=d=>ids.indexOf(U.root(d));let A=Array.from({length:n},()=>Array(ids.length).fill(0));for(let i=0;i<n;i++){let o=(mask>>i)&1;A[i][arc(4*i+o)]+=2;A[i][arc(4*i+1-o)]--;A[i][arc(4*i+3-o)]--}
 for(let col of [0,1]){let faces=C.map((x,i)=>x===col?i:-1).filter(x=>x>=0),v=faces.length,L=Array.from({length:v},()=>Array(v).fill(0));for(let i=0;i<n;i++){let d=4*i+(C[F[4*i]]===col?0:1),u=faces.indexOf(F[d]),z=faces.indexOf(F[rot[rot[d]]]),w=C[F[4*i+((mask>>i)&1)]]===col?1:-1;if(u!==z){L[u][u]+=w;L[z][z]+=w;L[u][z]-=w;L[z][u]-=w}}
 const R=L.slice(1).map(r=>r.slice(1));for(const p of [2,3,5,7]){const aNull=ids.length-rank(A,p),gNull=v-1-rank(R,p);ck(aNull===gNull+1,"Fox and Goeritz nullity");checks++;if(isKnot&&p===2){ck(gNull===0,"knot determinant odd");oddChecks++}}}
 }}
 function pair(){let i=a.indexOf(-1);if(i<0){inspect();return}for(let j=i+1;j<N;j++)if(a[j]<0){a[i]=j;a[j]=i;pair();a[i]=a[j]=-1}}pair()}
 return {maps,choices,knots,checks,oddChecks};
}
console.log('PASS GKT-26-FOX-GOERITZ-01', foxGoeritzControl());
