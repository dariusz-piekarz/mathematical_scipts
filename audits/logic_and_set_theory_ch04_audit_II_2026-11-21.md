# Audyt II — rozdział 04 „Pary uporządkowane i relacje”

**Data:** 21 listopada 2026 r.  
**Wersja źródłowa:** `chapters/pl/logic_and_set_theory/04-pary-uporzadkowane-i-relacje.tex`, gałąź `biblioteka-matematyczna-iteracja-6`, stan po audycie I (blob Git `11934c15ec626f8525eb29326d601c9f2e7aba8d`).  
**Zakres:** ponowny audyt całego istniejącego materiału, bez dopisywania twierdzeń, lematów, definicji ani przykładów.

## Usterki znalezione i naprawione

1. **Nieokreślony zbiór `C` w twierdzeniu o relacjach identycznościowych i odwracaniu składania** (`thm:relation-identities`). Po ustaleniu zbiorów `A`, `B` i relacji `R⊆A×B`, druga część twierdzenia używała dodatkowo `S⊆B×C` bez określenia, czym jest `C`. Dodano wprost: „Jeżeli dodatkowo `C` jest zbiorem i `S⊆B×C`, to…”. Treść równości `(S∘R)^{-1}=R^{-1}∘S^{-1}` i jej dowód były poprawne, nie zostały zmienione.
2. **Nieokreślony zbiór `C` w przykładzie macierzowym** z sekcji „Relacje a macierze zero-jedynkowe”. Występowały `S⊆B×C` i macierz `M_S`, choć wcześniej wprowadzono tylko skończone `A` i `B`. Jawnie wprowadzono skończony, wyliczony zbiór `C={c_1,…,c_p}`. Wzór na boolowski iloczyn macierzy oraz przykład numeryczny pozostały bez zmian.

To jedyne różnice w pliku rozdziału względem wersji po audycie I: dwa lokalne uzupełnienia założeń, bez zmian treści matematycznych. Zachowano wszystkie oryginalne etykiety, oznaczenia, kolejność twierdzeń i wszystkie odsyłacze.

## Kontrola matematyczna

Przeczytano ponownie wszystkie **12 twierdzeń, 3 lematy, 15 dowodów, 11 definicji, 17 przykładów i 6 uwag**. Sprawdzono dowód jednoznaczności kodowania Kuratowskiego, istnienie i monotoniczność iloczynu kartezjańskiego, równoważność jednoznaczności włókien i zachowania przecięć, kolejność składania, odwracanie relacji, charakterystyki własności relacji, potęgi relacji, minimalność domknięć, generowanie najmniejszej relacji równoważności oraz macierzowe kodowanie relacji. Szczególną uwagę zwrócono na puste zbiory i relacje, niewypełnione dziedziny i kodowanie macierzy o zerowej liczbie wierszy lub kolumn. Nie znaleziono błędu w tezie ani przejściach dowodowych istniejących twierdzeń i lematów.

Przeprowadzono ponownie **187 714** niezależnych kontroli enumeracyjnych z audytu I (`independent_check.py`), wszystkie zaliczone. Dodatkowo własny test przypadków brzegowych macierzowego składania i odwracania relacji na skończonych zbiorach o rozmiarach 0–2 sprawdził **499 par relacji** w **27 konfiguracjach rozmiarów**, w tym przypadki pustych zbiorów. Wszystkie testy zaliczono. Testy skończone nie zastępują dowodów dla dowolnych zbiorów.

## Kompilacja i odsyłacze

- Pełny skrypt: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0**, 44 rozdziały, **376 stron**. W całym skrypcie 1075 różnych etykiet i 866 odsyłaczy; **0 zdublowanych etykiet, 0 brakujących celów, 0 `Overfull \hbox`**.
- Książka repozytoryjna z zaimportowanymi rozdziałami 01–04: `latexmk` — **kod 0, 41 stron**, bez `Overfull \hbox`. W tej częściowej wersji istnieją jeszcze odsyłacze do rozdziałów 07, 09, 10 i 25 (`ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`). Cele te istnieją w pełnym skrypcie; zachowano ich etykiety.
- Oryginalne **35 etykiet** rozdziału nie zostało zmienionych; zachowano wszystkie istniejące środowiska (12 twierdzeń, 3 lematy, 11 definicji, 17 przykładów, 6 uwag, 15 dowodów).
- Wyrenderowano i obejrzano wszystkie **10 stron** rozdziału (strony 42–51 pełnego składu). Oba diagramy TikZ i poprawione zapisy są czytelne; nie stwierdzono nałożeń, obcięć ani błędów układu. Rozdział nie ma zależności od zewnętrznych obrazów lub plików kodu.

## Status

**Audyt II zakończony: dwie luki w deklaracji obiektów naprawione, matematyka i kompilacja sprawdzone.** Rozdział 04 pozostaje otwarty do kolejnej iteracji, ponieważ audyt wykrył rzeczywiste braki formalne. Po wypchnięciu poprawek na GitHub osobno sprawdzić testy CI (parser, indeks, testy aplikacji oraz Chromium). Nie dodano nowych twierdzeń ani lematów.
