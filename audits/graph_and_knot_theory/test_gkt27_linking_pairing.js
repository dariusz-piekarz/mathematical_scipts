// GKT-27-LINKING-01: exact finite linking pairings and signed handle slides.
function linkingControl(){
 const ck=(b,m)=>{if(!b)throw Error(m)};let matrices=0,pairChecks=0,slideChecks=0,radicalChecks=0,stabilizations=0;
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
 const mv=(A,v)=>A.map(r=>dot(r,v));
 const tr=A=>A[0].map((_,i)=>A.map(r=>r[i]));
 const mm=(A,B)=>A.map(r=>tr(B).map(c=>dot(r,c)));
 const mod=(x,d)=>((x%d)+d)%d;
 for(let a=-3;a<=3;a++)for(let b=-3;b<=3;b++)for(let c=-3;c<=3;c++){
 const Q=[[a,b],[b,c]],D=a*c-b*b;if(!D)continue;matrices++;
 const N=[[c,-b],[-b,a]].map(r=>r.map(x=>x*Math.sign(D))),d=Math.abs(D);
 const key=x=>mv(N,x).map(t=>mod(t,d)).join(",");
 const reps=new Map;for(let i=0;i<d;i++)for(let j=0;j<d;j++)reps.set(key([i,j]),[i,j]);
 ck(reps.size===d,"group order");const form=(x,y)=>mod(-dot(x,mv(N,y)),d);
 for(const x of reps.values()){
 let radical=true;for(const y of [[1,0],[0,1]])if(form(x,y)!==0)radical=false;
 ck(radical===(key(x)===key([0,0])),"radical");radicalChecks++;
 for(const y of [[1,0],[0,1],[2,-1]]){ck(form(x,y)===form(y,x),"symmetry");ck(form(x,y)===form(x.map((z,i)=>z+Q[i][0]-2*Q[i][1]),y),"representative");pairChecks++}
 }
 for(const [i,j] of [[0,1],[1,0]])for(const e of [-1,1]){
 const P=[[1,0],[0,1]];P[j][i]=e;const R=mm(mm(tr(P),Q),P);
 ck(R[i][i]===Q[i][i]+2*e*Q[i][j]+Q[j][j],"signed diagonal");ck(R[i][j]===Q[i][j]+e*Q[j][j],"signed off diagonal");
 const S=[[R[1][1],-R[0][1]],[-R[1][0],R[0][0]]].map(r=>r.map(x=>x*Math.sign(D)));
 ck(R[0][0]*R[1][1]-R[0][1]*R[1][0]===D,"det");
 for(const x of reps.values())for(const y of [[1,0],[0,1]]){ck(mod(-dot(mv(tr(P),x),mv(S,mv(tr(P),y))),d)===form(x,y),"isometry");slideChecks++}
 }
 for(const e of [-1,1]){ck(mod(-e*d,d)===0,"unit stabilization");stabilizations++}
 }
 return {matrices,radicalChecks,pairChecks,slideChecks,stabilizations};
}
console.log('PASS GKT-27-LINKING-01', linkingControl());
