# Audyt I — rozdział 05 „Relacje równoważności i zbiory ilorazowe”

**Data:** 21 listopada 2026 r.  
**Źródło:** `/Biblioteka matematyczna/skrypty/logic_and_set_theory/chapters/05-equivalence-relations-and-quotients.tex`, wersja 5, przed importem do repozytorium `dariusz-piekarz/mathematical_scipts`.  
**Zakres:** wyłącznie szczegółowy audyt istniejących definicji, twierdzeń, wniosku, dowodów, przykładów, odsyłaczy i redakcji. Nie dodano twierdzeń, lematów, definicji, przykładów ani sekcji.

## Wykryte i poprawione kwestie

1. **Samodzielność sformułowań matematycznych.** W definicji klasy równoważności i nasycenia, w twierdzeniach o równości klas, zawieraniu klas, przecięciu równoważności, relacji generowanej, charakteryzacji nasycenia i działaniach na ilorazie oraz w powiązanym wniosku i definicji relacji drobniejszej uzupełniono deklarację zbioru `X` (w razie potrzeby także zbioru indeksów `I` i zakresu zmiennych `x,y`). Wcześniejsze sformułowania opierały się na kontekście sąsiednich akapitów, chociaż powinny być poprawne samodzielnie.
2. **Dowód twierdzenia o przecięciu i najmniejszym wspólnym rozszerzeniu**, `thm:eq-meet-join-xliii`, uzasadniał największość przecięcia i minimalność równoważności generowanej, ale nie uzasadniał ostatniej części tezy — że `E ∪ F` nie musi być przechodnia. W dowodzie jawnie wskazano **już istniejący** kontrprzykład `ex:eq-union-not-equivalence-xliii` następujący po nim; nie dodano nowego przykładu.
3. **Dowód twierdzenia o nasyceniu jako najmniejszym domknięciu**, `thm:eq-saturation-closure-xliii`, nie odsyłał do uzasadnienia ostatniej części tezy (brak zachowania przecięć). Dodano odsyłacz do **już istniejącego** przykładu `ex:eq-sat-intersection-xliii` bez zmiany jego zawartości.
4. **Relacja równoważności generowana przez `R`.** W sformułowaniu kryterium ścieżkowego jawnie zapisano, że chodzi o `x,y∈X`, długość łańcucha `n≥0` (włącznie ze ścieżką długości zero) oraz zakres `j=1,…,n`. Nie zmieniono tezy.
5. **Twierdzenie o działaniach na ułamkach**, `thm:eq-fraction-operations-xliii`, powoływało się na relację „z poprzedniego przykładu” bez samodzielnego określenia jej wzorem. W samym twierdzeniu zapisano `(p,q)∼(r,s) ⇔ ps=rq` oraz zakres par należących do `D`. Dowód nie wymagał zmiany.
6. **Twierdzenie o podziałach**: doprecyzowano zakres `x,y∈X` we wzorze określającym relację na podstawie podziału.
7. **Końcowa zapowiedź** sugerowała, że własność uniwersalna odwzorowania ilorazowego zostanie dopiero udowodniona w rozdziale o funkcjach, chociaż dowód znajduje się już w `thm:lxv-quotient-factorization`. Poprawiono odesłanie, zachowując treść przyszłej zapowiedzi zastosowań.

## Szczegółowe kontrole matematyczne

Przeanalizowano wszystkie **11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów i 5 uwag**. Sprawdzono relację równoważności także na `X=∅`, klasy i podziały zbioru pustego, równoważności generowane przez relacje, zbiory nasycone, domknięcia nasyceniowe, niezależność od reprezentantów działań, własność uniwersalną ilorazu bez stosowania aksjomatu wyboru oraz poprawność konstrukcji liczb wymiernych z par całkowitych z niezerowym mianownikiem. Wszystkie tezy i dowody są matematycznie poprawne po powyższych doprecyzowaniach. Nie wprowadzono nowych twierdzeń ani lematów.

Niezależne testy enumeracyjne (`independent_check.py`) na uniwersach o rozmiarach 0–4, wszystkich podziałach takich zbiorów, wybranych i wyczerpująco analizowanych relacjach, funkcjach i działaniach oraz parach liczb całkowitych z mianownikami dodatnimi i ujemnymi: **23 542 kontrole zakończone powodzeniem**. Podział m.in.: 4 197 przypadków sum i przecięć nasyceń, 2 303 przypadki minimalności relacji generowanej, 8 983 sprawdzenia zgodności działań z ilorazem, 5 184 przypadki niezależności działań ułamkowych od reprezentantów. Skończone testy wspomagają, ale nie zastępują kontroli dowodów ogólnych.

Zachowano **29/29 istniejących etykiet** bez zmiany ich nazw, kolejności ani liczby środowisk: 11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów, 5 uwag. Zmieniono wyłącznie uzasadnienia, deklaracje i drobne zapisy. Wszystkie istniejące odsyłacze nadal są poprawne.

## Kompilacja, odsyłacze, rysunki

- Pełny skrypt, **44 rozdziały**: świeża kompilacja `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`, kod `0`, **376 stron**, **1075 unikatowych etykiet**, zero ich duplikatów, zero odsyłaczy do nieistniejących etykiet, zero `Overfull \hbox`; trzy nieblokujące `Underfull \hbox` w pełnym składzie.
- Książka repozytoryjna z zaimportowanymi rozdziałami **01–05**: świeża kompilacja `latexmk` zakończona kodem `0`, **50 stron**, bez `Overfull \hbox`. Odsyłacze `ch:orders`, `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms` oczekują dopiero na import rozdziałów 06, 07, 09, 10, 25; są rozwiązane w pełnym skrypcie. Nie przemianowano etykiet.
- Wyodrębniono i obejrzano **9 stron** rozdziału 05 (strony 52–60 pełnego składu), w tym geometryczny rysunek TikZ klas równoważności. Nie zaobserwowano obciętych napisów ani zachodzących na siebie elementów.

## Status

**Audyt I rozdziału 05 wykonany.** Stwierdzono i naprawiono luki w samodzielności założeń oraz niepełne odwołania do kontrprzykładów. Istniejący zakres merytoryczny nie został rozszerzony. **Rozdział pozostaje otwarty do audytu II** zgodnie z przyjętym trybem. Kontrola GitHub Actions po integracji jest oddzielnym etapem.
