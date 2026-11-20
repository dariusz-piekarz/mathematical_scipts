# Biblioteka matematyczna — importy `\input`, `shared/pl` i zakres geometrii różniczkowej

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** parser, SQLite, API, testy regresyjne i kontrola zakresu importu. Nie modyfikowano kanonicznych rozdziałów LaTeX.

## Wdrożenie

1. `application/backend/included_labels.py` analizuje literalne `\input{...}` widoczne poza komentarzami i otoczeniami dosłownymi. Ścieżki rozwiązuje względem katalogu kompilacji `books/pl`, w granicach repozytorium. Obsługuje pliki zagnieżdżone, ograniczenie głębokości oraz cykle przez zbiór odwiedzonych plików.
2. Schemat indeksu SQLite **v4** dodaje tabelę `included_label_origins`: rozdział cytujący, oryginalna nazwa etykiety, faktyczna ścieżka do pliku `shared`, linia, przesunięcie i fragment. Nie dopisuje etykiet jako fikcyjnych, lokalnych deklaracji w kanonicznym rozdziale.
3. Statyczny resolver przy jednoznacznym imporcie stosuje nowy status `included_resolved`, a `reference_provenance_audit.py` nie zalicza go do nierozstrzygniętych. Złożone lub niejednoznaczne przypadki nie są automatycznie zgadywane.
4. `GET /api/labels/{label}?source_document=ALG-10` może wskazać faktyczny plik w `shared/pl` i jego linię. Czytnik przekazuje kontekst rozdziału cytującego.
5. `application/scripts/dg_import_coverage.py` automatycznie liczy zaimportowane rozdziały `DG-*`, porównuje je z **36** rozdziałami pełnego skryptu oraz zapisuje nadal nierozstrzygnięte odsyłacze. Odpowiedni plik JSON dołączany jest do artefaktu audytu CI, więc po przyszłym imporcie zakres zostanie sprawdzony ponownie.

## Wyniki na aktualnej migawce

| Miara | Wynik |
|---|---:|
| Rozdziały w indeksie | 355 |
| Rozpoznane wystąpienia etykiet z importowanych źródeł | 12 |
| Odsyłacze rozwiązane przez `\input` | 2 |
| Nierozstrzygnięte w aktualnym indeksie | **17** |
| Niejednoznaczne | **0** |
| Odsyłacze międzytomowe `xr-hyper` | 72 |

Dwie naprawione pozycje należą do `ALG-10`:
- `tw:ga10-weak` — `shared/pl/slabe_twierdzenie_lefschetza.tex`, linia 10;
- `thm:xvii-blowup` — `shared/pl/rozdmuchanie_punktu_kohomologia.tex`, linia 10.

W obu przypadkach zachowano dodatkowe historyczne etykiety oraz oryginalne instrukcje `\input`. Rozdział `ALG-10` nie został przepisany.

## Warunki bezpieczeństwa i ograniczenia

Parser pozostaje **statyczny**: nie wykonuje makr ani warunków TeX-a. Weryfikacja, że ścieżka `\input` i etykieta istnieją w pliku, nie jest dowodem, że wszystkie gałęzie `\if...` wystawią daną etykietę w każdym możliwym złożeniu książki. Decydujący pozostaje test rzeczywistej kompilacji konkretnej książki.

Pełna geometria różniczkowa ma 36 rozdziałów; na obecnej gałęzi jest pierwszych 20. Pozostałych **16** nie dopisywano, bo trwa ich osobny audyt. Odsyłacze do Cherna–Weila, teorii Hodge'a, Bochnera i operatora Diraca nadal wymagają weryfikacji po dołączeniu brakującego materiału. Trzy odwołania do wersji Gaussa–Bonneta *z brzegiem* użyte dla `TS^2` wymagają osobnej korekty matematycznej w planowanym audycie źródeł — samo dodanie przyszłego rozdziału nie uzasadnia tych cytowań.

## Testy

- `application/tests/test_included_labels.py`: rzeczywisty plik `shared`, ścieżka i linia pochodzenia, brak fikcyjnych `\label` w rozdziale, ignorowanie komentarzy, nieistniejący import i cykl.
- `application/tests/test_api.py`: kontekstowe wyświetlenie `ALG-10 -> shared/pl` i pochodzenia cytatu.
- GitHub Actions: przebudowa indeksu, raport 17 nierozstrzygniętych, testy aplikacji i smoke testy w Chromium.
- Skrypt pokrycia 36 rozdziałów DG został dodany do CI; nie oznacza to, że niezaimportowane 16 rozdziałów już zweryfikowano matematycznie.

**Bez zmian:** `chapters/pl/`, oryginalne `\label`, `\ref`, `\eqref`, `main`; bez scalania skryptów.