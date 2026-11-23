# Atlas L1.4.1 — pakiet do niezależnego odbioru

**Kandydat:** `94a7b4a1e592b1b0504b881f9c016004786ca6d9`  
**Obszar:** odczytowy raport powiązań rozdziału LaTeX z katalogiem Lean  
**Status techniczny:** 3/3 pełnych rund 2+1 PASS na wskazanym SHA  
**Status formalny:** `stabilizing` — niezależny uwierzytelniony odbiór **nieudzielony**  
**Zgłoszenie odbiorowe:** [Issue #10](https://github.com/dariusz-piekarz/mathematical_scipts/issues/10)

## 1. Przedmiot recenzji i granice

Recenzent ocenia **dokładny kandydat Git** `94a7b4a1e592b1b0504b881f9c016004786ca6d9`, a nie ruchomą
gałąź `biblioteka-matematyczna-iteracja-6` ani zbiorczy PR #7.
Funkcja `backend.lean_chapter_report.chapter_report` i endpoint
`GET /api/lean/chapter-report?module_id=LST-01` prezentują wyłącznie
powiązania deklarowane przez rejestr i indeks źródeł. Nie uruchamiają
Lean, nie sprawdzają historii kompilacji ani nie obliczają fingerprintu
zależności. `ready` nie oznacza `compiled`; `statement_approved`
nie jest certyfikatem zgodności semantycznej. Każda odpowiedź ma
`certificate=false`.

**Kod do przeczytania:** `application/backend/lean_chapter_report.py`,
`lean_catalog.py`, `lean_source_provenance.py`,
`lean_formalization.py`, `api.py`.
**Testy:** `application/tests/test_lean_catalog.py` i
`application/tests/test_lean_http.py`.
**Dane i workflow:** `application/lean/manifest.json`,
`application/lean/src/LST01_SyntaxValuations.lean`,
`chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex`,
`.github/workflows/atlas-stabilization.yml`,
`.github/workflows/lean-formalization.yml`.

Liczby **5 wpisów manifestu**, **18 twierdzeń kontrolowanych przez
zadanie kompilacyjne** i **20–30 planowanych formalizacji w pilotażu**
opisują **różne wielkości**; nie wolno automatycznie uznać ostatniego
celu za osiągnięty na podstawie logu kompilacji.

## 2. Reprodukcja na niezmiennym SHA

Poniższe polecenia są instrukcją dla recenzenta (nie zapisem
nowego wykonania przez autora raportu).

```bash
git fetch origin biblioteka-matematyczna-iteracja-6
git cat-file -t 94a7b4a1e592b1b0504b881f9c016004786ca6d9
git show 94a7b4a1e592b1b0504b881f9c016004786ca6d9:application/backend/lean_chapter_report.py
git show 94a7b4a1e592b1b0504b881f9c016004786ca6d9:application/tests/test_lean_catalog.py
git show 94a7b4a1e592b1b0504b881f9c016004786ca6d9:application/lean/manifest.json
gh run view 45181138327 -R dariusz-piekarz/mathematical_scipts --json status,conclusion,headSha
gh run download 45181138327 -R dariusz-piekarz/mathematical_scipts -n atlas-validation-status -D /tmp/atlas-l141
```

Recenzent powinien sprawdzić `candidate_sha` w pobranym pliku
`atlas_validation_status.json` oraz wyniki wszystkich wymaganych
zadań; nie opierać się jedynie na zielonym odznaczeniu przebiegu.
Dokumentacja i pozostałe audyty mogą mieć nowsze SHA bez zmiany
weryfikowanego kodu.

[Workflow końcowy #45181138327](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181138327)
oraz [artefakt statusu #14823870210](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181138327/artifacts/14823870210)
potwierdzają: `passes[1..3].passed=true`,
`problems=[]`, `status=stabilizing`,
`skeptical_review=pending`, `certificate=false`.
Skrót archiwum artefaktu podany przez GitHub:
`sha256:2085cc3d62eb6c957b9e9af336e66fd561d137a3a7ee94469a0d484ff20e2bce`.

W każdej rundzie: 735 wyników testów Python, 10 sklasyfikowanych
pominięć, `unreviewed_skips=0`, Chromium 509 rozdziałów i bez błędów
JavaScript, natywne zadania Windows/Linux PASS. Rzeczywisty Lean
4.26.0 i przypięty Mathlib
`2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`:
4 pliki, 18 twierdzeń, `axiom_check=passed` i
`semantic_certificate=false` w każdej rundzie.

## 3. Macierz sceptycznej kontroli

| Próba negatywna | Oczekiwana odpowiedź |
| --- | --- |
| Brak lub uszkodzenie rekordu rozdziału, niezgodność `documents.sha256` | Odmowa albo `stale`, bez `approved` |
| Cofnięcie `statement_status=approved` pomiędzy odczytami | `changed_manifest_during_report`, `stale/needs_review` |
| Dodanie lub usunięcie wpisu rejestru dla rozdziału | Brak cichego zachowania `ready`; `changed_manifest_during_report` |
| Podmiana `source_document_path` na równoważny bajtowo plik | `changed_manifest_during_report`, `stale/needs_review` |
| Zmiana tytułu lub zakresu tej samej encji w SQLite | `changed_index_binding`, `stale/needs_review` |
| Usunięcie albo przesunięcie właściciela etykiety | `changed_index_binding` lub niepoprawne powiązanie; bez `ready` |
| Zmiana TeX po odczycie katalogu | `unverifiable_canonical_source`, `stale` |
| Zmiana indeksowanego tekstu przy zachowaniu wewnętrznie poprawnego SHA | `changed_during_report`, `stale` |
| Domieszka `proof_status=compiled` i `certificate=true` z katalogu | Pola niedopuszczone do raportu; `certificate=false` |

**Ograniczenie krytyczne do rozważenia:** kontrole wykonywane w
sekwencji nie tworzą atomowej migawki danych obejmującej system plików,
manifest i SQLite. Podmiana po ostatniej kontroli lub wielokrotna
podmiana z powrotem może pozostać niezaobserwowana. Recenzent musi
osobno ocenić, czy takie ryzyko jest akceptowalne **wyłącznie w
odczytowym, diagnostycznym API lokalnym**. Jeżeli nie, zgłosić
`request changes` z odtwarzalnym kontrprzykładem; zmiana kodu
wymaga nowego 2+1.

## 4. Warunki decyzji i rozdział odpowiedzialności

Recenzent musi być **niezależny od autora ocenianych zmian**, a jego
tożsamość i decyzja muszą być uwierzytelnione przez uprawniony
mechanizm GitHub/organizacji. Informacja w issue, niesygnowany JSON,
deklaracja `independent=true` oraz własna opinia asystenta nie
stanowią takiej aprobaty.

Decyzja powinna wskazywać:

1. pełne SHA kandydata oraz sprawdzone źródła i wyniki CI;
2. wynik `approve` albo `request changes`, z uzasadnieniem;
3. ocenę zagrożeń TOCTOU, wyjątków, konfliktów etykiet i odcięcia
   `proof_status` od diagnostyki źródła;
4. potwierdzenie, że **nie** wystawiono certyfikatu równoważności
   matematycznej Lean–LaTeX.

Dopiero po pozytywnym wyniku CI i osobnej, uwierzytelnionej aprobacie
można ręcznie rozważyć `L1.4.1=stable` i w **następnej iteracji**
przejść do L1.4.2. Aktualnie pozostawić `stabilizing`;
`certificate=false`.
