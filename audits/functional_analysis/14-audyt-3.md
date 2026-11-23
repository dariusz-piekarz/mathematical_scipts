# Analiza funkcjonalna — rozdział 14 — audyt 03 (druga niezależna czysta kontrola)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez tworzenia nowej).  
**Źródło:** chapters/pl/functional_analysis/14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex.  
**SHA bloba źródła:** 8ea2ec43a6dca36e644000517fa19d589bd134fe — identyczny jak w czystym audycie 14/02.  
**SHA bloba testu:** ad9ce5ad851b9f09a1323bb009ef1604a78150b7 (21 testów).  
**Werdykt matematyczno-redakcyjny:** **CZYSTY — 2/2** na niezmienionym źródle. Ostateczna decyzja STABILNY wymaga zakończonego CI wywołanego niniejszym raportem.

## Odczyt stanu projektu przed audytem

Przed rozpoczęciem odczytano katalog raportów na istniejącej gałęzi, potwierdzając, że istnieją wyłącznie raporty 14/01 (audyt z poprawkami, 0/2) i 14/02 (pierwszy czysty, 1/2); brak 14/03 i 15/01. Ponownie odczytano źródło i test rozdziału 14; oba zachowały SHA podane wyżej. Sprawdzono przez GitHub API rzeczywisty wynik [GitHub Actions #45275533277](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45275533277) na commicie 67f2965df90459fee8f5a7391ee49998946fa565: **COMPLETED/SUCCESS**. Bezpośrednio odczytano kroki: 21 testów PASS, przygotowanie rozdziałów 01–14 PASS, kompilacja LaTeX PASS, kontrola PDF i odsyłaczy PASS, publikacja artefaktu PASS. Ten zakończony przebieg potwierdza zgodność poprawionej wersji źródła/testów z bramką techniczną po 14/02.

## Drugi niezależny przegląd wszystkich 12 dowodów

1. **Fréchet implikuje Gâteaux i ciągłość.** Dla rozkładu \(f(x+h)-f(x)=Ah+r(h)\) i \(\|r(h)\|=o(\|h\|)\) ograniczoność A daje ciągłość f. Dla każdego ustalonego h iloraz \(r(th)/t\) dąży do zera, z osobnym przypadkiem h=0. Identyczność \(Ah=Bh\) dla wszystkich h dowodzi jednoznaczności pochodnej Frécheta.
2. **Jednostajność po kierunkach.** Dla E≠{0} i x we wnętrzu U istnieje wspólny promień dopuszczający wszystkie przyrosty \(th\) przy \(\|h\|=1\). Zmiana zmiennej \(k=th\) identyfikuje supremum błędu na sferze z ilorazem błędu Frécheta; implikacja odwrotna działa przy \(t=\|k\|\) i \(h=k/\|k\|\). Nie myli się granic zbieżności punktowej i jednostajnej.
3. **Kontrprzykład do reguły łańcuchowej dla Gâteaux.** Funkcja \(f(x,y)=x^3y/(x^4+y^2)\), f(0,0)=0, ma \(D_Gf(0)=0\), lecz dla gładkiej krzywej \(\gamma(t)=(t,t^2)\) mamy \(f(\gamma(t))=t/2\) także w t=0. Zatem \((f\circ\gamma)'(0)=1/2\ne0\). Kontrprzykład wykorzystuje zmieniające się kierunki i nie narusza reguły Frécheta.
4. **Gâteaux normy \(\ell^1\) bez Frécheta.** W przestrzeni rzeczywistej \(\ell^1\), jeśli każde \(x_n\ne0\), dominacja \(\left|(|x_n+th_n|-|x_n|)/t\right|\le|h_n|\) pozwala na przejście do granicy w szeregu i daje ograniczony funkcjonał \(\sum \mathrm{sgn}(x_n)h_n\). Przyrost \(h^{(n)}=-2x_ne_n\) ma normę malejącą do zera, a znormalizowana reszta równa jest dokładnie 1, więc nie ma pochodnej Frécheta. Warunek \(x_n\to0\) wynika z sumowalności.
5. **Sumy, operator liniowy, funkcja afiniczna.** Suma błędów typu \(o(\|h\|)\) pozostaje taka sama; ograniczony T spełnia \(\|Tr(h)\|\le\|T\|\|r(h)\|\). Dla funkcji afinicznej reszta wynosi zero. Nie założono niepotrzebnie \(C^1\).
6. **Reguła łańcuchowa.** Z \(f(x+h)-f(x)=Ah+r(h)\) mamy \(k=Ah+r(h)=O(\|h\|)\). Jeśli \(k\ne0\), to \(\|s(k)\|/\|h\|=(\|s(k)\|/\|k\|)(\|k\|/\|h\|)\to0\); przy \(k=0\) błąd jest zerowy. Otrzymany operator \(Dg(f(x))\circ Df(x)\) ma poprawne typy i jest ograniczony.
7. **Różniczkowanie odwzorowania dwuliniowego.** Dokładna reszta \(B(h,k)\) jest \(O(\max\{\|h\|,\|k\|\}^2)\), zaś liniowy przyrost ma postać \(B(h,v)+B(u,k)\). W regule dla \(B(f,g)\) argument z odwzorowaniem do przestrzeni produktowej jest poprawny. Zweryfikowano, że poprawka 14/01 wprowadziła brakującą przestrzeń **E** do jawnie podanych hipotez \((E,E_1,E_2,G)\).
8. **Podstawowe twierdzenie rachunku dla krzywej Banacha.** Jednostajna ciągłość \(\gamma'\) na [a,b], ograniczoność sum Riemanna i zupełność F zapewniają istnienie całki. Dla każdego rzeczywistego \(\ell\in F'\) o normie co najwyżej 1 skalarne twierdzenie o wartości średniej dla \(t\mapsto\ell(\gamma(t)-t\gamma'(\xi))\) daje oszacowanie błędu przyrostu przez \(\Delta t\sup_{t\in I}\|\gamma'(t)-\gamma'(\xi)\|\). Przez Hahn–Banacha supremum po \(\ell\) odtwarza normę błędu wektorowego. Suma błędów dąży do zera z siatką podziału, co daje wzór Newtona–Leibniza bez używania nieistniejącego ogólnego wektorowego twierdzenia o wartości średniej.
9. **Wzór całkowy i oszacowanie przyrostu.** Gdy odcinek [x,y] leży w U, krzywa \(t\mapsto f(x+t(y-x))\) jest \(C^1\) z pochodną \(Df(x+t(y-x))(y-x)\). Integracja po t i oszacowanie normy sum Riemanna dają właściwy wzór i nierówność \(\|f(y)-f(x)\|\le M\|y-x\|\).
10. **Ciągła pochodna Gâteaux implikuje Frécheta.** Ograniczone liniowe operatory \(D_Gf(z)\) istnieją w każdym z∈U i zależą ciągle w normie operatorowej. Wzdłuż odcinka różniczkowanie jednowymiarowe oraz ciągłość pochodnej dają wzór całkowy. Po odjęciu \(D_Gf(x)h\) jednostajny iloraz błędu nie przekracza \(\sup_{0\le t\le1}\|D_Gf(x+th)-D_Gf(x)\|\to0\). To prowadzi do \(C^1\); nie próbuje się wnioskować tego z samej punktowej ciągłości f.
11. **Norma na Hilbercie.** Przy rzeczywistej strukturze H i konwencji iloczynu liniowego w pierwszym argumencie \(D_\R(\|x\|^2/2)h=\operatorname{Re}\langle h,x\rangle\) z resztą \(\|h\|^2/2\). Dla x≠0 reguła łańcuchowa ze skalarną funkcją \(\sqrt{t}\) daje pochodną normy, a w zerze dwustronny iloraz \(|t|\|h\|/t\) nie ma granicy w kierunku niezerowym.
12. **Rzeczywista i zespolona pochodna Frécheta.** Po zapomnieniu struktury zespolonej reszta i normy pozostają bez zmiany. Odwrotnie, rzeczywisto-liniowy A jest zespolenie liniowy wtedy i tylko wtedy, gdy \(A(ih)=iA(h)\) dla każdego h. Dlatego kryterium jest konieczne i dostateczne, czego nie należy mylić z samą istniejącą pochodną kierunkową przy parametrze rzeczywistym.

**Werdykt wszystkich 12 dowodów:** bez znalezionej nowej fałszywej tezy ani przeskoku wymagającego poprawki źródła. Jest to przegląd matematyczny, a nie formalna kontrola Lean.

## Ponowny przegląd wszystkich 8 przykładów

1. **Pochodne kierunkowe bez ciągłości:** \(g(x,y)=x^3y/(x^6+y^2)\) poza zerem, g(0)=0; dla ustalonego kierunku \((a,b)\) iloraz różnicowy maleje do zera, ale dla \(y=x^3\) wartość funkcji jest stale 1/2, więc brak ciągłości.
2. **Ciągła Gâteaux, nie Fréchet:** \(f(x,y)=x^3y/(x^4+y^2)\), f(0)=0; dominacja przez \(|x|/2\) gwarantuje ciągłość, wszystkie kierunkowe pochodne w zerze wynoszą zero, natomiast po \(y=x^2\) znormalizowana reszta dąży do 1/2.
3. **Nieliniowe pochodne dwustronne:** \(q(x,y)=x^3/(x^2+y^2)\), q(0)=0, ma w kierunku \((a,b)\ne(0,0)\) wartość \(a^3/(a^2+b^2)\), ale funkcja kierunków nie jest addytywna; \(|x|+|y|\) ilustruje odrębnie pochodną tylko jednostronną.
4. **Funkcja kwadratowa:** \(Q(x)=B(x,x)\) ma pochodną \(B(h,x)+B(x,h)\); na rzeczywistym Hilbercie \(\|x\|^2/2\) daje gradient x i dokładny błąd drugiego rzędu.
5. **Niestabilność ciągłości pochodnej:** \(f(x)=x^2\sin(1/x^2)\) dla x≠0, f(0)=0 ma \(f'(0)=0\), ale dla x≠0 występuje wyraz \(-2x^{-1}\cos(1/x^2)\), który wyklucza ciągłość pochodnej w zerze.
6. **Energia kwadratowa:** dla samosprzężonego A gradient rzeczywisty \(J(x)=\langle Ax,x\rangle/2-\operatorname{Re}\langle x,b\rangle\) to \(Ax-b\); jeśli A jest koercywny, istnieje dokładnie jeden punkt stacjonarny będący minimum dzięki Laxowi–Milgramowi i dodatniości różnicy energii.
7. **Funkcjonał całkowy \(L^2\):** dokładna reszta \(\|h\|_2^2/2\) dowodzi Frécheta, gradient jest u−g, a całka różniczki jest zgodna z konwencją miary.
8. **Sprzężenie i moduł kwadratowy:** \(\overline z\) ma pochodną rzeczywistą \(h\mapsto\overline h\), która nie jest zespolenie liniowa; dla \(|z|^2\) pochodna rzeczywista w z≠0 ma wartości rzeczywiste i nie jest operatorem zespolenie liniowym, ale w zerze zespolona pochodna Frécheta istnieje i jest zerem, bo \(|h|^2=o(|h|)\). W źródle obecny jest jawny argument liniowości nad \(\C\), dodany w 14/01.

**Werdykt 8 przykładów:** bez nowej poprawki. Diagram TikZ na stronie 80 przedstawia krzywą \(y=x^2\), a nie trajektorię wynikającą z jednego ustalonego kierunku; w raporcie 14/01 udokumentowano wizualną inspekcję faktycznego 84-stronicowego PDF tej samej wersji źródła.

## Weryfikacja struktury, odsyłaczy, terminologii i testów

Ponownie pobrano wszystkie rzeczywiste pliki rozdziałów 01–14 z istniejącej gałęzi. Liczba etykiet **280**, liczba duplikatów **0**; rozdział 14 ma **29 etykiet i 4 odsyłacze**, wszystkie odnalezione. Sparowano środowiska: proof 12, twierdzenie 7, stwierdzenie 4, lemat 1, definicja 6, przyklad 8, uwaga 4, tikzpicture 1. W akapitach znaczniki matematyczne są zbilansowane. Nie znaleziono niewłaściwych terminów „sekwencja”, „injektywny”, „dualna” ani niepożądanych oznaczeń funkcji charakterystycznych. Zweryfikowano z bieżącego pliku testów 21 rzeczywistych testów, w tym kontrprzykłady do pochodnej Gâteaux, nieliniowość pochodnych kierunkowych, \(\ell^1\), regułę dwuliniową, zespoloną liniowość i kompletność hipotez. Zielony przebieg #45275533277 wykonuje również kompilację całego kontekstu 01–14 i kontrolę PDF.

## Decyzja przed końcową bramką

**14/03: DRUGI CZYSTY AUDYT MATEMATYCZNO-REDAKCYJNY — 2/2.** Źródło, testy i workflow pozostawiono bez zmian, aby oba czyste audyty odnosiły się dokładnie do bloba SHA 8ea2ec43a6dca36e644000517fa19d589bd134fe. Aby formalnie oznaczyć rozdział 14 jako **STABILNY** i rozpocząć audyt 15/01, należy potwierdzić zakończenie workflow wywołanego tym raportem z wynikiem **SUCCESS**. Do tej chwili nie deklarować wyniku CI z przyszłego przebiegu.
