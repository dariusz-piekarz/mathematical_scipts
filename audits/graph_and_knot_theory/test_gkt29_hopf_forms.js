// GKT-29-HOPF-FORMS-01: framed Hopf matrices, cyclic cokernels, inertia, and unit stabilization.
function hopfCheck(){
 const ck=(b,m)=>{if(!b)throw Error(m)};
 const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a};
 let models=0,modular=0,singular=0,sigChecks=0,stabilizations=0;
 for(let a=-20;a<=20;a++)for(let b=-20;b<=20;b++){
  const d=a*b-1,t=a+b,s=d<0?0:d>0?2*Math.sign(t):Math.sign(t);
  // independent rational congruence diagonalization via nonzero pivot
  let s2=a!==0?Math.sign(a)+Math.sign(a*d):b!==0?Math.sign(b)+Math.sign(b*d):0;
  ck(s===s2,"signature");sigChecks++;models++;if(!d)singular++;
  for(let n=2;n<=16;n++){let k=0;for(let x=0;x<n;x++)for(let y=0;y<n;y++)if((a*x+y)%n===0&&(x+b*y)%n===0)k++;ck(k===gcd(d,n),"cyclic cokernel");modular++;
   for(const eps of [-1,1]){let e=0;for(let z=0;z<n;z++)if(eps*z%n===0)e++;ck(k*e===k,"unit stabilization");stabilizations++}
  }
 }
 return {models,singular,sigChecks,modular,stabilizations}
}
console.log('PASS GKT-29-HOPF-FORMS-01',hopfCheck());
