# Algebra liniowa — rozdział 13, audyt II (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/13-ortogonalnosc-i-rzuty.tex`  
**SHA kontrolowanego tekstu:** `2189a0857b4616f74c22f5367f1def502382e58e`  
**Poprzedni raport:** `audits/linear_algebra/ch13_iteration_01.md`.

## Rygor i granice zakresu

Druga kontrola istniejącego tekstu objęła założenia, liniowość i sprzężenia, kryteria konieczne i wystarczające, przypadki wymiaru zero, konkretne przykłady, odsyłacze i jakość kompilacji. Nie rozszerzono zatwierdzonego pokrycia materiałowego ani nie zmieniono treści rozdziałów 01–12. Rzeczywiste twierdzenia o ortogonalizacji, rzutowaniu i formach kwadratowych odsyłają do rozdziału 09, a zespolona polaryzacja i reprezentacja Riesza do rozdziału 12.

## Niezależna kontrola dowodów — brak poprawek

1. **Algebra dopełnień:** (U^perp) jest przecięciem jąder funkcjonałów `h(u,·)`; `U∩U^⊥={0}` wynika z dodatniej określoności, a `(U_1+U_2)^⊥=U_1^⊥∩U_2^⊥` z półtoraliniowości.
2. **Podprzestrzeń skończenie wymiarowa:** nawet gdy `V` nie ma skończonego wymiaru, `U` ma bazę ortonormalną i umożliwia konstrukcję `v=Σ h(e_i,v)e_i+w` z `w∈U^⊥`. Przecięcie jest trywialne, dlatego rozkład jest jednoznaczny. `(U^⊥)^⊥=U` wynika z dodatniej określoności. Nie przypisano tego wniosku wszystkim podprzestrzeniom nieskończonego wymiaru.
3. **Rzut i aproksymacja:** `P_Uv=Σ h(e_i,v)e_i` jest liniowe względem `v` przy ustalonej konwencji. `P_U²=P_U`, `im P_U=U`, `ker P_U=U^⊥` oraz `h(P_Uv,w)=h(v,P_Uw)` wynikają z rozkładu, bez założenia istnienia abstrakcyjnego adjointu w nieskończonym wymiarze. Tożsamość Pitagorasa daje jedyny najlepszy aproksymant.
4. **Operator sprzężony:** w skończonych wymiarach funkcja `F_w(v)=h_W(w,Av)` jest liniowa w `v` i posiada reprezentanta Riesza `a_w`. Po sprzężeniu otrzymujemy `h_W(Av,w)=h_V(v,a_w)`; liniowość `w↦a_w` wynika z jednoznaczności. W bazach ortonormalnych macierz jest `[A]^*`. Złożenia, sprzężenia skalarne i podwójne sprzężenie są poprawne.
5. **Jądra, obrazy i dodatnia półokreśloność:** `(im A)^⊥=ker A^*` i analogiczna równość dla `A^*` wynikają wprost z definicji. `ker A^*A=ker A` wynika z `h(v,A^*Av)=||Av||²`, co wystarcza do równości rzędów.
6. **Samosprzężona idempotencja:** dla operatora `P²=P` istnieje rozkład `V=im P⊕ker P`; dodatkowy warunek `P^*=P` daje ortogonalność, więc `P` jest dokładnie rzutem na `im P`. Przykład `[[1,1],[0,0]]` wykazuje konieczność drugiego warunku.
7. **Macierz Grama:** dla niezależnych kolumn `B`, `G=B^*B` jest dodatnio określona i odwracalna; formuła `BG^{-1}B^*` daje resztę w `ker B^*=U^⊥`. Dla pustej rodziny, `r=0`, przyjęto jawnie rzut zerowy.
8. **Równania normalne:** istnienie minimizera wynika z rzutu `P_{im A}y` i definicji obrazu. Równoważności `miniff y-Ax∈(imA)^⊥iff A^*(Ax-y)=0iff A^*Ax=A^*y` są prawidłowe. Rozwiązania tworzą `x_0+ker A`, niekoniecznie pojedynczy punkt.
9. **Niepełny rząd:** spośród wszystkich minimizerów jeden, leżący w `(ker A)^⊥`, ma najmniejszą normę; tożsamość Pitagorasa dowodzi zarazem istnienia i jednoznaczności. Przykład `A=[[1,1],[2,2]]` ma rozwiązania `x_1+x_2=1/5` i unikalne rozwiązanie minimalnej normy `(1/10,1/10)`.
10. **Regresja liczbowa:** dla punktów `(0,1),(1,2),(2,2)` rachunek `A^TA=[[3,3],[3,5]]`, `A^Ty=(5,6)` daje `(a,b)=(7/6,1/2)` i `||r||²=1/6`; reszta jest ortogonalna do kolumn.
11. **Rzuty przemienne:** `(PQ)^*=QP` i `P²=P,Q²=Q`; zatem `PQ` jest samosprzężoną idempotencją dokładnie przy przemienności i wtedy ma obraz `U∩W`. Kontrprzykład z dwiema prostymi w `R²` jest poprawny. Formuła `(U∩W)^⊥=U^⊥+W^⊥` pozostaje prawidłowo ograniczona do skończonego wymiaru.
12. **Rysunek:** zorientowany wektor `P_Uv` i reszta `v-P_Uv` tworzą na rysunku kąt prosty; rysunek jest samodzielny TikZ, bez plików zewnętrznych.

## Kontrola GitHuba i regresji

- Rozdział 13: **1303 wiersze, 34 etykiety, 18 odsyłaczy**.
- Cały tom 01–13: **535 unikalnych etykiet i 223 odsyłacze do istniejących etykiet**; zgodne importy, katalog, bilans środowisk i terminologia.
- Testy `tools/test_linear_algebra_projections.py`: **560** przypadków sprzężenia, **4700** przypadków projekcji/odległości, **3761** przypadków najmniejszych kwadratów, **3** kontrole przemienności. Łącznie **9024** próby, wszystkie udane.
- W [GitHub Actions 44926186944](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926186944) komplet 13 rozdziałów zbudowano jako **139-stronicowy PDF**, **zero ostrzeżeń** kompilacji LaTeX; walidacje CLI i rozdziałów dla tego commitu były zielone.
- Po zapisaniu raportu CI uruchamiany jest ponownie; jego wynik należy osobno potwierdzić.

## Decyzja

**Audyt II — czysty.** Nie wykryto nowych błędów w sformułowaniach, przykładach ani dowodach; plik matematyczny pozostał bez zmian. Rozdział 13 uznajemy za **stabilny i zamknięty po dwóch audytach i zielonym CI**. Następna iteracja może rozpocząć rozdział 14 zgodnie z planem.
