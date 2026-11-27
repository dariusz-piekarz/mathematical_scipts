"""Check TeX headings and viewport-bound reader scrolling in real Chromium."""
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')


def assert_viewport_layout(page):
    metrics = page.evaluate("""() => {
        const root=document.scrollingElement, view=document.getElementById('view-reader');
        const box=view.getBoundingClientRect();
        return {height:innerHeight,width:innerWidth,rootHeight:root.scrollHeight,
                rootWidth:root.scrollWidth,scrollY,readerBottom:box.bottom,
                readerHeight:view.clientHeight,readerScroll:view.scrollHeight};
    }""")
    assert metrics['rootHeight'] <= metrics['height'] + 1, metrics
    assert metrics['rootWidth'] <= metrics['width'] + 1, metrics
    assert abs(metrics['readerBottom'] - metrics['height']) <= 1, metrics
    assert metrics['readerHeight'] > 0, metrics
    assert metrics['scrollY'] == 0, metrics
    return metrics


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1934, 'height': 877})
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.evaluate("() => openModule('AM1-14')")
    page.locator('#simplified .katex').first.wait_for(state='attached')

    # Previously KaTeX's absolute MathML spans enlarged the document to over
    # 6000 px while the reader remained one viewport tall. Scrolling the outer
    # document exposed a large blank region below the application.
    for width, height in ((1934, 877), (1547, 702), (967, 439), (390, 844), (390, 350)):
        page.set_viewport_size({'width': width, 'height': height})
        metrics = assert_viewport_layout(page)
        assert metrics['readerScroll'] > metrics['readerHeight'], metrics
        page.locator('#view-reader').evaluate('el => {el.scrollTop=el.scrollHeight}')
        page.mouse.move(width - 35, height - 35)
        page.mouse.wheel(0, 10000)
        page.wait_for_function('window.scrollY === 0')
        assert_viewport_layout(page)
        assert page.locator('#view-reader').evaluate('el => el.scrollTop > 0')
        if width == 1934:
            page.screenshot(path=str(Path(os.environ.get('TEMP', '/tmp')) / 'atlas-reader-am1-14-fixed.png'))

    page.set_viewport_size({'width': 1360, 'height': 900})
    page.locator('#view-reader').evaluate('el => {el.scrollTop=0}')
    for _ in range(8):
        page.locator('#textSizeUp').click()
    assert page.locator('#textSizeUp').is_disabled()
    assert_viewport_layout(page)
    assert page.locator('#tree').evaluate('el => el.scrollHeight > el.clientHeight')

    # Fullscreen retains the same single reader scroll owner with large text.
    page.locator('#readingMode').click()
    page.wait_for_function('document.fullscreenElement !== null')
    assert_viewport_layout(page)
    page.keyboard.press('Escape')
    page.wait_for_function("!document.documentElement.classList.contains('reading-mode')")
    assert_viewport_layout(page)
    page.locator('#textSizeReset').click()

    # Switching between short previews, full chapters and other tabs must not
    # leave an independently scrollable document underneath the app shell.
    for module in ('DG-14', 'ALG-10', 'AM1-14'):
        for full in (False, True):
            page.evaluate('([module,full]) => openModule(module,full)', [module, full])
            assert_viewport_layout(page)
            page.evaluate('window.scrollTo(0,100000)')
            assert_viewport_layout(page)

    page.evaluate("() => openModule('ALG-10', true)")
    tables = page.locator('#simplified .preview-table')
    assert tables.count() > 0
    assert tables.first.locator('tr').count() >= 2
    assert tables.first.locator('.katex').count() > 0
    assert r'\hline' not in tables.first.inner_text()
    assert tables.first.locator('.preview-rule-bottom').count() > 0

    table_source = (r'\begin{tabular}{cc}\hline '
                    r'\textbf{A\&B}&$\begin{aligned}x&=1\\y&=2\end{aligned}$\\\hline '
                    r'\textit{C}&D\\\hline\end{tabular}')
    page.evaluate("source => renderSimplified(source, 'DG-14')", table_source)
    table = page.locator('#simplified .preview-table')
    assert table.locator('tr').count() == 2
    assert table.locator('td').count() == 4
    assert table.locator('strong').inner_text() == 'A&B'
    assert table.locator('.katex').count() == 1
    assert table.locator('.preview-rule-bottom').count() == 2
    assert page.locator('#mathPreviewStatus').is_hidden()
    assert_viewport_layout(page)

    source = (r'\chapter{Test \texorpdfstring{\emph{Visible $x^2$}}{PDF-ONLY}}'
              r'\section{\texorpdfstring{Second \texorpdfstring{$\alpha$}{INNER-PDF}}{OUTER-PDF}}'
              r'\texorpdfstring{Body \textbf{bold}}{BODY-PDF}')
    page.evaluate("source => renderSimplified(source, 'DG-14')", source)
    box = page.locator('#simplified')
    assert box.locator('h2 em .katex').count() == 1
    assert box.locator('h3 .katex').count() == 1
    assert box.locator('strong').inner_text() == 'bold'
    assert 'texorpdfstring' not in box.inner_text()
    assert 'PDF' not in box.inner_text()
    assert page.locator('#mathPreviewStatus').is_hidden()

    # Real chapter-local macros must also work in detached theorem fragments.
    page.evaluate("() => openModule('AM1-36')")
    assert page.evaluate(r"() => previewMacros('AM1-36')['\\HK']") == r"\mathrm{KH}"
    fragment = r"$\R,\C,\K,\HK,\Var_I F,\osc_I F,\BV,\ind{A}$"
    page.evaluate("source => renderSimplified(source, 'AM1-36')", fragment)
    assert box.locator('.katex').count() == 1
    assert box.locator('.katex-error').count() == 0
    assert page.locator('#mathPreviewStatus').is_hidden()
    assert page.evaluate(r"() => previewMacros('AM1-14')['\\HK'] === undefined")
    assert page.evaluate(r"() => previewMacros('MOD')['\\Q']") == r"\mathrm Q"

    # Keep wide equations and code independently scrollable, rather than
    # hiding document overflow and accidentally clipping their contents.
    wide = r'\[' + '+'.join(f'x_{{{i}}}' for i in range(100)) + r'\]'
    listing = r'\begin{lstlisting}' + '\n' + 'long_code = ' + 'value + ' * 100 + '\n' + r'\end{lstlisting}'
    page.evaluate("source => renderSimplified(source, 'DG-14')", wide + listing)
    for selector in ('.katex-display', '.preview-listing'):
        assert box.locator(selector).evaluate('el => el.scrollWidth > el.clientWidth'), selector
    assert_viewport_layout(page)
    page.screenshot(path=str(Path(os.environ.get('TEMP', '/tmp')) / 'atlas-reader-layout-fixed.png'))
    assert not errors, errors
    browser.close()
    print('TeX/PDF headings, viewport fill, one reader scroll owner, small viewport, large text, fullscreen and local wide content: OK')
