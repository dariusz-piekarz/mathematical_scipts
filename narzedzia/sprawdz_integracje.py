#!/usr/bin/env python3
"""Iteracja II: każda zmiana musi być dokładnie opisaną zamianą fragmentu
na wspólne \\input; pozostałe 234 rozdziały i oryginały muszą pozostać identyczne.
"""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
base=json.loads((root/'manifest.json').read_text('utf8'))
integration=json.loads((root/'manifest_integracji.json').read_text('utf8'))
patches={x['path']:x for x in integration['modifications']}
errors=[]
h=lambda s:hashlib.sha256(s.encode('utf8')).hexdigest()
shared=(root/integration['shared_module']).read_text('utf8')
if h(shared)!=integration['shared_module_sha256']: errors.append('wspolne: suma kontrolna')
if shared.count('\\label{tw:ga10-weak}')!=1 or shared.count('\\label{thm:xvii-weak-lefschetz}')!=1: errors.append('brak aliasów twierdzenia')
if 'biblioteka@slabelefschetz@loaded' not in shared: errors.append('brak strażnika dwukrotnego włączenia')
modified_count=0
for doc in base['documents']:
    source=(root/'zrodla'/doc['source']).read_bytes().decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
    if h(source)!=doc['sha256_normalized_source']:errors.append(f"źródło zmienione: {doc['source']}")
    begin=source[:doc['prefix_length']]; end=source[-doc['tail_length']:]
    body=source[doc['prefix_length']:-doc['tail_length']]; head=body[:doc['body_prefix_length']]
    pos=doc['body_prefix_length']; originals=[]
    for chap in doc['chapters']:
        original=body[pos:pos+chap['length']];pos+=chap['length']
        path=chap['path'];actual=(root/path).read_text('utf8')
        if h(original)!=chap['sha256']:errors.append(f'niezgodny manifest źródła: {path}')
        if path in patches:
            modified_count+=1
            patch=patches[path]
            a=original.find(patch['start_anchor'])
            if a<0:errors.append('brak wyjściowego fragmentu '+path);continue
            b=original.find('\\end{twierdzenie}',a)
            if b<0:errors.append('brak końca twierdzenia '+path);continue
            b+=len('\\end{twierdzenie}')
            if patch['mode']=='theorem-proof':
                q=original.find('\\end{proof}',b)
                if q<0:errors.append('brak końca dowodu '+path);continue
                b=q+len('\\end{proof}')
            removed=original[a:b]
            expected=original[:a]+patch['replacement']+original[b:]
            if h(removed)!=patch['original_fragment_sha256']:errors.append('zmieniony fragment oryginalny '+path)
            if expected!=actual:errors.append('nieautoryzowane zmiany w '+path)
            if h(actual)!=patch['new_chapter_sha256']:errors.append('nowa suma kontrolna nie zgadza się '+path)
        elif original!=actual: errors.append('niezamierzona zmiana '+path)
        originals.append(original)
    if pos!=len(body):errors.append('fragmenty nie pokrywają całości '+doc['source'])
    if begin+head+''.join(originals)+end !=source:errors.append('odtwarzanie oryginału '+doc['source'])
    book=(root/doc['script']).read_text('utf8')
    imports=''.join('\\input{../'+ch['path']+'}\n' for ch in doc['chapters'])
    expected_main=begin+head+('\n' if head and not head.endswith('\n') else '')+imports+end
    if book!=expected_main:errors.append('zmieniony skrypt główny '+doc['script'])
print('Kontrola źródeł: 12; oryginalne rozdziały: 236; celowe zmiany:',modified_count)
if errors:
    print('NIEPOWODZENIE:',*errors,sep='\n- ')
    sys.exit(1)
print('OK — oryginały odtwarzalne; jedynie dwa fragmenty przeniesiono do wspólnego modułu.')
