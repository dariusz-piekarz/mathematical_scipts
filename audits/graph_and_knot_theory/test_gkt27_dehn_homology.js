// GKT-27-DEHN-H1-01: exact determinantal divisors of filling presentations.
function controlDehn(){
 const ck=(b,m)=>{if(!b)throw Error(m)};
 const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a};
 function det(A){if(!A.length)return 1;return A[0].reduce((s,x,j)=>s+(j%2?-1:1)*x*det(A.slice(1).map(r=>r.filter((_,i)=>i!==j))),0)}
 function subsets(n,k){let out=[];function visit(a,i){if(a.length===k){out.push(a);return}for(let j=i;j<=n-(k-a.length);j++)visit([...a,j],j+1)}visit([],0);return out}
 function smith(A){let last=1,diags=[],rank=0;for(let k=1;k<=A.length;k++){let g=0;const idx=subsets(A.length,k);for(const I of idx)for(const J of idx)g=gcd(g,det(I.map(i=>J.map(j=>A[i][j]))));if(!g)break;ck(g%last===0,"determinantal divisor");diags.push(g/last);last=g;rank=k}return {free:A.length-rank,torsion:diags.filter(x=>x!==1)}}
 const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 let slopes=0,completions=0,gluing=0,links=0;
 for(let p=-12;p<=12;p++)for(let q=-12;q<=12;q++){if(gcd(p,q)!==1)continue;slopes++;for(let r=-16;r<=16;r++)for(let s=-16;s<=16;s++){if(Math.abs(p*s-q*r)!==1)continue;completions++;let S=smith([[p,r],[0,-1]]);ck(same(S,{free:Number(p===0),torsion:Math.abs(p)>1?[Math.abs(p)]:[]}),"single filling");for(let e of [-1,1])for(let k of [-2,0,2]){const rr=p*k+r*e,ss=q*k+s*e;ck(p*e*ss-q*e*rr===p*s-q*r,"orientation preserving change");ck(same(smith([[p*e,rr],[0,-1]]),S),"slope independence");gluing++}}}
 function link(Q){let n=Q.length;const P=Array.from({length:2*n},(_,i)=>Array.from({length:2*n},(_,j)=>i<n&&j<n?Q[i][j]:i<n&&j>=n?Number(i===j-n):i>=n&&j>=n?-Number(i===j):0));ck(same(smith(P),smith(Q)),"link presentation");links++}
 for(let a=-3;a<=3;a++)for(let b=-3;b<=3;b++)for(let c=-3;c<=3;c++)link([[a,b],[b,c]]);
 for(let i=0;i<16;i++){const a=i%3-1,b=Math.floor(i/3)%3-1,c=Math.floor(i/9)-1;link([[a,b,c],[b,c,1],[c,1,b]])}
 return {slopes,completions,gluing,links};
}
console.log('PASS GKT-27-DEHN-H1-01', controlDehn());
