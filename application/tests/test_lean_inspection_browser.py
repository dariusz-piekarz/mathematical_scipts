"""Node regression for stale and safe Lean expression-constant inspection UI."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"

NODE = r"""
const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const node=(tag,attrs={},text='')=>({tag,attrs,textContent:text,children:[],
 append(...children){this.children.push(...children);},
 replaceChildren(...children){this.children=children;}});
const ui={
 leanInspect:{disabled:false,textContent:'Odczytaj stałe przez Lean'},
 leanInspection:node('div')
};
const state={leanEpoch:1,leanFragment:{formalization_id:'old',formalization_status:'ready'},
 leanRunner:{ready:true}};
const requests=[];
const ctx={state,$:id=>ui[id],node,
 api:(url,args)=>new Promise(resolve=>requests.push({url,args,resolve})),
 isCurrentLeanRun:(epoch,item)=>epoch===state.leanEpoch&&item===state.leanFragment};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
(async()=>{
 const first=ctx.inspectLeanConstants();
 assert.equal(requests.length,1);
 assert.equal(requests[0].url,'/api/lean/dependencies/inspect');
 assert.deepEqual(JSON.parse(requests[0].args.body),{formalization_id:'old'});
 state.leanEpoch=2;
 state.leanFragment={formalization_id:'new',formalization_status:'ready'};
 ui.leanInspection.textContent='New selection';
 requests[0].resolve({inspection_status:'complete',constants:{old:['Eq']}});
 await first;
 assert.equal(ui.leanInspection.textContent,'New selection');

 const second=ctx.inspectLeanConstants();
 requests[1].resolve({inspection_status:'complete',extraction_method:'Lean.ConstantInfo.getUsedConstantsAsSet',
  detail:'From actual Lean run',constants:{theorem_new:['<script>evil</script>','Eq']}});
 await second;
 assert.equal(ui.leanInspection.children.length,3);
 const group=ui.leanInspection.children[1];
 assert.equal(group.children[0].textContent,'theorem_new · 2 stałych');
 assert.equal(group.children[1].children[0].textContent,'<script>evil</script>');
 assert.match(ui.leanInspection.children[2].textContent,/certyfikat: NIE/);
 assert.equal(ui.leanInspect.disabled,false);
 const third=ctx.inspectLeanConstants();
 requests[2].resolve({inspection_status:'blocked',detail:'SHA changed',constants:{}});
 await third;
 assert.match(ui.leanInspection.children[0].textContent,/blocked/);
 assert.match(ui.leanInspection.children[0].textContent,/SHA changed/);
})().catch(e=>{console.error(e);process.exitCode=1;});
"""


class LeanInspectionBrowserTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js is required")
    def test_introspection_ui_is_scoped_and_safe(self):
        source=JS.read_text(encoding="utf-8")
        start=source.index("function renderLeanInspection(result){")
        end=source.index("function openLeanCurrent(){",start)
        result=subprocess.run(
            [shutil.which("node"),"-e",NODE],input=source[start:end],
            capture_output=True,text=True,timeout=15,check=False)
        self.assertEqual(result.returncode,0,result.stdout+"\n"+result.stderr)


if __name__=="__main__":
    unittest.main()
