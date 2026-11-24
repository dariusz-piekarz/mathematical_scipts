"""Execute the actual transcription UI with controlled HTTP completions."""
from pathlib import Path
import shutil
import subprocess
import unittest

JS = Path(__file__).resolve().parents[1] / "frontend" / "app.js"
NODE = r"""
const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const dom=Object.fromEntries(['leanTranscriptionConsent','leanTranscriptionPrepare','leanTranscriptionStatus','leanTranscriptionPackage'].map(x=>[x,{checked:false,disabled:false,textContent:''}]));
const state={leanEpoch:1,leanTranscriptionEpoch:0,leanTranscriptionBusy:false,leanFragment:null};
const jobs=[];
const ctx={state,$:id=>dom[id],TextEncoder,api:(url,args)=>new Promise((resolve,reject)=>jobs.push({url,args,resolve,reject}))};
vm.createContext(ctx);vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
const sha='a'.repeat(64);
const item=id=>({source_entity:id,source_module:'LST-01',source_labels:['thm:'+id],source_linkage:'exact_entity',source_sha256:sha,source_latex:'<script>ą</script>',start_line:1,end_line:3});
const packet=x=>({schema_version:1,status:'prepared',experimental:true,source_scope:'indexed_snapshot_only',
 source_module:x.source_module,source_entity:x.source_entity,source_label:x.source_labels[0],start_line:1,end_line:3,
 source_sha256:sha,source_latex:x.source_latex,source_bytes:new TextEncoder().encode(x.source_latex).length,
 source_document_sha256:sha,source_binding_sha256:sha,request_id:sha,candidate_status:'not_generated',lean_code:null,
 statement_status:'unreviewed',proof_status:'not_run',certificate:false,external_provider:null,external_transfer_allowed:false,
 license_status:'unreviewed',external_budget_minor_units:0,external_cost_minor_units:0,registry_written:false,canonical_source_written:false});
function select(x){++state.leanEpoch;state.leanFragment=x;ctx.resetLeanTranscription(x);}
function consent(){dom.leanTranscriptionConsent.checked=true;ctx.updateLeanTranscriptionConsent();}
(async()=>{
 const a=item('a'),b=item('b'),status=dom.leanTranscriptionStatus,output=dom.leanTranscriptionPackage,button=dom.leanTranscriptionPrepare;
 select(a);assert.equal(button.disabled,true);await ctx.prepareLeanTranscription();assert.equal(jobs.length,0);
 consent();assert.equal(button.disabled,false);const first=ctx.prepareLeanTranscription();await ctx.prepareLeanTranscription();
 assert.equal(jobs.length,1);assert.equal(jobs[0].url,'/api/lean/transcription/prepare');
 assert.deepEqual(JSON.parse(jobs[0].args.body),{entity_id:'a',expected_source_sha256:sha,consent:true});
 select(b);assert.equal(dom.leanTranscriptionConsent.checked,false);consent();const second=ctx.prepareLeanTranscription();
 jobs[0].resolve(packet(a));await first;assert.equal(output.textContent,'');
 jobs[1].resolve(packet(b));await second;assert.match(status.textContent,/Nie wygenerowano/);
 assert.equal(JSON.parse(output.textContent).source_latex,b.source_latex);assert.equal(button.disabled,true);
 consent();const third=ctx.prepareLeanTranscription();select(a);jobs[2].reject(Error('old error'));await third;
 assert.doesNotMatch(status.textContent,/old error/);assert.equal(output.textContent,'');
 for(const invalid of [{certificate:true},{source_sha256:'b'.repeat(64)},{source_entity:'wrong'},{external_cost_minor_units:1}]){
   consent();const next=ctx.prepareLeanTranscription();jobs.at(-1).resolve({...packet(a),...invalid});await next;
   assert.match(status.textContent,/Niezgodny format/);assert.equal(output.textContent,'');
 }
 consent();const last=ctx.prepareLeanTranscription();jobs.at(-1).reject(Error('409'));await last;assert.match(status.textContent,/409/);
 select({...b,source_linkage:'proof_of_adjacent_theorem'});consent();const count=jobs.length;await ctx.prepareLeanTranscription();assert.equal(jobs.length,count);
})().catch(e=>{console.error(e);process.exitCode=1;});
"""

class LeanTranscriptionBrowserTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js required")
    def test_transcription_consent_provenance_and_stale_responses(self):
        js = JS.read_text(encoding="utf-8")
        start = js.index("function canPrepareLeanTranscription(item){")
        end = js.index("async function loadLeanFragment(query){", start)
        result = subprocess.run([shutil.which("node"), "-e", NODE],
                                input=js[start:end], capture_output=True, text=True,
                                timeout=15, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)
