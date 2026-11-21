# Algebra liniowa — rozdział 13 „Ortogonalność i rzuty”, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Zbadana wersja:** `2189a0857b4616f74c22f5367f1def502382e58e`  
**Plik:** `chapters/pl/linear_algebra/13-ortogonalnosc-i-rzuty.tex`

## Źródła i zakres

Rozdział 13 kontynuuje rozdziały 09 „Formy dwuliniowe i kwadratowe” oraz 12 „Przestrzenie euklidesowe i unitarne”. Nie powtarza szczegółowego dowodu rzeczywistej ortogonalizacji, polaryzacji ani reprezentacji Riesza; wykorzystuje już zweryfikowane twierdzenia `thm:lin9-gram-schmidt`, `thm:lin12-gram-schmidt`, `thm:lin12-riesz` i `cor:lin12-pitagoras`. W przypadku geometrycznych rozkładów inspiracją pozostaje rozdział „Tensor metryczny, długość i miara” z geometrii różniczkowej, jednak tutejsze argumenty są autonomiczne.

Części rozdziału: dopełnienie ortogonalne nad `R` i `C`; rozkład względem skończenie wymiarowej podprzestrzeni w dowolnej przestrzeni z iloczynem skalarnym; operatory rzutów i najlepsze przybliżenie; adjoint i jego związki z jądrem i obrazem; rzut jako idempotentny operator samosprzężony; wzór `P=B(B^*B)^{-1}B^*`; równania normalne, minimalizacja błędu, przypadek pełnego i niepełnego rzędu; minimalna norma; przemienne projekcje i dopełnienia przecięć.

## Pierwsza kontrola poprawności matematycznej

1. **Ortogonalny rozkład:** istnienie `V=U⊕U^⊥` wykazano dla skończenie wymiarowego `U`, także gdy `V` może mieć nieskończony wymiar. Nie rozszerzono twierdzenia bez uzasadnienia na wszystkie podprzestrzenie nieskończenie wymiarowe.
2. **Rzut ortogonalny:** konstrukcja `P_Uv=Σ h(e_i,v)e_i` jest liniowa w drugim argumencie iloczynu skalarnego. Jawnie wykazano obraz, jądro, idempotencję i tożsamość `h(Pv,w)=h(v,Pw)`.
3. **Najlepsze przybliżenie:** `v-u=(v-P_Uv)+(P_Uv-u)` jest rozkładem na składniki ortogonalne, dzięki czemu tożsamość Pitagorasa daje minimalność oraz jednoznaczność.
4. **Operator sprzężony:** istnienie `A^*` udowodniono za pomocą *liniowego* funkcjonału `F_w(v)=h_W(w,Av)` i finite-dimensionalnego twierdzenia Riesza. Uzasadniono liniowość `A^*` i macierz `[A^*]=[A]^*` w bazach ortonormalnych. Przypadki wymiaru 0 są zgodne z definicją.
5. **Rachunek sprzężeń:** zapis `(λA+μB)^*=conj(λ)A^*+conj(μ)B^*`, `(CA)^*=A^*C^*` i `A^{**}=A` jest spójny z konwencją liniowości drugiego argumentu.
6. **Obraz i jądro:** `(im A)^⊥=ker A^*`, `(im A^*)^⊥=ker A` oraz `ker A^*A=ker A` udowodniono z dodatniej określoności, bez odwołania do twierdzenia spektralnego.
7. **Charakterystyka projekcji:** warunki `P²=P=P^*` są równoważne ortogonalnemu rzutowi na obraz. Kontrprzykład `[[1,1],[0,0]]` ilustruje, że sama idempotencja nie wystarcza.
8. **Wzór macierzowy:** dla niezależnych kolumn `B` macierz `B^*B` jest dodatnio określona; zatem `B(B^*B)^{-1}B^*` wybiera składową w `im B` z ortogonalną resztą.
9. **Równania normalne:** minimizer zawsze istnieje jako preobraz rzutu na `im A`, a `A^*(Ax-y)=0` jest warunkiem koniecznym i wystarczającym. Zbiór minimizerów to `x_0+ker A`; dla niepełnego rzędu `A^*A` nie jest odwracalne, ale istnieje jednoznaczny minimizer o najmniejszej normie.
10. **Przykłady:** regresja trzech punktów daje `a=7/6`, `b=1/2`, normę reszty do kwadratu `1/6`; przykład osobliwej macierzy `[[1,1],[2,2]]` daje dopasowanie `(1/5,2/5)` i `x_min=(1/10,1/10)`. Przykład dwóch nieprzemiennych rzutów jest rachunkowo poprawny.
11. **Złożenia:** iloczyn dwóch rzutów ortogonalnych jest rzutem ortogonalnym dokładnie przy przemienności; w tym przypadku obraz jest przecięciem podprzestrzeni. Tożsamość `(U∩W)^⊥=U^⊥+W^⊥` została ograniczona do skończonego wymiaru.

## Kontrola techniczna

- Rozdział 13: **1303 wiersze**, **34 etykiety**, **18 odsyłaczy**.
- Rozdziały 01–13: **535 różnych etykiet**, **223 odsyłacze do istniejących etykiet**, zrównoważone środowiska, poprawny katalog oraz `\\input`.
- `tools/test_linear_algebra_projections.py` sprawdza sprzężenia, dodatniość i idempotencję rzutów, równania normalne, minimalność reszty oraz nieprzemienność projekcji; nie wymaga zewnętrznych zależności.
- Workflow `linear-algebra-chapter.yml` został rozszerzony do 13 rozdziałów. Sprawdzenie kompilacji PDF i brak ostrzeżeń LaTeX należy potwierdzić w GitHub Actions przed zamknięciem.

**Wynik:** audyt I wykonał kontrolę konstrukcyjną i odsyłaczy; nie zamyka rozdziału. Przed stabilizacją potrzebny jest niezależny audyt II i zielony CI. Po zamknięciu stabilne rozdziały 01–12 pozostają niezmienione.
