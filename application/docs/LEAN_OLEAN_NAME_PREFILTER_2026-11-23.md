# Lean — iteracja optymalizacji skanowania artefaktów .olean (2026-11-23)

**Gałąź:** `biblioteka-matematyczna-iteracja-6`
**Zakres:** strumień A (architektura aplikacji), bez modyfikowania kanonicznych `.tex` ani formalizacji `.lean`.

## Kontekst i rezultat

Analiza `application/backend/lean_environment.py::_olean_tree` wskazała dwa drobne źródła narzutu związane z operacjami na każdym pliku kompilacji:

1. Kontrola `Path.is_file()` wykonywała dodatkowy odczyt metadanych po `Path.stat()`. Commit `6af22a40` zastąpił ją sprawdzeniem `stat.S_ISREG(info.st_mode)`, zachowując wcześniejsze i późniejsze porównania tożsamości pliku.
2. W pętli `os.walk` tworzono obiekt `Path` i sprawdzano `.suffix` także dla plików niewchodzących do zbioru artefaktów. Commit `c374171c` wprowadził wczesne filtrowanie nazw przed utworzeniem `Path`. Nazwa `.olean` jest celowo pomijana, ponieważ `Path(".olean").suffix` jest puste; nazwy takie jak `..olean` pozostają uwzględnione.

## Dowody regresyjne

- `application/tests/test_lean_environment.py::test_olean_regular_file_check_reuses_stat_snapshot` — porównanie pełnego wyniku przed i po zmianie przy obu trybach pokrycia oraz wymuszenie błędu przy wywołaniu `Path.is_file()`.
- `application/tests/test_lean_environment.py::test_olean_name_prefilter_matches_path_suffix_for_mixed_build_files` — rzeczywiste pliki na dysku, rozszerzenia podobne do `.olean`, ukryte nazwy, podkatalog i Unicode; porównanie nazw `Path.suffix` i wszystkich SHA256 danych.
- Wcześniejsze regresje pozostają: symlinki, podmiana deskryptora, wzrost pliku, przedwczesny EOF, limit 120000 plików, budżet 64 MiB i metadane poza budżetem.

Nie zmieniono schematu fingerprintu ani trzech punktów kontroli `before/locked/after`. Żadna z tych zmian **nie** certyfikuje dowodu matematycznego, nie zmienia `statement_status` i nie uzasadnia ustawienia `certificate=true`.

## Potwierdzenie i granice

- Zmiany poprzedniej iteracji, commit `0a0b980c`: pełne CI aplikacji [45141855465](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45141855465), szybkie regresje Lean [45141855222](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45141855222) i natywny Windows [45141855355](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45141855355) zakończyły się sukcesem.
- Dla najnowszej zmiany, commit `c64983d7`, uruchomiono [pełne CI aplikacji 45142363332](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363332) oraz [szybkie regresje 45142363338](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363338). **W chwili powstania raportu wynik jeszcze nie był znany**; nie zaliczać tych przebiegów przed końcowym `completed/success`.
- Osobny workflow jądra Lean po wcześniejszych commitach został anulowany w toku kolejnych pushów. Nie przypisywać mu wyniku sukcesu.

## Kolejna iteracja

Po sprawdzeniu powyższego CI wykonać niezależne, powtarzalne porównanie czasów na przypiętym Mathlib, z raportem identyczności fingerprintów i liczby operacji metadanych. Nie wprowadzać cache, redukcji zakresu hashy ani zmian limitów bezpieczeństwa tylko w celu poprawy czasu. Zamknięcie L1.1 wymaga odrębnego rozliczenia testów i pomiarów.

## Kontynuacja: profil liczby nazw bez dodatkowego skanowania (23.11.2026)

- `application/scripts/benchmark_lean_fingerprint.py` zapisuje obecnie `walk_files_seen`, `olean_name_candidates` oraz `non_olean_names_skipped`. Liczniki powstają **wewnątrz już istniejącego** `os.walk`; nie są nowym pełnym obejściem katalogów i nie modyfikują danych zwracanych przez skaner produkcyjny.
- Nowy test tworzy rzeczywiste pliki (7 nazw; 2 kandydatów `.olean`, 5 nazw odrzuconych), porównuje wynik instrumentowanego przebiegu z wynikami nieinstrumentowanego SHA256 i kontroluje faktyczną liczbę otwarć i odczytanych bajtów.
- To **metryka zakresu filtrowania**, a nie bezpośredni pomiar przyspieszenia. Nie wyciągać procentowego zysku czasu na podstawie samych liczników.
- Poprzednia zmiana `c64983d7` przeszła pełne CI aplikacji [45142363332](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363332), Lean-fast [45142363338](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363338) i Windows [45142363458](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363458). Pinned Lean+Mathlib [45142363347](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363347) nie miał jeszcze końcowego wyniku w chwili rozpoczęcia tej iteracji.
- Własne zmiany diagnostyki to commity `b279c518`, `fd58593c`. Ich wyniki CI należy ocenić osobno; nie deklarować stabilizacji przed `completed/success` i porównaniem nowego `ci_fingerprint_benchmark.json` z poprzednim profilem na przypiętym Mathlib.

## Potwierdzenie realnego Mathlib po poprzednim etapie (09:00 UTC, 23.11.2026)

- [Lean + Mathlib #45142363347](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45142363347), SHA `c64983d7`: kroki kompilacji z kontrolą aksjomatów, test rzeczywistego `MetaM` oraz pomiar trzech fingerprintów zakończyły się sukcesem.
- Trzy pełne fingerprinty: `0.513163 s`, `0.495617 s`, `0.500735 s`; mediana `0.500735 s`. Skan `.olean` miał medianę `0.427738 s`.
- Każda próbka obejmowała `1127` katalogów, `352` otwarcia plików `.olean` oraz `67100584` bajty odczytu. `stat_calls=16984`, `lstat_calls=8871`, `fstat_calls=352` w profilerze.
- Podczas weryfikacji nowego licznika, [szybkie testy #45143070328](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45143070328) na SHA `fd58593c` uzyskały `completed/success` dla Linux i Windows. Pełne CI oraz nowe pinned Mathlib dla tego SHA były jeszcze uruchomione; nie przypisywać im sukcesu przed zakończeniem.
- Benchmark poprzedniej optymalizacji wykonano na osobnym runnerze; porównanie samych median między uruchomieniami nie daje wiarygodnego procentowego zysku. Dane zapisano jako bazę do dalszych pomiarów, a nie jako dowód przyspieszenia.
