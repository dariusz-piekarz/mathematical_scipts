# Audyt I — rozdział 07 „Funkcje: jednoznaczność przyporządkowania”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** istniejący plik Biblioteki matematycznej `/Biblioteka matematyczna/skrypty/logic_and_set_theory/chapters/07-functions-and-mappings.tex` (22 411 bajtów), zgodny z historią audytu XLIV z 20 listopada.  
**Zakres:** pierwsza niezależna iteracja audytu istniejącego rozdziału 07 i jego bezstratne przeniesienie do modularnej książki na GitHubie; nie dodano wyników ani przykładów.

## Wykonane zmiany redakcyjno-formalne

1. W twierdzeniu o liczbie funkcji jawnie wprowadzono liczby naturalne `n,m` i ich równość z mocami skończonych zbiorów.
2. W twierdzeniu o włóknach, twierdzeniu o funkcji odwrotnej, o odwrotnościach jednostronnych i kryterium wykresu wskazano jawnie zbiory `A,B` i funkcję/relację, do której stosuje się twierdzenie.
3. W dokładnym kryterium odwrotności lewostronnej oddzielono warunek iniekcyjności od alternatywy `A ≠ ∅ lub B = ∅`. Nie zmieniono przesłanek ani tezy merytorycznej.
4. W sformułowaniu aksjomatu wyboru dodano jawne kwantyfikowanie zbioru indeksów `I`; dotychczasowa konstrukcja przekroju i dowód równoważności pozostały bez zmian.

Nie dodano ani nie usunięto żadnego środowiska twierdzenia, definicji, przykładu, uwagi ani rysunku. Zachowano wszystkie 14 etykiet rozdziału.

## Niezależny przegląd matematyczny

Ponownie sprawdzono **11 twierdzeń, 11 dowodów, 5 definicji, 10 przykładów, 9 uwag oraz jeden diagram TikZ**. Kontrolowano:
- funkcję jako relację z ustaloną dziedziną i przeciwdziedziną, istnienie `B^A` w ZF przez potęgowanie i wyróżnianie;
- istnienie funkcji dla pustej dziedziny i przeciwdziedziny, `0^0=1` w konwencji liczby funkcji oraz indukcyjne liczenie `|B^A|`;
- równoważność iniekcji i jednoelementowości lub pustki włókien, analogiczne kryterium surjekcji i podział dziedziny na włókna, także dla `A=∅`;
- definicję funkcji stałej dla `∅→∅` oraz funkcje charakterystyczne `χ_S`;
- konstrukcję funkcji odwrotnej, precyzyjne kryterium odwrotności lewostronnej, przekrój surjekcji na skończoną przeciwdziedzinę;
- równoważność aksjomatu wyboru i istnienia przekroju każdej surjekcji, zwłaszcza rozłączną sumę `{(i,x):i∈I,x∈X_i}` i indeksy pustej rodziny.

**Wynik:** brak wykrytego fałszywego twierdzenia lub wadliwego dowodu. Siedem miejsc poprawiono wyłącznie pod względem jawności założeń i języka.

## Kontrole niezależne i integralność

W bieżącej iteracji niezależnie wyliczono **499 funkcji** pomiędzy zbiorami o co najwyżej czterech elementach, w tym przypadki puste, sprawdzając liczności, włókna, własności injekcji i surjekcji, odwrotności lewostronne/prawostronne i obustronne: **0 kontrprzykładów**. Sprawdzono także bijekcję `P(A) ↔ {0,1}^A` dla `|A| ≤ 4`. Regresje włączono do `tools/tests/test_logic_and_set_theory_ch07.py`; testy skończone nie zastępują dowodów ogólnych.

Po imporcie rozdziałów 01–07 książka ma **223 unikatowe etykiety**, **86 wystąpień odsyłaczy** oraz dokładnie **4 odsyłacze w przyszłość** do rozdziałów 08, 09, 10 i 25: `ch:function-operations`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Poprawne odsyłacze zachowano bez zmian.

Obejrzano istniejący diagram włókien w pełnym PDF iteracji 79 (strona PDF 74). Nie stwierdzono widocznych kolizji opisów ani obcięć. Dla zaimportowanej książki wykonanie kompilacji i kontroli logów powierza się dedykowanemu workflow `.github/workflows/logic-and-set-theory-chapter.yml`; jego wynik należy zweryfikować na aktualnym commicie, nie zakładać powodzenia przed uruchomieniem.

## Status

**Audyt I zakończony; poprawki formalne wprowadzone.** Zgodnie z zasadą powtarzania kontroli po każdej modyfikacji **rozdział 07 pozostaje otwarty do audytu II**, nawet jeśli CI zakończy się sukcesem. Nie przechodzić do rozdziału 08 przed uzyskaniem czystej, niezależnej iteracji rozdziału 07.
