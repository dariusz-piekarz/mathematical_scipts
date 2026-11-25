// GKT-30-E8-BLOWDOWN-01: exact principal minors, explicit A5 and signed leaf blow-down.
function e8Check(){
const det=A=>{const n=A.length;if(!n)return 1n;let M=A.map(r=>r.map(BigInt)),s=1n,p=1n;for(let k=0;k<n-1;k++){let j=k;while(j<n&&!M[j][k])j++;if(j===n)return 0n;if(j!==k){[M[k],M[j]]=[M[j],M[k]];s=-s}let q=M[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){let z=M[i][j]*q-M[i][k]*M[k][j];if(z%p)throw Error("nonexact");M[i][j]=z/p}M[i][k]=0n}p=q}return s*M[n-1][n-1]};
const Q=Array.from({length:8},(_,i)=>Array.from({length:8},(_,j)=>i===j?-2:((i<7&&j<7&&Math.abs(i-j)===1)||(i===2&&j===7)||(i===7&&j===2))?1:0));let principal=0;
for(let mask=1;mask<256;mask++){const ids=Array.from({length:8},(_,i)=>i).filter(i=>mask>>i&1),d=det(ids.map(i=>ids.map(j=>Q[i][j])));if(d*(-1n)**BigInt(ids.length)<=0n)throw Error("principal sign");principal++}
if(det(Q)!==1n)throw Error("E8 det");
const mul=(a,b)=>b.map(i=>a[i]),id=[0,1,2,3,4],s=[1,0,3,2,4],t=[0,2,4,3,1],key=a=>a.join(""),order=a=>{let b=id,k=0;do{b=mul(a,b);k++;if(k>60)throw Error("order")}while(key(b)!==key(id));return k};
if(order(s)!==2||order(t)!==3||order(mul(s,t))!==5)throw Error("triangle rel");
const G=[id],seen=new Set([key(id)]);for(let i=0;i<G.length;i++)for(const a of [s,t]){const b=mul(a,G[i]);if(!seen.has(key(b))){seen.add(key(b));G.push(b)}}
if(G.length!==60)throw Error("A5");
let even=0;for(const g of G){let inv=0;for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)if(g[i]>g[j])inv++;if(inv%2)throw Error("odd");even++}
let blow=0,singular=0;for(let a=-5;a<=5;a++)for(let b=-5;b<=5;b++)for(let c=-5;c<=5;c++)for(let eps of [-1,1]){
const M=[[-1,eps,0],[eps,a,b],[0,b,c]],N=[[a+1,b],[b,c]];
const P=[[1,eps,0],[0,1,0],[0,0,1]],R=P.map((_,i)=>P.map((_,j)=>M.reduce((sum,r,k)=>sum+r.reduce((sum2,v,l)=>sum2+P[k][i]*v*P[l][j],0),0)));
const T=[[-1,0,0],[0,a+1,b],[0,b,c]];
if(JSON.stringify(R)!==JSON.stringify(T)||det(M)!==-det(N))throw Error("blowdown");if(det(M)===0n)singular++;blow++}
return {principal,groupOrder:G.length,even,blow,singular}
}
console.log('PASS GKT-30-E8-BLOWDOWN-01',e8Check());
