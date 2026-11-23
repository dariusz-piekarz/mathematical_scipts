# Atlas matematyczny — postępy sekwencyjnego planu

**Plan:** [ATLAS_DEVELOPMENT_ROADMAP.md](ATLAS_DEVELOPMENT_ROADMAP.md).  
**Inicjalizacja:** 22.11.2026, przed rozpoczęciem zaplanowanego pierwszego uruchomienia 23.11.2026 o 00:00 Europe/Warsaw.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Wskaźnik wykonywania

- Aktywny etap: **1 — Lean 4, stabilizacja i rozwój formalizacji**.
- Aktywny fragment: **L1.1 — limit odczytu `.olean` i weryfikacja CI**.
- Stan: **testing** (wdrożono poprawkę we wcześniejszej iteracji, ale nie potwierdzono jeszcze pełnych testów po zmianie).
- Stabilizacja 2+1 na SHA finalnego kodu: **0/3** potwierdzonych czystych kontroli.
- Dodatkowy sceptyczny audyt bieżącej poprawki: **niezaliczony / do wykonania**.
- Następny krok: odczytaj aktualny `application/docs/LEAN_FORMALIZATION_PLAN.md`, HEAD, logi i workflow dla poprawki limitu rzeczywistych odczytów `.olean`; uruchom/zweryfikuj regresje obejmujące współbieżny wzrost pliku, za wczesny EOF, narzut jednego bajtu, Windows/Linux oraz prawdziwy Lean/Mathlib. Wykonaj kolejne kontrole do 2+1. **Nie przechodź do L1.2 do pełnego zamknięcia L1.1.**

## Status etapów

| Etap | Status | Pierwszy nierozliczony fragment |
| --- | --- | --- |
| 1. Lean 4 | implementing | L1.1 |
| 2. Inteligentny graf | planned | G2.1 |
| 3. Generator PDF + Czytnik | planned | P3.1 |
| 4. Centrum audytów i deduplikacja | planned | A4.1 |
| 5. Wyszukiwanie semantyczne | planned | S5.1 |
| 6. Asystent matematyczny | planned | M6.1 |
| 7. Ścieżki nauki i desktop | planned | N7.1 |

## Dziennik iteracji

### 2026-11-22 — inicjalizacja planu

- Użytkownik zatwierdził siedem etapów w jednej kolejce zamiast dwóch niezależnych automatyzacji Lean.
- Jednostką pracy jest jeden konkretny fragment: implementacja/testy/poprawki → powtarzane kontrole → stabilność 2+1 i osobny sceptyczny audyt → dopiero następny fragment.
- Jest to **utworzenie planu**, nie dowód wykonania lub zaliczenia L1.1.
- Odwołanie do ostatniego statusu: sekcja „Strumień A — limit faktycznego odczytu .olean podczas zmian współbieżnych” w `LEAN_FORMALIZATION_PLAN.md`. Jej wartości 0 czystych kontroli są punktem startu, nie trwałą prawdą; każda automatyczna iteracja musi sprawdzić nowsze dane.
- Przy każdym przebiegu dopisz datę i godzinę, numer fragmentu, SHA, zmienione pliki, testy (wyniki rzeczywiste), błędy, status 2+1 i następny krok. Nie nadpisuj wierszy historii, chyba że prostujesz błąd z wyjaśnieniem.

### 2026-11-22, 23:55 Europe/Warsaw — L1.1: niezależna kontrola logów CI

- **HEAD przed zapisem:** `18541e46032323d425e496f3241fbb2a3a0ffb6f`; nie zmieniono kodu produkcyjnego ani testów, wyłącznie ten dziennik. Aktualne bloby `lean_environment.py` (`a76c52d1b05a5b80ecc27a981cadf114309e8e2c`) i `test_lean_environment.py` (`2b653ae92a0f9214a9587a342d401ce7890714be`) zawierają limit odczytu, odrzucenie przedwczesnego EOF i dodatkowy odczyt jednego bajtu oraz odpowiadające regresje.
- **Potwierdzone, zakończone CI dla SHA `31f65e151d9d8fa557947feee3cbbee6c6c101b2`:** [pełne CI aplikacji #45079829856](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829856) `completed/success`, 670 testów, 10 pominiętych, Chromium `passed`, 494 rozdziały, zero błędów JavaScript; [szybkie Linux/Windows #45079830059](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079830059) `completed/success`, Linux 137 testów (5 pominiętych), natywny Windows 40 testów (3 pominięte). Wyniki pochodzą z odczytanych logów rzeczywistych zadań, nie z samego statusu commitu.
- **Pinned Lean/Mathlib:** [#45079829879](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829879) pozostawał `in_progress` podczas kontroli; **niezaliczony**. Nie sprawdzono jeszcze, czy wszystkie pominięte testy są nieobowiązkowe dla L1.1. Dodatkowy sceptyczny audyt przypadków brzegowych, w tym rzeczywistego wzrostu pliku i limitu I/O, nadal wymagany.
- **Licznik 2+1:** na kandydacie `31f65e15` udokumentowano **1 pełny czysty przebieg aplikacji**, ale nie 2+1. Na aktualnym HEAD nie ma dwóch niezależnych pełnych kontroli ani dodatkowego audytu: **0/3** dla końcowego SHA. Status **testing**, nie `stable`.
- **Następny dokładnie jeden krok:** sprawdzić zakończenie pinned Lean+Mathlib na `31f65e15`, logi i pomiar, a następnie dopiero przygotować kontrolną serię 2+1 na jednym niezmienionym SHA z oceną wszystkich wymaganych skipów. Nie przechodzić do L1.2.

### 2026-11-23, 00:58 Europe/Warsaw — L1.1: potwierdzenie zakończenia pinned Lean/Mathlib

- **HEAD przed zapisem:** `2754923bff4bb75dfd3f2903799889b127d837d2`. Ta iteracja jest wyłącznie krokiem weryfikacyjnym L1.1; bez zmian kodu, testów, źródeł Lean ani kanonicznych `.tex`.
- **Nowy wynik:** [Lean/Mathlib #45079829879](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829879) dla `31f65e151d9d8fa557947feee3cbbee6c6c101b2` ma obecnie `completed/success` (zaktualizowany 2026-11-22 22:57:35 UTC). Odczytano rzeczywiste zadanie `lean-pilot` (`137385705969`): zakończone sukcesem kroki instalacji przypiętego Lean/Mathlib, kontroli dokładnych rewizji, kompilacji formalizacji i aksjomatów, obowiązkowej introspekcji Lean MetaM bez pominięć oraz trzech rzeczywistych pełnych wywołań fingerprintu na przypiętym Mathlib. To jest **potwierdzenie jednego zakończonego workflow**, nie trzech niezależnych przebiegów CI.
- **Wcześniejsze dowody na tym samym SHA:** [pełny CI aplikacji #45079829856](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829856) i [Linux/Windows #45079830059](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079830059), oba `completed/success`; odczytane zadania i ich kroki również potwierdzają sukces. Są to trzy **różne zakresowo workflow jednego zestawu na starym SHA**, a nie dwa niezależne powtórzenia pełnego zestawu plus sceptyczny audyt.
- **Kontrola źródła:** `application/backend/lean_environment.py` blob `a76c52d1b05a5b80ecc27a981cadf114309e8e2c` stosuje odczyty ograniczone pozostałym rozmiarem, odmowę przedwczesnego EOF, dodatkowy odczyt jednego bajtu i porównanie metadanych; `application/tests/test_lean_environment.py` blob `2b653ae92a0f9214a9587a342d401ce7890714be` zawiera regresje wzrostu strumienia i ucięcia. Nie wykonano w tej iteracji nowego lokalnego testu ani niezależnego eksperymentu z prawdziwym współbieżnie zmienianym plikiem.
- **Ograniczenia:** aktualny HEAD `2754923b` różni się od `31f65e15` (równoległe zmiany w Bibliotece). Nie zweryfikowano jeszcze wszystkich skipów, nie przeprowadzono dwóch niezależnych pełnych zestawów CI i dodatkowego sceptycznego audytu na identycznym końcowym SHA. Status **testing**, stabilizacja **0/3 na bieżącym HEAD**, audyt sceptyczny **niezaliczony**; `certificate=false` pozostaje wymagane.
- **Następny dokładnie jeden krok:** przeanalizować skipy i wymagane testy L1.1 na bieżącym SHA, następnie zaplanować czystą serię 2+1 bez zmian kodu; nie rozpoczynać L1.2.

### 2026-11-23, 02:04 Europe/Warsaw — L1.1: audyt pominięć testów natywnych

- **HEAD przed zapisem:** `a45289b57114abaf90cdcc28e20a399d8130c147`. Odczytano na aktualnym HEAD oba dokumenty Atlasu, ogólny dziennik, plan Lean, implementację `lean_environment.py`, testy `test_lean_environment.py` i trzy odpowiednie workflow. W tej iteracji **nie zmieniono kodu ani testów**, tylko udokumentowano weryfikację.
- **Linux:** [lean-inspection-fast #45079830059](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079830059), zadanie `137385250704`, `completed/success`, 137 testów, 5 pominiętych. Log ujawnia wszystkie pięć: `test_native_windows_junction_directory_is_rejected`, `test_windows_open_lock_file_cannot_be_renamed`, `test_native_nested_windows_jobs_preserve_inner_limit`, `test_native_windows_job_memory_restriction`, `test_native_windows_timeout_terminates_descendants`. Są to przypadki przeznaczone dla natywnego Windows; nie traktować ich jako zaliczonych na Linux.
- **Windows:** to samo workflow, zadanie `137385251037`, `completed/success`, 40 testów, 3 pominięte: `test_actual_linked_lock_directory_is_rejected` (wymaga POSIX symlinków katalogów), `test_replaced_lock_file_during_open_is_rejected` (Windows nie pozwala zmienić nazwy otwartego pliku blokady CRT), `test_symlinked_lock_file_fails_closed` (wymóg POSIX `O_NOFOLLOW`). Testy `lean_environment` dotyczące limitu i zawartości `.olean` przeszły na obu systemach. Żaden z 8 wymienionych skipów nie dotyczy bezpośrednio nowej regresji ograniczonego odczytu `.olean`.
- **Pinned Lean:** [#45079829879](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829879), zadanie `137385705969`, `completed/success`; 46 testów Pythona przed instalacją, 2 obowiązkowe rzeczywiste testy introspekcji Lean po instalacji i 3 pełne wywołania fingerprintu. Wewnętrzne kroki akcji Lean oznaczone `skipped` nie zastępują osobnych jawnych kroków kompilacji, audytu aksjomatów i MetaM, które zakończyły się sukcesem.
- **Pełne CI aplikacji:** [#45090419038](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45090419038) dla `c426ca4e24462ae009bfff2e76a0f7e72837858c` — `completed/success`, 670 testów, 10 pominiętych. Zbiorczy log `unittest -q` podaje liczbę, ale **nie nazwy** tych dziesięciu; ich klasyfikacja nadal jest otwarta. Nie wolno z tego wyniku wywodzić, że wszystkie wymagane przypadki zostały wykonane.
- **Sceptyczna uwaga o zakresie:** test `test_olean_read_remains_bounded_for_a_growing_stream` używa deterministycznego zastępnika `Path.open`, który zwraca kolejne bajty; test `test_olean_truncated_read_is_rejected` również używa zastępnika. To poprawne regresje logiki limitu, lecz nie niezależny test rzeczywistego współbieżnego wzrostu pliku na dysku. Sam sukces przypiętego Mathlib nie dowodzi, że taki wyścig został rzeczywiście wywołany.
- **2+1 na aktualnym HEAD:** **0/3**; ostatnie zakończone workflow są na innych SHA. Sceptyczny audyt rozpoczęty (ocena pominięć i granic testów), ale **niezaliczony**, brak niezależnego przebiegu kontrolnego. **Status: testing**, `certificate=false`; L1.2 pozostaje zamknięty.
- **Następny dokładnie jeden krok:** dodać i wykonać adekwatny niezależny test rzeczywistego współbieżnego wzrostu `.olean` (z kontrolą limitu odczytu i fail-closed), następnie od nowa rozliczyć 2+1 na końcowym SHA.


### 2026-11-23, 02:55 Europe/Warsaw — L1.1: test rzeczywistego wzrostu pliku .olean

- **HEAD przed zmianą testu:** `e69ec39ca1c84b02332c7dd6c549aa0d03df0098`; **commit testu:** [`3b1ca58dc74ce3a2e88f3826e1b50f108171459e`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/3b1ca58dc74ce3a2e88f3826e1b50f108171459e). Jedyny zmieniony plik kodowy: `application/tests/test_lean_environment.py`; źródła produkcyjne i kanoniczne `.tex` nietknięte.
- **Jedna mierzalna poprawka testowa:** dodano `test_real_olean_growth_during_read_fails_closed`. Test zapisuje prawdziwy plik 128 KiB, uruchamia osobny wątek dopisujący jeden bajt do rzeczywistego deskryptora pliku, synchronizuje dopisanie z pierwszym `read` (nakładka `Path.open` wyłącznie synchronizuje, nie zastępuje zwracanych bajtów), wymaga odmowy `grew while fingerprinting`, sprawdza rozmiar końcowy i brak zawieszenia wątku. Zabezpieczenie nadal czyta tylko początkowe 128 KiB i jeden bajt kontrolny.
- **Weryfikacja:** zapis na istniejącej gałęzi GitHub potwierdzony. Lokalnego uruchomienia nie wykonano: środowisko wykonawcze nie miało dostępu sieciowego do pobrania repozytorium. Bezpośrednio po commicie API GitHub Actions nie zwracało jeszcze żadnego workflow dla jego SHA; **nie ma potwierdzonego zakończonego CI** dla tej zmiany. Test wymaga rzeczywistego przebiegu na Linux i Windows; do tego czasu jest niezweryfikowany. Poprzednie zakończone sukcesem [aplikacja #45092456367](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45092456367) i [Lean #45079829879](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079829879) dotyczą innych SHA i nie zaliczają serii.
- **Sceptyczny audyt:** otwarty; synchronizacja eliminuje losowość momentu dopisania, ale test nie obejmuje zmiany pliku bezpośrednio po dodatkowym odczycie ani wszystkich zachowań systemów plików. Nie traktować sukcesu pojedynczego testu jako dowodu całkowitego braku TOCTOU. **Licznik 2+1: 0/3** (zmiana testu resetuje serię); **status: testing**, `certificate=false`, L1.2 nierozpoczęty.
- **Następny dokładnie jeden krok:** zweryfikować zakończone CI dla `3b1ca58d` (zwłaszcza natywne Windows/Linux oraz test współbieżnego dopisania), a w razie defektu poprawić wyłącznie L1.1.
