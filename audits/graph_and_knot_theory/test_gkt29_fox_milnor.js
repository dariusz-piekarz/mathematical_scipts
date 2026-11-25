// GKT-29-FOX-MILNOR-01: exact determinant identities on metabolic Seifert matrices.
function foxControl(){
function det(A){const n=A.length;if(!n)return 1n;const M=A.map(r=>r.map(BigInt));let sign=1n,prev=1n;for(let k=0;k<n-1;k++){let i=k;while(i<n&&!M[i][k])i++;if(i===n)return 0n;if(i!==k){[M[k],M[i]]=[M[i],M[k]];sign=-sign}const p=M[k][k];for(let a=k+1;a<n;a++){for(let b=k+1;b<n;b++){const v=M[a][b]*p-M[a][k]*M[k][b];if(v%prev)throw Error("nonexact");M[a][b]=v/prev}M[a][k]=0n}prev=p}return sign*M[n-1][n-1]}
let seed=29279;function rand(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>16)%9-4}
let models=0,evals=0,squares=0,unit=0;
for(let g=0;g<=4;g++)for(let trial=0;trial<(g?120:1);trial++){
const A=Array.from({length:g},()=>Array.from({length:g},rand)),C=Array.from({length:g},()=>Array.from({length:g},rand)),B=A.map((r,i)=>r.map((_,j)=>A[j][i]-(i===j?1:0)));
const V=Array.from({length:2*g},(_,i)=>Array.from({length:2*g},(_,j)=>i<g?(j<g?0:A[i][j-g]):j<g?B[i-g][j]:C[i-g][j-g]));
const F=t=>det(A.map((r,i)=>r.map((v,j)=>t*v-B[j][i])));const P=t=>det(V.map((r,i)=>r.map((v,j)=>t*v-V[j][i])));
if(P(1)!==1n||F(1)**2n!==1n)throw Error("unit");unit++;
if((P(-1)<0n?-P(-1):P(-1))!==F(-1)**2n||F(-1)%2n===0n)throw Error("square");squares++;
for(let t=-4;t<=4;t++){const scaled=det(A.map((r,i)=>r.map((v,j)=>v-t*B[j][i])));if(P(t)!==F(t)*scaled)throw Error("factorization");evals++}models++
}return {models,evals,squares,unit}}
console.log('PASS GKT-29-FOX-MILNOR-01',foxControl());
