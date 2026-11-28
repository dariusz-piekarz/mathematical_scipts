# Algebra liniowa — rozdział 09, audyt IV

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**Zweryfikowana wersja po poprawkach:** `36cc8dc64ae88beea31db953417a192a0e2e10af`  
**Materiał porównawczy:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` (rozdział 03 skryptu geometrii różniczkowej, SHA `7ab3f15ced06e8233f978471c779e343ac5902ca`).

## Zakres czwartego audytu

Audyt objął ponowne czytanie wszystkich definicji, twierdzeń i dowodów w rozdziale 09 oraz porównanie odpowiadających im konstrukcji z rozdziałem „Algebra tensorowa i zewnętrzna” geometrii różniczkowej. Nie dodano nowych twierdzeń ani nie rozszerzono zatwierdzonego zakresu tematycznego. Przeanalizowano w szczególności: konstrukcję `K^(V×W)/N`, kwantyfikatory własności uniwersalnej, jednoznaczność faktoryzacji, rozpiętość przez tensory proste, warunek zerowania, podstawy współrzędnych i rząd, iloczyn Kroneckera, łączność i zamianę czynników, linearyzację wieloliniowości, identyfikacje z przestrzeniami operatorów, dual, sumy proste i ilorazy oraz kontrakcję.

## Wyniki kontroli matematycznej

1. **Konstrukcja:** symbole `[v,w]` w wolnej przestrzeni `K^(V×W)` są przed utworzeniem ilorazu formalnie niezależne. Cztery rodziny generatorów `N` wymuszają dokładnie addytywność i jednorodność w dwóch argumentach. W dowodzie faktoryzacji sprawdzono `f+N=g+N ⇒ f-g∈N⊂ker L_b ⇒ L_b(f)=L_b(g)`.
2. **Własność uniwersalna i jednoznaczność:** dziedziną `b` jest `V×W`, jego wartości leżą w dowolnym `Z`, a `\\widetilde b` jest liniowe na całym iloczynie tensorowym. Dwie realizacje są połączone jednoznacznym izomorfizmem, skonstruowanym przez odwzorowania w przeciwnych kierunkach.
3. **Tensor prosty i baza:** `v⊗w=0` dokładnie wtedy, gdy przynajmniej jeden argument jest zerowy; w kierunku nietrywialnym funkcjonały rozdzielają niezerowe argumenty (w wymiarze nieskończonym korzystamy z baz Hamela). W bazie `(v_i⊗w_j)` liniową niezależność potwierdzają funkcjonały `L_pq`.
4. **Rząd:** minimalna długość rozkładu na tensory proste jest rzędem macierzy współczynników w przypadku dwóch czynników skończenie wymiarowych. Każda suma z `r` składnikami ma macierz rzędu co najwyżej `r`; rozkład według bazy przestrzeni kolumn daje nierówność odwrotną.
5. **Macierze:** wzór elementowy Kroneckera, reguła mnożenia, transpozycja oraz rząd są zgodne z leksykograficznym porządkiem tensorów bazowych. Dowody uwzględniają odwzorowania zerowe i rozmiary prostokątne.
6. **Kanoniczne izomorfizmy:** zamiana czynników i zmiana nawiasowania są izomorfizmami, a nie dosłownymi identycznościami formalnie różnych iloczynów. Po zamianie argumentów prostych mamy `v⊗w ↦ w⊗v`, co nie oznacza `v⊗w=w⊗v`.
7. **Wiele czynników i przestrzenie operatorów:** linearyzacja wieloliniowego odwzorowania jest jednoznaczna; `W⊗V*→Hom(V,W)` ma obraz wszystkich odwzorowań o skończonym rzędzie, przy `dim V<∞` jest surjektywne na całe `Hom`.
8. **Dual i kontrakcja:** `(V⊗W)*≅Hom(V,W*)` ma sens bez założenia skończonego wymiaru, natomiast identyfikację `V*⊗W*≅(V⊗W)*` prawidłowo ograniczono do skończonych wymiarów. `c_V:V⊗V*→K` wykorzystuje ewaluację i odtwarza ślad bez wyboru bazy lub iloczynu skalarnego.
9. **Podprzestrzenie i ilorazy:** wybór dopełnienia w dowodzie nie zmienia kanoniczności izomorfizmu indukowanego przez `q⊗id`. Równość jądra z obrazem włożenia została sprawdzona także na małych ciałach.

**Wniosek matematyczny:** brak błędu w sformułowaniach twierdzeń i brak konieczności zmiany dowodzonej tezy. Audyt wykrył trzy miejsca nadające się do doprecyzowania oraz jedną nieprecyzyjną notację macierzową.

## Wykonane korekty w rozdziale 09

- Doprecyzowano, że elementy bazy wolnej przestrzeni są formalne, a równości dwuliniowości pojawiają się dopiero w ilorazie. Objaśnienie adaptowano z rozdziału 03 geometrii różniczkowej.
- Dodano jawne sprawdzenie dobrej określoności linearyzacji na klasach oraz wzór na jej wartości dla dowolnego przedstawienia tensora jako skończonej sumy prostych składników. Objaśnienie adaptowano z tego samego źródła.
- Po dowodzie kanonicznego przestawiania czynników wyjaśniono, dlaczego jest to izomorfizm, a nie równość tensorów; rozróżnienie zilustrowano determinantem na `R^2×R^2`, również z materiału geometrii różniczkowej.
- Zapis elementu diagonalnego macierzy endomorfizmu ujednolicono z `[T]_B{}_{ii}` na `([T]_B)_{ii}`. Nie zmieniono definicji śladu ani argumentu dowodu.

Ważna różnica zakresu źródeł: rozdział 03 geometrii różniczkowej przyjmuje `K=R` albo `K=C`, a rozdział 09 algebry liniowej działa nad **dowolnym ciałem**. Dlatego konstrukcji z dzieleniem przez `k!` nie kopiowano bez dodatkowego warunku odwracalności `k!1_K`; stanowiłoby to nieuzasadnioną zmianę założeń. Nie kopiowano też algebry zewnętrznej, której dodanie oznaczałoby rozszerzenie zatwierdzonego materiału.

## Testy i integralność

- **1170 dodatkowych, niezależnych testów** nad `F_2` i `F_3`: dla wszystkich odwracalnych macierzy bazowych o rozmiarach `2×2` nad `F_2,F_3` i `3×3` nad `F_2`, wszystkich wybranych niezerowych podprzestrzeni właściwych w tych bazach oraz drugich czynników o wymiarach `1,2,3`, sprawdzono rangi `i⊗id` i `q⊗id`, zerowanie ich złożenia i równość `dim ker(q⊗id)=dim im(i⊗id)`. Zero rozbieżności.
- Dedykowane automatyczne testy `tools/test_linear_algebra_tensors.py` sprawdzają 4 przypadki konstrukcji ilorazowej, 6817 par macierzy Kroneckera (rząd i transpozycja), 6817 przypadków reguły mnożenia oraz 97 przypadków rozkładalności tensorów. Wynik w aktualnym workflow: test matematyczny **success**.
- Ponowna kontrola strukturalna rozdziałów 01–09: **387 unikalnych etykiet**, **154 odsyłacze z istniejącymi celami**, brak błędów środowisk i naruszeń terminologii.
- CI źródłowej wersji z objaśnieniami: [44913821043](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44913821043). CI dla końcowej wersji po korekcie zapisu śladu: [44913970737](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44913970737). Stan końcowy tych przebiegów wymaga sprawdzenia po ich zakończeniu.

## Decyzja

**Audyt IV wykonany, wykryte doprecyzowania wprowadzono.** Nie znaleziono usterki matematycznej zmieniającej wynik. Treść rozdziału zmieniła się wyłącznie redakcyjnie i w istniejących wyjaśnieniach. Do stwierdzenia pełnej stabilności wersji po korekcie wymagamy przejścia końcowego CI; następna niezależna iteracja może potwierdzić brak dalszych uwag.
