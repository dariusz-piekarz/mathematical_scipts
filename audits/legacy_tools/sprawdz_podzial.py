#!/usr/bin/env python3
"""Weryfikacja dokładnej zawartości podzielonych skryptów LaTeX."""
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
# Od iteracji II: weryfikacja bazowa z uwzględnieniem kontrolowanych integracji.
if (ROOT/'manifest_integracji.json').is_file():
    import subprocess
    sys.exit(subprocess.call([sys.executable, str(ROOT/'narzedzia/sprawdz_integracje.py')]))
manifest=json.loads((ROOT/'manifest.json').read_text('utf-8'))
failed=False
for d in manifest['documents']:
 b=(ROOT/'zrodla'/d['source']).read_bytes().decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
 prefix=b[:d['prefix_length']]
 end=b[-d['tail_length']:]
 body=b[d['prefix_length']:-d['tail_length']]
 pfx=body[:d['body_prefix_length']]
 chapter_texts=[(ROOT/c['path']).read_text('utf-8') for c in d['chapters']]
 check=prefix+pfx+''.join(chapter_texts)+end
 book=(ROOT/d['script']).read_text('utf-8')
 want=prefix+pfx+('\n' if pfx and not pfx.endswith('\n') else '')+''.join('\\input{../'+c['path']+'}\n' for c in d['chapters'])+end
 good=(b==check and book==want and hashlib.sha256(b.encode('utf-8')).hexdigest()==d['sha256_normalized_source'])
 good=good and all(hashlib.sha256(t.encode('utf-8')).hexdigest()==c['sha256'] for c,t in zip(d['chapters'],chapter_texts))
 print(('OK ' if good else 'BŁĄD ')+d['script']+f' — {len(d["chapters"])} plików')
 if not good:failed=True
sys.exit(1 if failed else 0)
