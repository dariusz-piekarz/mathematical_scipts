# Algebra liniowa — rozdział 09, audyt II (niezależny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**SHA sprawdzonej treści:** `6639b04df4de851feeb6e29e4e6afa39fdaf3764`

## Weryfikacja matematyczna

Ponownie skontrolowano wszystkie definicje i dowody, nie dodając nowych twierdzeń. Przedmiotem audytu były także przypadki zerowego wymiaru, dowolna charakterystyka ciała oraz rozróżnienie rezultatów skończenie wymiarowych od twierdzeń ogólnych.

1. **Konstrukcja uniwersalna:** wolna przestrzeń funkcji o skończonym nośniku `K^(V×W)` ma wskazaną bazę formalnych symboli. Podprzestrzeń `N` zawiera dokładnie generatory wymuszające addytywność i jednorodność w obu argumentach. Każde `b:V×W→Z` dwuliniowe wyznacza jedno liniowe `L_b`, które zeruje `N`, a więc przechodzi do jednoznacznego `F/N→Z`.
2. **Jednoznaczność:** konstruowane w obu kierunkach odwzorowania między realizacjami spełniają warunki identyczności po złożeniu z kanonicznymi mapami. Jednoznaczność w definicji wymusza tożsamości złożeń bez odwoływania się do baz.
3. **Tensor prosty:** implikacja `v⊗w=0 ⇒ v=0 lub w=0` wykorzystuje funkcjonały rozdzielające skonstruowane z baz Hamela. W wymiarze nieskończonym wymagane istnienie takich baz zostało jawnie wskazane w odsyłaczu do wcześniejszego twierdzenia.
4. **Baza i rząd:** `v_i⊗w_j` rozpinają przestrzeń przez dwuliniowość, a liniowa niezależność wynika z funkcjonałów współrzędnych `L_{pq}`. Dla macierzy współczynników `C_t` każdy rozkład na `r` tensorów prostych daje sumę `r` macierzy rzędu najwyżej 1, a rozkład według bazy przestrzeni kolumn daje nierówność odwrotną.
5. **Kronecker:** wzór elementowy `(A⊗B)_(p,q),(i,j)=a_(p,i)b_(q,j)` jest zgodny z porządkiem baz; równości mnożenia, transpozycji i rzędów nie wymagają kwadratowości macierzy.
6. **Kanoniczne izomorfizmy:** zamiana czynników, łączność i `K⊗V≅V` skonstruowane zostały przez własność uniwersalną. W dowodzie łączności wykazano oddzielną liniowość `(x,w)↦L_w(x)`; równości złożeń weryfikowano na rodzinach rozpinających.
7. **Wielokrotne czynniki:** indukcja w liczbie argumentów korzysta z linearyzacji dla pierwszych `k−1` argumentów. Sprawdzono liniowość rodziny `w↦L_w` i jednoznaczność odwzorowania końcowego.
8. **Hom i dual:** `W⊗V*→Hom(V,W)` jest iniektywne również dla nieskończonych wymiarów, a jego obrazem są dokładnie odwzorowania skończonego rzędu. Izomorfizm `(V⊗W)*≅Hom(V,W*)` zachodzi bez ograniczenia wymiarów, lecz `V*⊗W*≅(V⊗W)*` sformułowano tylko przy skończonych wymiarach.
9. **Sumy i ilorazy:** dopełnienie algebraiczne jest użyte tylko w dowodzie, a ostateczny izomorfizm `(V⊗W)/im(U⊗W)≅(V/U)⊗W` powstaje kanonicznie z `q⊗id`. Kontrakcja `V⊗V*→K` nie opiera się na niedostępnej identyfikacji `V=V*`.

## Niezależne testy i kontrola techniczna

Dodano `tools/test_linear_algebra_tensors.py` oraz osobny krok GitHub CI. Test obejmuje iloraz wolnej przestrzeni przez wymuszone warunki dwuliniowości w **4 konfiguracjach**, w tym jeden czynnik zerowy; rząd i transpozycję iloczynu Kroneckera dla wszystkich **6817 par** macierzy `2×2` nad `F_2` i `F_3`; równość dla złożenia w kolejnych **6817 konfiguracjach** oraz kryterium prostoty dla **97 macierzy**. Wszystkie testy przeszły bez rozbieżności.

Statyczna kontrola całej książki: **387 unikalnych etykiet**, **154 odsyłacze**, wszystkie rozwiązane; brak niezamkniętych środowisk LaTeX i naruszeń terminologii. Rozdział 09 ma 1360 wierszy, 41 etykiet i 14 odsyłaczy. Kompilację końcową po integracji kontrolujemy osobnym, aktualnym przebiegiem GitHub Actions; wynik należy zapisać po jego ukończeniu.

## Rezultat

**Nie wykryto nowego błędu ani istotnej luki matematycznej.** Treści rozdziału 09 nie zmieniono. Rozdział pozostaje formalnie otwarty do sprawdzenia końcowego CI i czystego audytu stabilizacyjnego.
