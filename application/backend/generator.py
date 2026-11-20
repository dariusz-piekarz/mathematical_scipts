"""Reproducible, read-only TeX project generator from the indexed library.

The canonical library is immutable; generated projects contain *copies* of the
selected sources.  Extra references use xr-hyper with *prefixed* external labels
so even selections of portions from the same chapter do not shadow labels.
No subprocesses are run by the HTTP API; build scripts are for the user locally.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import hashlib
import io
import json
from pathlib import Path
import re
import sqlite3
import zipfile
from typing import Any

REF_RE = re.compile(r'\\(ref|eqref|pageref|autoref|nameref|cref|Cref|vref|Vref)\s*\{([^{}]+)\}')
LABEL_RE = re.compile(r'\\label\s*\{([^{}]+)\}')
MODULE_ID = re.compile(r'^[A-Za-z][A-Za-z0-9]*-[0-9]{2}$')
MAX_PROJECT_MODULES = 75
MAX_EXTERNAL_MODULES = 75
MAX_ARCHIVE_FILES = 512
MAX_ARCHIVE_UNCOMPRESSED_BYTES = 64 * 1024 * 1024


class GenerationError(ValueError):
    pass


@dataclass(frozen=True)
class Fragment:
    start: int
    end: int
    entity_id: str


def tex_text(value: str) -> str:
    """Escape user-visible title, not raw content of the library."""
    specials = {'\\':r'\textbackslash{}', '{':r'\{','}':r'\}', '$':r'\$',
                '&':r'\&', '#':r'\#', '%':r'\%', '_':r'\_',
                '^':r'\textasciicircum{}', '~':r'\textasciitilde{}'}
    return ''.join(specials.get(c,c) for c in value.replace('\n',' '))


def deduplicate_fragments(ranges: list[Fragment]) -> list[Fragment]:
    """Reject partly overlapping ranges; suppress ranges wholly covered by others."""
    ranges=sorted(ranges,key=lambda x:(x.start,-x.end,x.entity_id))
    kept: list[Fragment]=[]
    for frag in ranges:
        if frag.end<=frag.start: continue
        if kept and frag.start < kept[-1].end:
            if frag.end<=kept[-1].end: continue
            raise GenerationError('Częściowo zachodzące na siebie fragmenty wymagają wyboru całego nadrzędnego obiektu.')
        kept.append(frag)
    return kept


def selected_modules_and_fragments(con: sqlite3.Connection, modules: list[str], entities: list[str]):
    selected=list(dict.fromkeys(modules))
    if len(selected)>MAX_PROJECT_MODULES: raise GenerationError('Zbyt wiele modułów.')
    known={r['id']:dict(r) for r in con.execute('SELECT id,path,title,domain,content,sha256 FROM documents')}
    for m in selected:
        if not MODULE_ID.fullmatch(m) or m not in known: raise GenerationError(f'Nieznany moduł: {m}')
    fragment_rows: dict[str,list[Fragment]]=defaultdict(list)
    for eid in dict.fromkeys(entities):
        row=con.execute('SELECT id,document_id,start_offset,end_offset FROM entities WHERE id=?',(eid,)).fetchone()
        if not row: raise GenerationError(f'Nieznany obiekt: {eid}')
        doc=row['document_id']
        if doc not in selected: fragment_rows[doc].append(Fragment(row['start_offset'],row['end_offset'],eid))
    if len(selected)+len(fragment_rows)>MAX_PROJECT_MODULES: raise GenerationError('Zbyt wiele modułów.')
    # Keep first occurrence order: whole documents, then excerpt-only documents.
    order=selected+[m for m in fragment_rows if m not in selected]
    out={}
    for m in order:
        row=known[m]
        if m in selected:
            content=row['content']; frag_ids=[]; spans=[(0,len(content))]
        else:
            fs=deduplicate_fragments(fragment_rows[m]);spans=[(f.start,f.end) for f in fs]
            content='\n\n'.join(row['content'][a:b] for a,b in spans)
            frag_ids=[f.entity_id for f in fs]
        out[m]={'row':row,'content':content,'fragments':frag_ids,'spans':spans, 'whole':m in selected}
    if not out: raise GenerationError('Wybierz przynajmniej jeden moduł lub obiekt.')
    return out,known


def closure(con:sqlite3.Connection, chosen:dict[str,Any], known:dict[str,Any], depth:int):
    """Optional transitive closure of external module references (bounded)."""
    frontier=set(chosen)
    for _ in range(depth):
        if not frontier: break
        marks=','.join('?' for _ in frontier)
        rows=con.execute(f'SELECT DISTINCT target_document FROM references_tex WHERE source_document IN ({marks}) AND target_document IS NOT NULL',tuple(sorted(frontier)))
        new={r[0] for r in rows if r[0] not in chosen}
        if len(chosen)+len(new)>MAX_PROJECT_MODULES: raise GenerationError('Domknięcie zależności przekracza limit 75 modułów.')
        for m in sorted(new):
            row=known[m]; chosen[m]={'row':row,'content':row['content'],'fragments':[],'spans':[(0,len(row['content']))],'whole':True}
        frontier=new



# Conservative syntactic inventory: it does not attempt to expand arbitrary TeX.
PACKAGE_DECL = re.compile(r'\\(?:usepackage|RequirePackage)(?:\[([^]]*)\])?\{([^{}]+)\}')
COMMAND_DECL = re.compile(r'\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator\*?|def)\s*(?:\{\s*(\\[A-Za-z@]+)\s*\}|(\\[A-Za-z@]+))')
ENV_DECL = re.compile(r'\\(?:newenvironment|renewenvironment|NewDocumentEnvironment)\s*\{([^{}]+)\}')

def preamble_compatibility(templates:dict[str,str], chosen:list[str]) -> dict[str,Any]:
    """Flag conflicts rather than silently concatenate incompatible preambles."""
    groups={}
    for module in chosen:
        prefix=module.split('-')[0]
        groups.setdefault(prefix,templates[module])
    if len(groups)==1:
        return {'status':'single_template','groups':sorted(groups),'conflicts':[],
                'not_merged':False,'warning':None}
    packages={}; commands={}; environments={}
    for group,source in groups.items():
        for options,names in PACKAGE_DECL.findall(source):
            for name in names.split(','):
                name=name.strip()
                if name:packages.setdefault(name,{}).setdefault(options.strip(),[]).append(group)
        for a,b in COMMAND_DECL.findall(source):
            commands.setdefault(a or b,set()).add(group)
        for name in ENV_DECL.findall(source):
            environments.setdefault(name,set()).add(group)
    conflicts=[]
    for name,options in sorted(packages.items()):
        if len(options)>1:
            conflicts.append({'type':'package_options','name':name,'variants':
                              [{'options':o,'groups':sorted(g)} for o,g in sorted(options.items())]})
    for kind,items in [('command_definition',commands),('environment_definition',environments)]:
        for name,owners in sorted(items.items()):
            if len(owners)>1:
                conflicts.append({'type':kind,'name':name,'groups':sorted(owners)})
    return {'status':'requires_review','groups':sorted(groups),'conflicts':conflicts,
            'not_merged':True,
            'warning':'Użyto tylko preambuły pierwszego modułu. Pozostałe preambuły nie zostały scalone; sprawdź makra i pakiety przed kompilacją.'}



# Conservative cross-template macro usage analysis. This is not TeX expansion.
MACRO_USE_RE = re.compile(r'(?<!\\)\\([A-Za-z@]+)')
VERBATIM_ENVS = ('verbatim', 'verbatim*', 'lstlisting', 'minted', 'Verbatim', 'comment')
VERBATIM_BLOCK_RE = re.compile(r'\\begin\{(' + '|'.join(re.escape(x) for x in VERBATIM_ENVS) + r')\}(?:\[[^\]]*\])?.*?\\end\{\1\}', re.S)
INLINE_VERB_RE = re.compile(r'\\(?:verb\*?|lstinline(?:\[[^\]]*\])?)')

def scan_tex_code(source: str) -> str:
    """Mask comments and common literal regions without shifting offsets.

    Conservative lexical filter; catcode changes and arbitrary custom verbatim
    environments cannot be decided without a TeX engine.
    """
    chars=list(source)
    for match in VERBATIM_BLOCK_RE.finditer(source):
        for i in range(match.start(),match.end()):
            if chars[i]!='\n': chars[i]=' '
    i=0
    while i<len(chars):
        if chars[i]==' ' or chars[i]=='\n':
            i+=1;continue
        match=INLINE_VERB_RE.match(source,i)
        if match and all(chars[k]!=' ' for k in range(i,match.end())):
            pos=match.end()
            if pos<len(chars) and source[pos] not in '\r\n':
                delimiter=source[pos]; end=source.find(delimiter,pos+1)
                if end>=0 and '\n' not in source[pos:end]:
                    for k in range(i,end+1):chars[k]=' '
                    i=end+1;continue
        if source[i]=='%' and chars[i]=='%':
            backslashes=0;j=i-1
            while j>=0 and source[j]=='\\':backslashes+=1;j-=1
            if backslashes%2==0:
                end=source.find('\n',i)
                if end<0:end=len(source)
                for k in range(i,end):chars[k]=' '
                i=end;continue
        i+=1
    return ''.join(chars)

def macro_usage_audit(templates:dict[str,str], chosen:list[str], contents:dict[str,str]) -> dict[str,Any]:
    """Report cross-template candidates after masking common literal text.

    Source-local declarations are excluded, but declarations in nested groups
    may be scoped; this is not proof of availability at each use site.
    """
    primary=chosen[0]
    def declarations(source:str)->set[str]:
        return {((a or b).lstrip('\\')) for a,b in COMMAND_DECL.findall(scan_tex_code(source))}
    primary_defs=declarations(templates[primary])
    all_defs={m:declarations(templates[m]) for m in chosen}
    candidates=[]
    local_counts={}
    for module in chosen:
        cleaned=scan_tex_code(contents[module])
        local_defs=declarations(cleaned)
        local_counts[module]=len(local_defs)
        uses=set(MACRO_USE_RE.findall(cleaned))
        for macro in sorted(uses-primary_defs-local_defs):
            providers=sorted({m for m,defs in all_defs.items() if macro in defs and m!=primary})
            if providers:
                candidates.append({'module':module,'macro':'\\'+macro,'providers':providers,
                                   'classification':'requires_review'})
    return {'primary_template':primary,'candidate_count':len(candidates),
            'candidates':candidates,'source_local_definition_counts':local_counts,
            'limitations':'Analiza leksykalna: pomija komentarze i typowe bloki dosłowne, ale nie rozwija makr, nie modeluje zasięgu grup, catcode, pakietów ani warunkowego TeX.'}


# Theorem registry: a declaration is transferable only if its counter and
# displayed name are unambiguous. No automatic renaming or counter changes.
THEOREM_DECL = re.compile(r'\\newtheorem\*?\s*\{([^{}]+)\}(?:\[([^]]+)\])?\s*\{([^{}]+)\}(?:\[([^]]+)\])?')
THEOREM_STYLE = re.compile(r'\\theoremstyle\s*\{([^{}]+)\}')
BEGIN_ENV = re.compile(r'\\begin\s*\{([^{}]+)\}')

def theorem_registry(source:str)->dict[str,dict[str,str]]:
    clean=scan_tex_code(source)
    result={}
    for m in THEOREM_DECL.finditer(clean):
        preceding=list(THEOREM_STYLE.finditer(clean,0,m.start()))
        style=preceding[-1].group(1) if preceding else 'plain'
        name,shared,caption,within=m.groups()
        result[name]={'declaration':m.group(0),'shared':shared or '',
                      'within':within or '', 'caption':caption,'style':style}
    return result

def theorem_declaration_occurrences(source: str) -> list[dict[str, Any]]:
    """Retain every declaration, including duplicates lost by dict registries.

    Brace depth is a conservative lexical signal, not TeX scope evaluation.
    """
    clean = scan_tex_code(source)
    occurrences = []
    for match in THEOREM_DECL.finditer(clean):
        prefix = clean[:match.start()]
        depth = 0
        for ch in prefix:
            if ch == '{': depth += 1
            elif ch == '}': depth = max(0, depth - 1)
        occurrences.append({'environment': match.group(1),
                            'declaration': match.group(0),
                            'offset': match.start(), 'brace_depth': depth,
                            'line': clean.count('\n', 0, match.start()) + 1})
    return occurrences


def theorem_environment_audit(templates:dict[str,str], chosen:list[str], contents:dict[str,str]):
    """Conservative audit of theorem environments in preambles AND selected bodies.

    Body-local declarations are never silently moved to the preamble: scope,
    counter order and repeated declarations must be checked by a TeX engine.
    """
    primary=chosen[0]
    registries={m:theorem_registry(templates[m]) for m in chosen}
    primary_registry=registries[primary]
    body_registries={m:theorem_registry(contents.get(m, "")) for m in chosen}
    requested=set()
    for content in contents.values():
        requested.update(BEGIN_ENV.findall(scan_tex_code(content)))
    additions=[];conflicts=[];unresolved=[];local_declarations=[]
    # A dict-based registry silently overwrites repeated declarations. Keep
    # their occurrences, since even identical \newtheorem calls can fail TeX.
    for module in chosen:
        for origin,source in (('preamble', templates[module]), ('body', contents.get(module, ''))):
            occurrences=theorem_declaration_occurrences(source)
            by_name=defaultdict(list)
            for item in occurrences:
                by_name[item['environment']].append(item)
                if origin == 'body' and item['brace_depth']:
                    unresolved.append({'environment':item['environment'], 'module':module,
                                       'reason':'declaration_inside_brace_group',
                                       'line':item['line'], 'brace_depth':item['brace_depth']})
            for name,items in by_name.items():
                if len(items)>1:
                    unresolved.append({'environment':name,'module':module,
                                       'reason':'repeated_declaration_within_source',
                                       'origin':origin,'lines':[item['line'] for item in items]})
    for module,reg in body_registries.items():
        for name,decl in reg.items():
            local_declarations.append({'module':module,'environment':name,'declaration':decl['declaration']})
            providers=[(m,r[name]) for m,r in registries.items() if name in r]
            providers += [(m,r[name]) for m,r in body_registries.items() if name in r]
            signatures={(r['caption'],r['shared'],r['within'],r['style']) for _,r in providers}
            if len(signatures)>1:
                conflicts.append({'environment':name,'providers':sorted(set(m for m,_ in providers)),
                                  'reason':'body_preamble_definition_mismatch'})
            elif len(providers)>1:
                unresolved.append({'environment':name,'reason':'repeated_declaration_across_sources',
                                   'providers':[m for m,_ in providers]})
    for name in sorted(requested):
        if name in primary_registry: continue
        if any(name in reg for reg in body_registries.values()):
            # Never import a duplicate preamble declaration if a body defines it.
            continue
        providers=[(m,reg[name]) for m,reg in registries.items() if name in reg]
        if not providers:continue
        signatures={(r['caption'],r['shared'],r['within'],r['style']) for _,r in providers}
        if len(signatures)>1:
            conflicts.append({'environment':name,'providers':[m for m,_ in providers], 'reason':'different_definitions'})
            continue
        declaration=providers[0][1]
        if declaration['shared'] and declaration['shared'] not in primary_registry:
            unresolved.append({'environment':name,'reason':'missing_shared_counter', 'counter':declaration['shared']})
            continue
        if declaration['within'] and declaration['within'] not in ('chapter','section','subsection') and declaration['within'] not in primary_registry:
            unresolved.append({'environment':name,'reason':'unknown_parent_counter','counter':declaration['within']})
            continue
        additions.append({'environment':name,'declaration':declaration['declaration'], 'style':declaration['style'], 'providers':[m for m,_ in providers]})
    return {'primary':primary,'additions':additions,'conflicts':conflicts,'unresolved':unresolved,
            'body_declarations':local_declarations,
            'limitations':'Lexical scan only: nested scopes, catcodes, conditional declarations and custom factories are not evaluated.'}


def project_files(con:sqlite3.Connection, modules:list[str], entities:list[str], title:str,
                  closure_depth:int=0) -> tuple[dict[str,bytes],dict[str,Any]]:
    if closure_depth not in (0,1,2,3): raise GenerationError('closure_depth musi należeć do {0,1,2,3}.')
    if not title.strip() or len(title)>160: raise GenerationError('Tytuł musi mieć od 1 do 160 znaków.')
    parts,known=selected_modules_and_fragments(con,modules,entities)
    if closure_depth: closure(con,parts,known,closure_depth)
    output_labels={}
    for m,p in parts.items():
        # Capture labels only in the included TeX spans. Other labels in same document are external.
        for a,b in p['spans']:
            for label in con.execute('SELECT name,offset FROM labels WHERE document_id=? AND offset>=? AND offset<?',(m,a,b)):
                output_labels[label['name']]=m
    references=[]
    external:dict[str,set[str]]=defaultdict(set)
    globally_missing=[]
    for m,p in parts.items():
        for a,b in p['spans']:
            for row in con.execute('SELECT target_label,target_document,status,offset,line FROM references_tex WHERE source_document=? AND offset>=? AND offset<?',(m,a,b)):
                label=row['target_label']; target=row['target_document']
                if label in output_labels:
                    status='internal'
                elif target is not None:
                    status='external';external[target].add(label)
                else:
                    status='missing';globally_missing.append({'module':m,'label':label,'line':row['line']})
                references.append({'source':m,'target_label':label,'target_module':target,'status':status})
    if globally_missing:
        raise GenerationError('Nierozwiązane etykiety: '+', '.join(x['label'] for x in globally_missing[:10]))
    if len(external)>MAX_EXTERNAL_MODULES: raise GenerationError('Zbyt wiele referencji zewnętrznych.')
    labels_to_rewrite={lab:(f'ext-{module}-'+lab) for module,labs in external.items() for lab in labs}
    # External labels are prefixed in xr-hyper, avoiding same-module collisions in fragment mode.
    def rewrite_tex_refs(content:str)->str:
        def sub(m:re.Match)->str:
            parts=m.group(2).split(',')
            normalized=[x.strip() for x in parts]
            return '\\'+m.group(1)+'{'+','.join(labels_to_rewrite.get(x,x) for x in normalized)+'}'
        return REF_RE.sub(sub,content)
    files:dict[str,bytes]={}
    ordered=list(parts)
    for m,p in parts.items():
        if p['whole']:
            body=p['content']
        else:
            body=(f'\\chapter*{{{tex_text(p["row"]["title"])}}}\n'
                  f'\\addcontentsline{{toc}}{{chapter}}{{{tex_text(p["row"]["title"])}}}\n'
                  f'% Fragmenty obiektów: {", ".join(p["fragments"])}\n\n'+p['content'])
        files[f'rozdzialy/{m}.tex']=rewrite_tex_refs(body).encode('utf-8')
    # Source preambles saved as templates from the original manuscripts.
    prefix_to_source={'ALG':'ALG','AT':'ALG','TOP':'TOP','GW':'GW','GA':'GA','KAT':'KAT','MOD':'MOD','CAL':'CAL','BT':'BT',
                      'P1':'P1','P2':'P2','P3':'P3','P4':'P4'}
    template_root=Path(__file__).resolve().parents[1]/'config'/'preambles'
    templates={}
    for m in set(ordered)|set(external):
        key=prefix_to_source.get(m.split('-')[0]); t=template_root/f'{key}.tex'
        if not key or not t.is_file():raise GenerationError(f'Brakuje preambuły dla {m}.')
        templates[m]=t.read_text('utf-8')
    compatibility=preamble_compatibility(templates,ordered)
    macro_audit=macro_usage_audit(templates,ordered,{m:parts[m]["content"] for m in ordered})
    theorem_audit=theorem_environment_audit(templates,ordered,{m:parts[m]["content"] for m in ordered})
    main_template=templates[ordered[0]]
    def prepare_header(template:str)->str:
        if r'\begin{document}' in template: template=template.split(r'\begin{document}')[0]
        # Source-book externaldocuments are not part of this generated project.
        # Only explicit, validated ext-MODULE- imports are inserted below.
        template=re.sub(r'(?m)^\s*\\externaldocument(?:\[[^]\n]*\])?\{[^}\n]+\}(?:\[[^]\n]*\])?[^\n]*$', '', template)
        template=re.sub(r'\\documentclass(?:\[[^\]]*\])?\{[^}]+\}',r'\\documentclass[11pt,a4paper,openany]{report}',template,count=1)
        # Some preambles contain hyperref already; insert xr-hyper before it.
        if r'\usepackage{xr-hyper}' not in template:
            m=re.search(r'\\usepackage(?:\[[^\]]*\])?\{hyperref\}',template)
            if m:template=template[:m.start()]+r'\usepackage{xr-hyper}'+'\n'+template[m.start():]
            else:template+='\n'+r'\usepackage{xr-hyper}'+'\n'+r'\usepackage[unicode]{hyperref}'+'\n'
        # Array column modifiers (>{...}p{...}) require array.sty, even when
        # the originating preamble omitted the explicit package.
        for package in ("array", "booktabs"):
            if not re.search(r"\\usepackage(?:\[[^\]]*\])?\{[^}]*\b" + package + r"\b[^}]*\}", template):
                template += "\n\\usepackage{" + package + "}\n"
        return template
    head=prepare_header(main_template)
    for addition in theorem_audit["additions"]:
        head += "\n\\theoremstyle{"+addition["style"]+"}\n"+addition["declaration"]+"\n"
    imports='\n'.join(f'\\externaldocument[ext-{m}-]{{aux/{m}}}' for m in sorted(external))
    body='\n'.join(f'\\input{{rozdzialy/{m}.tex}}' for m in ordered)
    main=(head+'\n'+imports+'\n'+r'\title{'+tex_text(title)+'}\n'+r'\author{}'+'\n'+r'\date{}'+'\n'
          +r'\begin{document}'+'\n'+r'\maketitle'+'\n'+r'\tableofcontents'+'\n'+r'\clearpage'+'\n'+body+'\n'+r'\end{document}'+'\n')
    files['main.tex']=main.encode('utf-8')
    # Generate self-standing reference sources; compilation produces aux/*.aux.
    for m in sorted(external):
        source=known[m]['content']
        ref=prepare_header(templates[m])+ '\n'+r'\begin{document}'+'\n'+source+'\n'+r'\end{document}'+'\n'
        files[f'aux/{m}.tex']=ref.encode('utf-8')
    scripts='''# Run this inside the generated project directory, with pdflatex installed.
$ErrorActionPreference = "Stop"
$refs = @(@REFS@)
foreach ($ref in $refs) {
    & pdflatex -interaction=nonstopmode -halt-on-error -output-directory=aux ("aux/" + $ref + ".tex")
    if ($LASTEXITCODE -ne 0) { throw "Compiling reference $ref failed" }
}
& pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { throw "Compiling main.tex failed" }
& pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { throw "Compiling main.tex (pass 2) failed" }
'''.replace('@REFS@',','.join('"'+m+'"' for m in sorted(external)))
    files['build.ps1']=scripts.encode('utf-8')
    sh='''#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
@REF_COMMANDS@
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
'''.replace('@REF_COMMANDS@','\n'.join(f'pdflatex -interaction=nonstopmode -halt-on-error -output-directory=aux aux/{m}.tex' for m in sorted(external)))
    files['build.sh']=sh.encode('utf-8')
    manifest={'format_version':1,'title':title,'modules':ordered,
              'whole_modules':[m for m,p in parts.items() if p['whole']],
              'fragments':{m:p['fragments'] for m,p in parts.items() if p['fragments']},
              'references_total':len(references),
              'references_internal':sum(x['status']=='internal' for x in references),
              'references_external':sum(x['status']=='external' for x in references),
              'external_targets':{m:sorted(v) for m,v in sorted(external.items())},
              'source_sha256':{m:p['row']['sha256'] for m,p in parts.items()},
              'closure_depth':closure_depth,
              'preamble':ordered[0].split('-')[0],
              'preamble_warning':compatibility['warning'],
              'preamble_compatibility':compatibility,
              'macro_usage_audit':macro_audit,
              'theorem_environment_audit':theorem_audit,
              'compilation_performed':False,
              'build_instructions':'Uruchom ./build.ps1 lub bash build.sh; referencyjne aux/*.aux muszą powstać przed main.tex.'}
    files['theorem_environment_audit.json']=(json.dumps(theorem_audit,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    files['macro_usage_audit.json']=(json.dumps(macro_audit,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    files['preamble_audit.json']=(json.dumps(compatibility,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    files['manifest.json']=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    files['README.md']=('''# Wygenerowany skrypt LaTeX

Źródłem były kanoniczne moduły z Biblioteki matematycznej. Pliki w `rozdzialy/` są kopiami i nie zmieniają oryginałów.

`main.tex` dołącza wybrane moduły, a `aux/*.tex` jest przeznaczony do utworzenia plików pomocniczych dla nieobecnych rozdziałów za pomocą `xr-hyper`.

**Budowanie:** `./build.ps1` (Windows / PowerShell) albo `bash build.sh` (Linux/macOS). Wymaga TeX Live lub MiKTeX z `pdflatex` i `xr-hyper`. Skrypt musi najpierw zbudować dokumenty referencyjne.

Uwaga: poprawność odsyłaczy sprawdza baza, natomiast kompilowalność dowolnej kombinacji preambuł i makr wymaga osobnego audytu; w szczególności łączenie skryptów z różnych dziedzin może wymagać ujednolicenia preambuł. Fragmenty mogą wymagać dodatkowego kontekstu matematycznego mimo rozwiązanych odsyłaczy.
''').encode('utf-8')
    return files,manifest


def zip_project(files:dict[str,bytes]) -> bytes:
    # Validate and budget the entire archive before writing any bytes.
    if len(files) > MAX_ARCHIVE_FILES:
        raise GenerationError('Zbyt wiele plików w archiwum.')
    total = 0
    for name, data in files.items():
        if not isinstance(data, bytes):
            raise GenerationError('Zawartość archiwum musi być typu bytes.')
        total += len(data)
        if total > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
            raise GenerationError('Przekroczono limit rozmiaru archiwum.')
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as archive:
        for name,data in sorted(files.items()):
            # ZIP names always use POSIX separators, including on Windows.
            # Reject ambiguous or platform-specific paths before serialization.
            if (not isinstance(name, str) or not name or "\\" in name
                    or name.startswith("/") or "\x00" in name
                    or any(part in ("", ".", "..") for part in name.split("/"))
                    or ":" in name.split("/")[0]):
                raise GenerationError('Niebezpieczna ścieżka w archiwum.')
            if not isinstance(data, bytes):
                raise GenerationError('Zawartość archiwum musi być typu bytes.')
            archive.writestr(name,data)
    return buf.getvalue()


def main(argv:list[str]|None=None)->int:
    import argparse
    parser=argparse.ArgumentParser(description='Generator modułowych skryptów Biblioteki matematycznej')
    parser.add_argument('--db',default='data/biblioteka.db')
    parser.add_argument('--modules',nargs='*',default=[],help='Identyfikatory modułów, np. ALG-09')
    parser.add_argument('--entities',nargs='*',default=[],help='Identyfikatory obiektów, np. ALG-09/proof/0004')
    parser.add_argument('--title',default='Mój skrypt matematyczny')
    parser.add_argument('--closure-depth',type=int,default=0,choices=range(4))
    parser.add_argument('--output',default='skrypt_matematyczny.zip')
    args=parser.parse_args(argv)
    con=sqlite3.connect(Path(args.db));con.row_factory=sqlite3.Row
    try:files,manifest=project_files(con,args.modules,args.entities,args.title,args.closure_depth)
    finally:con.close()
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(zip_project(files))
    print(json.dumps({'output':str(out),'modules':manifest['modules'],'references_external':manifest['references_external']},ensure_ascii=False))
    return 0


if __name__=='__main__':
    raise SystemExit(main())