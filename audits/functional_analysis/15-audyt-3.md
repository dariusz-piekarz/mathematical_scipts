# Analiza funkcjonalna — rozdział 15 — audyt 03 (drugi niezależny czysty przegląd)

**Data:** 23 listopada 2026 r.  
**Istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/15-pochodne-wyzszych-rzedow-i-lokalne-twierdzenia-analizy-nieliniowej.tex`.  
**Blob SHA źródła, niezmieniony od audytów 15/01 i 15/02:** `39f14f53417fd613006032d5cb5e9b7bbdcc6ebe`.  
**Blob SHA regresji:** `b077bed8553d8122a86a3d7dd4dab1dc052a73b5`.  
**Werdykt matematyczno-redakcyjny:** **DRUGI CZYSTY, 2/2**; do końcowego zamknięcia rozdziału wymagany jest pozytywny wynik dedykowanego CI po zapisie niniejszego audytu. Nie zmieniano LaTeX ani testów.

## Rewizja stanu i zielonego CI po 15/02

Ponownie sprawdzono bieżące źródło i testy na gałęzi, dwa wcześniejsze raporty oraz rzeczywisty workflow. Przebieg [#45280205438](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45280205438) dla commitu `05458991b17fd176ab0822c821b7874cce11d2cf` zakończył się **completed/success**. Bezpośredni odczyt dziewięciu kroków joba potwierdził wykonanie regresji, przygotowanie wrappera rozdziałów 01–15, kompilację LaTeX, kontrolę PDF/odsyłaczy i publikację artefaktu. Ta bramka była zielona po audycie 15/02 i dotyczyła identycznych blobów źródła oraz testów.

## Druga niezależna kontrola matematyczna — wszystkie 12 dowodów

1. **Wieloliniowość i ograniczoność:** ciągłość `A` w zerze oraz jednoczesne skalowanie m niezerowych argumentów do kuli o promieniu `delta/2` daje stałą `(2/delta)^m`. Argument z zerowym argumentem wynika z liniowości osobno w każdym z nich. W drugą stronę rozwinięcie przyrostu na skończoną sumę dowodzi ciągłości wszędzie.
2. **Zupełność przestrzeni operatorów wieloliniowych:** dla ciągu Cauchy'ego `(A_n)` wartości w `F` mają granice; wymagane jest, aby `F` było przestrzenią Banacha. Granica zachowuje wieloliniowość i ograniczenie normy; przejście do granicy najpierw punktowe, następnie jednostajne na produkcie kul jednostkowych, jest poprawne.
3. **Izometria przez wyodrębnienie pierwszego argumentu:** dowód utożsamia `sup_{||h0||<=1}sup_{||hj||<=1}` z normą m+1-liniową, a jawne `T_A` zapewnia surjektywność. Nie jest potrzebna zupełność E ani F dla samego utożsamienia.
4. **Symetria drugiej pochodnej:** prostokątny przyrost `Delta(s,t)` podzielony przez `st` można policzyć dwoma kolejnościami całkowania; normowa ciągłość `D²f` uzasadnia przejście do granicy dla dowolnych `h,k`.
5. **Symetria wszystkich wyższych pochodnych:** twierdzenie dla `D^{m-2}f` daje transpozycję argumentów 1 i 2; różniczkowanie symetrii `D^{m-1}f` daje transpozycje w pozycjach 2,...,m. To wystarcza, gdyż transpozycje sąsiednie generują grupę permutacji.
6. **Druga pochodna złożenia:** porządek argumentów `D²g(f(x))[Df(x)h,Df(x)k]` oraz `Dg(f(x))D²f(x)[h,k]` odpowiada pochodnej operatora składania; każdy składnik należy do G.
7. **Taylor z resztą całkową:** `gamma(t)=f(x+th)` jest `C^m`; iterowane podstawowe twierdzenie rachunku daje czynnik `(1-t)^{m-1}/(m-1)!`. Po odjęciu stałej `D^mf(x)[h^m]` norma reszty nie przekracza `||h||^m/m!` razy supremum normy różnicy pochodnych na odcinku. Ciągłość w x uzasadnia resztę `o(||h||^m)`.
8. **Minimum lokalne:** konieczność wynika z ograniczenia `f(x0+th)` do każdej prostej; wystarczalność wymaga *jednostajnego* oszacowania `D²f(x0)[h,h]>=c||h||²`. Przez ciągłość `D²f` otrzymujemy stałą `c/2` w pobliżu i `c/4` w oszacowaniu przyrostu.
9. **Szereg Neumanna:** tożsamość `(I-T)S_N=S_N(I-T)=I-T^{N+1}` daje obustronną odwrotność w granicy. Zupełność `L(E)` oraz `||T||<1` są jawne.
10. **Otwartość `GL(E)` i pochodna odwracania:** `A+H=A(I+A^{-1}H)`, a błąd przybliżenia pierwszego rzędu wynosi `A^{-1}H(A+H)^{-1}HA^{-1}`, więc ma normę `O(||H||²)`. Wzór na `D iota(A)H` jest poprawny bez założenia komutowania A i H; ciągłość i kolejne pochodne wynikają z ciągłych operacji wieloliniowych.
11. **Twierdzenie o funkcji odwrotnej i regularność `C^m`:** kontrola `||I-A^{-1}Df(x)||<=q<1` na domkniętej kuli daje kontrakcję `T_y`, jej jednoznaczny punkt stały oraz nierówność `||x-z||<=||A^{-1}||/(1-q)||f(x)-f(z)||`. Otwartość obrazu trzeba dowieść osobno — w tekście istotnie stosuje się kontrakcję na małych kulach wokół dowolnego x. Rozwijając `f(x+h)` i korzystając z powyższej nierówności, otrzymujemy resztę `o(||k||)` dla odwrotności. Wyższa regularność wynika z indukcji na `Dg=(Df\circ g)^{-1}`.
12. **Twierdzenie o funkcji uwikłanej:** blokowy izomorfizm `(h,k)->(h,Bh+Ak)` ma ograniczoną odwrotność `(h,z)->(h,A^{-1}(z-Bh))`. Lokalny dyfeomorfizm `Psi(x,y)=(x,F(x,y))` i zmniejszenie prostokątów zapewniają zarówno istnienie, jak i jedyność rozwiązania dla wszystkich punktów ich iloczynu. Różniczkowanie `F(x,phi(x))=0` daje prawidłowy wzór na `Dphi` wraz z wymaganą odwracalnością `D_yF`.

**12/12 dowodów bez nowo stwierdzonej luki lub fałszywej hipotezy.** Kontrola matematyczna nie stanowi formalizacji w Lean.

## Przegląd pięciu przykładów — 5/5

1. **Wielomiany z operatorów m-liniowych:** dla symetrycznego B dokładnie `D^mP=m!B`; dla B niesymetrycznego teza `m!B` nie jest automatycznie prawdziwa i tekst jej nie przypisuje.
2. **Hesjan na rzeczywistym Hilbercie:** `D²J(x)[h,k]=<h,((A+A*)/2)k>`; samosprzężoność części symetrycznej uzasadnia równość po zamianie h i k.
3. **Dodatnia forma bez jednostajnej dodatniości:** dla `x=t e_n`, `t=1/n`, `f(x)=1/(2n³)-1/n³<0` i `||x||=1/n->0`; oszacowanie `||D²(||x||³)||<=6||x||` uzasadnia klasę `C²` także w zerze.
4. **Lokalna odwracalność mapy Hilberta:** `Df(0)=I`; gdy `v!=0`, globalna różnowartościowość faktycznie zawodzi już na prostej `span(v)`: `f(0)=f(-v/||v||²)=0`. Tekst słusznie nie twierdzi o globalnej odwrotności.
5. **Równanie `(I-lambda K)u=g`:** w otoczeniu `lambda=0` Neumann gwarantuje jednoznaczność i wzór `u(lambda)=sum lambda^n K^n g`. Stąd `u'(0)=Kg`, `u''(0)=2K²g`.

## Niezależne kontrole LaTeX, języka, odsyłaczy i wizualna PDF

Ponownie odczytano rzeczywiste pliki **01–15** z bieżącej gałęzi i sprawdzono etykiety oraz odwołania: **302 etykiety, 0 duplikatów, 124 odsyłacze, 0 nierozwiązanych**. W rozdziale 15 stwierdzono prawidłowo sparowane środowiska: 12 `proof`, 4 `twierdzenie`, 4 `stwierdzenie`, 2 `lemat`, 3 `wniosek`, 2 `definicja`, 5 `przyklad` oraz 1 `uwaga`. Zbadano jawność założeń, brak nieuzasadnionej zmiany ciała skalarów i konsekwentne rozróżnienie pochodnej Frécheta od kierunkowej. Źródło nie zawiera rysunków TikZ.

Niezależnie otwarto faktyczny artefakt PDF `functional-analysis-ch15-pdf` z wcześniejszego dedykowanego CI: `pdfinfo` potwierdza **90-stronicowy dokument A4**. Wyrenderowano strony **84–90**, obejrzano ich zbiorczy podgląd: nagłówek i treść rozdziału 15 są widoczne od s. 84; wykresów w tym rozdziale nie ma; nie dostrzeżono obciętych wzorów, nałożeń tekstu ani uszkodzonych stron. W rzeczywistym logu LaTeX liczby diagnostyk `Undefined control sequence`, `There were undefined references`, `Overfull \\hbox`, `Underfull \\hbox`, `Missing character` oraz `LaTeX Warning:` wynoszą **0**.

## Decyzja i warunek zamknięcia

**15/03 — DRUGI NIEZALEŻNY CZYSTY AUDYT; matematyka/redakcja 2/2, bloby źródła i testów niezmienione.** Ten raport powinien wyzwolić dedykowany workflow rozdziału 15. **Nie oznaczać rozdziału jako ostatecznie STABILNY, dopóki po niniejszym commicie CI nie zostanie potwierdzone jako completed/success.** Po jego zielonym wyniku stabilizację można formalnie domknąć i odblokować jednostkę **15A** (przed rozdziałem 16 zgodnie z kolejnością książki). Plan dodatniego pierwiastka operatora pozostaje przy rozdziale 32.
