import re
"""Manual local smoke test; starts API, opens UI, generates first project ZIP."""
from pathlib import Path
import subprocess,sys,time,urllib.request,json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with subprocess.Popen([sys.executable,'-m','uvicorn','backend.api:app','--host','127.0.0.1','--port','18765','--log-level','error'],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE) as proc:
    try:
        for _ in range(70):
            try:
                with urllib.request.urlopen('http://127.0.0.1:18765/api/health',timeout=.5) as result:
                    if json.load(result)['ok']:break
            except Exception:time.sleep(.2)
        else:raise RuntimeError('Serwer API nie uruchomił się')
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
            try:
                page=browser.new_page(accept_downloads=True,viewport={'width':1350,'height':870})
                failures=[]
                page.on('pageerror',lambda e:failures.append(str(e)))
                page.goto('http://127.0.0.1:18765/',wait_until='networkidle')
                page.get_by_text(re.compile(r'^\d+ rozdziałów
                page.locator('#openFirst').click()
                page.locator('#addCurrent').click()
                page.locator('button[data-tab="selection"]').click()
                page.locator('#selectedCount').get_by_text('1 elementów').wait_for(timeout=10000)
                page.locator('#checkSelection').click()
                page.get_by_text('Weryfikacja generatora').wait_for(timeout=20000)
                with page.expect_download(timeout=30000) as d:
                    page.locator('#generateZip').click()
                download=d.value
                target=root/'samples'/'browser_generated.zip';download.save_as(target)
                assert target.exists() and target.stat().st_size>1000
                assert not failures,failures
                print(json.dumps({'status':'OK','module_selection':True,'project_generation':True,'filename':download.suggested_filename,'bytes':target.stat().st_size,'javascript_errors':failures},ensure_ascii=False))
            finally:browser.close()
    finally:proc.terminate())).wait_for(timeout=20000)
                page.locator('#openFirst').click()
                page.locator('#addCurrent').click()
                page.locator('button[data-tab="selection"]').click()
                page.locator('#selectedCount').get_by_text('1 elementów').wait_for(timeout=10000)
                page.locator('#checkSelection').click()
                page.get_by_text('Weryfikacja generatora').wait_for(timeout=20000)
                with page.expect_download(timeout=30000) as d:
                    page.locator('#generateZip').click()
                download=d.value
                target=root/'samples'/'browser_generated.zip';download.save_as(target)
                assert target.exists() and target.stat().st_size>1000
                assert not failures,failures
                print(json.dumps({'status':'OK','module_selection':True,'project_generation':True,'filename':download.suggested_filename,'bytes':target.stat().st_size,'javascript_errors':failures},ensure_ascii=False))
            finally:browser.close()
    finally:proc.terminate()