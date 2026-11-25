"""Real-browser regression for captions, multiple targets and ambiguous navigation."""
import os
from pathlib import Path
import sqlite3
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = os.environ.get('MATLIB_TEST_URL','http://127.0.0.1:8765')
with sqlite3.connect(ROOT/'data/biblioteka.db') as db:
    conflict = db.execute('SELECT name FROM label_conflicts ORDER BY name LIMIT 1').fetchone()[0]
    target_module, target_entity = db.execute('SELECT document_id,entity_id FROM label_conflicts WHERE name=? ORDER BY document_id LIMIT 1',(conflict,)).fetchone()

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':1360,'height':900})
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.goto(URL,wait_until='networkidle')
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    link=page.locator('#simplified [data-reference="ch:ga5-rozdmuchania"]').first
    link.filter(has_text='Rozdmuchania i rozwiązywanie').wait_for()
    assert 'ch:ga5' not in link.inner_text()
    link.hover()
    page.locator('#tipBody h3').filter(has_text='Rozdmuchania').wait_for()
    page.locator('#tipOpen').hover()
    assert page.locator('#referenceTip').is_visible()
    page.screenshot(path=str(Path(os.environ['TEMP'])/'atlas-reference-preview.png'))
    page.locator('#tipOpen').click()
    page.wait_for_function("state.currentModule==='ALG-05' && !!state.currentEntity")
    # Each label in a multi-reference must be separately clickable.
    page.evaluate(r"() => renderSimplified('Zobacz \\cref{ch:ga5-rozdmuchania,ch:ga6-powierzchnie}.', 'ALG-08')")
    assert page.locator('#simplified .ref-link').count()==2
    page.locator('#simplified .ref-link').first.filter(has_text='Rozdmuchania').wait_for()
    # Original source text, spaces and starred commands must stay byte-for-byte intact.
    sample=r'Tekst \cref* { ch:ga5-rozdmuchania, ch:ga6-powierzchnie }.'
    actual=page.evaluate("source => {const box=document.createElement('div');showRefs(box,source);return box.textContent;}",sample)
    assert actual==sample,(actual,sample)
    # Clicking an ambiguous reference keeps the chapter picker open.
    page.evaluate(r"label => renderSimplified('Zobacz \\ref{'+label+'}.','TEST')",conflict)
    page.locator('#simplified .ref-link').filter(has_text='Wybierz cel').wait_for()
    page.locator('#simplified .ref-link').click()
    page.locator('#tipBody .ref-choice').first.wait_for()
    page.locator('#tipBody .ref-choice').first.click()
    page.wait_for_function('target => state.currentModule===target[0] && state.currentEntity===target[1]',arg=[target_module,target_entity])
    # Missing explicit targets must not quietly redirect to a different chapter.
    page.evaluate(r"() => renderSimplified('Zobacz \\ref{ALG-08::ch:ga5-rozdmuchania}.','ALG-08')")
    page.locator('#simplified .ref-missing').filter(has_text='Brak celu').wait_for()
    assert not errors,errors
    browser.close()
    print('Reference titles, hover, exact navigation, multiple targets, conflicts, missing labels and source preservation: OK')
