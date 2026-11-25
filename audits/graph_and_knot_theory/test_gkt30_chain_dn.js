// GKT-30-CHAIN-DN-01: exact continuants, cyclic cokernels and Dn discriminant forms.
function chainDnCheck(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const det=A=>{let n=A.length;if(!n)return 1n;let M=A.map(r=>r.map(BigInt)),s=1n,p=1n;for(let k=0;k<n-1;k++){let j=k;while(j<n&&!M[j][k])j++;if(j===n)return 0n;if(j!==k){[M[k],M[j]]=[M[j],M[k]];s=-s}const q=M[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const z=M[i][j]*q-M[i][k]*M[k][j];if(z%p)throw Error("nonexact");M[i][j]=z/p}M[i][k]=0n}p=q}return s*M[n-1][n-1]};
 const minor=(M,i,j)=>M.filter((_,k)=>k!==i).map(r=>r.filter((_,k)=>k!==j));
 let chains=0,zero=0,cfUndefined=0,modular=0,cofactor=0,dn=0,dnPair=0,dnMod=0;
 for(let n=1;n<=6;n++)for(let code=0;code<5**n;code++){
  let k=code;const a=Array.from({length:n},()=>{const w=k%5-2;k=Math.floor(k/5);return w}),M=a.map((w,i)=>a.map((_,j)=>i===j?w:Math.abs(i-j)===1?1:0));
  const D=Array(n+2).fill(0n);D[n]=1n;for(let i=n-1;i>=0;i--)D[i]=BigInt(a[i])*D[i+1]-D[i+2];const d=det(M);
  if(d!==D[0]||gcd(D[0],D[1])!==1n)throw Error("continuant");chains++;if(!d)zero++;if(D.slice(1,n).some(x=>!x))cfUndefined++;
  if(d){if(det(minor(M,0,0))!==D[1])throw Error("cofactor");cofactor++}
  for(const p of [2,3,5,7]){let count=0;for(let x=0;x<p;x++){let prev=0,cur=x;for(const w of a)[prev,cur]=[cur,((-prev-w*cur)%p+p)%p];if(!cur)count++}if(BigInt(count)!==gcd(d,BigInt(p)))throw Error("cyclic kernel");modular++}
 }
 for(let n=4;n<=36;n++){const m=n-3,M=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?2:0));const E=[];for(let i=0;i<m;i++)E.push([i,i+1]);E.push([m,m+1],[m,m+2]);for(const [i,j] of E)M[i][j]=M[j][i]=-1;const d=det(M);if(d!==4n)throw Error("Dn det");dn++;
 for(const [i,j,v] of [[0,0,4n],[0,m+1,2n],[m+1,m+1,BigInt(n)]]){const c=det(minor(M,j,i))*((-1n)**BigInt(i+j));if(c!==v)throw Error("Dn pairing");dnPair++}
 for(let p of [2,4,8]){let cnt=0;for(let x=0;x<p;x++)for(let u=0;u<p;u++){const v=((n-1)*x-u+p*p)%p;if((2*u-(n-2)*x)%p===0&&(2*v-(n-2)*x)%p===0)cnt++}if(BigInt(cnt)!==(n%2?gcd(4n,BigInt(p)):gcd(2n,BigInt(p))**2n))throw Error("Dn group");dnMod++}
 }return {chains,zero,cfUndefined,modular,cofactor,dn,dnPair,dnMod}
}
console.log('PASS GKT-30-CHAIN-DN-01',chainDnCheck());
