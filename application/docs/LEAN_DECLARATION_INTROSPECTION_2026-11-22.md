# Lean 4 — inspekcja stałych występujących w wyrażeniach deklaracji
**Data:** 2026-11-22 · **Strumień A (aplikacja)**

## Co wdrożono

- `POST /api/lean/dependencies/inspect` przyjmuje **wyłącznie identyfikator** formalizacji obecnej w zaufanym lokalnym `manifest.json`; nie przyjmuje kodu, ścieżek ani argumentów procesu od klienta.
- `backend/lean_introspection.py`: dla zatwierdzonego, bieżącego SHA źródła i bieżącego pliku Lean tworzy tymczasową kopię z przypiętym do zarejestrowanych nazw poleceniem `run_meta`. Polecenie wykorzystuje `Lean.Meta.getConstInfo` oraz `ConstantInfo.getUsedConstantsAsSet` do odczytu stałych występujących w typie i wartości każdego twierdzenia, zatem nie opiera się wyłącznie na skanowaniu tekstu źródła.
- Uruchomienie za pomocą dotychczasowego `lake env lean`, **tylko** gdy `MATLIB_LEAN_RUN=1`, przy sprawdzeniu źródła i pełnego fingerprintu przed i po inspekcji. Wspólna systemowa blokada `lean_run_lock`, limit czasu, opcjonalne limity pamięci, ograniczenie wyjścia do 128 KiB oraz obowiązkowy kompletny raport z unikalnym tokenem zapobiegają przedstawianiu uciętych lub niepełnych wyników jako sukces.
- Formularz w panelu grafu zawiera przycisk „Odczytaj stałe przez Lean” i wyniki osobno dla każdej deklaracji. Zmiana zaznaczenia powoduje ignorowanie odpowiedzi poprzedniego żądania. Nieufny tekst wyświetlany jest wyłącznie przez `textContent`.
- Wdrożono testy jednostkowe i HTTP w `test_lean_introspection.py` oraz `test_lean_http.py`, test wykonywany przez Node w `test_lean_inspection_browser.py` i kontrakt HTML/JS.

## Co konkretnie znaczy wynik

`inspection_status=complete` oznacza jedynie, że **rzeczywiście uruchomiony proces Lean** zakończył się kodem zero, raportuje kompletny zbiór stałych dla każdej zarejestrowanej deklaracji, a badane pliki i zależności zachowały zgodny fingerprint. Nie oznacza to minimalnego zbioru przesłanek, przechodniego domknięcia wywołań ani dowodu zgodności tłumaczenia matematycznego z LaTeX-em. Wynik nie nadaje `proof_status=verified`, **zawsze `certificate=false`**, i nie nadpisuje istniejącej historii kompilacji.

Metoda Lean zwraca stałe syntaktycznie występujące w rozbudowanym wyrażeniu typu i dowodu; mogą to być również elementy infrastruktury elaboratora lub składniki przekazywane pośrednio. Nazw spoza bezpiecznego obsługiwanego podzbioru identyfikatorów API nie prezentuje jako częściowego sukcesu: odpowiedź jest blokowana. Przy więcej niż 160 stałych na deklarację i ponad 16 deklaracjach raport jest odrzucany zamiast obcinany.

## Stan walidacji

- Testy jednostkowe symulują proces narzędzia i kontrolują obsługę niekompletnego, fałszywego lub uciętego strumienia; **nie są dowodem rzeczywistej kompilacji poleceń MetaM w Lean 4.26.0**.
- Kiedy Lean/Lake jest niedostępny, interfejs zwraca `toolchain_unavailable` albo `blocked`; **nie deklarować `complete` bez rzeczywistego uruchomienia**.
- Dodano `application/tests/test_lean_introspection_real.py`, który uruchamia rzeczywisty `lake env lean` i weryfikuje kompletny raport dla `lst01_de_morgan_and`, **jeśli** na hoście istnieją Lake i lokalnie pobrana Mathlib. Bez tych warunków test jest oznaczany jako `skipped`, nigdy `PASS` rzeczywistego Lean. Polecenie: `cd application && python -m unittest tests.test_lean_introspection_real -v`.
- Potrzebny jest osobny smoke test kompilacji wygenerowanej części `run_meta` w przypiętym Lean 4.26.0 / Mathlib. Do czasu udanego testu kompatybilność konkretnego wyrażenia metaprogramistycznego pozostaje niepotwierdzona.
- Brak sandboxu dla kodu nieufnego, ryzyko TOCTOU i niepełne pokrycie przechodnich zależności pozostają otwarte; używać tylko na lokalnym, zaufanym serwerze.

Nie zmieniono kanonicznych `.tex`, `application/lean/src` ani `application/lean/manifest.json`.

## Jednoznaczna nawigacja po stałych i wymuszenie rzeczywistego testu

- Po udanej inspekcji aplikacja próbuje dopasować każdą nazwę stałej do listy zarejestrowanych twierdzeń w `/api/lean/catalog`. Tylko **jednoznaczne i aktualne** powiązanie daje odsyłacz do Czytnika; nie jest to formalne poświadczenie zależności semantycznej.
- Test Node `test_lean_inspection_browser.py` sprawdza nawigowanie do jedynego dopasowania, odmowę dla niejednoznacznych i nieaktualnych wpisów oraz nieuruchamianie kodu w wynikach tekstowych.
- Workflow `.github/workflows/lean-formalization.yml` uruchamia `test_lean_introspection_real.py` po zainstalowaniu przypiętych Lean 4.26.0 i Mathlib; `MATLIB_REQUIRE_REAL_LEAN_TEST=1` wymusza błąd, jeśli test nie może rozpocząć rzeczywistej inspekcji. Wynik należy odczytać z zakończonego GitHub Actions, a nie z samego commitu.
