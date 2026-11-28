# Audyt LVI (56) — rozdział 15, selektywny import odsyłaczy zewnętrznych

Data: 2026-11-23. Repozytorium: `dariusz-piekarz/mathematical_scipts`. Gałąź: `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowych gałęzi).
Kanoniczny plik: `chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex`.
SHA bloba treści rozdziału: `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab` — **bez zmian** od audytu LI.
Skrypt regresyjny: `tools/tests/test_measure_theory_ch15_li_gate.py`, blob `7b2ad0a3c6d4e230bcab437984eb7488310543f1` — bez zmian.
Workflow: `.github/workflows/measure-theory-ch15-lii-gate.yml`, nowy blob `4c3884d9ca0773e28239ca61f84a5dd8b4b8aead`.

## Problem

W audycie LV workflow importował do izolowanego PDF **wszystkie** etykiety z pliku `measure_theory.aux` oprócz etykiet lokalnych rozdziału 15. Było to poprawne co do unikania powielania nazw, ale importowało zbędne etykiety i uzależniało powodzenie testu od arbitralnego progu `len(external_labels)>30`. Taki próg nie gwarantuje, że rzeczywiście potrzebne odsyłacze zostały zaimportowane.

## Zmiana

Commit `178f90fa53ebbeafe9c3b47d33f19f9bd3535da8` aktualizuje istniejący workflow:
1. Z kanonicznego źródła rozdziału 15 odczytuje etykiety deklarowane lokalnie oraz nazwy występujące w `ref`, `eqref`, `pageref`, `autoref` i `nameref`.
2. Wylicza dokładnie zbiór zewnętrznych odsyłaczy jako różnicę nazw cytowanych i nazw lokalnych.
3. Z pliku AUX całej książki wybiera tylko wymagane `newlabel`, a nie wszystkie nie-lokalne; brak dowolnej wymaganej etykiety kończy się błędem.
4. Powtórzenie etykiety w AUX dla wymaganych odsyłaczy także kończy się błędem. Zapewnione jest rozdzielenie etykiet lokalnych i importowanych.
5. Usunięto arbitralny próg 30 importowanych etykiet.

W obecnym rozdziale 15 zweryfikowano **17 lokalnych etykiet, 17 odwołań i dokładnie 3 wymagane nazwy zewnętrzne**: `ch:przestrzenie-lp`, `thm:holder-14` i `thm:riesz-fischer-14`.

## Niezależny test lokalny

Na wcześniejszym syntetycznym dokumencie książki z AUX zawierającym trzy etykiety rozdziału poprzedniego i jedną lokalną:
- selekcja poprawnych trzech wymaganych etykiet: PASS;
- usunięcie jednej wymaganej etykiety z AUX powoduje oczekiwany `AssertionError`: PASS;
- powielenie wymaganej etykiety powoduje oczekiwany `AssertionError`: PASS;
- ponowna kompilacja izolowanego dokumentu przez `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -g`: PASS, wynikowy PDF **24 598 bajtów**;
- finalny log syntetycznego PDF nie zawiera `There were undefined references`, `multiply defined` ani `Rerun to get cross-references right`: PASS.

**Granica testu:** sprawdzono algorytm na syntetycznym AUX, nie wykonano pełnej kompilacji 31-rozdziałowej książki. W lokalnym kontenerze brak możliwości pobrania checkoutu `git` z GitHuba z powodu niedostępności DNS.

## Bieżąca bramka

Po ponownym odczycie przez konektor GitHub potwierdzono aktualny blob workflow, trzy wymagane odsyłacze, mechanizmy wykrywania braków/duplikatów, niezmieniony SHA rozdziału i testu.

**Matematyka rozdziału 15: dotychczasowy PASS.**
**Walidacja selekcji odsyłaczy: PASS na modelu syntetycznym.**
**Rzeczywisty wynik GitHub Actions `tests` + `pdf`: NIEPOTWIERDZONY** — nie uzyskano identyfikatora przebiegu z dostępnego interfejsu (listowanie runów ograniczone przez konektor, nieuprawnione wnioskowanie z pustej listy niedopuszczalne).
**Kompilacja całej rzeczywistej książki / wizualny przegląd PDF: NIEPOTWIERDZONE.**
**Status stabilizacji rozdziału 15: OTWARTA TECHNICZNIE.**

Przed przejściem do rozdziału 16 należy zweryfikować rzeczywisty run GitHub Actions dla powyższego commitu lub późniejszego, odczytać jego dwie części oraz artefakty i zamknąć bramkę dopiero po potwierdzonym sukcesie.
