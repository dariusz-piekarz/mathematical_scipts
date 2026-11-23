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
