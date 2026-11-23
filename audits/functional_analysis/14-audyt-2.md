# Analiza funkcjonalna — rozdział 14 — audyt 02 (pierwszy niezależny czysty przegląd)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Źródło:** chapters/pl/functional_analysis/14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex.  
**Blob SHA źródła:** 8ea2ec43a6dca36e644000517fa19d589bd134fe, identyczny z końcową wersją z audytu 14/01.  
**Blob SHA testów:** ad9ce5ad851b9f09a1323bb009ef1604a78150b7.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY, 1/2**. W niniejszej iteracji nie zmieniano ani źródła, ani testów. Rozdział 15 nadal zablokowany.

## Stan zastany i weryfikacja CI

Przed audytem odczytano istniejący katalog audytów na gałęzi: rozdział 13 został zamknięty jako stabilny (2/2), a rozdział 14 miał wyłącznie raport 14/01 — pierwszy audyt **z poprawkami**, który nie liczy się jako czysta kontrola. Nie znaleziono raportu 14/02 ani 14/03; nie powielano pracy automatyzacji.

Rzeczywiste przebiegi dedykowanego workflow:
- [#45273100710](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45273100710) — COMPLETED/SUCCESS po wdrożeniu workflow;
- [#45273331679](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45273331679) — COMPLETED/SUCCESS po utworzeniu audytu 14/01;
- [#45273885595](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45273885595) — COMPLETED/SUCCESS po domknięciu raportu 14/01.

Dla ostatniego przebiegu osobno zweryfikowano wszystkie kroki: **21/21 testów PASS**, przygotowanie faktycznego kontekstu źródłowego 01–14 PASS, kompilacja LaTeX PASS, weryfikacja PDF oraz odsyłaczy PASS i publikacja artefaktu PASS. W raporcie 14/01 jest udokumentowane pobranie 84-stronicowego PDF, inspekcja stron 78–84 i powiększonej strony 80 z rysunkiem krzywej. W niniejszym audycie nie twierdzi się, że przeprowadzono kolejny niezależny rendering PDF.

## Niezależny przegląd wszystkich 12 dowodów

1. **Fréchet ⇒ Gâteaux oraz ciągłość.** Rozkład \(f(x+h)=f(x)+Ah+r(h)\), gdzie \(r(h)=o(\|h\|)\) i A jest ograniczony, daje ciągłość. Dla każdego ustalonego h reszta \(r(th)/t\to0\) w F. Pochodne w każdym kierunku jednoznacznie wyznaczają A; przypadek h=0 nie stwarza wyjątku.
2. **Kryterium jednostajnego przybliżenia kierunkowego.** Przy \(t\ne0\) tożsamość \(\sup_{\|h\|=1}\|r(th)\|/|t|=\sup_{\|k\|=|t|}\|r(k)\|/\|k\|\) jest prawdziwa. Zbieżność normowo małej reszty Frécheta jest równoważna jednostajnej kontroli po sferze; odwrotnie podstawienie \(k=t h\) przy \(t=\|k\|\) i h jednostkowym dowodzi właściwego warunku. Otwartość U gwarantuje istnienie wspólnego promienia; źródło słusznie wyłącza E={0} w tym wariancie kryterium.
3. **Niepoprawność reguły łańcuchowej przy samej pochodnej Gâteaux.** Funkcja \(f(x,y)=x^3y/(x^4+y^2)\), f(0)=0, ma \(D_Gf(0)=0\), ale dla \(\gamma(t)=(t,t^2)\) funkcja złożona równa jest \(t/2\), a więc pochodna w t=0 wynosi 1/2. Wskazano gładką krzywą i zweryfikowano fakt, że pochodna f w zerze nie jest pochodną Frécheta.
4. **Norma w \(\ell^1\).** Dla każdego x o niezerowych współrzędnych i ustalonego h nierówność \(\bigl||x_n+t h_n|-|x_n|\bigr|/|t|\le|h_n|\) daje dominację sumy i formułę \(D_GN(x)h=\sum\operatorname{sgn}(x_n)h_n\). Otrzymany funkcjonał jest liniowy i ograniczony. Przyrost \(h^{(n)}=-2x_ne_n\) ma normę dążącą do zera, ale iloraz reszty względem wskazanego D_G jest równy 1; dlatego nie ma Frécheta.
5. **Reguła sumy i składania z operatorem.** Ograniczoność operatora gwarantuje przenoszenie \(o(\|h\|)\) przez T. Tożsamość dla kombinacji liniowej i funkcji afinicznej jest poprawna bez założenia ciągłości pochodnych w otoczeniu.
6. **Reguła łańcuchowa Frécheta.** Przy \(k=Ah+r(h)\) mamy \(k=O(\|h\|)\); zatem \(s(k)=o(\|k\|)=o(\|h\|)\), przy czym źródło osobno uwzględnia przypadek k=0. Równość \(D(g\circ f)(x)=Dg(f(x))Df(x)\) jest poprawna z właściwymi dziedzinami.
7. **Reguła dla odwzorowania dwuliniowego.** Równość \(B(u+h,v+k)-B(u,v)-B(h,v)-B(u,k)=B(h,k)\) daje resztę kwadratową. Składanie z odwzorowaniem \(z\mapsto(f(z),g(z))\) daje regułę iloczynu. Po poprawce 14/01 teza jawnie kwantyfikuje wszystkie przestrzenie **E,E1,E2,G**, w tym dziedzinę funkcji f i g.
8. **Podstawowe twierdzenie rachunku całkowego dla krzywej Banacha.** Ciągłość \(\gamma'\) na [a,b] implikuje jednostajną ciągłość, istnienie całki Riemanna z wartościami w zupełnym F i normowe oszacowanie różnicy. Dla każdej \(\ell\in F'\) o normie co najwyżej 1 stosuje się skalarne twierdzenie o wartości średniej do \(t\mapsto\ell(\gamma(t)-t\gamma'(\xi_j))\); potem twierdzenie Hahna–Banacha daje z supremum po \(\ell\) poprawne oszacowanie normy wektorowego przyrostu. Przy dzieleniu przedziału na dostatecznie krótkie części wszystkie błędy sumują się do \(\varepsilon(b-a)\).
9. **Wzór całkowy i oszacowanie przyrostu.** Parametryzacja odcinka \(x+t(y-x)\) należy do U, a reguła łańcuchowa i ciągłość Df pozwalają użyć poprzedniego lematu. Z nierówności normy całki wynika szacowanie Lipschitza po odcinku.
10. **Ciągła pochodna Gâteaux ⇒ \(C^1\).** Dla małego h funkcja \(t\mapsto f(x+th)\) ma pochodną \(D_Gf(x+th)h\), ciągłą w t. Istnienie pochodnej kierunkowej w punktach końcowych daje wymaganą ciągłość wzdłuż prostej. Wzór całkowy i norma operatorowa dają resztę kontrolowaną przez \(\sup_{0\le t\le1}\|D_Gf(x+th)-D_Gf(x)\|\to0\), więc zachodzi Fréchet.
11. **Pochodna kwadratu normy i normy Hilberta.** Tożsamość rozwinięcia iloczynu skalarnego prowadzi do \(D_{\R}(\|x\|^2/2)h=\operatorname{Re}\langle h,x\rangle\) z dokładną resztą \(\|h\|^2/2\). Dla x różnego od zera działa łańcuchowa z pierwiastkiem liczbowym; dla x=0 i niezerowego kierunku granica \(|t|\|h\|/t\) nie istnieje.
12. **Kryterium zespolonej pochodnej Frécheta.** Ta sama reszta jest mała niezależnie od tego, czy E,F traktujemy jako przestrzenie rzeczywiste czy zespolone. Rzeczywisto-liniowy operator A jest zespolenie liniowy wtedy i tylko wtedy, gdy \(A(ih)=iAh\) dla każdego h. Warunek jest zarówno konieczny, jak i wystarczający.

**Wynik: 12/12 dowodów bez nowej poprawki.** Nie interpretować wykonanych testów regresyjnych jako formalnego poświadczenia tych dowodów.

## Ponowna kontrola wszystkich 8 przykładów

1. \(g(x,y)=x^3y/(x^6+y^2)\) dla (x,y)≠0: iloraz kierunkowy dąży do zera dla każdego ustalonego kierunku, lecz \(g(x,x^3)=1/2\), więc brak ciągłości w zerze.
2. \(f(x,y)=x^3y/(x^4+y^2)\): z \(2|x^2y|\le x^4+y^2\) wynika \(|f|\le|x|/2\) i ciągłość w zerze, podczas gdy iloraz błędu po krzywej \(y=x^2\) dąży do 1/2; pochodna Gâteaux jest zerowa, Frécheta nie istnieje.
3. \(q(x,y)=x^3/(x^2+y^2)\): dwustronna pochodna kierunkowa w (a,b) wynosi \(a^3/(a^2+b^2)\), dla (a,b)≠0. Nie jest addytywna, co odróżnia ją od pochodnej Gâteaux według wybranej definicji.
4. Dla \(Q(x)=B(x,x)\) pełna pochodna wynosi \(DQ(x)h=B(h,x)+B(x,h)\). Dla \(\|x\|^2/2\) gradient w rzeczywistym Hilbercie wynosi x, a reszta jest kwadratowa.
5. \(f(x)=x^2\sin(1/x^2)\) z f(0)=0 ma pochodną w zerze równą zero, lecz \(f'(x)=2x\sin(1/x^2)-2x^{-1}\cos(1/x^2)\) nie jest ciągła w 0.
6. Energia kwadratowa z samosprzężonym A: gradient jest Ax-b przy rzeczywistej strukturze przestrzeni Hilberta. Silna dodatniość operatora zapewnia istnienie i jednoznaczność minimizatora przez Laxa–Milgrama.
7. Funkcjonał całkowy w \(L^2\): rozwinięcie kwadratu daje \(DJ(u)h=\int(u-g)h\,\mathrm d\mu\), gradient u-g i resztę normową \(\|h\|_2^2/2\).
8. Sprzężenie zespolone jest rzeczywiście liniowe w pochodnej, lecz narusza \(A(ih)=iAh\). Dla \(z\mapsto|z|^2\) pochodna rzeczywista w z≠0 jest niezerowym funkcjonałem o wartościach rzeczywistych, więc nie może być zespolenie liniowa. W zerze zespolona pochodna Frécheta istnieje i jest zerem.

**Wynik: 8/8 przykładów bez nowej usterki.** Diagram TikZ \(y=x^2\) jest zgodny z kontrprzykładem i ma udokumentowaną wizualną kontrolę strony 80 w raporcie 14/01, dla identycznego bloba źródła.

## Niezależna kontrola struktury i terminologii

Z bieżącej gałęzi ponownie pobrano wszystkie źródła rozdziałów **01–14** i dokonano własnego odczytu: **280 etykiet, 0 duplikatów**; w rozdziale 14 **29 etykiet, 4 odsyłacze, wszystkie rozwiązane**. Pary środowisk: proof 12/12, twierdzenie 7/7, stwierdzenie 4/4, lemat 1/1, definicja 6/6, przyklad 8/8, uwaga 4/4 i tikzpicture 1/1. Znaczniki matematyczne w akapitach są sparowane; nie znaleziono zakazanej terminologii (np. sekwencja, niepoprawna iniektywność, samodzielne angielskie dual) ani starych oznaczeń funkcji charakterystycznej. Skontrolowano obecność poprawionego założenia o E i wykresu kontrprzykładu w źródle.

## Decyzja

**14/02: CZYSTY — pierwszy niezależny czysty audyt stabilizacyjny (1/2).** Nie zmieniono rozdziału, testów ani workflow. Pozostaje kolejny niezależny audyt **14/03**, na tym samym blob SHA **8ea2ec43a6dca36e644000517fa19d589bd134fe**, oraz potwierdzenie zielonego CI po zapisaniu raportu. **Rozdział 15 zablokowany.**
