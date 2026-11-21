# Algebra liniowa — rozdział 10, audyt II (niezależna kontrola)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/10-algebry-tensorowa-symetryczna-i-zewnetrzna.tex`  
**Wersja po korekcie:** `05a9a359896c434c12f0e06c9764ecf6dab59a4e`  
**Tekst porównawczy:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`.

## Wyniki ponownej kontroli

Nie dodano nowych twierdzeń ani sekcji. Ponownie sprawdzono wszystkie twierdzenia, definicje, dowody i przykłady, zwracając szczególną uwagę na charakterytykę ciała, przypadki zerowe i poprawność przechodzenia do ilorazów.

1. **Łączna algebra stopniowana:** mnożenie w `T(V)=⊕V^{⊗k}` ma sens dzięki kanonicznym izomorfizmom łączności; skończony nośnik gwarantuje domknięcie mnożenia. Własność uniwersalna `T(V)` wynika z iterowanej linearyzacji odwzorowań wieloliniowych.
2. **Ideały i ilorazy:** ideały `J=(u⊗v-v⊗u)`, `I=(v⊗v)` są jednorodne, więc ich ilorazy dziedziczą stopniowanie. Dowody sprawdzają niezależność mnożenia klas od wyboru reprezentantów.
3. **Algebra symetryczna:** model wielomianowy opiera się na uniwersalnym homomorfizmie `S(V)→K[x_1,...,x_n]`. Obrazy jednomianów w różnych stopniach są liniowo niezależne; wymiary `binom(n+k-1,k)` nie wymagają dzielenia przez `k!`. Uwzględniono `n=0` i `k=0`.
4. **Algebra zewnętrzna:** relacje `v∧v=0` i `u∧v=-v∧u` wynikają z definicji przez kwadraty, także dla `char K=2`. Reguła `α∧β=(-1)^{pq}β∧α` dotyczy składowych stopni `p,q`, bez dodatkowego założenia charakterystyki.
5. **Uniwersalność `Λ^k(V)`:** forma naprzemienna zeruje całe `I∩V^{⊗k}`, ponieważ jest ono generowane w stopniu `k` przez tensory z dwoma sąsiednimi jednakowymi argumentami. Faktoryzacja i jej jednoznaczność zostały udowodnione oddzielnie.
6. **Baza zewnętrzna:** rozpiętość osiągnięto przez uporządkowanie indeksów; liniową niezależność wykazano funkcjonałami określonymi z minorów. Wzór `dim Λ^k(V)=binom(n,k)` i `dim Λ(V)=2^n` jest poprawny także w charakterystyce 2.
7. **Minory i operatory:** wzory na `Λ^k A` i współczynniki minorowe są zgodne z leksykograficznym porządkiem baz. `Λ^k(AB)=Λ^k A · Λ^k B` daje wzór Cauchy'ego--Bineta, także w przypadku `k>n`. Skalar działania endomorfizmu na `Λ^n V` jest wyznacznikiem z rozdziału 06.
8. **Formy naprzemienne:** pierwsza identyfikacja `(Λ^k V)^*≅Alt^k(V^*)` nie wymaga skończonego wymiaru. Druga `Λ^k(V^*)≅Alt^k(V^*)` jest udowodniona dla skończonego wymiaru. Wzór na iloczyn form sumuje po przetasowaniach zamiast dzielić przez silnie, działa więc nad każdym ciałem.
9. **Rzutowania:** w formule `(k!)^{-1}𝓢_k` i `(k!)^{-1}𝓐_k` jawnie wymagamy `k!1_K≠0_K`. Jądra odpowiednich ilorazów są zerowane przez operator symetryzacji lub alternowania dzięki parowaniu permutacji. W dowodach zachowano rozróżnienie ilorazu od obrazu rzutowania.

## Wykryta nieścisłość i poprawka

W dowodzie twierdzenia `thm:lin10-formy-alt` zapisano początkowo, że przy `k=0` obie strony pierwszego izomorfizmu są równe `K`. Formalnie lewa strona to `(Λ^0 V)^*=K^*`, a prawa to `Alt^0(V^*)=K`: nie są to dosłownie te same przestrzenie. Poprawiono fragment, podając **kanoniczną ewaluację `L↦L(1_K)` oraz jej odwrotność `a↦(x↦ax)`**. Jest to korekta ścisłości dowodu w przypadku brzegowym, bez zmiany twierdzenia.

## Sprawdzenia techniczne

- Rozdział 10 ma **1630 wierszy**, **42 etykiety** i **27 odsyłaczy**.
- Kontrola statyczna rozdziałów 01–10: **429 niepowtarzających się etykiet** i **181 poprawnych odsyłaczy**, poprawna kolejność i importy w książce, zgodny katalog, brak błędów zagnieżdżenia środowisk LaTeX i niepożądanej terminologii.
- Do `tools/test_linear_algebra_exterior.py` dodano niezależne testy dla ciał `F_2` i `F_3`: naprzemienność, współrzędne minorowe, Cauchy–Binet, wzór z przetasowaniami i wymiar baz. Test jest uruchamiany w dedykowanym CI obok wcześniejszych testów iloczynów tensorowych.
- Pierwszy przebieg CI dla zintegrowanego rozdziału, [44916678656](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44916678656), zakończył się `success`. Wersja po korekcie i po dołożeniu testów uruchomiła [44916955344](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44916955344); jej wynik trzeba potwierdzić po zakończeniu.

## Decyzja

**Audyt II zakończony jedną drobną korektą.** Nie znaleziono błędu w tezach matematycznych, ale ze względu na poprawkę `k=0` przed zamknięciem rozdziału 10 należy wykonać niezależną, czystą iterację III na aktualnym pliku. Nie dodajemy materiału.
