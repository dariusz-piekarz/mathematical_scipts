"""Execute the actual Lean UI async handler in Node with controlled HTTP completions."""
from pathlib import Path
import shutil
import subprocess
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "frontend" / "app.js"

NODE_TEST = r"""
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const elements={
  leanRun:{disabled:false,textContent:'Uruchom Lean'},
  leanLog:{textContent:''},leanRunnerInfo:{textContent:''}
};
const state={
  leanEpoch:1,
  leanFragment:{formalization_id:'old',formalization_status:'ready',proof_status:'not_run'},
  leanRunner:{ready:true}
};
const jobs=[],renders=[];
const ctx={
  state,$:id=>elements[id],
  api:()=>new Promise((resolve,reject)=>jobs.push({resolve,reject})),
  renderLeanFragment:item=>{
    renders.push(item.formalization_id);
    elements.leanRun.disabled=true;
  }
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(0,'utf8'),ctx);
(async()=>{
  const first=ctx.runLeanFormalization();
  assert.equal(jobs.length,1);
  // New fragment opens before the first Lean process has finished.
  state.leanEpoch=2;
  state.leanFragment={formalization_id:'new',formalization_status:'ready',proof_status:'not_run'};
  elements.leanRun.disabled=false;
  elements.leanRun.textContent='Uruchom Lean';
  elements.leanLog.textContent='Nowy fragment';
  jobs[0].resolve({proof_status:'compiled',detail:'Stary wynik',certificate:false});
  await first;
  assert.deepEqual(renders,[]);
  assert.equal(state.leanFragment.proof_status,'not_run');
  assert.equal(elements.leanLog.textContent,'Nowy fragment');
  assert.equal(elements.leanRun.disabled,false);

  // Only a result matching the current fragment changes the screen.
  const second=ctx.runLeanFormalization();
  jobs[1].resolve({proof_status:'compiled',detail:'Nowy wynik',certificate:false});
  await second;
  assert.deepEqual(renders,['new']);
  assert.equal(state.leanFragment.proof_status,'compiled');
  assert.match(elements.leanLog.textContent,/Nowy wynik/);
  assert.match(elements.leanRunnerInfo.textContent,/Brak certyfikatu/);
  assert.equal(elements.leanRun.disabled,false);

  // Rejected old request must not show an error in the next fragment.
  const third=ctx.runLeanFormalization();
  state.leanEpoch=3;
  state.leanFragment={formalization_id:'third',formalization_status:'ready',proof_status:'not_run'};
  elements.leanLog.textContent='Trzeci fragment';
  jobs[2].reject(new Error('Stary błąd'));
  await third;
  assert.equal(elements.leanLog.textContent,'Trzeci fragment');
  assert.deepEqual(renders,['new']);

  const fourth=ctx.runLeanFormalization();
  jobs[3].reject(new Error('Bieżący błąd'));
  await fourth;
  assert.match(elements.leanLog.textContent,/Bieżący błąd/);
  assert.equal(elements.leanRun.disabled,false);
})().catch(e=>{console.error(e);process.exitCode=1;});
"""

class LeanAsyncUiTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js required for executable JS regression")
    def test_stale_verification_response_does_not_override_new_fragment(self):
        js = SOURCE.read_text(encoding="utf-8")
        start = js.index("function isCurrentLeanRun(")
        end = js.index("\nasync function init()", start)
        result = subprocess.run(
            [shutil.which("node"), "-e", NODE_TEST],
            input=js[start:end], capture_output=True, text=True, timeout=15, check=False
        )
        self.assertEqual(result.returncode, 0, result.stdout + "\n" + result.stderr)

if __name__ == "__main__":
    unittest.main()
