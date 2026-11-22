# Algebra liniowa — audyt globalny, iteracja 25: LA25–26, 26 dowodów

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 24](iteration_24.md).

**Wynik:** przeczytano pełne tezy i kompletne dowody wszystkich **26 twierdzeń, lematów, wniosków i stwierdzeń** w LA25–26; po analizie podstawowych przypadków brzegowych i 14 przykładów nie znaleziono błędu matematycznego wymagającego zmiany rachunków ani dowodów. Wprowadzono za to **4 rzeczywiste poprawki samodzielności sformułowań głównych twierdzeń**. Rozdziały LA27–32 **nie są zaliczone** do niniejszej iteracji. Zielony CI nie jest formalizacją Lean.

## Zakres, integralność i wersje źródeł

| Rozdział | Git blob SHA po korektach | Wiersze | Dowody | Etykiety | Odsyłacze | Przykłady | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA25 — sterowalność, obserwowalność i stabilizowalność | `3e1bde35f7407ad001423fde5c6a577b338cd573` | **2166** | **17/17** | 47 | 30 | 9 | 0 |
| LA26 — uogólnione twierdzenia Riccatiego | `1c183e4e0f05639cc87b75c8fb485e17b8bbd936` | **1928** | **9/9** | 38 | 45 | 5 | 0 |
| **Łącznie** | | **4094** | **26/26** | **85** | **75** | **14** | **0** |

**[Rejestr per-dowodowy](iteration_25_proof_review_25_26.csv)** zawiera dla każdej z 26 pozycji prawdziwy SHA źródła, zakres wierszy twierdzenia i całego dowodu, typ środowiska, etykietę i osobną merytoryczną adnotację sprawdzanego kroku. Każdy dowód ma sparowane środowisko `proof`, etykiety nie powtarzają się lokalnie. Kontrola zakazanych terminów w treści źródeł nie wykazała naruszeń. Brak rysunków w LA25–26, zatem nie wykonano osobnej inspekcji wizualnej stron PDF. Kolumna `Lean_formalization_reviewed=NIE` nie pozwala pomylić audytu z rzeczywistą kompilacją Lean.

## LA25 — 17 indywidualnych dowodów

1. **Przestrzenie osiągalna i nieobserwowalna.** Ich niezmienniczość wynika z Cayleya–Hamiltona. Sprawdzono, że skończona suma obrazów `im A^k B`, `k<n`, zawiera również wszystkie późniejsze potęgi. Dualnie, `ker O(C,A)` jest największą A-niezmienniczą podprzestrzenią zawartą w `ker C`.
2. **Kryteria Kalmana.** Iteracja `x_N=A^Nx_0+Σ_{j=0}^{N−1}A^{N−1−j}Bu_j` wykazuje osiągalność dokładnie po n krokach, gdy `rank K=n`; wybór celu `z−A^nx` obsługuje dowolne dwa stany. Dla ciągłego sterowania wzór wariacji stałych obowiązuje dla przedziałami ciągłego `u`.
3. **Gramian ciągły i dyskretny.** `ker W_T=ker K*` dla każdego T>0: całka normy kwadratowej zanika wtedy i tylko wtedy, gdy `B*e^{tA*}v≡0`; zróżniczkowanie przy 0 i Cayley–Hamilton dają równoważność. Dla sterowania minimalnej energii `K_Nw=d`, wektor `w_0=K_N*(K_NK_N*)^{-1}d` jest ortogonalny do jądra K_N. Sprawdzono poprawność wzoru na wartość minimalnego kosztu i wymóg `W_N>0`.
4. **Obserwowalność i sprzężenie.** Pierwszych n obserwacji wystarcza dzięki Cayleyowi–Hamiltonowi. Dualność `K(A*,C*)=O(C,A)*` zapewnia równoważność rang. Wykrywalność i stabilizowalność porównano przez sprzężenie hermitowskie, zachowując części rzeczywiste i moduły wartości własnych.
5. **PBH i rozkład Kalmana.** Awaria poziomej macierzy `[(λI−A) B]` jest równoważna istnieniu lewego wektora własnego w anihilatorze przestrzeni osiągalnej. Rozkład na R i iloraz nieosiągalny daje niezmienniczość niesterowalnych wartości własnych dla dowolnego K. W rozkładzie czterech składników U,R₀,N₀,W **nie narzuca się** nieistniejącej A-niezmienniczości dopełnień — interpretacja odbywa się przez podilorazy.
6. **Konstrukcja stabilizującego sprzężenia.** Rezolwenta `(H−μI)^{-1}D` na dowolnym niepustym obszarze otwartym ma w obrazie wektory poza każdą właściwą podprzestrzenią, bo w przeciwnym razie funkcja wymierna i jej rozwinięcie w nieskończoności przeczyłyby sterowalności. Pozwala to wybrać różne μ_j i niezależne wektory własne zamkniętej pętli; daje wystarczalność warunków PBH stabilizowalności.
7. **Obserwator i przykłady.** Błąd `e=x−x̂` spełnia `e'=(A−LC)e` lub `e_(k+1)=(A−LC)e_k`, a jego zanik wynika z poprzednich twierdzeń spektralnych. Zweryfikowano dziewięć przykładów: łańcuch dwóch stanów, gramian o wyznaczniku `T⁴/12`, wzajemną niezależność obserwowalności i sterowalności, stabilizowalność wyłącznie ciągłą dla nieosiągalnego −2, centralny przykład PBH i energię osiągania celu.

## LA26 — 9 indywidualnych dowodów

1. **Koszt półokreślony:** dla `Q=Q*≥0` dodatni pierwiastek `C=Q^(1/2)` spełnia `C*C=Q`, `ker C=ker Q`. Kryterium wykrywalności PBH zależy wyłącznie od tego jądra, zatem nie zależy od wyboru faktoryzacji.
2. **Ograniczenie kosztu:** stabilizowalna para dopuszcza sprzężenie ujemne K₀ stabilizujące D=A−BK₀. Szereg Steina oraz całka Lapunowa dla `H=Q+K₀*RK₀≥0` są bezwzględnie zbieżne również bez `H>0`; zapewniają globalne ograniczenia kosztów optymalnych.
3. **DARE:** rekurencja Bellmana jest poprawna przy `Q≥0`, bo `M_N=R+B*P_NB>0`. Rosnące `P_N` są ograniczone przez koszt sterowania K₀ i mają granicę. Tożsamość energetyczna `P−D*PD=Q+K*RK` oraz wykrywalność wykluczają niestabilny wektor własny D, nawet gdy `P` jest tylko półokreślona. Jednoznaczność hermitowskich stabilizujących rozwiązań wynika z `E=D₁*ED₂`.
4. **DRE i CARE:** dla skończonego horyzontu minimalizacja przez uzupełnienie kwadratu zapewnia `S(T)≥0` i monotoniczność. Porównanie z kosztem zerowego sterowania wyklucza skończone wybuchy rozwiązania Riccatiego. Granica S(T) istnieje przy stabilizowalności, `S'(T)=F(S(T))→F(P)` wraz ze zbieżnością S wymusza `F(P)=0`. Z CARE i wykrywalności wynika stabilność Hurwitza D=A−BR⁻¹B*P. Jednoznaczność dowiedziono przez porównanie nieskończonych kosztów dla dwóch stabilizujących sprzężeń.
5. **Koszt optymalny:** ważne przejście do nieskończoności przy `Q≥0` korzysta z dodatkowego lematu: `u,Cx∈ℓ²` lub `L²` i wykrywalność pozwalają napisać dynamikę jako stabilny układ z wymuszeniem o skończonej energii. Oszacowanie splotu po rozdzieleniu na skończoną część i ogon daje `x_k→0` albo `x(t)→0`, co zeruje wyraz końcowy w tożsamości kosztu. Dodatnia określoność R i M zapewnia jednoznaczność sterowania.
6. **Kontrprzykłady i hipotezy:** przejrzano pięć przykładów, w tym `A=2,B=1,Q=4/5` z DARE `p=4` stabilizującym i `p=−1/5` niestabilizującym; `A=1,B=1,Q=3` z CARE `p=3` i `p=−1`; półokreślony `Q=diag(4/5,0)` z singularnym P; brak wykrywalności `Q=0` z granicą `P=0` niestabilizującą; brak stabilizowalności `B=0` i brak nieujemnego rozwiązania.

## Korekty plików źródłowych

Poprawiono cztery **tezy**, zachowując dowody, przykłady, etykiety i wszystkie wzory:

- LA25: `thm:lin25-kalman` podaje teraz `n,m≥1`, `A∈Mat_(n×n)(C)`, `B∈Mat_(n×m)(C)`, przestrzeń stanu i sterowania; `thm:lin25-pbh` jawnie kwantyfikuje `n,m≥1` i określa rozmiary A,B. Commit `c49b95f8c296408d006e0996c79515fe99f0f1d9`.
- LA26: `thm:lin26-dare` i `thm:lin26-care` podają `n,m≥1`, pełne rozmiary A,B,Q,R, `Q=Q*≥0`, `R=R*>0`, stabilizowalność i wykrywalność. Commit `699f3bdbc5e6c243e4c613edaf056c7fcf8626a3`.

## Testy i status CI

Nowy [test LA25–26](../../../tools/test_linear_algebra_la25_la26_control_riccati.py) włączono do `.github/workflows/linear-algebra-chapter.yml` i filtra ścieżek. Wyczerpująco przelicza małe macierze nad F₂,F₃: rangę Kalmana, identyczność dualnej obserwowalności, Cayleya–Hamiltona dla przestrzeni osiągalnej i nieobserwowalnej, PBH tam, gdzie χ rozszczepia się w ciele, niezmienniczość rangi przy sprzężeniu. Osobno dla rzeczywistych i zespolonych macierzy sprawdza gramiany, ich dodatniość i minimalną energię, efekty sprzężenia stanu i obserwatora oraz nieujemną granicę DARE/CARE przy Q o niezerowym jądrze, niestabilnej otwartej pętli i stabilizowalnej parze. Obejmuje też jawny brak wykrywalności.

**Przebieg początkowy** [45069955546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069955546) zakończył się `failure` w nowym teście przez **błędne łańcuchowe porównanie boolean z rangą w języku Python**, nie przez kontrprzykład do dualności. Skrypt poprawiono w commicie `0deb2386686c2119b6507fe59413b4a1241e94b5`. W [ponownym CI 45070080608](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070080608) nowy krok LA25–26 ma już **`completed/success`**. **Cały workflow, dwukrotną kompilację PDF i liczbę asercji należy potwierdzić osobno w końcowym logu.**

## Zakończenie i plan

Po udokumentowanych indywidualnych audytach iteracji 17–25 sprawdzono **337/382** dowodów; **pozostało 45**: LA27 (**10**), LA28 (**10**), LA29 (**6**), LA30 (**3**), LA31 (**6**), LA32 (**10**). Następne bloki: LA27–28, następnie LA29–32. Po uzyskaniu 382/382 — jeszcze jedna odrębna sceptyczna iteracja globalna z prawdziwą inspekcją stron PDF, grafu odsyłaczy, terminologii i regresji matematycznych.
