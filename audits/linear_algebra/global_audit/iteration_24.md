# Algebra liniowa — audyt globalny, iteracja 24: LA21–24, 34 dowody

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Poprzednio:** [iteracja 23](iteration_23.md).

**Wynik przeglądu:** wszystkie **34 tezy wraz z pełnymi dowodami** przeczytano indywidualnie i przeanalizowano; wykryto i poprawiono **6 miejsc wymagających uściślenia hipotez i interpunkcji** w rozdziale LA24. Pozostałe kontrolowane argumenty matematyczne nie wymagały modyfikacji. **Testy i przegląd dowodów nie stanowią formalizacji Lean.**

## 1. Skontrolowane wersje źródeł

| Rozdział | Blob SHA pliku | Wiersze | Dowody | Etykiety | Odsyłacze | Przykłady | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA21 — komutanty i centralizatory | `6527ae1a6daca48717e6a5f5e83958271abb16f5` | 899 | **9/9** | 25 | 37 | 7 | 0 |
| LA22 — równania Sylvestera i Lapunowa | `dfa3d790bfed4c92c66642ea626a6213bc06ad3f` | 936 | **10/10** | 25 | 25 | 5 | 0 |
| LA23 — równanie dyskretne i Schur | `bbd199baed1ee2c1a88843aad9fbfd0eac665d22` | 965 | **7/7** | 25 | 12 | 6 | 0 |
| LA24 — Riccati i sterowanie LQR, **po korekcie** | `52335170d324782c97a70331b7b834f0d2b1c5cc` | 1479 | **8/8** | 26 | 31 | 3 | 0 |
| **Razem** | | **4279** | **34/34** | **101** | **105** | **21** | **0** |

[Rejestr per-dowodowy](iteration_24_proof_review_21_24.csv) zawiera zakresy tezy i dowodu, dokładną wersję blob SHA, adnotację o krytycznych krokach, status poprawek LA24 oraz osobne pole `formal_Lean_review=NIE`. Wszystkie 34 środowiska `proof` mają koniec, a w każdym rozdziale etykiety są lokalnie niepowtarzalne.

## 2. LA21 — dziewięć dowodów

- Algebra komutanta i grupa elementów odwracalnych są niezmiennicze względem podobieństwa, ponieważ conjugation `S↦USU^{-1}` zachowuje równanie `ST=TS`. Endomorfizmy `K[t]`-modułu `V_T` identyfikują się dokładnie z komutantem.
- Izomorfizm `Hom_(K[t])(K[t]/(f),K[t]/(g)) ≅ K[t]/(gcd(f,g))` skontrolowano przez obraz klasy `[1]`, warunek `fy=0` oraz skrócenie `g=d g_0`, `f=d f_0` w dziedzinie całkowitości `K[t]`. Obejmuje on względnie pierwsze f,g.
- Wzór na wymiar `C(T)` z czynników niezmienniczych obejmuje `Σ_{i,j}deg gcd(f_i,f_j)` oraz wersję `Σ_i(2(r−i)+1)deg f_i`; sprawdzono liczbę uporządkowanych par o mniejszym indeksie i przypadek `dim V=0`.
- Dolna granica `n` osiągana jest dokładnie przez operatory cykliczne; górna `n²` dokładnie przez operatory skalarne. Dla dzielników elementarnych wymiar komutanta to `Σ_p deg p Σ_k B_{p,k}²`, gdzie `B_{p,k}` liczy bloki wykładnika co najmniej k. Zweryfikowano `deg p=2` i charakterystykę 2.
- Dla ciała skończonego `F_q` jednostki komutanta operatora cyklicznego odpowiadają jednostkom `K[t]/(m_T)`; przez CRT liczba elementów wynosi `q^n ∏(1−q^(−deg p))`. Skontrolowano przykład `C((t²+t+1)²)` nad F₂ z `16` elementami komutanta i `12` odwracalnymi.

## 3. LA22 — dziesięć dowodów

- Jądro liniowego operatora Sylvestera `X↦AX−XB` to przestrzeń przeplotów modułów `K[t]`. Wymiar jest `Σ deg gcd(f_i,g_j)`, a każde niepuste włókno równania `AX−XB=C` jest przesunięciem jądra.
- Z faktu, że przestrzeń macierzy ma wymiar `nm`, wynika kryterium: **jedno rozwiązanie dla każdego C** iff `gcd(χ_A,χ_B)=1`, bez konieczności algebraicznego domknięcia K. Wzór z wielomianem charakterystycznym h=χ_A wykorzystuje **h(B) odwracalne** przez Bézout i poprawne mnożenie przez `h(B)^{-1}` z prawej strony. Zbadano ujemny znak w formule.
- Na różnych blokach Jordana operator `X↦N_aX−XN_b` ma potęgę `(a+b−1)` równą zeru, również w charakterystyce dodatniej; skończony szereg geometryczny daje odwrotność Sylvestera dla `λ≠μ`. Dla wspólnej wartości własnej wymiar jądra to `min(a,b)`.
- Ciągłe twierdzenie Lapunowa: dla macierzy Hurwitza całka `P=∫_0^∞ e^{tA*}Qe^{tA}dt` jest bezwzględnie zbieżna dzięki oszacowaniu wielomian razy malejąca wykładnicza, daje `P=P*>0` i jedyne rozwiązanie równania **wśród wszystkich macierzy**, nie tylko hermitowskich. Równanie z P,Q dodatnimi wyklucza wartości własne o nieujemnej części rzeczywistej. Wyprowadzono pochodną funkcji energii.

## 4. LA23 — siedem dowodów

- `ρ(A)<1` iff `A^k→0` iff `||A^k||≤Mr^k` dla odpowiedniego `r∈(ρ(A),1)`. W dowodzie sprawdzono nilpotentne bloki λ=0, w tym przypadek potęgi zerowej i niediagonalizowalności.
- Dyskretne równanie Steina ma dla Schur A jedyne rozwiązanie `P=Σ_{k≥0}(A*)^k QA^k` i `P>0` dla Q>0. Nie założono odwracalności A: wyraz k=0 zapewnia dodatnią określoność, a zanik `A^k` zapewnia jednoznaczność.
- Energia maleje `E_(k+1)−E_k=−x_k*Qx_k`; z `P−Q=A*PA≥0` i estymat wartości własnych P,Q otrzymano **`γ=1−q_min/p_max∈[0,1)`** bez nieuprawnionego dzielenia przez A. Całkowity koszt energii jest równy `x_0*P x_0`.
- Widmo endomorfizmu `X↦A*XA` to wszystkie iloczyny `conj(λ_i)λ_j`, również bez diagonalizowalności A: dowód wykorzystuje triangularizację Schura i jednostki macierzowe. Unikalność rozwiązania dowolnego równania Steina **nie implikuje Schur-stabilności**, co pokazują przykłady.
- Dokładne próbkowanie `e^{hH}` zachowuje równoważność Hurwitza/Schura dla każdego h>0, lecz jawny Euler wymaga `2 Reλ+h|λ|²<0`. Rachunek przykładu 2×2 i warunki dodatniej określoności zweryfikowano osobno.

## 5. LA24 — osiem dowodów i sześć poprawek sformułowań

Poprawiono w oryginalnym pliku LaTeX **dwa twierdzenia** (`thm:lin24-dare-recursion`, `thm:lin24-dre`) oraz **cztery definicje** (`def:lin24-discrete-cost`, `def:lin24-dare`, `def:lin24-continuous-cost`, `def:lin24-care`). We wszystkich sześciu miejscach podano jawnie `n,m≥1`, `A∈Mat_(n×n)(C)`, `B∈Mat_(n×m)(C)`, `Q∈Mat_(n×n)(C)`, `R∈Mat_(m×m)(C)`, `Q=Q*>0`, `R=R*>0`, zamiast polegać na globalnych „założeniach rozdziału”. Po wprowadzeniu osobnych zdań poprawiono też wielkie litery w początkach zdań w obu twierdzeniach. **Treść równań, dowody i etykiety pozostały niezmienione**. Pierwsze dwie poprawki w commicie `a88e57e06dcfe1c4e733abe45e29a0414713a8df`, uzupełnienia definicji i interpunkcji w `061005098f476ba5e6dfd083490ef2a82fbf3f4c`. Są to rzeczywiste poprawki źródeł.

- Rekurencja DARE: uzupełnienie kwadratu przy `M_N=R+B*P_N B>0` daje unikat pierwszego sterowania i `P_N≥0`; monotoniczność wartości optymalnej z nieujemności kosztów; ograniczenie z góry przez rozwiązanie Steina dla sterowania zerowego, gdy A jest Schur.
- Stabilizujące DARE: monotoniczne `P_N↑P≥Q>0`, ciągłość inwersji `R+B*P B`, równanie `P=Q+K*RK+(A−BK)*P(A−BK)` i Schur-stabilność zamkniętej pętli. **Jednoznaczność dwóch stabilizujących rozwiązań** wynika z `D=A_1* D A_2` i zaniku ich potęg. Dodatnie rozwiązanie nie może być niestabilizujące przy Q>0.
- Dla sterowania na nieskończonym horyzoncie zakończenie tożsamości teleskopowej wymaga `x_N→0`; dowód wykorzystuje fakt, że dodatnio określony Q i skończony koszt implikują `Σ||x_k||²<∞`. Warunek `u=−Kx` daje jedyne minimum.
- Różniczkowe DRE: lokalna teoria ODE, hermitowskość, tożsamość z kwadratem `u+R^{-1}B*S x` oraz minimalizujący liniowy układ stanu. Globalne przedłużenie wynika z jednostajnego oszacowania `S(T)` przez koszt sterowania zerowego na każdym skończonym przedziale, co wyklucza skończony blow-up.
- Stabilizujące CARE: monotoniczność `S(T)` i ograniczenie przez całkowy operator Lapunowa dla Hurwitz A, `P≥S(1)>0`, argument `S'(t)=F(S(t))→F(P)` i zbieżność S(t) wymuszają `F(P)=0`. Z CARE wynika Hurwitz-stabilność `A−BR^{-1}B*P`, a dwa stabilizujące rozwiązania mają ten sam koszt i tę samą formę P.
- Przy sterowaniu ciągłym ze skończonym kosztem `x,u∈L²`, stąd `x'∈L²`; całkowanie pochodnej `||x||²` i Cauchy–Schwarz dają `x(t)→0`. To uzasadnia przejście do nieskończonego horyzontu i wyznacza jedyny (prawie wszędzie) minimizator.

## 6. Niezależne testy regresyjne i ciągła integracja

Dodano [tools/test_linear_algebra_la21_la24_control.py](../../../tools/test_linear_algebra_la21_la24_control.py) do `.github/workflows/linear-algebra-chapter.yml` wraz z filtrem ścieżki. Wyczerpujące testy w wybranych rozmiarach nad `F₂,F₃,F₅` weryfikują: granice i kryteria równości wymiaru komutanta, komutanty operatorów cyklicznych, liczbę elementów odwracalnych `K[t]/(f)` (również nierozkładalne i wielokrotne pierwiastki), jądra map Sylvestera i warunek względnej pierwszości wielomianów charakterystycznych, złożone bloki Jordana. NumPy użyto w deterministycznych testach zespolonych równań ciągłych i dyskretnych, dodatniej określoności i unikalności operatorów rozwiązań oraz równań Riccatiego DARE, DRE, CARE, z przypadkami skalarnego niestabilizującego rozwiązania i dwóch stanów.

**Pierwszy przebieg** [45068874857](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068874857) zakończył się **failure** przez niestabilne numerycznie sortowanie zespolonego spektrum operatora Steina w nowym teście; nie był to kontrprzykład matematyczny. Poprawiono test, dopasowując multizbiór wartości własnych z tolerancją (commit `5290b51e3236b3a71ac1860ab4cfb2a31d110329`). **Zweryfikowany przebieg po poprawce: [45069113282](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069113282) — `completed/success` dla pełnego workflow** na commicie `19e86667b8ae9f5d21be9de1350931926be4e2b6`: z logu testu **12 467 / 12 467 PASS, 0 FAIL**, SHA256 skryptu `32690d19c1d2834606d9a084553300ad338cc1a727bd7cd8f1698ff4a5ea6a11`. Osobno potwierdzono w tym przebiegu **sukces dwukrotnej kompilacji książki PDF, kontroli nierozwiązanych odsyłaczy i eksportu samodzielnego rozdziału**. **Istotne: późniejszy commit `061005098f476ba5e6dfd083490ef2a82fbf3f4c` obejmujący ostateczne brzmienie czterech definicji LA24 ma własny [przebieg CI 45069279245](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069279245), również zakończony `completed/success` dla CAŁEGO workflow**, w tym nowy test LA21–24, dwukrotną kompilację PDF oraz kontrolę odsyłaczy i eksport rozdziału. Ten przebieg potwierdza też późniejszy blob źródła LA24 `52335170d324782c97a70331b7b834f0d2b1c5cc` użyty w końcowym rejestrze.

## 7. LaTeX, graf odsyłaczy, dalsze prace

- **4279 wierszy, 34 środowiska dowodów z `\end{proof}`, 101 etykiet bez lokalnych powtórzeń, 105 odsyłaczy, 21 przykładów.** W tych czterech plikach brak ilustracji i środowisk TikZ. Kontrola terminologiczna nie wykazała odrzuconych określeń w prozie. Rendering strony PDF nie był oglądany wizualnie.
- **Postęp globalny po iteracji 24: 311/382 indywidualnie przejrzanych dowodów. Pozostało 71 dowodów, wszystkie w LA25–32.** To nie zastępuje wcześniejszych audytów rozdziałowych; po zamknięciu pełnej ewidencji należy przeprowadzić dodatkowy sceptyczny audyt końcowy, w tym rzeczywistą inspekcję PDF, zgodności etykiet, treści matematycznych, języka i przykładów.
