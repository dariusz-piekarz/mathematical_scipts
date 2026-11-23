# Analiza funkcjonalna — rozdział 14 — audyt 01 (matematyka, redakcja, regresje)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Źródło:** chapters/pl/functional_analysis/14-pochodne-gateaux-i-frecheta-w-przestrzeniach-banacha-i-hilberta.tex.  
**SHA przed audytem:** 87f8e83ef4e95124f587e3dc78f7dfb4a740a972.  
**SHA po poprawkach:** 8ea2ec43a6dca36e644000517fa19d589bd134fe.  
**Werdykt:** **AUDYT Z POPRAWKAMI, 0/2 czystych przeglądów**. Rozdział 15 pozostaje zablokowany do dwóch niezależnych czystych audytów i zielonej bramki technicznej.

## Zastany stan i kolejność pracy

Przed wykonaniem zmian zweryfikowano katalog audytów na gałęzi: rozdział 13 jest oznaczony **STABILNY — 2/2** po audytach 13/03 i 13/04, zaś [ostatni przebieg CI #45271147469](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45271147469) zakończył się **completed/success**. Nie było raportu 14/01 ani testów/workflow ch14. W niniejszej iteracji po raz pierwszy audytowano 14, bez przedwczesnego przejścia do 15.

## Przegląd wszystkich 12 dowodów

1. **Fréchet implikuje Gâteaux i ciągłość.** Niech \(A=Df(x)\), \(r(h)=o(\|h\|)\). Ograniczoność A wraz z oszacowaniem reszty zapewnia ciągłość f w x. Dla ustalonego h podstawienie \(th\) daje \(\|r(th)/t\|=\|h\|\cdot\|r(th)\|/\|th\|\to0\). Identyfikacja ze wszystkimi pochodnymi kierunkowymi daje również jednoznaczność A.
2. **Kryterium jednostajne względem kierunków.** Dla \(\|h\|=1\) supremum po h i sfera \(\|k\|=|t|\) dają to samo maksimum górne błędu. Otwarta dziedzina zapewnia wspólne dopuszczenie wszystkich małych przyrostów. Wyłączenie E={0} jest jawne; implikacja odwrotna przez \(t=\|k\|,\,h=k/\|k\|\) jest poprawna.
3. **Brak reguły łańcuchowej dla samej pochodnej Gâteaux.** Funkcja \(f(x,y)=x^3y/(x^4+y^2)\) ma w zerze pochodną kierunkową równą zero w każdym kierunku, lecz na \(\gamma(t)=(t,t^2)\) zachodzi \(f(\gamma(t))=t/2\); zatem \((f\circ\gamma)'(0)=1/2\) mimo \(D_Gf(0)\gamma'(0)=0\). Kontrprzykład jest poprawny i nie przeczy regule Frécheta.
4. **Norma \(\ell^1\): Gâteaux bez Frécheta.** Przy niezerowych współrzędnych x kierunkowe ilorazy mają majorantę \(|h_n|\) i punktowo zbiegają do \(\operatorname{sgn}(x_n)h_n\). Zbieżność zmajoryzowana dla szeregu daje ciągły funkcjonał o normie 1. Przyrosty \(h^{(n)}=-2x_ne_n\) dążą w normie \(\ell^1\) do 0, lecz stosunek błędu do normy przyrostu stale jest 1. Argument wyklucza pochodną Frécheta.
5. **Suma i składanie z operatorem liniowym.** Rozwinięcia pierwszego rzędu i ograniczenie \(\|Tr(h)\|\le\|T\|\|r(h)\|\) dają właściwe reguły. Dla funkcji afinicznej pochodna L, reszta zerowa.
6. **Reguła łańcuchowa Frécheta.** Dla \(k=Ah+r(h)\) zachodzi \(\|k\|\le(\|A\|+1)\|h\|\) przy małym h. Wyrazy \(Br(h)\) oraz \(s(k)\) są \(o(\|h\|)\), również przy \(k=0\). Nie jest potrzebna ciągłość pochodnych na otoczeniu.
7. **Ciągłe odwzorowanie dwuliniowe.** Reszta dokładnie równa \(B(h,k)\), ograniczona przez \(C\|h\|\|k\|\), czyli \(o(\max(\|h\|,\|k\|))\). Reguła dla \(B(f,g)\) wynika z rachunku na przestrzeni produktowej. **Zidentyfikowano brak jawnego założenia o przestrzeni E**, z której wychodzą f i g; poprawiono tezę z „Niech E1,E2,G” na „Niech E,E1,E2,G będą rzeczywistymi przestrzeniami Banacha”. Obecnie wszystkie obiekty mają ustalony typ i dziedzinę.
8. **Podstawowe twierdzenie rachunku dla krzywych Banacha.** Ciągłość \(\gamma'\) na zwartym odcinku zapewnia jednostajną ciągłość i kryterium Cauchy'ego sum Riemanna w zupełnym F. Dla każdego przedziału podziału normę błędu aproksymacji przyrostu przez \(\gamma'(\xi)\Delta t\) kontroluje skalarne twierdzenie o wartości średniej zastosowane do funkcjonałów rzeczywistych z kulą jednostkową \(F'\); Hahn–Banach przywraca oszacowanie normy. Sumowanie i granica dają wzór całkowy.
9. **Wzór całkowy i oszacowanie przyrostu.** Łańcuchowa dla \(\gamma(t)=f(x+t(y-x))\) daje ciągłą pochodną \(\gamma'(t)=Df(x+t(y-x))(y-x)\). Poprzedni lemat zapewnia równość całkową, a norma całki nie przekracza całki normy.
10. **Ciągła pochodna Gâteaux implikuje \(C^1\).** Na każdym odcinku wewnątrz U funkcja \(t\mapsto f(x+th)\) jest różniczkowalna z ciągłą pochodną \(D_Gf(x+th)h\). Jednostronne granice zapewniają ciągłość w końcach odcinka. Wzór całkowy i supremum norm operatorów na odcinku kontrolują błąd jednostajnie po h; z założonej ciągłości \(D_Gf\) wynika Fréchet.
11. **Rzeczywista pochodna kwadratu normy i normy Hilberta.** Tożsamość \(\frac12\|x+h\|^2-\frac12\|x\|^2-\operatorname{Re}\langle h,x\rangle=\frac12\|h\|^2\) daje Frécheta. Dla x różnego od zera działa rzeczywista reguła łańcuchowa ze skalarnym pierwiastkiem. W zerze, jeśli H jest niezerowe, dwustronna pochodna kierunkowa normy nie istnieje.
12. **Rzeczywista i zespolona różniczkowalność Frécheta.** Zespolona pochodna jest rzeczywisto-liniowa z tą samą resztą. Odwrotnie, rzeczywista pochodna jest zespolona dokładnie wtedy, gdy ograniczony rzeczywisto-liniowy operator A spełnia \(A(ih)=iAh\). Dowód poprawnie używa kompleksowej liniowości, a nie samego istnienia granic dla rzeczywistego parametru.

**Werdykt 12/12:** nie wykryto fałszywych tez, lecz poprawiono niepełne założenie dla reguły dwuliniowej.

## Przegląd wszystkich 8 przykładów i rysunku

1. **Nieciągła funkcja o zerowych wszystkich pochodnych kierunkowych:** \(g(x,y)=x^3y/(x^6+y^2)\), \(g(0)=0\). Na prostych przez zero iloraz jest zerowy w granicy, natomiast wzdłuż \(y=x^3\) wartość to 1/2. Nie zachodzi nawet ciągłość mimo istnienia pochodnej Gâteaux równej zero.
2. **Ciągła funkcja różniczkowalna Gâteaux bez Frécheta:** \(f(x,y)=x^3y/(x^4+y^2)\) ma \(|f|\le|x|/2\), pochodne kierunkowe zero i wartość \(x/2\) na \(y=x^2\); stosunek błędu do \(\sqrt{x^2+x^4}\) dąży do 1/2.
3. **Pochodne dwustronne nieliniowe w kierunku:** \(q=x^3/(x^2+y^2)\) poza zerem daje \(\partial_{(a,b)}q(0)=a^3/(a^2+b^2)\) dla niezerowego kierunku. W kierunkach \((1,0)\), \((0,1)\) i \((1,1)\) wartości 1, 0 i 1/2 naruszają addytywność. Rozróżniono dodatkowo jednostronną pochodną funkcji \(|x|+|y|\) od dwustronnej.
4. **Odwzorowanie kwadratowe i Hilbert:** \(DQ(x)h=B(h,x)+B(x,h)\), a dla \(\frac12\|x\|^2\) rzeczywista pochodna to \(\langle h,x\rangle\) i dokładny błąd kwadratowy.
5. **Pochodna istniejąca, lecz nieciągła:** \(f(x)=x^2\sin(1/x^2)\) dla x różnego od zera, \(f(0)=0\). W zerze pochodna jest zero, a wyrażenie \(-2x^{-1}\cos(1/x^2)\) przy x różnym od zera uniemożliwia ciągłość pochodnej w zerze.
6. **Gradient energii kwadratowej:** dla samosprzężonego A i rzeczywistej struktury Hilberta \(D_\R J(x)h=\operatorname{Re}\langle h,Ax-b\rangle\), z gradientem \(Ax-b\). Koercywność zapewnia jedynego minimizatora \(Ax=b\), dzięki Laxowi–Milgramowi.
7. **Funkcjonał całkowy w \(L^2\):** rozwinięcie kwadratu daje \(DJ(u)h=\int (u-g)h\,\mathrm d\mu\), gradient \(u-g\) i resztę \(\frac12\|h\|_2^2\).
8. **Sprzężenie zespolone i kwadrat modułu:** rzeczywista pochodna \(z\mapsto\overline z\) jest antyliniowa względem i, a pochodna \(z\mapsto|z|^2\) ma niezerowe wartości rzeczywiste dla \(z\ne0\), co wyklucza jej zespoloną liniowość. **Rozbudowano uzasadnienie** przez jawne kryterium \(A(ih)=iAh\). W zerze \(|h|^2=o(|h|)\), więc istnieje zespolona pochodna równa zero.

**Rysunek:** jeden diagram TikZ przy kontrprzykładzie reguły łańcuchowej; pokazuje krzywą \(y=x^2\) i ustalone kierunki. Jest semantycznie zgodny z matematycznym przykładem; jego faktyczny układ graficzny należy zweryfikować na wygenerowanym PDF po zakończeniu CI.

## Kontrola LaTeX, terminologii, odsyłaczy

Pobrano wszystkie źródła rozdziałów 01–14: **280 etykiet bez duplikatów**, w tym **29 etykiet rozdziału 14**; rozdział 14 zawiera **4 odsyłacze, wszystkie rozwiązane**. Sparowano: 12 proof, 7 twierdzenie, 4 stwierdzenie, 1 lemat, 6 definicja, 8 przyklad, 4 uwaga, 1 tikzpicture. Nie znaleziono niedozwolonej terminologii „sekwencja”, „dualna”, „injektywny”, „wskaźnik” ani oznaczeń funkcji charakterystycznej przez \`\\mathbf{1}\`. Znaczniki matematyki inline zostały sparowane.

## Testy i workflow

Dodano \`tools/tests/test_functional_analysis_ch14.py\` z **21 testami regresyjnymi**, obejmującymi: pełną strukturę źródeł 01–14, terminologię, referencje, formalną reprezentację obu kontrprzykładów z \(\R^2\), brak reguły łańcuchowej dla Gâteaux, \(\ell^1\) z perturbacjami współrzędnych, różniczkowanie funkcji dwuliniowych i energii kwadratowych, przyrost krzywej Banacha, nieciągłą pochodną, różniczkowanie normy Hilberta, sprzężenie zespolone, \(|z|^2\) w zerze oraz obecność diagramu TikZ.

Dodano \`.github/workflows/functional-analysis-ch14.yml\`: testy, przygotowanie faktycznego skryptu z \`\\input\` 01–14, kompilacja LaTeX, kontrola PDF/logu/odsyłaczy i udostępnienie PDF. W pierwszym przebiegu #45273100710 testy i przygotowanie skryptu przeszły. Wyniku całego workflow nie należy deklarować, dopóki GitHub nie zwróci stanu \`completed/success\`.

## Decyzja

**14/01: Z POPRAWKAMI — 0/2 czystych audytów.** Kolejna iteracja powinna sprawdzić wynik CI, wizualnie skontrolować PDF (zwłaszcza wykres \(y=x^2\)), ponownie przeanalizować cały rozdział 14 na niezmienionym blobie i wykonać audyt 14/02. Rozdział 15 zablokowany do dwóch czystych niezależnych kontroli identycznego źródła.
