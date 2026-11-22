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
