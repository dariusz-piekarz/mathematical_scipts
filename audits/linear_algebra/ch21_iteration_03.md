# Algebra liniowa — rozdział 21, audyt III (niezależny, po korekcie II)

**Data:** 21 listopada 2026.  
**Źródło:** `chapters/pl/linear_algebra/21-komutant-operatora-i-centralizatory-macierzy.tex`.  
**Kontrolowany blob:** `6527ae1a6daca48717e6a5f5e83958271abb16f5`.  
**Poprzednie audyty:** I (utworzenie tekstu), II (uproszczenie uzasadnienia zliczania indeksów).

## Niezależny przegląd matematyczny

1. **Przypadki zerowe.** Przy `V={0}` pierścień endomorfizmów jest zerową przestrzenią, komutant ma wymiar 0, jego jedyny element działa jako jedynka na zerowej przestrzeni. Wszystkie sumy po pustych listach czynników są równe 0. Wyniki wymagające operatora cyklicznego i oszacowania równości sformułowano dla `n≥1`.
2. **Niezmienniczość względem podobieństwa.** Sprawdzono oba kierunki `S'T'=T'S' iff ST=TS` przy `S'=USU^{-1}`, `T'=UTU^{-1}`; działanie jest izomorfizmem algebr, a nie wyłącznie bijekcją zbiorów.
3. **Hom cyklicznych modułów.** Każda składowa jest wyznaczona przez obraz generatora, a warunek zgodności relacji `f·[1]=0` daje `g|fy`. Po rozłożeniu przez największy wspólny dzielnik `d` jednoznaczny parametr `[h]_d` opisuje wszystkie obrazy. Dla `gcd(f,g)=1` jedynym homomorfizmem jest zerowy. Nie przyjęto milcząco algebraicznego domknięcia ciała.
4. **Wielomiany operatora cyklicznego.** Po przeniesieniu z `K[t]/(m_T)` każda mapa przemienna z `T` jest wielomianem w `T`. Odwrotność wielomianu `p(T)` należy do tego komutanta i daje równość Bézouta modulo `m_T`, co uzasadnia obie implikacje kryterium odwracalności.
5. **Wymiar z czynników Smitha.** Mapa rozkładająca endomorfizm sumy prostej na wszystkie komponenty Hom jest wzajemnie jednoznaczna i liniowa; liczba par dla minimum indeksów `i` wynosi `2(r-i)+1`. Dla `r=1` otrzymujemy wymiar `deg f_1=n`; dla `r>1` wymiar jest większy.
6. **Kryterium operatora skalarnego.** Jeśli każdy endomorfizm przemienia się z `T`, to jego macierz komutuje z `E_{ii}` i `E_{ij}`. Pierwsze równości wykluczają elementy niediagonalne, drugie identyfikują elementy diagonalne; dla `n=1` warunek jest automatyczny.
7. **Wymiar z bloków pierwotnych.** Pomiędzy odmiennymi pierwotnymi składnikami Hom zanika przez względną pierwszość, a w obrębie `p` wymiar wynosi `deg p min(a,b)`. Po korekcie II identyczność z `∑ B_{p,k}²` opiera się na bezpośrednim zliczeniu trójek `(i,j,k)`; nie występują nieobjaśnione symbole.
8. **Filtracje jąder.** Podstawienie `D_{p,k}-D_{p,k-1}=deg(p)B_{p,k}` daje sumę kwadratów z czynnikiem `1/deg p`. Suma po `k` jest skończona, ponieważ dla dużego `k` wszystkie przyrosty zanikają.
9. **Centralizator odwracalny nad `F_q`.** W każdym pierwotnym pierścieniu `F_q[t]/(p^a)` dokładnie `q^{(a-1)deg p}` klas jest nieodwracalnych. Po wymnożeniu liczby jednostek otrzymujemy dokładnie wzór zapisany w rozdziale. 

## Przykłady i testy

- `J_3(λ)`: przemienność dokładnie z macierzami górnotrójkątnymi Toeplitza `aI+bN+cN²`.
- `J_2(0)⊕J_1(0)`: pięć parametrów, odwracalność `a²e≠0`, `(q−1)²q³` jednostek.
- `diag(1,1,2)`: komutant blokowy `M_2(Q)⊕Q`, wymiar 5.
- Obrót `[[0,-1],[1,0]]`: komutant rzeczywisty izomorficzny do `C`.
- Sześciowymiarowe nilpotentne przykłady: wymiary komutantów 12 i 14.
- Blok `C((t²+t+1)²)` nad `F_2`: 16 elementów komutanta, 12 jednostek.

Regresje w `tools/test_linear_algebra_commutants.py` sprawdzają wymiar rozwiązań `AX=XA`, wzór z czynników niezmienniczych oraz wzór z dzielników elementarnych na wszystkich `2×2/F_2,F_3`, wszystkich `3×3/F_2` i deterministycznej próbce `3×3/F_3`; przykłady grup jednostek testują niezależnie.

## Struktura, LaTeX i wydruk

- 25 etykiet o 25 różnych nazwach, 37 odsyłaczy, 9 otwarć i 9 zamknięć środowiska `proof`.
- Nie wykryto nowych kolizji etykiet ani terminów zabronionych przez `AGENTS.md`.
- [CI 44943810579](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943810579) **SUCCESS** dla skorygowanego bloba rozdziału: pełny zestaw testów, kompilacja i kontrola odsyłaczy.
- PDF z poprzedniego pomyślnego przebiegu ma 7 niepustych stron; kontrola PyMuPDF: 0 bloków tekstu poza stroną. Należy obejrzeć końcowy artefakt dla najnowszej wersji po raportach audytowych.

## Decyzja

**Audyt III czysty** — bez nowych poprawek. Pierwsza czysta iteracja po korekcie z audytu II. Pozostaje audyt IV oraz ostateczne potwierdzenie CI i PDF.
