"""Execute actual catalog JavaScript functions with a small Node DOM stub."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"

NODE = r"""
const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const dom={};
function element(tag='',attrs={},text=''){
  return {tag,attrs,textContent:text,children:[],value:'',disabled:false,handlers:{},
    replaceChildren(...children){this.children=children;},
    append(...children){this.children.push(...children);},
    addEventListener(name,callback){this.handlers[name]=callback;}};
}
for(const id of ['leanCatalogSummary','leanCatalogList','leanCatalogSearch','leanCatalogFilter'])
  dom[id]=element();
dom.leanCatalogFilter.value='all';
const visits=[];
const state={leanCatalog:null,leanCatalogLoading:false,leanCatalogEpoch:0};
const data={total:2,ready:1,draft:0,stale:1,items:[
  {formalization_id:'a',source_module:'LST-01',source_label:'thm:good',
    source_entity_id:'entity-a',lean_theorem:'theoremA',lean_theorems:['theoremA'],
    formalization_status:'ready',statement_status:'approved',index_status:'ok'},
  {formalization_id:'b',source_module:'LST-02',source_label:'<bad>',
    source_entity_id:null,lean_theorem:'theoremB',lean_theorems:['theoremB'],
    formalization_status:'stale',statement_status:'needs_review',index_status:'ambiguous_label'}
]};
const ctx={state,$:id=>dom[id],node:element,
  api:async path=>{assert.equal(path,'/api/lean/catalog');return data;},
  tr:x=>String(x??''),loadLeanFragment:query=>visits.push(query),
  leanFormalizationLabels:{ready:'Przypięte',stale:'Nieaktualne'},
  leanStatementLabels:{approved:'Zatwierdzone',needs_review:'Do kontroli'}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
(async()=>{
  await ctx.loadLeanCatalog();
  assert.match(dom.leanCatalogSummary.textContent,/2 formalizacji/);
  assert.equal(dom.leanCatalogList.children.length,2);
  assert.equal(dom.leanCatalogList.children[0].disabled,false);
  assert.equal(dom.leanCatalogList.children[1].disabled,true);
  assert.equal(dom.leanCatalogList.children[1].children[0].textContent,'LST-02 · <bad>');
  assert.match(dom.leanCatalogList.children[1].children[1].textContent,/Niejednoznaczna etykieta/);
  data.items[1].index_status='invalid_label_binding';
  ctx.renderLeanCatalog();
  assert.match(dom.leanCatalogList.children[1].children[1].textContent,/Błędne położenie etykiety/);
  assert.equal(dom.leanCatalogList.children[1].disabled,true);
  dom.leanCatalogList.children[0].handlers.click();
  assert.equal(visits.length,1);
  assert.equal(visits[0].entity_id,'entity-a');
  dom.leanCatalogFilter.value='stale';
  ctx.renderLeanCatalog();
  assert.equal(dom.leanCatalogList.children.length,1);
  assert.equal(dom.leanCatalogList.children[0].disabled,true);
  dom.leanCatalogFilter.value='all';
  dom.leanCatalogSearch.value='THEOREMA';
  ctx.renderLeanCatalog();
  assert.equal(dom.leanCatalogList.children.length,1);
  assert.match(dom.leanCatalogList.children[0].children[0].textContent,/thm:good/);
  dom.leanCatalogSearch.value='unmatched';
  ctx.renderLeanCatalog();
  assert.match(dom.leanCatalogList.children[0].textContent,/Brak pasujących/);
})().catch(err=>{console.error(err);process.exitCode=1;});
"""


class LeanCatalogBrowserTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js required")
    def test_search_filter_ambiguous_link_and_navigation(self):
        js = JS.read_text(encoding="utf-8")
        start = js.index("async function loadLeanCatalog(){")
        end = js.index("async function loadLeanFragment(query){", start)
        result = subprocess.run(
            [shutil.which("node"), "-e", NODE],
            input=js[start:end], capture_output=True, text=True,
            timeout=15, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)


if __name__ == "__main__":
    unittest.main()
