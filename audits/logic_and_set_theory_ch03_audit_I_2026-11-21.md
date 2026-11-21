# Rozdział 03 „Zbiory i operacje na zbiorach” — audyt I

**Data:** 21 listopada 2026 r.  
**Źródło:** `/Biblioteka matematyczna/skrypty/logic_and_set_theory/chapters/03-sets-and-operations.tex` (wersja 4).  
**Cel:** weryfikacja poprawności już istniejącego materiału, bez dodawania twierdzeń, lematów, definicji, przykładów i sekcji.

## Usterka w dowodzie i poprawka

1. W dowodzie twierdzenia `thm:relative-complement-families`, dotyczącym `A \setminus \bigcup_i B_i = \bigcap_i(A\setminus B_i)` przy niepustym zbiorze indeksów, zdanie przypisywało potrzebę założenia `I\ne\varnothing` przejściu **od formuły uniwersalnej do przynależności do przecięcia**. To przejście jest poprawne nawet dla pustego `I`, przy przecięciu liczonym względem `U`. **Niepustość jest potrzebna przy poprzednim przejściu**, tj. przy przeniesieniu stałej koniunkcji `x\in A` pod kwantyfikator `\forall i\in I` (odwrotne wyprowadzenie `x\in A` z uniwersalnego warunku zawodzi dla pustego `I`). W tekście poprawiono wskazanie miejsca użycia hipotezy oraz zapisano uzasadnienie obu kroków.
2. W następującej po dowodzie uwadze `rem:empty-relative-intersection-xlii` odróżniono *równoważność formuł przy zmiennej przebiegającej `U`* od *równości zbiorów po zmianie zbioru odniesienia na `A`*. Przy pustym `I` druga równość daje poprawną konwencję przecięcia, ale nie czyni logicznie równoważnymi obu warunków dla wszystkich `x\in U`.

Żaden wzór w tezie twierdzenia nie wymagał zmiany. Wszystkie etykiety i struktura rozdziału pozostały nienaruszone.

## Kontrola matematyczna

Przejrzano 15 twierdzeń i ich 15 dowodów, 8 definicji, 15 przykładów i 8 uwag: zawieranie, ekstensjonalność, sumy i przecięcia, rozdzielność, prawa de Morgana, różnice zbiorów, różnicę symetryczną, zbiory potęgowe, rodziny indeksowane (także puste), granice górne i dolne ciągów zbiorów oraz paradoks Russella. Przeanalizowano przypadki `A=\varnothing`, `U=\varnothing`, `I=\varnothing` i rodzin z powtarzającymi się wartościami.

Test wyczerpujący na `U={0,1,2,3}`: 4096 trójek zbiorów dla działań skończonych, 256 par, 4369 rodzin indeksowanych o długościach 0–3, 69 904 kombinacji rodziny i zbioru `A`, 256 porównań zbiorów potęgowych; dodatkowo 8 wierszy tablicy różnicy symetrycznej, 32 okresowe schematy przynależności w ciągach oraz 1 kontrprzykład dla błędnego przeniesienia koniunkcji pod pusty kwantyfikator. **Łącznie: 78 922 kontrole, wszystkie zaliczone.** Testy mają charakter pomocniczy, nie zastępują weryfikacji dowodów dla dowolnych zbiorów.

Zachowano **15/15 twierdzeń, 15/15 dowodów, 8/8 definicji, 15/15 przykładów, 8/8 uwag, 33/33 etykiety**. Nie dodano żadnego materiału. W rozdziale nie ma zewnętrznych grafik ani plików wykonywalnych: rysunek jest samodzielnym kodem TikZ.

## Kompilacja, odsyłacze i wygląd

- Pełny skrypt obejmujący 44 rozdziały: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 376 stron**. W całym skrypcie **1075 różnych etykiet, 866 odsyłaczy, 0 niezdefiniowanych celów i 0 powielonych etykiet**; brak ostrzeżeń `Overfull \hbox`, 3 nieblokujące `Underfull \hbox` w innych częściach.
- Częściowa książka w układzie repozytorium, z rozdziałami 01–03: kompilacja `latexmk` **kod 0, 30 stron**, bez przepełnionych wierszy. Trzy niezdefiniowane odsyłacze (`ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`) wskazują rozdziały 09, 10, 25, których *jeszcze nie zaimportowano do tej częściowej książki*; w pełnym skrypcie wszystkie trzy są rozwiązane. Nie przemianowano etykiet, żeby ich nie uszkodzić.
- Obejrzano wszystkie **10 stron** wyodrębnionego z pełnego składu PDF rozdziału 03 (strony pliku głównego 32–41), w tym rysunek zbiorów `A∩B`. Nie stwierdzono nachodzenia elementów lub obciętych napisów.

## Status

**Audyt I wykonany, znalezioną usterkę uzasadnienia naprawiono.** Rozdział 03 pozostaje do ponownego audytu przed uznaniem go za stabilny. Bieżący przebieg CI GitHuba po publikacji będzie osobną kontrolą.
