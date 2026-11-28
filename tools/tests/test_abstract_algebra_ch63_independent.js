// AA-63: finite-type diagrams, root counts and equivalence by permutation.
function classification63(){
 const assert=(p,m)=>{if(!p)throw Error(m)};
 function chain(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?2:Math.abs(i-j)===1?-1:0));}
 function edge(A,i,j,a=-1,b=-1){A[i][j]=a;A[j][i]=b;return A;}
 const models=[];
 for(let n=1;n<=8;n++)models.push(["A"+n,chain(n),n*(n+1)]);
 for(let n=2;n<=8;n++){models.push(["B"+n,edge(chain(n),n-2,n-1,-1,-2),2*n*n],["C"+n,edge(chain(n),n-2,n-1,-2,-1),2*n*n]);}
 for(let n=4;n<=8;n++){let A=chain(n);edge(A,n-2,n-1,0,0);edge(A,n-3,n-1);models.push(["D"+n,A,2*n*(n-1)]);}
 for(const [n,c] of [[6,72],[7,126],[8,240]]){let A=chain(n);edge(A,n-2,n-1,0,0);edge(A,2,n-1);models.push(["E"+n,A,c]);}
 models.push(["F4",edge(chain(4),1,2,-1,-2),48],["G2",edge(chain(2),0,1,-3,-1),12]);
 const orbits=(A,count)=>{const n=A.length,roots=[],seen=new Set();function insert(v){const k=v.join(",");if(!seen.has(k)){seen.add(k);roots.push(v);assert(roots.length<=count,"root overflow");}}for(let i=0;i<n;i++)insert(Array.from({length:n},(_,j)=>Number(i===j)));for(let k=0;k<roots.length;k++){let v=roots[k];for(let i=0;i<n;i++){let u=v.slice();u[i]-=A[i].reduce((s,a,j)=>s+a*v[j],0);insert(u);}}assert(roots.length===count,"root count");return roots;};
 function equivalent(A,B){if(A.length!==B.length)return false;let n=A.length,p=[],used=new Set();function go(){let i=p.length;if(i===n)return true;for(let j=0;j<n;j++){if(used.has(j))continue;if(p.some((k,l)=>A[i][l]!==B[j][k]||A[l][i]!==B[k][j]))continue;p.push(j);used.add(j);if(go())return true;used.delete(j);p.pop();}return false;}return go();}
 let roots=0,pairs=0,collision=0,permutations=0;
 for(const [name,A,c] of models){roots+=orbits(A,c).length;const n=A.length,p=Array.from({length:n},(_,i)=>n-i-1);assert(equivalent(A,p.map(i=>p.map(j=>A[i][j]))),"relabeling");permutations++;}
 for(let i=0;i<models.length;i++)for(let j=0;j<i;j++){const [name,A]=models[i],[other,B]=models[j];if(A.length!==B.length)continue;pairs++;const same=(name==="C2"&&other==="B2");assert(equivalent(A,B)===same,`${name} vs ${other}`);if(same)collision++;}
 const sum=(A,B)=>[...A.map(r=>[...r,...B.map(()=>0)]),...B.map(r=>[...A.map(()=>0),...r])];
 const A=chain(2),B=edge(chain(3),1,2,-1,-2),C=edge(chain(3),1,2,-2,-1);
 assert(equivalent(sum(A,B),sum(B,A)),"direct sum reorder");assert(!equivalent(sum(A,B),sum(A,C)),"distinct components");
 return {models:models.length,roots,pairs,collision,permutations,directSums:2};
}
console.log('AA-63 classification: PASS',classification63());
