// GKT-30-PLUMBING-LEAF-01: weighted tree determinants and signed edge switching.
function plumbingCheck(){
 const det=A=>{const n=A.length;if(!n)return 1n;let M=A.map(r=>r.map(BigInt)),s=1n,p=1n;for(let k=0;k<n-1;k++){let j=k;while(j<n&&!M[j][k])j++;if(j===n)return 0n;if(j!==k){[M[k],M[j]]=[M[j],M[k]];s=-s}const q=M[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const z=M[i][j]*q-M[i][k]*M[k][j];if(z%p)throw Error("nonexact");M[i][j]=z/p}M[i][k]=0n}p=q}return s*M[n-1][n-1]};
 const remove=(M,ids)=>M.filter((_,i)=>!ids.includes(i)).map(r=>r.filter((_,j)=>!ids.includes(j)));
 let trees=0,models=0,leaves=0,signs=0,zeros=0;
 for(let n=1;n<=5;n++)for(let code=0;code<(n<3?1:n**(n-2));code++){
 let a=code,seq=[];for(let i=0;i<n-2;i++){seq.push(a%n);a=Math.floor(a/n)}let deg=Array(n).fill(1);for(const v of seq)deg[v]++;const E=[];for(const v of seq){const u=deg.indexOf(1);E.push([u,v]);deg[u]--;deg[v]--}if(n>1)E.push(deg.map((d,i)=>d===1?i:-1).filter(i=>i>=0));trees++;
 const adj=Array.from({length:n},()=>Array(n).fill(0));for(const [u,v] of E)adj[u][v]=adj[v][u]=1;
 for(let k=0;k<3**n;k++){
 let z=k;const M=adj.map((r,i)=>r.map((v,j)=>{if(i!==j)return v;const w=[-2,0,2][z%3];z=Math.floor(z/3);return w}));const D=det(M);models++;if(!D)zeros++;
 for(let v=0;v<n;v++){const ns=adj[v].map((d,i)=>d?i:-1).filter(i=>i>=0);if(ns.length===1){if(D!==BigInt(M[v][v])*det(remove(M,[v]))-det(remove(M,[v,ns[0]])))throw Error("leaf identity");leaves++}}
 // independent signed-edge reorientation for each possible pattern
 const mask=k%(1<<E.length),S=M.map(r=>r.slice()),t=Array(n).fill(0);t[0]=1;for(let pass=0;pass<n;pass++)E.forEach(([u,v],i)=>{const e=(mask>>i&1)?-1:1;S[u][v]=S[v][u]=e;if(t[u])t[v]=t[u]*e;else if(t[v])t[u]=t[v]*e});
 if(!t.every(Boolean)||!S.every((r,i)=>r.every((v,j)=>t[i]*v*t[j]===M[i][j]))||det(S)!==D)throw Error("tree reorientation");signs++;
 }
 }return {trees,models,leaves,signs,zeros}
}
console.log('PASS GKT-30-PLUMBING-LEAF-01',plumbingCheck());
