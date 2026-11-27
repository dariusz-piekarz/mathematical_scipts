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
    # Explicit captions use the source's macros, while tooltip content uses
    # the destination chapter's macros, even when detached from its header.
    page.evaluate(r"""() => {
        const box=document.getElementById('simplified');
        box.replaceChildren(createReferenceLink('ALG-05::ch:ga5-rozdmuchania','AM1-36',
            {caption:'$\\HK$'}));
    }""")
    page.locator('#simplified .ref-link .katex').wait_for()
    assert page.locator('#simplified .ref-link .katex-html').inner_text() == 'KH'
    page.evaluate(r"() => renderSimplified('Zobacz \\ref{AM1-36::ma1:kh:lem:variation-additivity}.','ALG-08')")
    link=page.locator('#simplified .ref-link')
    link.hover()
    page.locator('#tipBody .tip-code .katex-html').filter(has_text='BV').first.wait_for()
    assert 'Nie złożono' not in page.locator('#tipBody').inner_text()
    page.evaluate("() => closeTip()")
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
    # A slow label lookup must not override a more recent chapter selection.
    # A source-specific cached preview must not answer an unqualified lookup.
    cases = page.evaluate("""async () => {
        const originalApi = api;
        let pending, count = 0;
        const toastBox = document.getElementById('toast');
        const resetToast = () => {toastBox.textContent = ''; toastBox.classList.add('hidden');};
        try {
            api = (url, options) => url.startsWith('/api/labels/atlas-race-test')
                ? new Promise((resolve, reject) => {pending = {resolve, reject};})
                : originalApi(url, options);
            for (const result of [{entity_id:'invalid'}, {document_id:'invalid'},
                                  {ambiguous:true}, null]) {
                closeTip(); resetToast(); pending = null;
                const old = openLabel('atlas-race-test','ALG-08');
                await openModule('ALG-08');
                if (!pending) throw Error('lookup not intercepted');
                if (result === null) pending.reject(new Error('obsolete error'));
                else pending.resolve(result);
                await old;
                if (state.currentModule !== 'ALG-08' || state.currentEntity !== null ||
                    toastBox.textContent || !document.getElementById('referenceTip').classList.contains('hidden'))
                    throw Error('obsolete lookup changed current view');
                count++;
            }
            closeTip(); pending = null;
            state.tooltipData = {name:'atlas-race-test', source_document:'ALG-05',
                                 entity_id:'invalid'};
            const current = openLabel('atlas-race-test');
            if (!pending) throw Error('wrong source cache reused');
            pending.resolve({document_id:'ALG-08'});
            await current;
            if (state.currentModule !== 'ALG-08' || state.currentEntity !== null)
                throw Error('uncached target not opened');
            count++;
        } finally {
            api = originalApi; closeTip(); resetToast();
        }
        return count;
    }""")
    assert cases == 5
    # Search responses cannot reopen a dismissed dropdown or replace a
    # more recent query, including repeated submission of the same text.
    search_cases = page.evaluate("""async () => {
        const originalApi = api, input = document.getElementById('searchInput');
        const list = document.getElementById('searchResults');
        const toastBox = document.getElementById('toast');
        const requests = [];
        let count = 0;
        try {
            api = (url, options) => url.startsWith('/api/search?')
                ? new Promise((resolve, reject) => requests.push({resolve, reject}))
                : originalApi(url, options);
            for (const mode of ['escape', 'outside', 'repeat', 'change']) {
                for (const failure of [false, true]) {
                    dismissSearch(); requests.length = 0;
                    toastBox.textContent = ''; input.value = 'alpha';
                    const old = performSearch('alpha');
                    if (mode === 'escape') {
                        input.dispatchEvent(new KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
                    } else if (mode === 'outside') {
                        document.getElementById('docTitle').click();
                    } else {
                        input.value = mode === 'change' ? 'beta' : 'alpha';
                        const current = performSearch(input.value);
                        requests[1].resolve({items:[]}); await current;
                    }
                    const before = list.firstChild;
                    if (failure) requests[0].reject(new Error('stale search'));
                    else requests[0].resolve({items:[]});
                    await old;
                    const dismissed = mode === 'escape' || mode === 'outside';
                    if (list.classList.contains('hidden') !== dismissed ||
                        list.firstChild !== before || toastBox.textContent !== '')
                        throw Error('stale search: ' + mode);
                    count++;
                }
            }
        } finally {
            api = originalApi; input.value = ''; dismissSearch();
            toastBox.textContent = ''; toastBox.classList.add('hidden');
        }
        return count;
    }""")
    assert search_cases == 8
    assert not errors,errors
    browser.close()
    print('Reference titles, hover, exact navigation, multiple targets, conflicts, missing labels and source preservation: OK')
