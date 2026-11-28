# Audyt II — rozdział 03 „Zbiory i operacje na zbiorach”

**Data:** 21 listopada 2026 r.  
**Punkt wyjścia:** plik `chapters/pl/logic_and_set_theory/03-zbiory-i-operacje-na-zbiorach.tex` z gałęzi `biblioteka-matematyczna-iteracja-6`, treść po audycie I (blob `51e095e62b7c897ab2075bfa2f60ae8e73a0902f`).

## Zakres

Niezależnie przejrzano istniejący materiał rozdziału: 15 twierdzeń wraz z 15 dowodami, 8 definicji, 15 przykładów, 8 uwag; prawa działań skończonych i indeksowanych, przypadek pustej rodziny, zbiory potęgowe, granice mnogościowe, monotoniczność oraz paradoks Russella. Audyt dotyczy **poprawności i precyzji**, nie dodawania nowych stwierdzeń.

## Dwie poprawione luki formalne

1. **Twierdzenie `thm:set-lims` — znaczenie granic zbiorów.** Wcześniejsze brzmienie nie wiązało zmiennej `x` w dwóch równoważnościach dotyczących przynależności do `liminf` i `limsup`. Teraz jawnie określono zbiór odniesienia `U`, ciąg `(A_n)` jego podzbiorów oraz zakres `x∈U` w punktach (i) i (ii). Tezy (iii), (iv) i dowód nie uległy zmianie.
2. **Twierdzenie `thm:monotone-sets` — monotoniczne ciągi zbiorów.** Doprecyzowano hipotezy, jawnie wprowadzając zbiór `U` i ciąg `(A_n)_{n≥1}` jego podzbiorów. Same warunki monotoniczności, obie tezy i dowód pozostały bez zmian.

Nie znaleziono nowego błędu matematycznego w pozostałych tożsamościach ani dowodach. W szczególności hipoteza `I≠∅` w twierdzeniu `thm:relative-complement-families` jest po poprzednim audycie użyta we właściwym miejscu (przeniesienie stałej koniunkcji pod kwantyfikator `∀`, nie definicja przecięcia).

## Testy matematyczne i niezmienniki

- Niezależny test enumeracyjny na wszystkich podzbiorach czteroelementowego uniwersum: 4096 trójek, 256 par zbiorów, 4369 rodzin długości 0–3, 69 904 kombinacji zbioru i rodziny oraz 256 przypadków zbiorów potęgowych. Testy objęły m.in. prawa de Morgana, rozdzielność, łączność różnicy symetrycznej, prawa różnicy i konwencję pustych rodzin.
- Sprawdzono również 930 wzorców ciągów o skończonym prefiksie i okresowym ogonie oraz 160 monotonicznych przypadków. Kontrola objęła semantykę `liminf` / `limsup`, dopełnienia, monotoniczność i odporność na skończone zmiany. **Łącznie 79 971 kontroli, wszystkie zaliczone.** Testy skończone wspomagają audyt, ale nie zastępują dowodów dla dowolnych zbiorów.
- Zachowano wszystkie **15 twierdzeń, 15 dowodów, 8 definicji, 15 przykładów, 8 uwag oraz 33 etykiety**; nie zmieniono żadnej nazwy `\label` ani nie wprowadzono twierdzenia lub lematu.
- Rozdział nie wymaga zewnętrznych plików obrazów ani danych; schemat zbiorów jest zbudowany bezpośrednio w TikZ.

## Kompilacja i walidacja odsyłaczy

- **Pełny skrypt 44 rozdziałów:** `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` zakończył się kodem 0 i wygenerował **376 stron**. We wszystkich rozdziałach znaleziono **1075 etykiet (wszystkie unikatowe)** oraz **866 odsyłaczy (0 niezdefiniowanych celów)**. Brak `Overfull \hbox`; trzy `Underfull \hbox` w pozostałych fragmentach są nieblokujące.
- **Książka repozytoryjna, obecnie z rozdziałami 01–03:** `latexmk` — kod 0, **30 stron**, bez przepełnionych wierszy. Nierozwiązane odsyłacze do `ch:syntax-fol`, `ch:semantics-fol` i `ch:zf-axioms` odnoszą się odpowiednio do niezaimportowanych rozdziałów 09, 10 i 25. Nie zmieniano ich, bo działają w pełnym skrypcie.
- Dokonano oględzin **10 stron** PDF rozdziału 03, w tym nowego składu obu sformułowań. Nie stwierdzono wad składu ani konfliktu napisów z diagramem.

## Status

**Audyt II wykonany.** Dwie poprawki formalnej kompletności sformułowań zostały naniesione i zweryfikowane. Rozdział pozostaje otwarty do kolejnej iteracji audytu, zgodnie z zasadą powtarzania kontroli przed zamknięciem. Po publikacji należy osobno potwierdzić automatyczne kontrole GitHub Actions.