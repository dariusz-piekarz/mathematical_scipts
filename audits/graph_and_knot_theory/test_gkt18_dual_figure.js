// GKT-18-FIG-01: source-level angular separation guard for the planar dual drawing.
// Run from repository root: node audits/graph_and_knot_theory/test_gkt18_dual_figure.js
// Does not replace inspecting the compiled figure.
function check(s){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const pic=s.match(/\\begin\{tikzpicture\}\[scale=\.88[\s\S]*?\\end\{tikzpicture\}/)?.[0];
 assert(pic,"dual drawing missing");
 const pt={};
 for(const m of pic.matchAll(/\((f[123])\) at \(([-.\d]+),([-.\d]+)\)/g))pt[m[1]]=[+m[2],+m[3]];
 assert(Object.keys(pt).length===3,"three dual vertices");
 const edges=[...pic.matchAll(/\((f[12])\) to\[bend (left|right)=(\d+)\] \(f3\)/g)];
 assert(edges.length===4,"four outer dual edges");
 const dirs={};
 for(const v of ["f1","f2"]){const es=edges.filter(m=>m[1]===v);assert(es.length===2&&new Set(es.map(m=>m[2])).size===2,"two opposite bends per pair");dirs[v]=Math.max(...es.map(m=>+m[3]));}
 const angle=v=>Math.atan2(pt[v][1]-pt.f3[1],pt[v][0]-pt.f3[0]);
 const separation=Math.acos(Math.cos(angle("f1")-angle("f2")))*180/Math.PI;
 assert(dirs.f1+dirs.f2<separation,"incoming tangent cones overlap at F3");
 assert(pic.includes("{$F_3$}")&&pic.match(/\{\$F_3\$\}/g).length===2,"mark exterior face and dual vertex");
 return {separation,bendSum:dirs.f1+dirs.f2,edges:edges.length};
}
if(typeof module!=="undefined")module.exports=check;
if(typeof require!=="undefined"&&require.main===module)console.log(check(require("fs").readFileSync("chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex","utf8")));
