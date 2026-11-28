# Algebra liniowa — rozdział 14, audyt II (niezależny audyt stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`  
**Zbadana niezmieniona treść:** `09fda2f083ad5fbd752699606d42862eb7022987`  
**Raport poprzedni:** `audits/linear_algebra/ch14_iteration_01.md`.

## Kontrola formalna i matematyczna

Ponownie sprawdzono każdą definicję, twierdzenie, dowód, przykład i ograniczenie zakresu. Audyt skupiał się na możliwych lukach ukrytych przez intuicję spektralną, przypadkach wymiaru zero, elementach odróżniających `R` od `C` i formalnym pochodzeniu własności sprzężeń. Rozdział 14 nie zakłada twierdzenia spektralnego w dowodzie samego twierdzenia spektralnego.

1. **Twierdzenie charakterystyczne i krotności:** `λ` jest wartością własną dokładnie gdy `T-λI` nie jest odwracalne i `χ_T(λ)=0`; zapis niezależności `χ_T` od bazy jest prawidłowy, a dla `dim V=0` wielomian stały `1` nie ma pierwiastków. Blok macierzy `[[λI_g,C],[0,D]]` udowadnia `g_T(λ)≤a_T(λ)`.
2. **Diagonalizowalność:** bezpośredniość sumy różnych przestrzeni własnych udowodniono wielomianem `R_k(T)` — wszystkie różnice wartości własnych są odwracalne jako niezerowe skalary ciała. Warunek `Σ g=n` jest równoważny bazie własnej, a wersja z równością `a=g` wymaga jawnie rozszczepienia wielomianu nad `K`. Blok Jordana `[[1,1],[0,1]]` jest prawidłowym kontrprzykładem nad dowolnym ciałem.
3. **Schur:** po wyborze wektora własnego ogólnego operatora `T` nie można założyć niezmienniczości `e_1^⊥`. Dowód poprawnie stosuje *kompresję* `P_{e_1^⊥}T|_{e_1^⊥}`, a nie ograniczenie `T|_{e_1^⊥}`. Indukcyjna baza ortonormalna daje w macierzy `[[λ,*],[0,R_1]]`, w której `R_1` jest trójkątna. Przypadek `n=0` sprawdzono.
4. **Normalność:** tożsamość `||Nv||=||N^*v||` wyprowadzono wprost z `N^*N=NN^*`. Ponieważ `T-λI` pozostaje normalny, z `Tv=λv` wynika `T^*v=conj(λ)v`. Dowód tej implikacji emph{nie} korzysta z własnej bazy spektralnej, więc nie ma błędnego koła.
5. **Główne twierdzenie spektralne:** przestrzeń `e_1^⊥` jest niezmiennicza zarówno dla `T`, jak i dla `T^*`. Sprzężeniem ograniczenia `T|_W` jest `T^*|_W`, więc normalność przechodzi na ograniczenie. Stosowanie indukcji jest legalne. W przeciwnym kierunku `U^*AU=D` z diagonalnym `D` implikuje normalność. Wariant operatorów hermitowskich daje `λ∈R`, a unitarnych `|λ|=1`.
6. **Rzeczywiste twierdzenie spektralne:** rzeczywista symetryczna macierz jest hermitowska po kompleksyfikacji. Rzeczywistość `λ` umożliwia rozdzielenie `z=x+iy` na niezerowy rzeczywisty wektor własny; w rzeczywistym dopełnieniu ortogonalnym pozostaje operator symetryczny, więc indukcja daje emph{rzeczywistą} bazę własną. Nie rozszerzono twierdzenia fałszywie na rzeczywiste macierze ortogonalne: rotacja z wielomianem `t²+1` nie ma rzeczywistych wartości własnych.
7. **Rzuty i wielomiany:** ortogonalna suma przestrzeni własnych `E_λ` daje samosprzężone idempotenty `P_λ`, które są wzajemnie ortogonalne i sumują się do `I`. Wielomian interpolacyjny o wartości `1` w `λ` i `0` w pozostałych wartościach daje `P_λ`. Rachunek `p(T)=Σ p(λ)P_λ`, wzory na ślad, wyznacznik i odwrotność wynikają ze współrzędnych w bazie własnej; uwzględniono puste sumy i iloczyny.
8. **Rayleigh, norma i określoność:** iloraz `h(v,Tv)/h(v,v)` dla samosprzężonego `T` jest rzeczywistą kombinacją wypukłą jego wartości własnych, ze współczynnikami `|c_j|²/Σ|c_k|²`; dzięki temu nierówności i warunki osiągnięcia ekstremów są prawidłowe. Dodatnia (pół-)określoność odpowiada dodatnim (nieujemnym) wartościom własnym; norma operatora normalnego jest maksymalnym modułem wartości własnej w niezerowym wymiarze.
9. **Jednoczesna diagonalizacja:** przemienność `ST=TS` sprawia, że `T` zachowuje `E_λ(S)`; samo-sprzężoność `T` przechodzi na każde ograniczenie, a ortogonalne połączenie baz własnych daje wspólną bazę bez wymagania prostych wartości własnych.
10. **Przykłady:** `H=[[2,i],[-i,2]]` ma wartości `1,3`, niezależne ortonormalne wektory `(-i,1)/sqrt(2)`, `(i,1)/sqrt(2)`; `A=[[2,1],[1,2]]` ma rzuty `P_3=(A-I)/2`, `P_1=(3I-A)/2`. Wariant `diag(1,i)` jest normalny, ale nie samosprzężony. Rachunki zostały potwierdzone bez postulowania twierdzenia wyższego rzędu.

## Sprawdzenia techniczne

- Rozdział 14: **1455 wierszy, 39 etykiet, 22 odsyłacze**.
- Cała książka 01–14: **574 unikalne etykiety, 245 poprawnych odsyłaczy**, zrównoważone środowiska LaTeX, poprawne importy i manifest.
- Test `tools/test_linear_algebra_spectral.py`: 108 konfiguracji normalnych unitarnie podobnych do diagonalnych, 38 kontroli form hermitowskich i ilorazu Rayleigha, 8 przypadków operatorów przemiennych i nienormalnych; wewnątrz konfiguracji sprawdzono również normy, rzuty i kalkul wielomianowy.
- W [CI 44927318488](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44927318488) pełny PDF miał **151 stron, zero ostrzeżeń LaTeX**, a wszystkie regresje przeszły. Sprawdzania CLI i rozdziałów z tego samego commitu były zielone.
- Skorygowano wyłącznie drobną omyłkę w **raporcie audytu I**: identyfikator wcześniejszego wyniku to `prop:lin12-zmiana-ortonormalna`, nie `thm:lin12-zmiana-ortonormalna`. Właściwy rozdział i jego odsyłacze były już poprawne.

## Decyzja

**Audyt II — czysty.** Nie znaleziono kolejnych usterek w sformułowaniach matematycznych, założeniach, dowodach ani przykładach. Plik rozdziału 14 pozostawiono bez zmian. Po audycie I, czystej kontroli II i zielonym CI uznajemy rozdział 14 za **stabilny i zamknięty**. Rozdziały 01–14 są oznaczone w książce jako stabilne. Commit raportowy uruchamia własny przebieg CI, którego wynik sprawdza się osobno.
