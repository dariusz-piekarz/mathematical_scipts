# Audyt III — rozdział 03 „Zbiory i operacje na zbiorach”

**Data:** 21 listopada 2026 r.  
**Punkt wyjścia:** rozdział 03 po audycie II, zgodny z blobem Git `63ab3e3abf8e2a7d2a3ebc5a8f300b1071a59c5c`.  
**Zakres:** wyłącznie poprawność istniejących definicji, sformułowań, dowodów, przykładów, terminologii, formuł i składu; bez dodawania twierdzeń, lematów, przykładów lub sekcji.

## Wynik kontroli treści

Niezależnie od poprzednich raportów przeanalizowano 15 twierdzeń wraz z 15 dowodami, 8 definicji, 15 przykładów i 8 uwag. Ponownie skontrolowano rozróżnienie `\in` / `\subseteq`, ekstensjonalność, sumę i przecięcie, dopełnienia, prawa de Morgana, prawa rozdzielności, różnicę symetryczną, zbiory potęgowe, rodziny indeksowane, przypadek pustej rodziny, różnicę z dowolną sumą/przecięciem oraz granice dolne i górne ciągów zbiorów.

W sprawdzonym zakresie **nie stwierdzono błędu w tezie ani dowodzie żadnego z 15 twierdzeń**. Zweryfikowano szczególnie przypadki `I=\varnothing`, `U=\varnothing`, `A=\varnothing`, niepustość indeksów w `thm:relative-complement-families`, wzory na monotoniczne ciągi i niezmienniczość granic przy skończonych zmianach.

## Jedyna poprawka — terminologia

Nagłówek istniejącej uwagi „Dlaczego puste przecięcie wymaga otoczenia?” został zmieniony na „Dlaczego puste przecięcie wymaga zbioru odniesienia?”. Słowo „otoczenie” ma odrębne znaczenie w topologii i nie opisuje tutaj potrzebnego zbioru `U`. Treść uwagi, jej położenie i wszystkie wzory pozostały niezmienione. Nie dodano i nie usunięto żadnego środowiska LaTeX ani etykiety.

## Testy i kompilacja

- Testy wyczerpujące na czteroelementowym uniwersum i skończonych rodzinach, a także testy ostatecznie okresowych ciągów zbiorów: **79 971** przypadków zaliczonych (`independent_check.py`). Obejmują też pustą rodzinę i granice mnogościowe; testy nie zastępują dowodów dla wszystkich zbiorów.
- Struktura: **15 twierdzeń, 15 dowodów, 8 definicji, 15 przykładów, 8 uwag i 33 etykiety**; nazwy i kolejność wszystkich etykiet zachowano.
- Pełny skrypt (44 rozdziały): `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — kod `0`, **376 stron**; 1075 unikatowych etykiet, 0 duplikatów, 0 nierozwiązanych odsyłaczy, 0 ostrzeżeń `Overfull \hbox`.
- Wersja repozytoryjna z rozdziałami 01–03: kompilacja `latexmk` — kod `0`, **30 stron**, 0 ostrzeżeń `Overfull \hbox`. Pozostają trzy spodziewane odsyłacze do rozdziałów 09, 10 i 25: `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Wszystkie rozwiązują się w pełnym skrypcie. Nie zmieniano tych etykiet.
- Z wyjściowego PDF wyodrębniono **10 stron** rozdziału 03 (strony 32–41 pełnego pliku) i obejrzano je po ponownym renderingu. Nie stwierdzono nakładających się elementów, obciętych tekstów ani problemów z rysunkiem TikZ.
- Rozdział nie wymaga zewnętrznych plików graficznych ani kodu wykonywalnego.

## Status

**Audyt III zakończony.** Wymagana była tylko pojedyncza poprawka terminologiczna. Matematyczny materiał rozdziału nie został zmieniony. Zgodnie z zasadą końcowego potwierdzenia po każdej poprawce warto wykonać jeszcze jedną iterację audytu III → IV bez rozszerzania materiału, zanim zamkniemy rozdział 03. Po publikacji kontrolujemy osobno wynik GitHub Actions.
