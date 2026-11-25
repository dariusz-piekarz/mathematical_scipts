// GKT-28-TORUS-H1-01: Smith invariants checked by modular kernel enumeration.
function torusControl(){
const ck=(b,m)=>{if(!b)throw Error(m)};
const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a};
const mul=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0)));
const inv=A=>[[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]];
function invariants(A){const M=[[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]],g=M.flat().reduce(gcd,0),det=M[0][0]*M[1][1]-M[0][1]*M[1][0];ck(det===2-A[0][0]-A[1][1],"det trace");if(!g)return [3,[]];if(!det)return [2,[g]];ck(Math.abs(det)%(g*g)===0,"divisibility");return [1,[g,Math.abs(det)/g]]}
let matrices=0,hyperbolic=0,rank2=0,rank3=0,modChecks=0,changes=0;
for(let a=-6;a<=6;a++)for(let b=-6;b<=6;b++)for(let c=-6;c<=6;c++)for(let d=-6;d<=6;d++){if(a*d-b*c!==1)continue;const A=[[a,b],[c,d]],S=invariants(A);matrices++;if(Math.abs(a+d)>2)hyperbolic++;if(S[0]===2)rank2++;if(S[0]===3)rank3++;
for(let n=2;n<=12;n++){let count=0;for(let x=0;x<n;x++)for(let y=0;y<n;y++)if(((a-1)*x+b*y)%n===0&&(c*x+(d-1)*y)%n===0)count++;const predicted=n**(S[0]-1)*S[1].reduce((p,k)=>p*gcd(k,n),1);ck(count===predicted,"modular kernel");modChecks++}
for(const P of [[[1,1],[0,1]],[[0,-1],[1,0]],[[1,0],[2,1]]]){ck(JSON.stringify(invariants(mul(mul(P,A),inv(P))))===JSON.stringify(S),"basis");changes++}
ck(JSON.stringify(invariants(inv(A)))===JSON.stringify(S),"inverse");changes++;
}
return {matrices,hyperbolic,rank2,rank3,modChecks,changes}}
console.log('PASS GKT-28-TORUS-H1-01',torusControl());
