# Atlas / Lean — L1.4.1: sceptyczny przegląd techniczny kandydata

**Data:** 2026-11-23  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Sprawdzany niezmienny commit:** `1c4b89b1a9ef8affe95e3073739d99bc1c57aa2d`  
**Wynik cząstkowy w chwili pierwotnego sporządzenia dokumentu (przed CI):** przegląd statyczny i samodzielne pełne CI aplikacji wykonane; **stabilizacja 2+1 = 0/3 potwierdzonych kompletnych rund**, końcowa decyzja `stable` **wstrzymana**. Raport nie jest podpisaną aprobatą niezależnego człowieka.

## Granice zaufania

L1.4.1 jest tylko odczytowym raportem rejestracji formalizacji. `ready` opisuje zgodność powiązania z aktualnym dokumentem i wymaganym kanonicznym plikiem, **nie** wykonany dowód. `statement_approved` liczy wpisy z recenzją stwierdzenia, ale nie poświadcza jej niezależności ani równoważności z całym kontekstem LaTeX. Raport zawsze ma `proof_status_included=false`, `run_history_checked=false`, `dependency_fingerprint_checked=false`, `certificate=false`. Nie dotyka runnera, logów ani zapisów JSON.

## Sprawdzone kontrprzypadki

1. **Przenikanie przyszłych danych cache:** jawny allowlist `REPORT_ITEM_FIELDS` eliminuje podrobione `proof_status=compiled`, `last_run_log` i `certificate=true` nawet wtedy, gdy katalog zostanie później rozszerzony.
2. **Niespójny indeks rozdziału:** rozbieżny SHA256 treści indeksu powoduje `corrupt_document`; podmiana dokumentu pomiędzy dwoma odczytami powoduje `changed_during_report`. W obu sytuacjach nie wolno zwrócić statusu `ready`/zatwierdzenia.
3. **Brak fizycznego TeX:** sama deklaracja `source_document_sha256` w manifeście nie wystarcza; brak `source_document_path` oznacza `unverifiable_canonical_source`.
4. **Zmiana TeX po odczycie katalogu:** ponowne sprawdzenie zawartości kanonicznego pliku obniża `ready` do `stale` i `approved` do `needs_review`.
5. **Niewykonanie historii/fingerprintu:** testy wymuszają wyjątek przy niechcianym odczycie `lean_results.last_run` lub obliczeniu `lean_results.fingerprint`.
6. **Nieznany/błędny rozdział:** HTTP 404/400; rozdział bez formalizacji jest poprawnym pustym raportem.
7. **Zgodność zakresu:** bez zmian kanonicznych `.tex`, `.lean`, manifestu pilotażu, `lean_results.py`, runnera i trzech checkpointów `before/locked/after`; commit `1c4b89b1` obejmuje wyłącznie `lean_chapter_report.py`, `test_lean_catalog.py` i dokumentację.

## Rzeczywiste dowody CI — wyłącznie dla wskazanego SHA

[Pełne CI aplikacji #45160932019](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160932019): `completed/success`, 729 wykonanych testów Python, 10 sklasyfikowanych pominięć, 0 pominięć bez kategorii; wszystkie **10 nazwanych testów L1.4** kończą się `ok` w rzeczywistym logu. Chromium: `passed`, 506 zaindeksowanych rozdziałów, `javascript_errors=[]`. Działanie przeglądarki i zapisy projektów sprawdzone.

Pominięcia w tym jobie obejmują osobny host dla Lean/Mathlib, Windows i konfigurację lokalnego TeX oraz brak delegowanego kontrolera cgroup. Nie wolno liczyć ich jako zaliczenia tych obowiązkowych kontroli. Oddzielny [immutable-SHA 2+1 #45160961943](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943) został zgłoszony dla tego kandydata; przy sporządzaniu raportu oczekuje w kolejce, gdy starszy [#45159511491](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159511491) kończy własne rundy na innym SHA. Wyniki starszego uruchomienia nie są przypisywane do tego kandydata.

## Niezamknięte ryzyka i bramka końcowa

- Kontrole dwóch odczytów SQLite i powtórnego hash TeX nie są atomową migawką wieloplikowego systemu. Modyfikacja po ostatniej kontroli albo jednoczesna edycja etykiet/manifestu nadal wymaga odpowiedniego modelu blokowania lub migawkowania w kolejnej jednostce architektury.
- Lokalnie modyfikowalne dane i rekordy JSON nie stanowią podpisanego poświadczenia wykonania Lean. Pomyślny Lean, kontrola aksjomatów i recenzja tekstu to odrębne wymagania.
- Status `stable` wymaga końcowego raportu z **trzech kompletnych** rund na identycznym SHA: pełne CI aplikacji/Chromium, natywne Linux i Windows, przypięty Lean 4.26.0/Mathlib z kontrolą aksjomatów, sceptyczny kontrakt i brak nierozliczonych krytycznych defektów; dodatkowa niezależna, uwierzytelniona aprobata recenzenta według kanonicznego planu.
- Jeżeli 2+1 ma błąd lub test wymagany został pominięty, pozostać przy `testing`/`blocked`, naprawić i **wyzerować** licznik dla nowego SHA. Nie przechodzić do L1.4.2.

**Decyzja tej iteracji:** odnotować zakończony przegląd statyczny i 10 rzeczywistych regresji, **nie** zamykać L1.4.1. `certificate=false` pozostaje niezmienne.

## Aktualizacja 2026-11-23, 13:00 Europe/Warsaw — wykonane 3/3

Stan `0/3` z pierwotnego nagłówka był migawką **przed** zakończeniem CI.
Aktualne, sprawdzone wyniki kandydata
`1c4b89b1a9ef8affe95e3073739d99bc1c57aa2d`:

- [2+1 #45160961943](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943)
  zakończony `completed/success` 2026-11-23 11:23:30 UTC;
  trzy pełne rundy aplikacji, Lean/Mathlib, testów natywnych i regresji Lean,
  `skeptical_contract` oraz `evidence` zakończone `success`.
- **3 × 729** nazwanych wyników testów Python, **3 × 10**
  sklasyfikowanych pominięć, **zero** nierozliczonych. Osobne testy
  przypiętego Lean/Mathlib i natywnego Windows przechodzą w wymaganych
  zadaniach, więc pominięcia w jobach aplikacyjnych nie są fałszywie
  liczone jako wykonane testy.
- W każdej rundzie zadanie `lean-pilot` zgłosiło rzeczywistą
  kompilację **4 plików Lean i 18 twierdzeń**, `axiom_check=passed`,
  `semantic_certificate=false`.
- [Artefakt `atlas-validation-status`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943/artifacts/14814696978):
  `passes[1..3].passed=true`, `workflow_results` bez błędów,
  `problems=[]`, **`skeptical_review=pending`,
  `status=stabilizing`, `certificate=false`**.
- [Issue #8](https://github.com/dariusz-piekarz/mathematical_scipts/issues/8)
  otwarte jako formalny wniosek o **niezależną, uwierzytelnioną recenzję**
  konkretnie tego SHA. Automatyczna walidacja/raport sporządzony przez
  asystenta nie może jej zastąpić.

**Decyzja:** techniczna bramka 2+1 jest zakończona; niezależny odbiór
i formalne przejście do `stable` — **nie**. Obecna jednostka L1.4.1
pozostaje `stabilizing`. L1.4.2 nie rozpoczęto.

## Aktualizacja audytu 2026-11-23 — krytyczne znalezisko po 3/3

Weryfikacja źródeł przed zewnętrznym odbiorem wskazała realną lukę
w `1c4b89b1`: drugi odczyt manifestu sprawdzał ścieżkę kanonicznego
TeX, lecz nie porównywał aktualnego `statement_status`. Zatem
wycofanie `approved` po odczycie katalogu mogło pozostawić licznik
`statement_approved=1`. Ponadto zmiana liczby pozycji rejestru albo
przypisania etykiety w SQLite nie musiała zmieniać SHA dokumentu.

Poprawka w [`a1f93d98`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/a1f93d985778492082a66db3975d05e9d73ed763)
wymaga spójnego zestawu identyfikatorów dla całego rozdziału,
porównuje najważniejsze pola drugiego manifestu, ponawia
`owner_status` na etykietach i obniża `ready/approved` do
`stale/needs_review` w razie rozbieżności. Trzy nowe regresje
testują cofnięcie aprobaty, dopisanie formalizacji i usunięcie
etykiety w trakcie przygotowania raportu.

To nadal nie jest transakcja atomowa obejmująca SQLite, manifest i
TeX. Zostaje `certificate=false`. Wcześniejszy, prawdziwy
[3/3 PASS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943)
odnosi się **wyłącznie do starszego SHA**. Wniosek o recenzję starego
kandydata ([issue #8](https://github.com/dariusz-piekarz/mathematical_scipts/issues/8))
zamknięto jako zastąpiony, bez udawania odbioru. Dla
[`a1f93d98` testy/2+1 ruszyły od zera](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175198218).
Końcowy status `stable` pozostaje wstrzymany.

## Wynik 3/3 na nowym kandydacie — 2026-11-23

Niezmienny commit `a1f93d985778492082a66db3975d05e9d73ed763`
po naprawie weryfikacji manifestu i relacji etykiet przeszedł
[pełny techniczny 2+1 #45175198218](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175198218).
W każdej rundzie: `732` testy Pythona, `10` sklasyfikowanych
pominięć, `0` nierozliczonych; 507 rozdziałów w Chromium; natywne
Windows i przypięty Lean/Mathlib PASS; kompilacja 18 twierdzeń w
4 plikach, `axiom_check=passed`. Sceptyczne testy kontraktowe PASS.

[Końcowy status](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175198218/artifacts/14820217988):
`problems=[]`, `skeptical_review=pending`,
`status=stabilizing`, `certificate=false`.
Niezależnej, uwierzytelnionej aprobaty w
[issue #9](https://github.com/dariusz-piekarz/mathematical_scipts/issues/9)
jeszcze nie uzyskano; wpisy autora zmian ani asystenta nie stanowią jej
substytutu. Historyczne przeglądy nie poświadczają semantycznej
równoważności LaTeX–Lean. Pozostaje `stabilizing`, nie `stable`;
L1.4.2 nadal nierozpoczęte.

## Zakończenie technicznej stabilizacji — `94a7b4a1`

[Workflow 2+1 #45181138327](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181138327)
zakończył się `completed/success` na niezmiennym SHA
`94a7b4a1e592b1b0504b881f9c016004786ca6d9`. Wszystkie trzy pełne rundy aplikacji,
natywnego Windows, rzeczywistego Lean/Mathlib i regresji
zakończyły się sukcesem. Każda runda: 735 testów Python, 10
sklasyfikowanych pominięć, 0 nierozliczonych, Chromium 509 rozdziałów,
brak błędów JavaScript. Lean 4.26.0 / Mathlib
`2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`,
4 pliki, 18 twierdzeń i `axiom_check=passed` w każdym przebiegu.
Sceptyczny kontrakt i końcowe zadanie `evidence` także PASS.

[Artefakt końcowy](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45181138327/artifacts/14823870210)
dokumentuje `problems=[]`, `3/3`, lecz `status=stabilizing`,
`skeptical_review=pending`, `certificate=false`.
To techniczne potwierdzenie wskazanego kodu, **nie**
uwierzytelniony niezależny odbiór ani certyfikacja matematyczna.
[Issue #10](https://github.com/dariusz-piekarz/mathematical_scipts/issues/10)
pozostaje otwarte. Nie awansować do L1.4.2 przed formalnym `stable`.
