// AA-66: exact ranks of cocycles and coboundaries; trace-normalized Casimir.
function whitehead66(){
 const A=(b,m)=>{if(!b)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 function rank(cols){let rows=[];for(let v of cols){v=v.slice();for(const [p,w] of rows){if(!v[p])continue;let a=w[p],b=v[p];v=v.map((x,j)=>a*x-b*w[j]);const g=v.reduce(gcd,0n);if(g)v=v.map(x=>x/g)}let p=v.findIndex(x=>x!==0n);if(p>=0)rows.push([p,v]);}return rows.length;}
 const zero=n=>Array(n).fill(0n);
 function ops(m){let n=m+1;return [Array.from({length:n},(_,j)=>{let a=zero(n);a[j]=BigInt(m-2*j);return a}),Array.from({length:n},(_,j)=>{let a=zero(n);if(j)a[j-1]=BigInt(j*(m-j+1));return a}),Array.from({length:n},(_,j)=>{let a=zero(n);if(j<m)a[j+1]=1n;return a})];}
 function check(mats,br,n){const r=mats.length,pairs=[];for(let i=0;i<r;i++)for(let j=i+1;j<r;j++)pairs.push([i,j]);
  const cols=[];for(let k=0;k<r;k++)for(let l=0;l<n;l++){let col=[];for(const [i,j] of pairs){let v=zero(n);if(k===j)v=v.map((x,t)=>x+mats[i][l][t]);if(k===i)v=v.map((x,t)=>x-mats[j][l][t]);v[l]-=br(i,j,k);col.push(...v);}cols.push(col);}
  const cob=Array.from({length:n},(_,j)=>mats.flatMap(M=>M[j]));
  const z=r*n-rank(cols),b=rank(cob);A(z===b,"H1 dimension");return {z,b};
 }
 const b=(i,j,k)=>i===0&&j===1&&k===1?2n:i===0&&j===2&&k===2?-2n:i===1&&j===2&&k===0?1n:0n;
 let models=0,cocycles=0,casimir=0,productModels=0,nonfaithful=0;
 for(let m=0;m<=12;m++){let n=m+1,M=ops(m);const q=check(M,b,n);A(q.z===(m?n:0),"rank sl2");cocycles+=q.z;models++;
  if(m){ // trace form: B(H,H)=2 B(E,F); normalized Casimir numerator H²+2EF+2FE.
   let t=M[0].reduce((s,col,j)=>s+col[j]*col[j],0n);
   A(t!==0n,"trace nonzero");
   for(let j=0;j<n;j++){const h=BigInt(m-2*j),ef=BigInt((j+1)*(m-j)),fe=BigInt(j*(m-j+1));A(BigInt(n)*(h*h+2n*(ef+fe))===3n*t,"Casimir trace scalar");casimir++;}
  }
 }
 // Direct products sl2+sl2 acting on L(a) tensor L(b), including inactive ideals.
 for(let a=0;a<=3;a++)for(let c=0;c<=3;c++){let p=a+1,q=c+1,n=p*q,L=ops(a),R=ops(c);
  let M=[...L.map(X=>Array.from({length:n},(_,j)=>{let v=zero(n);for(let i=0;i<p;i++)v[i+p*Math.floor(j/p)]=X[j%p][i];return v;})),...R.map(X=>Array.from({length:n},(_,j)=>{let v=zero(n);for(let i=0;i<q;i++)v[j%p+p*i]=X[Math.floor(j/p)][i];return v;}))];
  let z=check(M,(i,j,k)=>i<3&&j<3&&k<3?b(i,j,k):i>=3&&j>=3&&k>=3?b(i-3,j-3,k-3):0n,n);
  A(z.z===(a||c?n:0),"product H1");productModels++;if(!a||!c)nonfaithful++;cocycles+=z.z;
 }
 return {models,productModels,nonfaithful,cocycles,casimir};
}
console.log('AA-66 Whitehead and Casimir: PASS',whitehead66());
