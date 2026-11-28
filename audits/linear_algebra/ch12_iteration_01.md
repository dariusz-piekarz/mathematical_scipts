# Algebra liniowa — rozdział 12, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/12-przestrzenie-euklidesowe-i-unitarne.tex`  
**Weryfikowany blob:** `f205ea41e5562cc14f13869e0ff17877d2d29079`

## Cel i źródła

Nowy rozdział 12 „Przestrzenie euklidesowe i unitarne” kontynuuje uzgodniony plan po rozdziałach 09 „Formy dwuliniowe i kwadratowe”, 10 „Iloczyny tensorowe” i 11 „Algebry tensorowa, symetryczna i zewnętrzna”. Wykorzystuje rozdział `chapters/pl/linear_algebra/09-formy-dwuliniowe-i-kwadratowe.tex` dla rzeczywistej ortogonalizacji i rzutowania, a także `chapters/pl/differential_geometry_and_topology/11-tensor-metryczny-dlugosc-i-miara.tex` dla interpretacji metryki jako dodatnio określonej formy. Dowodów o rzeczywistych rzutach nie powielano. Nowy zakres obejmuje formy hermitowskie i geometrię zespoloną, reprezentację Riesza oraz izometrie unitarne.

## Sprawdzenia matematyczne

1. **Definicja:** przyjęto jawnie konwencję form półtoraliniowych: pierwszy argument sprzężenie liniowy, drugi liniowy. Hermitowskość wymusza rzeczywistość przekątnej; dodatnia określoność nadaje normę. Przypadek `K=R` jest szczególny.
2. **Polaryzacja:** kompleksowy wzór `h(u,v)=1/4(q(u+v)-q(u-v)-i q(u+iv)+i q(u-iv))` ma poprawny znak przy części urojonej dla wybranej konwencji. Przykład `h(1,i)=i` weryfikuje ten znak.
3. **Gram:** `G_{ij}=h(e_i,e_j)`, `h(u,v)=X^*GY`, `G'=P^*GP`; wszystkie sprzężenia są umieszczone zgodnie z liniowością drugiego argumentu.
4. **Cauchy–Schwarz:** w dowodzie dobiera się `c=h(v,u)/h(v,v)`, aby `h(v,u-cv)=0`; dodatnia określoność daje żądaną nierówność. Przypadek `v=0` i warunek równości sprawdzono osobno.
5. **Ortonormalizacja:** z `w_j=v_j-Σ_{i<j}h(e_i,v_j)e_i` wynika ortogonalność do wcześniejszych `e_i`; `w_j≠0` wynika z niezależności rodziny. Rzeczywisty przypadek jest odesłany do rozdziału 09.
6. **Reprezentacja Riesza:** funkcjonał liniowy `F` reprezentuje `a=Σ_j conjugate(F(e_j))e_j` przez `F(v)=h(a,v)`. Mapa `a↦h(a,·)` jest **sprzężenie liniowa** nad `C`, liniowa nad `R`; nie wprowadzono błędnego zespolono-liniowego utożsamienia.
7. **Bessel i Parseval:** rozwinięcie ortonormalne daje rozkład Pitagorasa i nierówność Bessela, z równością dokładnie w rozpiętości rodziny. Sprawdzono przypadek `m=0`.
8. **Kryterium Grama:** macierz `G=(h(v_i,v_j))` jest dodatnio półokreślona; przy niezależności `G=R^*R` i `det G=|det R|²>0`; przy zależności wykazano `Gc=0` dla niezerowego `c`. Wymiar przestrzeni może być nieskończony, bo sprawdzana rodzina jest skończona.
9. **Izometrie unitarne:** zachowanie normy implikuje zachowanie iloczynu skalarnego przez polaryzację; w ortonormalnej bazie `A^*A=I` jest równoważne odwracalności i `A^{-1}=A^*`. Wyznacznik ma moduł `1`, także w wymiarze zero.
10. **Przykłady:** nieprzemienna część zespolona w macierzy `[[2,i],[-i,2]]` oraz jej dodatnia określoność przez uzupełnienie modułu kwadratu są spójne. Gram–Schmidt dla `(1,i),(1,0)` daje bazę `((1,i),(1,-i))/sqrt(2)`.

## Kontrola struktury

- Rozdział 12: **1065 wierszy**, **36 etykiet** i **9 odsyłaczy**.
- Cała algebra liniowa 01–12: **501 różnych etykiet** i **205 prawidłowych odsyłaczy**; brak konfliktów etykiet, brak otwartych środowisk, katalog i importy są zgodne.
- Dodano regresję `tools/test_linear_algebra_unitary.py`: polaryzacja, wyznacznik Grama, ortogonalizacja zespolona, Riesz/Bessel, zachowanie normy przez unitarne macierze.
- Workflow `linear-algebra-chapter.yml` obejmuje 12 rozdziałów oraz nowe testy. Końcowy stan kompilacji dokumentujemy dopiero po potwierdzeniu GitHub Actions.

**Status audytu I:** rozdział 12 otwarty; kolejna niezależna kontrola matematyczna oraz wynik kompilacji są wymagane do stabilizacji. Nie zmieniano rozdziałów 01–11.
