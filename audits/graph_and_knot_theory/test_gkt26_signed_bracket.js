// GKT-26-SIGNED-BRACKET-01: exact root-of-unity phases and two-strand examples.
function signedBracketControl(){
 const ck=(v,m)=>{if(!v)throw Error(m)};
 const cycles=p=>{let id=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(id[i]<0){let j=i;do{id[j]=n;j=p[j]}while(j!==i);n++}return[n,id]};
 function dsu(n){const p=Array.from({length:n},(_,i)=>i);const root=i=>{while(p[i]!==i)i=p[i];return i};return {join:(a,b)=>{p[root(a)]=root(b)},count:()=>new Set(p.map((_,i)=>root(i))).size}}
 function det(M){if(!M.length)return 1;return M[0].reduce((a,x,j)=>a+(j%2?-1:1)*x*det(M.slice(1).map(r=>r.filter((_,k)=>j!==k))),0)}
 function addPhase(vec,e,c){e=((e%8)+8)%8;vec[e%4]+=(e>=4?-c:c)}
 let maps=0,signs=0,states=0,minors=0,dualChecks=0,oneCircle=0;
 function inspect(p,m){const [v,V]=cycles(p),[f,F]=cycles(p.map((_,i)=>p[i^1]));const conn=dsu(v),E=[],D=[];for(let i=0;i<m;i++){E.push([V[2*i],V[2*i+1]]);D.push([F[2*i],F[2*i+1]]);conn.join(...E[i])}if(conn.count()!==1||v-m+f!==2)return;maps++;
 const circles=[];for(let mask=0;mask<(1<<m);mask++){let S=dsu(4*m);for(let d=0;d<2*m;d++)S.join(2*d+1,2*p[d]);for(let i=0;i<m;i++){let d=2*i,e=d+1;if(mask&(1<<i)){S.join(2*d,2*e+1);S.join(2*d+1,2*e)}else{S.join(2*d,2*d+1);S.join(2*e,2*e+1)}}circles.push(S.count())}
 function matrix(n,edges,w){let L=Array.from({length:n},()=>Array(n).fill(0));edges.forEach(([a,b],i)=>{if(a!==b){L[a][a]+=w[i];L[b][b]+=w[i];L[a][b]-=w[i];L[b][a]-=w[i]}});return L}
 for(let code=0;code<(1<<m);code++){signs++;const w=E.map((_,i)=>code&(1<<i)?-1:1),sum=w.reduce((a,b)=>a+b,0),B=[0,0,0,0];for(let mask=0;mask<(1<<m);mask++){states++;if(circles[mask]!==1)continue;oneCircle++;let e=0;for(let i=0;i<m;i++)e+=(mask&(1<<i)?1:-1)*w[i];addPhase(B,e,1)}
 const L=matrix(v,E,w),LD=matrix(f,D,w.map(x=>-x));
 for(let r=0;r<v;r++){const d=det(L.filter((_,i)=>i!==r).map(row=>row.filter((_,j)=>j!==r))),C=[0,0,0,0];addPhase(C,-sum+2*(v-1),d);ck(C.every((x,i)=>x===B[i]),"signed bracket phase");minors++}
 for(let r=0;r<f;r++){const d=det(LD.filter((_,i)=>i!==r).map(row=>row.filter((_,j)=>j!==r))),C=[0,0,0,0];addPhase(C,sum+2*(f-1),d);ck(C.every((x,i)=>x===B[i]),"color swap phase");dualChecks++}
 }}
 for(let m=1;m<=3;m++){let p=Array.from({length:2*m},(_,i)=>i);function perm(k){if(k===p.length){inspect(p,m);return}for(let j=k;j<p.length;j++){[p[k],p[j]]=[p[j],p[k]];perm(k+1);[p[k],p[j]]=[p[j],p[k]]}}perm(0)}
 // Independent Laurent calculation in the 2-strand Temperley-Lieb algebra.
 const mono=(e,c=1)=>new Map([[e,c]]),delta=new Map([[2,-1],[-2,-1]]);
 function plus(P,Q){let R=new Map(P);for(const [e,c] of Q)R.set(e,(R.get(e)||0)+c);return R}
 function mul(P,Q){let R=new Map;for(const [a,x] of P)for(const [b,y] of Q)R.set(a+b,(R.get(a+b)||0)+x*y);return R}
 function braid(word){let P=mono(0),Q=new Map;for(const s of word){const X=mono(s),Y=mono(-s),oldP=P,oldQ=Q;P=mul(oldP,X);Q=plus(plus(mul(oldP,Y),mul(oldQ,X)),mul(mul(oldQ,Y),delta))}return plus(mul(P,delta),Q)}
 function equal(P,Q){return [...new Set([...P.keys(),...Q.keys()])].every(e=>(P.get(e)||0)===(Q.get(e)||0))}
 ck(equal(braid([1,1,1]),new Map([[-7,1],[-3,-1],[5,0],[5,-1]])),"trefoil bracket");
 for(const word of [[-1,1,1],[1,-1,1],[1,1,-1]])ck(equal(braid(word),mono(3,-1)),"crossing change bracket");
 return {maps,signs,states,oneCircle,minors,dualChecks,braidExamples:4};
}
console.log('PASS GKT-26-SIGNED-BRACKET-01', signedBracketControl());
