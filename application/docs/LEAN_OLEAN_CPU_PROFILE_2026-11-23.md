# Lean L1.1 — profil CPU prawdziwego skanowania .olean (2026-11-23)

**Strumień:** A — architektura aplikacji Atlas. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Stan wejściowy

- Poprzednia zmiana benchmarku `51e67723` otrzymała poprawne szybkie testy Linux/Windows [#45143635852](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635852), pełne testy aplikacji [#45143635752](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635752), a przypięty Lean+Mathlib i audyt aksjomatów [#45143635766](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143635766) zakończyły się `completed/success`.
- Rzeczywisty pomiar po filtrze nazw (SHA `fd58593c`, [#45143070388](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143070388)): 85 022 nazw, 7 732 kandydatów .olean, 77 290 odrzuconych nazw (90,9%); brak wiarygodnego sparowanego porównania czasu przed/po na tym samym runnerze.
- Podstawowy benchmark `benchmark_lean_fingerprint.py` mierzy trzy faktyczne pełne fingerprinty. Każde odczytanie pliku pozostaje limitowane pierwotnymi zabezpieczeniami produkcyjnymi.

## Implementacja

Dodano `application/scripts/profile_lean_olean_cpu.py`:

- `profile_olean_cpu(lean_root, limit=12)` używa istniejącej walidacji wejścia benchmarku, a następnie uruchamia **dokładnie jeden** prawdziwy `compiled_artifacts_sha256(lean_root)` pod kontrolą `cProfile`.
- Zapisuje wynik SHA256, listę maksymalnie 20 funkcji posortowaną według łącznego czasu wykonywania, liczniki wywołań i wartość `certificate=false`.
- Nie korzysta z imitacji haszowania; wyjątki rzeczywistej kontroli integralności są propagowane. Nie wykonuje drugiego przejścia po katalogach ani nie zapisuje stanu formalizacji.
- Wyniki `cProfile` służą do znajdowania hotspotów, nie do porównania z bezprofilowanym `perf_counter`. Sam profiler dodaje narzut.

Uruchomienie w zaufanej kopii repozytorium:

```bash
cd application
python scripts/profile_lean_olean_cpu.py --top 12 --output lean/ci_olean_cpu_profile.json
```

## Testy i CI

- `application/tests/test_lean_olean_cpu_profile.py` porównuje prawdziwy digest przed i po profilowaniu; zapewnia dokładnie jedno produkcyjne wywołanie, brak zmian w plikach, walidację parametrów, odmowę przy błędnym źródle i przy symlinku .olean.
- Szybki workflow uruchamia testy na natywnych Linux i Windows. [#45144394316](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45144394316) zakończył się `completed/success`.
- Przypięty workflow Lean 4.26.0/Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` wywołuje profiler po rzeczywistym benchmarku, zapisując `application/lean/ci_olean_cpu_profile.json` do artefaktów workflow.
- W chwili dopisania dokumentacji nie odnotowano jeszcze zakończonego pozytywnie CI całego nowego przebiegu profilera; nie nazywać L1.1 zamkniętym do czasu sprawdzenia.

## Kolejny punkt kontrolny

1. Zweryfikować pełny nowy przebieg CI Lean/Mathlib, opublikowany JSON i kompletną listę hotspotów.
2. Sprawdzić regresje Windows i realną kompilację; zachować odniesienie do konkretnego SHA.
3. Dalsze optymalizacje podejmować na podstawie hotspotów i równoważności fingerprintu, a nie wyłącznie czasu.
4. Bez zmian dla `certificate=false` bez rzeczywistej, aktualnej kompilacji i niezależnej kontroli semantycznej przekładu LaTeX.

## Kontrola rzeczywistego profilera i nowa optymalizacja (23.11.2026)

**Dane z realnego CI:** [pinned Lean 4.26.0 + Mathlib #45144415733](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45144415733), commit `aecd94e7`, zakończony `completed/success`. Profil `cProfile` zawierał 2 116 775 wywołań i `profiled_seconds=0.737163`. Wśród funkcji o największym czasie kumulacyjnym znalazły się: `_olean_tree` (10 wywołań; 0.724415 s), `Path.relative_to` (7 732; 0.313158 s), `Path.stat` (16 984; 0.175563 s), `Path.is_symlink` (8 871; 0.150315 s). Czasy kumulacyjne nachodzą na siebie. To **czas profilowanego wykonania**, nie efekt nowej optymalizacji.

**Hipoteza:** największy łatwy do usunięcia koszt poza kontrolami bezpieczeństwa pochodzi z `Path.relative_to(root)` wykonywanego dla każdej nazwy `.olean`. W skanowaniu mamy 1127 katalogów i 7732 kandydatów; wykonanie tej operacji raz na katalog zawierający kandydata powinno ograniczyć liczbę wywołań bez zmiany przetwarzanego zbioru.

**Zmiana `b1bd6db7`:** produkcyjny `_olean_tree` zapisuje względną nazwę katalogu raz na katalog z przynajmniej jednym kandydatem `.olean`, a następnie łączy ją z nazwą zwróconą przez `os.walk`. Nie stosuje `resolve()`, nie podąża za symlinkami i nie zmienia kolejności ani metadanych. Osobny test `5cf01379` sprawdza dla plików w katalogu głównym i zagnieżdżonym dokładnie dwa wywołania `relative_to` zamiast pięciu, poprawność nazw Unicode i brak wywołań w katalogu bez kandydatów. Istniejący test porównawczy przeciw poprzedniemu algorytmowi pozostaje w zestawie.

**Kontrola między profilerami:** komity `dcb7169f`, `ea43fc19`, `42addf18`, `55db1c06`, `6128cf9e` pozwalają zapisać wynik `compiled_artifacts_sha256` z oryginalnego pełnego benchmarku, porównać go z **pojedynczym rzeczywistym** przebiegiem `cProfile` i odrzucić wynik, jeżeli pliki `.olean` zmieniły się między pomiarami. Porównanie to nie dodaje kolejnego haszowania ani certyfikatu matematycznego. Nowy workflow używa `--compare-with lean/ci_fingerprint_benchmark.json`.

**Bramka:** po zmianie produkcyjnej należy uzyskać testy Linux/Windows, pełne CI, rzeczywisty pinned Mathlib, raport o identycznych digestach, a dopiero potem ocenić ewentualne przyspieszenie na sparowanym pomiarze. Nie obniżać limitów 64 MiB, 120000 plików ani liczby punktów kontroli `before/locked/after`. `certificate=false` niezmiennie.

## Niezależna regresja pełnego fingerprintu — projekt i Mathlib (23.11.2026)

Dodano `application/tests/test_lean_environment.py::test_olean_multiroot_digest_matches_independent_expected_schema` (`41d60ad9`, uzupełnienie importu `4aa3f8fd`). Regresja tworzy rzeczywiste pliki i metadane OS w drzewie projektu oraz pakietu Mathlib, z nazwami podkatalogów, plikami wyłączonymi przez filtr i **wspólnym** budżetem SHA256 ograniczonym do trzech bajtów. Oczekiwany JSON i jego SHA256 są budowane niezależnie od produkcyjnego skanera; porównanie dotyczy **całego** `compiled_artifacts_sha256`, nie tylko poszczególnych nazw.

Ten test uzupełnia test zgodności z poprzednim algorytmem (różne budżety, Unicode, kolejność pól) oraz test policzalnej redukcji wywołań `Path.relative_to`. Celem jest wykrycie regresji w kolejności sortowania, dzieleniu budżetu między projekt i pakiety lub nazwach względnych. Zmian produkcyjnych nie wprowadzono w tej poditeracji.

**Wynik nowego testu pozostaje zależny od zakończenia CI.** Do czasu potwierdzenia CI na jego commicie nie podnosić statusu stabilizacji L1.1. Pomiary z wcześniejszego, rzeczywistego profilera pozostają ważne wyłącznie dla commita, na którym je uruchomiono.

## Wynik niezależnego testu projektu i Mathlib (23.11.2026)

- Pierwszy przebieg nowego testu na commicie `41d60ad9` zakończył się błędem **wyłącznie testowym** `NameError: name 'json' is not defined`, potwierdzonym osobno w Linux i Windows ([CI #45145944311](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145944311)). Nie był to błąd produkcyjnego fingerprintu.
- Dodano brakujący import w commicie `4aa3f8fd` i uruchomiono testy ponownie. [Szybki Lean CI #45145976138](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145976138) zakończył się `completed/success` zarówno dla Linux, jak i natywnego Windows. Logi obu zadań jawnie potwierdzają `test_olean_multiroot_digest_matches_independent_expected_schema ... ok`.
- [Windows Job Objects #45145976141](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145976141) na tym samym SHA również zakończył się sukcesem.
- Pełne CI aplikacji i nowy przypięty Lean+Mathlib na `4aa3f8fd` **nie miały potwierdzonego zakończenia** podczas tej kontroli. Wynik poprzedniego profilera `aecd94e7` jest potwierdzony, ale nie dowodzi jeszcze przyspieszenia najnowszej produkcyjnej optymalizacji `b1bd6db7`.

**Wniosek:** test niezależnej budowy SHA256 całego drzewa projekt/pakiety działa poprawnie na dwóch systemach, a wymaganie zamknięcia L1.1 nadal obejmuje realny pinned Mathlib i pełny CI na bieżącym kodzie.

## Parowany mikrobenchmark `relative_to` na tym samym runnerze (23.11.2026)

**Wynik poprzedniego pełnego Lean CI:** [#45145379315](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145379315) na `5cf01379` zakończony sukcesem, w tym kompilacja przypiętego Mathlib, kontrola aksjomatów, introspekcja i wszystkie trzy odciski oraz profil CPU. Po optymalizacji `b1bd6db7` mediana pełnego fingerprintu to `0.402131 s`, a części `.olean` `0.334226 s`; `cProfile` zarejestrował `1112269` wywołań. Wcześniejszy profil (SHA `aecd94e7`) wykazał `2116775` wywołań. Porównanie między runnerami jest przesłanką poprawy, ale **nie wiarygodnym pomiarem względnego zysku czasowego**.

**Nowe narzędzie:** `application/scripts/benchmark_lean_paths.py` zbiera jeden niepodążający za symlinkami zestaw nazw `.olean` w drzewach projektu i pakietów; odtwarza starą konwersję `(base / name).relative_to(root)` i nową konwersję z jednym `base.relative_to(root)` na katalog. Sprawdza pełną zgodność uporządkowanych par `(label, relative_name)`, a następnie naprzemiennie mierzy oba algorytmy na **tym samym zestawie nazw i runnerze**. Nie odczytuje zawartości `.olean` ani nie zastępuje produkcyjnej kontroli integralności.

**Zakres metryki:** zmierzony czas dotyczy **wyłącznie tworzenia nazw względnych**, bez skanowania katalogów, walidacji plików i SHA256. Wyniki muszą być opisane jako mikrobenchmark, a nie całkowity zysk w fingerprintingu. Dodatkowy warunek `--compare-with` wymaga, by liczba kandydatów była zgodna z wcześniejszym raportem prawdziwego fingerprintu na tym samym runnerze.

**Testy:** `application/tests/test_lean_paths_benchmark.py` sprawdza zgodność obu sposobów konwersji dla podkatalogów, Unicode, plików ukrytych i pakietu Mathlib, niezmienność plików, redukcję liczby wywołań `relative_to`, reakcję na zmianę populacji oraz odmowę przy symlinku. Testy są podłączone do Linux i Windows, a parowany benchmark do przypiętego Lean+Mathlib w `.github/workflows/lean-formalization.yml`.

**Commity tej poditeracji:** `0ac3c9e5` (narzędzie), `9d89afaf` (testy), `54cfeb95` (CI Linux/Windows), `1a7b9e9a` (realny Mathlib). W momencie opracowania raportu wyniki tych zmian pozostają do zweryfikowania. Funkcje produkcyjne fingerprintu i certyfikacja matematyczna nie zostały zmienione.

## Audyt porównania z raportem pełnego fingerprintu (23.11.2026)

**Potwierdzenie etapu wejściowego:** [pełne CI aplikacji #45146976963](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146976963) dla `39681861` zakończone `success`. [Szybkie CI Linux/Windows #45146885940](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146885940) zakończone `success`. Realny [pinned Mathlib #45146914480](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146914480) nadal pozostawał aktywny w momencie rozpoczęcia tej iteracji; nie ma jeszcze podstaw do podania wyniku mikrobenchmarku.

**Nowa kontrola danych wejściowych:** `benchmark_lean_paths.py::expected_candidates_from_benchmark` weryfikuje strukturę poprzedniego raportu przed użyciem liczby kandydatów do mikrobenchmarku. Wymaga jawnego celu raportu, `certificate=false`, poprawnego SHA256 artefaktów, liczby próbek w zakresie, dokładnie określonych liczników nieujemnego typu `int` (odrzuca `bool`), niezmienności próbek oraz równości `walk_files_seen=olean_name_candidates+non_olean_names_skipped`. Odrzuca dane niepełne i sprzeczne; nie uruchamia ponownie fingerprintu i nie zmienia produkcyjnego skanera.

**Regresje:** `test_compare_with_rejects_corrupted_fingerprint_evidence` tworzy rzeczywisty pełny raport dla lokalnej poprawnej struktury bez pakietów i weryfikuje scenariusze brakujących pól, fałszywego certyfikatu, uszkodzonego SHA, nienumerycznych i zmienionych liczników. Pierwszy CI testu `60cbbbb3` wykrył poprawną odmowę skanera dla **sztucznego katalogu Mathlib, który nie był Git checkoutem**; porównanie schematu błędnie zakładało, że da się z takiej fikstury zbudować realny pełny raport. Commit `95508306` wydzielił do testu poprawną fiksturę bez niezweryfikowanej zależności. Nie osłabiono wymogu czystego repozytorium Git dla realnego Mathlib.

**Commity:** `7d4bac2e` (walidacja), `60cbbbb3` (regresje), `95508306` (poprawka fikstury). W chwili zapisu potwierdzenie pełnego CI tych commitów było w toku; **nie należy przedstawiać ich jako zaliczonych przed końcowymi statusami**. Kryteria L1.1 pozostają te same: realne Lean, Mathlib, zgodność fingerprintów, oddzielny status semantyki twierdzenia, a wszystkie raporty diagnostyczne `certificate=false`.
