# Iteracja 6 — ciągłość importu geometrii różniczkowej i kontrola odsyłaczy

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zasada:** wyłącznie kod kontrolny i raportowanie, bez zmian kanonicznych `.tex`, historycznych `\label`, `\ref`, `\eqref` oraz bez scalania książek.

## Stan źródeł i wcześniejszych testów

- W `chapters/pl/differential_geometry_and_topology/` są rozdziały `01`–`20` z docelowych `01`–`36`; zatem 16 dalszych rozdziałów oczekuje na import po audycie matematycznym.
- Raport `WDROZENIE_INPUT_SHARED_I_COVERAGE_DG_2026-11-20.md` stwierdzał 17 nierozstrzygniętych wystąpień cytowań w całej migawce oraz 2 cytowania rozwiązane przez `\input` do `shared/pl`. To stan wcześniejszego indeksu, nie nowy wynik po kolejnych commitach.
- Przebieg Actions `44749200502` dla `837fbfda` zakończył się sukcesem.

## Naprawa bramki pokrycia DG

Dotychczas `dg_import_coverage.py` uznawał zakres za pełny, gdy w indeksie było **co najmniej 36** rekordów o prefiksie `DG-`. Sam licznik dopuszczał błędną akceptację zestawu z luką (np. `DG-01`–`DG-35`, `DG-37`). Dodatkowo zestawienie cytowań uwzględniało tylko status `missing`, pomijając potencjalne `ambiguous`.

Aktualnie raport:
1. sprawdza dokładny zbiór identyfikatorów `DG-01`–`DG-36`;
2. podaje `missing_ids`, `unexpected_ids` oraz `not_yet_imported`;
3. ustawia `scope_complete=true` **tylko** dla dokładnie zgodnego zbioru;
4. rejestruje wszystkie statusy cytowań i zachowuje jako nierozwiązane każdy status spoza `resolved`, `external_resolved`, `alias_resolved`, `included_resolved`;
5. zachowuje informację, że nawet komplet identyfikatorów nie dowodzi poprawności matematycznej ani faktycznej kompilacji LaTeX.

Dodano `tests/test_dg_import_coverage.py` z czterema przypadkami: niekompletny import, 36 dokumentów z luką i obcym identyfikatorem, pełne 36 poprawnych dokumentów oraz brakujące/niejednoznaczne odsyłacze z pominięciem prawidłowo rozwiązanych.

## Ograniczenia i kolejka

- **Nie naprawiać automatycznie 17 historycznie nierozwiązanych odsyłaczy.** Dla każdego trzeba zestawić źródłowy kontekst z miejscem docelowym i brakującymi rozdziałami.
- **Gauss–Bonnet i `TS^2`**: trzy wskazane wcześniej cytowania wymagają weryfikacji właściwego twierdzenia (wersja zamknięta/z brzegiem, ewentualnie teoria klas charakterystycznych) i założeń przykładu. Sama zamiana nazwy etykiety może prowadzić do fałszywego uzasadnienia.
- **Rozdziały 21–36**: zaimportować dopiero po ich osobnym audycie; uruchomić ponownie raport DG, audyt pochodzenia odsyłaczy, testy przeglądarkowe i rzeczywistą kompilację książki.
- **Przenoszenie treści i etykiet**: zachować wszystkie pierwotne etykiety i docelowe odsyłacze, sprawdzać także zależności od obrazów, danych i kodu. Nie oznaczać testu parsera jako audytu matematycznego.

Kod i testy tej iteracji są zapisane na tej samej gałęzi; wynik najnowszego CI należy sprawdzić osobno, zanim zostanie uznany za sukces.
