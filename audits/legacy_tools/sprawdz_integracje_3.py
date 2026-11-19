#!/usr/bin/env python3
"""Audyt integralności trzech iteracji: 12 oryginałów, 236 plików, wyłącznie zadeklarowane edycje."""
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
j=lambda name:json.loads((ROOT/name).read_text('utf8'))
base=j('manifest.json');v2=j('manifest_integracji.json');v3=j('manifest_integracji_3.json')
sha=lambda x:hashlib.sha256(x.encode('utf8')).hexdigest()
errors=[];count2=count3=0
patch2={x['path']:x for x in v2['modifications']}
patch3={}
for p in v3['modifications']:
    patch3.setdefault(p['path'],[]).append(p)

def apply_v2(raw,p):
    a=raw.find(p['start_anchor'])
    if a<0:raise ValueError('brak kotwicy II')
    b=raw.find('\\end{twierdzenie}',a)
    if b<0:raise ValueError('brak końca twierdzenia II')
    b+=len('\\end{twierdzenie}')
    if p['mode']=='theorem-proof':
        b=raw.find('\\end{proof}',b)
        if b<0:raise ValueError('brak końca dowodu II')
        b+=len('\\end{proof}')
    assert sha(raw[a:b])==p['original_fragment_sha256'], 'hash fragmentu II'
    new=raw[:a]+p['replacement']+raw[b:]
    assert sha(new)==p['new_chapter_sha256'], 'hash rozdziału II'
    return new

def apply_v3(raw,p):
    assert sha(raw)==p['stage2_chapter_sha256'], 'hash rozdziału poprzedniego III'
    a=raw.find(p['start_anchor']);assert a>=0,'brak kotwicy III'
    b=raw.find(p['end_anchor'],a);assert b>=0,'brak końca fragmentu III'
    b+=len(p['end_anchor'])
    assert sha(raw[a:b])==p['removed_sha256'] and len(raw[a:b])==p['removed_chars'], 'niezgodny usunięty fragment III'
    assert sha(p['replacement'])==p['replacement_sha256'], 'niezgodna wstawka III'
    new=raw[:a]+p['replacement']+raw[b:]
    assert sha(new)==p['stage3_chapter_sha256'], 'hash rozdziału III'
    return new

for name,expected_hash in [(v2['shared_module'],v2['shared_module_sha256']),*list(v3['new_modules'].items())]:
    p=ROOT/name
    if not p.is_file():errors.append('Brak modułu '+name)
    elif sha(p.read_text('utf8'))!=expected_hash:errors.append('Hash modułu '+name)

for doc in base['documents']:
    source=(ROOT/'zrodla'/doc['source']).read_bytes().decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
    if sha(source)!=doc['sha256_normalized_source']:errors.append('Zmienione źródło: '+doc['source'])
    before=source[:doc['prefix_length']];end=source[-doc['tail_length']:]
    body=source[doc['prefix_length']:-doc['tail_length']]
    lead=body[:doc['body_prefix_length']]
    cursor=doc['body_prefix_length'];originals=[]
    for chap in doc['chapters']:
        path=chap['path'];start=body[cursor:cursor+chap['length']];cursor+=chap['length']
        if sha(start)!=chap['sha256']:errors.append('Niezgodny bazowy hash: '+path)
        originals.append(start)
        try:
            stage=start
            if path in patch2:
                stage=apply_v2(stage,patch2[path]);count2+=1
            for p in patch3.get(path,[]):
                stage=apply_v3(stage,p);count3+=1
            actual=(ROOT/path).read_text('utf8')
            if stage!=actual:errors.append('Nieautoryzowane zmiany: '+path)
        except Exception as exc:errors.append(f'{path}: {exc}')
    if cursor!=len(body) or before+lead+''.join(originals)+end!=source:
        errors.append('Oryginał nieodtwarzalny: '+doc['source'])
    want=before+lead+('\n' if lead and not lead.endswith('\n') else '')
    want+=''.join('\\input{../'+ch['path']+'}\n' for ch in doc['chapters'])+end
    if (ROOT/doc['script']).read_text('utf8')!=want:
        errors.append('Zmieniony skrypt główny: '+doc['script'])
if count2!=2 or count3!=5 or len(patch3)!=3:
    errors.append(f'Liczby niezgodne: II={count2}, III={count3}, rozdziały III={len(patch3)}')
for filename,labels,guard in [
    ('wspolne/rozdmuchanie_punktu_normalna.tex',['st:ga6-exceptional-normal','lem:xvii-exceptional'],'biblioteka@rozdmuchanie@normalna@loaded'),
    ('wspolne/rozdmuchanie_punktu_kohomologia.tex',['tw:ga10-blowup','thm:xvii-blowup'],'biblioteka@rozdmuchanie@kohomologia@loaded')]:
    t=(ROOT/filename).read_text('utf8')
    if guard not in t or any(t.count('\\label{'+lab+'}')!=1 for lab in labels):
        errors.append('Moduł bez guardów lub etykiet: '+filename)
print(f'Źródła: {len(base["documents"])}; rozdziały: {sum(len(d["chapters"]) for d in base["documents"])}; zmiany II: {count2}; zmiany III: {count3} w {len(patch3)} rozdziałach')
if errors:
    print('BŁĘDY:',*errors,sep='\n- ');sys.exit(1)
print('OK: oryginały i nieruszone fragmenty zachowane, moduły i zmiany zgodne z manifestami.')
