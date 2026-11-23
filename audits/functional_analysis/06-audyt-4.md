# Analiza funkcjonalna — rozdział 06 — audyt 04 (niezależna kontrola potwierdzająca)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/06-twierdzenie-hahna-banacha-i-ciagly-dual.tex`.  
**SHA źródła:** `c8caeb6a6c102e6bfa4ad4560c6a0f3d6c682000`, niezmieniony od audytu 06/02 i pierwszej czystej kontroli 06/03.  
**Wynik matematyczno-redakcyjny:** **CZYSTY — drugi kolejny czysty audyt, 2/2**. Po potwierdzeniu CI i PDF rozdział 06 można uznać za **STABILNY**. Nie zmieniono źródła.

## Metodologia

Przeprowadzono ponowny, niezależny audyt całego aktualnego rozdziału, a nie wyłącznie odczyt poprzedniego raportu. Przeanalizowano sformułowania wszystkich wyników, wszystkie **17 dowodów** i **5 środowisk przykładów**, również w konfiguracjach brzegowych: funkcje podliniowe z wartościami ujemnymi, pusta podprzestrzeń lub zerowy funkcjonał, przestrzenie nie-Hausdorffa, nietrywialna część urojona, niezamknięte podprzestrzenie, puste zbiory indeksów i nieosiągane infima odległości. Testy regresyjne są diagnostyką konkretnych modeli, a nie poświadczeniem dowodu ogólnego.

## Weryfikacja 17 dowodów — 17/17 PASS

1. **Kryterium ciągłości funkcjonału:** otoczenie z ograniczeniem `|f|<1` skaluje się do otoczenia z `|f|<ε`; ciągłość w zerze równoważna ciągłości wszędzie dla odwzorowania liniowego.
2. **Jednowymiarowe przedłużenie:** przedstawienie `m+t x_0` jest jednoznaczne; dla `t>0` i `t<0` otrzymuje się odpowiednie górne/dolne ograniczenia na `a`. Z `f(y+z)≤p(y+z)≤p(y−x_0)+p(z+x_0)` wynika `L≤R`. Ponieważ `L≥−p(−x_0)`, `R≤p(x_0)` i `L≤R`, obie wartości są skończone. Nie zakłada się `p(x)≥0`.
3. **Rzeczywiste twierdzenie Hahna–Banacha:** relacja przedłużania daje częściowy porządek, dla niepustego łańcucha działa zgodna unia dziedzin i funkcjonałów, a łańcuch pusty ma ograniczenie górne `(M,f)`. Lemat Kuratowskiego–Zorna i przedłużenie jednowymiarowe wymuszają maksymalną dziedzinę `E`.
4. **Rekonstrukcja zespolona:** wzór `G(x)=u(x)−iu(ix)` ma część rzeczywistą `u`; `G(ix)=iG(x)` wraz z liniowością nad `R` zapewnia liniowość nad `C`. Unikatowość z części rzeczywistej poprawna.
5. **Wersja zespolona z dominacją:** rzeczywiście liniowe przedłużenie `v` części rzeczywistej prowadzi do `F`; dla `F(x)≠0` wybór `α=\overline{F(x)}/|F(x)|` daje `|F(x)|=v(αx)≤p(αx)=p(x)`. Osobno przypadek `F(x)=0`.
6. **Ciągłość przez seminormę:** dla ciągłego `f` funkcja `|f|` jest ciągłą seminormą. Odwrotnie dominacja przez `p` ciągłą dowodzi ciągłości `f` z otoczeń zera.
7. **Topologiczny Hahn–Banach:** ciągłość `f|_M` dostarcza otwartego absolutnie wypukłego `U` w `X`, którego funkcjonał Minkowskiego dominuje `|f|` na `M`. Przedłużenie pozostaje ciągłe; nie jest konieczny Hausdorff ani domkniętość `M`.
8. **Jednoznaczność przedłużenia z gęstej podprzestrzeni:** domknięte jądro ciągłej różnicy funkcjonałów zawiera gęste `M`, a więc całe `X`.
9. **Zachowanie normy:** dla `p(x)=||f||·||x||` przedłużenie ma normę najwyżej `||f||`, a ograniczenie do `M` wymusza nierówność odwrotną. Działa także dla `f=0` i `M={0}`.
10. **Funkcjonał normujący wektor:** dla `x_0≠0` definicja na `Kx_0` daje normę 1 i wartość `||x_0||`; przedłużenie zachowuje normę. W tożsamości z supremum `x=0` traktowany osobno.
11. **Seminorma jako supremum funkcjonałów:** przy `p(x_0)>0` konstrukcja na `Kx_0` daje `f(x_0)=p(x_0)`; przy `p(x_0)=0` funkcjonał zerowy realizuje tezę. Dominacja przez `p` zapewnia ciągłość w przestrzeni lokalnie wypukłej.
12. **Rozdzielanie punktów:** przy lokalnej wypukłości i Hausdorffie rodzina ciągłych seminorm rozdziela niezerowe wektory, a twierdzenie z punktu 11 dostarcza żądanego funkcjonału.
13. **Oddzielanie punktu od domkniętej podprzestrzeni:** z `(x_0+W)∩M=∅` oraz `U=-U⊂W` wynika `x_0−m∉U`. Zatem `p_U(x_0−m)≥1`, co dominuje `g(m+λx_0)=λ`. Przedłużenie ma wartość 1 w `x_0` i jest ciągłe bez założenia Hausdorffa całego `X`.
14. **Charakteryzacja domknięcia przez jądra:** `cl M` należy do każdego jądra ciągłego funkcjonału zerującego się na `M`; punkt poza `cl M` zostaje oddzielony od tej domkniętej podprzestrzeni.
15. **Przestrzeń sprzężona produktu:** otoczenie ogranicza tylko skończone współrzędne `I_0`; skalowanie w pozostałych współrzędnych wymusza ich wyzerowanie przez funkcjonał. Zatem funkcjonał zależy od `I_0`. Zawiera także przypadek `I=∅`: jedyny funkcjonał jest zerowy.
16. **Przestrzeń sprzężona ilorazu:** `q^*` jest iniekcją przez surjektywność `q`, a funkcjonały zerujące się na `M` faktoryzują się przez `X/M`; ciągłość przez własność finalną topologii ilorazowej, niezależnie od domkniętości `M`.
17. **Odległość od domkniętej podprzestrzeni:** w przypadkach `x_0∈M` i `x_0∉M` osobno, konstrukcja na `M+Kx_0` jest dominowana przez normę; `d>0` dla domkniętej `M`, a definicja infimum daje `||g||=1` nawet gdy najbliższy punkt w `M` nie istnieje.

## Sprawdzenie pięciu przykładów — 5/5 PASS

1. Nieciągły funkcjonał algebraiczny na nieskończenie wymiarowej przestrzeni unormowanej, otrzymany przez przedłużenie znormalizowanych wektorów liniowo niezależnych z wartościami `n`; rola aksjomatu wyboru jest jawna.
2. Sumowanie na `c_{00}⊂ℓ¹`, gęstość obcięć oraz kontrprzykład z normą supremum na `c_{00}`.
3. Ciągłość funkcjonałów `f↦f^{(j)}(t_0)` na `C∞([0,1])` przez seminormy pochodnych.
4. Wiele przedłużeń `F_a(x,y)=ax+(1−a)y`, `a∈[0,1]`, zachowujących normę na `(R²,||·||∞)`.
5. Ciągły funkcjonał na jednowymiarowej `Kχ_[0,1]` bez ciągłego przedłużenia na `L^p([0,1])`, `0<p<1`, ponieważ `X'={0}`.

## Kontrole dodatkowe i regresje

- **Warunek Hausdorffa dla skończenie wymiarowej TVS:** kontrprzykład `R` z topologią trywialną wykazuje, że poprzednia teza bez Hausdorffa była fałszywa. Po korekcie 06/02 założenie jest jawne i właściwe.
- **Funkcja podliniowa podpisana:** przykład `p(x,y)=x+|y|` daje wartości ujemne i poprawny przedział przedłużenia `[-1,1]`; nie opierano ogólnej wersji rzeczywistej na założeniu nieujemności.
- **Separacja nie-Hausdorffa:** `R²` z seminormą `p(x,y)=|x|`, zamknięta prosta `M={0}×R` i punkt `x_0=(3,1)` mają separator `F(x,y)=x/3`.
- **Struktura:** **17** par środowisk `proof`, **5** par `przyklad`, **22** unikatowe etykiety, **19** wystąpień odsyłaczy; wszystkie ich cele istnieją w źródłach 01–06.
- **Terminologia:** brak niedozwolonego samodzielnego słowa „dual”, zapisów `\\mathbf1`, wyrazów „sekwencyjny” i „pierwszoprzeliczalna”. W przykładzie `L^p` użyto `\\chi_{[0,1]}`.
- Dotychczasowy pakiet **19 testów regresyjnych** obejmuje skończenie wymiarowe modele przedłużenia jednowymiarowego, fazę zespoloną, przypadki nie-Hausdorffa, anihilator ilorazu, wzór na odległość i niejednoznaczność. **Nie weryfikuje numerycznie lematu Kuratowskiego–Zorna** — jego zastosowanie sprawdzono wyłącznie w dowodzie matematycznym.
- Przed niniejszym raportem ukończono pełnym **SUCCESS** [CI 45178710978](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45178710978) z identycznym SHA źródła, 19/19 testami oraz pełną kontrolą kontekstu 01–06. Po zapisaniu niniejszego raportu uruchomiony dedykowany workflow powtórzy niezależnie kontrolę CI; ostateczny wynik zostanie dodany po zakończeniu.
- Wizualna inspekcja siedmiu stron rozdziału 06 (33–39) została przeprowadzona w audycie 06/03 i potwierdziła brak kolizji oraz elementów poza stroną. Źródło rozdziału od tej kontroli pozostało niezmienione.

## Decyzja

**Matematyka 17/17 PASS; przykłady 5/5 PASS. Audyt 06/04 jest drugim czystym audytem bez modyfikacji źródła.** Po potwierdzeniu technicznych kontroli z raportu rozdział 06 jest **STABILNY (2/2)**. Dopuszcza się rozpoczęcie audytu rozdziału 07 dopiero po tym potwierdzeniu.
