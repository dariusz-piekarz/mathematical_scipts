# AA-X24 — niezależny audyt przekrojowy AA-11 → AA-28: kryterium Eisensteina i wielomiany cyklotomiczne potęg liczb pierwszych

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD odczytany ponownie bezpośrednio przed zapisem:** `c9d64b59609da87a8638392f293a4494128b3427`.

## Stan i zakres

W aktualnym katalogu `chapters/pl/abstract_algebra` jest 50 źródeł AA-01–AA-50; AA-51 nie istnieje. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, `books/pl/abstract_algebra.tex` oraz listę wcześniejszych raportów. Audyt X24 jest odrębny od X04 (wyróżniki i wypadkowe) i X10 (Gauss/Eisenstein w ogólnej sytuacji): dotyczy **interfejsu** kryterium Eisensteina AA-11 z konstrukcją `Phi_n` AA-28, szczególnie podstawienia `X↦X+1` dla `n=p^k`.

Źródła: AA-11 blob `62eb6a239ddcae2958c10b923b50a30dcb528ecc` (818 wierszy); AA-28 blob `2e24a69608aeab7856acf40f882480a97eb455bc` (328 wierszy). Nie zmieniono zatwierdzonych rozdziałów.

## Kontrola matematyczna

1. AA-11 podaje kryterium Eisensteina nad dziedziną z jednoznacznym rozkładem: `p∤a_n`, `p|a_j` dla `j<n`, `p²∤a_0`. AA-28 konstruuje moniczne `Phi_n∈Z[X]` i dowodzi nierozkładalności nad `Q` niezależnym argumentem modularnym. Hipotezy są zgodne; zastosowanie Eisensteina **po przesunięciu argumentu** nie wymaga dopisania nowego twierdzenia do zatwierdzonego tekstu.
2. Dla liczby pierwszej `p` i `k≥1` zachodzi `Phi_{p^k}(X)=Σ_{j=0}^{p-1}X^{jp^{k-1}}` oraz `Phi_{p^k}(X)≡(X-1)^{φ(p^k)} (mod p)`. Zatem `Phi_{p^k}(X+1)≡X^{φ(p^k)} (mod p)`. Jest moniczny, a jego wyraz wolny `Phi_{p^k}(1)=p`; spełnia więc wszystkie warunki Eisensteina przy `p`. Ponieważ podstawienie `X↦X+1` jest automorfizmem `Q[X]`, nierozkładalność wielomianu przesuniętego implikuje nierozkładalność oryginału. To **niezależna kontrola matematyczna** dla rodziny potęg liczb pierwszych, nie dowód nierozkładalności wszystkich `Phi_n` na tej drodze.
3. Przypadki brzegowe: `p=2,k=1` daje `Phi_2(X+1)=X+2`; `p=2,k=3` daje `(X+1)^4+1`, stały wyraz 2. Dla `n=1` nie ma pierwszej `p` w formule i należy korzystać z `Phi_1=X-1`. Dla ogólnego `n` złożonego z różnych liczb pierwszych nie wolno bez dowodu stosować tego samego argumentu (np. `Phi_6(X+1)=X²+X+1`, wyraz wolny 1).
4. Rachunek niezależny w Python/SymPy, wykonany **w bieżącym uruchomieniu**: dla `p∈{2,3,5,7,11}`, `1≤k≤3` i `φ(p^k)≤120` zweryfikowano dokładnie **13/13** wielomianów: moniczność, podzielność wszystkich niewiodących współczynników przez `p`, wyraz wolny równy `p`, brak podzielności tego wyrazu przez `p²` oraz stopień `φ(p^k)`. To test skończonej rodziny, nie zamiennik ogólnego dowodu powyżej.
5. Struktura: AA-11 ma 37 etykiet, 18 odsyłaczy, 19 środowisk dowodu i 11 przykładów; AA-28 ma 10 etykiet, 6 odsyłaczy, 4 dowody i 2 przykłady. **47 etykiet unikatowych**, 24 odsyłacze; wszystkie 6 celów zewnętrznych odczytano bezpośrednio w AA-09, AA-10, AA-19, AA-26. Nie stwierdzono duplikatu etykiet w parze. Kontrola ta nie jest pełną kontrolą wszystkich etykiet całej książki.

## Statusy niezależne

- **Matematyka (ściśle wybrany interfejs AA-11/AA-28):** 13/13 dokładnych testów PASS, dodatkowy ogólny argument opisany powyżej; nie wykryto błędu w badanym interfejsie. Nie deklaruje się pełnego przeglądu 23 dowodów.
- **Terminologia, odsyłacze i skład źródeł:** zgodność sprawdzonych sformułowań; 47 etykiet bez duplikatów, 24 odsyłacze z odnalezionymi celami. Brak zmian źródeł, więc licznik czystych audytów nie jest resetowany.
- **Nowa kompilacja LaTeX:** NIE WYKONANO. **Wizualna inspekcja PDF:** NIE WYKONANO. **Nowy CI na tym HEAD:** NIE URUCHOMIONO / NIEZWERYFIKOWANO. Nie wolno przenosić wcześniejszego zielonego CI na nowy audyt.
- **Stabilność:** ten raport nie stanowi nowej deklaracji stabilności całego tomu.

## Propozycja (bez wprowadzania do źródeł)

Opcjonalnie w AA-28 po dowodzie nierozkładalności dodać przykład alternatywnego zastosowania kryterium Eisensteina do `Phi_{p^k}(X+1)`; wymaga odrębnej zgody, gdyż jest to nowe uzupełnienie zatwierdzonego rozdziału.

**Następny krok:** ponownie sprawdzić HEAD i istnienie AA-51; jeśli nadal brak, wybrać nową, niepowtórzoną kontrolę przekrojową i przeprowadzić ją w osobnym numerowanym raporcie. Przy dostępie do artefaktów CI wykonać osobną inspekcję PDF i weryfikację workflow.
