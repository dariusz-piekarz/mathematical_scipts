// Cross-chapter AA-31 to AA-36 regression: exact BigInt algebra and modular factorization.
// Run: node tools/tests/test_abstract_algebra_cross_aa31_36.js
function runCrossAA31to36(){
  const counts={vieta:0,resultant:0,discriminant:0,resolvent:0,groupAction:0,frobenius:0};
  const assert=(ok,part,detail)=>{counts[part]++;if(!ok)throw new Error(`${part}: ${detail}`)};
  const B=x=>BigInt(x);
  const polyMul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c};
  const polyRoots=r=>r.reduce((a,x)=>polyMul(a,[-B(x),1n]),[1n]);
  const evalPoly=(f,x)=>f.reduceRight((s,c)=>s*B(x)+c,0n);
  const derivative=f=>f.slice(1).map((v,i)=>v*B(i+1));
  const determinant=A=>{
    let a=A.map(r=>r.slice()),n=a.length,prev=1n,sign=1n;
    for(let k=0;k<n-1;k++){
      if(a[k][k]===0n){let i=k+1;while(i<n&&a[i][k]===0n)i++;if(i===n)return 0n;[a[i],a[k]]=[a[k],a[i]];sign=-sign}
      const pivot=a[k][k];
      for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
        const z=a[i][j]*pivot-a[i][k]*a[k][j];if(z%prev!==0n)throw Error("nonintegral Bareiss division");a[i][j]=z/prev;
      }
      for(let i=k+1;i<n;i++)a[i][k]=0n;
      prev=pivot;
    }
    return sign*a[n-1][n-1];
  };
  const resultant=(f,g,n=g.length-1)=>{
    const m=f.length-1,N=m+n,A=Array.from({length:N},()=>Array(N).fill(0n));
    for(let shift=0;shift<n;shift++)for(let j=0;j<f.length;j++)A[shift+j][shift]=f[j];
    for(let shift=0;shift<m;shift++)for(let j=0;j<g.length;j++)A[shift+j][n+shift]=g[j];
    return ((m*n)%2?-1n:1n)*determinant(A);
  };
  const disc=f=>{const n=f.length-1;return ((n*(n-1)/2)%2?-1n:1n)*resultant(f,derivative(f),n-1)};
  const quarticRes=f=>{const [d,c,b,a]=f;return [-(a*a*d+c*c-4n*b*d),a*c-4n*d,-b,1n]};
  const rootDisc=r=>{let v=1n;for(let i=0;i<r.length;i++)for(let j=i+1;j<r.length;j++)v*=B(r[i]-r[j])**2n;return v};
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++){
    let f=polyRoots([a,b,c]);
    assert(f[2]===-B(a+b+c)&&f[1]===B(a*b+a*c+b*c)&&f[0]===-B(a*b*c),"vieta","cubic coefficients");
    assert(disc(f)===rootDisc([a,b,c]),"discriminant","cubic Vandermonde");
  }
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
    let f=polyRoots([a,b,c,d]),r=quarticRes(f);
    let rootsR=[B(a*b+c*d),B(a*c+b*d),B(a*d+b*c)],rExpected=polyRoots(rootsR);
    assert(r.every((v,i)=>v===rExpected[i]),"resolvent","root pairings");
    assert(disc(f)===rootDisc([a,b,c,d]),"discriminant","quartic Vandermonde");
    assert(disc(r)===disc(f),"resolvent","equal discriminants for root specializations");
  }
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
    let f=[B(d),B(c),B(b),B(a),1n],r=quarticRes(f),D=disc(f);
    assert(disc(r)===D,"resolvent","generic quartic coefficient specialization");
    for(let p of [2n,3n,5n,7n])assert((disc(r)-D)%p===0n,"discriminant","quartic modulo "+p);
  }
  for(let a=-5;a<=5;a++)for(let b=-5;b<=5;b++){
    const f=[B(b),B(a),0n,1n];
    assert(disc(f)===-4n*B(a)**3n-27n*B(b)**2n,"discriminant","depressed cubic");
  }
  const sets=[[0],[1],[2],[-1,2],[0,0],[1,1,2]];
  for(let u of sets)for(let v of sets){
    let f=polyRoots(u),g=polyRoots(v),r=resultant(f,g);
    let p=u.reduce((z,x)=>z*evalPoly(g,x),1n);
    assert(r===p,"resultant","product of evaluations");
    assert(resultant(g,f)===((u.length*v.length)%2?-1n:1n)*r,"resultant","exchange sign");
    assert((r===0n)===u.some(x=>v.includes(x)),"resultant","common root criterion");
  }
  const pairings=[[[0,1],[2,3]],[[0,2],[1,3]],[[0,3],[1,2]]];
  const key=P=>P.map(pair=>pair.slice().sort((a,b)=>a-b).join(",")).sort().join(";");
  const label=new Map(pairings.map((x,i)=>[key(x),i]));
  const perms=a=>a.length===0?[[]]:a.flatMap((v,i)=>perms(a.filter((_,j)=>j!==i)).map(t=>[v,...t]));
  const S4=perms([0,1,2,3]);
  const rho=p=>pairings.map(P=>label.get(key(P.map(pair=>pair.map(x=>p[x])))));
  const parity=p=>{let n=0;for(let i=0;i<p.length;i++)for(let j=i+1;j<p.length;j++)if(p[i]>p[j])n++;return n%2};
  const images=S4.map(rho);
  assert(new Set(images.map(p=>p.join(""))).size===6,"groupAction","surjective S4 to S3");
  assert(images.filter(v=>v.join("")==="012").length===4,"groupAction","kernel is V4");
  for(let p of S4){
    assert(parity(p)===parity(rho(p)),"groupAction","parity descends");
    for(let q of S4){
      const comp=p.map((_,i)=>p[q[i]]),R=rho(comp),A=rho(p),B=rho(q);
      assert(R.every((x,j)=>x===A[B[j]]),"groupAction","homomorphism");
    }
  }
  const mod=(x,p)=>(x%p+p)%p;
  const trim=(a,p)=>{let v=a.map(x=>mod(x,p));while(v.length>1&&v.at(-1)===0)v.pop();return v};
  const div=(a,b,p)=>{
    a=trim(a,p);b=trim(b,p);let n=b.length-1,inv=Array.from({length:p},(_,i)=>i).find(x=>mod(x*b[n],p)===1);
    if(inv===undefined)throw Error("invalid leading coefficient");
    while(a.length>=b.length&&a.at(-1)!==0){
      let k=a.length-b.length,t=mod(a.at(-1)*inv,p);
      for(let i=0;i<b.length;i++)a[k+i]=mod(a[k+i]-t*b[i],p);
      a=trim(a,p);
    }
    return a;
  };
  const gcd=(a,b,p)=>{a=trim(a,p);b=trim(b,p);while(!(b.length===1&&b[0]===0)){let r=div(a,b,p);a=b;b=r}return a.length-1};
  const factor=(f,p)=>{
    f=trim(f,p);const n=f.length-1;if(!n)return [];
    for(let k=1;k<=Math.floor(n/2);k++)for(let x=0;x<p**k;x++){
      let y=x,coef=[];for(let i=0;i<k;i++){coef.push(y%p);y=Math.floor(y/p)}coef.push(1);
      if(div(f,coef,p).every(a=>a===0)){
        let q=f.slice(),quo=Array(n-k+1).fill(0);
        for(let s=n-k;s>=0;s--){let t=q[k+s];quo[s]=t;for(let j=0;j<=k;j++)q[j+s]=mod(q[j+s]-t*coef[j],p)}
        return [...factor(coef,p),...factor(quo,p)];
      }
    }
    return [n];
  };
  const examples=[
    {name:"cubic X^3-X-1",f:[-1,-1,0,1],known:{2:[3],5:[1,2],59:[1,1,1]}},
    {name:"S4 quartic",f:[-1,-1,0,0,1],known:{}},
    {name:"C4 quartic",f:[1,1,1,1,1],known:{}},
    {name:"D4 quartic",f:[-2,0,0,0,1],known:{}},
    {name:"V4 quartic",f:[1,0,-10,0,1],known:{}}
  ];
  for(let e of examples){
    let D=disc(e.f.map(B)),n=e.f.length-1;
    for(let p of [2,3,5,7,11,13,23,59]){
      const g=trim(e.f,p),df=g.slice(1).map((c,i)=>mod(c*(i+1),p));
      let degrees=factor(g,p).sort((a,b)=>a-b);
      let good=D%B(p)!==0n;
      assert((gcd(g,df,p)===0)===good,"frobenius","good reduction and separability "+e.name+" p="+p);
      assert(degrees.reduce((a,b)=>a+b,0)===n,"frobenius","factor degrees "+e.name+" p="+p);
      if(good&&e.known[p])assert(degrees.join(",")===e.known[p].join(","),"frobenius","explicit factorization "+e.name+" p="+p);
      if(good&&p!==2){
        let d=Number((D%B(p)+B(p))%B(p)),sq=Array.from({length:p},(_,i)=>i*i%p).includes(d);
        assert(((n-degrees.length)%2===0)===sq,"frobenius","quadratic character parity "+e.name+" p="+p);
      }
    }
  }
  for(let [f,D,name] of [
    [[1n,1n,1n,1n,1n],125n,"C4"],
    [[-1n,-1n,0n,0n,1n],-283n,"S4"],
    [[-2n,0n,0n,0n,1n],-2048n,"D4"],
    [[1n,0n,-10n,0n,1n],147456n,"V4"]
  ])assert(disc(f)===D&&disc(quarticRes(f))===D,"examples" in counts?"frobenius":"resolvent","quartic example "+name);
  return {counts,total:Object.values(counts).reduce((x,y)=>x+y,0)};
}
const output=runCrossAA31to36();
console.log(JSON.stringify(output,null,2));
