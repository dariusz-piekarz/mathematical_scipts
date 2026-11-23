# Atlas / Lean — L1.3: bezpieczniejszy odczyt lokalnych zapisów Lean

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Stan:** implementacja i regresje weryfikowane przez CI; **L1.3 nie jest jeszcze stabilny**.

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

## Bramka stabilizacji — otwarta

- [ ] Szybkie regresje na Linux i Windows po końcowych commitach
  `1d659bb2` i `42426f17`.
- [ ] Pełne CI aplikacji na aktualnym kodzie; odsyłacze oraz
  rzeczywisty Chromium.
- [ ] Rzeczywisty Lean 4.26.0 + przypięty Mathlib z kompilacją i
  kontrolą aksjomatów na aktualnym kodzie (nie na wcześniejszym SHA).
- [ ] Osobny sceptyczny przegląd, w tym odmowa dla FIFO/symlinków
  i opis niezamkniętych klas ataków.
- [ ] Rygor 2+1: trzy **zakończone sukcesem** pełne kontrole
  dokładnie tego samego niezmiennego SHA.

Wyniki L1.1 i L1.2 pozostają zamknięte na własnych SHA. Nowe
wymagania L1.3 rozlicza się niezależnie; nie przenosi się
historycznego PASS na zmieniony kod.
