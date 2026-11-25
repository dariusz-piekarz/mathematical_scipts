// GKT-27-CYCLIC-COVER-01: exact block determinants and independent Sylvester resultants.
function cyclicCoverControl(){
 const ck=(b,m)=>{if(!b)throw Error(m)};
 function det(A){A=A.map(r=>r.map(BigInt));const n=A.length;if(!n)return 1n;let sign=1n,last=1n;for(let i=0;i<n-1;i++){let k=i;while(k<n&&!A[k][i])k++;if(k===n)return 0n;if(k!==i){[A[k],A[i]]=[A[i],A[k]];sign=-sign}const p=A[i][i];for(let j=i+1;j<n;j++){for(let l=i+1;l<n;l++){const v=p*A[j][l]-A[j][i]*A[i][l];ck(v%last===0n,"Bareiss exact");A[j][l]=v/last}A[j][i]=0n}last=p}return sign*A[n-1][n-1]}
 function rank(A,p){let M=A.map(r=>r.map(x=>(x%p+p)%p)),r=0;for(let j=0;j<(M[0]?.length||0)&&r<M.length;j++){let i=r;while(i<M.length&&!M[i][j])i++;if(i===M.length)continue;[M[i],M[r]]=[M[r],M[i]];let inv=1;while(inv*M[r][j]%p!==1)inv++;M[r]=M[r].map(x=>x*inv%p);for(let k=r+1;k<M.length;k++){let c=M[k][j];if(c)M[k]=M[k].map((x,l)=>(x-c*M[r][l]%p+p)%p)}r++}return r}
 function polynomial(V){let n=V.length,coeff=Array(n+1).fill(0);function perm(p,seen,sign){if(p.length===n){let c=[sign];for(let i=0;i<n;i++){let j=p[i],q=Array(c.length+1).fill(0);for(let k=0;k<c.length;k++){q[k]-=c[k]*V[j][i];q[k+1]+=c[k]*V[i][j]}c=q}c.forEach((x,k)=>coeff[k]+=x);return}for(let j=0;j<n;j++)if(!seen.has(j)){seen.add(j);perm([...p,j],seen,sign*(-1)**p.filter(x=>x>j).length);seen.delete(j)}}perm([],new Set,1);while(coeff.length>1&&coeff.at(-1)===0)coeff.pop();return coeff}
 function resultant(P,d){let n=P.length-1,N=d+n;let A=Array.from({length:N},()=>Array(N).fill(0));for(let i=0;i<d;i++)for(let j=0;j<=n;j++)A[i][i+j]=P[n-j];for(let i=0;i<n;i++){A[d+i][i]=1;A[d+i][i+d]=-1}return det(A)}
 const abs=x=>x<0n?-x:x;
 function block(V,d){let n=V.length,A=Array.from({length:n*d},()=>Array(n*d).fill(0));for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<d;k++){A[i*d+(k+1)%d][j*d+k]+=V[i][j];A[i*d+k][j*d+k]-=V[j][i]}return A}
 let matrices=0,covers=0,zero=0,modChecks=0;
 function inspect(V){matrices++;const P=polynomial(V);ck(P.reduce((a,b)=>a+b,0)===1,"Alexander at 1");for(let d=2;d<=8;d++){const B=block(V,d),D=det(B);ck(abs(D)===abs(resultant(P,d)),"cyclic resultant");covers++;if(D===0n)zero++;if(d===2){const S=V.map((r,i)=>r.map((x,j)=>x+V[j][i]));ck(abs(D)===abs(det(S)),"double cover determinant");for(let p of [2,3,5,7,11]){ck(B.length-rank(B,p)===S.length-rank(S,p),"double cover nullity");modChecks++}}}}
 for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)inspect([[a,b],[b-1,c]]);
 for(let i=0;i<12;i++){let V=Array.from({length:4},(_,r)=>Array.from({length:4},(_,s)=>((i+3*Math.min(r,s)+5*Math.max(r,s))%5)-2));V[1][0]--;V[3][2]--;inspect(V)}
 const T=[[1,0],[-1,1]];ck(abs(det(block(T,2)))===3n,"trefoil d2");ck(abs(det(block(T,3)))===4n,"trefoil d3");ck(det(block(T,6))===0n,"trefoil d6");ck(abs(det(block([[1,0],[-1,-1]],2)))===5n,"figure eight");
 return {matrices,covers,zero,modChecks,examples:4};
}
console.log('PASS GKT-27-CYCLIC-COVER-01', cyclicCoverControl());
