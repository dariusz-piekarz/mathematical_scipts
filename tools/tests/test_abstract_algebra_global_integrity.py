#!/usr/bin/env python3
"""Global AA-01..AA-69 source audit, preserving verified AA-01..AA-42: chapters, labels, references, coverage.

The mathematical cross-audits remain distinct: this gate tests objective
source consistency rather than claiming to prove theorems.
"""
from pathlib import Path
from collections import Counter,defaultdict
import re

ROOT=Path(__file__).resolve().parents[2]
CHDIR=ROOT/"chapters/pl/abstract_algebra"
BOOK=ROOT/"books/pl/abstract_algebra.tex"
AUD=ROOT/"audits/abstract_algebra"

COVERAGE={
    "cross_01_aa41_aa42_q8_2026-11-23.md":(41,42),
    "cross_02_aa25_aa27_cyclic_field_theories_2026-11-23.md":(25,26,27),
    "cross_03_aa31_aa36_polynomials_galois_2026-11-23.md":tuple(range(31,37)),
    "cross_04_aa28_aa32_aa33_cyclotomic_resultants_2026-11-23.md":(28,32,33),
    "cross_05_aa16_aa18_modules_smith_tensor_2026-11-23.md":(16,17,18),
    "cross_06_aa09_12_13_14_ideals_localization_noether_artin_2026-11-23.md":(9,12,13,14),
    "cross_07_aa37_aa40_transcendence_normalization_dimension_integrality_2026-11-23.md":(37,38,39,40),
    "cross_08_aa19_aa24_fields_galois_trace_norm_radicals_2026-11-23.md":tuple(range(19,25)),
    "cross_09_aa01_aa08_group_series_semidirect_schreier_torsion_2026-11-23.md":tuple(range(1,9)),
    "cross_10_aa10_aa11_aa15_euclidean_gauss_noncommutative_2026-11-23.md":(10,11,15),
    "cross_11_aa29_aa30_finite_fields_constructibility_2026-11-23.md":(29,30),
}

INPUT=re.compile(r"\\input\s*\{([^}]+)\}")
CHAPTER=re.compile(r"\\chapter(?:\[[^\]]*\])?\s*\{")
LABEL=re.compile(r"\\label\s*\{([^}]+)\}")
REF=re.compile(r"\\(?:ref|eqref|autoref|cref|Cref|nameref|pageref)\s*\{([^}]+)\}")
ENV=re.compile(r"\\(begin|end)\s*\{([^}]+)\}")
COMMENT=re.compile(r"(?<!\\)%.*$",re.MULTILINE)

def text(src):
    return COMMENT.sub("",src.read_text(encoding="utf-8"))

def main():
    chapters=sorted(CHDIR.glob("[0-9][0-9]-*.tex"))
    assert len(chapters)==69,("wrong chapter number",len(chapters))
    ids=[int(p.name[:2]) for p in chapters]
    assert ids==list(range(1,70)),("numbering",ids)
    canonical={p.resolve() for p in chapters}
    book=text(BOOK)
    ins=[(BOOK.parent/p).resolve() for p in INPUT.findall(book)]
    assert len(ins)==69,("book input number",len(ins))
    assert len(set(ins))==69,("duplicate book input",ins)
    assert set(ins)==canonical,("book mismatched sources",
                                 [str(p) for p in canonical-set(ins)],
                                 [str(p) for p in set(ins)-canonical])
    assert ins==chapters,("chapter order",list(zip(ins,chapters)))
    owners=defaultdict(list)
    references=defaultdict(list)
    counter=Counter()
    for chapter in chapters:
        s=text(chapter)
        assert len(CHAPTER.findall(s))==1,("chapter heading",str(chapter))
        stack=[]
        for m in ENV.finditer(s):
            if m.group(1)=="begin":
                stack.append((m.group(2),m.start()))
            else:
                assert stack and stack[-1][0]==m.group(2),(
                    "unmatched TeX environment",chapter.name,m.group(2),stack[-1] if stack else None)
                stack.pop()
        assert not stack,("unterminated TeX environments",chapter.name,stack)
        for lab in LABEL.findall(s):
            assert lab.strip(),("empty label",chapter.name)
            owners[lab].append(chapter.name)
            counter["label_occurrences"]+=1
        for ref in REF.findall(s):
            for r in ref.split(","):
                r=r.strip()
                assert r,("empty reference",chapter.name)
                references[r].append(chapter.name)
                counter["reference_occurrences"]+=1
        counter["proofs"]+=len(re.findall(r"\\begin\s*\{proof\}",s))
        counter["examples"]+=len(re.findall(r"\\begin\s*\{przyklad\}",s))
        counter["theorems"]+=len(re.findall(r"\\begin\s*\{twierdzenie\}",s))
        counter["lemmas"]+=len(re.findall(r"\\begin\s*\{lemat\}",s))
        counter["corollaries"]+=len(re.findall(r"\\begin\s*\{wniosek\}",s))
    dup={l:s for l,s in owners.items() if len(s)!=1}
    assert not dup,("duplicate labels",dup)
    missing={r:s for r,s in references.items() if r not in owners}
    assert not missing,("unresolved references",missing)
    covered=defaultdict(list)
    for report, chapters_ in COVERAGE.items():
        file=AUD/report
        assert file.is_file() and file.stat().st_size>1000,("missing cross audit report",report)
        for num in chapters_:
            covered[num].append(report)
    assert set(covered)==set(range(1,43)),("cross-audit coverage",sorted(set(range(1,43))-set(covered)))
    # This checks existence/coverage, NOT the verdict or mathematical correctness
    # of individual reports. Each report carries its own CI and PDF evidence.
    assert len(COVERAGE)==11
    previous=AUD/"ch43_iteration_01.md"
    assert previous.is_file() and previous.stat().st_size>1000,("missing AA-43 first audit",previous)
    previous44=AUD/"ch44_iteration_01.md"
    assert previous44.is_file() and previous44.stat().st_size>1000,("missing AA-44 first audit",previous44)
    previous45=AUD/"ch45_iteration_01.md"
    assert previous45.is_file() and previous45.stat().st_size>1000,("missing AA-45 first audit",previous45)
    previous46=AUD/"ch46_iteration_01.md"
    assert previous46.is_file() and previous46.stat().st_size>1000,("missing AA-46 first audit",previous46)
    previous47=AUD/"ch47_iteration_01.md"
    assert previous47.is_file() and previous47.stat().st_size>1000,("missing AA-47 first audit",previous47)
    previous48=AUD/"ch48_iteration_01.md"
    assert previous48.is_file() and previous48.stat().st_size>1000,("missing AA-48 first audit",previous48)
    previous49=AUD/"ch49_iteration_01.md"
    assert previous49.is_file() and previous49.stat().st_size>1000,("missing AA-49 first audit",previous49)
    newest=AUD/"ch50_iteration_01.md"
    assert newest.is_file() and newest.stat().st_size>1000,("missing AA-50 first audit",newest)
    newest51=AUD/"ch51_iteration_01.md"
    assert newest51.is_file() and newest51.stat().st_size>1000,("missing AA-51 first audit",newest51)
    newest52=AUD/"ch52_iteration_01.md"
    assert newest52.is_file() and newest52.stat().st_size>1000,("missing AA-52 first audit",newest52)
    newest53=AUD/"ch53_iteration_01.md"
    assert newest53.is_file() and newest53.stat().st_size>1000,("missing AA-53 first audit",newest53)
    newest54=AUD/"ch54_iteration_01.md"
    assert newest54.is_file() and newest54.stat().st_size>1000,("missing AA-54 first audit",newest54)
    newest55=AUD/"ch55_iteration_01.md"
    assert newest55.is_file() and newest55.stat().st_size>1000,("missing AA-55 first audit",newest55)
    newest56=AUD/"ch56_iteration_01.md"
    assert newest56.is_file() and newest56.stat().st_size>1000,("missing AA-56 first audit",newest56)
    newest57=AUD/"ch57_iteration_01.md"
    assert newest57.is_file() and newest57.stat().st_size>1000,("missing AA-57 first audit",newest57)
    newest58=AUD/"ch58_iteration_01.md"
    assert newest58.is_file() and newest58.stat().st_size>1000,("missing AA-58 first audit",newest58)
    newest59=AUD/"ch59_iteration_01.md"
    assert newest59.is_file() and newest59.stat().st_size>1000,("missing AA-59 first audit",newest59)
    newest60=AUD/"ch60_iteration_01.md"
    assert newest60.is_file() and newest60.stat().st_size>1000,("missing AA-60 first audit",newest60)
    newest61=AUD/"ch61_iteration_01.md"
    assert newest61.is_file() and newest61.stat().st_size>1000,("missing AA-61 first audit",newest61)
    newest62=AUD/"ch62_iteration_01.md"
    assert newest62.is_file() and newest62.stat().st_size>1000,("missing AA-62 first audit",newest62)
    newest63=AUD/"ch63_iteration_01.md"
    assert newest63.is_file() and newest63.stat().st_size>1000,("missing AA-63 first audit",newest63)
    newest64=AUD/"ch64_iteration_01.md"
    assert newest64.is_file() and newest64.stat().st_size>1000,("missing AA-64 first audit",newest64)
    newest65=AUD/"ch65_iteration_01.md"
    assert newest65.is_file() and newest65.stat().st_size>1000,("missing AA-65 first audit",newest65)
    newest66=AUD/"ch66_iteration_01.md"
    assert newest66.is_file() and newest66.stat().st_size>1000,("missing AA-66 first audit",newest66)
    newest67=AUD/"ch67_iteration_01.md"
    assert newest67.is_file() and newest67.stat().st_size>1000,("missing AA-67 first audit",newest67)
    newest68=AUD/"ch68_iteration_01.md"
    assert newest68.is_file() and newest68.stat().st_size>1000,("missing AA-68 first audit",newest68)
    newest69=AUD/"ch69_iteration_01.md"
    assert newest69.is_file() and newest69.stat().st_size>1000,("missing AA-69 first audit",newest69)
    assert all(k not in covered for k in range(43,70)), "AA-43..69 retain separate audits from AA-01..AA-42"
    assert len(chapters)==len(covered)+27
    assert len(owners)>0 and len(references)>0
    counter.update({
        "chapters":len(chapters),
        "cross_reports":len(COVERAGE),
        "cross_covered_chapters":len(covered),
        "individually_audited_new_chapters":27,
        "unique_labels":len(owners),
        "unique_reference_targets":len(references),
        "unresolved_reference_targets":len(missing),
        "duplicate_label_targets":len(dup),
        "misordered_or_missing_chapters":0
    })
    print("AA GLOBAL 01-69 SOURCE INTEGRITY: PASS",dict(sorted(counter.items())))
    print("AA GLOBAL cross-audit chapter coverage:",{
        "all_chapters":len(covered),
        "overlap_chapters":{k:len(v) for k,v in covered.items() if len(v)>1},
        "uncovered_chapters":[]})

if __name__=="__main__":main()
