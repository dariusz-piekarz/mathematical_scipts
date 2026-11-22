"""Executable Node.js UI regression for declared dependencies and stale responses."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"

NODE = r"""
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
function node(tag,attrs={},content=''){
  return {tag,attrs,textContent:content,children:[],events:{},
    append(...items){this.children.push(...items);},
    replaceChildren(...items){this.children=items;},
    addEventListener(type,handler){this.events[type]=handler;}};
}
const dom={
  leanDependencies:{classList:{remove(){},add(){}}},
  leanDependencyStatus:{textContent:''},
  leanDependencyLimitations:{textContent:''},
  leanDependencyGraph:node('div')
};
const state={leanEpoch:1,leanFragment:{formalization_id:'old'}};
const jobs=[],opened=[];
const ctx={state,$:id=>dom[id],node,URLSearchParams,
  leanFormalizationLabels:{ready:'Przypięte',stale:'Zmiana źródła'},
  openEntity:id=>opened.push(id),
  isCurrentLeanRun:(epoch,item)=>state.leanEpoch===epoch&&state.leanFragment===item,
  api:url=>new Promise(resolve=>jobs.push({url,resolve}))};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
const build=(id,link)=>({
  formalization_id:id,
  nodes:[
    {kind:'latex_statement',label:'LST-01 · <script>alert(1)</script>'},
    {kind:'registered_declaration',label:'theorem_x'},
    {kind:'lean_file',label:'src/T.lean'},
    {kind:'imported_module',label:'Mathlib'}
  ],
  edges:[{kind:'manifest_correspondence'},{kind:'manifest_file'},
         {kind:'declared_import'}],
  source_entity_id:'entity_x',index_status:link,
  formalization_status:'ready',limitations:'To nie graf zależności lematów'
});
(async()=>{
  const old=state.leanFragment,first=ctx.loadLeanDependencies(old,1);
  assert.match(jobs[0].url,/formalization_id=old/);
  state.leanEpoch=2;
  state.leanFragment={formalization_id:'new'};
  const second=ctx.loadLeanDependencies(state.leanFragment,2);
  jobs[0].resolve(build('old','ok'));await first;
  assert.equal(dom.leanDependencyGraph.children.length,0);
  jobs[1].resolve(build('new','ok'));await second;
  assert.equal(dom.leanDependencyGraph.children.length,7);
  const source=dom.leanDependencyGraph.children[0].children[1];
  assert.equal(source.tag,'button');
  assert.equal(source.textContent,'LST-01 · <script>alert(1)</script>');
  source.events.click();
  assert.deepEqual(opened,['entity_x']);
  assert.match(dom.leanDependencyStatus.textContent,/4 węzłów/);
  assert.match(dom.leanDependencyLimitations.textContent,/nie graf zależności lematów/);
  ctx.renderLeanDependencies(build('new','ambiguous_label'));
  assert.equal(dom.leanDependencyGraph.children[0].children[1].tag,'span');
  assert.equal(dom.leanDependencyGraph.children[0].children[1].events.click,undefined);
})().catch(error=>{console.error(error);process.exitCode=1;});
"""


class LeanDependencyBrowserTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js required")
    def test_graph_renders_safely_and_discards_stale_responses(self):
        javascript = JS.read_text(encoding="utf-8")
        start = javascript.index("function renderLeanDependencies(data){")
        end = javascript.index("function openLeanCurrent(){", start)
        process = subprocess.run(
            [shutil.which("node"), "-e", NODE], input=javascript[start:end],
            capture_output=True, text=True, timeout=15, check=False
        )
        self.assertEqual(process.returncode, 0, process.stdout + "\n" + process.stderr)


if __name__ == "__main__":
    unittest.main()
