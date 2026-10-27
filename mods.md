# Uzasadnienia zmian w repozytorium `mathematical_scipts`

## 2026-10-27 — wspólny przykład chirurgii w rozdziałach 26–28

### Problem

Rozdział 26 pokazywał przejście od sfery do produktu, rozdział 27
liczył hiperboliczne jądro, a rozdział 28 podawał ciąg chirurgii.
Brakowało jednego przypadku, w którym czytelnik widzi te same dane
normalne, uchwyt, przeszkodę i strukturę w kolejnych miejscach.
Dotychczasowe zdanie o $\mu=0$ mogło też sugerować, że sama
trywialność wiązek normalnych wyznacza kwadratową część przeszkody.

### Rozwiązanie i wpływ

W `22-chirurgia-geometryczna.tex` zapisano standardowy ślad
$S^6\to S^3\times S^3$ z uchwytem indeksu trzy i dualnym uchwytem
indeksu cztery. Wybrano dane normalne lokalnej stabilizacji zgodne
z produktowymi obramowaniami obu sfer czynnikowych.
W `23-przeszkoda-chirurgiczna.tex` połączono istniejący przykład
hiperbolicznego jądra z tym śladem i doprecyzowano, dlaczego
$\mu(A)=\mu(B)=0$ dla wybranego obramowania. Rachunku macierzy
nie powielono. W `24-ciag-chirurgii.tex` policzono Arfa, zerową
klasę w $L_6^s(\Z)$ i normalny niezmiennik $a=0$; zaznaczono,
że mapa z niezerowym jądrem nie jest jeszcze elementem zbioru
struktur, a nad $a$ leży tylko struktura standardowej sfery.

Kompromis: przykład reprezentuje punkt bazowy ciągu i nie służy
klasyfikacji wszystkich struktur nad $S^6$. Podstawy geometrii
uchwytów, standardowej pary kwadratowej i dokładności pozostają
jawnie cytowanymi wynikami Walla.
Po pierwszym składzie nagłówek nowego przykładu w rozdziale 28
zostawał u dołu strony. Dodano `\clearpage` przed przykładem;
kosztem niewielkiej wolnej przestrzeni na poprzedniej stronie
cały przykład zaczyna się teraz od góry następnej strony.

### Weryfikacja

Sprawdzono zgodność wymiarów uchwytów, położenie sfery dualnej,
wybór danych normalnych i wzór $q(\bar x[A]+\bar y[B])=\bar x\bar y$
z [§§1, 5 i 10 Walla](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf)
oraz z wcześniejszymi przykładami w rozdziałach 26–27.
Pełny skład czterech tomów zakończył się po dwóch przebiegach:
216, 182, 99 i 80 stron. Indeksy przyjęły 113, 96, 28 i 93 wpisy
bez odrzuconych. Kontrola logów, łączy do pozostałych tomów
i sum SHA-256 kopii PDF przeszła. Strony 43 i 51 tomu III sprawdzono
po korekcie danych normalnych, a strony 77–79 po ostatnim składzie,
bez uwag.

## 2026-10-27 — uzupełnienie ciągu chirurgii w tomie III

### Problem

Rozdział 28 podawał poprawny ciąg chirurgii i wyjaśnienie dokładności,
ale pozostawiał czytelnikowi przejście od normalnej mapy do każdej
strzałki. Wersja z ustalonym brzegiem i dokładne połączenie ze
strukturami gładkimi $S^7$ były tylko zaplanowane.

### Rozwiązanie i wpływ

W `tex/rozdzialy/24-ciag-chirurgii.tex` dodano diagram podniesienia
normalnej fibracji do $BO$, konstrukcyjne opisy czterech strzałek,
diagram śladu nad $X\times I$ i doprecyzowanie sklejania śladów
o przeciwnych przeszkodach. Nowa sekcja podaje ciąg względny dla
zwartego gładkiego $X^n$, $n\geq5$, z ustalonym brzegiem, a przykład
$D^n$ pokazuje rolę ilorazu $X/\partial X$. Związek
$\mathcal S^s_{\mathrm{DIFF}}(S^7)\cong\Theta_7$ uzasadniono
bez sugerowania, że liczba $28$ wynika z obliczenia tego ciągu.
Po niezależnym przeglądzie doprecyzowano, że mapy względne wysyłają
brzeg w punkt bazowy i są rozpatrywane z homotopiami ustalonymi
na brzegu; sama stałość mapy na brzegu byłaby za słabym warunkiem.
Stary abstrakcyjny rysunek powielał nowy opis i po rozbudowie
przenosił się na osobną niemal pustą stronę, więc go usunięto;
sekcja względna zaczyna się teraz od nowej strony.
`PLAN_DZIALANIA.md` zapisuje potwierdzoną przez autora kolejność
dalszych prac tomu III, a `PRZEGLAD.md` rozdziela własne wyjaśnienia
od wyników Walla i klasyfikacji sfer.

Kompromis: rozdział jest dłuższy, a realizacja działania,
identyfikacja danych normalnych i dokładność pozostają
jawnie cytowanymi twierdzeniami zewnętrznymi. Nie zmieniono
rachunków rozdziału 27 ani klasyfikacji rozdziału 30.

### Weryfikacja

Zmieniony fragment porównano z §10 Walla i z rozdziałem 30.
Sprawdzono hipotezy wymiarowe, charakter orientacji, warunek
brzegowy, rozróżnienie grupy i zbioru struktur oraz to,
że prawa strzałka $\theta_n$ nie musi być homomorfizmem.
Po ostatniej korekcie `buduj_tomy.ps1` zbudował cztery tomy w dwóch
przebiegach (216, 182, 99 i 80 stron). Indeksy przyjęły odpowiednio
113, 96, 28 i 93 hasła bez odrzuceń. Sprawdzenie logów nie wykazało
niezdefiniowanych odsyłaczy, przepełnionych wierszy ani brakujących
znaków. Wszystkie strony tytułowe mają po trzy łącza do pozostałych
PDF-ów, a sumy SHA-256 kopii w katalogu projektu i `build/tomy`
są zgodne. Obejrzano strony PDF 75--79 tomu III; diagramy i ciąg
względny są czytelne, bez ucięć i kolizji etykiet.

## 2026-10-27 — podział tomu III na III i IV

### Problem

Dotychczasowy tom III łączył chirurgię w wysokich wymiarach
z potokiem Ricciego, wymiarem cztery i dodatkami. Utrudniało to
rozwijanie chirurgii oraz przykładów czterowymiarowych jako
samodzielnych ciągów dydaktycznych.

### Rozwiązanie i wpływ

Po rozdziale 30, na naturalnej granicy części książki,
`geometria_tom3.tex` kończy się własnym indeksem. Nowy
`geometria_tom4.tex` obejmuje rozdziały 31--38, dodatki A--C
i własny indeks. Numery rozdziałów, kolejność części i etykiety
pozostają takie jak w dokumencie zbiorczym. Tomy I--IV importują
pliki `.aux` trzech pozostałych tomów, a odsyłacze wskazują PDF-y
o właściwych nazwach. Zmieniono mapę na stronach tytułowych,
`buduj_tomy.ps1`, `README.md` i projektowe `AGENTS.md`.
`PLAN_DZIALANIA.md` ma osobne priorytety uzupełnień dla III i IV;
`PRZEGLAD.md` rejestruje decyzję i kontrolę.

Kompromis: cztery osobne PDF-y i indeksy wymagają pełnego składu
czterech tomów do ustabilizowania odsyłaczy. Tom III zaczyna się
w środku części III książki, podobnie jak przed podziałem;
nowy tom IV rozpoczyna całą część IV. Nie przenoszono ani nie
przepisywano treści rozdziałów z powodu samego podziału.

### Weryfikacja

Skontrolowano statycznie po trzy importy `.aux` w każdym tomie,
liczbę rozdziałów 10/12/8/8, liczniki `chapter` i `part`, składnię
PowerShell skryptu oraz `git diff --check`.
`buduj_tomy.ps1` zakończył dwa przebiegi: tomy I--IV mają
216, 182, 97 i 80 stron; indeksy przyjęły 113, 96, 26 i 93
hasła bez odrzuceń. Logi nie wykazują błędów ani brakujących
odsyłaczy, cztery kopie PDF są identyczne z plikami w `build/tomy`,
a strony tytułowe zawierają łącza do pozostałych trzech tomów.
Wybrane strony i indeksy III/IV obejrzano; szczegóły poleceń są
w `manual.md`, a zakres kontroli w `PRZEGLAD.md`.

## 2026-10-27 — audyt i ujednolicenie skryptu teorii modeli

### Problem

Samodzielny skrypt miał inny krój pisma, marginesy, odstępy,
kolory odsyłaczy i żywą paginę niż tomy geometrii. Komentarz do
aksjomatu Q8 mógł sugerować przemienność dodawania w słabej
arytmetyce $Q$. W lemacie o skończonych odcinkach zapis
$\overline{n-1}$ nie miał sensu dla $n=0$, mimo późniejszej umowy
o pustej alternatywie.

### Rozwiązanie i wpływ

W `teoria modeli/teoria modeli.tex` przyjęto Latin Modern, margines
2,5 cm, odstęp 4 pt między akapitami bez wcięcia, ciemnoniebieskie
odsyłacze, żywą paginę i odstępy list zgodne z geometrią.
Komentarz do Q8 zachowuje dokładną kolejność $z+S(x)=y$.
Lemat zapisuje skończoną alternatywę jako
$\bigvee_{j<n}(x=\overline j)$, więc przypadek $n=0$ jest
określony jako alternatywa pusta. Tytuł, numeracja, etykiety i
struktura `article` pozostały; zapisano nowy PDF.

Kompromis: zmiana składu zwiększyła objętość z 34 do 36 stron.
Skrypt zachowuje własną, małą preambułę, zamiast zależeć od
preambuły wielotomowej geometrii. D1--D3, twierdzenia o zupełności
oraz formalizacja arytmetyki są wykładane w dotychczasowym zakresie.

### Weryfikacja

Przejrzano dowody Gödla I i II, Rossera, Tarskiego, Löba,
zwartości oraz Löwenheima--Skolema i porównano ich hipotezy
ze źródłami akademickimi. Nie znaleziono luki wymagającej
przebudowy tych dowodów. Dwa przebiegi `pdflatex` zakończyły się
bez błędów i ostrzeżeń; PDF A4 ma 36 stron. Obejrzano strony 1,
8 i 20, a `git diff --check` przeszedł.

## 2026-10-27 — audyt i ujednolicenie skryptu Banacha--Tarskiego

### Problem

Skrypt miał inny krój nagłówków, marginesy, odstępy akapitów,
kolor odsyłaczy i styl środowiska „Uwaga” niż tomy geometrii.
Makro równorozkładu zapisywało $\sim_G$, choć później tekst używał
$\equiv$ bez indeksu. Schemat końcowy sugerował bezpośrednie
odwzorowanie sfery na kulę pozbawioną środka zamiast przedłużenia
rozkładu na promienie.

### Rozwiązanie i wpływ

W `banach_tarski/banach_tarski_przepisany.tex` ustawiono Latin Modern,
margines 2,5 cm, brak wcięć i odstęp 4 pt, ciemnoniebieskie łącza,
żywą paginę oraz style twierdzeń zgodne z geometrią. Poprawiono makro
na $\equiv_G$, schemat kroku stożkowego i mylący zwrot o
„nieskończonym algorytmie”. Dodano elementarny przykład
równorozkładu, doprecyzowano opis kawałka z wielu poziomów,
usunięto nieużywane makra oraz podlinkowano pracę Banacha--Tarskiego
i katalog książki Wagona. Numeracja twierdzeń i etykiety zostały
zachowane; w repozytorium zapisano nowy PDF.

Kompromis: nowy skład ma 19 zamiast 18 stron, a projekt nadal jest
samodzielnym artykułem, bez przejęcia całej preambuły wielotomowej
książki. Aksjomat wyboru pozostaje jawnie wskazanym wejściem dowodu.

### Weryfikacja

Przejrzano cały dowód od paradoksalnego rozkładu $F_2$ po podwojenie
kuli i porównano źródła. Dodatkowy rachunek komputerowy potwierdził
tabelę modulo 3, rozkłady macierzy rzędu jeden oraz niezerowość
iloczynów dla 13\,120 słów zredukowanych długości co najwyżej osiem;
nie zastępuje on ogólnego dowodu w tekście. PDF ma 19 stron,
log składu nie wykazuje ostrzeżeń ani przepełnionych wierszy;
obejrzano strony 1, 2, 11, 18 i 19. `git diff --check` przeszedł.

## 2026-10-27 — pełny audyt rozdziału 38

### Problem

W ostatnim rozdziale numerowanym przejście od lokalnie płaskich dysków
do otoczeń $D^2\times D^2$ korzystało z głębokiego twierdzenia bez
wskazania źródła. Rozpoznanie kraty $-E_8$ pomijało konstrukcję bazy
i mogło sugerować nieprzywołaną klasyfikację kratek określonych.
Przy sklejeniu w lemacie 1.2 Gompfa nie były jawne orientacje dwóch
końców kołnierza.

### Rozwiązanie i wpływ

W `tex/rozdzialy/35-egzotyczne-r4.tex` wskazano twierdzenia 9.6--9.7
Freedmana--Quinna o topologicznym otoczeniu normalnym, także
względnie przy brzegu, oraz trywializację nad dyskiem. Podano
osiem konkretnych wektorów
generujących $-E_8$, ich iloczyny oraz argument z wyznacznika
i indeksu. Uzupełniono konwencję orientacji i produktowe pierścienie
w lemacie Gompfa. Dzięki temu każdy z trzech kroków ma jawne
uzasadnienie lub precyzyjnie nazwane wejście zewnętrzne.

Kompromis: twierdzenie o otoczeniu normalnym, konstrukcja uchwytów
Cassona, przeszkody Gompfa i klasyfikacja rodzin egzotycznych
$\R^4$ przez De Michelisa--Freedmana pozostają wynikami zewnętrznymi.
Nie zmieniono konstrukcji ani zakresu wniosku rozdziału.

### Weryfikacja

Sprawdzono hipotezy twierdzeń w źródłach Freedmana--Quinna,
Freedmana, Gompfa i De Michelisa--Freedmana, rachunek formy
przecięcia, orientacje brzegów oraz odsyłacze do rozdziału 36.
Końcowy skład tomu IV przeszedł bez błędów i niezdefiniowanych
odsyłaczy; w PDF odczytano nowe sformułowanie twierdzeń 9.6--9.7,
bazę $-E_8$ i obejrzano rysunek indukcji na stronie fizycznej 56.
Szczegółowy zakres kontroli zapisano w `PRZEGLAD.md`.

## 2026-10-27 — pełny audyt rozdziałów 36 i 37

### Problem

Rozdział 36 przypisywał pełną klasyfikację topologiczną bez dostatecznego
rozróżnienia pierwotnego twierdzenia Freedmana dla rozmaitości gładkich
poza punktem i wersji Freedmana--Quinna w kategorii TOP. Warunek na
niezmiennik Kirby'ego--Siebenmanna, zakres twierdzenia o zanurzaniu sfer
oraz wpływ chirurgii na grupę podstawową wymagały jawniejszych przejść.
W rozdziale 37 zmiana trywializacji była zapisana globalnie, choć wiązka
może być nietrywialna; znikanie formy reprezentującej $c_1$ nie dowodziło
znikania całkowitej klasy. Krótki opis metody Donaldsona pomijał różnicę
konwencji samodualnej i antysamodualnej oraz dostępny rachunek algebraiczny.

### Rozwiązanie i wpływ

- W `tex/rozdzialy/33-freedman-klasyfikacja.tex` wskazano osobno zakres
  twierdzenia Freedmana z 1982 roku i pełnej klasyfikacji TOP z §10.1
  Freedmana--Quinna. Dodano spinową relację
  $\operatorname{ks}\equiv\sigma/8\pmod2$ i wyjaśniono, że jej
  konieczność nie zastępuje twierdzenia o istnieniu.
- Doprecyzowano hipotezy oraz wniosek o homotopii regularnej w twierdzeniu
  o zanurzaniu sfer. Rachunek van Kampena dla chirurgii na obramowanej
  sferze z dualną sferą pokazuje zachowanie $\pi_1$. W opisie
  topologicznego $s$-kobordyzmu dodano warunek dobrej grupy, a w dowodzie
  wniosku Poincarégo jawnie wybrano orientację.
- W `tex/rozdzialy/34-donaldson.tex` zapisano zmianę trywializacji nad
  $U\subset X$, wskazano trywialną wiązkę w przykładzie połączenia
  płaskiego i uzasadniono całkowite $c_1(E)=0$ przez $\det E$.
- Wyjaśniono zmianę orientacji między samodualną konwencją oryginału
  Donaldsona a używaną tu konwencją ASD. Dla punktów redukowalnych
  rozpisano równanie $1=-c_1(L)^2[X]$ i algebraiczne przejście od
  $n(Q_X)=b_2(X)$ do bazy diagonalnej. Tytuł wniosku o $E_8$
  zawężono do jednospójności; niedostępny adres szkicu Donaldsona
  zastąpiono DOI.
- `PLAN_DZIALANIA.md` odnotowuje zakończenie rozdziałów 36--38
  i dalsze priorytety; `PRZEGLAD.md` opisuje zakres audytów.
  Podział tomów zapisano jako osobny etap powyżej.

Kompromis: klasyfikacja Freedmana, topologiczne zanurzanie sfer,
$s$-kobordyzm oraz analityczna konstrukcja i orientowalność przestrzeni
moduli Donaldsona są nadal jawnie oznaczonymi wynikami zewnętrznymi.
Dopisany rachunek algebraiczny nie jest przedstawiany jako pełny dowód
diagonalizacji.

### Weryfikacja

Sformułowania porównano z pracą Freedmana z 1982 roku, książką
Freedmana--Quinna, twierdzeniem Powella--Raya--Teichnera oraz pracą
i szkicem Donaldsona z 1983 roku. Skontrolowano znaki $c_2$ i energii,
przykłady $H$, $[1]$, $E_8$, $2E_8$, hipotezy i odsyłacze; szczegóły
są w `PRZEGLAD.md`. Końcowy tom IV złożono bez błędów i brakujących
odsyłaczy; obejrzano wybrane strony fizyczne 44--50 rozdziałów 36
i 37 oraz ich powiązanie z następnym rozdziałem.

## 2026-10-26 — pełny audyt rozdziału 35

### Problem

Rozdział poprawnie przedstawiał ideę wież Cassona, lecz kilka miejsc
zacierało granicę między rachunkiem skończonych pięter a głębokim
twierdzeniem o zanurzaniu dysku. Dowód typu homotopijnego uchwytu
z załamaniami sugerował istnienie relacji od rdzenia uchwytu 2, chociaż
w diagramie absolutnej rozmaitości widoczne są tylko uchwyty 1. Tekst nie
rozróżniał niezredukowanej liczby samoprzecięcia $\mu$ od
$\widetilde\mu$, więc nie wyjaśniał różnicy między homotopią regularną
a dowolną. W cytacie Freedmana--Quinna brakowało drukowanej numeracji
wyników, a konkluzja o geometrycznie dualnych sferach nie zapisywała
jawnie zachowania ich klas homotopii. Sformułowanie o grupach wzrostu
podwykładniczego mogło też sugerować błędną relację zawierania z klasą
grup wielostopniowo skończonych lub cyklicznych.

### Rozwiązanie i wpływ

- W `tex/rozdzialy/32-uchwyty-cassona.tex` zapisano bezpośredni rachunek
  Kirby'ego: uchwyt z $k$ załamaniami, po zapomnieniu obszaru
  przyczepienia, jest brzegową sumą spójną $k$ kopii $S^1\times D^3$.
  Krzywa bez kropki oznacza okrąg przyczepienia, a nie dodatkowy uchwyt 2,
  więc nie daje relacji między wolnymi generatorami.
- Zdefiniowano osobno $\mu$ w ilorazie przez $g-g^{-1}$ oraz
  $\widetilde\mu$ po dodatkowym podzieleniu przez $\mathbb Z\cdot1$.
  Wyjaśniono, dlaczego pierwsza wielkość odpowiada homotopii regularnej,
  a druga zwykłej klasie homotopii.
- Zaznaczono, że klasyczny uchwyt Cassona sam wystarcza w konstrukcji
  jednospójnej. Dla nietrywialnej grupy podstawowej argument
  Freedmana--Quinna używa również powierzchni z dyskami zamykającymi,
  uogólnionych wież i kontroli pętli punktów podwójnych.
- Definicję grupy poly-(finite or cyclic) doprecyzowano do ilorazów
  skończonych albo nieskończenie cyklicznych. Grupy podwykładniczego
  wzrostu opisano jako inny znany zakres wyniku, bez twierdzenia, że są
  szerszą klasą zawierającą wszystkie poprzednie grupy.
- W twierdzeniu o zanurzaniu zapisano, że geometrycznie dualne sfery
  $B'_j$ są homotopijne do zadanych $B_j$. Dodano dokładne numery
  Freedmana--Quinna w wydaniu przeformatowanym i drukowanym oraz wskazano
  wersję Powell--Raya--Teichnera używającą $\widetilde\mu$ i dobrych grup.
- Uzasadnienie $\pi_1$-pomijalności dopełnienia powiązano z Uwagą 1.2
  Powell--Raya--Teichnera. We wniosku z homotopią regularną wyjaśniono,
  że warunek $\mu(A_i)=0$ dotyczy liczby niezredukowanej.
- `PRZEGLAD.md` rejestruje zakres audytu i wyniki kontroli, a
  `PLAN_DZIALANIA.md` oznacza rozdział 35 jako ukończony i ustawia
  rozdział 36 jako następny etap. Zaktualizowano wszystkie trzy PDF-y,
  ponieważ pełny skrypt stabilizuje odsyłacze między tomami.

Kompromisem jest pozostawienie konstrukcji powierzchni z dyskami
zamykającymi, uogólnionych wież, argumentu zbieżności i standardowości
topologicznej uchwytu Cassona jako nazwanych wyników zewnętrznych. Tekst
nie sugeruje dzięki temu pełnego dowodu tam, gdzie podaje tylko jego
geometryczne przygotowanie i precyzyjną konkluzję.

### Weryfikacja

Treść porównano z pracą Freedmana z 1982 roku, przeformatowanym wydaniem
Freedmana--Quinna, publikacją Powell--Raya--Teichnera z 2025 roku oraz
korektą Krushkala--Quinna dotyczącą grup podwykładniczego wzrostu.
Sprawdzono rachunek $\pi_1$ pięter, role $\mu$ i $\widetilde\mu$, numery
i hipotezy twierdzeń, klasy homotopii sfer dualnych oraz dowód kontroli
grupy podstawowej dopełnienia.

Pełny `buduj_tomy.ps1` zakończył dwa przebiegi: tomy mają 216, 182 i 173
strony, a indeksy przyjęły 113, 96 i 119 haseł bez odrzuceń i ostrzeżeń.
Logi nie zawierają błędów, niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Obejrzano wszystkie siedem stron rozdziału 35
w finalnym PDF-ie tomu III; tekst, wzory, rysunek i odsyłacze są czytelne.
Znane ostrzeżenia `Underfull`, zduplikowany cel `page.1` i dwa komunikaty
tomu I o zmianie specyfikatora rysunku nie dotyczą zmienionego rozdziału.

## 2026-10-25 — pełny audyt rozdziału 34

### Problem

Rozdział o formach przecięcia zawierał poprawny pełny rachunek $E_8$,
macierz obramowanego splotu i wyjaśnienie przeszkody dla triku Whitneya,
ale zaplanowany przypadek $2E_8$ był jedynie wymieniony. Nie było jawnego
rachunku jego rzędu, wyznacznika i sygnatury ani wyraźnego rozróżnienia
sumy ortogonalnej $E_8\oplus E_8$ od skalarnej macierzy $2\cdot E_8$.
Opis macierzy splotu nie objaśniał także, dlaczego pomocniczy wybór
orientacji komponentów nie zmienia klasy izometrii formy.

### Rozwiązanie i wpływ

- W `tex/rozdzialy/31-freedman-formy-przeciecia.tex` dodano przykład
  $2E_8=E_8\oplus E_8$. Z blokowej postaci wyprowadzono wyznacznik $1$,
  sygnaturę $16$, parzystość, unimodularność i dodatnią określoność.
- Parzystość odróżnia $2E_8$ od dodatnio określonej formy diagonalnej
  $I_{16}$, mimo zgodności rzędu i sygnatury.
- Dwie rozłączne kopie splotu realizują blokową macierz $2E_8$, ale tekst
  wyraźnie nie utożsamia tego gładkiego korpusu z brzegiem z zamkniętą
  rozmaitością. Topologiczne istnienie nadal jest jawnym wejściem
  Freedmana, a przeszkoda gładka pozostaje w rozdziale o Donaldsonie.
- Dopisano wpływ odwrócenia orientacji komponentu splotu. Zmiana znaków
  odpowiedniego wiersza i kolumny jest kongruencją przez diagonalną
  macierz z jednym wpisem $-1$, więc nie zmienia klasy izometrii.
- `PLAN_DZIALANIA.md` oznacza wyłącznie rozdział 34 jako ukończony i
  pozostawia rozdział 35 jako następny etap. `PRZEGLAD.md` zapisuje zakres
  audytu i wyniki kontroli; rozdziałów 35--38 w tej iteracji nie audytowano.
- Zaktualizowano trzy PDF-y tomów, ponieważ pełny skrypt stabilizuje
  odsyłacze między nimi. Tom III wydłużył się ze 171 do 172 stron.

Kompromisem jest pozostawienie głębokiego topologicznego wypełnienia
brzegu i klasyfikacji Freedmana jako wyników zewnętrznych. Jest to zgodne
z rzeczywistym zakresem rozdziału 34 i nie sugeruje dowodu, którego tekst
nie zawiera.

### Weryfikacja

Niezależna kontrola wyłącznie rozdziału 34 potwierdziła rachunki $E_8$,
$2E_8$, macierzy splotu, homologii brzegu i wymiarów w argumencie Whitneya.
Pełny `buduj_tomy.ps1` zakończył dwa przebiegi: tomy mają 216, 182 i 172
strony, a indeksy przyjęły 113, 96 i 119 haseł bez odrzuceń i ostrzeżeń.
Logi nie zawierają błędów, niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Obejrzano wszystkie strony rozdziału 34 w finalnym
PDF-ie tomu III; nowy przykład, akapit o orientacjach, wzory i rysunki są
czytelne. Kontrola XML potwierdziła poprawne cele odsyłaczy, w tym do
wyników używanych później, bez audytowania treści późniejszych rozdziałów.

## 2026-10-25 — audyt dodatków A i B

### Problem

Dodatek A nie odzwierciedlał w pełni wyników zewnętrznych faktycznie
używanych w rozdziałach. Najistotniejsza niezgodność podawała zakres
twierdzenia Walla jako wymiar co najmniej sześć, chociaż wersja
nieparzysta obejmuje również wymiar pięć. Katalog pomijał także między
innymi dekorację `h`, ciąg Rothenberga, część teorii torsji Whiteheada,
globalną geometrię rozdziału 14, normalizację Cherna--Weila oraz główne
wejścia do klasyfikacji Bardena i sfer wymiaru siedem.

Dodatek B miał poprawne rachunki, lecz trzy miejsca wymagały domknięcia:
użyty homeomorfizm nie był nazwany, skończony model CW kobordyzmu nie
wynikał jawnie z tekstu, a planowany związek cechy Eulera z dualnością
Poincarégo nie został podany.

### Rozwiązanie i wpływ

- W `tex/dodatki/a-zaleznosci-zewnetrzne.tex` poprawiono zakres Walla
  do `n >= 5`, rozdzielono kryterium przeszkody od twierdzeń
  realizacyjnych i opisano wersję z brzegiem, dekorację `h`, ciąg
  Rothenberga oraz ciąg dokładny chirurgii.
- Poprawiono niedziałający DOI pracy Whiteheada o triangulacji gładkiej,
  zapisano współczynniki grup `L` w ciągu chirurgii, doprecyzowano
  kofinalność dobrych pokryć i jednoznaczność rozkładu de Rhama oraz
  uzupełniono odsyłacz do stabilnego wygładzania u Freedmana--Quinna.
- Ten sam katalog uzupełniono o miarę Hausdorffa, dokładniejsze hipotezy
  triku Whitneya, torsję Whiteheada, Ambrose'a--Singera, globalny
  rozkład de Rhama, miarę Haara, zgodność Cherna--Weila z klasami
  topologicznymi, pełniejsze wejścia Bardena, Eellsa--Kuipera,
  Kervaire'a--Milnora i Quinna. Doprecyzowano też zależności w wymiarach
  trzy i cztery.
- W `tex/dodatki/b-homologia-singularna-euler.tex` nazwano homeomorfizm
  `h`, wyprowadzono skończony typ CW przestrzeni `W` z względnego
  rozkładu uchwytowego oraz dodano konsekwencję dualności Poincarégo:
  zamknięta zorientowana rozmaitość nieparzystego wymiaru ma cechę
  Eulera równą zero.
- `PLAN_DZIALANIA.md` zaktualizowano po zakończeniu obu audytów;
  pozostaje on jedynym miejscem bieżącego zakresu i kolejki.
- `PRZEGLAD.md` rejestruje ustalenia matematyczne, źródła, zakres
  poprawek i wyniki weryfikacji. `README.md` wskazuje niniejszy plik
  i `manual.md` jako dokumentację ogólnorepozytoryjną.
- `manual.md` rozdziela wykonane polecenia od instrukcji dla czystego
  stanowiska i podaje instalację Git, MiKTeX, pakietów TeX oraz `ripgrep`,
  katalog roboczy, wersje sprawdzone i używane polecenia kontroli PDF.
- Trzy pliki `geometria_tom1.pdf`, `geometria_tom2.pdf` i
  `geometria_tom3.pdf` wygenerowano ponownie, aby utrwalić zgodne
  odsyłacze między tomami; wydłużył się tylko tom III, z 168 do
  171 stron.

Zmiana nie próbuje zastępować głębokich twierdzeń własnymi szkicami.
Kompromisem jest dłuższy dodatek A, ale w zamian granica
samowystarczalności skryptu i dokładne hipotezy są jawne w jednym
miejscu.

### Weryfikacja

Uruchomiono pełny `buduj_tomy.ps1`. Dwa przebiegi ustabilizowały pliki
pomocnicze. Tomy mają 216, 182 i 171 stron, a indeksy przyjęły 113, 96
i 119 haseł bez odrzuceń. Nie ma niezdefiniowanych odsyłaczy,
`Overfull`, brakujących znaków ani błędów TeX-a. Obejrzano wszystkie
zmienione strony dodatków A i B. Na finalnym PDF-ie ponownie wyodrębniono
tekst i XML, po czym sprawdzono odsyłacze do tomów I i II. Znane
ostrzeżenia `Underfull`, zduplikowany cel `page.1` oraz dwa ostrzeżenia
tomu I o zmianie specyfikatora rysunku z `h` na `ht` były obecne przed
tym etapem i nie dotyczą zmienionych stron.
