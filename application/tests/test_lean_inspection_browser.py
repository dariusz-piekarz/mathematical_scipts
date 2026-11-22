"""Node regression for stale and safe Lean expression-constant inspection UI."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"

NODE = r"""
const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const node=(tag,attrs={},text='')=>({tag,attrs,textContent:text,children:[],events:{},
 append(...children){this.children.push(...children);},
 replaceChildren(...children){this.children=children;},
 addEventListener(type,callback){this.events[type]=callback;}});
const ui={
 leanInspect:{disabled:false,textContent:'Odczytaj stałe przez Lean'},
 leanInspection:node('div')
};
const state={leanEpoch:1,leanFragment:{formalization_id:'old',formalization_status:'ready'},
 leanRunner:{ready:true}};
const requests=[],visits=[];
const ctx={state,$:id=>ui[id],node,
 loadLeanFragment:query=>visits.push(query),
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
 state.leanCatalog={items:[
   {formalization_id:'candidate',source_module:'LST-01',source_label:'thm:example',
    source_entity_id:'valid-e1',index_status:'ok',formalization_status:'ready',
    lean_theorems:['Aux.value']},
   {formalization_id:'amb1',source_entity_id:'amb-e2',index_status:'ok',
    formalization_status:'ready',lean_theorems:['Ambiguous']},
   {formalization_id:'amb2',source_entity_id:'amb-e3',index_status:'ok',
    formalization_status:'ready',lean_theorems:['Ambiguous']},
   {formalization_id:'stale',source_entity_id:'stale-e4',index_status:'ok',
    formalization_status:'stale',lean_theorems:['Old.value']}
 ]};
 ctx.renderLeanInspection({inspection_status:'complete',
   detail:'from Lean',extraction_method:'method',
   constants:{new_thm:['Aux.value','Ambiguous','Old.value']}});
 const linked=ui.leanInspection.children[1].children[1].children;
 assert.equal(linked[0].children[0].tag,'button');
 assert.equal(linked[0].children[0].textContent,'Aux.value');
 linked[0].children[0].events.click();
 assert.equal(visits.length,1);
 assert.equal(visits[0].entity_id,'valid-e1');
 assert.equal(linked[1].children.length,0,'ambiguous declaration must not navigate');
 assert.equal(linked[2].children.length,0,'stale declaration must not navigate');
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
