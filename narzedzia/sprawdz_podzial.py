#!/usr/bin/env python3
"""Kontrola odtworzenia oryginału z rozdziałów; ścieżki względem katalogu repozytorium."""
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'manifest.json').read_text('utf8'))
errors=0
for d in m['documents']:
    raw=(root/'zrodla'/d['source']).read_bytes().decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
    prefix=raw[:d['prefix_length']]
    tail=raw[-d['tail_length']:]
    body=raw[d['prefix_length']:-d['tail_length']]
    lead=body[:d['body_prefix_length']]
    chapters=[(root/c['path']).read_text('utf8') for c in d['chapters']]
    joined=prefix+lead+''.join(chapters)+tail
    imports=''.join('\\input{../'+c['path']+'}\n' for c in d['chapters'])
    expected_master=prefix+lead+('\n' if lead and not lead.endswith('\n') else '')+imports+tail
    master=(root/d['script']).read_text('utf8')
    sha=lambda t:hashlib.sha256(t.encode('utf8')).hexdigest()
    valid=(joined==raw and master==expected_master and sha(raw)==d['sha256_normalized_source']
      and all(sha(t)==c['sha256'] for c,t in zip(d['chapters'],chapters)))
    print(('OK: ' if valid else 'BLAD: ')+d['script'])
    errors+=not valid
sys.exit(int(errors>0))
