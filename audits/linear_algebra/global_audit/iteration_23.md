# Algebra liniowa — audyt globalny, iteracja 23: LA17–20, 27 indywidualnych dowodów

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 22](iteration_22.md).

**Wynik: CZYSTY W BADANYM ZAKRESIE.** Przeczytano pełne sformułowania oraz dowody wszystkich **27 środowisk `proof`** w LA17–20, 18 przykładów, sprawdzono strukturę, etykiety, odsyłacze i terminologię. Nie znaleziono koniecznej korekty matematycznych źródeł. **Nie przeprowadzono audytu LA21–24 w tej iteracji**, nie został on zaliczony do postępu. Nie wykonano formalizacji Lean ani samodzielnej wizualnej inspekcji stron PDF.

## 1. Dokładny zakres

| Rozdział | Blob SHA Git | Linie | Dowody | Etykiety | Odsyłacze | Przykłady | TikZ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA17 — postać Jordana | `05b93309d0e444f1c3fcbe3489cfd98a0f02846f` | 661 | **7/7** | 21 | 8 | 4 | 0 |
| LA18 — Jordan–Chevalley i funkcje macierzy | `ef815633cf3a1f795d912c510fbc8575f21e464d` | 790 | **6/6** | 21 | 13 | 4 | 0 |
| LA19 — Frobenius i czynniki niezmiennicze | `dd289d5c86452910a89d60ddfbcc558ef6d5be85` | 720 | **7/7** | 20 | 14 | 4 | 0 |
| LA20 — dzielniki elementarne | `8d585c7f4c208990ad5f82222cc47f586144c138` | 727 | **7/7** | 22 | 23 | 6 | 0 |
| **Razem** | | **2898** | **27/27** | **84** | **58** | **18** | **0** |

[Indywidualny rejestr 27 sprawdzonych twierdzeń](iteration_23_proof_review_17_20.csv) zawiera dla każdej pozycji: poprawnie odczytany tytuł ze źródła, etykietę, wersję blob SHA, zakres wierszy tezy i dowodu, spersonalizowaną kontrolę matematyczną i informację o braku sprawdzenia formalnego w Lean. Przy migracji z wcześniejszego rejestru naprawiono odczyt tytułu LA20 o `K[t]`, gdyż w pliku bazowym występuje niezacytowany przecinek/znak nawiasu, przez który jego pole tytułu było ucięte. Nowy rejestr zawiera poprawnie cytowane pola CSV.

## 2. LA17 — konstrukcja i jednoznaczność postaci Jordana

- **Filtracja jąder:** `K_k=ker N^k` jest rosnąca. Po pierwszym zatrzymaniu przyrostów następuje stabilizacja; dla nilpotentnego N na niezerowym V liczba ścisłych włączeń wynosi najwyżej `dim V`, a więc `N^n=0`.
- **Łańcuchy i baza Jordana:** niezależność wektorów łańcucha uzasadniono kolejnymi zastosowaniami potęg N. Przy indukcji po `dim V` baza Jordana dla `im N` daje przedłużane łańcuchy, a jądro dopełnia o łańcuchy jednowektorowe. W szczególności w dowodzie udokumentowano sytuację N=0 i V=0; nie użyto założenia algebraicznej domkniętości ciała.
- **Zliczanie bloków:** `dim ker N^k=Σ_i min(k,s_i)` i drugie różnice `2d_k−d_{k-1}−d_{k+1}` wyznaczają liczbę bloków rozmiaru k. W postaci Jordana operatora T wartości własne różne od λ nie wnoszą elementów do `ker(T−λI)^k`, gdyż `(μ−λ)I+N_s` jest odwracalny przez skończony szereg.
- **Warunek na ciało:** rozkład m_T na czynniki liniowe nad K jest konieczny i wystarczający dla zwykłej postaci Jordana nad K; formuły na m_T i χ_T z bloków są poprawne także w wymiarze 0. Sprawdzono cztery przykłady, w tym blokowy typ `3+1+2` i nilpotentne typy `3`, `2+1`.

## 3. LA18 — Jordan–Chevalley i rachunek funkcji

- **Rzuty wielomianowe:** tożsamość Bézouta przy dwóch względnie pierwszych wielomianach `f_λ=(t−λ)^{a_λ}`, `g_λ=m_T/f_λ` daje `P_λ=q_λ(T)`; działanie P na każdym uogólnionym składniku jest niezależne od wyboru wielomianu i daje parami ortogonalne w sensie algebraicznym (niekoniecznie ortogonalne względem iloczynu skalarnego) rzuty, których suma to `I_V`.
- **Jednoznaczność S+N:** dla przemiennych składników `S` diagonalizowalnego i `N` nilpotentnego przestrzenie własne S są niezmiennicze dla N, a więc zawierają się w odpowiednich przestrzeniach uogólnionych T. Z bezpośredniości sumy otrzymujemy jednoznaczne `S=Σλ P_λ`, `N=T−S`, oba jako wielomiany w T. Uwzględniono V=0.
- **Dodatnia charakterystyka:** w rachunku wielomianowym użyto współczynników **pochodnych Hassego**, określonych przez `p(λ+u)`, a nie błędnego dzielenia przez `j!` w dowolnym ciele. Formuła na T^k używa współczynników dwumianowych interpretowanych w K; przy k=j=0 zachowuje konwencję składnika stałego.
- **Część analityczna:** twierdzenie o f(T) ograniczone do zespolonych funkcji holomorficznych wokół widma; skończone rozwinięcia Taylora przy nilpotentnym N gwarantują multiplikatywność. Wykładnicza `e^{zT}` jest bezwzględnie zbieżna w normie operatorowej, ma wzór z `e^{zλ}` i skończoną sumą potęg N oraz własność grupową. Rachunki czterech przykładów obejmują projector, rozkład oraz rozwiązanie ODE.

## 4. LA19 — Smith i Frobenius nad K[t]

- **Moduł operatora:** `K[t]` działa przez p(T), a jego izomorfizmy odpowiadają przeplotom operatorów. Iloraz `K[t]^n/(tI−A)K[t]^n` jest poprawnie uzasadniony przez ewaluację `f(t)↦ΣA^k v_k` i teleskopową równość `t^kI−A^k=(tI−A)Σ_j t^{k−1−j}A^j`.
- **Postać Smitha:** redukcja wielomianowego elementu wiodącego dzieleniem Euklidesowym i przez dołożenie elementu z resztą z dolnego bloku wymusza ścisły spadek stopnia, co zapewnia terminację. Operacje na wierszach i kolumnach zachowują ideały minorów; moniczne `Δ_k` odtwarzają czynniki `d_k=Δ_k/Δ_{k−1}`. Przy n=0 działa pusta rodzina.
- **Bloki towarzyszące:** `K[t]/(f)` ma bazę `1,t,...,t^{d−1}`, a operator mnożenia przez t ma wielomian minimalny oraz charakterystyczny równy f. Z postaci Smitha macierzy `tI−A` otrzymujemy jednoznaczny łańcuch czynników niezmienniczych, po pominięciu czynników stopnia zero, postać Frobeniusa, kryterium podobieństwa i `T` cykliczny iff `m_T=χ_T` dla n≥1.
- **Przykłady:** sprawdzono macierz nilpotentną z czynnikami `1,t,t²`, diagonalną `diag(1,1,2)` i obrót rzeczywisty z nierozkładalnym `t²+1`. Zwrócono uwagę, że **same χ_T i m_T nie klasyfikują operatorów**.

## 5. LA20 — dzielniki elementarne i nierozkładalne bloki pierwotne

- **Chińskie twierdzenie o resztach:** odtwarzanie klasy modulo iloczynu z klas modulo `f_i` przez funkcje `e_i=u_i∏_{j≠i}f_j` sprawdzone, wraz z parami względną pierwszością.
- **Jednoznaczne dzielniki elementarne:** każdy f_i rozpisany na potęgi p^a, następnie CRT i companion. Przy rekonstrukcji łańcucha Smitha wykładniki dla każdego p wyrównuje się **zerami od lewej**, nie od prawej; zapewnia to `f_i|f_{i+1}` i jednoznaczność.
- **Jądra `p(T)^k`:** na `K[t]/(p^a)` jądro mnożenia przez p^k ma wymiar `deg(p)min(k,a)`, a inne nierozkładalne czynniki nie dają wkładu. Pierwsze i drugie różnice po podzieleniu przez `deg(p)` odtwarzają liczbę bloków. **Istotne dla `deg p>1`**, np. q=t²+1 nad R, p=t²+t+1 nad F₂.
- **Jordan i Frobenius:** dla liniowego p=t−λ z bazy `u^{a−1},...,1` otrzymujemy J_a(λ); zachowano krotności bloków. Przeanalizowano przykład macierzy 6×6 o tych samych m_T, χ_T i różnych jądrach oraz wszystkie pozostałe przykłady rozdziału.

## 6. Niezależny test regresyjny i CI

Nowy [test dokładny LA17–20](../../../tools/test_linear_algebra_la17_la20_classification.py) wykonuje rachunki wyłącznie w arytmetyce skończonych ciał pierwszych **F₂/F₃/F₅** bez NumPy i bez pakietów zewnętrznych. Test oblicza niezależnie minory wielomianowe `tI−A`, wyznacznik wielomianowy, największe wspólne dzielniki minorów i czynniki Smitha, a także minimalny wielomian przez liniową zależność potęg macierzy. Kontroluje równości `d_1|...|d_n`, `χ_A=∏d_i`, `m_A=d_n`, Cayleya–Hamiltona, minimalność modułu companion; dalej klasyfikuje jądra bloków p^a oraz dla wszystkich małych rozkładów n oblicza filtrację bloków Jordana. Odrębny test konstrukcyjny CRT sprawdza wielomianowe rzuty, semisimple S, nilpotentne N, komutowanie i formułę Taylora z pochodnymi Hassego, również w charakterystyce 2.

Test włączono do `.github/workflows/linear-algebra-chapter.yml` z filtrem nowej ścieżki. [GitHub Actions dla wersji z testem](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068148560): nowy krok **„Verify LA17-LA20 exact Smith, Frobenius, Jordan, Chevalley and primary divisors”** uzyskał `completed/success`. Po zakończeniu całego CI należy osobno odnotować wynik PDF i dokładną liczbę kontroli z logów.

## 7. Redakcja, struktura, dalszy plan

- Łącznie **2898 linii**, **27** sparowanych środowisk dowodów, **84** etykiety bez lokalnych duplikatów, **58** odsyłaczy, **18** przykładów, **0** rysunków TikZ w kontrolowanych czterech rozdziałach. Weryfikacja źródeł nie wykazała obecności zakazanych terminów w prozie. Źródła matematyczne pozostawiono bez zmian.
- Globalny rejestr indywidualnego audytu obejmuje po tej iteracji **277/382** dowodów. Do zamknięcia brakuje **105**: LA21–24 (**34**) oraz LA25–32 (**71**). Nie należy mylić tego rejestru z wcześniej przeprowadzonymi, wielokrotnymi audytami rozdziałów.
- **Następny etap:** dokładna kontrola LA21–24 (komutanty, równania Sylvestera i Lapunowa, stabilność Schura, równania Riccatiego i sterowanie) oraz nowe testy regresyjne; potem LA25–32. Po uzyskaniu kompletnego rejestru wykonać jeszcze jeden odrębny sceptyczny audyt globalny, w tym kontrolę renderingu PDF, grafu odsyłaczy i języka.
