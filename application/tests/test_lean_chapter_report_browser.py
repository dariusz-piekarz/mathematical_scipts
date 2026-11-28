"""Execute actual chapter-report frontend code against deterministic responses."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"
NODE = r"""
const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
function el(){return {value:'',textContent:'',children:[],replaceChildren(){this.children=[];},append(x){this.children.push(x);}};}
const dom={leanChapterModule:el(),leanChapterReportSummary:el(),leanChapterReportItems:el()};
const requests=[];
const ctx={state:{leanChapterReportEpoch:0},$:id=>dom[id],
  node:(tag,attrs,text)=>({tag,attrs,textContent:text}),
  leanFormalizationLabels:{ready:'Przypięte'},leanStatementLabels:{approved:'Zatwierdzone'},
  api:path=>new Promise((resolve,reject)=>requests.push({path,resolve,reject}))};
vm.createContext(ctx);vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
function report(id,items=[]){return {report_schema_version:1,source_module:id,scope:'manifest_and_index_only',
 certificate:false,proof_status_included:false,run_history_checked:false,dependency_fingerprint_checked:false,
 source_index_status:'ok',source_document_sha256:'a'.repeat(64),total:items.length,ready:items.length,draft:0,stale:0,
 statement_approved:items.length,items};}
(async()=>{
  const summary=dom.leanChapterReportSummary,list=dom.leanChapterReportItems;
  dom.leanChapterModule.value='LST-01';const first=ctx.loadLeanChapterReport();
  assert.equal(requests[0].path,'/api/lean/chapter-report?module_id=LST-01');
  dom.leanChapterModule.value='LST-02';const second=ctx.loadLeanChapterReport();
  requests[1].resolve(report('LST-02',[{source_label:'<tag>',lean_theorem:'t',formalization_status:'ready',statement_status:'approved',index_status:'ok'}]));
  await second;assert.match(summary.textContent,/LST-02/);assert.match(summary.textContent,/nie jest certyfikatem/);
  assert.match(summary.textContent,/a{64}/);assert.match(list.children[0].textContent,/<tag>/);
  requests[0].resolve(report('LST-01'));await first;assert.match(summary.textContent,/LST-02/);
  dom.leanChapterModule.value='LST-03';const third=ctx.loadLeanChapterReport();
  ctx.clearLeanChapterReport();requests[2].reject(Error('old'));await third;
  assert.match(summary.textContent,/Wybierz/);assert.equal(list.children.length,0);
  const fourth=ctx.loadLeanChapterReport();requests[3].resolve(report('LST-03'));await fourth;
  assert.match(list.children[0].textContent,/Brak rejestracji/);
  const fifth=ctx.loadLeanChapterReport();requests[4].resolve({...report('LST-03'),certificate:true});await fifth;
  assert.match(summary.textContent,/Nieobsługiwany format/);assert.equal(list.children.length,0);
  const sixth=ctx.loadLeanChapterReport();requests[5].reject(Error('404'));await sixth;
  assert.match(summary.textContent,/404/);
  dom.leanChapterModule.value='';await ctx.loadLeanChapterReport();assert.equal(requests.length,6);
})().catch(e=>{console.error(e);process.exitCode=1;});
"""

class LeanChapterReportBrowserTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js required")
    def test_chapter_report_async_provenance_and_errors(self):
        js = JS.read_text(encoding="utf-8")
        start = js.index("function clearLeanChapterReport(){")
        end = js.index("async function loadLeanFragment(query){", start)
        result = subprocess.run([shutil.which("node"), "-e", NODE],
                                input=js[start:end], capture_output=True, text=True,
                                timeout=15, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)
