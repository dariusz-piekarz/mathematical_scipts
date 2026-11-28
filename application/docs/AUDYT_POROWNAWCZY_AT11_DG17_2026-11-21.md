# Etap V: porównawczy audyt AT-11 / DG-17

**Data:** 21 listopada 2026 r.
**Repozytorium:** dariusz-piekarz/mathematical_scipts.
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez nowych gałęzi i bez aktualizacji main).
**Rozdziały:** AT-11 i DG-17, „Przecięcia, dualność i klasy charakterystyczne”.
**Reguła:** audyt poprawności matematycznej, hipotez, znaków, kompletności dowodów i przykładów, rysunków, terminologii oraz niezależności źródeł. Nie wykonano automatycznego scalania ani zmiany historycznych \label.

## 1. Wyniki porównania treści i pochodzenia

Po audycie istnieją **42 wspólne nazwy etykiet**, **8 etykiet unikalnych AT** oraz **11 etykiet unikalnych DG**. Wspólność nazwy etykiety nie gwarantuje wspólności założeń ani tego samego stopnia szczegółowości dowodu. Pełny wykaz z rozdzieleniem właścicieli znajduje się w
application/config/KANDYDACI_SCALEN_AT_DG_ETAP_05.json.

Osiem unikalnych AT:
- sec:lokalne-kolancuchy-v4 i prop:local-delta-v4 (konstrukcja kołańcuchów ze skręconymi współczynnikami, funktorialność i monodromia);
- sec:pl-v4 i thm:pl-v4 (dualność Poincarégo–Lefschetza);
- sec:alexander-v4 i thm:alexander-v4 (dualność Aleksandra dla zwartego A z kohomologią Čecha);
- prz:formy-przeciecia-cp2-s2 i fig:formy-przeciecia-parzystosc (formy przecięcia rozróżniające przestrzenie o tych samych grupach homologii).

Jedenaście unikalnych DG:
- prz:kubek-kap-trojkat-21; prz:pd-torus-sfery-21; prz:pd-dysk-21; prz:przeciecia-krzywych-torus-21;
- prz:pd-rp2-21; prz:sw-rp2-21; prz:sw-sfera-stabilna-21;
- fig:indeksy-torus-21; fig:chirurgia-walce-21; prz:cp2-forma-21;
- prz:samoprzeciecie-wykres-stopien-17 (NOWY przykład z tej iteracji).

Zachować sumę powyższych treści, a także szczegółowe warianty dowodów ukryte pod wspólnymi nazwami etykiet.

## 2. Audyt wybranych wspólnych rezultatów

### Iloczyn kubkowy i przemienność stopniowana (prop:kubek-graded-16)

Oba źródła przyjmują konwencję Alexandera–Whitneya, z iloczynem na pierwszej i ostatniej ścianie sympleksu, zachodzącej na jednym wierzchołku.
W AT-11 poprzedni dowód łańcuchowej przemienności z właściwym znakiem opierał się na ogólnej deklaracji acykliczności kompleksu $C_*(\sigma)\otimes C_*(\sigma)$. **Rozwinięto krok konstrukcyjnie:**
- stożek $h$ do pierwszego wierzchołka oraz projekcja $P=i\epsilon$ spełniają $\partial h+h\partial=\mathrm{id}-P$;
- homotopia na iloczynie tensorowym ma postać
  $K(a\otimes b)=h(a)\otimes b+(-1)^{|a|}P(a)\otimes h(b)$;
- rachunek ze znakami Koszula daje $\partial K+K\partial=\mathrm{id}-P\otimes P$;
- cykl $z=TA(\sigma)-A(\sigma)-H(\partial\sigma)$ jest stopnia dodatniego, zatem $H(\sigma)=Kz$ dostarcza wymagane wypełnienie.
Wynik dla kocykli to $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$.

Dopisano ostrzeżenie o **kwadracie klasy nieparzystego stopnia**: z przemienności stopniowanej wynika tylko $2a^2=0$; gdy 2 jest odwracalne, $a^2=0$, lecz nad $\mathbb F_2$ w $H^*(\mathbb{RP}^2;\mathbb F_2)$ istnieje $x\in H^1$ z $x^2\ne0$. Nie należy twierdzić, że dowolny iloczyn nieparzystej klasy przez siebie musi zawsze znikać.

### Dualność Poincarégo (thm:poincare-dualnosc-16)

Oba dowody wykorzystują komórki dualne i porównanie ich operatora brzegu z kobrzegiem oraz klasę fundamentalną. DG-17 dokładniej konstruuje homotopię łańcuchową między reprezentacją komórki dualnej i iloczynem kapowym, i rozwija argument o wagach barycentrycznych przy brzegu. AT-11 pozostawia bardziej syntetyczny wariant. Przy docelowym scalaniu zachować pełniejszą kontrolę stopni i znaków z DG oraz interpretację globalną z AT; dla rozmaitości z brzegiem zachować dokładnie dwie, nierównoważne bezwzględnie/względnie wersje dualności. Nie zastępować grup względnych bezwzględnymi.

### Dualność ze skręconymi współczynnikami (thm:pd-skrecenie-16)

W obu wersjach obecna jest skręcona klasa fundamentalna i system orientacji $\mathcal O_M$. AT-11 ma ponadto osobną konstrukcję skręconych kołańcuchów: współczynniki są we włóknach nad pierwszym wierzchołkiem i operator $\delta$ transportuje klasę pominiętej pierwszej ściany odwrotnie do pierwotnego punktu. Weryfikacja $\delta^2=0$ opiera się na homotopii drogi $01*12$ z $02$ w obrazie dwusympleksu. DG-17 rozwija z kolei konkretny rachunek $\mathbb{RP}^2$ z komórkową różniczką $T-1$ i $1+T$.
Nie utożsamiać lokalnego systemu orientacji przy brzegu z grupą $H_n(M,M\setminus\{p\})$, która w punkcie brzegu znika.

### Dualność Poincarégo–Lefschetza i Aleksandra: tylko AT

Wersje Poincarégo–Lefschetza w thm:pl-v4:
$H^k(M;\mathcal L)\cong H_{n-k}(M,\partial M;\mathcal L\otimes\mathcal O_M)$ oraz
$H^k(M,\partial M;\mathcal L)\cong H_{n-k}(M;\mathcal L\otimes\mathcal O_M)$.
Konwencje współczynników i warunki orientacji muszą pozostać jawne.

Twierdzenie thm:alexander-v4 wiąże $\widetilde H_i(S^n\setminus A;G)$ z **kohomologią Čecha** zwartego $A$, a nie automatycznie z kohomologią singularną dowolnego dzikiego zbioru. W dowodzie potrzebne są regularne otoczenia i granice proste homologii dopełnień. Ten fragment musi pozostać osobnym pełnym modułem lub sekcją przed scaleniem, z zachowaniem odsyłaczy do wcześniejszego rozdziału o kohomologii Čecha.

### Klasy Stiefela–Whitneya (thm:wi-klasy-16)

W AT-11 dowód twierdzenia o module dla wiązki projektowej zawierał skok „sprawdzić komórka po komórce”. **Rozwinięto go**:
- konstrukcja odwzorowań
  $\Phi^q_{B,A}:\bigoplus_{j=0}^{r-1}H^{q-j}(B,A;\mathbb F_2)\to H^q(P_B,P_A;\mathbb F_2)$;
- analiza pary nad każdą dołączaną komórką jako
  $(D^d\times\mathbb RP^{r-1},\partial D^d\times\mathbb RP^{r-1})$;
- identyfikacja grup względnych ze stopniowo przesuniętymi grupami kohomologii włókna;
- użycie diagramu długich ciągów par i lematu pięciu odwzorowań, w tym uzasadnienie przypadku nieskończenie wielu komórek w skończonym wymiarze.

DG-17 zachowuje bardzo wartościowe, niewystępujące w AT obliczenia
$w(T\mathbb RP^2)=1+x+x^2$ oraz $w(TS^2)=1$ mimo nietrywialności $TS^2$. W obu plikach uniknięto błędnego koła w wyprowadzeniu $w_i$ z klasy Thoma i z iloczynu Eulera modulo 2.

### Klasa Eulera, samoprzecięcie i formy całkowite

Oba źródła ustanawiają, że orientowana normalna wiązka do zamkniętej środkowymiarowej podrozmaitości mierzy jej samoprzecięcie. AT ma kompletny przykład
$N=\mathbb CP^2\#\overline{\mathbb CP^2}$ oraz $S^2\times S^2$:
obie mają jednakowe grupy homologii, ale odpowiednio nieparzystą formę $\operatorname{diag}(1,-1)$ i parzystą formę hiperboliczną $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$. Ich przestrzenie nie mogą być homotopijnie równoważne.
Dopisano też w AT jawny argument, że antysymetryczna unimodularna całkowita macierz wymiaru nieparzystego ma wyznacznik 0, co jest sprzeczne z $\det Q=\pm1$. Stąd ranga środkowej homologii w wymiarze $4m+2$ jest parzysta.

W DG-17 dodano **niezależny, parametryczny przykład**:
- dla $f:S^2\to S^2$ o stopniu $d$, wykres $\Gamma_f$ ma klasę $A+dB$ w $H_2(S^2\times S^2)=\mathbb Z A\oplus\mathbb Z B$;
- macierz hiperboliczna daje $Q(A+dB,A+dB)=2d$;
- różniczka wykresu identyfikuje normalną przez $[(v,w)]\mapsto w-Df(v)$ z $f^*TS^2$; orientacja jest dodatnia, bo odpowiednia macierz blokowa ma wyznacznik 1;
- pole $X(x)=e_3-\langle e_3,x\rangle x$ ma zera na północnym i południowym biegunie, o lokalnych różniczkach $-I_2$ i $I_2$ i dwóch indeksach +1, stąd $\langle e(TS^2),[S^2]\rangle=2$;
- naturalność klasy Eulera daje $I(\Gamma_f,\Gamma_f)=2d$, zgodnie z metodą homologii.
Sprawdzono w szczególności $d=0,1,-1$. Nie używa się twierdzenia Poincarégo–Hopfa, więc obliczenie nie jest koliste względem późniejszej sekcji.

## 3. Zmiany faktycznie zapisane

- AT-11: rozwinięto dowód przemienności stopniowanej, projektowego Leraya–Hirscha, dodano wyjaśnienia o kwadratach nieparzystych klas i parzystej randze form antysymetrycznych;
- DG-17: wprowadzono pełen przykład $\Gamma_f$ z dwiema metodami obliczenia;
- w obu plikach poprawiono redakcyjne formy „kocykel” i „injektywny”;
- DG-17: ujednolicono termin „kołańcuch” w miejsce obcego „kochain”;
- stworzono manifest bezstratnego scalania application/config/KANDYDACI_SCALEN_AT_DG_ETAP_05.json oraz dziesięć testów application/tests/test_at_dg_pairwise_11_17.py;
- stworzono dedykowany workflow .github/workflows/paired-at-dg-duality-characteristic-audit.yml.

Wszystkie historyczne \label, \ref, \eqref, rysunki i inne niepowtarzalne przykłady pozostawiono. Zmiany nie dotyczą main i nie ustanawiają nowego właściciela wspólnych etykiet.

## 4. Testy i kompilacja

GitHub Actions: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44838288490

Testy obejmują:
- obliczenia macierzy formy przecięcia dla $d=-12,\ldots,12$;
- niezależne porównanie znaków wyznaczników $4\times4$ dla normalnej wykresu;
- obliczenie indeksów obu zer pola na $S^2$;
- parzystość formy hiperbolicznej i nieparzystość drugiej unimodularnej formy;
- zerowanie wyznaczników całkowitych antysymetrycznych macierzy $3\times3$;
- zachowanie wszystkich unikalnych źródłowych etykiet oraz bilans środowisk TeX;
- obecność jawnych homotopii i diagramów względnych w dwóch uzupełnionych dowodach.

Dedykowany workflow buduje trzykrotnie pełny aktualny tom AT-01–30 oraz pełny aktualnie zaimportowany tom DG-01–20, a nie tylko wycinek DG-01–10.
Znane odsyłacze DG do jeszcze niezaimportowanych rozdziałów 21–36 są kontrolowane według jawnej listy dopuszczonych etykiet. Nie są deklarowane jako naprawione bez importu źródeł. Nie wolno utożsamiać poprawnego składu PDF z globalną weryfikacją wszystkich twierdzeń.

**Zweryfikowany wynik:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44838349123 —
oba zadania GitHub Actions zakończone SUCCESS na najnowszej wersji czterech plików audytu:
- **10/10 testów matematycznych — OK**;
- **AT-01–30: 297 stron**; trzy przebiegi pdflatex, brak nieustabilizowanych odsyłaczy i przepełnień wierszy;
- **DG-01–20: 488 stron**; trzy przebiegi pdflatex, brak niestabilnych odsyłaczy i przepełnień wierszy;
- **12 różnych, jawnie dopuszczonych brakujących etykiet DG** (13 użyć, jedna nazwa powtórzona):
  ch:chern-weil, ch:grafy-wezly-cztery, cor:bochner-vanishing, cor:hodge-de-rham,
  lem:angular-form-26, prop:euler-identification-26, prz:hodge-dwie-sfery-18,
  prz:thur-dop-nil-kontakt, sec:algebra-liego, sec:rownanie-diraca,
  subsec:dirac-koneksja, thm:CGB-boundary-26.
  Ich cele znajdują się w niezaimportowanych późniejszych rozdziałach,
  a workflow odrzuca dodatkowe, niespodziewane nazwy.

Pobrano z GitHub Actions dwa rzeczywiste dokumenty PDF z ostatniego przebiegu.
Oględziny po wyrenderowaniu (bez OCR): AT strony 128, 129, 140 i 148,
DG strony 437 i 438. Sprawdzono czytelność wszystkich kluczowych
równości, podpisów, numerów twierdzeń, diagramu form przecięcia
oraz podziału stron nowego przykładu wykresu. Nie zauważono nakładania
się podpisów, obcięć ani zniekształceń czcionek.

## 5. Dalsze zadania

Przed scaleniem należy uzgodnić założenia o systemach lokalnych, porównać szczegółowo kolejne etapy dualności Aleksandra z niezależnym skryptem kohomologii Čecha i przeprowadzić audyt odsyłaczy DG-21–36 po rzeczywistym imporcie brakujących rozdziałów.

Kolejna jednostka porównawcza powinna zostać wybrana na podstawie aktualnej mapy pokrycia AT–DG–AG i rzeczywistego stanu najnowszej gałęzi, nie na podstawie podobieństwa samych tytułów.
