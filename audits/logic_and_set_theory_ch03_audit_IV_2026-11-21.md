# Audyt IV — rozdział 03 „Zbiory i operacje na zbiorach”

**Data:** 21 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/03-zbiory-i-operacje-na-zbiorach.tex` na gałęzi `biblioteka-matematyczna-iteracja-6`, identyczny z blobem Git `cc06948aae17dc6af7980cbfe63389a1b1ade201` po audycie III.  
**Cel:** niezależna, czwarta kontrola wyłącznie obecnego materiału, bez jego rozbudowy.

## Wynik matematyczny

Przejrzano wszystkie **15 twierdzeń, 15 dowodów, 8 definicji, 15 przykładów i 8 uwag**. Sprawdzono sens `\in`, `\subseteq` i ekstensjonalności, przemienność, łączność, rozdzielność, prawa de Morgana, różnice zbiorów i ich brak łączności, różnicę symetryczną, zbiory potęgowe, rodziny indeksowane, prawa de Morgana dla rodzin dowolnych, różnicę względem rodzin, granice mnogościowe i paradoks Russella.

Przeanalizowano w szczególności **pusty zbiór indeksów** i rozróżnienie przecięcia pustej rodziny względem `U` oraz względem `A` w twierdzeniu `thm:relative-complement-families`. Sprawdzono, że założenie `I\ne\varnothing` jest użyte dokładnie przy równoważnym przenoszeniu stałego warunku `x\in A` pod kwantyfikator uniwersalny. Zweryfikowano także przypadki `U=\varnothing`, `A=\varnothing`, wielokrotne wartości rodziny, ciągi monotoniczne, oscylujące oraz skończone modyfikacje ciągów.

**Nie stwierdzono kolejnego błędu ani luki wymagającej poprawki.** Żadna teza, dowód, definicja, etykieta, uwaga ani przykład nie została zmieniona, dodana lub usunięta. Pozostało dokładnie **33 unikatowych etykiet**. Terminologia została sprawdzona pod kątem „suma zbiorów” zamiast „unia”; nie wykryto odstępstw.

## Niezależne kontrole techniczne

- Zgodność źródła z wersją opublikowaną na GitHubie: blob `cc06948aae17dc6af7980cbfe63389a1b1ade201` (`git hash-object` lokalnego pliku). Brak zmian źródła podczas audytu IV.
- Test enumeracyjny na czteroelementowym uniwersum, rodzinach indeksowanych długości od 0 do 3 i ostatecznie okresowych ciągach: **79 971 sprawdzonych przypadków, wszystkie pozytywne**. Testy wspierają audyt, ale nie zastępują dowodów dla dowolnych zbiorów.
- Kompilacja od nowa pełnego skryptu (`latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`): **sukces, 44 rozdziały, 376 stron**. Sprawdzono **1075 różnych etykiet i 866 odsyłaczy**, **bez powielonych etykiet ani brakujących celów**; brak `Overfull \hbox`.
- Kompilacja od nowa książki repozytoryjnej zawierającej rozdziały 01–03: **sukces, 30 stron**, bez `Overfull \hbox`. Pozostają wyłącznie trzy znane odsyłacze do jeszcze niezaimportowanych do częściowej książki rozdziałów 09, 10, 25: `ch:syntax-fol`, `ch:semantics-fol` i `ch:zf-axioms`; wszystkie są rozwiązane w skrypcie pełnym.
- Wyodrębniono 10 stron rozdziału 03 z pełnego PDF i ponownie renderowano wszystkie strony; kontrola układu, wzorów i rysunku TikZ nie wykazała kolizji ani obcięć.
- Rozdział nie ma zależności od zewnętrznych plików graficznych, kodu wykonywalnego ani dodatkowych plików wejściowych.
- Poprzedni przebieg GitHub Actions dla ostatniej **zmiany treści** rozdziału 03 zakończył się sukcesem: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44905198887.

## Decyzja

**Audyt IV zaliczony bez zmian. Rozdział 03 zamknięty jako stabilny.** Na GitHub trafia wyłącznie raport audytu, bez nowego commitu modyfikującego plik `.tex`. Kolejny rozdział do audytu: 04 — „Pary uporządkowane i relacje”.
