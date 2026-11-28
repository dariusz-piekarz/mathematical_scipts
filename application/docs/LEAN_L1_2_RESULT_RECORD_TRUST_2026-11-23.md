# Atlas / Lean — L1.2: ścisła walidacja zapisanych wyników uruchomień

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Jednostka:** L1.2 — osobna od ustabilizowanej optymalizacji L1.1.
**Stan końcowy: STABILNY (2026-11-23)** dla niezmienionego commita
`cfcf23f8eb3d60814c60212c27745b6dd01edf9d`. Trzy pełne przebiegi
CI na tym samym SHA, osobny przypięty Lean 4/Mathlib, natywne regresje
Linux/Windows i niezależny sceptyczny przegląd zakończone pomyślnie.
Odnosi się to wyłącznie do rygoru interpretacji lokalnych rekordów
uruchomienia; nie jest certyfikatem zgodności twierdzeń z LaTeX-em.

## Problem i ograniczony zakres

`application/backend/lean_results.py::last_run` dotąd sprawdzał podstawowe pola
rekordu, jego wersję i zgodność wartości z podanym fingerprintem, ale nie
wymagał pełnego, dokładnego schematu JSON. Nie odrzucał jawnie
`certificate=true`, nie sprawdzał duplikatów kluczy, a odczyt poprzez
`Path.read_text` po osobnym `stat` nie miał **limitu rzeczywistych bajtów
odczytanych** w razie wzrostu pliku pomiędzy operacjami. Odczyt mógł też
podążyć za dowiązaniem symbolicznym pliku rekordu.

Nie oznaczało to automatycznego uznania `certificate=true` w API, ponieważ
zwracana wartość `certificate` jest na sztywno `false`. Mimo to
niekompletny rekord nie powinien w ogóle być dopuszczany jako poprawny cache.

## Zmiana produkcyjna

Commit `23cf4183`:

- wymaga dokładnego zestawu pól bieżącego schematu 5, włącznie z **ośmioma
  SHA256**, `source_binding_sha256`, wersją toolchainu i `certificate=false`;
- odrzuca duplikaty kluczy JSON niezależnie od ich wartości, dzięki
  `object_pairs_hook`;
- rozróżnia rekord **nieprawidłowy** (`run_record_invalid`) od strukturalnie
  poprawnego rekordu ze **starym SHA** (`previous_run_outdated`);
- odrzuca dowiązania symboliczne pliku zapisu, błędny/bezstrefowy
  `finished_at`, nieprawidłowy `proof_status` oraz przekroczony limit pól
  `detail` i `log`;
- ogranicza rzeczywisty odczyt pliku do `MAX_RECORD_BYTES+1`, odrzucając
  rekord większy niż `MAX_RECORD_BYTES=30000` bajtów;
- używa jednego walidatora fingerprintu przy odczycie i zapisie.
  Nie zmienia `SCHEMA_VERSION=5` ani formatu poprawnie zapisanych rekordów.

**Uczciwa granica zaufania:** lokalny edytowalny plik JSON nie jest
kryptograficznym potwierdzeniem przeprowadzenia kompilacji Lean. Kontrola
formatu zmniejsza ryzyko przyjęcia uszkodzonych lub błędnie przygotowanych
danych, ale nie eliminuje dowolnej modyfikacji procesu/plików przez podmiot
mający prawa zapisu. Sprawdzenie `Path.is_symlink()` nie stanowi pełnej
ochrony przed wyścigiem zmian ścieżki przez inny proces. Testy i komunikaty
nie mogą podnosić semantycznego statusu dowodu.

## Testy

Commit `db5c2a70`, `application/tests/test_lean_results.py`:

- podstawowy zapis/odczyt prawdziwie utworzonego rekordu;
- `certificate=true` i `"false"`, dodatkowe i brakujące pola;
- niepoprawny SHA, `proof_status`, timestamp i wersja schematu;
- za długie `detail`, `log` i `declared_toolchain`;
- duplikat `proof_status` w JSON oraz nadmierny fizyczny rozmiar rekordu;
- prawidłowy, ale nieaktualny fingerprint nadal daje `previous_run_outdated`;
- brakujący/rozszerzony fingerprint oczekiwany i symlink rekordu.

Commity `752ea793` i `550bb1ea` podłączają ten test do szybkiego
Linux/Windows i osobnego przypiętego workflow Lean 4 / Mathlib. Kontrakt
API i runner Lean pozostają bez zmian.

## Niezależny przegląd sceptyczny i poprawki

Przeanalizowano bezpośrednio `lean_results.last_run`,
`lean_results.save_run` oraz miejsca użycia w API czytnika i w procesie
uruchamiania Lean. Weryfikacja nie opierała się wyłącznie na pozytywnych
wynikach testów: w jej trakcie wykryto i poprawiono dwa realne problemy.

1. **Rozmiar zapisu vs odczytu:** pierwotnie `save_run` ograniczał log do
   16 000 *znaków*, a `last_run` odrzucał rekord przekraczający
   30 000 *bajtów*. Wielobajtowe znaki UTF-8 oraz rozwinięcie escapingu
   JSON powodowały, że prawidłowo zapisany rekord był potem odrzucany.
   Commit [`7e50cd3e`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/7e50cd3ed3a14359be669f03c37d2d2e4f14141a)
   dobiera najdłuższy mieszczący się w limicie **sufiks logu** na podstawie
   rzeczywiście zakodowanego JSON i zapisuje maksymalnie 30 000 bajtów
   atomowo. Testy w commicie
   [`3c613db2`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/3c613db2d3a67840276c780e87cded0fa6748308)
   sprawdzają Unicode, znaki sterujące i odczyt zapisanej historii.
2. **Głębokie zagnieżdżenie JSON:** nawet lokalny plik mniejszy niż
   30 000 bajtów może zawierać 14 000 zagnieżdżonych tablic i wywołać
   `RecursionError` parsera. Zamiast błędu serwera odczyt ma zwracać
   `not_run` i `run_record_invalid=true`, zawsze
   `run_cached=false`. Implementacja:
   [`08419340`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/08419340233b0d9787fda06c31c9c00480cf8108);
   test deterministyczny (28 001 bajtów):
   [`cfcf23f8`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/cfcf23f8eb3d60814c60212c27745b6dd01edf9d).

Przegląd potwierdza: dokładny schemat rekordu 5; odrzucanie
zduplikowanych kluczy, fałszywego `certificate`, nadmiarowych lub
brakujących pól i błędnych SHA256; prawidłowe rozróżnienie rekordu
**niepoprawnego** od poprawnego, ale **nieaktualnego**; limit faktycznego
odczytu; jawnie `certificate=false` dla całej diagnostyki. Kompilacja
Lean i kontrola aksjomatów nie zastępują ręcznej oceny równoważności
twierdzenia z kanonicznym źródłem LaTeX.

**Pozostałe granice zaufania (jawnie zaakceptowane w zakresie L1.2):**
lokalny JSON z uprawnieniami zapisu nie ma podpisu/poświadczenia
kryptograficznego; proces mogący modyfikować katalog wyników może
podrobić strukturalnie poprawny rekord. `is_symlink()` przed
`open()` nie usuwa wyścigu TOCTOU, a zmiana katalogu nadrzędnego
przez niezaufany proces również wymaga oddzielnego modelu bezpieczeństwa.
Nie przypisujemy testom własności sandboxa ani dowodu pochodzenia danych.
Mechanizmy uruchamiania Lean i checkpointy `before/locked/after`
nie były w tej iteracji osłabiane.

## Bramka stabilizacji — ZALICZONA

Dla **identycznego** SHA
`cfcf23f8eb3d60814c60212c27745b6dd01edf9d`:

| Kontrola | Dowód | Wynik |
|---|---|---|
| Szybki Linux + natywny Windows | [#45154777288](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154777288), 185/85 testów, nowe przypadki Unicode i głębokiego JSON `ok` | PASS |
| Natywne Windows Job Objects | [#45154777383](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154777383) | PASS |
| Pełne CI, próba 1 | [#45154777272](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154777272), job `137624819790` | PASS |
| Pełne CI, próba 2 | ten sam run, `run_attempt=2`, job `137625935752` | PASS |
| Pełne CI, próba 3 | ten sam run, `run_attempt=3`, job `137627050626` | PASS |
| Lean 4.26.0, przypięty Mathlib, kompilacja i kontrola aksjomatów | [#45154777475](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154777475) | PASS |
| Rzeczywista introspekcja MetaM oraz trzy pełne fingerprinty | ten sam run Lean+Mathlib; fingerprint artefaktów zgodny z niezależnym przebiegiem profilera CPU | PASS |
| Sceptyczny przegląd semantyki zapisów oraz granic zaufania | powyższa analiza i testy z wykryciem dwóch usterek | PASS, z wyszczególnionymi ograniczeniami |

W **każdej** z trzech prób pełnego CI: `715` wykonanych testów Pythona,
`10` sklasyfikowanych pominięć, `unreviewed_skips=0`; Chromium
`passed`, `504` zaindeksowane rozdziały, `javascript_errors=[]`.
Wszystkie próby miały `candidate_sha=cfcf23f8eb3d60814c60212c27745b6dd01edf9d`.

**Decyzja:** L1.2 — walidacja i spójność lokalnych rekordów uruchomienia
Lean — **ZAMKNIĘTY / STABILNY** w precyzyjnie opisanym zakresie.
Jeżeli przyszła zmiana obejmie ten podsystem, wymaga własnych regresji
i nowej stabilizacji; sukcesy dla starego SHA nie przechodzą
automatycznie na nowy kod. L1.1 pozostaje niezależnie **ZAMKNIĘTY**
dla SHA `95508306`.
