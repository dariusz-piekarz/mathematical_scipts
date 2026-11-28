# Atlas / Lean — L1.3: bezpieczniejszy odczyt lokalnych zapisów Lean

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Stan końcowy: L1.3 ZAMKNIĘTY / STABILNY** (2026-11-23), wyłącznie dla niezmienionego commita `42426f17dd90a553050657b55537f907e3231d45` i zakresu opisanego poniżej. Rygor 2+1, natywne testy Windows/Linux oraz rzeczywisty Lean+Mathlib zakończone sukcesem.

## Motywacja i zakres

Zakończony podetap L1.2 wymaga kompletnego schematu JSON, fingerprintu,
`certificate=false` i ściśle ograniczonego rozmiaru zapisanego rekordu.
Pozostawiał jednak lukę między `Path.is_symlink()` /
`Path.is_file()` a późniejszym otwarciem przez `Path.open()`. Zmiana
wpisu katalogowego w tym oknie mogła doprowadzić do otwarcia innego pliku,
zanim proces ponownie zbadał jego typ.

**L1.3** zmienia wyłącznie odczyt w
`application/backend/lean_results.py::last_run`; nie modyfikuje
`save_run`, procesu kompilacji ani trzech checkpointów fingerprintu
`before/locked/after`.

## Mechanizm

- `os.open(path, O_RDONLY | O_BINARY? | O_NOFOLLOW? | O_NONBLOCK?)`:
  `O_NOFOLLOW` blokuje podążanie za końcowym symlinkiem na obsługujących
  systemach POSIX. Na Windows brak tego samego mechanizmu w przenośnym
  `os.open`, więc dodatkowo walidowany jest `lstat` nazwy.
- `O_NONBLOCK` na POSIX zapobiega zawieszeniu przy podmianie
  regularnego rekordu na FIFO między wstępnym sprawdzeniem a `os.open`.
  Po uzyskaniu deskryptora odrzucany jest każdy typ inny niż regularny.
- `os.fstat` deskryptora porównywany z `Path.lstat` wpisu katalogowego
  **przed** i **po** ograniczonym odczycie (maksymalnie 30 001 bajtów).
  Porównuje się identyfikator pliku `(st_dev, st_ino)`, rozmiar i
  `st_mtime_ns`; `st_ctime_ns` w tym samym API dodatkowo sprawdza, czy
  metadane nie zmieniły się podczas odczytu.
- Na Windows `os.fstat(fd)` i `Path.lstat(path)` mogą raportować różną
  semantykę `st_ctime_ns` dla tego samego pliku. Z tego powodu
  **nie porównuje się między tymi dwoma API pola ctime**, ale nadal
  kontroluje się ctime *w ramach każdego z tych API*.
  Kontekst techniczny: [CPython issue 157671](https://github.com/python/cpython/issues/157671).
- Nieudana walidacja musi zwrócić `not_run`, `run_cached=false` i
  `run_record_invalid=true`, bez podniesienia do `compiled`.
  `certificate=false` pozostaje bez zmian.

## Testy negatywne

Nowe przypadki w `application/tests/test_lean_results.py`:
1. Przy prawidłowym pliku otrzymujemy nadal `compiled`; test sprawdza
   flagę `O_NOFOLLOW`, jeśli jest obsługiwana.
2. Rozbieżność metadanych deskryptora i wpisu katalogowego — odmowa.
3. Rzeczywista podmiana końcowej nazwy na symlink tuż przed
   `os.open` — odmowa. Test jest jawnie pomijany, jeśli symlinki
   nie są dostępne.
4. Rzeczywista podmiana otwartego pliku na nową nazwę o identycznych
   bajtach — odmowa na POSIX; Windows może odmówić zmiany nazwy
   otwartego uchwytu, więc to szczególne ćwiczenie jest jawnie
   pomijane, nie oznaczane jako PASS.
5. Podmiana na FIFO przed `os.open` — odmowa bez zawieszenia.
   Test na systemach bez `mkfifo` jest pomijany.

## Dziennik korekt

- `58623b69`: pierwszy odczyt z deskryptora i statystykami.
- `b17677a6`: regresje wyścigów i symlinków.
- Windows ujawnił błędne założenie: porównanie `st_ctime_ns`
  między `fstat` a `lstat` odrzucało nawet poprawny, niezmieniony
  rekord. Szybkie CI i natywny Windows po tych commitach miały
  **FAIL**, co resetuje stabilizację.
- `7254a66d`: poprawka semantyki ctime w Windows, bez wyłączenia
  kontroli tożsamości i zmian między checkpointami.
- `1d659bb2`: dodatkowe `O_NONBLOCK` przed kontrolą FIFO.
- `42426f17`: regresja FIFO.

## Granice bezpieczeństwa

To jest warstwa **lokalnego cache diagnostycznego**, a nie bezpieczny
mechanizm odczytu nieufnego drzewa katalogów. Podmiana katalogów
nadrzędnych (w tym symlinków), uprawnienia zapisu zewnętrznych
procesów, możliwe podwójne podmiany nazwy między kontrolami oraz
brak pełnego atomowego snapshotu są poza gwarancją L1.3.
Nie zapewnia to kryptograficznego poświadczenia kompilacji Lean,
izolacji wykonywalnych plików Lean ani równoważności formalizacji
z kanonicznym LaTeX-em.

## Bramka stabilizacji — ZALICZONA

**Zamrożona wersja kodu i regresji:**
`42426f17dd90a553050657b55537f907e3231d45`. Dalszy
commit dokumentacyjny nie stanowi nowego SHA produkcyjnego.

| Kontrola | GitHub Actions / szczegóły | Wynik |
|---|---|---|
| Szybki Linux + Windows | [#45157059258](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157059258), 189/89 testów | PASS |
| Natywne Windows Job Objects | [#45157059445](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157059445) | PASS |
| Pełne CI aplikacji, próba 1 | [#45157059233](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157059233), job `137632579507` | PASS |
| Pełne CI aplikacji, próba 2 | ten sam run, `run_attempt=2`, job `137633720323` | PASS |
| Pełne CI aplikacji, próba 3 | ten sam run, `run_attempt=3`, job `137634737212` | PASS |
| Przypięty Lean 4.26.0 / Mathlib, realna kompilacja i aksjomaty | [#45157059389](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157059389) | PASS |
| MetaM, trzy fingerprinty, parowany benchmark ścieżek, profil CPU | ten sam pinned workflow, job `137634354400`; digest artefaktów z benchmarku i profilera identyczny | PASS |
| Niezależny przegląd sceptyczny | poniższa analiza i regresje modyfikujące rzeczywistą ścieżkę pliku | PASS w opisanym modelu |

W **każdym** z trzech pełnych przebiegów: `719` wykonanych testów
Pythona, `10` sklasyfikowanych pominięć,
`unreviewed_skips=0`, `505` rozdziałów w indeksie,
Chromium `passed`, `javascript_errors=[]`, pełny
`candidate_sha=42426f17dd90a553050657b55537f907e3231d45`.

**Przegląd sceptyczny:** przebieg pierwszych zmian L1.3 wykazał
rzeczywistą regresję na Windows, której nie zamaskowano. Wyjaśniono
niezgodne semantyki `ctime` między `fstat` i `lstat`, a następnie
uzyskano sukces testów Windows bez rezygnacji z kontroli identyfikatora,
rozmiaru i modyfikacji pliku. Dodatkowo wykryto i poprawiono ryzyko
blokady przy podmianie rekordu na FIFO jeszcze przed kontrolą typu.
Na Linux potwierdzono: odmowę podmiany ścieżki na symlink przed otwarciem,
odmowę zastąpienia otwartego pliku mimo identycznej treści oraz odmowę
dla FIFO bez oczekiwania na zapisujący proces. Na Windows test symlinku
i symulacji metadanych przeszedł; test zamiany nazwy **otwartego**
pliku został **jawnie pominięty** ze względu na odmowę WinError 32,
a test POSIX FIFO również został pominięty. Te pominięcia nie są
udawanymi sukcesami; odnoszą się do specyficznych możliwości hosta.

**Granice niezmienione:** lokalny modyfikowalny JSON nie jest
kryptograficznym dowodem pochodzenia, sprawdzenie końcowego wpisu
nie zapewnia atomowej kontroli wszystkich katalogów nadrzędnych,
nie wyklucza wszystkich wielokrotnych wyścigów ani nie izoluje
dowolnego kodu Lean. Jak wcześniej, `certificate=false`;
kompilacja, kontrola aksjomatów i zgodność tezy z LaTeX-em mają
odrębne statusy. Nie osłabiono checkpointów `before/locked/after`.

**Decyzja:** zamknąć **L1.3 — odczyt i tożsamość lokalnego rekordu
historii Lean**. Następny podetap architektury wymaga własnego
zakresu, testów i stabilizacji. L1.1 i L1.2 pozostają
zamknięte na swoich odrębnych SHA.
