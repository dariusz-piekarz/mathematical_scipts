"""Reader regression check against a running local Atlas (MATLIB_TEST_URL)."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1520, 'height': 900}, color_scheme='light')
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    chapter = (ROOT.parent / 'chapters/pl/algebraic_geometry/08-geometria-biwymierna-i-modele-minimalne-powierzchni.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'ALG-08')", chapter)
    box = page.locator('#simplified')
    page.wait_for_function("document.querySelectorAll('#simplified .preview-figure').length === 4 && [...document.querySelectorAll('#simplified .preview-figure')].every(box => box.querySelector('button') || (box.querySelector('img')?.complete && box.querySelector('img').naturalWidth > 0))", timeout=90000)
    assert box.locator('.preview-figure').count() == 4
    assert box.locator('.preview-figure button').count() == 0, box.locator('.preview-figure').all_inner_texts()
    text = box.inner_text()
    assert r'\providecommand' not in text and r'\noindent' not in text and r'\atlasref' not in text
    assert 'Dlaczego izomorfizm' in box.locator('h3').first.inner_text()
    assert box.locator('.ref-link').filter(has_text='AA-37:').count() == 1
    assert box.locator('.katex').count() > 20
    assert page.locator('#mathPreviewStatus').is_hidden(), page.locator('#mathPreviewStatus').inner_text()
    assert box.locator('.preview-block-title').filter(has_text='Definicja').count() > 0
    layout = box.locator('p').filter(has_text='Przy badaniu').evaluate('el => ({whiteSpace:getComputedStyle(el).whiteSpace,width:el.clientWidth,parent:el.parentElement.clientWidth})')
    assert layout['whiteSpace'] == 'normal' and layout['width'] > layout['parent'] * .9, layout
    # Balanced arguments, comments, math preservation and HTML safety.
    page.evaluate(r'''() => renderSimplified('Tekst pierwszej linii\nciąg dalszy.\n\n\\textbf{Ważne \\emph{zagnieżdżenie}} % komentarz\n $x<y$ <img src=x onerror=alert(1)> \\[a+b\\]', 'ALG-08')''')
    assert box.locator('strong em').inner_text() == 'zagnieżdżenie'
    assert box.locator('img').count() == 0
    assert 'komentarz' not in box.inner_text()
    assert box.locator('.katex').count() == 2
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    dark = box.evaluate('el => ({background:getComputedStyle(el).backgroundColor,color:getComputedStyle(el).color})')
    assert dark['background'] != 'rgb(255, 255, 255)', dark
    page.reload(wait_until='networkidle')
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    page.evaluate("latex => renderSimplified(latex, 'ALG-08')", chapter)
    page.wait_for_function("[...document.querySelectorAll('#simplified .preview-figure img')].filter(img => img.complete && img.naturalWidth > 0).length === 4", timeout=90000)
    box.locator('.preview-figure').first.scroll_into_view_if_needed()
    page.screenshot(path=os.environ.get('MATLIB_SCREENSHOT', str(Path(os.environ['TEMP']) / 'atlas-reader-dark.png')))
    page.set_viewport_size({'width': 390, 'height': 844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'light'
    assert not errors, errors
    browser.close()
    print('Reader prose, math, references, safe content, responsive layout and persistent themes and four rendered TikZ figures: OK')
