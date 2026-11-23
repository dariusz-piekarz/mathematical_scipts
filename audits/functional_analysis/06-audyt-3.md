# Analiza funkcjonalna — rozdział 06 — audyt 03 (pierwsza kontrola stabilizacyjna)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/06-twierdzenie-hahna-banacha-i-ciagly-dual.tex.  
**SHA źródła:** c8caeb6a6c102e6bfa4ad4560c6a0f3d6c682000, identyczny z końcowym stanem audytu 06/02.  
**Wynik matematyczny, redakcyjny i techniczny:** **CZYSTY — 1/2 kolejnych czystych audytów** po ostatniej korekcie. Brak zmian źródła. Pełny CI i PDF zweryfikowane; rozdział 06 nie jest jeszcze stabilny.

## Niezależność i zakres

Na nowo przejrzano pełne twierdzenia i wszystkie 17 dowodów, pięć przykładów i przypadki brzegowe. Audyt uwzględnia nie-Hausdorffa w skończonym wymiarze, skalowanie i nierówność dominacji dla funkcji podliniowej przyjmującej wartości ujemne, fazę zespoloną, lemat Kuratowskiego–Zorna, przejście od algebraicznego do ciągłego przedłużenia, anihilatory oraz separację. Matematyczny przegląd nie opiera się na wyniku testu numerycznego. **Nie zmieniono pliku LaTeX.**

## Sprawdzenie dowodów — 17/17 PASS

1. **Kryterium ciągłości funkcjonału liniowego:** ograniczenie na otoczeniu i skalowanie otoczenia są równoważne ciągłości w zerze; liniowość daje ciągłość wszędzie.
2. **Lemat przedłużenia o jeden wymiar:** przedział [L,R] jest niepusty i ma skończone krańce; dla t>0 dostajemy ograniczenie od góry a, a dla t<0 — od dołu, bez założenia nieujemności ani symetrii p. Przypadek t=0 pozostaje na M.
3. **Hahn–Banach rzeczywisty:** relacja przedłużania daje częściowy porządek, łańcuchy mają ograniczenie górne przez zgodną unię (również łańcuch pusty z ograniczeniem (M,f)), a Zorn zapewnia maksymalny element. Lemat jednowymiarowy wyklucza właściwe N⊊E.
4. **Rekonstrukcja zespolona:** G(x)=u(x)−iu(ix), G(ix)=iG(x), liniowość rzeczywista i jednoznaczność z części rzeczywistej.
5. **HB zespolony i dominacja przez seminormę:** rzeczywiste przedłużenie u=Re f, odtworzenie G i wybór α=conj(F(x))/|F(x)| przy F(x)≠0 dają |F(x)|≤p(x). Dla F(x)=0 wynik natychmiastowy.
6. **Ciągłość a seminorma:** p=|f| jest ciągłą seminormą dla f∈X'; ograniczenie przez p ciągłą zapewnia ciągłość w odwrotną stronę.
7. **HB w lokalnie wypukłych TVS:** z ciągłości f na M wybiera się absolutnie wypukłe otwarte U w X, na którym |f|<1 na przecięciu M∩U. Minkowski p_U jest ciągłą seminormą dominującą |f| i przez HB umożliwia przedłużenie bez Hausdorffa/zupełności.
8. **Jednoznaczność na gęstej M:** jądro F₁−F₂ jest domknięte i zawiera M, więc jest całym X.
9. **HB z normą:** p=||f||·||x||, jednorodność, ograniczenie normy przedłużenia i odwrotna nierówność na M. Działa także dla f=0 i M={0}.
10. **Funkcjonał normujący:** f₀(λx₀)=λ||x₀|| ma normę 1 na Kx₀, HB zachowuje normę; osobno x=0 w formule supremum.
11. **Seminorma jako supremum:** przy p(x₀)=0 funkcjonał zerowy, a przy p(x₀)>0 normujące przedłużenie z Kx₀. Dominacja przez p daje ciągłość i osiągnięcie supremum.
12. **Ciągłe funkcjonały rozdzielają punkty:** lokalna wypukłość i Hausdorff dostarczają p(x−y)>0, następnie HB funkcjonał spełniający f(x−y)=p(x−y).
13. **Separacja punktu od domkniętej podprzestrzeni:** z (x₀+W)∩M=∅, −U=U i U⊂W poprawnie wynika x₀−m∉U. Dla g(m+λx₀)=λ zachodzi |g|≤p_U, a przedłużenie jest ciągłe. Brak potrzeby Hausdorffa X.
14. **Domknięcie podprzestrzeni przez anihilator:** każde jądro zawiera cl(M); punkt poza cl(M) jest oddzielany od domkniętej podprzestrzeni przez funkcjonał.
15. **Przestrzeń sprzężona produktu K^I:** podstawowe otoczenie ogranicza jedynie skończenie wiele współrzędnych; funkcjonał zeruje się na wektorach o zerach w tych współrzędnych, więc ma skończony nośnik.
16. **Przestrzeń sprzężona ilorazu:** f∈M⊥ faktoryzuje się przez q:X→X/M; definicja topologii ilorazowej zachowuje ciągłość. Rzut jest surjektywny, więc q* jest iniekcją.
17. **Odległość do podprzestrzeni:** funkcjonał normujący coset x₀+M skonstruowany na M+Kx₀ i przedłużony przez HB osiąga d=dist(x₀,M). Przy M domkniętej i x₀∉M mamy d>0, a ||g||=1 z przybliżania infimum. Dla x₀∈M obie strony 0.

Wszystkie powyższe dowody oceniono **PASS**.

## Pięć środowisk przykładów — 5/5 PASS

1. **Przestrzeń algebraicznie sprzężona większa niż sprzężona:** konstrukcja Hamelowska z f(eₙ)=n na unormowanej niezależnej rodzinie jest nieciągła.
2. **Sumowanie na c₀₀ i ℓ¹:** ciągłe w normie ℓ¹, jednoznaczne przedłużenie z gęstej M; nieciągłe na c₀₀ z normą supremum.
3. **Ewaluacja pochodnych na C∞([0,1]):** |f^(j)(t₀)|≤p_j(f) zapewnia ciągłość.
4. **Nieunikatowe przedłużenie na (R²,||·||∞):** F_a(x,y)=ax+(1−a)y dla a∈[0,1] zachowuje normę i ograniczenie do przekątnej.
5. **L^p([0,1]), 0<p<1:** funkcjonał f(cχ_[0,1])=c jest ciągły na jednowymiarowej M, natomiast nie ma niezerowych ciągłych funkcjonałów na X.

## Niezależne próby obalenia i kontrprzykłady

- **Skończony wymiar bez Hausdorffa:** R z trywialną topologią ma nieciągłe odwzorowanie x↦x do R ze zwykłą topologią. Nowe ograniczenie tezy do skończenie wymiarowych TVS Hausdorffa zachowano.
- **Nie-Hausdorff w twierdzeniu separacji:** R² z topologią generowaną przez p(x,y)=|x|; zamknięta M={0}×R, x₀=(3,1), funkcjonał f(x,y)=x/3 jest ciągły, zeruje się na M i spełnia f(x₀)=1. Model jest zgodny z twierdzeniem bez założenia Hausdorffa.
- **Podliniowość z wartościami ujemnymi:** p(x,y)=x+|y| ma p(-2,0)=-2<0. Dla M=R×{0}, f(x,0)=x, wektor x₀=(0,1), przedział dopuszczalnych wartości jednowymiarowego przedłużenia jest dokładnie [-1,1]; wszystkie wartości wewnątrz zachowują dominację.
- **Faza zespolona:** numerycznie sprawdzono rotację α taką, że Re(αF(x))=|F(x)| przy |α|=1, i jednorodność seminormy.
- **Źródło niezmienione**, lecz rozszerzono regresje 17→**19** testów w tools/tests/test_functional_analysis_ch06.py, dodając dwa modele powyżej.

## Poprawność struktury i kontrola techniczna

- Zachowano **17 środowisk dowodów, 5 środowisk przykładów, 22 unikatowe etykiety, 19 wystąpień odsyłaczy**; **0** brakujących celów odsyłaczy w rzeczywistym kontekście rozdziałów 01–06.
- Nie występują niepoprawne formy „ciągły dual”, „Dual ilorazu”, „sekwencyj”, „pierwszoprzeliczalna” ani niedozwolony zapis funkcji charakterystycznej. Wszystkie poprawki z 06/01 i 06/02 pozostają w tekście.
- **[CI 45178170981](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45178170981) — pełny SUCCESS**: 19/19 testów PASS, przygotowanie kontekstu 01–06, kompilacja LaTeX, końcowa weryfikacja PDF i odsyłaczy oraz zapis artefaktu PASS. W pierwszym przebiegu LaTeX pojawiło się przejściowe ostrzeżenie o odsyłaczach, którego nie ma w logu końcowym.
- Pobrano artefakt tego przebiegu: **PDF A4, 39 stron, 523156 bajtów**. Rozdział 06 zaczyna się na stronie 33 i kończy na 39. Strony **33–39 wyrenderowano i obejrzano**, bez kolizji tekstu i równań, obcięć lub uszkodzeń znaków. Automatyczna kontrola granic bloków tekstowych: **0 bloków poza stroną**. Końcowy log LaTeX: **0** `Undefined control sequence`, `There were undefined references`, `Overfull \\hbox`, `Missing character`.
- Poprzednie [CI 45177664269](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45177664269): pełny SUCCESS (17 testów, LaTeX i odsyłacze) dla tego samego niezmienionego tekstu rozdziału.

## Decyzja

**CZYSTY audyt matematyczny, redakcyjny i techniczny 06/03, z pełnym CI PASS. Zalicza się jako 1/2 kolejnych czystych audytów.** Rozdział 06 pozostaje w stabilizacji; w następnej iteracji przeprowadzić audyt 06/04, nie rozpoczynać rozdziału 07.
