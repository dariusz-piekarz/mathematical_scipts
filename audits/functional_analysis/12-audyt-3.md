# Analiza funkcjonalna — rozdział 12 — audyt 03 (drugi niezależny czysty audyt stabilizacyjny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Rozdział:** chapters/pl/functional_analysis/12-klasyczne-przestrzenie-banacha-i-ich-duale.tex.  
**SHA blob źródła:** 923f7976d09f42030687a8873401cf34da4ff2fb, **ten sam** co w audycie 12/02.  
**SHA pliku testów:** a3d6007eb6ded526358b5a02fccd943bd8c2f4a5 (**18 testów**).  
**Werdykt merytoryczny:** **CZYSTY 2/2** po poprzedniej kontroli 12/02; źródło, testy i workflow pozostawiono bez zmian. Ostateczne formalne zamknięcie rozdziału 12 jest zależne od zielonego, rzeczywiście zakończonego workflow wywołanego niniejszym raportem.

## Kontrola stanu i oddzielenie iteracji

Przed rozpoczęciem sprawdzono katalog raportów na istniejącej gałęzi, w którym były 12-audyt-1.md (audyt z poprawkami, 0/2) i 12-audyt-2.md (pierwszy niezależny przegląd bez poprawek, 1/2), ale nie było audytu 12/03. Potwierdzono odrębnie blob źródła: identyczny w 12/02 i niniejszym audycie. Potwierdzono ukończone sukcesem przebiegi dedykowanego workflow: [#45248566903](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45248566903), [#45248672491](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45248672491) oraz [#45249198030](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45249198030); wszystkie miały COMPLETED/SUCCESS. Raport 12/01 dokumentuje rzeczywistą inspekcję wizualną PDF zawierającego rozdział 12 (72 strony, końcówka strony 66 i strony 67–72). Sukces samej kompilacji nie jest traktowany jako formalne poświadczenie dowodów matematycznych.

## Niezależna kontrola matematyczna wszystkich 10 dowodów

1. **Zupełność \(\mathcal L(E,F)\):** przy normowanej E i zupełnej F sekwencja operatorów Cauchy'ego w normie jest punktowo Cauchy'ego. Liniowa granica jest ograniczona przez szacunek \(\|(T_n-T)x\|\le\varepsilon\|x\|\), więc daje zbieżność w normie operatorowej. Nie zakłada się niepotrzebnie zupełności E.
2. **Nierówność Höldera dla ciągów:** Young dla wartości znormalizowanych i przejście od skończonych sum do monotonicznie rosnącego szeregu pozwala uzyskać normę iloczynu; \(p=1,q=\infty\) i zerowe normy obsłużono oddzielnie.
3. **Zupełność \(\ell^p,\ell^\infty,c_0\):** argument podciągu z sumowalnymi normami różnic i majorantem współrzędnych dowodzi zupełności \(\ell^p\) dla \(p<\infty\). Zbieżność jednostajna współrzędnych wystarcza dla \(\ell^\infty\). Domkniętość \(c_0\) i oszacowania obcięć są poprawne; \(c_{00}\) nie jest gęste w \(\ell^\infty\), co potwierdza stały ciąg jedynek.
4. **Przestrzenie sprzężone \(\ell^p\) i \(c_0\):** z wartości na \(e_n\) odzyskuje się jedyne możliwe współczynniki \(a_n\). Dla \(p>1\) normalizacja przez \(S_N^{-1/p}\) i tożsamość \((q-1)p=q\) dają jednostkowy wektor testowy z \(F(x)=S_N^{1/q}\); dla \(p=1\) działa supremum współczynników, a dla \(c_0\) wektory fazowe na skończonym nośniku. Dla zera określono oddzielną wartość, więc nie powstaje potęga zera o ujemnym wykładniku.
5. **Hölder, Minkowski i zupełność \(L^p\):** źródło jawnie uzasadnia \(f+g\in L^p\) nierównością \(|f+g|^p\le2^{p-1}(|f|^p+|g|^p)\), zanim zastosuje Höldera do \(|f+g|^{p-1}\). Dla Cauchy'ego w \(L^p\) podciąg o sumowalnych normach różnic oraz monotoniczna zbieżność sum modułów prowadzą do granicy w \(L^p\); dla \(L^\infty\) można usunąć przeliczalną sumę zbiorów \(\mu\)-zerowych.
6. **Gęstość funkcji prostych:** aproksymacja rosnąca funkcji dodatnich i zbieżność zmajoryzowana dają zbieżność w \(L^p\); rozkład na części rzeczywiste i urojone oraz dodatnie i ujemne pozwala objąć funkcje ogólne.
7. **Reprezentacja \((L^p)'\), \(1\le p<\infty\):** dla skończonej miary \(\nu(A)=F(\chi_A)\) jest przeliczalnie addytywna, absolutnie ciągła względem \(\mu\) i ma skończoną wariację; wybór \(\theta_j\) o module 1 daje sumę wariacji nie większą niż \(\|F\|\mu(\Omega)^{1/p}\). Radon–Nikodym daje \(g\in L^1\), test fazowy dowodzi \(g\in L^\infty\) przy \(p=1\), a obcięcia \(g_N\) i testy \(\overline{g_N}|g_N|^{q-2}\) dają \(g\in L^q\) dla \(p>1\). Gęstość funkcji prostych i Hölder zapewniają reprezentację, normę i jednoznaczność. Poprawnie uwzględniono przypadek \(\mu(\Omega)=0\).
8. **Zupełność \(C(K)\):** ciąg Cauchy'ego w normie supremum daje jednostajną granicę funkcji ciągłych. Zwartość K pozwala traktować normę maksimum i zachować ciągłość granicy.
9. **Reprezentacja dodatniego funkcjonału:** ponownie, bardziej szczegółowo niż w audycie 12/02, sprawdzono poniżej konstrukcję funkcji \(m\), miary zewnętrznej \(\mu^*\), regularności oraz funkcji \(h_j\). Te elementy nie wprowadzają fałszywego założenia σ-skończoności ani nie wymagają aproksymacji w innych topologiach.
10. **Twierdzenie Riesza–Markowa:** część dodatnia funkcjonału jest addytywna na dodatnim stożku dzięki rozkładowi \(h=\min(h,f_1)+(h-\min(h,f_1))\), a rozszerzenie liniowe daje różnicę dodatnich funkcjonałów. W przypadku zespolonym reprezentuje się rzeczywiste części ograniczenia do rzeczywistych funkcji ciągłych. W oszacowaniu normy wariacją stosuje się aproksymację fazy \(\overline u\) w \(L^1(|\nu|)\) funkcjami ciągłymi o module co najwyżej 1; taką aproksymację zapewnia gęstość funkcji ciągłych i ciągłe rzutowanie na zamknięty dysk jednostkowy.

**Werdykt dowodów:** 10/10 przejrzanych ponownie przy jawnych hipotezach, bez znalezionej nowej luki wymagającej korekty.

## Uzupełniająca kontrola kroku miarowego i funkcji \(h_j\)

Dla otwartego U definicja \(m(U)=\sup\{T(f):0\le f\le1,\operatorname{supp}f\subset U\}\) ma wartość skończoną (nie większą niż \(T(\chi_K)\)). Jeśli nośnik testowego f leży w sumie otwartych U_j, zwartość nośnika pozwala wybrać skończone podpokrycie. Przez partycję jedności na tym nośniku rozkłada się f na funkcje \(f\psi_j\) o nośnikach zawartych w U_j, stąd przeliczalna podaddytywność m. Dla rozłącznych U,V testy odpowiednio z nośnikami w U i V dodają się bez przekroczenia 1; wraz z poprzednią nierównością daje to \(m(U\cup V)=m(U)+m(V)\).

Dla dowolnych A,B o dodatniej odległości i dowolnego otwartego W zawierającego \(A\cup B\) można wybrać rozłączne otwarte \(W_A,W_B\subset W\), obejmujące odpowiednio A i B (przez otoczenia odległości mniejszej od połowy dystansu). Następnie \(m(W)\ge m(W_A)+m(W_B)\ge\mu^*(A)+\mu^*(B)\); po wzięciu infimum otrzymuje się metryczną addytywność miary zewnętrznej. Monotoniczność m daje \(\mu^*(U)=m(U)\) dla każdego otwartego U, skąd \(\mu^*(K)=m(K)=T(\chi_K)\).

Dla \(\delta>0\) i \(f\ge0\), \(h_j=\min\{1,\max\{0,(f-j\delta)/\delta\}\}\) spełnia \(0\le h_j\le1\) oraz \(f=\delta\sum_{j=0}^{N-1}h_j\), jeśli \(N\delta\ge\|f\|_\infty\). Jeśli \(0\le\varphi\le1\) i \(\operatorname{supp}\varphi\subset\{f>(j+1)\delta\}\), to \(\varphi\le h_j\), co daje dolne oszacowanie \(m(\{f>(j+1)\delta\})\le T(h_j)\). Z drugiej strony, pomnożenie \(h_j\) przez ciągłe funkcje obcięcia zerujące się przy \(f\le j\delta+\varepsilon\) daje funkcje o nośnikach w \(\{f>j\delta\}\) zbiegające jednostajnie do \(h_j\); dodatniość i ciągłość T dają \(T(h_j)\le m(\{f>j\delta\})\). Różnica sum górnej i dolnej jest nie większa niż \(\delta\,\mu_T(K)\), więc po przejściu z \(\delta\to0\) i użyciu warstwowego wzoru całkowania uzyskuje się reprezentację. Użyte twierdzenia o metrycznej mierze zewnętrznej, regularności i warstwowym całkowaniu są standardowymi, wyraźnie przywołanymi wynikami; testy kodowe nie dowodzą ich prawdziwości.

## Kontrola dwóch przykładów oraz uwag o przestrzeniach sprzężonych

1. Funkcjonał granicy na przestrzeni ciągów zbieżnych ma normę 1; przedłużenie Hahna–Banacha znika na wszystkich \(e_n\), lecz przyjmuje wartość 1 na stałym ciągu \(u=(1,1,\ldots)\). Nie można go reprezentować przez żaden element \(\ell^1\), co pokazuje, że \((\ell^\infty)'\) jest większa od \(\ell^1\).
2. Miara Diraca \(\delta_{x_0}\) na niepustej zwartej przestrzeni metrycznej K jest regularna, jej wariacja wynosi 1, a funkcjonał ewaluacji \(f\mapsto f(x_0)\) ma normę 1. Różne punkty rozdziela funkcja ciągła, więc przykłady są rozróżnialne.

Sprawdzono też uwagę o \((L^\infty)'\) z operatorem uśredniania na parami rozłącznych zbiorach dodatniej miary: funkcjonał \(\Phi\) znika na \(\chi_{A_n}\), ale przyjmuje 1 na \(\chi_{\bigcup A_n}\), co wyklucza reprezentację przez \(L^1\).

## Niezależna kontrola struktury źródeł 01–12

Z bieżącej gałęzi ponownie pobrano rzeczywiste źródła wszystkich dwunastu rozdziałów. W tych plikach jest **221 etykiet i 0 duplikatów**. Sam rozdział 12 zawiera **19 etykiet** i **5 odsyłaczy, wszystkie rozwiązane**. Parowanie środowisk: 10 proof, 5 twierdzenie, 2 stwierdzenie, 3 lemat, 4 definicja, 2 przyklad, 2 uwaga; brak rysunków TikZ w rozdziale 12. Nie znaleziono niedopuszczonych określeń „sekwencyjny”, „wskaźnik”, „przestrzeń dualna” ani zakazanych zapisów funkcji charakterystycznej. Wszystkie akapity mają parzystą liczbę nieescapowanych znaków dolara, więc w szczególności nie odtworzono wcześniej naprawionego błędu \(\$\).

Źródło rozdziału 12 po audycie 12/01 i po audycie 12/02 ma niezmieniony blob SHA 923f7976d09f42030687a8873401cf34da4ff2fb. Wcześniejsze przebiegi dedykowanego workflow na identycznym źródle i zestawie testów zakończyły się sukcesem. Poprzedni audyt 12/01 opisuje inspekcję rzeczywistego 72-stronicowego PDF; nie przypisuje się niniejszej iteracji nowej wizualizacji.

## Decyzja stabilizacyjna

**Matematycznie i redakcyjnie: CZYSTY 12/03 — 2/2 kolejnych czystych audytów na identycznym źródle.** W tej iteracji nie poprawiano pliku źródłowego, testów ani workflow. **Ostateczne zamknięcie rozdziału 12 i zezwolenie na audyt rozdziału 13 wymagają bezpośredniego sprawdzenia zielonego CI uruchomionego zapisaniem tego raportu.** Kompilacja i testy regresyjne są kontrolami technicznymi, a nie zastępują kontroli merytorycznej.
