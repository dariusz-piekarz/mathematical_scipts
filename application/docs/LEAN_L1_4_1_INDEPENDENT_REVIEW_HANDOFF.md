# Atlas L1.4.1 — pakiet do niezależnego odbioru po naprawie #12

**Aktualny kandydat kodu:** `ca6165bcd0f59aa6fb836e1922b51aeba51be193`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (ruchomy HEAD; **nie** jest przedmiotem odbioru)  
**Zakres:** odczytowy raport rozdziałowy powiązań kanonicznego LaTeX-u z rejestrem Lean  
**Stan techniczny (23.11.2026, ok. 19:58 UTC):** dwie pełne rundy 2+1 zakończone PASS; trzecia w toku. Sprawdzić końcowy stan workflow, nie ekstrapolować.  
**Stan formalny:** `stabilizing` najwyżej po 3/3, niezależna uwierzytelniona recenzja nadal **oczekiwana**. `certificate=false`.  
**Odbiór:** [issue #10](https://github.com/dariusz-piekarz/mathematical_scipts/issues/10); [naprawiona usterka #12](https://github.com/dariusz-piekarz/mathematical_scipts/issues/12).  
**Właściwa stabilizacja:** [Atlas 2+1 #45252666627](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45252666627), wywołana kontrolnym commitem `fdc102952a99fb726a31f9b717afdb82c9af134c` z `candidate_sha=ca6165bc...` oraz `fragment=L1.4`.

## 1. Co dokładnie podlega recenzji

Funkcja `backend.lean_chapter_report.chapter_report` i endpoint `GET /api/lean/chapter-report?module_id=LST-01` raportują źródłowe powiązania; nie wykonują Lean, nie odczytują historii kompilacji, nie certyfikują zgodności twierdzeń z LaTeX-em. Flagi `run_history_checked=false`, `dependency_fingerprint_checked=false`, `proof_status_included=false` oraz `certificate=false` są celowe. `ready` nie oznacza `compiled`; `statement_approved` nie oznacza formalnego certyfikatu semantycznego.

Bieżący rejestr obejmuje **9 mapowań**: LST-01 — 5, LST-02 — 4 z `statement_status=needs_review`, LA-01 — 0. Liczba **26 deklaracji Lean w 5 plikach** w historycznym, faktycznym CI LST-02 jest inną jednostką niż liczba mapowań; nie dowodzi zakończenia pilotażu 20–30. Zewnętrzna ocena czterech nowych mapowań LST-02 należy osobno do [issue #11](https://github.com/dariusz-piekarz/mathematical_scipts/issues/11).

Główne źródła kodu na wskazanym SHA:
- `application/backend/lean_chapter_report.py`, `lean_catalog.py`, `lean_source_provenance.py`, `lean_formalization.py` i `api.py`;
- `application/tests/test_lean_catalog.py` (w szczególności `test_l14_draft_tex_changed_after_catalog_downgrades_draft` i `test_l14_draft_with_unchanged_canonical_tex_stays_draft`), `test_lean_http.py`;
- `application/lean/manifest.json`, rozdziały `chapters/pl/logic_and_set_theory/`, `.github/workflows/atlas-stabilization.yml` i `.github/workflows/lean-formalization.yml`.

## 2. Reprodukcja: właściwy SHA, właściwy workflow

```bash
git fetch origin biblioteka-matematyczna-iteracja-6
git cat-file -t ca6165bcd0f59aa6fb836e1922b51aeba51be193
git show ca6165bcd0f59aa6fb836e1922b51aeba51be193:application/backend/lean_chapter_report.py
git show ca6165bcd0f59aa6fb836e1922b51aeba51be193:application/tests/test_lean_catalog.py
git show ca6165bcd0f59aa6fb836e1922b51aeba51be193:application/lean/manifest.json
gh run view 45252666627 -R dariusz-piekarz/mathematical_scipts --json status,conclusion,headSha
gh run download 45252666627 -R dariusz-piekarz/mathematical_scipts -n atlas-validation-status -D /tmp/atlas-l141
```

**Ważne:** `headSha` workflow wskazuje commit **kontrolny** `fdc10295...`, a nie oceniany SHA. Weryfikacja celu musi użyć `candidate_sha` z wygenerowanego `atlas_validation_status.json` oraz `prepare.outputs.sha`, następnie wszystkich trzech pełnych rund aplikacji, Windows, szybkich regresji, prawdziwego Lean/Mathlib, sceptycznego kontraktu i zadania `evidence`. Kontrolne `fragment=L1.4` to poprawna składnia selektora obejmująca podetap L1.4.1; próba z `fragment=L1.4.1` została odrzucona w `prepare` [#45252342342](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45252342342) i nie liczy się jako PASS.

[Pełne CI aplikacji #45251663688](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45251663688) na `ca6165bc` zakończyło się sukcesem: 738 testów Python, 10 sklasyfikowanych pominięć, `unreviewed_skips=0`, Chromium 509 rozdziałów, bez błędów JavaScript. Jest to **osobny** sukces CI, nie zastępuje kompletu 2+1. Poprzedni [3/3 #45181138327](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181138327) dotyczył wyłącznie historycznego `94a7b4a1e592b1b0504b881f9c016004786ca6d9`, przed poprawką #12.

## 3. Macierz kontroli negatywnych i pozytywnych

| Scenariusz | Oczekiwany skutek |
| --- | --- |
| Uszkodzone `documents.sha256` lub nietekstowe źródło | Odmowa albo `stale`, bez aprobaty |
| Manifest: cofnięcie `approved`, dopisanie/usunięcie wpisu, zmiana ścieżki przy identycznych bajtach | `changed_manifest_during_report` i `stale/needs_review` |
| SQLite: zmiana `entities.title`, `end_offset`, właściciela etykiety | `changed_index_binding`, `stale/needs_review` |
| SQLite: nowa spójna generacja `documents.content` i `sha256` podczas raportu | `changed_during_report`, `stale/needs_review` |
| `ready` bez sprawdzalnej ścieżki kanonicznego TeX | `unverifiable_canonical_source`, `stale/needs_review` |
| TeX zmieniony **po katalogu** dla `ready` | `unverifiable_canonical_source`, `stale/needs_review` |
| TeX zmieniony **po katalogu** dla `draft` z jawną ścieżką (nowa regresja #12) | `draft=0, stale=1`, `unverifiable_canonical_source`, bez `approved` |
| TeX niezmieniony dla `draft` z jawną ścieżką (nowa regresja pozytywna #12) | `draft=1`, `statement_status=needs_review`, bez `approved` |
| Przemycony `proof_status=compiled`, log i `certificate=true` w katalogu | Ścisła projekcja pól, bez wykonania i zawsze `certificate=false` |

**Dowód RED/GREEN:** [CI RED #45251355545](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45251355545) na `4cb894fd` odtworzył defekt; [poprawka `c84b00bc`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/c84b00bc6258fd08256afc60c3913bcbf8512621) i [regresja pozytywna `ca6165bc`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/ca6165bcd0f59aa6fb836e1922b51aeba51be193) są objęte zielonym CI #45251663688.

## 4. Granice bezpieczeństwa i kryterium odbioru

Kolejność odczytów SQLite, rejestru i pliku systemowego **nie tworzy atomowego snapshotu**. Podmiana po ostatniej kontroli lub szybka podmiana i cofnięcie może pozostać niewykryta. Recenzent musi samodzielnie ocenić, czy ograniczenie jest dopuszczalne dla **lokalnego odczytowego endpointu diagnostycznego**. To nie jest sandbox, atestacja kryptograficzna ani zewnętrzna recenzja zgodności Lean–LaTeX.

Wymagana decyzja `approve` lub `request changes` od **rzeczywiście niezależnego, uwierzytelnionego recenzenta**, przypięta do pełnego `ca6165bcd0f59aa6fb836e1922b51aeba51be193`, zawierająca ocenę powyższych testów i ostatecznego 3/3. Komentarz autora, AI, samodzielnie ustawiona flaga JSON i zielone testy nie spełniają tego warunku. Do tej decyzji utrzymać `stabilizing` i `certificate=false`, nie rozpoczynać L1.4.2 ani LA-01. Każda późniejsza zmiana ocenianego kodu wymaga nowego kandydata i nowego 2+1.
