# Przegląd matematyczny skryptu

Gałąź: `review/rozdzialy-matematyka`. Zwykła iteracja obejmuje jeden rozdział;
autor może wyznaczyć szerszy etap.
Źródło zbiorcze: `geometria_i_topologia_rozniczkowa.tex`; podstawowy skład: cztery tomy `geometria_tom1.tex`--`geometria_tom4.tex`.
Rejestr zawiera także uzasadnienia, aby można było niezależnie sprawdzić poprawki.
Aktualny zakres, kolejka i propozycje są wyłącznie w [planie](PLAN_DZIALANIA.md).
Poniższe wpisy są chronologiczne: numery rozdziałów, strony i statusy dotyczą
wersji wskazanej w danym wpisie. Audyt 18 rozdziałów nie obejmuje późniejszych
dodatków autora. Od 5 października źródła są w `tex/rozdzialy/`;
pliki główne tylko ustalają ich kolejność.

Decyzją autora głębokie wyniki Walla pozostają jawnie cytowanymi
wejściami zewnętrznymi; audyt wyprowadzonego tekstu wykonano
bez samodzielnego dowodzenia tych lematów.

## Rozdział 37 — instanton BPST i wejścia do twierdzenia Donaldsona (2026-10-28)

Dotychczasowy lokalny przykład połączenia antysamodualnego miał
nieskończoną energię na $\R^4$. Dodano więc przykład instantonu BPST
na $S^4$ w orientacji i normalizacji rozdziału. Na karcie
$S^4\setminus\{\infty\}\cong\R^4$ jego forma to
$A_\lambda=\operatorname{Im}(\bar q\,\mathrm{d}q)/(|q|^2+\lambda^2)$.
Obliczenie krzywizny rozkłada ją na trzy antysamodualne $2$-formy,
a całka radialna daje $\int_{S^4}|F|^2=8\pi^2$. Druga trywializacja,
po zmianie cechowania i odwróceniu współrzędnych, ma formę gładką
przy punkcie $\infty$. To pokazuje, że lokalny wzór określa połączenie
na wiązce nad całą sferą; wcześniej ustalona tożsamość energii daje
$c_2(E)[S^4]=1$. Wariant rozwiązania pochodzi od
[Belavina, Polyakova, Schwartza i Tyupkina (1975)](https://strings.itp.ac.ru/Papers/belavin1975.pdf).

Przed twierdzeniem o diagonalizacji dodano operator deformacji
$D_A=d_A^*\oplus d_A^+$ w przekroju cechowania i wzór na jego indeks.
Dla jednospójnej rozmaitości o ujemnie określonej formie przecięcia
i $c_2=1$ wymiar oczekiwany wynosi $5$; gładkość części
nieredukowalnej wymaga osobnej regularności i perturbacji. Tabela
wyodrębnia punkty redukowalne z linkiem $\mathbb{C}P^2$,
koncentrację energii, kompaktifikację Uhlenbeck oraz kołnierz
$X\times(0,\varepsilon)$ pochodzący z konstrukcji Taubesa i analizy
Donaldsona. Samo twierdzenie Uhlenbeck o oszacowaniach $L^p$ daje
słabą zwartość dla $p>2$; ograniczenie krytycznej energii $L^2$
dopuszcza bąble. Indeks i regularność porównano z
[Atiyahem, Hitchinem i Singerem](https://doi.org/10.1098/rspa.1978.0143)
oraz [Donaldsonem](https://doi.org/10.1090/S0273-0979-1983-15090-5),
zwartość i przedłużanie z pracami
[Uhlenbeck o oszacowaniach $L^p$](https://doi.org/10.1007/BF01947069)
i [usuwaniu osobliwości](https://doi.org/10.1007/BF01947068),
a opis końca z [Taubesem](https://doi.org/10.4310/jdg/1214436701)
i Donaldsonem. Te wejścia analityczne oraz diagonalizacja pozostają
wynikami zewnętrznymi.

Poprawiono także dawny skrót w rachunku sygnatury: dopuszczalne
orientacje linków punktów redukowalnych dają najpierw
$n(Q_X)\geq b_2(X)$. Odwrotna nierówność wynika z algebraicznej
ortogonalności różnych par klas o kwadracie $-1$; razem dają
równość potrzebną do diagonalizacji. Jest to korekta zakresu
wcześniejszego wniosku, bez nowego dowodu analitycznej części
twierdzenia.

Podgląd tomu IV złożono poprawnie i obejrzano fizyczne strony 50–52:
przykład BPST i tabela mieszczą się w łamie oraz są czytelne.
Pełny `buduj_tomy.ps1` zakończył się kodem 0 po dwóch przebiegach.
Tomy I–IV mają 216, 182, 102 i 82 strony; indeksy przyjęły
113, 96, 30 i 94 wpisy bez odrzuceń. Kontrola logów nie wykazała
nieustalonych odsyłaczy, przepełnionych wierszy ani brakujących
znaków. Na stronie tytułowej każdego tomu są trzy łącza do
pozostałych tomów, a PDF w katalogu głównym i kopia w `build/tomy`
mają zgodną sumę SHA-256. `git diff --check` nie zgłosił uwag.

## Rozdziały 34 i 36 — sploty obramowane i droga do klasyfikacji TOP (2026-10-28)

W rozdziale 34 dodano rzut dwóch prostych diagramów uchwytów $2$.
Splot Hopfa ma oba obramowania równe zero, a przy zaznaczonych
orientacjach dwa dodatnie skrzyżowania dają
$\operatorname{lk}(K_1,K_2)=1$; jego macierz sprzężeń jest więc
$H=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$.
Niewęzeł z obramowaniem $+1$ daje formę $[1]$. Białe przerwy
w rysunku oznaczają przejścia pod spodem. Wcześniejszy graf $E_8$
pozostaje grafem macierzy, więc nie powielano go rzutem
ośmioskładnikowego splotu.

W rozdziale 36 zebrano drogę od immersyjnych dysków i sfer
algebraicznie dualnych, przez wieże Cassona i ich uogólnienia,
do lokalnie płaskich dysków i sfer mających geometrycznie dualne sfery.
Dalsze pola schematu pokazują chirurgię TOP z kontrolą $\pi_1$,
topologiczny $s$-kobordyzm w wymiarze pięć i klasyfikację przez
formę przecięcia oraz niezmiennik Kirby'ego--Siebenmanna.
Sfery algebraicznie dualne są założeniem twierdzenia o zanurzaniu,
a geometrycznie dualne należą do jego konkluzji. Strzałki są
mapą zależności, nie dowodem ani bezwarunkowym algorytmem:
przejście przez uogólnione wieże, twierdzenie o zanurzaniu dysków,
twierdzenie o sferach dualnych, chirurgia i $s$-kobordyzm
pozostają wynikami zewnętrznymi przy odpowiednich hipotezach.
Ich zakres i źródła podano w tekście, w szczególności u
[Freedmana i Quinna, *Topology of 4-Manifolds*](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf);
konkluzję o geometrycznie dualnych sferach uzasadnia
[Powell--Ray--Teichner, *The 4-dimensional disc embedding theorem and dual spheres*](https://arxiv.org/pdf/2006.05209).
Realizacja form i rachunek niezmiennika Kirby'ego--Siebenmanna
są dodatkowymi wejściami do klasyfikacji.

Tabela w rozdziale 36 zestawia $H$, dwa dopuszczalne typy
o formie $[1]$, $E_8$ i $2E_8$: parzystość, sygnaturę,
niezmiennik Kirby'ego--Siebenmanna oraz istnienie typu TOP
i struktury DIFF. Dla $2E_8$ wpis $\operatorname{ks}=0$
nie oznacza wygładzalności; wyklucza ją twierdzenie Donaldsona.
Kolumna DIFF mówi wyłącznie o istnieniu wygładzenia, nie o jego
jednoznaczności. Tabela syntetyzuje wcześniejsze rachunki i
twierdzenia, bez ich powtarzania. Diagramy wykonano w dotychczasowej
niebieskiej stylistyce TikZ; ograniczono je do zależności potrzebnych
czytelnikowi, zamiast ilustrować całą konstrukcję Freedmana.

Doraźny skład tomu IV zakończył się poprawnie: PDF ma 81 stron.
Obejrzano fizyczne strony 35, 46 i 47 z nowymi elementami;
rysunki i tabela mieszczą się w łamie i są czytelne. Po
powiększeniu tabeli ponownie obejrzano stronę 47 końcowego PDF.
Pełny `buduj_tomy.ps1` zakończył się kodem 0 po dwóch przebiegach.
Tomy I--IV mają 216, 182, 102 i 81 stron; indeksy przyjęły
113, 96, 30 i 93 wpisy bez odrzuceń. W logach nie znaleziono
nieustalonych odsyłaczy, przepełnionych wierszy ani brakujących
znaków. Każdy tom ma trzy łącza do pozostałych na stronie
tytułowej, a kopia PDF w `build/tomy` ma tę samą sumę SHA-256.

## Rozdział 26 — wizualne przykłady uchwytów (2026-10-28)

Na prośbę autora uzupełniono sekwencję przykładów chirurgii powierzchni.
Rysunek jednej sfery przechodzącej w torus był już w rozdziale 23,
a lokalna wymiana dwóch dysków na pierścień na początku rozdziału 26.
Nowy przykład i oryginalny schemat w rozdziale 26 pokazują brakującą
sekwencję brzegów: $S^2\sqcup S^2\to S^2\to T^2$.
Pierwszy uchwyt łączy dwie składowe, drugi tworzy otwór na
już połączonej powierzchni. Złote pola wskazują dyski wycinane
w każdym kroku; podpisy pod trzema bryłami podają topologię ich
brzegów, $b_0$ i $\chi$. Tekst rozdziela trójwymiarowy
uchwyt $D^1\times D^2$ śladu od pierścienia $D^1\times S^1$
wklejanego do brzegu. Sklejenie zachowujące orientowalność
jest warunkiem wyniku $T^2$; druga możliwość daje butelkę Kleina.
Każdy krok obniża $\chi$ o dwa, zatem wartości wynoszą $4,2,0$.

Nazwę modyfikacji sferycznej, dwa typy sklejenia i przypadek
łączenia składowych porównano z
[A. H. Wallace'em, *Modifications and Cobounding Manifolds*,
§§1 i 3](https://doi.org/10.4153/CJM-1960-045-7).
Wallace zapisuje typ tej operacji jako $(0,1)$, podając wymiar
nowej sfery; rozdział używa wcześniej zdefiniowanej konwencji
$(p,q)=(0,2)$, gdzie $q$ jest wymiarem dysku normalnego.
Ilustracja jest nowym schematem, bez kopiowania rysunku źródłowego.
W pierwszym podglądzie wcześniejszy rysunek lokalnej wymiany
dysków wypłynął między części nowego przykładu. Zmieniono jego
specyfikator na `[H]`, używając obecnego już w preambule pakietu
`float`. W ponownie złożonym tomie III na fizycznych stronach
37–39 lokalny model stoi przed pełnym nowym przykładem,
a powiększony Rysunek 26.2 mieści się w łamie. Złote dyski,
obie rurki, strzałki, podpisy i prześwit ostatniej bryły
są czytelne; nie ma kolizji ani ucięć.

Na dalszą prośbę autora dodano osobny przykład sfery z dwoma
rozłącznymi uchwytami, których pobocznice przecinamy wzdłuż
meridianów, przeplatamy i sklejamy z zachowaniem pierwotnych
par końców. Odpowiedź autora określiła właśnie te pary, więc
rysunek pokazuje czysty warkocz $\sigma_1^2$ z dwoma
skrzyżowaniami rzutu i naprzemienną głębokością rur.
Trzy stany ilustracji pokazują sferę z uchwytami, cztery
otwarte obrzeża oraz ponownie sklejoną powierzchnię.
Pozostała po cięciu sfera z czterema otworami ma $\chi=-2$,
a dwie wklejane pobocznice mają $\chi=0$; wynik jest nadal
orientowalną powierzchnią rodzaju dwa. Zaznaczony przebieg
rdzeni nie dowodzi sam przez się zmiany klasy izotopii
nieoznaczonej powierzchni. Przykład niezawęźlonego ciała
uchwytowego z przeplecionymi rdzeniami porównano z
[Benedettim, Frigeriem i Ghiloniem, *The topology of Helmholtz
domains*, przykładem 6.16](https://people.dm.unipi.it/benedett/Expositiones_online.pdf).
Ilustrację wykonano od podstaw w TikZ, z cieniowaną sferą,
walcowymi rurkami i białymi maskami pod przejściami.
Po pierwszym podglądzie przypięto ją do przykładu przez `[H]`,
bo swobodny rysunek wypadł dopiero za dwiema późniejszymi
uwagami. W końcowym PDF tomu III przykład jest na fizycznej
stronie 39, a rysunek 26.4 zaczyna stronę 40 bezpośrednio
po nim; obie strony obejrzano. Cztery obrzeża, dwa przejścia
nad/pod, etykiety i podpis są czytelne, bez ucięć lub kolizji.
Pełny skład czterech tomów zakończył się kodem 0 po dwóch
przebiegach. PDF-y mają 216, 182, 102 i 80 stron, a indeksy
przyjęły 113, 96, 30 i 93 wpisy bez odrzuceń. W logach brak
nieustalonych odsyłaczy, przepełnionych wierszy i brakujących
znaków; każdy tom ma trzy łącza do pozostałych i zgodną sumę
SHA-256 z kopią w `build/tomy`.

## Rozdział 28 — mapa hipotez chirurgii (2026-10-28)

Po ukończeniu konstrukcyjnego opisu ciągu i przykładu przez rozdziały
26–28 brakowało jednego miejsca, w którym można sprawdzić zakres
każdego użycia twierdzenia chirurgicznego. W rozdziale 28 dodano
mapę: kategoria DIFF/TOP, wymiar $n$ celu i $n+1$ śladu, dowolna
grupa $\pi_1(X)$ z charakterem orientacji, ustalony brzeg oraz
dekoracje $s/h$. Dla $n=5$ wyraźnie oddzielono kryterium w $L_5^s$
od działania $L_6^s$, które realizuje parzyste twierdzenie 5.8 Walla.
Końcowy gładki $s$-kobordyzm ma wtedy wymiar sześć. Nie użyto w tym
przypadku nieparzystego twierdzenia realizacyjnego 6.5, zaczynającego
się od wymiaru siedem.

Wariant z ustalonym brzegiem wymaga konkretnej identyfikacji
dyfeomorficznej i produktowego kołnierza; jej prostota wynika
z dyfeomorfizmu. Nie nakłada się warunku izomorfizmu grup
podstawowych składowych brzegu z $\pi_1(X)$. Mapa rozróżnia
twierdzenie Smale'a dla jednospójnego $h$-kobordyzmu od ogólnego
$s$-kobordyzmu z zerową torsją oraz grupy $L^s$ od $L^h$.
Odpowiednik TOP z $G/\mathrm{TOP}$ jest wskazany jako osobne
wejście zewnętrzne. Nie wyprowadzono z tabeli nowego twierdzenia.

Zakresy porównano z
[Wallem, twierdzenia 5.6, 5.8, 6.4, 6.5 i §10](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
[Ranickim, §18](https://webhomes.maths.ed.ac.uk/~v1ranick/homology/topman.pdf)
oraz [Crowleyem–Macko, §2.2](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/crowmac.pdf).
Sprawdzono też zgodność odsyłaczy z rozdziałami 24, 25, 27 i 36.
Po końcowej korekcie pełny `buduj_tomy.ps1` zakończył dwa przebiegi.
PDF-y I–IV mają 216, 182, 100 i 80 stron, a indeksy przyjęły
113, 96, 29 i 93 wpisy bez odrzuceń. Kontrola logów nie wykazała
niezdefiniowanych odsyłaczy, `Overfull` ani brakujących znaków;
strony tytułowe mają po trzy łącza do pozostałych tomów, a kopie
PDF zgadzają się według SHA-256. W finalnym PDF-ie tomu III
obejrzano fizyczne strony 78–80: przejście z wersji względnej,
tabelę hipotez i przykład 28.6.2. Tekst i odsyłacz do tomu IV
są czytelne; tabela nie wychodzi poza pole strony.

## Rozdziały 26–28 — jeden śledzony przykład chirurgii (2026-10-27)

Przeprowadzono istniejący przykład $S^6\to S^3\times S^3$
przez trzy rozdziały, bez powtarzania rachunku form z rozdziału 27.
W rozdziale 26 zapisano ślad $W^7$ standardowo obramowanej
chirurgii na $S^2\subset S^6$: od dołu ma uchwyt indeksu trzy,
od góry dualny uchwyt indeksu cztery na
$B=\{0\}\times S^3\subset S^3\times S^3$.
Górna mapa normalna $(f,b)$ stopnia jeden korzysta z wybranego
standardowego przedłużenia danych normalnych. Rozdział 27
odsyła do tego śladu w istniejącym przykładzie pary hiperbolicznej.
Ponieważ kwadratowa część przeszkody zależy od zgodności obramowań
z danymi normalnymi, doprecyzowano także uzasadnienie
$\mu(A)=\mu(B)=0$ w przykładzie i dowodzie lematu lokalnej
stabilizacji. W rozdziale 28 jądro $K_3(f)\cong\Z^2$ ma
$q(\bar x[A]+\bar y[B])=\bar x\bar y$, zatem Arf i klasa
w $L_6^s(\Z)$ są zerowe. Normalny ślad od identyczności daje
ponadto $a=[f,b]=0\in[S^6,G/O]$. W ciągu chirurgii nad $a$
leży standardowa struktura; $L_7^s(\Z)=0$ czyni to włókno
jednoelementowym. Sama mapa $f$ nie jest strukturą, ponieważ
ma niezerowe $H_3$ w jądrze.

Źródłowe wejścia geometryczne i algebraiczne porównano z
[§§1, 5 i 10 Walla](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
w szczególności z twierdzeniem 5.2, lematem 5.5,
twierdzeniem 5.6 i twierdzeniem 10.8. Jawne rozróżnienie
wyboru $b$ jest konieczne: sam ślad bez wybranych danych
nie wyznacza wartości $\mu$ w nazwanej bazie.

Po ostatniej korekcie pełny `buduj_tomy.ps1` zakończył się poprawnie
po dwóch przebiegach. PDF-y tomów I–IV mają odpowiednio
216, 182, 99 i 80 stron; indeksy przyjęły 113, 96, 28 i 93
wpisy, bez odrzuconych. Logi nie zgłosiły niezdefiniowanych odsyłaczy,
przepełnionych wierszy ani brakujących znaków. Każda strona tytułowa
ma trzy łącza do pozostałych tomów, a kopie PDF w katalogu projektu
są identyczne z wynikami składu według SHA-256. Strony 43 i 51
tomu III sprawdzono po korekcie danych normalnych, a strony 77–79
po ostatnim składzie: akapity oraz wzory są czytelne.
Przykład 28.5.2 zaczyna się na stronie PDF 79;
po pierwszym składzie jego nagłówek zostawał u dołu poprzedniej strony,
więc w źródle dodano podział strony przed przykładem i ponowiono skład.

## Rozdział 28 — konstrukcyjne objaśnienie ciągu chirurgii (2026-10-27)

Po potwierdzeniu przez autora kolejności prac dla tomu III uzupełniono
`tex/rozdzialy/24-ciag-chirurgii.tex`. Diagram podniesienia do $BO$
objaśnia klasę $[X,G/O]$ względem wiązki normalnej $X$.
W czterech krokach rozpisano dane wejściowe i wynik każdej strzałki
ciągu: normalne dane cylindra, działanie $L_{n+1}^s$, przejście
ze struktury do klasy normalnej i przeszkodę $L_n^s$.
Osobny diagram pokazuje ślad $W^{n+1}\to X\times I$ z dolnym i górnym
brzegiem. Doprecyzowano, że przy porównaniu dwóch struktur
skleja się odwrócony ślad działania z danym normalnym kobordyzmem;
ich przeszkody $-\alpha$ i $\alpha$ znoszą się przed zastosowaniem
twierdzenia o $s$-kobordyzmie. Stabilizator bazy pozostaje
wnioskiem z twierdzenia Walla, a nie z samego rysunku.
Usunięto dawny abstrakcyjny schemat czterech obiektów,
powielający teraz listę strzałek; podczas składu wypadał na
osobnej, niemal pustej stronie. Wersja względna zaczyna się
na nowej stronie po geometrycznym diagramie.

Wersja z ustalonym brzegiem ma jawne hipotezy: zwarta spójna
gładka $X^n$ z $n\geq5$, ustalona struktura i identyfikacja brzegu,
proste równoważności par, produktowe dane na kołnierzu,
względny stopień jeden ze współczynnikami lokalnymi i
$\pi=\pi_1(X)$ z charakterem orientacji. Dane normalne opisuje
$[X/\partial X,G/O]$, a dane cylindra
$[\Sigma(X/\partial X),G/O]$. Nie dodano sztucznego założenia
o izomorfizmie $\pi_1(\partial X)\to\pi_1(X)$; dla wielu składowych
brzegu chodzi o ich osobne inkluzje. Przykład $D^n$ pokazuje
różnicę między klasami względnymi i bez warunku brzegowego.
Po niezależnym przeglądzie doprecyzowano, że odwzorowania do $G/O$
wysyłają cały brzeg w punkt bazowy, a homotopie są ustalone na brzegu.
Gładką wersję powiązano z
[§10 Walla](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf):
10.2 i 10.6 dają normalne niezmienniki, 10.3 kryterium realizacji,
10.4--10.5 działanie i orbity, 10.7 lewą strzałkę, a gładki
odpowiednik 10.8 dokładność. Wydrukowany wzór 10.8 używa $G/PL$;
wariant $G/O$ wymaga gładkiej identyfikacji z 10.6.

Stwierdzenie $\mathcal S^s_{\mathrm{DIFF}}(S^7)\cong\Theta_7$
uzasadniono przez orientację indukowaną przez równoważność,
jej prostotę dla grupy podstawowej $1$ oraz jednoznaczność
klasy homotopii mapy stopnia $+1$ do $S^7$.
Liczbę $28$ podaje wcześniejsze Twierdzenie~30.4.2, oparte na
Kervairze--Milnorze i Eellsie--Kuiperze; rozdział 28
nie oblicza obrazu $\theta_8$ i nie przypisuje tej liczby
samemu ciągowi. Zmienione miejsca porównano niezależnie
ze źródłem Walla i rozdziałem 30; nie ponawiano audytu
pozostałych części rozdziału 28.

Po tej korekcie `buduj_tomy.ps1` zakończył się po dwóch przebiegach.
PDF-y I--IV mają odpowiednio 216, 182, 99 i 80 stron;
indeksy przyjęły 113, 96, 28 i 93 hasła bez odrzuceń.
Logi nie zawierają niezdefiniowanych odsyłaczy, przepełnionych
wierszy ani brakujących znaków. Kontrola stron tytułowych
potwierdziła w każdym tomie łącza do trzech pozostałych PDF-ów;
sumy SHA-256 plików w katalogu projektu i `build/tomy` są zgodne.
Obejrzano strony PDF 75--79 tomu III: diagramy na stronach 75 i 77,
ciąg względny na stronie 78 oraz układ końca rozdziału na 79.
Po poprawie zdania o brzegu paginacja pozostała taka sama;
etykiety, strzałki i wzór mieszczą się w polu strony.

## Podział tomu III na III i IV (2026-10-27)

Na prośbę autora rozdzielono dawny tom III po rozdziale 30,
czyli przed częścią o potoku Ricciego. Nowy tom III zawiera
rozdziały 23--30 o kobordyzmach, chirurgii i sferach Milnora;
tom IV obejmuje rozdziały 31--38 o wymiarach trzy i cztery,
dodatki A--C i indeks. Granica zachowuje obie części o niskich
wymiarach razem i daje miejsce na rozwinięcie chirurgii w III
oraz przykładów czterowymiarowych w IV. Dokument zbiorczy
i źródła rozdziałów zachowują dotychczasową kolejność.

Sprawdzono mapę importów: tomy mają odpowiednio 10, 12, 8 i 8
rozdziałów. Liczniki nowego tomu IV zaczynają od rozdziału 31
i części IV; oba nowe tomy mają własny indeks. Każdy plik
główny importuje `.aux` trzech pozostałych tomów przez `xr-hyper`,
aby etykiety i łącza działały między wszystkimi czterema PDF-ami.
Plan dalszych uzupełnień dla obu tomów jest wyłącznie w
`PLAN_DZIALANIA.md`.

Pełny `buduj_tomy.ps1` zakończył się po dwóch przebiegach. PDF-y I--IV
mają odpowiednio 216, 182, 97 i 80 stron, a indeksy przyjęły
113, 96, 26 i 93 hasła bez odrzuceń i ostrzeżeń. Sumy SHA-256
czterech PDF-ów w katalogu projektu są identyczne z wynikami
w `build/tomy`. Logi nie zawierają błędów, niezdefiniowanych
odsyłaczy, przepełnionych wierszy ani brakujących znaków.
Pozostały znane komunikaty `Underfull`, powtórzony cel `page.1`
we wszystkich tomach i dwa ostrzeżenia o specyfikatorze rysunku
w tomie I. XML stron tytułowych potwierdził w każdym tomie
łącza do trzech pozostałych plików PDF; w tekście tomu IV
sprawdzono także odsyłacze do tomu II. Obejrzano strony
tytułowe III i IV, indeksy III i IV oraz wybrane strony
rozdziałów 36--38, w tym rysunek indukcji Gompfa.

## Rozdział 38 — pełny audyt (2026-10-27)

Rozdział 38 jest ostatnim rozdziałem numerowanym. Sprawdzono przejścia
od dysków plastra do zanurzeń śladów splotów, obie przeszkody Gompfa,
lematy 1.1 i 1.2 oraz indukcję dającą nieskończenie wiele struktur
gładkich na topologicznym $\R^4$. Porównano hipotezy i kolejność kroków
z [oryginalną pracą Gompfa](https://doi.org/10.4310/jdg/1214439566),
z [Freedmanem](https://www.maths.gla.ac.uk/~mpowell/1982_The%20topology%20of%20four-dimensional%20manifolds.pdf),
z [Freedmanem--Quinnem, §9.5](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf)
oraz z [De Michelisem--Freedmanem](https://doi.org/10.4310/jdg/1214447810).

W lemacie o dyskach plastra wskazano jawnie, że topologiczne
otoczenie normalne lokalnie płaskiego dysku, także względnie przy
brzegu, zapewniają twierdzenia 9.6--9.7 Freedmana--Quinna;
trywializacja nad $D^2$ daje otoczenie
$D^2\times D^2$. W obliczeniu przeszkody podano bazę
$f_i=e_i-e_{i+1}$ dla $1\leq i\leq7$ oraz
$f_8=e_0+e_6+e_7+e_8$. Po odwróceniu kolejności pierwszych
siedmiu wektorów macierz Grama jest $-E_8$,
a wyznacznik $1$ i unimodularność dopełnienia pokazują, że baza
generuje całe $x^\perp$. Zastępuje to niejawne odwołanie do
klasyfikacji określonych kratek. W sklejeniu z lematu 1.2
doprecyzowano odwrócenie orientacji sfer brzegowych i wynikające
z niego produktowe pierścienie między odpowiadającymi splotami.

Istnienie i właściwości uchwytów Cassona, twierdzenia Freedmana,
lematy Gompfa i wynik De Michelisa--Freedmana pozostają jawnie
zewnętrznymi wejściami. Kontrola tekstu obejmuje ich zastosowanie,
nie nowy dowód tych wyników.
W końcowym tomie IV rozdział zajmuje drukowane strony 50--56;
na fizycznej stronie 56 skontrolowano rysunek indukcji,
a ekstrakcja tekstu potwierdziła nowe sformułowanie źródła
Freedmana--Quinna i bazę $-E_8$.

## Rozdziały 36–37 — pełny audyt (2026-10-27)

Na prośbę autora wspólnie sprawdzono rozdziały 36 i 37. Wcześniejszy
przegląd pięciu krótkich rozdziałów z 12 października nie zastępował
pełnej kontroli obu obecnych wersji. Przed zmianami `git fetch origin`
i `git pull --ff-only origin review/rozdzialy-matematyka` potwierdziły,
że czysta gałąź była aktualna.

W rozdziale 36 porównano twierdzenie klasyfikacyjne i jego hipotezy
z [Freedmanem, twierdzenie 1.5](https://www.maths.gla.ac.uk/~mpowell/1982_The%20topology%20of%20four-dimensional%20manifolds.pdf)
oraz [Freedmanem--Quinnem, §10.1--10.2](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf).
Oryginalne twierdzenie dotyczy rozmaitości gładkich poza jednym punktem;
pełna wersja dla zamkniętych jednospójnych rozmaitości TOP pochodzi
z Freedmana--Quinna. Dopisano spinową relację
$\operatorname{ks}(X)\equiv\sigma(X)/8\pmod2$ jako konieczność warunku
dla formy parzystej, odróżniając ją od zewnętrznego istnienia.
Sprawdzono wnioski dla form $H$, $[1]$, $E_8$ i $E_8\oplus E_8$ oraz
topologiczny wniosek Poincarégo; w jego dowodzie jawnie wybrano
orientację sfery homologicznej.

Zakres twierdzenia o zanurzaniu sfer porównano z
[Powellem--Rayem--Teichnerem, twierdzenie B i uwaga 2.2](https://link.springer.com/article/10.1007/s00029-025-01069-y).
Zapisano dokładniej, że obramowane sfery można doprowadzić przez
homotopię regularną do parami rozłącznych lokalnie płaskich zanurzeń
z geometrycznie dualnymi sferami. Warunek
$\lambda(A_i,A_i)=2\mu(A_i)+e(A_i)=0$ i obramowanie dualnych sfer
zapewniają hipotezy użytej wersji. Dopisany rachunek van Kampena
pokazuje, że chirurgia na sferze z geometryczną dualną sferą zachowuje
$\pi_1$. Dla użytego w opisie klasyfikacji topologicznego
$s$-kobordyzmu w wymiarze pięć dopisano założenie dobrej grupy
podstawowej i [Twierdzenie 7.2 Freedmana--Quinna](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf).
Samo zanurzanie, klasyfikacja i twierdzenie o $s$-kobordyzmie pozostają
jawnymi wynikami zewnętrznymi.

W rozdziale 37 sprawdzono lokalny model połączenia, równanie ASD,
rozwinięcie wyznacznika dające znak $c_2$, tożsamość energii oraz
zastosowania do $E_8$ i $E_8\oplus E_8$. Zmianę trywializacji zapisano
na otwartym $U\subset X$, a przykład połączenia płaskiego umieszczono
na wiązce trywialnej. Dla wiązki o grupie $\mathrm{SU}(2)$
uzasadniono całkowite $c_1(E)=0$ przez trywialność $\det E$,
nie tylko znikanie formy Cherna--Weila.
Porównanie z [oryginalną pracą Donaldsona](https://doi.org/10.4310/jdg/1214437665)
i jego [szkicem metody z 1983 roku](https://doi.org/10.1090/S0273-0979-1983-15090-5)
wyjaśnia przejście od źródłowej konwencji samodualnej
$c_2(E)[X]=-1$ na dodatnio określonej rozmaitości do konwencji ASD
$c_2(E)[X]=1$ po odwróceniu orientacji. Dopisano rachunek klas
redukcji $E\cong L\oplus L^{-1}$ o kwadracie $-1$ i elementarny
krok algebraiczny: pary takich klas są ortogonalne, a przy
zewnętrznym wyniku $n(Q_X)=b_2(X)$ tworzą bazę. Konstrukcja,
zwartość i orientowalność przestrzeni moduli, równość $n(Q_X)=b_2(X)$
oraz diagonalizacja Donaldsona pozostają wejściami zewnętrznymi.
Zawężono też tytuł wniosku o $E_8$ do przypadku jednospójnego,
zgodnie z cytowaną wersją twierdzenia. Niedostępny adres PDF-u
szkicu Donaldsona zastąpiono DOI.
W końcowym tomie IV rozdziały 36 i 37 zajmują odpowiednio
drukowane strony 43--45 i 46--49; obejrzano ich wybrane strony
oraz sprawdzono odsyłacze, log i przejście do rozdziału 38.

## Rozdział 35 — uchwyty Cassona i zanurzanie dysków (2026-10-26)

Przeprowadzono pełny audyt matematyczny i redakcyjny rozdziału 35.
Definicje uchwytu z załamaniami, wieży i uchwytu Cassona porównano
z pracą Freedmana z 1982 roku. W rachunku pierwszego piętra wyjaśniono,
że po zapomnieniu obszaru przyczepienia uchwyt z $k$ załamaniami jest
dyfeomorficzny z brzegową sumą spójną $k$ kopii $S^1\times D^3$.
Nieozdobiona krzywa diagramu jest wyróżnionym okręgiem przyczepienia,
a nie dodatkowym uchwytem 2, więc nie narzuca relacji generatorom.
Sprawdzono następnie indukcyjne zabijanie generatorów między piętrami
i wniosek $\pi_1(CH)=0$; tekst nadal nie utożsamia tej własności ze
standardowością otwartego uchwytu 2.

Rozdzielono niezredukowaną liczbę samoprzecięcia $\mu$, zachowywaną przez
homotopię regularną, od zredukowanej $\widetilde\mu$, zależnej od klasy
homotopii. Doprecyzowano dzięki temu różnicę między twierdzeniem
Freedmana--Quinna i współczesną wersją Powell--Raya--Teichnera oraz rolę
warunku $\mu(A_i)=0$ we wniosku z homotopią regularną. Poprawiono numery
wyników: w przeformatowanym wydaniu Freedmana--Quinna są to Twierdzenie
5.2 i Wniosek 5.2.1, a w druku z 1990 roku odpowiednio 5.1A i 5.1B.
W konkluzji zapisano jawnie, że geometrycznie dualne sfery $B'_j$ można
wybrać w klasach homotopii $B_j$. Dowód $\pi_1$-pomijalności dopełnienia
dysków sprawdzono przez meridiany i przekłute sfery dualne.

Wyjaśniono też granicę konstrukcji: klasyczny uchwyt Cassona sam wystarcza
w przypadku jednospójnym, natomiast dla nietrywialnej grupy podstawowej
twierdzenie używa powierzchni z dyskami zamykającymi, uogólnionych wież
i kontroli pętli punktów podwójnych. Grupy o wzroście podwykładniczym
przedstawiono jako inny ważny znany zakres wyniku, a nie jako nadklasę
grup wielostopniowo skończonych lub cyklicznych. Konstrukcja powierzchni
zamykających, zbieżność wież i standardowość topologiczna uchwytu Cassona
pozostają jawnie nazwanymi wynikami zewnętrznymi.

Pełny `buduj_tomy.ps1` zakończył dwa przebiegi powodzeniem. Tomy mają
216, 182 i 173 strony; indeksy przyjęły odpowiednio 113, 96 i 119 haseł,
bez odrzuceń i ostrzeżeń. Logi nie zawierają błędów, niezdefiniowanych
odsyłaczy, przepełnionych wierszy ani brakujących znaków. Pozostały znane
komunikaty o powtórzonym celu `page.1`, wcześniejsze `Underfull` poza
rozdziałem 35 oraz dwa ostrzeżenia tomu I o zmianie specyfikatora rysunku
z `h` na `ht`. Obejrzano fizyczne strony PDF 131--137 tomu III, czyli cały
rozdział 35 na stronach drukowanych 130--136. Tekst, wzory, rysunek drzewa,
odnośniki i podział stron są czytelne; rozdział 36 zaczyna się na fizycznej
stronie 138.

## Rozdział 34 — formy przecięcia i uchwyty w wymiarze cztery (2026-10-25)

Przeprowadzono pełny audyt rozdziału 34, bez rozszerzania zakresu na
rozdziały 35–38. Sprawdzono definicję formy przecięcia w kategoriach
TOP i DIFF, argument o braku torsji w $H_2$ w przypadku jednospójnym,
niezmienniczość parzystości i sygnatury, przykłady $H$ i $I_{1,1}$
oraz rachunek macierzy $E_8$. Rekurencja dla wyznaczników $A_m$,
minor $(A_7^{-1})_{33}=15/8$, dopełnienie Schura $1/8$ i wniosek
$\det E_8=1$, $\sigma(E_8)=8$ są poprawne.

Dopisano osobny rachunek $2E_8=E_8\oplus E_8$: forma jest parzysta,
unimodularna, dodatnio określona, ma rząd i sygnaturę $16$ oraz nie jest
izometryczna z $I_{16}$. Wyraźnie odróżniono sumę ortogonalną od
skalarnej macierzy $2\cdot E_8$. Dwie rozłączne kopie splotu dają
blokową macierz $2E_8$, lecz sam gładki korpus z uchwytów nie dowodzi
istnienia zamkniętej rozmaitości o tej formie; topologiczne domknięcie
pozostaje wejściem Freedmana, a przeszkoda gładka jest omawiana dopiero
w rozdziale o twierdzeniu Donaldsona.

W części uchwytowej sprawdzono względny kompleks uchwytowy, opis
samoprzecięcia przez obramowanie, przecięć mieszanych przez liczby
sprzężenia oraz ciąg dokładny pary użyty do wykazania, że unimodularna
macierz daje brzeg będący całkowitą sferą homologiczną. Dopisano wpływ
odwrócenia orientacji komponentu: odpowiedni wiersz i kolumna zmieniają
znak, co jest zmianą bazy i nie zmienia izometrii formy. Rachunek
$2+2-4=0$ poprawnie wyjaśnia przeszkodę dla gładkiego triku Whitneya,
ale nie jest przedstawiany jako dowód twierdzenia o zanurzaniu dysku.

Pełny `buduj_tomy.ps1` zakończył dwa przebiegi powodzeniem. Tomy mają
216, 182 i 172 strony; indeksy przyjęły odpowiednio 113, 96 i 119 haseł,
bez odrzuceń i ostrzeżeń. Logi nie zawierają niezdefiniowanych odsyłaczy,
przepełnionych wierszy, brakujących znaków ani błędów składu. Pozostały
znane komunikaty o powtórzonym celu `page.1`, wcześniejsze `Underfull`
poza rozdziałem 34 oraz dwa ostrzeżenia tomu I o zmianie specyfikatora
rysunku z `h` na `ht`. Obejrzano fizyczne strony PDF 125--130 tomu III,
czyli cały rozdział 34 na stronach drukowanych 124--129. Nowy przykład
$2E_8$, akapit o orientacjach, oba rysunki i odsyłacze są czytelne;
kontrola XML potwierdziła cele 34.4.2, 36.2.1 i 37.3.3 oraz odsyłacze
międzytomowe do tomu II.

## Dodatki A i B — niezależny audyt (2026-10-25)

W dodatku A porównano katalog zależności zewnętrznych z faktycznymi
deklaracjami i dowodami w 38 rozdziałach oraz z podanymi źródłami.
Usunięto krytyczną niezgodność wymiarową: twierdzenie Walla o
przeszkodzie chirurgicznej obejmuje $n\geq5$, z przypadkiem parzystym
$2k\geq6$ i nieparzystym $2k+1\geq5$; oddzielne nieparzyste
twierdzenie realizacyjne 6.5 zaczyna się w wymiarze siedem.
Dopisano hipotezy wersji względnej, dekorację $h$, ciąg Rothenberga,
normalne niezmienniki, działanie grupy $L$ i ciąg chirurgii, w tym
realizację przez twierdzenia 5.8 i 6.5 Walla.

Katalog uzupełniono o brakujące, jawnie zewnętrzne składniki:
miarę Hausdorffa w przestrzeni euklidesowej, dokładne warunki triku
Whitneya, charakterystykę prostej równoważności przez torsję
Whiteheada i porównanie torsji Morse'a z komórkową, twierdzenie
Ambrose'a--Singera, globalny rozkład de Rhama, miarę Haara oraz
topologiczną normalizację teorii Cherna--Weila. Rozdzielono
triangulację powierzchni od klasyfikacji Bardena i wskazano jej
pozostałe wejścia Walla, Whiteheada, Haefligera i teorii kobordyzmu.
Poprawiono błędny DOI pracy Whiteheada, doprecyzowano konstrukcję
dobrego rozdrobnienia, współczynniki grup $L$ w ciągu chirurgii,
jednoznaczność globalnego rozkładu de Rhama oraz odsyłacz do kryterium
stabilnego wygładzania Freedmana--Quinna.
W części o sferach Milnora dopisano całkowitość indeksu Diraca,
zupełność niezmiennika Eellsa--Kuipera i
$\Theta_7=bP_8\cong\Z/28$ Kervaire'a--Milnora. Doprecyzowano także
hipotezę wygasania potoku Ricciego, orientację w topologicznej
dualności Poincarégo, pełne założenia twierdzenia o zanurzaniu dysków,
stabilny charakter przeszkody Kirby'ego--Siebenmanna i rolę twierdzeń
Quinna w konstrukcji egzotycznych $\R^4$.

W dodatku B sprawdzono lokalną homologię także dla wymiaru zero,
oba wzory na cechę Eulera, znak charakterystyki względnej, wkład
uchwytu $(-1)^k$, addytywność przy sklejaniu oraz komórkowe rachunki
powierzchni orientowalnych i nieorientowalnych. Rachunki były poprawne.
W dowodzie homologicznej niezmienniczości wymiaru nazwano użyty
homeomorfizm. W rachunku uchwytowym dopisano względny model CW,
który uzasadnia istnienie skończonego modelu dla $W$, a po wzorze
nad dowolnym ciałem dodano odsyłacz do dualności Poincarégo i wniosek
$\chi(M)=0$ dla zamkniętej zorientowanej rozmaitości nieparzystego
wymiaru.

Pełny `buduj_tomy.ps1` zakończył dwa przebiegi powodzeniem. Tomy mają
216, 182 i 171 stron; indeksy przyjęły odpowiednio 113, 96 i 119
haseł, bez odrzuceń i ostrzeżeń. Logi nie zawierają niezdefiniowanych
odsyłaczy, przepełnionych wierszy ani brakujących znaków. Pozostały
znane ostrzeżenia o powtórzonym celu `page.1`, wcześniejsze
nieprzepełnione `Underfull` oraz dwa ostrzeżenia tomu I o zmianie
specyfikatora rysunku z `h` na `ht`, niezwiązane z dodatkami.
Obejrzano wszystkie
strony dodatków A i B: fizyczne strony PDF 150–159, odpowiadające
stronom drukowanym 149–158. Sprawdzono także, że odsyłacze z tych stron
prowadzą do `geometria_tom1.pdf` i `geometria_tom2.pdf`; tekst i XML
wyodrębniono ponownie z finalnego PDF-u po ostatniej zmianie źródeł.

## Rozdział 2, §2.3 — równanie krzywej całkowej w jednej mapie (2026-10-23)

W dowodzie Twierdzenia 2.3.2 doprecyzowano, że mapa
$\varphi\colon U\to D=\varphi(U)\subset\R^n$ przenosi wektor pola
do $T_vD$, a ponieważ $D$ jest otwarty w $\R^n$, zapis tego wektora
w standardowej bazie daje funkcję $F\colon D\to\R^n$ potrzebną
do równania $u'=F(u)$. Jest to konstrukcja w jednej mapie;
odwołanie do wcześniejszej uwagi, omawiającej także zmianę dwóch map,
usunięto z dowodu. Zaznaczono również powrót do krzywej na $M$
przez $\varphi^{-1}$.
We wzorze poprzedzającym twierdzenie poprawiono dziedziny:
współczynniki $X_\varphi^i$ są funkcjami na $U$, natomiast
$X_\varphi^i\circ\varphi^{-1}$ są funkcjami punktu $x\in D$.
Pełny `buduj_tomy.ps1` zakończył się powodzeniem: tomy mają 216, 182
i 168 stron, indeksy przyjęły odpowiednio 113, 96 i 119 haseł bez
odrzuceń, a logi nie zawierają brakujących odsyłaczy ani przepełnionych
wierszy. Obejrzano strony 70–71 tomu I z nowym zapisem równania
i początkiem dowodu.

## Przeniesienie projektu do podkatalogu (2026-10-22)

Przeniesiono źródła, PDF-y, skrypt budowania i dokumentację do katalogu
`geometria i topologia różniczkowa/`. Zachowano ich wzajemne położenie, więc
ścieżki `\input`, odsyłacze między tomami i polecenia budowania działają po
uruchomieniu z nowego katalogu. Instrukcje w `README.md` i `AGENTS.md`
wskazują teraz właściwy katalog roboczy.
Pełny `buduj_tomy.ps1` zakończył się powodzeniem: trzy tomy złożono,
odsyłacze ustabilizowały się po dwóch przebiegach, a kontrola indeksów
i niezdefiniowanych odsyłaczy nie zgłosiła błędów.

## Rozdział 2, §2.3 — dowód istnienia i gładkiej zależności krzywych całkowych (2026-10-22)

W dowodzie Twierdzenia 2.3.2 wskazano mapę $(U,\varphi)$ o współrzędnych
$(u^1,\ldots,u^n)$, przeniesiono pole przez różniczkę $\dd\varphi$
i rozpisano regułę łańcucha prowadzącą od $\gamma'=X_\gamma$
do $u'=F(u)$, a także przejście odwrotne. Kula kontrolna leży
w obrazie mapy $\varphi(U)$. Operator Picarda działa na krzywych
zdefiniowanych na $[-h,h]$; dla $t<0$ całka ma przeciwną orientację,
a jej argument pozostaje w dziedzinie krzywej. Oszacowania z $|t|\leq h$
obejmują oba kierunki czasu bez ograniczania dowodu do $[0,h]$.

Uściślono lokalną jednoznaczność również dla rozwiązań zadanych
na mniejszym przedziale, warunek $a+v\in B_r(u_0)$ przy różniczkowaniu
po danych i normę supremum w oszacowaniu pochodnej. Dopisano
równanie kontrakcyjne dla kandydatów na pochodne wyższych rzędów,
sprawdzenie ich przez resztę Taylora i uzasadnienie ciągłości
pochodnych mieszanych. Wskazano, jak złożenie lokalnych rozwiązań
wzdłuż zwartego fragmentu krzywej daje zależność przy dowolnym czasie;
pełne szczegóły pozostają w następnym twierdzeniu o przepływie.
Poprawiono tam odsyłacz z samego kroku 1 na kroki 1–2.
Zakres tej iteracji nie obejmuje ponownego audytu całego rozdziału.

`buduj_tomy.ps1` zakończył dwa przebiegi: tomy mają 216, 182 i 168 stron.
Indeksy przyjęły 113, 96 i 119 haseł, bez odrzuceń. W logach nie ma
brakujących odsyłaczy, przepełnionych wierszy ani brakujących znaków.
Obejrzano strony PDF 71–74 tomu I z dowodem i sąsiednim rysunkiem;
łącza do wzorów (2.1.2) i (2.3.1) wskazują właściwe strony.
Zastany przed pracą, lokalnie zmieniony PDF tomu I (213 stron)
zachowano w `build/tomy/preexisting-geometria_tom1.pdf` przed
zastąpieniem go aktualnym składem ze źródeł.

## Rozdział 2, §2.2 — nawias Liego i rozkłady styczne (2026-10-22)

Sprawdzono zależności dalszego tekstu: lokalne twierdzenie Frobeniusa
z etykietą `prop:frobenius-lokalny` jest użyte w dowodzie
lokalnego rozkładu metryki w rozdziale 14. Daje tam liście dwóch
rozkładów równoległych oraz lokalne współrzędne produktu. Z tego
powodu zachowano twierdzenie i jego pełny dowód po prostowaniu pola.

Po wzorze współrzędnych na nawias Liego dopisano interpretację
krótkich ruchów: składnik rzędu $t^2$ ich różnicy w dwóch
kolejnościach jest wyznaczony przez $[X,Y]$. Odesłano do późniejszego
rachunku przepływów i doprecyzowano podpis rysunku: znikanie nawiasu
w jednym punkcie usuwa tylko składnik rzędu $t^2$.
W uwadze o Frobeniusie zdefiniowano podrozmaitość
całkową przez równość przestrzeni stycznych, podano sprawdzanie
inwolutywności na lokalnej bazie i przykład
$\mathcal D=\ker\dd(z-xy)$ z powierzchniami $z-xy=c$.
W przykładzie przeciwnym doprecyzowano, dlaczego $\partial_z$
nie należy do rozkładu. Rachunek $[X,xY]=Y$ pokazuje, że
inwolutywność wymaga pozostawania nawiasu w rozkładzie, a nie
zerowania nawiasów wszystkich jego pól. Dodano odsyłacz do
zastosowania w rozdziale 14. Zakres iteracji obejmuje tę część
rozdziału 2, bez ponownego audytu całego rozdziału.

`buduj_tomy.ps1` zakończył trzy przebiegi: tomy mają 215, 182 i 168 stron,
a indeksy przyjęły 113, 96 i 119 haseł bez odrzuceń. Logi nie wykazują
błędów, przepełnionych wierszy ani nierozwiązanych odsyłaczy.
Obejrzano strony PDF 70–71 tomu I z nowym tekstem oraz stronę 81
z rysunkiem komutatora przepływów. Łącze przy Twierdzeniu 14.8.2
prowadzi z tomu I do `geometria_tom2.pdf`, a odsyłacz do
Stwierdzenia 2.5.4 z dowodu w tomie II do `geometria_tom1.pdf`.

## Rozdział 2, §2.1 — pole wzdłuż odwzorowania (2026-10-21)

Na prośbę autora rozpisano ostatnią uwagę sekcji. Pole $Y$ na celu
musiałoby spełniać $Y_{F(p)}=dF_p(X_p)$ dla każdego $p$. Przy
$F(t)=t^2$ i $X=\partial_t$ punkty $t$ i $-t$ dla $t>0$ wymuszają
w tym samym $T_{t^2}\R$ przeciwne wartości $2t$ i $-2t$;
wartości pola na obrazie nie da się więc nawet określić jednoznacznie.
Przy $F(t)=t^3$ każdy punkt ma jeden przeciwobraz, lecz wymuszony
współczynnik $3|y|^{2/3}$ nie ma pochodnej w zerze, co wykazano
ilorazem różnicowym. Dodano przykład $X=t\partial_t$ dla $F(t)=t^2$,
aby sprecyzować, że przeszkoda zależy od pary $(F,X)$.

`buduj_tomy.ps1` zakończył dwa przebiegi: tomy mają 215, 182 i 168 stron.
Indeksy przyjęły 113, 96 i 119 haseł, bez odrzuceń i ostrzeżeń.
W logach nie ma błędów, przepełnionych wierszy ani nierozwiązanych
odsyłaczy. Sprawdzono, że łącza między tomami wskazują właściwe
nazwy PDF-ów. Obejrzano strony PDF 68–69 tomu I (drukowane 67–68):
nowe wzory i tekst są czytelne, a istniejący rysunek sfery na pierwszej
z tych stron zachowuje widoczne etykiety.

## Rozdział 2, §2.1 — przegląd sekcji o polach wektorowych (2026-10-21)

Przejrzano całą sekcję „Pola wektorowe i derywacje globalne”, od definicji
pola do uwagi o polu wzdłuż odwzorowania. Sprawdzono typy obiektów i
uzasadnienia: derywacja w punkcie daje liczbę, derywacja globalna funkcję,
a pole $X$ jest gładką sekcją. W dowodzie ich odpowiedniości wskazano
otoczenie o zwartym domknięciu, co uzasadnia wybór funkcji odcinającej.
Przykład derywacji na $\R$ przeniesiono za twierdzenie, a uwagę o module
pól i lokalnych bazach umieszczono bezpośrednio po nim.

Przed schematem pól w przestrzeni otaczającej podano osobno wzór
$\widehat X_\varphi(u)=(d\varphi)_{\varphi^{-1}(u)}X_{\varphi^{-1}(u)}$
na przeniesienie pola przez mapę i wyprowadzono z reguły łańcucha
transformację współczynników przy zmianie mapy. Następnie połączono
trzy kroki rachunku: styczność $W_p$, pole $X_p$ wyznaczone przez
różniczkę inkluzji oraz współczynniki w mapie odczytywane z równania
$W_{F(u)}=(dF)_u\widehat X_\varphi(u)$ dla
$F=\iota\circ\varphi^{-1}$. To równanie wyjaśnia wystąpienie
różniczki odwrotności mapy.

Przykłady okręgu i sfery stoją teraz obok siebie. Na okręgu
odróżniono odwrotność mapy $\gamma\colon I\to S_r^1$ od
parametryzacji $F=\iota\circ\gamma$ w $\R^2$, a przed funkcją stałą na okręgu
obliczono działanie pola na zmienną funkcję współrzędnościową.
Na sferze wyróżniony punkt rysunku leży w użytej mapie górnej
półsfery; strzałka w $\R^3$ ma oznaczenie $W_p$, zgodne z typem
wektora. Na końcu przykładów wyjaśniono dwa sposoby różniczkowania
funkcji, w tym istnienie lokalnego przedłużenia do $\R^N$ i
niezależność wyniku od tego przedłużenia. Ostatnia uwaga łączy
przeniesienie pola przez mapę z ogólnym pojęciem pola wzdłuż
odwzorowania. Przegląd obejmuje §2.1, nie cały rozdział 2.

Po zmianach `buduj_tomy.ps1` zakończył dwa przebiegi i złożył tomy
o 215, 182 i 168 stronach. Indeksy przyjęły odpowiednio 113, 96
i 119 haseł, bez odrzuceń i ostrzeżeń. W logach nie ma błędów,
przepełnionych wierszy ani nierozwiązanych odsyłaczy; cztery
komunikaty o niedopełnionych wierszach i dwa o zmianie specyfikatora
rysunku dotyczą innych miejsc. Potwierdzono nazwy docelowych PDF-ów
w łączach między wszystkimi tomami. Obejrzano strony PDF 63–69
tomu I (drukowane 62–68): cała sekcja jest czytelna, a punkt
na sferze i etykieta $W_p$ nie kolidują z siatką ani powierzchnią.

## Rozdział 2 — schemat pól na okręgu i sferze (2026-10-21)

Na prośbę autora przełożono oba przykłady na kolejność odpowiadającą
rzeczywistemu rachunkowi: pole $W$ w przestrzeni otaczającej,
sprawdzenie styczności, jednoznaczne pole $X$ na podrozmaitości
przez różniczkę inkluzji, wybór mapy i odczyt współczynników.
Dopisano schemat przestrzeni stycznych i równanie
$(d(\iota\circ\varphi^{-1}))_u\widehat X_\varphi(u)=W_p$.
Wyjaśnia on rolę różniczki odwrotności mapy oraz związek ze
wcześniejszym wzorem na zmianę mapy. W przykładzie okręgu
pochodna parametryzacji daje współczynnik $X^1=1$;
na sferze rozwiązanie dwóch pierwszych składowych równania
daje $(-v,u)$, a trzecia jest z nimi zgodna dzięki styczności.
Rozdzielono zapis $W_p\in T_p\R^N$ od $X_p\in T_pM$,
zachowując dotychczasowe działanie pola na funkcję i rysunek.
Jest to redakcja wskazanych przykładów, nie pełny audyt rozdziału 2.

`buduj_tomy.ps1` ustabilizował odsyłacze po dwóch przebiegach
i złożył tomy o 215, 182 i 168 stronach. Indeksy przyjęły
odpowiednio 113, 96 i 119 haseł, bez odrzuceń i ostrzeżeń.
W logach nie ma błędów, przepełnień ani nierozwiązanych odsyłaczy;
cztery komunikaty o niedopełnionych wierszach dotyczą innych miejsc.
Sprawdzono nazwy PDF-ów w łączach między wszystkimi tomami
oraz obejrzano strony PDF 66–68 tomu I (drukowane 65–67),
zawierające schemat, oba przykłady i rysunek sfery.

## Rozdział 2 — współrzędne pola na sferze (2026-10-20)

W przykładzie pola $X_p=(-y,x,0)$ rozpisano przejście do współrzędnych
na górnej półsferze. Różniczka mapy $\varphi(x,y,z)=(x,y)$ odczytuje
z $X_p$ współczynniki $(-v,u)$, co daje $X=-v\partial_u+u\partial_v$.
Odwrotna mapa, złożona z inkluzją sfery do $\R^3$, parametryzuje
półsferę; jej różniczka przelicza te współczynniki z powrotem
na wektor w przestrzeni otaczającej. Obliczono pochodne funkcji
$z(u,v)=\sqrt{1-u^2-v^2}$ i pokazano, że składowa pionowa
znika dla pary $(-v,u)$. Wyjaśniono użycie reguły łańcucha
i znaczenie wektorów bazy współrzędnościowej. Zmiana odpowiada
na pytanie o rolę odwrotności mapy i obejmuje tylko ten przykład.

Po zmianie `buduj_tomy.ps1` złożył dwa przebiegi oraz trzy tomy
o 214, 182 i 168 stronach. Indeksy przyjęły odpowiednio 113, 96
i 119 wpisów bez odrzuceń. Logi nie zawierają błędów, przepełnień
ani brakujących odsyłaczy; sprawdzono też łącza między tomami.
Obejrzano strony 67–68 PDF tomu I (drukowane 66–67): rachunek
i rysunek są czytelne, a etykiety nie są zasłonięte.

## Rozdział 1 — wektory normalne do podrozmaitości (2026-10-20)

Po twierdzeniu o poziomicy dodano ogólny wzór dla podrozmaitości
$S\subseteq\R^m$ opisanej lokalnie przez niezależne równania
$f_1=\cdots=f_{m-k}=0$:
$T_pS=\bigcap_j\ker df_{j,p}
=(\operatorname{span}\{\nabla f_j(p)\})^\perp$.
Wyprowadzono go z twierdzenia o przeciwobrazie wartości regularnej
i tożsamości $df_{j,p}(v)=\langle\nabla f_j(p),v\rangle$.
Mapy plasterkowe dostarczają takich równań dla każdej podrozmaitości
euklidesowej. Wynik umieszczono po twierdzeniu o poziomicy,
przed istniejącym przykładem sfery. Przegląd obejmuje dopisany wynik,
nie cały rozdział.

Po zmianie buduj_tomy.ps1 wykonał dwa przebiegi i złożył tomy
o 214, 182 i 168 stronach. Indeksy przyjęły 113, 96 i 119 wpisów
bez odrzuceń; logi nie zawierają błędów, przepełnień ani brakujących
odsyłaczy. Potwierdzono docelowe nazwy plików w łączach między
każdą parą tomów. Obejrzano strony 61–62 PDF tomu I
(drukowane 60–61): stwierdzenie i jego dowód są czytelne,
a dotychczasowy przykład sfery następuje bezpośrednio po dowodzie.

## Rozdział 1 — przestrzeń styczna do podrozmaitości (2026-10-20)

W §1.12, bezpośrednio po konstrukcji struktury gładkiej podrozmaitości,
dodano stwierdzenie identyfikujące $T_pS$ z obrazem różniczki inkluzji
w $T_pM$. W mapie plasterkowej obraz ten jest rozpięty przez pochodne
w kierunkach współrzędnych podrozmaitości i jest wspólnym jądrem
różniczek współrzędnych poprzecznych. Dowód wyprowadza oba opisy
z lokalnej postaci inkluzji $u\mapsto(u,0)$ i pokazuje, że każdy
wektor z obrazu jest prędkością krzywej w $S$. Uściślono także
przypadki skrajnych wymiarów $k=0$ i $k=n$. Wynik uzasadnia
identyfikację używaną zaraz potem przy wiązce normalnej.

Przykład $S^1\subset\R^2$ w punkcie $(1,0)$ oblicza
$T_pS^1=\{(0,b):b\in\R\}$ dwoma krokami: różniczkowanie równania
okręgu ogranicza możliwe prędkości, a krzywe
$(\cos bt,\sin bt)$ realizują każdą z nich. Lokalna postać
submersji uzasadnia status okręgu jako podrozmaitości.
Rysunek rozróżnia przestrzeń wektorów stycznych od jej przesuniętej
prostej afinicznej w punkcie $p$. Ujednolicono termin „podrozmaitość
zanurzona” w następnym przykładzie i dodano hasło do indeksu.
Przegląd dotyczy nowego fragmentu, nie całego rozdziału 1.

Po zmianach buduj_tomy.ps1 wykonał trzy przebiegi i złożył tomy
o 214, 182 i 168 stronach. Indeksy przyjęły odpowiednio 113, 96
i 119 wpisów bez odrzuceń, w tym nowe hasło o przestrzeni stycznej.
Logi nie zawierają błędów, przepełnień ani nierozwiązanych odsyłaczy.
W PDF-ach sprawdzono nazwy plików w łączach między każdą parą tomów.
Obejrzano stronę 59 PDF tomu I (drukowaną 58): wynik, przykład
i rysunek są na jednej stronie, a etykiety i punkt styczności
pozostają czytelne.

## Rozdział 2 — rysunek pola na sferze (2026-10-20)

Do przykładu $X_p=(-y,x,0)$ dodano rysunek sfery w jasnoniebieskim
stylu rozdziału 1. Strzałki są rzutami wektorów w punktach widocznej
części równika i górnego równoleżnika; dla wyróżnionego
$p=(0,-1,0)$ wskazują $X_p=(1,0,0)$. Złote znaczniki pokazują
oba zera pola; przerywany znacznik bieguna południowego oznacza,
że leży po niewidocznej stronie sfery. Rzut, położenia znaczników
i znaki wektorów sprawdzono ze wzorem pola. Po składzie tomu I
obejrzano strony PDF 66–67: ilustracja poprzedza następną uwagę,
a etykiety $N,S,p,X_p$ nie są zasłonięte.
Pełny skład dał tomy o 213, 182 i 168 stronach. Logi nie zgłaszają
brakujących odsyłaczy ani przepełnionych wierszy; indeksy przyjęły
112, 96 i 119 wpisów bez odrzuceń. W gotowych PDF-ach potwierdzono
łącza między każdą parą tomów.

## Rozdział 2 — inkluzja okręgu (2026-10-20)

W przykładzie działania pola na funkcję na $S_r^1$ dopisano jawny
wzór $\iota(u,v)=(u,v)$. Wyjaśniono, że inkluzja jest ograniczeniem
identyczności płaszczyzny do okręgu, lecz ma przeciwdziedzinę
$\R^2$, więc nie jest identycznością $S_r^1\to S_r^1$.
To doprecyzowanie ustala sens dalszej różniczki
$(\dd\iota)_p:T_pS_r^1\to T_p\R^2$ bez zmiany rachunku pola.
Pełny skład trzech tomów zakończył się PDF-ami o 212, 182 i 168
stronach. Logi nie zawierają brakujących odsyłaczy ani przepełnionych
wierszy; indeksy przyjęły 112, 96 i 119 wpisów bez odrzuceń.
Nowe zdania odczytano w PDF tomu I, a łącza z niego do tomów II i III
pozostały aktywne.

## Audyt rozdziałów 15–18 (2026-10-20)

Przeczytano całe cztery rozdziały tomu II i sprawdzono ich zależności.
W rozdziale 15 porównano nawias, pola niezmiennicze, eksponentę,
działanie adjungowane i nakrycie
$\mathrm{SU}(2)\to\mathrm{SO}(3)$ z [notatkami Conrada i
Landesmana](https://math.stanford.edu/~conrad/210CPage/handouts/lie_groups_notes.pdf).
Nie znaleziono błędu w rachunkach. Doprecyzowano identyfikację torusa
obrotowego z $(\R/2\pi\Z)^2$ i oszacowanie pochodnych szeregu
macierzowego; wcześniej oszacowanie obejmowało tylko same wyrazy.

W rozdziale 16 sprawdzono uśrednianie, działanie $G$ na $G/H$,
zupełność, ilorazy przez grupy dyskretne, lokalny model orbifoldu
oraz modele euklidesowy, afiniczny, rzutowy i hiperboliczny względem
[Lee](https://julianchaidez.net/materials/reu/lee_smooth_manifolds.pdf),
[Thurstona](https://library.slmath.org/nonmsri/gt3m/PDF/13.pdf) i
[Scotta](https://sschleimer.warwick.ac.uk/Teach/2021_3MFDS/References/1983the_geometries_of_three-manifolds.pdf).
Wstęp ograniczono do rzeczywiście wyprowadzonego działania
$\mathrm{PSL}(2,\R)$ przez izometrie: rozdział nie dowodzi, że jest to
pełna grupa izometrii.

W rozdziale 17 sprawdzono transgresję, normalizację Pfaffianu,
klasę Eulera i brzegowy wzór Cherna--Gaussa--Bonneta. Zastąpiono
zbyt skrótowe odwołanie do rozszczepienia rachunkiem
$p_1(E)=-c_2(E\otimes_\R\C)$ i jawnie oznaczono zgodność formy
Cherna z całkowitą klasą topologiczną jako wejście zewnętrzne.
Sprawdzono znak według [Hatchera](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
i wzory krzywizny według
[Biquarda](https://webusers.imj-prg.fr/~olivier.biquard/m2dg2022.pdf).
Rozpisano kompleks względnych form de Rhama, jego różniczkę,
porównanie z formami znikającymi na brzegu i znak parowania z
włóknem; punktem odniesienia jest
[Bott--Tu, §7](https://doi.org/10.1007/978-1-4757-3951-0).
Granicę całek wokół zer uzasadniono w zorientowanej ramie przez
oszacowanie $O(\varepsilon)$ składników poziomych. W wersji brzegowej
doprecyzowano transwersalność pól, zachowanie dodatniej składowej
normalnej oraz znaki końców kobordyzmu zer.

W rozdziale 18 sprawdzono znaki kodiferencjału, laplasjanu
Hodge'a, wzoru Weitzenböcka i tożsamości Bochnera w konwencji
rozdziału 14. Zakres twierdzenia o sprzężeniu obejmuje jawnie
stopnie krańcowe. Doprecyzowano, że
[notatki MIT, wykład 15](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/d6848bb391c032ef27993e984fef4558_lect15.pdf)
omawiają rozkład Hodge'a i parametryks, a przyjęte twierdzenie
eliptyczne pozostaje wejściem analitycznym. Zdefiniowano sygnaturę
formy przecięcia i dodano kontrolny przykład $S^2\times S^2$
z $b_2^+=b_2^-=1$.
Pełny skład zakończył się PDF-ami o 212, 182 i 168 stronach.
Logi nie zgłaszają brakujących odsyłaczy ani przepełnionych
wierszy, a indeksy przyjęły odpowiednio 112, 96 i 119 wpisów
bez odrzuceń. W gotowych PDF-ach potwierdzono łącza między
każdą parą tomów; tekst nowych akapitów sprawdzono w tomie II.
W tych czterech rozdziałach nie zmieniano rysunków.

## Audyt rozdziałów 31–33 (2026-10-20)

Przeczytano w całości rozdziały o potoku Ricciego, trójwymiarowym
twierdzeniu Poincarégo i geometryzacji Thurstona. Rachunek skalowania,
ewolucji objętości i skalara, zasady maksimum oraz symbolu poprawki
DeTurcka w rozdziale 31 jest zgodny z przyjętą konwencją krzywizny.
Istnienie i jednoznaczność rozwiązań układów parabolicznych pozostają
jawnym wejściem analitycznym Hamiltona i DeTurcka. Sprawdzono założenia
braku lokalnego zapadania z twierdzeniem 4.1 Perelmana, wersję
wygasania z twierdzeniem 18.1 Morgana–Tiana oraz przejście od
wygaśnięcia do sumy spójnej sferycznych form przestrzennych i
$S^2\times S^1$. Własne lematy o cięciu sfery, grupie podstawowej
i $\pi_3$ zachowują potrzebne hipotezy. Twierdzenia Perelmana
o chirurgii, otoczeniach kanonicznych i wygasaniu są nadal
wyraźnie oznaczone jako zewnętrzne.

W rozdziale 32 ujednolicono termin „rozmaitość trójwymiarowa”
i poprawiono tytuł źródła cytującego twierdzenie Moise'a;
tę samą poprawkę wprowadzono do dodatku A. W rozdziale 33
zdefiniowano dysk ściskający i wskazano twierdzenie o pętli
Papakyriakopoulosa jako zewnętrzną podstawę jego równoważności
z nieinjektywnością $\pi_1(T^2)\to\pi_1(M)$. Opis rozdziału 31
poprawiono tak, aby nie przypisywał mu samodzielnego dowodu
istnienia potoku. Tabelę sześciu geometrii Seiferta porównano
z tablicą 4.1 Scotta, a sformułowanie rozkładu JSJ z wersją
geometryzacji dla orientowalnych, nierozkładalnych rozmaitości.
Uzupełniono indeks o centralne pojęcia trzech rozdziałów.
Pełny skład dał PDF-y o 212, 181 i 168 stronach. Logi nie
zawierają brakujących odsyłaczy ani przepełnionych wierszy;
indeksy przyjęły odpowiednio 112, 96 i 119 wpisów bez odrzuceń.
W tomie III potwierdzono łącza do PDF-ów tomów I i II oraz
obejrzano strony PDF 100 (rysunek 31.1), 113 i 121--122.

## Końcowy audyt Walla i ciągu chirurgii (2026-10-20)

Cały dopisany wykład w rozdziałach 27–28 porównano z oryginalnym
*Surgery on Compact Manifolds*, §§1–2, 5–6 i 10. Sprawdzono
hipotezy oraz progi wymiarowe przypadków parzystego i nieparzystego,
proste bazy i dualność nad $\Z[\pi]$, ruchy $T1$--$T4$,
lokalny efekt chirurgii środkowej, pięciowymiarową granicę
twierdzenia 6.4, realizację przez twierdzenia 5.8 i 6.5 oraz
dokładność ciągu zbiorów struktur.

W parzystym rachunku dualności poprawiono wzór
$[p]\mapsto(a\mapsto\lambda(p,\partial a))$ na
$[p]\mapsto(a\mapsto\lambda(\partial a,p))$.
Pierwszy nie był liniowy przy przyjętej konwencji lewych modułów;
drugi zgadza się z wcześniejszym wyprowadzeniem względnym.
Zamieniono także błędne określenie „samoprzecięcia zanurzonej
sfery” na „samoprzecięcia obramowanej immersji sfery”,
doprecyzowano pełne hipotezy lematu 5.7 i racjonalne jądro
użyte do rachunku sygnatury. W podsumowaniu przykładów
oddzielono algebraiczną formę od jej ewentualnej realizacji
jako jądra mapy normalnej. Nie stwierdzono dalszych błędów
podważających kryterium Walla ani ciąg chirurgii. Przyjęte
przez autora głębokie lematy Walla, wersja $h$ i ciąg
Rothenberga pozostają jawnie zewnętrznymi wynikami.
Pełny skład trzech tomów i indeksów zakończył się powodzeniem;
odsyłacze między tomami ustabilizowały się, a w PDF tomu III
potwierdzono łącza do tomów I i II. Logi nie zgłaszają brakujących
odsyłaczy ani przepełnionych wierszy. Indeksy przyjęły odpowiednio
112, 96 i 111 haseł bez odrzuceń. Zmienione strony 47, 64--65,
72 i 77 tomu III sprawdzono wizualnie.

## Klasyfikacja sfer siedmiowymiarowych (2026-10-20)

Do rozdziału 30 dopisano dwa twierdzenia przy jawnych wejściach
zewnętrznych: zupełności niezmiennika $\mu$ Eellsa--Kuipera dla
zorientowanych gładkich sfer homotopijnych wymiaru siedem oraz
$\Theta_7=bP_8\cong\Z/28$ Kervaire'a--Milnora. Z obliczonego wcześniej
$\mu(M_k)=(k^2-1)/224$ wyprowadzono kryterium
$M_k\cong M_l$ z zachowaniem orientacji dokładnie wtedy, gdy
$k^2\equiv l^2\pmod{224}$. Rachunek liczby trójkątnej modulo $4$ i $7$
daje dokładnie 16 zorientowanych klas wiązkowych. Addytywność $\mu$
pokazuje, że sumy spójne $r$ kopii $M_3$ mają wartości $r/28$;
zewnętrzna liczba klas daje pełną listę 28 klas zorientowanych.
Inwolucja zmiany orientacji ma dwie klasy stałe i 13 par,
czyli 15 klas bez orientacji. Oryginalne twierdzenia o zupełności
i rzędzie grupy pozostają wyraźnie nazwanymi wynikami zewnętrznymi,
a nie częścią własnego dowodu rozdziału.
Pełny skład trzech tomów i indeksów zakończył się powodzeniem.
Logi nie zgłaszają brakujących odsyłaczy ani przepełnionych wierszy;
indeksy przyjęły odpowiednio 112, 96 i 111 haseł bez odrzuceń.
Nową klasyfikację na stronach 95--96 tomu III sprawdzono wizualnie.

## Pełny audyt rozdziału 29 i klasyfikacji Bardena (2026-10-20)

Sprawdzono cały rozdział: klasyfikację powierzchni, argumenty
pięcio- i wyższowymiarowe oraz oba twierdzenia Bardena 2.2 i 2.3
z lematami 3.1 i 4.1--4.4, indukcją oraz modelami $M_k,X_j$.
Główną sekcję porównano z oryginalnym artykułem Bardena;
rachunek macierzy modeli i zakres użytego twierdzenia Walla
o dyfeomorfizmach czterowymiarowych sprawdzono osobno.
W opisie normalnej bazy formy wiązania uzupełniono pominiętą
mieszaną parę rzędów $q,2q$, doprecyzowano hipotezy lematu 4.4
i zakres czterowymiarowego wejścia. Przy wniosku dla $S^5$ jawnie
wybrano orientację, a triangulację powierzchni topologicznych
uzasadniono przez wygładzalność Hatcherowską i wynik Cairnsa.
Nie znaleziono błędu podważającego klasyfikację; wyniki głębokie
Thoma, Nowikowa, Walla, Haefligera, Milnora, Whiteheada i Smale'a
pozostają cytowanymi wejściami zewnętrznymi.
Pełny skład trzech tomów i indeksów zakończył się powodzeniem.
Logi nie zgłaszają brakujących odsyłaczy ani przepełnionych wierszy;
indeksy przyjęły odpowiednio 112, 96 i 111 haseł bez odrzuceń.
Poprawiony opis formy wiązania na stronie 82 tomu III sprawdzono wizualnie.

## Chirurgia na jednej sferze w dowodzie Walla (2026-10-20)

Rozpisano lokalny efekt pojedynczej chirurgii w nieparzystym wymiarze:
$S^k\times D^{k+1}$ zostaje zastąpione przez $D^{k+1}\times S^k$,
podczas gdy dopełnienie $M_0$ i jego strzałka brzegowa pozostają te same.
W starym module hiperbolicznym lagranżjan rurki zmienia pierwszy
generator z $e_1$ na $f_1$, a lagranżjan dopełnienia pozostaje $L_1$.
Jawna identyfikacja nowych współrzędnych przez $\sigma_1^{-1}$ daje
$\alpha'=\sigma_1\alpha$ przy przyjętej konwencji składania. Ustalono
też rolę znaku dla nieparzystego $k$. Rachunek porównano z dowodem
lematu 6.1 Walla; przygotowanie całego kobordyzmu i kryterium zera
pozostają wskazanymi w tekście wynikami zewnętrznymi.
Pełny skład trzech tomów i indeksów zakończył się powodzeniem.
Logi nie zgłaszają brakujących odsyłaczy ani przepełnionych wierszy;
indeksy przyjęły odpowiednio 112, 96 i 111 haseł bez odrzuceń.
Strony 71--72 tomu III, obejmujące nowy lemat i dalszy argument,
sprawdzono wizualnie.

## Ruchy T2--T4 Walla w rozdziale 27 (2026-10-20)

Po lokalnym rachunku ruchu T1 dopisano dowód algebraicznego efektu
ruchów T2--T4. Z definicji $H(B)$ wyprowadzono działanie na bazie
dualnej, w tym poprawkę $f_2\mapsto f_2-f_1$ dla sumy generatorów
oraz czynnik $(\bar u)^{-1}$ dla zmiany drogi i orientacji. Sprawdzono
parowania hiperboliczne i prostotę trzech typów macierzy. Rachunek
porównano z §6 Walla; geometryczna realizacja dyfeomorfizmu
pogrubionego układu rurek w ruchu T4 pozostaje jawnym wynikiem
zewnętrznym wskazanym tam przez Walla jako [W8, s.~272].
Pełny skład trzech tomów zakończył się powodzeniem. Logi nie wykazały
brakujących odsyłaczy ani przepełnionych wierszy; indeksy przyjęły
odpowiednio 112, 96 i 111 haseł bez odrzuceń. Strony 70--71 tomu III
z nowym lematem sprawdzono wizualnie.

## Rozdział 2, linie 93–153 — krzywa reprezentująca wektor (2026-10-20)

Sprawdzono wyprowadzenie $X_p(f)$ przez krzywą w mapie z definicją
klas krzywych z rozdziału 1. Otwartość obrazu mapy zapewnia istnienie
krzywej dla małych dodatnich i ujemnych czasów; reguła łańcucha
daje lokalny wzór na derywację. Doprecyzowano, że ten sam rachunek
działa dla każdego reprezentanta o klasie $X_p$, oraz wskazano
wcześniejszy dowód niezależności tej klasy od mapy.
Pełny skład trzech tomów i indeksów zakończył się powodzeniem.
Odsyłacze między tomami ustabilizowały się; logi nie zgłaszają
niewyjaśnionych odsyłaczy, a indeksy mają odpowiednio 112, 96 i 111
przyjętych haseł oraz po `0 rejected`. Stronę 62 tomu I z nowym
wyprowadzeniem sprawdzono wizualnie.

## Przykład pola stycznego do okręgów w rozdziale 2 (2026-10-15)

Do przykładu $X=-v\partial_u+u\partial_v$ dodano rachunek na okręgu
$S_r^1$ w lokalnej mapie kątowej. Pokazano, że $X^1=1$ oraz
$(f|_{S_r^1})\circ\varphi^{-1}=r^2$ dla $f(u,v)=u^2+v^2$,
stąd $X(f|_{S_r^1})=0$. Rachunek $X(u|_{S_r^1})=-r\sin t$
pokazuje, że zerowanie pochodnej tej funkcji nie oznacza znikania pola.
Przy przykładzie pola na sferze dodano rozróżnienie między rachunkiem
w mapie rozmaitości a wykorzystaniem współrzędnych otaczającej
$\R^N$ dla podrozmaitości. Wskazano, jak sprawdza się styczność
bez mapy oraz dlaczego pochodna funkcji na podrozmaitości,
obliczona przez lokalne przedłużenie, od niego nie zależy.
Pełny skład trzech tomów zakończył się powodzeniem; logi nie zawierają
nierozwiązanych odsyłaczy, a wszystkie trzy indeksy mają `0 rejected`.
Tekst nowego przykładu i uwagi sprawdzono w PDF tomu I.
Uwagę i przykład sfery doprecyzowano na prośbę autora: w przykładzie
sprawdzamy styczność pola bez różniczkowania funkcji; $x,y,z$ są
ograniczeniami współrzędnych $\R^3$, a $X_p=(-y,x,0)$ jest
gładkim, stycznym wektorem dla każdego $p\in S^2$. Wskazano również
lokalny zapis w mapie górnej półsfery.
Po tym doprecyzowaniu tom I złożono dwukrotnie w `build/tomy`;
log nie zgłasza nierozwiązanych odsyłaczy. PDF-u w katalogu głównym
nie nadpisywano, ponieważ miał równoległe zmiany użytkownika.

## Różniczka i zapis rozdziału 1 (2026-10-15)

Do definicji różniczki odwzorowania dodano równoważny opis przez
prędkości krzywych: $dF_p(\gamma'(0))=(F\circ\gamma)'(0)$.
W przykładzie grupy ortogonalnej wskazano krzywą $A+tH$ w przestrzeni
macierzy, która daje użyty rachunek. Treść wcześniejszych dowodów
i przykładów zachowano. W całym rozdziale 1 zamieniono 278 krótkich
bloków matematycznych na zapis w tekście, bez zmiany ich treści.
Uzasadniono niezależność różniczki od krzywej reprezentującej wektor
styczny przez porównanie działania otrzymanych derywacji na funkcjach.
W 53 wystąpieniach matematyki w tekście zamieniono `\qquad` na `\ `.
Na prośbę autora nie wykonywano składu PDF w tej iteracji.

## Podział na trzy tomy (2026-10-13)

Zachowano wspólne źródła rozdziałów i nie zmieniono ich numeracji ani etykiet.
Tom I obejmuje rozdziały 1–10, tom II rozdziały 11–22, a tom III rozdziały
23–38 oraz dodatki. Każdy tom ma własny spis treści i indeks. Pakiet
`xr-hyper` oraz pliki pomocnicze pozostałych tomów zapewniają odsyłacze
między trzema plikami PDF. Skrypt `buduj_tomy.ps1` wykonuje kolejne przebiegi,
aż ustalą się etykiety zewnętrzne. Plik zbiorczy pozostaje dostępnym
wariantem składu. W dodatku B przywrócono etykietę rozdziału do nagłówka
rozdziału, aby istniejące odsyłacze nadal wskazywały właściwe miejsce.
Sprawdzony skład ma odpowiednio 208, 172 i 146 stron. Ostatnie logi nie
zgłaszają nierozwiązanych odsyłaczy; indeksy przyjęły 112, 89 i 111 haseł
bez odrzuceń. Na stronach tytułowych sprawdzono po dwa odsyłacze do innych
plików PDF oraz wygląd mapy tomów.

## Uzupełnienie rozdziału 1 — kowektory (2026-10-12)

W nienumerowanej podsekcji przestrzeni kostycznej wyprowadzono zmianę
bazy dualnej bezpośrednio z reguły transformacji derywacji
`eq:transformacja-derywacji`: różniczki współrzędnych zmieniają
się przez macierz Jacobiego, a współczynniki tego samego kowektora
przez jej odwrotną transpozycję. Rachunek sprawdza ewaluację na bazie
stycznej; przykład liniowej zmiany map w $\R^2$ kontroluje znaki.
W konstrukcji $T^*M$ zastąpiono skrót „analogicznie” jawnym wzorem
odwzorowania przejścia i argumentem jego gładkości. Uzupełnienie nie
stanowi ponownego audytu całej rozbudowanej sekcji o wiązkach.
Pełny skład z 13 października: 522 strony; ostatni log bez błędów
i nierozwiązanych odsyłaczy, indeks 312 haseł bez odrzuceń.
Sprawdzono wygląd stron 46 i 56 z nowymi wzorami oraz konstrukcją $T^*M$.

## Iteracja 16 — Egzotyczne struktury gładkie na R⁴

Status: rozdział 35 doprecyzowano i ujednolicono z resztą konstrukcji Gompfa.
Data: 2026-10-12. Źródło: `tex/rozdzialy/35-egzotyczne-r4.tex`.

1. **Suma przy końcu i indukcja.** Uściślono, że w konstrukcji wystarczy
   jeden konkretny model sumy przy końcu, w którym obie wybrane rozłączne
   zwarte części pozostają rozdzielone, a orientacja jest zachowana.
   To odpowiada rzeczywistemu potrzebnemu kroki indukcji, bez rozbudowanego
   dowodu niezależności od wyboru łuku i promieni.
2. **Spójność argumentu.** Wzmocniono komentarz przy przejściu od zewnętrznej
   konstrukcji do indukcji Gompfa, aby czytelnik widział, gdzie wchodzą
   twierdzenia o zanurzeniach i gdzie kończy się sama algebraiczna przeszkoda.
3. **Kontrola odwołań.** Wersja tekstu nadal odwołuje się do tych samych
   wyników zewnętrznych i etykiet, a dodatkowy komentarz nie wprowadza nowych
   symboli ani konfliktów z wcześniejszą notacją.

## Iteracja 1 — Rozmaitości różniczkowe

Status: sprawdzono i poprawiono wszystkie 11 sekcji oraz 15 ilustracji.
Data: 2026-09-30. Źródło bazowe: pierwotny `origin/main` pobrany w tej iteracji.

### 1.1. Rozmaitości topologiczne

1. **Niezmienniczość wymiaru a niezmienniczość obszaru.** Tekst utożsamiał
   nazwy dwóch twierdzeń. Podano właściwą treść twierdzenia Brouwera i wyprowadzono
   z niej niezmienniczość wymiaru przez dołączenie zer. Obraz w podprzestrzeni
   niższego wymiaru nie może być otwarty w przestrzeni wyższego wymiaru.
   Doprecyzowano wyjątek pustej rozmaitości.
2. **Metryzowalność i parazwartość.** Rozpisano ciąg przesłanek:
   lokalna zwartość + Hausdorff → regularność; przeliczalna baza + regularność
   → metryzacja Urysohna; metryzowalność → parazwartość. Są to jawnie
   przyjęte twierdzenia topologii ogólnej. Usunięto błędną sugestię, że lokalna
   funkcja odcinająca wymaga rozkładu jedności, który dopiero z takich funkcji się buduje.

### 1.2. Atlasy i rozmaitości gładkie

3. Sprawdzono zgodność map, równoważność atlasów, maksymalizację atlasu
   i przykład struktury określonej przez x³. Dowody zasadniczo poprawne;
   różność struktur na ustalonym zbiorze nie oznacza braku dyfeomorfizmu.

### 1.3. Rozmaitości zespolone

4. **Holomorficzność implikuje gładkość.** Zastąpiono niepełne odwołanie
   do równań Cauchy’ego–Riemanna argumentem z lokalnej analityczności,
   wynikającej ze wzoru całkowego Cauchy’ego na polidysku.
5. **Sfera Riemanna.** Rzeczywiste rzuty z dalszego przykładu mają przejście
   z/|z|² = 1/conj(z), a nie 1/z. Odwrócono drugą współrzędną w mapie
   południowej; wtedy przejście jest holomorficzne. Dodano jawny wzór
   CP¹ → S², sprawdzenie niezależności od reprezentanta, obrazu na sferze,
   bijektywności i gładkości obu kierunków. Rysunek otrzymał zgodne oznaczenia
   ζ_N, ζ_S i objaśnienie dziedziny przejścia.

### 1.4. Odwzorowania gładkie

6. **Gładkość w punkcie.** Doprecyzowano, że chodzi o gładkość na otwartym
   otoczeniu współrzędnych punktu. Rozpisano wynikającą z definicji ciągłość
   i możliwość zmniejszenia dziedzin przy zmianie map.

### 1.5. Przykłady rozmaitości

7. **Przestrzenie rzutowe.** Uzupełniono dowód ciągłości map ilorazowych:
   współrzędne schodzą z ciągłych ilorazów, a odwrotność wstawia 1
   i przechodzi do klasy. Oddzielono budowę map od późniejszego sprawdzenia
   aksjomatów Hausdorffa i przeliczalności. Poprawiono „nadającym struktury”.
8. **Torus jako iloraz.** Brakowało sprawdzenia Hausdorffa i drugiej
   przeliczalności. Rozłączne otoczenia skonstruowano z dodatniej odległości
   różnicy reprezentantów od kraty; bazę uzyskano przez otwarte rzutowanie
   przeliczalnej bazy Rⁿ.

### 1.6–1.7. Przestrzeń styczna i kostyczna

9. **Przedłużanie funkcji odcinającej przez zero.** Wymagamy zawierania
   całej domkniętej kuli w obrazie mapy. Zwarty nośnik leży wewnątrz mapy
   i jest domknięty w M; pokrycie U oraz M poza nośnikiem uzasadnia gładkość
   przedłużenia, której samo uzgodnienie wartości nie wystarczało dowieść.
10. **Błąd dziedziny we współrzędnych.** W dowodzie izomorfizmu przestrzeni
    stycznych zastąpiono niedozwolone złożenie xⁱ∘φ przez xⁱ = φⁱ.
    Funkcje xⁱ zostały wcześniej zdefiniowane na M, nie na Rⁿ.
    Jawnie dobrano funkcję odcinającą w bieżącej mapie.
11. Sprawdzono trzy definicje przestrzeni stycznej, lemat Hadamarda,
    lokalność derywacji, bazę współrzędnościową i dualną oraz wzór na df.

### 1.8–1.9. Wiązki i funkcje przejścia

12. **Terminologia.** Obraz całej wiązki nie jest jej „przekrojem”;
    zmieniono podpis rysunku. Dodano równoważne terminy „sekcja” i „przekrój”,
    definicję izomorfizmu wiązek oraz uzasadnienie gładkości przekroju zerowego.
13. **Trywializacja Möbiusa przy sklejeniu.** Dotychczas opisano wyłącznie
    łuki omijające sklejenie. Dodano trywializację z ujemnym kątem i zmianą
    znaku we włóknie oraz sprawdzenie przejść i aksjomatów topologicznych.
14. **Przekroje ciągłe i gładkie.** Warunek f(2π) = −f(0) zapewnia jedynie
    ciągły przekrój. Dla gładkości trzeba zgodności wszystkich pochodnych
    z tym samym znakiem. Dodano też odwrotny kierunek korespondencji,
    niezbędny w dowodzie nietrywialności.
15. **Brzeg wstęgi Möbiusa — błąd rzeczowy.** Cała wiązka z włóknem R
    nie ma brzegu. Zwarty pas |t| ≤ c ma brzeg, ale jego włókna są odcinkami,
    więc nie jest wiązką wektorową. Doprecyzowano też ograniczenie parametru
    w modelu narysowanym w R³ i jedną składową brzegu zwartego pasa.
16. **Topologia TM i sklejanej wiązki.** Zbiór z bijekcjami współrzędnych
    nie jest jeszcze rozmaitością. Dodano definicję topologii i uzasadnienie,
    że dziedziny są otwarte, mapy są homeomorfizmami, a rzutowanie ciągłe.
    Poprawiono kolejność złożenia definiującego trywializację TM.
17. **Warunek kocyklu.** Poprawiono „kokykl” oraz objaśnienie:
    porównujemy bezpośrednią zmianę współrzędnych z jej złożeniem przez trzecią mapę.

### 1.10. Różniczka i rząd

18. **Niewymierne nawinięcie torusa.** Sama wzmianka o gęstości nie była
    uzasadnieniem nieciągłości odwrotności. Dodano dowód injektywności,
    immersyjności, ciąg powracających punktów z zasady szufladkowej i dowód
    gęstości przez małe niezerowe wielokrotności α modulo 1.
19. **Twierdzenie o rzędzie stałym.** Oddzielnie obsłużono rząd zero.
    Znikanie pochodnych w kierunkach włókna przekłada się na niezależność
    od tych zmiennych po ograniczeniu do produktu kul; dodano całkę
    wzdłuż odcinka, która uzasadnia ten krok.

### 1.11. Podrozmaitości

20. **Obraz zanurzenia.** Postać lokalna u ↦ (u,0) nie daje automatycznie
    równości obrazu z całym plasterkiem w dowolnie dobranej mapie celu.
    Dodano dobór produktu kul i odpowiednie zmniejszenie obu map przed
    zastosowaniem homeomorficzności na obraz.
21. Sprawdzono dowód struktury podrozmaitości, przeciwobrazu wartości
    regularnej, identyfikacji przestrzeni stycznej z jądrem oraz rachunki
    dla sfery, O(n) i torusa obrotowego.

### Dalsze doprecyzowania z tej samej iteracji

22. **Rzut stereograficzny — nowy rysunek.** Zastąpiono rzut na płaszczyznę
    styczną w biegunie południowym dokładnym przekrojem rzutu na płaszczyznę
    równikową, czyli tę z definicji. Usuwa to konieczność pamiętania o czynniku 2.
    Współrzędne rysunkowe N=(0,1), x=(3/5,4/5), P=(3,0) spełniają
    równanie okręgu, współliniowość i wzór P=x₁/(1−x₂).
23. **Kolejność wprowadzania pojęć.** Przeniesiono przykład wiązki normalnej
    za definicję podrozmaitości i dowód jej struktury. Poprzednio używał
    niezdefiniowanej mapy plasterkowej. Jawnie wskazano identyfikację TS
    przez różniczkę inkluzji.
24. **Druga przeliczalność.** Dodano prosty kontrprzykład: nieprzeliczalną
    sumę rozłączną prostych. Długa prosta pozostaje przykładem spójnym;
    nie jest już potrzebna do uzasadnienia niezależności aksjomatów.
25. **RP¹ i wiązka tautologiczna.** Dodano dowód identyfikacji RP¹ z S¹
    przez z ↦ z² oraz jawny izomorfizm wiązki Möbiusa z tautologiczną,
    używający wektora (cos(θ/2), sin(θ/2)). Sprawdzono sklejenie
    i gładką odwrotność w lokalnych trywializacjach.
26. **Metryka na przestrzeni rzutowej.** Dodano ciągłość rzutowania
    z przestrzeni bez zera przez normalizację. Wcześniejsze przejście
    od ciągłości na sferze do zgodności z pierwotną topologią ilorazową
    pomijało właśnie ten krok.
27. **Drobne doprecyzowania.** Ustalono konwencję rozmaitości bez brzegu,
    dodano brakujące dim M=n w twierdzeniu o poziomicy, ujednolicono
    „surjektywność”, poprawiono zapis mapy jako pary (U,φ) z osobno
    podanymi współrzędnymi i gramatykę zdania o bazie dualnej.
28. **Rysunek przestrzeni stycznej.** Kontrola PDF wykazała sztuczny
    trójkąt wypełnienia poza obrysem powierzchni. Zbudowano jeden ciągły
    obrys z tej samej parametryzacji co siatka: S(u,v)=(u,v,0.12u²+0.08v²).
    Rzut (x,y,z) ↦ (x+0.45y,0.65y+z) i mniejsza krzywizna dają czytelny
    obraz bez nakładania się siatki. Płaszczyzna styczna w zerze to z=0,
    krzywa γ(t)=(t,0,0.12t²) leży na powierzchni i ma styczną (1,0,0).
29. **Pliki pomocnicze.** Dodano `.gitignore` dla katalogu `build/`
    i produktów pośrednich LaTeX. PDF pozostaje śledzony i zostanie
    zaktualizowany razem ze źródłem. Skrypty robocze i podglądy nie trafiają do repozytorium.
    Dodano też `.gitattributes` z `*.pdf binary`, aby Git nie traktował
    zawartości PDF jako tekstu przy kontroli białych znaków i zmian końców linii.
30. **Domknięcie argumentów lokalnych.** Rozpisano blokową różniczkę
    przejść map plasterkowych: dolny lewy blok jest zerowy, a odwracalny
    dolny prawy blok wyznacza przejścia wiązki normalnej i spełnia warunek
    kocyklu. Dopisano otwartość rzutowania przestrzeni rzutowej przez sumę
    dylatacji. Przy dxⁱ doprecyzowano przedłużanie funkcji zgodnej jedynie
    blisko punktu, zamiast sugerować możliwość przedłużenia dowolnej
    funkcji z całej dziedziny mapy.

### Kontrola i materiały pomocnicze

- Kontrola rachunków i logicznych zależności: bezpośrednio ze źródła LaTeX.
- Sprawdzenia symboliczne (SymPy): wzór CP¹ → S² i obie mapy zespolone,
  Jacobian przejścia w RP² oraz dokładna geometria nowego rzutu stereograficznego — poprawne.
- Porównanie źródeł z bazowym commitem: treść rozdziałów 2–18 niezmieniona.
- Kontrola zbilansowania środowisk LaTeX w rozdziale 1 oraz `git diff --check` — poprawne.
- Rozróżnienie twierdzeń Brouwera porównano z pierwotnym artykułem
  [Takayukiego Kihary](https://www.math.mi.i.nagoya-u.ac.jp/~kihara/pdf/paper/invariance.pdf), twierdzenie 1.1.
- Punkt odniesienia dla konwencji rozmaitości:
  [John M. Lee, Introduction to Smooth Manifolds, strona autora i errata](https://sites.math.washington.edu/~lee/Books/ISM/).
- Kontrola wizualna: obejrzano strony 4–35 PDF, w tym wszystkie 15 ilustracji
  rozdziału 1. Ponownie sprawdzono strony po zmianach wypełnienia powierzchni
  stycznej i końcowych uzupełnieniach tekstu.
- Kompilacja: pełny dokument, pdfLaTeX z lokalnego MiKTeX Portable;
  ponawiana do ustabilizowania odsyłaczy. Nie ma błędów LaTeX, niezdefiniowanych
  odsyłaczy ani przepełnionych wierszy (`Overfull`). Pozostają cztery ostrzeżenia
  `Underfull` w dalszych, jeszcze nieprzejrzanych rozdziałach i automatyczne
  dopuszczenie położenia `ht` dla dwóch rysunków zadanych jako `h`.
  MiKTeX emituje dodatkowo komunikat administracyjny o niesprawdzonych
  aktualizacjach; nie przerywa on poprawnej kompilacji.

Polecenie odtworzenia PDF (utworzyć wcześniej katalog `build` i uruchamiać,
aż zniknie komunikat o konieczności ponownego przeliczenia odsyłaczy):

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build geometria_i_topologia_rozniczkowa.tex
```

Źródło i wynikowy PDF należą do tego samego commita przeglądu rozdziału 1.

## Iteracja 2 — Pola wektorowe, przepływy i pochodna Liego

Status: sprawdzono i poprawiono wszystkie 7 sekcji oraz 4 ilustracje.
Data: 2026-10-01. Baza rozpoczęcia pracy: `e144985` (ukończony rozdział 1).
Przed publikacją pobrano i zachowano zdalne commity `5043a70` i `dc53c6b`,
rozwijające przykład 1.1.6. Poprawki rozdziału 2 nałożono na `dc53c6b`;
konflikt binarnego PDF rozwiązano przez ponowną kompilację wspólnego źródła.

1. **Konwencje i terminologia.** Ujednolicono „infinitezymalny” oraz
   „zupełny/zupełność” w odniesieniu do pól. Określono konwencję rozmaitości
   bez brzegu i znaczenie gładkości w półprzestrzeniach, potrzebne na końcu
   rozdziału. Przedział krzywej całkowej jest otwarty.
2. **Derywacje globalne.** W konstrukcji współczynników pola wybiera się
   kulę we współrzędnych o zwartym domknięciu w dziedzinie mapy. Dzięki temu
   funkcja odcinająca wynika bezpośrednio z konstrukcji w rozdziale 1.
3. **Pola wzdłuż odwzorowania.** Zdefiniowano wiązkę cofniętą F*TN i jej
   lokalne trywializacje. Wyjaśniono, dlaczego dla ogólnego F nie powstaje
   automatycznie pole na N; odróżniono je od przenoszenia przez dyfeomorfizm.
   Przy nietrywialności TS² dodano odsyłacz do późniejszego uzasadnienia.
4. **Nawias Liego.** Dodano wyprowadzenie współczynników przez działanie
   na współrzędne lokalne i wyjaśnienie sumowania powtarzających się indeksów.
5. **Frobenius.** Uściślono definicję rozkładu, treść twierdzenia w mapach
   i konieczność inwolutywności; sprawdzono kontrprzykład w R³. Dodano dowód
   wystarczalności przez indukcję po rzędzie: prostowanie jednego pola,
   macierzowe równanie Q′=−AQ usuwające zależność bazy od tego czasu
   i zastosowanie indukcji na przekroju. Umieszczono go dopiero po twierdzeniu
   o prostowaniu, na którym się opiera.
6. **Gładka zależność rozwiązań.** Rozpisano oszacowanie różnic rozwiązań
   równania wariacyjnego i ciągłość pierwszej pochodnej. Przy kolejnych
   pochodnych wskazano równanie liniowe dla nieznanej pochodnej, kontrolę
   reszty Taylora i krok indukcyjny; samo formalne różniczkowanie nie dowodzi
   wcześniej istnienia tych pochodnych. Pochodne mieszane wynikają z równania.
7. **Zmiana parametryzacji.** Podano całkę definiującą nowy czas dla Y=fX,
   f>0, i argument zgodności maksymalnych orbit w obu kierunkach. Przykład
   ∂x oraz (1+x²)∂x pokazuje, że zupełność nie jest zachowywana.
8. **Prostowanie pola.** Skonstruowano przekrój poprzeczny w mapie, wybrano
   produktową dziedzinę i wyprowadzono postać przepływu z prawa grupowego.
9. **Niezmienniczość i komutowanie.** Uzupełniono dowód równoważności trzech
   warunków, w tym zgodność maksymalnych przedziałów pola Y po działaniu
   zupełnego przepływu X. Dodano osobny dowód wzoru
   d/dt Φt*Y = Φt*[X,Y], z jawnym odsyłaczem w miejscu użycia.
10. **Pierwsza całka obrotu.** Poziomice dodatnie są okręgami, zerowa jest
    punktem stałym, ujemne są puste; pierwotne zdanie pomijało te wyjątki.
11. **Komutator przepływów.** Przeniesiono rysunek i rachunek za definicję
    przepływu oraz pochodnej Liego. Rozpisano wszystkie cztery rozwinięcia
    Taylora do rzędu drugiego, aby uzasadnić znak nawiasu dla dowolnych pól.
    Podpis nie nazywa już składnika t² pierwszym niezerowym przy zerowym nawiasie.
12. **Rysunek przesuwania przekroju.** Końce obu odcinków poprzecznych mają
    teraz identyczny zakres niezmiennika y−A sin(κx). Wcześniej były dobierane
    przybliżeniowo i nie stanowiły dokładnego obrazu przez ten przepływ.
    Podano rzeczywiste stałe rysunku i dokładny wzór przepływu.
13. **Pola zależne od czasu.** Wymagana jest łączna gładkość w (t,p).
    Podniesienie do ∂t+Xt uzasadnia gładką zależność od obu czasów i punktu.
    Wskazano dziedziny praw ewolucji i dowód istnienia na całym [0,1]
    przy wspólnym zwartym nośniku, także przy końcach przedziału czasu.
14. **Generator izotopii.** Dodano dowód łącznej gładkości odwrotności ht⁻¹
    przez odwzorowanie (t,p)↦(t,ht(p)). Doprecyzowano „osadzenie”
    i zdefiniowano nośnik całej izotopii.
15. **Ślad izotopii.** To podrozmaitość z brzegiem, nie bez brzegu.
    Skonstruowano mapy zachowujące czas, które prostują ślad również
    w chwilach 0 i 1; nie stosuje się bez wyjaśnienia twierdzenia bez brzegu.
16. **Przedłużenie prędkości izotopii.** Uściślono lokalne nośniki i zbiór U,
    na którym suma funkcji odcinających jest dodatnia. Końcowa funkcja
    odcinająca musi mieć nośnik wewnątrz U, a nie jedynie w dużym otoczeniu O:
    inaczej wcześniejszy wzór dzieliłby przez zero. Podano konstrukcję funkcji
    odcinającej i wspólnego zwartego nośnika przez rzut na M.
17. **Kołnierz brzegu.** Uzasadniono konstrukcję pola skierowanego do wnętrza
    i lokalną odwracalność w półotoczeniach. Dodano argument ciągowy ze
    zwartości, który zamienia lokalną injektywność w globalną dla wspólnego
    małego czasu. Samo twierdzenie o funkcji odwrotnej tego nie zapewnia.
18. **Doprecyzowania po kontroli.** Uzasadniono konieczność i lokalną
    wystarczalność styczności do brzegu dla przepływu dwustronnego.
    Odróżniono lokalne prawo grupowe od globalnej grupy przy polu zupełnym.
    W zmianie parametryzacji dopisano argument zachowania maksymalności.
    Podpis pola obrotowego ujawnia wspólną skalę strzałek (0,22), a wektor
    t²[X,Y] na schemacie komutatora ma teraz dokładnie długość pionowej
    różnicy między początkiem i końcem. Użyto terminu „przekrój poprzeczny”.

### Kontrola iteracji 2

- Przeczytano cały rozdział, sprawdzając definicje, rachunki, dowody
  i kolejność zależności. Nowe dowody korzystają z wcześniej wykazanych
  faktów; późniejsze użycia są oznaczone odsyłaczami.
- Weryfikacja symboliczna w SymPy: znak komutatora dla pary nieliniowych
  pól na płaszczyźnie, rozwiązania obrotu, x′=x², x′=1+x² oraz niezmiennik
  i pochodna przepływu z rysunku przekrojów — poprawne.
- Porównanie ze źródłem w `dc53c6b` po integracji zdalnych zmian:
  rozdział 1 i rozdziały 3–18 pozostały niezmienione przez tę iterację.
  Środowiska LaTeX są zbilansowane, wszystkie
  odsyłacze rozdziału mają cele, brak powtórzonych etykiet.
- Jako zewnętrzny punkt odniesienia dla lokalnej postaci twierdzenia
  Frobeniusa wykorzystano twierdzenie 14.5 w
  [J. M. Lee, Introduction to Smooth Manifolds, wersja robocza 3.0](https://www.math.colostate.edu/~renzo/teaching/DiffGeo2011/Introduction%20to%20Smooth%20Manifolds%20-%20J.%20Lee.pdf),
  s. 359 (strona 371 pliku PDF). Numeracja dotyczy tej wersji,
  nie drugiego wydania wymienionego w bibliografii skryptu.
- Kontrola wizualna całego rozdziału: strony 36–51 PDF; wszystkie cztery
  ilustracje obejrzano również w większej rozdzielczości (strony 42, 44,
  47, 49). Opisy, kierunki strzałek i wzajemne położenia są czytelne.
- Pełna kompilacja pdfLaTeX: 275 stron, bez błędów, niezdefiniowanych
  odsyłaczy i przepełnionych wierszy. Pozostały wcześniejsze cztery
  ostrzeżenia `Underfull` poza rozdziałem 2 oraz trzy automatyczne zmiany
  położenia rysunków `h` na `ht` po integracji zmian przykładu 1.1.6.
  Polecenie odtworzenia PDF podano wyżej.
- `git diff --check` poprawny. Źródło i zaktualizowany PDF publikowane razem.

## Iteracja 3 — Algebra tensorowa i zewnętrzna

Status: sprawdzono i poprawiono wszystkie 9 sekcji oraz sprawdzono 2 ilustracje.
Data: 2026-10-01. Baza: `9bfa3af`.

1. **Konstrukcja iloczynu tensorowego.** Poprawiono klasę x+R dla x∈F
   (wcześniejsze [x]+R niepotrzebnie wprowadzało drugi symbol klasy).
   Wskazano kombinacje liniowe klas generatorów i poprawiono gramatykę.
   Zaznaczono, że pomocnicza przestrzeń wolna jest na ogół nieskończenie
   wymiarowa mimo skończonych wymiarów V i W.
2. **Terminologia baz.** Eij nazwano jednostkami macierzowymi i podano ich
   elementy. „Macierz jednostkowa” oznacza zwykle macierz identycznościową,
   więc poprzednia nazwa była myląca. „Tuple” zastąpiono układami lub ciągami.
3. **Wiele czynników.** Dopisano uzasadnienie niezależności izomorfizmów
   od sposobu zmiany nawiasowania dla więcej niż trzech przestrzeni.
4. **Dualność i stopień zero.** Wyraźnie określono liniowość nad C bez
   sprzężenia, puste iloczyny, funkcje bez argumentów oraz T⁰₀(V)=K.
   Wyprowadzono zmianę bazy dualnej i macierzy operatora A⁻¹[S]A.
5. **Iloczyn mieszany.** Ustalono kanoniczne przestawienie bloków, które
   identyfikuje iloczyn tensorów typów (r,s), (r′,s′) z typem (r+r′,s+s′).
   Przestawienie nie wprowadza znaku. Podano porządek par dla macierzy Kroneckera.
6. **Kontrakcja.** Określono zakres indeksów, kolejność pozostałych czynników
   i wzór sumowania współczynników. Wcześniejszy opis pomijał te konwencje.
7. **Algebra tensorowa.** Zdefiniowano homomorfizm algebr z jedynką
   i element jednorodny. Uzasadniono dobre określenie mnożenia przez własność
   uniwersalną, przypadek skalarów i skończoność wyniku w sumie prostej.
8. **Symetryzacja.** Dopisano działanie permutacji z prawej strony
   symetryzatora i antysymetryzatora; jest ono używane w dowodzie zanikania
   ideału. Wyjaśniono, że rozkład Sym+Alt=id zachodzi w stopniu 2,
   i podano kontrprzykład dla stopnia 3.
9. **Algebra symetryczna.** Uzasadniono jednorodność ideału J i stopniowanie
   ilorazu. Doprecyzowano odwrotność izomorfizmu z obrazem symetryzatora,
   stopień zero i przestrzeń V=0, do której nie stosuje się podanego wzoru
   wymiaru dla n≥1. Ujednolicono termin „jednomian”.
10. **Alternowanie i znaki.** Wyprowadzono równoważność zerowania przy
    powtórzeniu argumentów ze zmianą znaku przy transpozycji (nad R lub C).
    Wyjaśniono, że ideał zewnętrzny nie ma w stopniach 0 i 1 elementów
    niezerowych. Poprawiono odmianę „odwzorowanie ilorazowe”.
11. **Potęgi odwzorowania i dualność zewnętrzna.** Osobno ustalono Λ⁰A=id,
    E₀=id oraz wyznacznik pustej macierzy. Zdefiniowano używaną przestrzeń
    Altᵏ(V;K) i wskazano zerowanie przy k>dim V.
12. **Normalizacje.** Poprawiono jₖ na j₂ przy iloczynie dwóch kowektorów.
    Dopisano ogólną relację Eₖ=k!jₖ po odczytaniu tensorów jako funkcji.
    Wyprowadzono czynnik (k+ℓ)!/(k!ℓ!) przed antysymetryzatorem dla form.
13. **Zmiana współrzędnych pola tensorowego.** Zamiast samej wzmianki
    dodano pełne prawo transformacji, wyprowadzone z reguły łańcucha
    osobno dla wektorów i kowektorów. Przykład y=x² pokazuje czynnik 1/(4y)
    dla dx⊗dx. Wyjaśniono, że wyznacznik różniczki między różnymi włóknami
    wymaga wyborów, choć sama najwyższa potęga zewnętrzna jest kanoniczna.
14. **Cofnięcie i pochodna Liego.** Dodano cofnięcie funkcji i regułę
    F*(fT)=(f∘F)F*T, uzasadniono gładkość cofnięcia i pochodnej Liego.
    Wyjaśniono, że wystarcza rozkład lokalny, bez założenia globalnej bazy.
    Poprawiono gramatykę dowodu kontrakcji; „koneksja (połączenie)”
    uzgadnia terminologię z dalszymi rozdziałami.
15. **Cauchy–Binet i lektura.** Doprecyzowano zakresy indeksów i nawiasy
    wokół podmacierzy AB. Wyjaśniono pustą sumę przy k>n i przypadek k=0.
    Dodano krótką bibliografię na końcu rozdziału, analogicznie do sąsiednich.
    W dowodzie własności wyznacznika poprawiono zgodę gramatyczną:
    „jedna z kolumn”, zamiast „jeden z nich”.

### Kontrola iteracji 3

- Przeczytano cały rozdział: konstrukcje ilorazowe i własności uniwersalne,
  bazy, operacje tensorowe, znaki, wyznacznik, wiązki i pochodną Liego.
- SymPy: sprawdzono relację między wyznacznikiem i antysymetryzacją
  w stopniach 1–4, współczynniki iloczynu form w stopniach (1,2), (2,1)
  i (2,2), wszystkie minory stopnia 2 w przykładzie Cauchy’ego–Bineta
  dla macierzy 3×4 i 4×3 oraz pole równoległoboku równe 5.
- Sprawdzono zgodność kontrakcji ze zmianą współrzędnych tensora (2,1).
  Niezależne różniczkowanie dokładnego cofnięcia przez przepływ ścinania
  Φt(x,y)=(x+ty,y) zgadza się ze wzorem współrzędnym pochodnej Liego
  we wszystkich ośmiu składowych zmiennego tensora (2,1).
- Zakres zmian porównany z `9bfa3af`: źródła rozdziałów 1–2 i 4–18
  są niezmienione. Środowiska LaTeX zbilansowane, brak powtórzonych etykiet
  i odsyłaczy bez celu. `git diff --check` poprawny.
- Zewnętrzny punkt odniesienia dla konstrukcji tensorowych i dualności:
  [B. Conrad, Tensor algebras, tensor pairings, and duality](https://math.stanford.edu/~conrad/diffgeomPage/handouts/tensor.pdf).
- Kontrola wizualna wszystkich 19 stron rozdziału (52–70 PDF).
  Diagram własności uniwersalnej (s. 52) oraz równoległobok (s. 64)
  obejrzano w większej rozdzielczości. Oba są poprawne i czytelne;
  ich geometria nie wymagała zmian.
- Pełny dokument kompiluje się do 277 stron. Brak błędów LaTeX,
  niezdefiniowanych odsyłaczy i ostrzeżeń `Overfull`. Pozostają wcześniejsze
  cztery ostrzeżenia `Underfull` w dalszych rozdziałach i trzy zmiany
  położenia rysunków `h` na `ht`. PDF aktualizowany razem ze źródłem.

## Iteracja 4 — Grassmanniany, algebra Clifforda i spinory

Punkt odniesienia: `02ea77d`. Przeczytano cały rozdział.

### Zmiany i uzasadnienia

1. **Atlas Grassmannianu.** Doprecyzowano zależność map od dopełnienia,
   wybór baz przy wyznacznikach i topologię określoną przez atlas.
   Uzupełniono model rzutów ortogonalnych: otwartość dziedzin map,
   identyfikację z idempotentami samosprzężonymi i dowód zwartości.
2. **Przestrzeń styczna i wiązki.** Dodano argument z lokalną ramką
   dla niezależności identyfikacji od reprezentującej krzywej,
   sprawdzenie różnowartościowości i gładkości izomorfizmu wiązek.
   Poprawiono zapis izomorfizmu wiązki ilorazowej z dopełnieniem
   ortogonalnym oraz odsyłacz do wcześniejszej definicji wiązki normalnej.
3. **Modele jednorodne i Plücker.** Podano lokalne sekcje z procedury
   Grama–Schmidta i lokalną strukturę iloczynową ilorazu grupowego.
   W dowodzie zanurzenia Plückera ilorazy współrzędnych przedłużono
   na otwarte podzbiory przestrzeni otaczającej, co rzeczywiście daje
   lewą odwrotność różniczki. Uzasadniono gładkość modelu z normalnymi.
4. **Algebra Clifforda.** Poprawiono porównanie z algebrą zewnętrzną:
   teraz oba kwadraty dotyczą tego samego wektora. Zdefiniowano
   automorfizm parzystości i rewersję, dowodząc, że przechodzą na iloraz.
   Rewersja jest niezbędna w późniejszym dowodzie jądra nakrycia Spin.
5. **Grupa Spin.** Uzupełniono przejście od lokalnych podniesień obrotów
   do gładkiej struktury grupy i gładkości jej działań. W wymiarze 3
   wyjaśniono, dlaczego każdy jednostkowy biwektor jest iloczynem
   dwóch ortogonalnych wektorów jednostkowych.
6. **Moduły i chiralność.** Doprecyzowano dwuliniowość działania,
   niezerowość modułu nieredukowalnego oraz zależność operatora
   chiralności od orientacji. Dodano projektory na jego podprzestrzenie
   własne i dowód nieredukowalności ograniczeń modułów w wymiarze nieparzystym.
   W uwadze o tych ograniczeniach sprecyzowano n≥3, zgodnie z zakresem
   wcześniej zdefiniowanej grupy Spin. Zredagowano początek dowodu
   kwadratu operatora chiralności, usuwając nierówne odstępy w składzie.
7. **Sfera Blocha.** Dodano jawne współrzędne mapy i jej odwrotności
   oraz rachunek ekwiwariantności z wykorzystaniem projektora rzędu 1.
8. **Struktury spinowe.** Poprawiono indeks ilorazu definiującego
   wiązkę stowarzyszoną (grupa Spin zamiast modułu), podano kierunek
   zmian współrzędnych spinora i rozszerzono definicję na wiązki
   euklidesowe. W konstrukcji na S² ustalono właściwą podgrupę
   stabilizującą e₃ i jej działanie z prawej strony; poprzedni opis
   odwoływał się do stabilizatora zmiennego punktu. Sprawdzono lokalną
   trywialność i zgodność z nakryciem wiązki ramek.
9. **Rachunki algebraiczne.** Uzasadniono alternowanie wzoru na kontrakcję
   w dowodzie bazy algebry Clifforda. W indukcyjnej klasyfikacji algebr
   zespolonych zdefiniowano mnożenie tensorów algebr i podano izomorfizm
   macierzowy przez jednostki macierzowe, zamiast pomijać ten krok.
10. **Podnoszenie i przeszkoda spinowa.** Dodano uzasadnienie podnoszenia
    map z obszarów ściągalnych przez podnoszenie dróg i homotopii.
    Wyjaśniono, dlaczego hipotetyczna struktura spinowa wiązki
    tautologicznej nad S² wymuszałaby zamknięte podniesienie jej przejścia
    na równiku. Poprawiono zdanie, które myliło podnoszenie pętli
    z podnoszeniem samego odwzorowania nakrywającego.
11. **Kryterium znaków.** Podano jawną relację sklejania wiązki głównej
    i wzór na mapę do wiązki ramek. W implikacji odwrotnej podnosimy
    dokładnie ustalone wcześniej ramki. Sprawdzono też niezależność
    przeszkody od zmiany ramek, poza wcześniej opisaną zmianą znaków.
    Wyjaśniono założenie dobrego pokrycia i wskazano, że utożsamienie
    z klasą w H² korzysta z teorii kohomologii Čech, nieudowodnionej tutaj.
12. **Terminologia i redakcja.** Poprawiono „kokykl” na „kocykl”,
    „realna” na „rzeczywista”, „lift” na „podniesienie”, literówki
    i niejasną „wiązkę podstawową” przy zapomnieniu struktury zespolonej.
    Dopisano pozycję dalszej lektury do spisu treści.
13. **Rysunki.** Mapa wykresowa jest teraz rzutem konkretnych płaszczyzn
    liniowych przechodzących przez zero; punkty u i u+Au rzeczywiście
    należą do odpowiednich płaszczyzn, a ich różnica jest pionowym Au.
    W ilustracji iloczynu Clifforda oba wektory jednostkowe mają tę samą
    długość, a rzut i kąt pochodzą z tych samych współrzędnych.
    Na ilustracji nakrycia Spin łuki mają dokładnie 180° i 360°,
    ze strzałkami wewnątrz ścieżek. Normalne n i −n na rysunku orientacji
    mają teraz równe długości.
    Po obejrzeniu PDF odsunięto opisy punktów od krawędzi płaszczyzn
    i poszerzono ramkę na rysunku Blocha, aby mieściła warunek normy 1.

### Kontrola iteracji 4

- Przeczytano wszystkie siedem sekcji rozdziału, w tym dowody bazy
  algebry Clifforda, nakrycia Spin i klasyfikacji modułów.
- Rachunki dokładne w SymPy sprawdzają rzeczywisty i zespolony model
  rzutów Grassmannianu (samosprzężoność, idempotentność, ślad i odwrotną
  mapę wykresową) oraz relację Plückera dla dwupłaszczyzn w wymiarze 4.
- Niezależna implementacja mnożenia uporządkowanych słów Clifforda
  sprawdza znaki w wymiarach 2–6, kwadrat i antykomutację chiralności,
  rewersję i działanie jawnego rotora na parze wektorów jednostkowych.
  Sprawdzono też rekurencję macierzy Pauliego w wymiarach 2, 4 i 6,
  normę mapy Blocha, wzór projektora i znak działania obrotu.
- Zweryfikowano dokładne współrzędne poprawionej ilustracji wykresu.
  Obejrzano wszystkie 17 stron rozdziału (71–87 PDF) oraz osobno
  pięć ilustracji w większej rozdzielczości; po poprawkach etykiet
  ponowiono kontrolę odpowiednich stron.
- Zakres porównany z `02ea77d`: rozdziały 1–3 i 5–18 są niezmienione.
  Środowiska LaTeX zbilansowane, etykiety niepowtórzone, wszystkie
  odsyłacze rozdziału mają cel. `git diff --check` poprawny.
- Punkty odniesienia: [B. Conrad, Clifford algebras and spin groups](https://math.stanford.edu/~conrad/210CPage/handouts/clifford.pdf)
  oraz [K. Wernli, Lecture Notes on Spin Geometry, §2.3](https://arxiv.org/pdf/1911.09766).
  Sprawdzono zgodność kryterium znaków z opisem przeszkody w₂;
  własny dowód sklejania podano jawnie w tekście.
- Pełny dokument ma 280 stron. Brak błędów LaTeX, niezdefiniowanych
  odsyłaczy i ostrzeżeń `Overfull`. W rozdziale 4 brak `Underfull`;
  pozostają trzy takie ostrzeżenia w dalszych rozdziałach oraz trzy
  wcześniejsze zmiany położenia rysunków `h` na `ht`.
  PDF jest aktualizowany razem ze źródłem.

## Iteracja 5 — Algebra homologiczna: moduły, kompleksy i (ko)homologie

Punkt odniesienia: `831cbcc`. Przeczytano wszystkie dziesięć sekcji.

### Zmiany i uzasadnienia

1. **Moduły wolne.** Naprawiono dowód niewolności Z/mZ: poprzedni
   zakładał, że [1] należy do hipotetycznej bazy. Teraz rozwijamy [1]
   w dowolnej bazie i wykorzystujemy jednoznaczność współczynników.
   Dodano niezbędne założenie m≥2.
2. **Podstawowe konstrukcje.** Wyjaśniono rolę przemienności pierścienia
   w strukturze modułu Hom i zdefiniowano sumę prostą z jej włączeniami
   i rzutami. W dowodzie rozszczepienia zapisano retrakcję jako konkretne
   złożenie, usuwając niejasny kierunek izomorfizmu.
3. **Długi ciąg homologii.** Naprawiono końcowy argument: H₋₁(A)=0
   wynika z A₋₁=0, a nie z C₋₁=0. Założenie twierdzenia pozostaje to samo.
   „Niezależność od [c]” zastąpiono niezależnością od reprezentanta [c];
   wynik oczywiście zależy od klasy.
   W uwadze o naturalności określono wszystkie trzy odwzorowania
   między krótkimi ciągami i wymagane równości przemienności.
4. **Kohomologia i naturalność.** Uzupełniono zgodność homomorfizmu
   łączącego z mnożeniem przez skalary i jego naturalność. W twierdzeniu
   o dualności nad ciałem dodano rachunek naturalności ewaluacji.
5. **Homotopie.** Wymagamy jawnie, aby hₙ były homomorfizmami modułów,
   a f i g odwzorowaniami łańcuchowymi. Bez pierwszego warunku późniejszy
   przykład kompleksu acyklicznego, lecz nieściągalnego nie działałby.
   W dowodzie kasowania pary przedłużono homotopię na cały kompleks
   i podano id−jp=∂h+h∂ oraz pj=id, uzasadniając zastosowanie twierdzenia.
6. **Ilorazy i suma kompleksów.** Rozróżniono klasę c modulo podkompleks
   od jej klasy homologii. Doprecyzowano, że używana filtracja jest
   skończona i rosnąca. W dowodzie Mayera–Vietorisa uzasadniono
   Hₙ(A⊕B)≅Hₙ(A)⊕Hₙ(B) przez cykle, brzegi i ich ilorazy.
7. **Redukcja modulo m.** Dodano jawny wzór na ostatnią strzałkę:
   ∂c=ma prowadzi do [a]. Wyjaśniono jednoznaczność a, warunek bycia
   cyklem, m-torsję oraz naturalność. Wstęp do sekcji ograniczono
   do kompleksów wolnych grup, zgodnie z założeniem twierdzenia.
8. **Tensorowanie modułów.** Uzupełniono brakującą konstrukcję nad
   pierścieniem: iloraz modułu wolnego przez relacje dwuliniowości,
   własność uniwersalną, rozszerzenie skalarów i bazę modułu po tej
   operacji. Uzasadniono zachowanie sum prostych i izomorfizmów.
   To wyjaśnia operacje potrzebne w istniejącym dowodzie zmiany
   współczynników; wcześniejszy rozdział dotyczył tensorowania nad ciałem.
9. **Charakterystyka zero.** Zdefiniowano zapis Hₙ(C;Z), poprawność
   różniczki po tensorowaniu, pełną mapę [c]⊗q↦[c⊗q] i reprezentowanie
   dowolnego tensora przez wspólny mianownik. Zapisano oba kierunki
   izomorfizmu rozszerzenia skalarów Z→Q→F i wyjaśniono kanoniczność
   wyniku mimo wyboru dopełnień. Usunięto niepasujący zapis Hₙ(D;Q)
   dla kompleksu D, który już jest racjonalny.
10. **Terminologia i skład.** W całym rozdziale zastąpiono „kokykl”
    przez „kocykl” oraz „lift” przez „podniesienie”, z poprawną odmianą.
    Zamiast „n-ta homologia” piszemy „homologia stopnia n”. Poprawiono
    zgodę gramatyczną kilku zdań i dodano dalszą lekturę do spisu treści.
    W diagramie podnoszenia krótki podpis „wybór b” mieści się nad strzałką.

### Kontrola iteracji 5

- Cały rozdział przeczytano i sprawdzono matematycznie: definicje modułów,
  dokładność, oba długie ciągi, dualność, kasowanie pary, filtracje,
  Mayer–Vietoris, zmiana współczynników, Euler i lemat pięciu.
- Dla kompleksów Z —k→ Z sprawdzono 64 pary k,m∈{2,…,9}:
  wzór homomorfizmu łączącego, jego addytywność, obraz równy m-torsji
  i rozmiary jąder/ilorazów. Obejmuje to złożone m, a nie tylko ciała.
- Na kompleksie Z→Z³→Z² z macierzami ∂₂=(−6,3,0)ᵀ,
  ∂₁=((1,2,3),(2,4,8)) sprawdzono dokładnie całkowite zmiany baz,
  oddzielenie pary, zgodność rzutów z różniczkami i tożsamość homotopii.
  Po przejściu do Q sprawdzono homologię, kohomologię dualną i Eulera.
- Przykład Mayera–Vietorisa zweryfikowano nad F₂, F₃, F₅ i F₇:
  obraz klasy u+v jest x−y i daje wymagane jądro następnej mapy.
- Obejrzano wszystkie 17 stron rozdziału (88–104 PDF) i osobno diagram
  odwzorowania łączącego na stronie 93. Geometria diagramu była poprawna;
  zmieniono tylko podpis na polski. Pozostały układ jest czytelny.
- Porównanie z `831cbcc` potwierdza, że rozdziały 1–4 i 6–18 nie zostały
  zmienione. Środowiska LaTeX są zbilansowane, etykiety niepowtórzone,
  odsyłacze mają cele. `git diff --check` poprawny.
- Punkty odniesienia: [The Stacks Project, Complexes](https://stacks.math.columbia.edu/tag/010V)
  oraz [Tensor products](https://stacks.math.columbia.edu/tag/00CV).
  Sprawdzono wymaganie liniowości homotopii i zakres konstrukcji tensorowej.
- Pełny dokument kompiluje się do 281 stron, bez błędów, niezdefiniowanych
  odsyłaczy i `Overfull`. Brak ostrzeżeń `Underfull` w rozdziale 5;
  pozostają trzy wcześniejsze w dalszych rozdziałach i trzy zmiany `h` na `ht`.
  PDF aktualizowany wraz ze źródłem.

## Iteracja 6 — Homotopia, nakrycia i komórkowe modele przestrzeni

Status: sprawdzono i poprawiono wszystkie 5 sekcji oraz 6 ilustracji.
Data zakończenia: 2026-10-01.

Przegląd rozpoczęto od `4f017f4`. W jego trakcie, na prośbę użytkownika,
wykonano pull trzech commitów Darka, do `5b259e6`; ten commit jest
końcowym punktem odniesienia iteracji. Niezacommitowane zmiany rozdziału 6
zabezpieczono w stashu i przywrócono bez konfliktów. Przeczytano cały
rozdział i źródła sześciu rysunków.

**Drobna naprawa po pullu poza rozdziałem 6.** W przykładzie „Prosta
z podwojonym początkiem” w rozdziale 1 przywrócono widoczne klamry zbiorów
(`\{…\}` zamiast grupujących `{…}`) i zapis `{[x]: x∈I, x≠0}`.
Pobrany zapis błędnie umieszczał klasę [x] w przedziale liczb rzeczywistych.
Zachowano nowe nawiasy w definicji relacji równoważności i wszystkie
pozostałe zmiany merytoryczne oraz redakcyjne Darka.

### Zmiany i uzasadnienia

1. **Homotopie i retrakty.** Dodano jawne wymagania ciągłości f,g,H
   w definicjach. Zbiór wypukły uznano za ściągalny przy niezbędnym
   założeniu niepustości. Wyjaśniono, że homotopia dróg jest relacją
   równoważności. Poprawiono zdanie o parametrze czasu.
2. **Punkt bazowy.** Wyjaśniono, dlaczego obraz brzegu kwadratu jest
   homotopijny do stałej z ustalonym narożnikiem. W dowodzie niezmienniczości
   π₁ rozróżniono drogę fu od drogi otrzymanej z homotopii fg≃id:
   mają te same końce, ale nie muszą być równe; podano potrzebne złożenie
   izomorfizmów zmiany punktu bazowego.
3. **Podnoszenie.** Doprecyzowano homeomorfizmy na arkuszach i podano
   dowód lematu o liczbie Lebesgue’a, używanego przy podziale odcinka
   i kwadratu. W kryterium podnoszenia uzasadniono równość końców
   przez odwrócenie drugiej części podniesionej pętli i jednoznaczność.
4. **Warunek półlokalny.** Poprawiono tytuł definicji i określono ją
   dla pętli opartych w rozważanym punkcie. Wyjaśniono zmianę punktu
   bazowego w łukowo spójnym otoczeniu, potrzebną w konstrukcji nakrycia.
5. **Nakrycie uniwersalne.** Sprawdzono aksjomat bazy topologii dla
   przecięcia arkuszy nad różnymi U,U′ oraz ciągłość i otwartość mapy
   na każdym arkuszu, zamiast tylko postulować homeomorfizm.
6. **Klasyfikacja nakryć.** Udowodniono wolność działania, rozłączność
   przesunięć arkusza i otwartość projekcji na orbity. Sama wolność
   działania nie gwarantuje nakrycia. Wykazano, że iloraz realizuje
   dokładnie zadaną podgrupę. Przy porównaniu z dowolnym nakryciem
   uzasadniono surjektywność oraz równoważność włókien i orbit.
   Opisano sprzężenie podgrupy przy zmianie punktu nad bazą i jego odwrotność.
7. **Van Kampen.** Rozwinięto opis iloczynu wolnego i jego własności
   uniwersalnej. Naprawiono punkt bazowy pętli porównującej drogi
   pomocnicze: używamy λ′ⱼ*λ̄ⱼ, z początkiem w x₀. Dowód jądra
   zapisano przez drogi do wszystkich wierzchołków siatki, elementy
   przypisane krawędziom i relacje wokół prostokątów. Sprawdzono zgodność
   na wspólnych krawędziach oraz odtworzenie początkowego słowa.
8. **Sympleksy.** Rozróżniono ściany kowymiaru jeden od ogólnych ścian,
   osobno określono pusty brzeg Δ⁰. Usunięto literówkę „afininicznej”.
   W homeomorfizmie z dyskiem dodano jawne przedłużenie radialne
   i kontrolę ciągłości w środku. Definicja triangulacji zaznacza
   używany zakres skończony, więc nie sugeruje objęcia przestrzeni niezwartych.
9. **Δ-kompleksy i CW.** Doprecyzowano warunek Hausdorffa i ciągłość map
   charakterystycznych, zgodność kolejności wierzchołków ścian oraz
   topologię ilorazową także dla nieskończonej sumy sympleksów.
   Dla torusa podano oba porządki wierzchołków. W definicji CW poprawiono
   równoważność definiującą topologię słabą, gramatykę i nazwę warunku
   skończoności domknięć. Wyjaśniono argument o zwartej sumie sympleksów
   i topologii ilorazowej skończonej realizacji.
10. **Dołączanie komórek.** Sprawdzono osadzenie Y jako podzbioru
    domkniętego i otwarte osadzenie wnętrza komórki. W dowodzie zmiany π₁
    podano wzór homotopii pasa przy brzegu, uzasadniono ciągłość przy Y
    przez otoczenia zawierające całe odcinki radialne i sprawdzono
    otwartość obu zbiorów użytych w twierdzeniu van Kampena.
11. **Płaszczyzna rzutowa.** Uzasadniono homeomorfizm [z]↦z² na
    okręgu z utożsamionymi antypodami i wynikającą z niego relację a²=1.
    Zamiast niewprowadzonego jeszcze stopnia mapy użyto liczby owinięć.
    Niejasne porównanie z podgrupą indeksu 2 zastąpiono opisem roli brzegu komórki.
12. **Rysunki i redakcja.** Dodano kierunek przekątnej torusa i usunięto
    niezwiązane z matematyką zdanie o kratkowanym tle. Na rysunku szkieletów
    strzałka wskazuje właściwą 1-komórkę. W rysunku D²/∂D² strzałka
    ma oznaczenie mapy ilorazowej q: wcześniejsze φ było zdefiniowane
    tylko na brzegu, a strzałka dotyczyła całego dysku. Doprecyzowano podpis.
    Nakrycie okręgu przedstawiono jako linię śrubową (zamiast „spirali”).
    Dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 6

- Przeczytano cały rozdział, w tym definicje, dowody i przykłady.
  Sprawdzono kolejność wprowadzania pojęć oraz zależności między dowodami.
- Niezależnie sprawdzono rachunek słów przy zmianie dróg pomocniczych
  i identyfikacji orbit w nakryciu. Dla siatek 1×1, 2×3 i 5×4 sprawdzono,
  że przesuwanie drogi przez prostokąty przechodzi przez każdą komórkę
  dokładnie raz i zachowuje końce drogi.
- Symbolicznie sprawdzono warunki końcowe homotopii radialnej,
  normę odwzorowania dysku na sferę i granicę w środku dysku.
  Dla sympleksów wymiarów 1–4 sprawdzono przecięcia promieni z brzegiem
  w zestawie kierunków o współrzędnych całkowitych. Zweryfikowano
  orientacje ścian obu trójkątów torusa i zgodność liczby komórek.
  Są to kontrole pomocnicze; ogólne uzasadnienia pozostają w tekście.
- Obejrzano wszystkie 14 stron rozdziału (105–118 PDF), a sześć rysunków
  dodatkowo w większej rozdzielczości (strony 106, 108, 113, 115 i 116).
  Sprawdzono czytelność podpisów, kierunki strzałek i wskazania komórek.
  Obejrzano także poprawiony zapis przykładu z rozdziału 1 na stronie 6.
- Porównanie z `5b259e6` potwierdza brak zmian w rozdziałach 2–5 i 7–18.
  Jedyny wyjątek poza rozdziałem 6 to opisana wyżej naprawa notacji
  w pobranym przykładzie z rozdziału 1. Środowiska LaTeX są zbilansowane,
  etykiety niepowtórzone, a odsyłacze mają cele.
- Punkty odniesienia: [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  rozdział 1 (van Kampen, podnoszenie, konstrukcja i klasyfikacja nakryć),
  oraz [materiały UW o CW-kompleksach](https://www.mimuw.edu.pl/~sjack/ta/5_cw_grupy_homotopii_jhcw.pdf)
  (definicje i terminologia).
- Pełny dokument kompiluje się do 283 stron. Końcowy przebieg nie zgłasza
  błędów, niezdefiniowanych odsyłaczy, potrzeby ponownej kompilacji ani
  `Overfull`. Pozostają trzy wcześniejsze ostrzeżenia `Underfull`
  w dalszych rozdziałach i trzy zmiany położenia ilustracji z `h` na `ht`.
  PDF zaktualizowano wraz ze źródłem; `git diff --check` poprawny.

Następna iteracja: rozdział 7 — „Homologia przestrzeni”.

## Iteracja 7 — Homologia przestrzeni

Status: sprawdzono i poprawiono wszystkie 8 sekcji oraz 3 ilustracje.
Data zakończenia: 2026-10-01.

Punkt odniesienia: `21a3ecb`. Przed rozpoczęciem wykonano pull;
gałąź była aktualna. Przeczytano cały rozdział: osiem sekcji i trzy ilustracje.

### Zmiany i uzasadnienia

1. **Orientacja i składowe.** W dowodzie opisu H₀ symplicjalnego
   podano argument z otwartymi i domkniętymi realizacjami składowych
   grafu krawędzi. Samo stwierdzenie, że sympleksy są spójne, nie wyjaśniało
   wystarczająco przejścia od drogi ciągłej do drogi po krawędziach.
   Ujednolicono „składowe łukowe” z poprzednim rozdziałem.
2. **Operator pryzmatyczny.** Rozpisano osobno znaki ścian bocznych
   dla j<i i j>i oraz kasowanie ściany między dwiema sąsiednimi częściami.
   Określono P₋₁=0. Poprawiono błędną odmianę „afininiczną posyłającą”.
3. **Homologia zredukowana.** Zdefiniowano ją jednolicie przez kompleks
   augmentowany, także dla przestrzeni pustej. Wzór Z^(c−1) ograniczono
   do skończonej liczby składowych; dla dowolnej liczby podano bazę
   różnic klas i sumę prostą. Uzasadniono zredukowany ciąg pary,
   używany następnie do obliczenia homologii dysku względem brzegu.
4. **Podział barycentryczny.** Ustalono kolejność barycentrów według
   wymiarów ścian i podano sumę po permutacjach ze znakiem permutacji.
   W łańcuchach singularnych zmiana parametryzacji nie jest formalnie
   mnożeniem przez −1; wspólne ściany muszą mieć identyczną parametryzację.
   Rozpisano kasowanie ścian wewnętrznych i znaki ścian zewnętrznych.
5. **Homotopia podziału i małe łańcuchy.** Zastąpiono nieokreślony zapis
   tₙ₋₁(∂uₙ) sumą obrazów przez włączenia ścian. Dodano wzór stożka
   singularnego i sprawdzenie ciągłości w jego wierzchołku. Wyjaśniono
   stopień zero. Oszacowanie zmniejszenia średnicy wyprowadzono ze wzoru
   na barycentra dwóch zagnieżdżonych ścian.
6. **Porównanie z modelem symplicjalnym.** Podkreślono, że mapa porównawcza
   używa wybranych uporządkowanych generatorów i rozszerzenia liniowego,
   a nie dowolnego odwracania parametryzacji. W dowodzie indukcyjnym
   wykazano, że mapa par przenosi generator na generator przez
   homeomorfizm ilorazów; sam fakt, że obie grupy są Z, nie wystarcza.
7. **Iloraz pary komórkowej.** Dodano niezbędne założenie A≠∅ oraz
   uzasadnienie ciągłości homotopii na ilorazie z parametrem czasu.
   Użyto domkniętości projekcji i zwartości jej włókien. Rozszerzono
   konstrukcję otoczenia na dołączenie jednej komórki, potrzebne w dowodzie
   porównania. Wyjaśniono ciągłość radialnej retrakcji przy sklejanym A.
   Poprawiono zdanie utożsamiające pełne kompleksy z modelami małych
   łańcuchów: lemat zapewnia tu izomorfizm homologii.
8. **Generator sympleksu i bukiet sfer.** Skonstruowano konkretne otwarte
   pokrycia oraz retrakcje części i przecięć do użycia w Mayerze–Vietorisie.
   Używanie bezpośrednio domkniętych części nie wynikało z wcześniejszej
   wersji tego twierdzenia. W warstwie komórek obsłużono pusty szkielet.
9. **Homologia komórkowa i stopień.** Oddzielono przypadek n=1 w dowodzie
   ∂²=0, unikając niezdefiniowanych map w stopniach ujemnych. Uzasadniono
   deg(z↦zʳ)=r przez konkretny singularny trójkąt realizujący dodawanie
   klas pętli, odwrotność pętli i generator z Mayera–Vietorisa.
   We wzorze brzegu komórkowego określono orientacje sfer dziedziny
   i obrazu zgodnie z orientacjami komórek; to ustala znaki stopni.
10. **Współczynniki.** Zdefiniowano łańcuchy z wartościami w R i wyjaśniono,
    dlaczego konstrukcje pryzmatu, podziału, ciągów par i szkieletów działają
    także nad pierścieniem. Wykorzystano rozszczepienie odpowiednich ciągów
    w każdym stopniu, bez zakładania dokładności dowolnego tensorowania.
    Uzasadnia to w szczególności podany w skrypcie rachunek RP² modulo 2.
    Wyjaśnienie wydzielono do osobnej uwagi przed przykładem.
11. **Lokalna homologia.** Rozróżniono otoczenie U w rozmaitości od kuli
    Bᵐ będącej obrazem mapy. Retrakcję otwartej kuli bez środka skierowano
    na sferę o promieniu 1/2: jednostkowa sfera nie należy do otwartej kuli.
12. **Rysunki i język.** Na ilustracji singularnego sympleksu zaznaczono
    trzy obrazy wierzchołków i trzy skierowane części brzegu; wypełnienie
    ma teraz dokładnie ten sam brzeg co strzałki. W diagramie torusa
    „wnętrze torusa” zastąpiono „jedna 2-komórka”. Poprawiono m.in.
    „dowolna ciągłe”, „homologa punktu”, „fundament dysku”, „nie koniecznie”,
    odmianę słowa „odwzorowanie” i odsyłacze nazywające sekcje rozdziałami.
    Dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 7

- Niezależnie obliczono brzegi uporządkowanych sympleksów afinicznych
  w wymiarach 0–5, traktując różne parametryzacje jako różne generatory.
  Sprawdzono ∂²=0, ∂S=S∂ i tożsamość operatora pryzmatycznego.
  Nie upraszczano sympleksów przez zamianę orientacji ani nie usuwano
  generatorów zdegenerowanych, co mogłoby ukryć błąd znaku.
- W wymiarach 1–4 skonstruowano łańcuchy homotopii stożkowej
  i sprawdzono dokładnie ∂T+T∂=S−id. Sprawdzono też ich obrazy
  przez nieróżnowartościowe odwzorowania afiniczne.
- Z porządków wierzchołków obu trójkątów torusa niezależnie otrzymano
  macierz brzegu i jej postać Smitha: H₁=Z², H₂=Z, zgodnie z modelem CW.
  Dla RP² sprawdzono torsję całkowitą oraz jądra i ilorazy mnożenia
  przez 2 nad Z/m dla m=2,3,4,5,7. Kontrole te uzupełniają ogólne dowody.
- Obejrzano wszystkie 14 stron rozdziału (119–132 PDF), a rysunki
  na stronach 120, 121 i 130 także w większej rozdzielczości.
  Po końcowych poprawkach sprawdzono ponownie zmieniony skład.
- Porównanie z `21a3ecb` potwierdza, że pozostałe rozdziały są bez zmian.
  Środowiska LaTeX są zbilansowane, etykiety unikalne, odsyłacze mają cele;
  `git diff --check` nie wykazał problemów.
- Punktem odniesienia był [Allen Hatcher, Algebraic Topology, rozdział 2](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf):
  podział barycentryczny, homologia ilorazu dobrej pary i model komórkowy.
- Pełny dokument skompilowano lokalnie do 285 stron. Końcowy przebieg
  nie zgłasza błędów, niezdefiniowanych odsyłaczy, potrzeby ponownej
  kompilacji ani `Overfull`. Pozostały trzy wcześniejsze `Underfull`
  poza rozdziałem 7 i trzy zmiany położenia ilustracji z `h` na `ht`.
  Próba wbudowanego kompilatora edytora zwróciła status nieznany;
  potwierdzona kompilacja i dostarczony PDF pochodzą z lokalnego MiKTeX.
  PDF zaktualizowano wraz ze źródłem.

Następna iteracja: rozdział 8 — „Wyższe grupy homotopii i związek z homologią”.

## Iteracja 8 — Wyższe grupy homotopii i związek z homologią

Status: sprawdzono i poprawiono wszystkie 7 sekcji merytorycznych oraz 4 ilustracje.
Data zakończenia: 2026-10-02.

Punkt odniesienia: `3e871f0`. Pull przed rozpoczęciem nie pobrał nowych zmian.
Przeczytano cały rozdział: siedem sekcji merytorycznych, zakończenie i cztery rysunki.

### Zmiany i uzasadnienia

1. **Definicje i punkty bazowe.** Zastąpiono nieokreślone „dobrze wskazane
   topologicznie” wyborem punktu bazowego; w argumentach komórkowych jest
   on wierzchołkiem. Ujednolicono „spójność łukową”. Wyjaśniono zależność
   zmiany punktu bazowego od klasy drogi i zgodność z homotopią, która
   porusza bazę; jest to potrzebne przy przybliżaniu słabej równoważności.
2. **Eckmann–Hilton.** Rozpisano podstawienia elementu neutralnego.
   Oddzielono równość map na czterech ćwiartkach od równości klas po
   usunięciu stałych połówek. Te drugie wymagają zmiany parametryzacji.
3. **Ciąg względny.** W dokładności przy πₙ(X) wykorzystano konkretną
   ścianę homotopii zerującej i dwie drogi w kwadracie parametrów.
   Rozpisano koniec ciągu jako ciąg zbiorów wskazanych i dowód naturalności.
   W definicji spójności par zaznaczono wszystkie punkty bazowe w A.
4. **Nieskończone CW.** Dodano dowód, że zwarty podzbiór leży w skończonym
   podkompleksie. Wyjaśniono ilorazowość iloczynu z przedziałem i wynikające
   z niej kryterium ciągłości homotopii na wszystkich komórkach.
   Uzasadniono komórkową homologię par przez iloraz kompleksów i lemat pięciu,
   a następnie przejście z homologii skończonych CW do dowolnych CW.
   Rozdział 7 dowodził wcześniej twierdzenia jedynie w zakresie skończonym.
5. **Przybliżenie komórkowe.** Wypełniono techniczną lukę: zwarte K,
   wielościenne otoczenie P, interpolacja afiniczna, funkcja odcinająca
   i kontrola błędu zapewniają punkt pominięty przez cały nowy obraz,
   także poza obszarem przybliżania. Opisano kolejność usuwania komórek.
   W równych wymiarach wybór punktu poza obrazami ścian i części niższego
   rzędu daje skończone przeciwobrazy z lokalnymi znakami; ten wariant
   uzasadnia późniejsze liczenie komórek w dowodzie Hurewicza.
6. **Szkielety i homotopie nieskończone.** Przed względnym przybliżaniem
   dysku przybliżono jego brzeg i użyto HEP. Wcześniej brzeg nie musiał być
   komórkowy, więc nie można było zachować go i otrzymać obrazu w Xⁱ.
   Dla kolejnych etapów podano przedziały czasu i sprawdzono ciągłość
   w chwili granicznej na każdej komórce z całym przedziałem.
7. **Nakrycia i H₁.** Podnoszenie homotopii wyprowadzono z kryterium dla
   jednospójnego Sⁿ×I; wyjaśniono stałość bazy w dyskretnym włóknie.
   W dowodzie Hurewicza w stopniu 1 dopisano niezmienniczość względem
   homotopii pętli. Kasowanie dróg pomocniczych odbywa się w łańcuchach
   modulo brzegi, nie w „klasach” pojedynczych niezamkniętych dróg.
8. **Ściskanie i Whitehead.** Podano jawny wzór kołnierza unieruchamiającego
   cały brzeg dysku podczas homotopii. Oddzielono pustą przestrzeń i stopień 1,
   gdzie zamiast argumentu dla grup potrzebny jest rachunek dróg.
   Opisano komórki cylindra odwzorowania i jawną odwrotność homotopijną.
9. **Pierwsze komórki.** Uzasadniono abelowość π₂(W,A) przy jednospójnym A,
   doprowadzanie dysków do bazy, lokalne znaki i rozcinanie wzdłuż drzewa.
   Dla relacji od wyższych komórek wskazano, że drogi doprowadzające leżą
   w W, które też jest jednospójne. Poprawiono Zⁿ⁺¹ na A∪Zⁿ⁺¹ tam,
   gdzie A może mieć komórki wyższych wymiarów. Dodano surjektywność
   przed opisem jądra oraz sens obrazu klas dołączających w grupie względnej.
10. **Model Hurewicza.** Dodano osobny wniosek o zabijaniu wybranych klas
    z dowodem z ciągu pary. W kolejnych etapach bazą jest cały aktualny
    model, a nie punkt: lemat o pierwszych komórkach z bazą punktową
    nie miałby wtedy wymaganych założeń. Sprawdzono stabilizację grup,
    komórkowość map dołączających i przejście do nieskończonego modelu.
11. **Względny Hurewicz i przykłady.** W porównaniu ciągów osobno obsłużono
    π₂ i względny stopień 1. Ustalono zgodne orientacje dla map Hurewicza,
    ograniczono względny homomorfizm do n≥2 i opisano addytywność.
    W przykładzie dysku chodzi o reprezentanta generatora, nie każdej klasy.
    Wyjaśniono oparte i nieoparte mapy sfer. W kompleksie Moore’a zaznaczono
    także C₀. Dla nakrycia S¹∨S² podano bezpośredni model CW i uzasadnienie
    jednospójności, bez nieuzasadnionego zwijania nieskończonej prostej.
12. **Język i ilustracje.** Poprawiono odmianę słowa „odwzorowanie”,
    „antipodalne” na „antypodalne”, niejasne użycie słowa „baza” i wymiar
    sfery jako brzegu dysku. Rysunek względnego dysku pokazuje A jako pas
    zawierający obraz brzegu, a wnętrze obrazu może wyjść poza A.
    W nakryciu bukietu usunięto szczelinę między sferami i prostą.
    Wycentrowano pionowy podpis kierunku sklejania i przeniesiono
    oznaczenie utożsamienia w cylindrze ponad rysunek, poza tekst objaśnienia.
    Zakończenie i dalszą lekturę dodano do spisu treści.

### Kontrola iteracji 8

- Przejrzano kolejność zależności: zwarte obrazy i iloczyn z przedziałem
  poprzedzają HEP oraz przybliżenie komórkowe; Whitehead poprzedza budowę
  modelu; lemat o pierwszych komórkach poprzedza zabijanie klas i Hurewicza.
  Lokalny argument afiniczny nie korzysta z twierdzenia Sarda ani z
  twierdzenia Hurewicza, które dopiero ma być udowodnione.
- Sprawdzono wzory Eckmanna–Hiltona na 441 parach wymiernych parametrów,
  także na liniach sklejania, zachowując współrzędne wewnątrz każdej ćwiartki.
  Rachunek potwierdza równość map używaną przed przejściem do klas.
- Dla retrakcji HEP sprawdzono na tej samej siatce, że obraz leży
  na dole lub boku cylindra, współrzędne pozostają w dozwolonym zakresie,
  a zadany podzbiór jest nieruchomy. Symbolicznie sprawdzono zgodność
  czasów obu wzorów kołnierza i jego promienie końcowe.
- Dla skończonych fragmentów nakrycia z 3,5,…,13 sferami niezależnie
  obliczono macierze brzegów: H₀=Z, H₁=0, a H₂ ma po jednym generatorze
  na sferę. Rzut sumujący współczynniki ma rangę 1. Sprawdzono też
  ilorazy Smitha dla kompleksów Moore’a o m=2,3,5,7.
  Te kontrole są pomocnicze; argumenty ogólne, w tym przejście do
  nieskończonego nakrycia, pozostają w tekście.
- Obejrzano wszystkie 15 stron rozdziału (133–147 PDF). Cztery rysunki
  na stronach 134, 135, 141 i 147 sprawdzono także w większej rozdzielczości,
  a po zmianie położenia podpisów ponownie obejrzano dwa zmienione rysunki.
- Kontrola zakresu względem `3e871f0` potwierdziła brak zmian w pozostałych
  rozdziałach. Środowiska LaTeX są zbilansowane, etykiety niepowtórzone,
  odsyłacze mają cele. `git diff --check` poprawny.
- Punkty odniesienia: [Hatcher, rozdział 4](https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf)
  oraz [dodatek o CW](https://pi.math.cornell.edu/~hatcher/AT/ATapp.pdf)
  (w szczególności skończone podkompleksy zawierające zwarte obrazy).
- Pełny PDF ma 288 stron. Kompilację potwierdzono lokalnym MiKTeX;
  wbudowany kompilator edytora ponownie zwrócił status nieznany.
  Nie ma błędów ani `Overfull`. Pozostały dwa wcześniejsze `Underfull`
  w późniejszych rozdziałach i trzy zmiany położenia ilustracji `h` na `ht`.
  Poprzednie ostrzeżenie `Underfull` w rozdziale 8 zniknęło po redakcji.
  PDF zaktualizowano razem ze źródłem.

Następna iteracja: rozdział 9 — „Formy różniczkowe, orientacja i kohomologia de Rhama”.

## Rozdział 9 — formy, orientacja i kohomologia de Rhama (2026-10-02)

Punkt wyjścia: `f7df0ae`. W trakcie przeglądu pobrano także commit Darka
`0d9857f` („Uzupelnienie dowodow i przykladow do przestrzeni stycznej.”).
Przywrócenie lokalnych zmian po aktualizacji przebiegło bez konfliktów.
Kontrola względem `0d9857f` potwierdza zachowanie jego zmian w całości;
nasze poprawki tej iteracji dotyczą wyłącznie rozdziału 9.
Przegląd i poniższe kontrole rozdziału 9 zakończono.
Nowe uzupełnienia Darka z rozdziału 1 zachowano; ich osobny ponowny
przegląd merytoryczny należy uwzględnić w końcowej kontroli zmian
powstałych po wcześniejszych iteracjach.

### Dowód de Rhama i całkowanie po sympleksach

- Poprawiono definicję gładkiego sympleksu dla rozmaitości z brzegiem.
  Przedłużamy jego składowe we współrzędnych do przestrzeni euklidesowej;
  nie wymagamy przedłużenia o wartościach w samej półprzestrzeni.
  Wcześniejsze sformułowanie wykluczało np. gładki odcinek t ↦ t
  zaczynający się na brzegu półprostej.
- Zastąpiono nieuzasadnione rozcinanie sympleksu na części z gładkim
  brzegiem lokalnym dowodem Stokesa w narożach. Każda współrzędna
  półprzestrzeni daje wkład jednej ściany; przecięcia ścian mają w nich
  miarę zero. Wyjaśniono zgodność orientacji ścian ze znakami (−1)^j.
- Usunięto sugestię, że można niezależnie wygładzać poszczególne
  sympleksy ciągłe przy definiowaniu kołańcucha całkowania. Bez zgodności
  na ścianach taki wybór nie definiuje odwzorowania kompleksów.
- Przepisano dowód porównania trzech kompleksów: form, gładkich
  kołańcuchów singularnych oraz wszystkich kołańcuchów singularnych.
  Izomorfizm ograniczenia z ciągłych do gładkich kołańcuchów otrzymujemy
  równocześnie z izomorfizmem całkowania, zamiast powoływać się na
  niedowiedzione wygładzanie względne przy narożach.
- Uzupełniono algebrę kompleksu podwójnego: znaki różniczki całkowitej,
  usuwanie składników kocyklu w dokładnych kolumnach, kryterium
  izomorfizmu przez stożek odwzorowania oraz rolę skończonych przekątnych.
  Dokładność wierszy jest uzasadniona osobno dla form (podział jedności)
  i kołańcuchów (wybór indeksu zawierającego mały sympleks).
- Wyeliminowano odwołanie do silnie wypukłych kul geodezyjnych i
  nieuzasadnionych „półkul” przy brzegu. Dwukrotne sklejanie wystarcza:
  najpierw prostokąty w dowolnym otwartym podzbiorze przestrzeni lub
  półprzestrzeni, następnie dziedziny map na rozmaitości. Ich przecięcia
  nie muszą być ściągalne. Dowód nie używa pojęć z późniejszych rozdziałów.
- Wyjaśniono dualizację nad R także w nieskończonym wymiarze oraz
  wynikającą stąd możliwość zastąpienia całego cyklu gładkim cyklem.
  Niezależność okresów wynika z istnienia gładkiego łańcucha między
  takimi reprezentantami i ze Stokesa.

### Pozostałe dowody, założenia i terminologia

- W dowodzie jednoznaczności różniczki zewnętrznej najpierw wykazano
  lokalność za pomocą pojedynczej funkcji odcinającej. Dopiero to pozwala
  stosować warunki określające globalny operator do lokalnych współrzędnych.
- Dodano konwencję zerowych form w ujemnych stopniach i przypadek k=0
  operatora homotopii. Wyjaśniono gładkość homotopii przy narożach iloczynu.
- Dla definicji pochodnej Liego przez dwustronny przepływ wymagamy
  styczności pola do brzegu. Dla dowolnego pola wskazano definicję przez
  wzór Cartana i jednoznaczne przedłużenie z wnętrza. Rozróżniono też
  różniczkę form od euklidesowych identyfikacji z rotacją i dywergencją.
- Doprecyzowano lokalną skończoność rodziny nośników w podziale jedności,
  zawieranie domknięcia większej kuli wewnątrz mapy, wersję przy brzegu
  i grupowanie funkcji według pierwotnego pokrycia. To ostatnie uzasadnia
  nośniki dwóch funkcji używanych w dowodzie Mayera–Vietorisa.
- Uzupełniono orientację w wymiarze 0: są dwa znaki, lecz tylko jedna
  baza pusta, więc opis przez dwie klasy baz nie działa w tym wymiarze.
  Całka jest sumą ze znakami, a orientację brzegu przedziału definiuje
  wartość kontrakcji formy z wektorem skierowanym na zewnątrz.
- W dowodzie równoważności opisów orientowalności wydzielono wymiar 0,
  zmniejszono mapy do spójnych dziedzin i dopuszczono obie półprzestrzenie.
  Pozwala to dobierać mapy dodatnie także na obu końcach przedziału.
- W twierdzeniu o orientacji regularnego przeciwobrazu dodano konieczne
  założenie regularności ograniczenia do brzegu, jeśli M ma brzeg.
  Dowiedziono lokalnej postaci półprzestrzeni i równości brzegów.
  Kontrprzykład F(x,s)=x²+s na s≥0 pokazuje, że sama regularność F
  nie wystarcza. Ilorazowy wzór na formę orientującą poziomicę obejmuje
  także wymiar 0 i wyjaśnia niezależność od podniesień i baz.
- We wzorze Stokesa sprawdzono znaki normalnej zewnętrznej i indeksu
  pominiętej współrzędnej. Zaznaczono, że odzyskanie podstawowego
  twierdzenia rachunku całkowego jest identyfikacją przypadku szczególnego;
  dowód Stokesa sam już używa tego faktu analizy.
- Dla okręgu wykazano pełną okresowość funkcji pierwotnej, zamiast
  jedynie równości wartości na końcach przedziału. Dla sfer rozpisano
  surjekcję (a,b) ↦ b−a w stopniu 0; dla torusa oddzielono niezależność
  dwóch klas stopnia 1 od niezerowości klasy stopnia 2.
- W porównaniu trzech teorii dodano spójność drogową przy H₁ oraz k≥2
  przy wyższym twierdzeniu Hurewicza, objaśniono warianty oznaczeń
  homologii i przejście do lokalnie skończonych triangulacji przez
  skończone podkompleksy. Doprecyzowano położenie wycinanego dysku w torusie.
- Jawnie wskazano dodatkową zależność zastosowania Hurewicza:
  twierdzenie o triangulacji gładkich rozmaitości daje strukturę CW.
  Jest to wskazany z nazwy wynik zewnętrzny, z odsyłaczem do
  [notatek Luriego](https://www.math.ias.edu/~lurie/937notes/937Lecture3.pdf),
  a nie twierdzenie udowodnione w tym rozdziale. Dowód de Rhama po
  poprawkach nie korzysta z triangulacji. Ewentualny osobny dowód
  twierdzenia o triangulacji pozostaje propozycją rozbudowy do oceny
  po zakończeniu całego przeglądu.
- Poprawiono „kokcykl” na „kocykl”, nawiasy w definicji jądra operatora
  brzegu, błędne położenie odsyłacza do przykładu dysku i określenie
  „baza otoczenia” w obliczeniu orientacji odwzorowania antypodalnego.

### Ilustracje i skład

- Rysunek 9.1: nawiasy w wartości iloczynu zewnętrznego, łuk o właściwym
  środku i precyzyjny podpis odróżniający wybraną formę od pola
  euklidesowego. Dowolna 2-forma nie jest automatycznie polem powierzchni.
- Rysunek 9.2: oba łuki orientacji leżą dokładnie na obwodzie dysku.
- Rysunek 9.4: usunięto biały dysk i jego przerywany obwód, które
  sugerowały usunięcie całego otworu. Pozostaje jeden zaznaczony punkt;
  podpis wyjaśnia, że niebieski dysk jest fragmentem dziedziny.
- Rysunki 9.3 i 9.5 są merytorycznie poprawne. Do przykładu z dwoma
  trójkątami dopisano argument o składowych otoczenia po usunięciu
  wspólnego wierzchołka. Zwiększono odstępy w tabeli porównawczej.

### Kontrole w trakcie pracy

- Kontrola zakresu względem `f7df0ae`: źródło zmieniono tylko w rozdziale 9.
  Środowiska są zbilansowane, etykiety niepowtórzone, odsyłacze mają cele.
- Symboliczny rachunek form wielomianowych w stopniach 0–3 potwierdził
  d²=0, wzór Cartana porównany z niezależnym wzorem współrzędnych
  pochodnej Liego oraz tożsamość radialnego operatora homotopii.
- Wyznaczniki dla wszystkich 35 ścian standardowych sympleksów
  wymiarów 1–7 potwierdziły znaki (−1)^j z normalną zewnętrzną najpierw.
- Sprawdzono tożsamość hδ+δh=id dla rozszerzonego kompleksu Čecha
  z pięcioma indeksami w stopniach 0–4, w tym indeksy powtórzone.
  Rozpisano też znaki stożka porównania tabel w samym dowodzie.
  Te kontrole są pomocnicze; uzasadnienia ogólne pozostają w tekście.
- Obejrzano wszystkie 21 stron rozdziału (148–168 PDF po drugiej kompilacji,
  przed przesunięciem numeracji przez nowy commit Darka)
  oraz pięć stron z ilustracjami w większej rozdzielczości.
- Sprawdzono materiał porównawczy o formach i kohomologii w
  [notatkach Gualtieriego](https://www.math.toronto.edu/mgualt/courses/17-1300/docs/17-1300-notes-13.pdf)
  oraz wskazane w rozdziale źródła MIT i Luriego. Nowy dowód sklejania
  jest rozpisany bez przyjmowania istnienia dobrego pokrycia rozmaitości.

### Weryfikacja końcowa

- Po pobraniu zmian Darka ponownie sprawdzono zakres: względem `0d9857f`
  źródło przed i po rozdziale 9 pozostaje identyczne. Powtórzono kontrole
  odsyłaczy i rachunków. Niezależne macierze kompleksu podwójnego
  potwierdziły zgodność podanych znaków stożka kolumn ze stożkiem
  odwzorowania kompleksów całkowitych.
- Ponownie obejrzano wszystkie strony rozdziału w aktualnej numeracji
  157–177 oraz tabelę na stronie 175 w większej rozdzielczości.
  Pięć rysunków znajduje się teraz na stronach 158, 163, 165, 170 i 174.
- Końcowa kompilacja lokalnym MiKTeX dała 300 stron, bez błędów,
  nieznanych odsyłaczy, żądań ponownej kompilacji i ostrzeżeń `Overfull`.
  Pozostały dwa wcześniejsze `Underfull` w późniejszych rozdziałach
  oraz trzy automatyczne zmiany położenia ilustracji `h` na `ht`.
  Wbudowany kompilator edytora zwrócił status nieznany; potwierdzeniem
  kompilacji jest wynik lokalnego MiKTeX. PDF zaktualizowano ze źródłem.

Następna iteracja: rozdział 10 — „Tensor metryczny, długość i miara”.

## Rozdział 10 — tensor metryczny, długość i miara (2026-10-02–03)

Punkt wyjścia: `c4efcb0`. Aktualizacja repozytorium na początku iteracji
potwierdziła brak nowych commitów. Przeczytano cały rozdział (osiem sekcji,
dwie ilustracje); przegląd oraz poniższe kontrole zakończono.

### Definicje, modele i odległość

- Oddzielono zapowiedź zachowania geodezyjnych i krzywizny przez izometrie
  od bieżącego wywodu: dowód tych dwóch własności korzysta z definicji
  następnych rozdziałów, co teraz wskazano wprost. Długość, odległość
  i miara są dalej rozwijane niezależnie od tych przyszłych pojęć.
- Dopisano R>0 przy sferze. W przykładzie Schwarzschilda doprecyzowano
  asymptotyczne unormowanie czasu i podano czas własny obserwatora
  statycznego: dτ=√(1−2M/r) dt.
- Dla Kerra obliczono wyznacznik Σ zmiany bazy różniczek t,φ;
  uzasadnia to sygnaturę. Dodatnią określoność przekroju t=const
  potwierdza jawny dodatni współczynnik przy dφ², po przekształceniu
  nawiasu do (r²+a²)Σ+2Mr a² sin²θ. Poprawiono pisownię
  „pseudoriemannowska”.
- W definicji długości podano a<b, ciągłość krzywej i skończony podział
  na kawałki klasy C¹. Rozróżniono wektor prędkości i jego długość.
  Dla punktów w różnych składowych infimum pustej rodziny wynosi +∞;
  zwykłą metrykę otrzymujemy na każdej składowej osobno.
- Uściślono klasę regularności przeparametryzowania do stałej szybkości:
  dla regularnej krzywej C¹ jest ono C¹, dla krzywej odcinkami regularnej
  odpowiednio odcinkami C¹. Dodano niezmienniczość długości przy
  odwróceniu kierunku parametru.
- W dowodzie skończoności odległości użyto otwartych klas osiągalności
  krzywymi odcinkami C¹. Dopisano przypadek wymiaru 0 i pełną wersję
  argumentu lokalnego w półkulach przy brzegu.
- Poprawiono przykład ciągu 1/j w (0,1): indeksowanie zaczyna się od j=2.
- Rozpisano dolne oszacowanie długości drogi w kuli Poincarégo przez
  całkę 2|ρ′|/(1−ρ²), z jawnym użyciem absolutnej ciągłości ρ=|γ|.
  To obejmuje również przejścia przez środek, gdzie norma nie zawsze
  ma klasyczną pochodną. Promień osiąga dolne oszacowanie.

### Całkowanie i dywergencja

- Zwarty nośnik funkcji mierzalnej nie wystarcza do całkowalności.
  Definicję całki sformułowano dla funkcji nieujemnych (możliwa wartość
  +∞) albo całkowalnych bezwzględnie. Dodano miarę liczącą i formę
  objętościową ze znakiem w wymiarze 0.
- Przy całkowaniu po sferze wyjaśniono pominięcie biegunów i południka:
  mają zerową miarę powierzchniową w regularnych mapach, z twierdzenia
  Fubiniego. Nie traktujemy osobliwych współrzędnych jako poprawnej mapy.
- Przy wzorze z iloczynem wektorowym dopisano konieczne założenie
  euklidesowej metryki na R³, a przy całce strumienia jednokrotne
  pokrywanie fragmentu przez parametryzację.
- Uzasadniono gładkość gradientu przez gładką macierz odwrotną oraz
  niezależność lokalnej dywergencji od lokalnie stałych znaków orientacji.
- Skonstruowano zewnętrzną normalną jednostkową jako −∇s/|∇s| przy
  lokalnej funkcji brzegowej s≥0 i wyjaśniono zgodność na przecięciach.
- W dowodzie Gaussa wydzielono n=1: w zerowymiarowej przestrzeni
  stycznej brzegu nie zawsze istnieje „dodatnia baza”, więc użyto
  znaków punktów i kontrakcji formy. Twierdzenie wyraźnie obejmuje
  również przypadek nieorientowalny, już uzasadniony przez podział jedności.

### Miara Hausdorffa

- Doprecyzowano skończone i przeliczalne pokrycia, puste pokrycie,
  pomijanie pustych składników oraz brak dopuszczalnego pokrycia.
  Wykazano, że H⁰ rzeczywiście liczy punkty, także dla zbiorów nieskończonych.
- Dodano dowód, że konstrukcja daje miarę zewnętrzną, addytywną na
  zbiorach o dodatniej wzajemnej odległości. Kryterium Carathéodory’ego
  dla zbiorów domkniętych sprawdzono przez warstwy odległości od zbioru;
  z niego wynika mierzalność borelowska. Jest to potrzebne do późniejszego
  przeliczalnego rozcinania zbiorów w dowodzie równości miar.
- W lemacie Lipschitza użyto dodatnich stałych, unikając nieokreślonych
  iloczynów 0·∞; mapy stałe nadal są objęte twierdzeniem. Wyjaśniono,
  dlaczego pokrycia można ograniczać do samego podzbioru.
- Poprawiono „podrozmaitość zanurzona (bez samoprzecięć)” na precyzyjne
  założenie osadzenia. Sam brak samoprzecięć immersji nie zapewnia
  topologii podprzestrzeni. Rozróżniono składowe dla odległości wewnętrznej.
- W kroku euklidesowym osobno wykazano, że zbiór zerowej miary Lebesgue’a
  ma zerową miarę Hausdorffa: pokrycie drobnymi sześcianami ma koszt
  ograniczony stałą razy sumę ich objętości. Dzięki temu argument
  Vitalego nie zakłada już niejawnie właśnie dowodzonej równości miar.
- Zastąpiono „dostatecznie bliskie punkty” konkretnymi kulami B_r i B_3r.
  Wyjście z większej kuli kosztuje co najmniej 2r√(1−ε), co wystarcza
  do dolnego oszacowania dla każdej pary punktów w mniejszej kuli.
  Argument obejmuje półkule i drogi opuszczające dziedzinę mapy.
- Rozpisano współczynniki ((1−ε)/(1+ε))^(n/2) i odwrotne w porównaniu
  miar, przeliczalny rozkład dla ustalonego ε i dopiero późniejsze
  przejście ε→0, także dla zbiorów nieskończonej miary.
- Na podrozmaitości wykorzystano DF bliskie izometrycznemu włożeniu J.
  Całkowanie po odcinku parametrów daje dolną granicę odległości
  otoczenia, a obraz odcinka daje górną granicę odległości wewnętrznej.
  Razem z wyznacznikiem Grama dowodzi to równości obu miar z μ_h,
  bez twierdzenia, że same odległości są globalnie równe.

### Ilustracje

- Rysunek trzech modeli: czerwone wektory mają teraz dokładnie długość
  hiperboliczną 1, z uwzględnieniem skali narysowanej kuli. Profil
  hiperboloidy pochodzi ze wzoru t=√(1+r²), zamiast krzywych z ostrym
  czubkiem; dodano dwa przekroje i usunięto nieobjaśnioną złotą strzałkę.
- Rysunek pozostaje przed sekcją o metrykach lorentzowskich. Skrócono
  pierwszy nagłówek sekcji, który wcześniej łamał wyraz między wierszami.
- Rysunek parametryzacji powierzchni jest poprawny: odróżnia obszar
  parametrów, jego obraz, wektory styczne i normalną. Pozostawiono go.
  Określenie „Gram ich iloczynów” zastąpiono „macierzą Grama tych wektorów”.

### Weryfikacja rachunkowa i źródła

- Kontrola zakresu względem `c4efcb0` potwierdziła brak zmian poza
  rozdziałem 10. Etykiety są niepowtórzone, odsyłacze mają cele,
  środowiska są zbilansowane, rozdział zawiera dwie ilustracje.
- Symbolicznie sprawdzono cofnięcie i przeniesienie metryki przez
  ścinanie (u,v) ↦ (u,v+u²), metrykę sfery w obu układach współrzędnych,
  metrykę hiperboloidy, jej macierz odwrotną i wyznacznik.
- Oba przekształcenia między modelami hiperbolicznymi sprawdzono przez
  macierze Jacobiego; wzory odwrotne między kulą a półprzestrzenią przez
  złożenie w obu kierunkach. Są to kontrole w wymiarze 2; ogólny argument
  dla n znajduje się w tekście.
- Dla metryki Kerra obliczono niezależnie blok t,φ, wyraz mieszany,
  wyznacznik pełnej macierzy −Σ²sin²θ, dodatni współczynnik przestrzenny
  i granicę a=0 dającą Schwarzschilda.
- Sprawdzono całkę pola paraboloidy, całkę z² po sferze oraz przykład
  regularnej krzywej o zmiennej szybkości i jej przeparametryzowanie
  osiągające minimalną energię.
- Jako kontrolę wzorów na gęstość, normalną i dywergencję obliczono
  obie strony tożsamości Gaussa dla X=(xy,y²) w metryce hiperbolicznej
  na prostokącie [1,2]×[1,3]. Całka objętościowa i suma strumieni
  przez cztery krawędzie wynoszą log(3). Jest to pomocniczy rachunek
  z narożami, nie zastępstwo dowodu ogólnego twierdzenia.
- Wszystkie cztery strzałki na rysunku modeli mają normę hiperboliczną 1;
  pochodna profilu hiperboloidy w najniższym punkcie jest zerowa.
- Punkty odniesienia: wzory tensorów
  [Schwarzschilda](https://sites.science.oregonstate.edu/physics/coursewikis/GGR/_export/xhtml/book/ggr/schwarz.html)
  i [Kerra](https://sites.science.oregonstate.edu/coursewikis/GGR/book/content/kerr)
  w kursie Teviana Draya oraz twierdzenie Carathéodory’ego i dodatek A
  [notatek Gautama Iyera](https://www.math.cmu.edu/~gautam/sj/teaching/2022-23/720-measure/pdfs/measure.pdf).
  Nierówność izodiametryczna i twierdzenie Vitalego pozostają jawnie
  nazwanymi faktami z teorii miary; ich pełne dowody nie są deklarowane
  jako zawartość tego rozdziału. Aneks z podstawami miary jest kandydatem
  do listy możliwych rozszerzeń po przeglądzie całego skryptu.

### Kontrola końcowa

- Obejrzano wszystkie 18 stron rozdziału (178–195 PDF), a po korektach
  nagłówka i położenia ilustracji ponownie sprawdzono układ stron.
  Oba rysunki, na stronach 182 i 188, sprawdzono w większej rozdzielczości.
- Końcowa kompilacja lokalnym MiKTeX dała 303 strony. Brak błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostały dwa wcześniejsze `Underfull` w późniejszych rozdziałach
  oraz trzy automatyczne zmiany położenia ilustracji `h` na `ht`.
- Wbudowany kompilator ponownie zwrócił status nieznany; poprawną
  kompilację potwierdza lokalny MiKTeX. PDF zaktualizowano ze źródłem.
- Kontrole zakresu, odsyłaczy i rachunków zakończyły się poprawnie;
  `git diff --check` nie wykazał błędów. Przed wysłaniem ponownie
  sprawdzono serwer: brak nowych commitów do włączenia.

Następna iteracja: rozdział 11 — „Koneksje i transport równoległy”.

## Rozdział 11 — koneksje i transport równoległy (2026-10-03)

### Zakres i stan początkowy

- Pobrano stan zdalnego brancha `review/rozdzialy-matematyka`:
  brak nowych commitów względem `3735830`. Wcześniejsze zmiany Darka
  pozostają zachowane. Ta iteracja obejmuje wyłącznie rozdział 11,
  ten dziennik oraz wynikowy PDF.
- Przeczytano wszystkie sześć sekcji: aksjomaty i lokalne współczynniki,
  konstrukcję Leviego-Civity, przykłady modelowe, transport i tensory,
  Schwarzschilda i Kerra oraz wariację energii. Sprawdzono oba rysunki.

### Definicje i dowody

1. **Lokalność koneksji.** Dodano lemat i dowód z funkcją odcinającą.
   Aksjomaty początkowo dotyczą pól globalnych; przed użyciem lokalnej
   ramki trzeba uzasadnić ograniczanie koneksji do otwartych podzbiorów.
   Dowód wyjaśnia również zależność pierwszego argumentu tylko od
   wektora w punkcie. „Kierunek” zastąpiono „wektorem”, ponieważ
   długość tego wektora również wpływa na wynik.
2. **Transformacja symboli Christoffela.** Pokazano etap przed zmianą
   bazy, z którego pochodzi druga pochodna zmiany współrzędnych.
   Ułatwia to sprawdzenie kolejności indeksów i członu nietensorowego.
3. **Konstrukcja Koszula.** Poprawiono sformułowanie „współczynniki są
   kowektorem”: to całe `K(X,Y,·)` jest 1-formą. Dodano jawny wzór
   z czynnikiem 1/2 i odwrotną macierzą metryki oraz argument zgodności
   konstrukcji na przecięciach map. Pozostałe sprawdzenia wzoru Koszula
   i rzutowania pochodnej na podrozmaitość są poprawne.
4. **Izometrie a koneksje.** Rozwinięto użycie jednoznaczności:
   zdefiniowano przeniesioną koneksję i wskazano rolę naturalności
   nawiasu Liego oraz cofnięcia metryki. To uzasadnia porównywanie
   koneksji w różnych modelach hiperbolicznych.
5. **Pochodna wzdłuż dowolnej krzywej — istotna luka.** Wcześniejszy
   argument przez przedłużenie pola nie obejmował nawet krzywej stałej
   z polem `V(t)=t v`. Zastąpiono go pełnym sprawdzeniem transformacji
   `A` i `V` za pomocą jakobianu. Nie trzeba zakładać immersyjności,
   braku samoprzecięć ani niezerowej prędkości. Dodano wymaganie
   gładkości pola jako przekroju wiązki cofniętej.
6. **Zmiana parametru i sklejenia.** Udowodniono regułę łańcuchową
   dla pochodnej kowariantnej. Uzasadnia ona niezależność transportu
   od zachowującej orientację zmiany parametru. Dodano definicję
   transportu dla krzywych kawałkami gładkich i niezależność od
   zagęszczania podziału; obejmuje to sklejenia z narożnikiem.
7. **Istnienie transportu na całym odcinku.** Dodano oszacowanie
   normy rozwiązania przez nierówność Grönwalla oraz argument
   przedłużania rozwiązania z granicy na końcu przedziału.
   Regułę różniczkowania `g(V,W)` wyprowadzono we współrzędnych,
   także dla pól niemających przedłużenia poza krzywą.
8. **Założenia metryczne.** Zdanie o izometrii dla zamkniętej drogi
   wymaga koneksji zgodnej z metryką; dodano ten warunek. W sekcji
   o tensorach oddzielono ogólną koneksję afiniczną od szczególnego
   warunku `nabla g=0`. W dywergencji jawnie wskazano koneksję
   Leviego-Civity i ślad endomorfizmu `Y -> nabla_Y X`.
9. **Pochodne tensorów.** Uzasadniono, dlaczego wzór dla 1-formy jest
   liniowy nad funkcjami w argumencie wektorowym. Dodano definicję
   dla typu `(r,s)` przez różniczkowanie ewaluacji, wyjaśnienie
   tensorialności oraz istnienia i jednoznaczności rozszerzenia.
   Wyjaśniono znaki przy górnych i dolnych indeksach.
10. **Wariacja energii.** Doprecyzowano gładkość i założenie, że
    krzywa leży we wnętrzu rozmaitości. Inaczej dowolne małe wariacje
    współrzędnych mogą być niedopuszczalne. Dodano realizację pól
    wariacyjnych o zwartym nośniku, dowód użytej wersji lematu
    podstawowego rachunku wariacyjnego oraz przejście przez wiele map.
    Udowodniono także kierunek odwrotny: równanie geodezyjnej implikuje
    stacjonarność, bo wyrazy brzegowe na wewnętrznych punktach podziału
    się znoszą. Dodano zachowanie kwadratu normy prędkości i wyjaśnienie,
    dlaczego parametr geodezyjnej niestałej można zmieniać afinicznie.

### Przykłady, terminologia i ilustracje

- Doprecyzowano zakres współrzędnej kątowej w mapie biegunowej.
  W przykładzie sferycznym wyjaśniono, że pełny równoleżnik wymaga
  wielu map, lecz ramka ortonormalna skleja się i jest okresowa.
  Ustalono orientację pomiaru kąta transportu.
- Uzupełniono symetryczne symbole w modelu półprzestrzeni i informację
  o zerowaniu pozostałych. Wyjaśniono euklidesowy sens dolnych indeksów
  współrzędnych w modelu kuli i hiperboloidy: nie jest to obniżanie
  indeksu metryką hiperboliczną.
- Poprawiono pisownię „pseudoriemannowska”, użyto „ramka ortonormalna”
  i wyjaśniono „kontrakcję”. Mylące „odjęcie zmiany bazy” zastąpiono
  „uwzględnieniem zmiany bazy”, zgodnie ze znakiem we wzorze.
- Pierwszy rysunek zachowano jako schemat; podpis wyraźnie określa,
  że wygląd strzałek nie koduje metryki ani konkretnego kąta.
- Drugi rysunek zbudowano na nowo jako rzut ortogonalny sfery.
  Równoleżnik ma dokładnie `theta=pi/3`, a dwa wektory są przeciwne,
  zgodnie z obliczonym obrotem `-pi`. Oba wychodzą z oznaczonego punktu
  i mają tę samą skalę. Widoczność łuku wynika z iloczynu z kierunkiem
  obserwacji, a nie z arbitralnego podziału elipsy na połowy.
  Podpis wyjaśnia przesunięcie początku pętli na potrzeby rysunku.

### Kontrole rachunkowe

- Ponownie obliczono wszystkie symbole dla współrzędnych biegunowych,
  sfery, półpłaszczyzny, dysku Poincarégo i dwuwymiarowej hiperboloidy.
  Ogólne wzory wielowymiarowe sprawdzono bezpośrednio w tekście.
- Sprawdzono transformację zerowej koneksji kartezjańskiej do
  współrzędnych biegunowych i transformację pochodnej dowolnego pola
  na krzywej o jednocześnie zmiennym promieniu i kącie.
- Sprawdzono jednostkowe pola równoległe w modelach hiperbolicznych,
  pochodne ramki sferycznej, macierz rozwiązania transportu, jej
  ortogonalność oraz wartość `-I` po obiegu przy `theta=pi/3`.
- Ponownie wyliczono pełny zestaw symboli Schwarzschilda i wszystkie
  wypisane symbole Kerra, w tym znak członu mieszanego. Sprawdzono
  przejście `a=0` do Schwarzschilda. Istniejące wzory są poprawne.
- Sprawdzono zgodność równań Eulera–Lagrange'a z kowariantnym
  przyspieszeniem dla przykładu z niediagonalną macierzą metryki.
- Sprawdzono styczność wektora z rysunku sfery, jego rzut oraz
  punkty przejścia między widoczną i zasłoniętą częścią równoleżnika.
- Kontrole symboliczne wykonano w SymPy. Osobno sprawdzono zakres
  zmian, zgodność środowisk LaTeX, unikatowość etykiet i odsyłacze.
  Źródła porównawcze: rozdział 15
  [notatek Eckharda Meinrenkena](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)
  i wykład 7
  [notatek MIT 8.962](https://web.mit.edu/8.962/www/lecnotes/8_962TA-lec-all.pdf).

### Kontrola końcowa

- Obejrzano wszystkie 11 stron rozdziału (196–206 PDF), a oba rysunki
  na stronach 196 i 203 także w większej rozdzielczości. Po pierwszym
  oglądzie poprawiono kolizję podpisu ze sferycznym równoleżnikiem,
  odstęp opisu drogi i skrócono tytuł sekcji 11.3, aby nie łamał słowa
  „modelowych”. Ponownie sprawdzono wszystkie strony po korektach.
- Końcowa kompilacja lokalnym MiKTeX dała 305 stron. Brak błędów,
  niezdefiniowanych odsyłaczy, żądań kolejnej kompilacji i `Overfull`.
  Pozostał jeden `Underfull` w późniejszym rozdziale oraz trzy
  wcześniejsze automatyczne zmiany położenia ilustracji `h` na `ht`.
- Wbudowany kompilator zwrócił status nieznany; poprawną kompilację
  potwierdza lokalny MiKTeX. PDF zaktualizowano ze źródłem.
- Kontrole rachunkowe i zakresu zmian przeszły ponownie po końcowych
  poprawkach. `git diff --check` nie wykazał błędów. Ponowne pobranie
  stanu serwera potwierdziło brak nowych commitów do włączenia.

Następna iteracja: rozdział 12 — „Geodezyjne, odwzorowanie wykładnicze
i zupełność”.

## Rozdział 12 — geodezyjne, odwzorowanie wykładnicze i zupełność (2026-10-03)

### Zakres

- Pobrano stan serwera: brak nowych zmian względem `4c29411`.
  Przegląd obejmuje wszystkie sześć sekcji rozdziału i dziewięć
  ilustracji. Zmiany poza rozdziałem ograniczają się do tego dziennika
  oraz wygenerowanego PDF.

### Założenia i dowody lokalne

1. **Rozmaitości bez brzegu.** Dodano ogólne założenie i powtórzono
   je przy twierdzeniu Hopfa–Rinowa. Bez niego stwierdzenia są fałszywe:
   domknięty przedział jest zwarty, ale geodezyjnej dochodzącej do jego
   końca nie można przedłużyć. Określono też domyślny riemannowski
   charakter metryki i rozpatrywanie odległości w jednej składowej.
2. **Pierwsza wariacja długości.** Uzasadniono różniczkowanie normy
   przez jednostajną regularność na zwartym przedziale. Zamianę
   pochodnych kowariantnych wyprowadzono we współrzędnych; nie wymaga
   ona immersyjności odwzorowania wariacji. Doprecyzowano regularność
   kawałków i stały podział przy wzorze z wyrazami narożnikowymi.
3. **Dziedzina eksponenty.** Dodano otwartość `D_p`, jej gwiaździstość,
   gładkość eksponenty na całej dziedzinie i zależność od punktu
   bazowego. Podano ogólne prawo skalowania geodezyjnej, również
   potrzebne przy różniczkowaniu eksponenty dla ujemnego parametru.
   Opiera się to na otwartości dziedziny maksymalnego przepływu na `TM`.
4. **Współrzędne normalne w sygnaturze nieokreślonej.** Wyjaśniono,
   że macierz jednostkową zastępuje macierz sygnatury, a kula w
   przestrzeni stycznej korzysta z pomocniczej normy euklidesowej.
   Niezdegenerowana metryka nieokreślona sama nie definiuje normy.
5. **Minimalność radialnej geodezyjnej.** Wybrano większą dziedzinę
   dyfeomorfizmu, zawierającą domknięcie kuli użytej w dowodzie.
   Uzupełniono krok w punkcie centralnym: funkcja promienia wzdłuż
   drogi jest lipschitzowska i absolutnie ciągła, a jej pochodna jest
   zerowa prawie wszędzie na zbiorze zer. Argument działa również dla
   wielokrotnych powrotów do środka, nie tylko skończonego podziału.
6. **Przypadek równości.** Wykazano niemalejący promień i stały
   kierunek na jedynym końcowym przedziale, gdzie promień jest dodatni.
   Wyjaśniono dopuszczalność postojów; nie każda droga minimalna jest
   regularną reparametryzacją przez dyfeomorfizm. Osobno uwzględniono
   identyczne końce i drogę stałą.
7. **Małe kule.** Dodano równość małych kul metrycznych (otwartych
   i domkniętych) z obrazami kul przez eksponentę. Argument pierwszego
   wyjścia wyklucza krótsze drogi spoza otoczenia. Ten krok jest
   później potrzebny do zwartości sfer w dowodzie Hopfa–Rinowa.

### Modele i twierdzenie Hopfa–Rinowa

8. **Sfera.** Dopisano `R>0` i uzasadniono dolne ograniczenie długości
   drogi przechodzącej przez antypodę, przez pierwsze osiągnięcia
   poziomów zbliżających się do `pi R`. Wskazano obsługę niegładkości
   promienia przy przejściu przez punkt początkowy.
9. **Półprzestrzeń hiperboliczna.** Dodano jawne rozwiązanie półokręgu
   przez `tanh` i `cosh`, aby uzasadnić gładkie przejście przez punkt
   maksymalnej wysokości, gdzie wcześniejsze dzielenie przez pochodną
   wysokości nie działa. Oddzielono krzywe stałe i przypadek wymiaru 1.
10. **Hiperboloida.** Rozwinięto argument rzutowania pochodnej dla
    metryki lorentzowskiej otoczenia: wcześniejsze stwierdzenie
    dotyczyło otoczenia euklidesowego. Podano wzór `nabla_X Y =
    D_X Y - g(X,Y)x` i sprawdzono przyspieszenie. Wykazano pozostawanie
    na górnym płacie, istnienie przez cały czas oraz nierówność
    `-<p,q>_L >= 1`, z równością dokładnie dla `p=q`, potrzebną do
    użycia `arcosh`. W modelu dysku uzasadniono położenie środka
    okręgu poza dyskiem.
11. **Wykluczenie narożnika.** Zastąpiono argument wymagający kontroli
    promienia normalnego otoczenia przy zmieniającym się środku
    bezpośrednią wariacją. Wektor wariacyjny jest różnicą stycznych,
    a pierwsza pochodna długości wynosi minus kwadrat normy tej
    różnicy. Daje to ścisłe skrócenie narożnika bez dodatkowego
    twierdzenia o jednolitych otoczeniach normalnych.
12. **Zupełność.** W lemacie o jednej pełnej eksponencie dodano
    spójność i wskazano wcześniejsze uzasadnienie małych kul.
    W implikacji „zupełność metryczna => geodezyjna” wyodrębniono
    ciąg zbieżny do końca parametru, a następnie pełną granicę krzywej.
    Osobno uwzględniono geodezyjne stałe. Dla zwartej rozmaitości
    argument stosuje się składowa po składowej.
13. **Przebita płaszczyzna.** Dopisano rodzinę dróg o długościach
    `2+(pi-2)epsilon`, wykazującą, że infimum rzeczywiście wynosi 2.
    Wyjaśniono także warunek równości wykluczający osiągnięcie infimum.

### Czasoprzestrzenie i przekroje

14. **Lokalna maksymalność czasu własnego.** Uzupełniono brakujący
    krok: dlaczego przyszłościowa krzywa czasopodobna pozostająca
    w dostatecznie małym otoczeniu normalnym nie opuszcza obrazu
    przyszłego stożka. Dla `Q(exp_p v)=g_p(v,v)` lemat Gaussa daje
    `dQ(W)=2g(R,W)`. Na niezerowym świetlnym brzegu pochodna wzdłuż
    krzywej czasopodobnej jest ujemna, co wyklucza pierwsze wyjście.
    Lokalna współrzędna czasu wyklucza powrót do wierzchołka.
    Uzasadniono znak pochodnej radialnego czasu i całkowanie od jego
    zerowej wartości początkowej. Pozostają jawne ograniczenia do
    małego otoczenia i krzywych czasopodobnych; nie jest to twierdzenie
    o globalnej maksymalności w dowolnej czasoprzestrzeni.
15. **Schwarzschild.** Wyjaśniono redukcję do płaszczyzny równikowej
    przez odbicie i jednoznaczność danych początkowych. Dopisano pełne
    równanie radialnego przyspieszenia, z którego wynika warunek
    zerowania pochodnej potencjału dla orbity kołowej. Sama pochodna
    pierwszej całki nie uzasadnia tego w punkcie `dot r=0`.
16. **Kerr.** Powtórzono zakres parametrów i dziedzinę zewnętrzną;
    wskazano analogiczne ograniczenie pierwszej całki radialnej przy
    punktach zwrotnych. Istniejące wzory pędów, energii i dwóch
    kandydatów na prędkość kątową są poprawne.
17. **Przekroje przestrzenne.** Sprecyzowano, że ciąg Cauchy'ego
    zbliżający się do pominiętego horyzontu leży na ustalonym promieniu
    równikowym. Sam warunek zbiegania współrzędnej radialnej nie
    wystarcza przy dowolnie zmieniających się kątach. Poprawiono też
    odsyłacz na „Wniosek” zamiast „Twierdzenie”.

### Język i ilustracje

- „Minimizer” zastąpiono polskimi określeniami krzywej lub geodezyjnej
  minimalnej. Poprawiono „pseudoriemannowska”, rozróżnienie prędkości
  i jej normy oraz zapis kwadratów pochodnych.
- Na sferze zastąpiono arbitralne krzywe Béziera dokładnymi rzutami
  dwóch półokręgów wielkich kół. Równik rzutuje się na odcinek,
  zgodnie z położeniem biegunów w przyjętym kierunku obserwacji.
- Niespójny szkic hiperboloidy i płaszczyzny zastąpiono dokładnym
  przekrojem `z_2=0` z hiperbolą `(cosh u,sinh u,0)`, początkiem
  przestrzeni otaczającej oraz oznaczonymi parametrami punktów.
  Podpis precyzuje, że to przekrój, nie widok całej powierzchni.
- Odsunięto końce kolorowych fragmentów geodezyjnych hiperbolicznych
  od idealnego brzegu, który nie należy do rozmaitości.
- W diagramie czasu własnego poprawiono nachylenie promieni świetlnych
  na 45 stopni w skali użytych współrzędnych. Poprzedni stożek był
  zbyt wąski i umieszczał narysowaną krzywą czasopodobną poza nim.
  Sprawdzono również czasopodobność całej czerwonej krzywej Béziera.

### Sprawdzenia rachunkowe

- Kontrole symboliczne potwierdziły wzory eksponenty sfery i
  hiperboloidy, normy prędkości, przyspieszenia, metryki w radialnych
  współrzędnych riemannowskich i lorentzowskich, półokręgi hiperboliczne
  w obu orientacjach oraz wzory odległości w dysku i półpłaszczyźnie.
- Sprawdzono radialne równanie Schwarzschilda, promień i energię
  orbity fotonowej, pędy Kerra, normalizację prędkości, granicę
  `a=0`, oba pierwiastki równania orbit kołowych i ich normy.
- Kontrola zakresu zmian, etykiet, odsyłaczy i dziewięciu rysunków
  przeszła poprawnie. Testy symboliczne wykonano w SymPy.
- Punkty odniesienia: [dowód Daniela Spiegla](https://math.uchicago.edu/~may/REU2016/REUPapers/Spiegel.pdf),
  [notatki Eckharda Meinrenkena](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)
  oraz [postać metryki Kerra w kursie Teviana Draya](https://sites.science.oregonstate.edu/coursewikis/GGR/book/content/kerr).

### Kontrola końcowa

- Obejrzano wszystkie 15 stron rozdziału (207–221 PDF), w tym wszystkie
  dziewięć ilustracji w większej rozdzielczości. Po oglądzie rozdzielono
  nakładające się strzałki dwóch kierunków orbity Kerra, odsunięto
  podpisy od krzywych na rysunkach orbity fotonowej i przebitej
  płaszczyzny. Ilustracje hiperboliczne umieszczono przed nagłówkiem
  sekcji o twierdzeniu Hopfa–Rinowa. Poprawione strony sprawdzono ponownie.
- Końcowa kompilacja lokalnym MiKTeX: 307 stron, bez błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale oraz trzy
  wcześniejsze automatyczne zmiany ustawienia ilustracji `h` na `ht`.
- Wbudowany kompilator ponownie zwrócił status nieznany; wynik
  potwierdza kompilacja lokalna. PDF zaktualizowano ze źródłem.
- Ponownie wykonano kontrole zakresu i rachunków; `git diff --check`
  nie wykazał błędów. Ponowne pobranie stanu serwera potwierdziło
  brak nowych commitów do włączenia.

Następna iteracja: rozdział 13 — „Krzywizna: od transportu równoległego
do tensorów”.

## Iteracja 13 — Krzywizna (2026-10-04)

Przeczytano cały rozdział: tensor Riemanna i jego symetrie,
krzywiznę Gaussa, Ricciego i skalarną, modele, Schwarzschilda
i Kerra, płaskość, drugą wariację, pola Jacobiego, twierdzenia
porównawcze oraz Gaussa–Bonneta z uogólnieniami.

### Matematyka i dowody

- Dopisano domyślne założenie braku brzegu. Rozwijanie walca na
  płaszczyznę opisano lokalnie.
- Zdefiniowano rzeczywistą małą pętlę we współrzędnych normalnych
  i wyprowadzono znak oraz resztę wzoru na jej transport. Przy
  interpretacji „na jednostkę pola” uwzględniono pole równoległoboku.
- Naprawiono błędny zapis kwadratów we wzorze Gaussa. Dodano dowód
  symetrii Ricciego potrzebnej przy polaryzacji i doprecyzowano
  użycie symetrii par w dowodzie o stałej krzywiźnie.
- Wyjaśniono jednostajność reszt rozwinięcia małej kuli i związek
  współrzędnych normalnych z rzeczywistą kulą metryczną. Wyprowadzono
  obwód małego okręgu bez niedozwolonego różniczkowania symbolu O.
- Przy skalowaniu metryki rozróżniono niezmieniony tensor Ricciego
  typu (0,2), jego wartości na nowych jednostkowych wektorach oraz
  skalujące się krzywizny sekcyjną i skalarną.
- Dopisano dziedzinę i sygnaturę ramki Schwarzschilda. Usunięto
  niepopartą dalszą treścią obietnicę późniejszego rozkładu Weyla.
- W dowodzie płaskości zapisano homotopię liniową i obsługę dróg
  odcinkami gładkich. Wyprowadzono komutator pochodnych pól wzdłuż
  dowolnej mapy, także bez założenia immersji.
- Uzupełniono regularność krzywej minimalnej: lokalna równość
  długości wymusza promienie, brak narożnika skleja je w geodezyjną.
  Doprecyzowano niezerowość danych pola Jacobiego w przykładach.
- Dodano lemat o czasie cięcia: mierzalność, jedyność promieni,
  lokalną odwrotność, gładkość odległości i zerową miarę zbioru
  cięcia. Dowód miary wykorzystuje wykres czasu cięcia i Fubiniego,
  dzięki czemu nie wymaga jeszcze nieprzedstawionego twierdzenia
  Sarda ani Rademachera. Porównanie hesjanu ma jawne założenie
  zupełności i oddzielony przypadek zerowego wektora.
- Naprawiono końcowy argument Bishopa–Gromowa: wykazano lokalną
  absolutną ciągłość ilorazu, bo sama ciągłość i niedodatnia pochodna
  prawie wszędzie nie dowodzą monotoniczności. Dodano n >= 2.
- Pełne niezależne obliczenie symboliczne z metryki Kerra potwierdziło
  wszystkie składowe Ricciego i pełną kontrakcję Kretschmanna;
  na tej podstawie dodano kompletną tabelę krzywizny w ramce
  pseudoortonormalnej. Tekst zawiera ramkę, odwrotną metrykę,
  dwa pośrednie rachunki, wszystkie niezależne składowe, oba ślady
  i zliczenie składników pełnej kontrakcji, w tym ujemnych wkładów
  mieszanych. Wyjaśniono przedłużenie tożsamości wymiernych poza
  obszar rzeczywistości użytej ramki.
- Dla Kerra wyprowadzono metrykę we współrzędnych wpadających
  i obliczono jej wyznacznik. To uzasadnia usuwalność osobliwości
  współrzędnych na horyzoncie; sama skończoność jednego niezmiennika
  nie wystarczałaby do takiego wniosku. Założenie M > 0 pozwala
  wnioskować o osobliwości pierścieniowej z rozbieżności na równiku.
- W lemacie indeksowym dopisano ciągłość pól odcinkami gładkich
  i poprawiono brakujący znak pochodnej w całkowaniu przez części.
  Opis wersji Raucha odpowiada teraz dokładnie użytemu założeniu,
  bez nieprecyzyjnej obietnicy słabszego porównania.
- W przykładzie sprzężenia na sferze podano n >= 2, R > 0
  i niezerowe pole początkowe. W twierdzeniu Bonneta–Myersa
  uzupełniono jawne n >= 2 i oddzielono identyczne końce drogi.
- W Cartanie–Hadamardzie uzasadniono otwartość obrazów gałęzi
  odwrotnych, potrzebną w definicji nakrycia.
- Krzywiznę Gaussa abstrakcyjnej powierzchni zdefiniowano wewnętrznie;
  utożsamienie jej z iloczynem krzywizn głównych dotyczy zanurzenia
  w przestrzeni euklidesowej. Podano regularność łuków i zakres
  kątów w wersji Gaussa–Bonneta z narożnikami.
- Naprawiono argument o obrocie stycznej: ramka współrzędnych
  nie jest na ogół ortonormalna, więc przejście nie jest samym
  obrotem. Rozkład polarny macierzy i przedłużenie na dysk
  uzasadniają niezmienność liczby obrotów.
- Doprecyzowano gładką triangulację i niezdegenerowane kąty,
  a w przykładzie trójkąta założono, że rzeczywiście ogranicza dysk.
- W wersji stożkowej dodano brak brzegu i argument z nakryciem
  orientacyjnym dla powierzchni nieorientowalnych.
- Wyjaśniono niezmienniczość Pfaffianu przy dodatniej zmianie ramki
  i jego sklejanie w formę globalną. Rozpisano kontrakcję z symbolami
  antysymetrycznymi prowadzącą do współczynników 1, -4, 1 w 4D.
- Pełne twierdzenie Cherna–Gaussa–Bonneta pozostaje jawnie wskazanym
  wynikiem zewnętrznym, wymagającym teorii klas charakterystycznych.
  Jego wersja brzegowa jest oznaczona jako schemat bez definicji
  formy brzegowej i bez dowodu. Nie przedstawiamy testów wzoru jako
  dowodu ogólnego twierdzenia. Ewentualne pełne rozwinięcie tej teorii
  trafia do propozycji po zakończeniu całego przeglądu.
- W brzegowym przykładzie zastąpiono kulę otwartą kulą domkniętą.

### Terminologia i ilustracje

- Poprawiono zdanie o znikaniu pochodnych metryki we współrzędnych
  normalnych i użyto określenia „brak torsji”. Dla kąta od bieguna
  użyto „kąt biegunowy (kolatytuda)”, zamiast mylącej szerokości.
- Zastąpiono szkic siodła rzutem rzeczywistej powierzchni
  z siatką i przekrojami x = 0, y = 0 przez zaznaczony punkt.
  Złoty łuk na sferze jest rzeczywistym rzutem wielkiego okręgu.
- Ilustrację pól Jacobiego oparto na dokładnych rzutach południków,
  z poprawnym równikiem, wspólnymi biegunami i stycznym rzutem pola.
  Podpis wyjaśnia umowną skalę strzałki.
- Poprawiono podpis wykresu Raucha: jednakowa jest początkowa
  pochodna pola, a samo pole początkowo znika. Odsunięto etykiety
  krzywych od linii wykresu.
- Rysunek brzegu Gaussa–Bonneta zastąpiono ćwierćdyskiem, na którym
  T jest dokładnie styczny, JT wewnętrzny, a kąt narożnika jednoznaczny.
  Czapkę pokazano w jawnym rzucie od bieguna, z prawidłowym kierunkiem
  obiegu. Rozdzielono etykiety JT i kąta po kontroli PDF.
- W trójkącie Poincarégo zastąpiono zaokrąglone parametry okręgów
  dokładnymi zależnościami: boki są prostopadłe do brzegu dysku
  i kończą się dokładnie we wspólnych wierzchołkach.

### Weryfikacja

- Do repozytorium dodano `weryfikacja/rozdzial13_krzywizna.py`,
  aby rachunki dało się odtworzyć później. Uruchomienie:
  `uv run --with sympy python weryfikacja/rozdzial13_krzywizna.py`.
  Skrypt nie modyfikuje książki i nie zapisuje plików wynikowych.
- Skrypt wyprowadza Christoffela i Riemanna z metryki Kerra,
  sprawdza Ricciego, wszystkie 36 pozycji tabeli oraz pełną
  kontrakcję. Oddzielnie sprawdza zmianę współrzędnych na horyzoncie
  i wyznacznik metryki. Wszystkie kontrole przeszły poprawnie.
- Tożsamość 4D Pfaffianu sprawdzono dodatkowo na pięciu ogólnych
  algebraicznych tensorach krzywizny z dokładnymi całkowitoliczbowymi
  składowymi mieszanymi, zbudowanych z iloczynów Kulkarni–Nomizu.
  Jest to kontrola rachunku, nie zastępstwo dowodu.
- Kontrola źródła potwierdziła, że zmiany dotyczą tylko rozdziału 13;
  wcześniejsze i późniejsze rozdziały zachowano dokładnie. Sprawdzono
  unikalność etykiet, istnienie odsyłaczy, parowanie środowisk i osiem
  ilustracji. Pobranie stanu serwera nie wykazało nowych zmian.
- Punkty odniesienia: [kurs Davida Tonga](https://davidtong.org/teaching/general-relativity/grhtml/S6)
  oraz wskazane już w rozdziale źródła twierdzeń porównawczych
  i Gaussa–Bonneta. Nową tabelę Kerra i wzór przedłużenia sprawdzono
  bezpośrednio z metryki, niezależnie od tabel z literatury.

### Kontrola końcowa

- Obejrzano wszystkie 33 strony rozdziału (222–254 PDF), a osiem
  ilustracji również w większej rozdzielczości. Po poprawkach ponownie
  obejrzano rysunki siodła, wykres porównawczy i brzeg Gaussa–Bonneta.
  Przy rysowaniu siodła poprawiono nawiasowanie kwadratów ujemnych
  parametrów w TikZ i podniesiono kierunek obserwacji, by uniknąć
  nakładania się fragmentów rzutu.
- Końcowa kompilacja lokalnym MiKTeX: 310 stron, bez błędów,
  niezdefiniowanych odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale i trzy
  wcześniejsze automatyczne zmiany ustawienia ilustracji `h` na `ht`.
- Wbudowany kompilator zwrócił nieznany status; wynik potwierdza
  ukończona kompilacja lokalna. Zaktualizowano PDF razem ze źródłem.
- Końcowe kontrole zakresu i `git diff --check` przeszły poprawnie.
  Repozytorium zawiera również skrypt do samodzielnego ponowienia
  rachunków Kerra i Pfaffianu.

Następna iteracja: rozdział 14 — „Twierdzenie Sarda i transwersalność”.

## Iteracja 14 — Twierdzenie Sarda i transwersalność (2026-10-04)

Przeczytano cały rozdział: dowód Sarda, transwersalny przeciwobraz,
iloczyn włóknisty, brzeg, transwersalność parametryczną, przybliżanie
względne, zera przekrojów, gęstość funkcji Morse'a i lokalny wymiar
przestrzeni trajektorii. Pobranie zmian potwierdziło aktualność gałęzi.

- Wyjaśniono domyślne założenia: brak brzegu, Hausdorff, drugi
  aksjomat przeliczalności i znaczenie podrozmaitości z topologią
  podprzestrzeni. Domkniętość podrozmaitości nadal jest osobnym
  założeniem tam, gdzie jest potrzebna.
- Doprecyzowano definicję zbioru miary zero w mapie i lokalny
  argument Lipschitza na zwartej kostce. W dowodzie Sarda podano
  otwarte dziedziny przekrojów h_t zamiast całych przestrzeni.
  Sprawdzono indukcję, mierzalność obrazów, Fubiniego i oszacowanie
  Taylora; zasadniczy czterostopniowy dowód jest poprawny.
- Wyjaśniono zastosowanie Sarda osobno do wnętrza i brzegu oraz
  siłę warunku regularności ograniczenia do brzegu.
- Poprawiono lokalny zapis mapy plasterkowej i słowo
  „odzwierciedlenie” na „odwzorowanie”. W twierdzeniach o przecięciu,
  iloczynie włóknistym, brzegu i zerach przekrojów zaznaczono możliwy
  pusty przeciwobraz. Dla skończoności przecięcia wystarcza zwartość
  jednego zbioru i domkniętość drugiego; sama dyskretność nie wystarcza.
- Rozpisano argument przy brzegu: gładkie przedłużenie przez r = 0,
  odwracalny minor po zmiennych stycznych i funkcja odwrotna
  zachowująca współrzędną brzegową. Omówiono przypadki m < c i m = c.
- W transwersalności parametrycznej rozpatrzono również przestrzeń
  parametrów wymiaru zero, do której podana wersja Sarda nie stosuje
  się bezpośrednio. Wersję brzegową wyprowadzono z rzutów wnętrza W
  i jego brzegu, obu będących rozmaitościami bez brzegu.
- Dodano brakującą definicję używanej topologii C^r/C^infinity na
  zwartej dziedzinie. Wyjaśniono różnicę między kontrolą każdego
  skończonego rzędu a jednym wspólnym oszacowaniem wszystkich rzędów.
- Uzasadniono jednostajną zbieżność skonstruowanej rodziny w każdym
  C^r i homotopię w wypukłej kuli parametrów. W dowodzie względnym
  otwartość zastosowano do zwartego podzbioru, bez traktowania jego
  domknięcia jako gładkiej rozmaitości. Cała homotopia jest stała
  na zachowywanym otoczeniu C.
- Wyjaśniono kanoniczną pochodną pionową przekroju w zerze oraz
  brak zer przekroju transwersalnego, gdy r > m. Rozpisano prawo
  transformacji hesjanu i zgodność z hesjanem kowariantnym z rozdziału 13.
- Dopisano zwarte nośniki funkcji odcinających w konstrukcji Morse'a;
  w przykładzie na R² „małość” perturbacji dotyczy zbiorów zwartych.
- W zapowiedzi Smale'a wyjaśniono niezależność indeksu od metryki,
  potrzebę istnienia trajektorii na odpowiedniej półprostej czasu
  i lokalne użycie gałęzi immersji. Prostowanie pola stosuje się
  do pola na przecięciu. Oddzielono izolację od skończoności oraz
  lokalny iloraz od globalnego ilorazu Hausdorffa.
- Poprawiono wykres rodziny t² - a: wcześniej rysowano 0,62 t² - a.
  Obecnie wszystkie trzy panele i zaznaczone zera odpowiadają
  dokładnie parametrom -1/2, 0 i 1/2 oraz wzorowi w podpisie.

### Kontrola końcowa

- Obejrzano wszystkie 11 stron rozdziału (255–265 PDF), a wszystkie
  cztery ilustracje również w większej rozdzielczości. Okręgi
  poziomic, transwersalność prostych, parabole i kierunki przepływu
  siodła są zgodne z tekstem. Poprawiona rodzina parabol ma zera
  w zaznaczonych punktach t = ±sqrt(1/2).
- Zweryfikowano zmianę hesjanu przez regułę łańcucha, rangi
  różniczek w iloczynie włóknistym i transwersalności parametrycznej,
  oraz wymiar przecięcia i lokalnego ilorazu trajektorii. Nie dodawano
  testów odtwarzających sam tekst dowodów.
- Kontrola źródła względem początku iteracji potwierdziła, że
  zmiany dotyczą wyłącznie rozdziału 14. Etykiety są unikalne,
  odsyłacze istnieją, środowiska są sparowane; `git diff --check`
  nie wykazał błędów.
- Końcowa kompilacja lokalnym MiKTeX: 312 stron, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji i `Overfull`.
  Pozostał wcześniejszy `Underfull` w późniejszym rozdziale oraz
  trzy wcześniejsze automatyczne zmiany położenia ilustracji `h` na `ht`.
  Wbudowany kompilator ponownie nie potwierdził statusu; wynik
  potwierdza kompilacja lokalna. Zaktualizowano PDF.
- Porównano zakres twierdzeń z [wykładem 3 A. Rittera](https://people.maths.ox.ac.uk/ritter/morse-cambridge/lecture03.pdf),
  [wykładem 4](https://people.maths.ox.ac.uk/ritter/morse-cambridge/lecture04.pdf)
  i [notatkami M. Mügera](https://www.math.ru.nl/~mueger/diff_notes.pdf).
- Podczas końcowego pobrania wykryto commity `5915d4a` i `57de31e`,
  dodające i aktualizujące `do_zrobienia.md`. Włączono je przez
  fast-forward, zachowując plik bez zmian. Lista jest materiałem
  do końcowej propozycji rozszerzeń; nie rozszerza bieżącej iteracji.

Następna iteracja: rozdział 15 — „Zanurzenia i otoczenia podrozmaitości”.

## Iteracja 15 — Zanurzenia i otoczenia podrozmaitości

Punkt wyjścia: `bde2d8d`. Przeczytano cały rozdział, łącznie
z dowodami obu twierdzeń Whitneya i czterema ilustracjami.
Pobranie zmian przed rozpoczęciem iteracji nie wykazało nowych commitów.

### Matematyka, terminologia i kompletność

- Ustalono domyślny brak brzegu, z wyraźnymi wyjątkami dla kołnierzy
  i wyczerpań. Ujednolicono „zanurzenie” w części o izotopiach.
  W dowodzie słabego twierdzenia Whitneya wybór skończonych map
  zachowuje pokrycie; nie polega na dowolnym zmniejszeniu ich dziedzin.
- W lemacie o dysku Whitneya dopisano zwartość M. Jest potrzebna
  w podanym dowodzie do skończoności par oraz oddzielenia otoczenia
  ruchu od pozostałego obrazu immersji. Samo założenie immersji
  nie wyklucza gromadzenia się innych płatów.
- Rozpisano względne położenie ogólne dysku: perturbacje wartości
  i różniczki funkcjami odcinającymi, kowymiar warstw macierzy
  niepełnego rzędu, następnie eliminacja samoprzecięć i przecięć
  z M. Sam ujemny oczekiwany wymiar samoprzecięć nie dowodzi immersji.
- Doprecyzowano obramowanie dysku: przedłużamy rozkład na dwie
  podwiązki; na drugim łuku przepisujemy dopełnienie kierunków
  drugiego płata. Dowiedziono potrzebnej własności grupy podstawowej
  grassmannianu przez jego zorientowane nakrycie i wiązania grup SO.
  Wyjaśniono rolę przeciwnych znaków oraz różnicę między przedłużeniem
  rozkładu a przedłużeniem dowolnej pełnej ramki na brzegu.
- Dodano jawny model ruchu dwóch wykresów w dysku Whitneya,
  sposób pogrubienia i powód niezależności użycia późniejszego
  twierdzenia tubularnego. Uściślono zastosowanie tego twierdzenia
  do powierzchni przedłużonej poza brzeg i naroża dysku.
- Uzupełniono graniczny argument dla siecznych, skończoną rodzinę
  perturbacji usuwających trójki, weryfikację rangi immersji W,
  standardowe sklejenie M z przebitą sferą i skończoność składowych.
  W zanurzeniu RP² zaznaczono normalizację współrzędnych jednorodnych.
- Dowód tubularny działa teraz dla dowolnej ustalonej metryki g.
  Poprzednio dowód zmieniał ją w przypadku niezwartym. Zastąpiono
  zmianę metryki jednolitym oszacowaniem zmiany wartości funkcji
  wyczerpującej na krótkich wektorach nad zwartym zbiorem.
  Wyjaśniono też zgodność map wykładniczych po ograniczeniu do
  otwartego otoczenia niedomkniętej podrozmaitości.
- W homologii wskazano abelową grupę współczynników. Rozróżniono
  otwarty dysk wiązki i domknięty dysk używany w danych chirurgii;
  uzasadniono wspólny promień dla nieortonormalnego obramowania.
- Zastąpiono niepełny globalny argument kołnierzowy dowodem
  z jednoznaczności trajektorii: spotkanie dwóch trajektorii
  wymuszałoby powrót jednej z wnętrza na brzeg. Podano konstrukcję
  gładkiej zmiennej szerokości i różniczkę w każdym punkcie kołnierza.
  Usunięto zbędne założenie pomocniczej zupełnej metryki.
- W podwojeniu sprawdzono Hausdorffa i przeliczalną bazę.
  Rodzinę kołnierzy przy zwartym brzegu przedłużono do izotopii
  ustalonej na brzegu, co uzasadnia dyfeomorfizm podwojeń.
  Wyjaśniono zmianę metryki przy przenoszeniu map tubularnych izotopią.
- Dopisano ciągłość w definicji wyczerpania, względną zwartość
  użytego pokrycia i wspólne otoczenie zerowania ogona szeregu.
  Przy konstrukcji Morse'a ustalono porównywalne normy pochodnych
  oraz przesunięto końcową funkcję do wartości nieujemnych: teraz
  wszystkie podpoziomice są zwarte. Sama właściwość funkcji do R
  nie zapewnia tego bez ograniczenia od dołu.
- W dowodzie zupełności uwzględniono brzeg i rozmaitości niespójne.
  W twierdzeniu o pasie dopisano cofanie przepływu do poziomicy a
  i przypadek pustej poziomicy; poprawiono składnię założenia.

### Ilustracje

- Dysk Whitneya: zastąpiono niezależne krzywe Béziera dwiema
  parabolami. Zaznaczone punkty są teraz dokładnie ich przecięciami,
  a wypełnienie ma granicę na obu narysowanych łukach.
- Otoczenie tubularne: użyto jednej analitycznej krzywej i jej
  jednostkowych normalnych. Strzałki są rzeczywiście prostopadłe,
  a brzegi pasa stanowią odsunięcia wzdłuż tych normalnych.
- Kołnierz: wyróżniono trajektorię wskazanego punktu p i przeniesiono
  jej podpis do właściwej strzałki.
- Pas bez punktów krytycznych: poziomice wyprostowano we współrzędnych
  produktowych przepływu i opisano te współrzędne w podpisie.
  Etykieta pola nie zasłania już strzałek.

### Kontrola końcowa

- Zakres argumentu Whitneya porównano z
  [wykładami T. Mrowki 21–22](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/d0598b3b5ced2d2d0a9884ee14abeae3_lecture21_22.pdf).
  Dodatkowe rachunki rang, model ruchu, szczegóły zwartości i dowód
  własności grassmannianu rozpisano bezpośrednio w tekście.
- W ostatnim sprawdzeniu rozwinięto również argument o podnoszeniu
  pętli i dysków w wiązaniach grup SO. Nie pozostawiono samego
  powołania się na długi ciąg homotopii wiązania: wyjaśniono potrzebne
  własności przez lokalne trywializacje oraz znikanie π₁ i π₂ sfer
  wymiaru co najmniej trzy.
- Skontrolowano wszystkie 15 stron rozdziału (266–280 PDF), a cztery
  ilustracje także w większej rozdzielczości. Po kontroli przeniesiono
  jeszcze podpis trajektorii poza linię ograniczającą pas kołnierza.
- Zweryfikowano rachunki różniczek, warstwy macierzy rzędu r,
  rozkład wiązki normalnej, indeksy promieni nad pierścieniami
  wyczerpania oraz odwrotność mapy produktowej z przepływu.
  Dla krzywej ilustracji normalna ma postać (-h',1)/sqrt(1+h'²),
  więc jej iloczyn skalarny ze styczną (1,h') jest równy zeru.
- Kontrola względem początku iteracji potwierdziła, że źródło
  poza rozdziałem 15 nie zmieniło się. Etykiety są unikalne,
  odsyłacze istnieją i środowiska są sparowane; `git diff --check`
  nie wykazał błędów.
- Końcowa kompilacja lokalnym MiKTeX daje 315 stron, bez błędów,
  brakujących odsyłaczy, żądań powtórzenia kompilacji i `Overfull`.
  Zaktualizowano PDF. Wbudowany kompilator
  nie potwierdził statusu; wynik sprawdzono lokalnie. Pozostał
  wcześniejszy `Underfull` w późniejszym rozdziale i trzy wcześniejsze
  automatyczne zmiany położenia ilustracji `h` na `ht`.
  Błąd kolizji nazwy pomocniczej funkcji TikZ z nazwą wbudowaną
  usunięto, nadając funkcjom rysunku odrębne nazwy.
- Końcowe pobranie zmian z repozytorium nie wykazało nowych commitów.

Następna iteracja: rozdział 16 — „Przecięcia, dualność i klasy charakterystyczne”.

## Iteracja 16 — Przecięcia, dualność i klasy charakterystyczne

Punkt wyjścia: `f3d1458`. Pobrano zmiany (repozytorium aktualne)
i przeczytano wszystkie dziesięć sekcji oraz cztery ilustracje.

### Zmiany i ich uzasadnienie (uzupełniane podczas przeglądu)

- Iloczyn kubkowy zdefiniowano także nad Z i wskazano rosnący
  porządek wierzchołków. Poprawiono dowód reguły Leibniza:
  skracają się dwa dodatkowe wyrazy prawej strony, a nie wyrazy
  lewego kobrzegu. Dopisano znak przy zmianie drugiego czynnika.
- Zastąpiono nieuzasadnione utożsamienie końców pryzmatu z dwiema
  przekątnymi konstrukcją homotopii łańcuchowej między mapą
  Alexandera–Whitneya i jej zamianą czynników. Wypełnienia cykli
  istnieją w ściągalnych kompleksach przypisanych sympleksom.
- Dodano brakującą definicję iloczynu kapowego, jego wzór na brzeg
  i zgodność ewaluacji z iloczynem kubkowym. Ustalono jedną
  kolejność czynników dla dalszych rachunków znaków.
- W dualności wyprowadzono jawnie znak (-1)^(k+1) przy brzegu
  komórki dualnej. Usunięto arbitralną zmianę orientacji stopni,
  która bez komentarza zmieniałaby znak deklarowanej mapy kapowej.
  Podano ewentualny czynnik przeskalowania i argument homotopii
  porównującej mapę komórek dualnych z iloczynem kapowym.
- Przy brzegu rozróżniono klasę względną i lokalną homologię:
  ta ostatnia w punkcie brzegu jest zerowa. System orientacji
  określa się tam przez przestrzeń styczną lub kołnierz.
  Uzupełniono jedyność klasy względnej, jej brzeg i przypadek n=0.
- Wyjaśniono, dlaczego dualne komórki do sympleksów niebrzegowych
  tworzą podkompleks obliczający homologię M: wnętrze cofa się
  na niego przez normalizację wag barycentrycznych, a kołnierz
  porównuje wnętrze z całą rozmaitością.
- Uściślono abelowość grup współczynników. W klasyfikacji przez
  równik dopisano normalizację całej homotopii, nie tylko pojedynczej
  mapy, aby uzasadnić użycie opartych grup homotopii, i wymaganie
  zachowania orientacji przez izomorfizmy. Podano jawnie obie
  względne wersje dualności ze skręconymi współczynnikami.
- Równość przecięcia i iloczynu kubkowego uzasadniono całkowitymi
  względnymi klasami Thoma, wycięciem i lokalizacją na punktach
  przecięcia. Rachunek form przy punkcie służy tylko kontroli
  orientacji; nie zastępuje argumentu nad Z.
- Uzupełniono przejście od znaków funkcji przejścia w definicji
  w₁ do kohomologii singularnej przez monodromię pętli i H¹.
  Dopisano gładkość ram i wygładzenie homotopii w sklejaniu wiązek.
- W konstrukcji wᵢ dopisano brakujące uzasadnienie bazy
  1,x,…,x^(r−1) na włóknie projektowym: hiperpłaszczyzny są dualne
  do w₁ tautologicznej linii, a ich transwersalne przecięcia
  wykrywają kolejne potęgi. Uwzględniono rząd zero i zgodność
  nowego współczynnika w₁ z wcześniejszą definicją przez wyznaczniki.
- Rozdzielono niezależną klasę Eulera modulo 2 od nazwy wᵣ.
  Najpierw dowodzi się jej własności z klasy Thoma, potem
  e₂(L)=w₁(L) dla linii, a dopiero przez rozszczepienie e₂(E)=wᵣ(E).
  Dzięki temu argument dla sumy Whitneya nie zakłada swojego wniosku.
- Dopisano uzasadnienie zgodności w₂ z przeszkodą spinową:
  redukcję do 2-szkieletu, rozszczepienie części trywialnej,
  płaszczyznową klasę Eulera i parzystość nawinięcia w SO(2).
- W dowodzie Thoma zbudowano globalny kocykl w kompleksie
  komórkowym pary, zamiast uznawać lokalne generatory za automatycznie
  sklejone. Uściślono jedyność, niezwartą bazę, zapominanie względności
  przed cofnięciem do zera i iloczyn względny dla sumy wiązek.
- W twierdzeniu o zerach ustalono orientację „normalna, styczna”
  i cofnięcie klasy pary (E,E bez przekroju zerowego).
  Przy samoprzecięciu podano konieczne założenie orientacji otoczenia
  oraz konkretną orientację normalnej „styczna, normalna”.
  Macierz blokowa bezpośrednio potwierdza znak lokalnego stopnia.
- W indeksie zera uzasadniono niezależność od mapy i wskazano
  konwencje n=1 oraz n=0. Doprecyzowano użycie funkcji uwikłanej
  z parametrem przy krótkim przepływie, wykluczając dodatkowe
  punkty stałe zarówno blisko zer, jak i na zwartym dopełnieniu.
- Zastąpiono skrótowy rachunek śladu Lefschetza obliczeniem klasy
  przekątnej w dualnych bazach kohomologii. Wyprowadzono wszystkie
  znaki, lokalną macierz grafu i przekątnej oraz przejście do śladu;
  potrzebną formułę Künnetha nad Q uzasadniono na kompleksach.
- Dla formy przecięcia podano termin „unimodularna”, konkretny
  znak izomorfizmu z kratą dualną i niezależność od reprezentantów
  modulo torsja. Symetrię wyprowadzono z iloczynu kubkowego,
  bez założenia, że każda klasa ma reprezentanta podrozmaitościowego.
- W chirurgii rozróżniono wymiar operowanej sfery i indeks uchwytu
  jej śladu. Ustalono sklejenie wyznaczone przez obramowanie,
  rolę kołnierzy i warunek zachowania orientacji. Dwa walce dają
  torus przy odpowiednim sklejeniu; bez tego warunku możliwa jest
  butelka Kleina. Uzupełniono rachunek charakterystyki Eulera.

### Ilustracje i kontrola końcowa

- W komórce dualnej użyto dokładnych barycentrów, a podpis
  przeniesiono do wnętrza dysku, aby nie przecinał krawędzi triangulacji.
- Na sferze zastąpiono dowolne pionowe strzałki rzutami rzeczywistych
  południkowych trajektorii gradientu wysokości. Podano wzór pola.
- Dodano niezależny, niewymagający bibliotek skrypt
  `weryfikacja/rozdzial16_znaki.py`: 8540 par bazowych kołańcuchów
  dla Leibniza, 247 przypadków wzoru kapowego oraz 128 macierzy
  dla porównania klasy przekątnej z det(I−A) w wymiarach 1–4.
  Wszystkie kontrole przechodzą. Zakres skryptu jest rachunkowy;
  nie zastępuje dowodów dualności, triangulacji czy twierdzenia Thoma.
- Obejrzano cały rozdział (17 stron, 281–297 PDF), a wszystkie
  cztery ilustracje również w większej rozdzielczości. Rysunki
  torusa i sklejania wiązki na równiku zachowano po kontroli.
- Sprawdzono dodatkowo porządek orientacji w samoprzecięciu,
  względny charakter przeszkody w₂ na 2-komórce oraz brak
  cyklicznej zależności między klasą Thoma i konstrukcją wᵢ.
- Końcowa kompilacja lokalnym MiKTeX: 319 stron, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`.
  Wbudowany kompilator nie potwierdził statusu; wynik zweryfikowano
  lokalnie. Pozostały trzy wcześniejsze zmiany położenia ilustracji
  `h` na `ht`. Przeredagowanie początku dowodu Thoma usunęło
  wcześniejszy `Underfull`; skład tego akapitu obejrzano.
  Zaktualizowano PDF.
- Kontrola zakresu względem `f3d1458` potwierdziła, że źródło
  poza rozdziałem 16 jest identyczne. Wszystkie etykiety są unikalne,
  odsyłacze istnieją, środowiska są sparowane i `git diff --check`
  przechodzi. Końcowe pobranie nie wykazało nowych commitów.
- Konwencję kapową i zakres twierdzeń porównano z
  [A. Hatcherem, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  a zależności w konstrukcji klas z
  [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
  oraz [wykładami R. Cohena](https://math.stanford.edu/~ralph/bookR4.pdf).
  Rozwinięcia dowodów i kontrole rachunkowe zapisano w repozytorium.

Następna iteracja: rozdział 17 — „Teoria Morse'a: punkty krytyczne, uchwyty i przepływ”.

## Iteracja 17 — Teoria Morse'a: punkty krytyczne, uchwyty i przepływ

Punkt wyjścia: `f3222f9`; pobranie zmian na początku iteracji
nie wykazało nowych commitów. Przegląd obejmuje cały rozdział 17.

### Matematyka i uzupełnienia dowodów

- W lemacie Morse'a wyjaśniono gładkość pierwiastka macierzy
  przez lokalnie jednostajną zbieżność szeregów pochodnych.
  Osobno uwzględniono indeksy 0 i n, bez odwracania pustych bloków.
- Poprawiono sprzeczne założenie przy uchwycie: regularne są
  końce a,b, natomiast c=f(p) jest wartością krytyczną.
- Zastąpiono nieuzasadnioną globalną deformację za pomocą pola Y
  jawnym uchwytem H={|v|≤r, |u|²≤ε+|v|²}. Podano jego parametryzację
  i dokładne przecięcie z dolną podpoziomicą. Poprzednie twierdzenie,
  że tylko punkty v=0 mogą nie dojść do dolnego poziomu, było błędne:
  w obszarze μ=0 także inne punkty mogą asymptotycznie zbiegać do rdzenia.
- Uzasadniono zaokrąglanie naroży z zachowaniem poprzeczności,
  skończony i gładki czas trafienia oraz produktową postać dopełnienia.
  Przy przejściu od uchwytu do komórki użyto homotopii mapy
  przyczepienia i kołnierzy. Samo kurczenie czynnika poprzecznego
  nie unieruchamia punktowo pierwotnej części przyczepianej.
  Doprecyzowano wycięcie i przypadki skrajnych indeksów.
- Aproksymację komórkową umieszczono w każdym kroku indukcji
  budującej CW, zanim nowa komórka zostanie dołączona.
- Rozszerzono dowód rozmaitości stabilnej na dowolną gładką metrykę,
  zgodnie z zakresem późniejszych twierdzeń. Podano liniowy rozkład
  spektralny, równania całkowe, normę z wagą wykładniczą, oszacowanie
  kontrakcji, gładką zależność i globalne przedłużenie kołnierzem.
  Dla metryki euklidesowej podano jawną parametryzację przez R^m.
- Iloraz trajektorii zidentyfikowano z globalnym przekrojem regularnym,
  uzasadniając jego strukturę rozmaitości i własność Hausdorffa.
  Rozróżniono przecięcie rozmaitości immersowanych od założenia,
  że ich obrazy są globalnie osadzone.
- W dowodzie gęstości metryk Morse'a–Smale'a użyto stałych lokalnych
  sfer oraz map pierwszego trafienia. Warunki z czasami ≤N są otwarte
  i gęste; zwartość parametrów uzasadnia oba stwierdzenia.
  Wyjaśniono przestrzeń Baire'a i zachowanie metryki blisko punktów
  krytycznych. Poprzednie „zwarte fragmenty” zależały od zmienianej metryki.
- Dodano osobny lemat o zwartości z przełamaniami: wybór podciągu
  na skończenie wielu poziomach, ograniczenie czasu w regularnym paśmie,
  wykluczenie skoku między różnymi punktami tej samej wartości
  przez oszacowanie spadku ≥ długość razy dolne ograniczenie gradientu,
  zachowanie końców i topologię przestrzeni trajektorii łamanych.
- Sklejanie trajektorii rozpisano na mapy wykresów i jawne równania
  θ=A(δρω), ω=B(δρθ); ich różniczka przy ρ=0 jest identycznością.
  Dla ogólnej metryki dodano problem z mieszanymi warunkami końcowymi
  oraz oszacowania map przejścia. Nie założono nieuprawnionej gładkiej
  linearyzacji gradientu. Do brzegu przestrzeni jednowymiarowej wystarcza
  kołnierz topologiczny, gładki we wnętrzu; nie twierdzimy, że ewaluacja
  jest gładka na brzegu w dowolnie wybranym parametrze.
- Ustalono orientację przekroju przez kolejność „X, przekrój”
  oraz koorientację rozmaitości stabilnej. W dowodzie ∂²=0
  oddzielono iloczyn znaków trajektorii od wspólnego znaku konwencji
  zależnego wyłącznie od wymiarów, który nie wpływa na zerowanie sumy.
- Porównanie z homologią komórkową przebudowano wokół filtracji
  według indeksów. Jawnie wskazano odwołanie naprzód do geometrycznego
  twierdzenia o przestawianiu w rozdziale 18 i brak zależności kołowej.
  Zmiana funkcji zachowuje pole i trajektorie; podano metrykę realizującą
  to samo pole jako ujemny gradient nowej funkcji.
- Generatory względne reprezentują dyski niestabilne przedłużone
  do wspólnego poziomu; współczynniki odczytują współrdzenie stabilne.
  Wyjaśniono osiąganie poziomu, lokalny stopień i zgodność znaków.
  Usunięto niepoprawny termin „kokorem”; użyto „współrdzeń”.

### Ilustracje i kontrola

- W lokalnych poziomicach tło zmieniono na neutralne, aby niebieski
  oznaczał wyłącznie podpoziomicę.
- Rysunek uchwytów zastąpiono widokiem z góry z dokładnymi szwami
  na brzegach. Poprzednia perspektywa pokazywała końce mostka wewnątrz dysków.
- Na sferze użyto rzeczywistych rzutów południków zamiast dowolnych krzywych.
  Równik pokazano jako odcinek, zgodnie z tym samym rzutem prostopadłym.
- Sprawdzono rachunek czterech punktów krytycznych przechylonej wysokości
  torusa, nierówności Morse'a i dowód twierdzenia Reeba; zachowano wyniki.
- Kontekst i zakres twierdzeń porównano z
  [wykładami R. Cohena](https://math.stanford.edu/~ralph/morsecourse/biglectures.pdf),
  [wykładami A. Rittera](https://people.maths.ox.ac.uk/ritter/morse-cambridge/full.pdf)
  i [pracą J. Webera](https://arxiv.org/abs/math/0411465).
  Dodano odsyłacz do tej ostatniej pracy w dalszej lekturze.
- Kontrola zakresu względem `f3222f9`: poza rozdziałem 17 źródło
  pozostało identyczne. Etykiety są unikalne, odsyłacze istnieją,
  środowiska są sparowane; rozdział zawiera pięć ilustracji.
- Obejrzano wszystkie 15 stron rozdziału (298–312 PDF) i każdą
  z pięciu ilustracji w większej rozdzielczości. Rysunek torusa
  oraz schemat trajektorii łamanej zachowano po kontroli.
- Końcowy skład lokalnym MiKTeX: 322 strony, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`. Pozostały trzy wcześniejsze ostrzeżenia zmieniające
  położenie ilustracji z `h` na `ht`. Wbudowany kompilator zwrócił
  nieznany status, dlatego wynik zweryfikowano lokalnie.
  Zaktualizowano PDF. `git diff --check` przechodzi.
- Ponowne pobranie zmian przed zapisem nie wykazało nowych commitów.

Następna iteracja: rozdział 18 — „Kobordyzmy i rachunek uchwytów”.
Przy jego przeglądzie trzeba również sprawdzić zgodność twierdzenia
o przestawianiu z używaną tutaj wersją zachowującą pole spadku.

## Iteracja 18 — Kobordyzmy i rachunek uchwytów

Punkt wyjścia: `af689aa`; pobranie zmian na początku iteracji
nie wykazało nowych commitów. Przegląd obejmuje cały rozdział 18.

### Poprawki i ich uzasadnienie

- Ustalono wymiar m≥1 oraz konwencję kobordyzmu zorientowanego
  ∂W=(−N₋)∐N₊. Usunięto sugestię, że całkowity kompleks uchwytów
  wymaga orientowalnego W: wystarczają orientacje rdzeni
  i koorientacje sfer pasa.
- Poprawiono dobór regularnych pasów w rozkładzie uchwytowym,
  uwzględniając brak punktów krytycznych, pusty brzeg wejściowy
  i składowe rozpoczynające się uchwytem indeksu 0.
- Dla dysku zastąpiono F=|x|² przez F=(1+|x|²)/2.
  Poprzedni wzór naruszał F⁻¹(0)=∅. Wskazano także współrzędną
  kołnierza, w której nowa funkcja ma wymaganą postać 1−t.
- Przy śladzie chirurgii odróżniono wnętrze części przyczepianej
  od jej brzegu, który przed wygładzeniem leży na narożu.
- W przykładzie S²→T² dodano konieczny warunek przedłużenia orientacji.
  Drugie sklejenie pierścieni daje butelkę Kleina, więc samo usunięcie
  dwóch dysków i wartość χ=0 nie wystarczają do stwierdzenia, że to torus.
- Dla bloku uchwytów jednego indeksu uzasadniono sprowadzenie ich sfer
  do wspólnego poziomu i rozłączność małych pogrubień przez brak
  trajektorii między równymi indeksami. Jawnie zapisano różniczkę
  filtracji względnej i lokalną konwencję znaku TA→νB.
- Rozwinięto algebraiczne skracanie przy współczynniku ±1:
  zerowanie wiersza i kolumny oraz użycie ∂²=0 wydzielają ściągalny
  podkompleks. To nadal nie dowodzi jednego przecięcia geometrycznego.
- Zdefiniowano używane pole gradientopodobne spadku i wyjaśniono,
  jak realizować je jako gradient metryki. Definicja obejmuje
  dowolną metrykę, a nie tylko szczególny model euklidesowy.
- Przebudowano dowód przestawiania: zwarte, rozłączne ślady stabilny
  i niestabilny w poziomicy pozwalają skonstruować gładką funkcję ρ
  stałą wzdłuż trajektorii, równą 1 przy p i 0 przy q.
  Udowodniono gładkość także tam, gdzie trajektorie nie trafiają
  w tę poziomicę. Dwie rosnące reparametryzacje hₚ,h_q dają
  F̃=ρhₚ(F)+(1−ρ)h_q(F), z XF̃<0 i translacjami przy punktach krytycznych.
  Całe pole pozostaje niezmienione. Jest to dokładnie wersja
  wymagana w dowodzie homologii Morse'a w rozdziale 17.
- W przesunięciu uchwytu użyto równoległej kopii sfery q,
  wyznaczonej przez obramowanie, i wstęgi omijającej pozostałe dane.
  Wskazano dysk Dᵏ×{v₀} w nowym brzegu: izotopia przebiega tam,
  a nie po rdzeniu we wnętrzu kobordyzmu. Dalsze przyklejenia
  także trzeba przenieść przez otrzymany dyfeomorfizm.
  Ustalony pozostaje brzeg wejściowy N₋; nie obiecuje się
  punktowego unieruchomienia całej wcześniej dołączonej części.
- W znoszeniu pary uzupełniono dostosowaną wersję lematu Morse'a
  zachowującą odpowiedni dysk stabilny/niestabilny. Pole można
  zmienić lokalnie przez wypukłe sklejenie pól spadku; nie zakładamy
  gładkiej linearyzacji dowolnego pierwotnego gradientu.
- Dopasowanie przekrojów rozpisano na gładką izotopię przez skalowanie
  i rozkład blokowy z dopełnieniem Schura. Wyjaśniono warunek
  odwracalności bloku poprzecznego, wybór znaków i kontrolę nośnika.
  Izotopię realizuje pole styczne do poziomic, dodane do pola
  znormalizowanego; funkcja nadal ściśle maleje.
- Argument braku powrotów zastosowano po zmianie pola, z dwoma
  otoczeniami V⊂U. Modyfikacja usuwająca zera ma nośnik w V,
  a model obowiązuje w U. Dopisano, dlaczego wyjście z U uniemożliwia
  powrót do V i dlaczego wszystkie trajektorie docierają do brzegów.
  Przy budowie funkcji końcowej uzasadniono gładkość czasu trafienia.
- W warunkowym użyciu triku Whitneya doprecyzowano jednoczesny wybór
  rozłącznych dysków dla sparowanych przecięć. Warunek obramowania
  oznacza przedłużenie obramowania zadanego na brzegu, a nie samą
  trywialność wiązki normalnej dysku. Wskazano zakres wymiarów,
  gdy trzeba faktycznie wykonać ruch.
- Przy torsji Whiteheada odróżniono kompleks nad Z od kompleksu
  nakrycia uniwersalnego nad Z[π₁]. Usunięto zapowiedź nieistniejącego
  jeszcze dalszego rozdziału chirurgii; pozostaje propozycją rozbudowy.

### Ilustracje i weryfikacja

- Poprawiono podpis każdej podstawy 1-uchwytu: pojedyncza podstawa
  to {−1}×D² albo {1}×D², a nie całe S⁰×D². Rdzeń dochodzi teraz
  do obu podstaw, a strzałka sfery pasa trafia w jej rzeczywisty brzeg.
- Wykresy znoszenia są dokładnie funkcjami t³/3−t oraz t³/3+t/2;
  punkty krytyczne zaznaczono w (±1,∓2/3), zgodnie ze wzorem modelu.
- Na ilustracji przesunięcia dodano przerywaną równoległą kopię
  sfery q i doprowadzono wstęgę do tej kopii. Podpis odróżnia
  ją od pozostającej na miejscu sfery przyczepienia drugiego uchwytu.
- Kontekst dowodu znoszenia i zakres wyników porównano z
  [wykładem J. Morgana](https://www.math.columbia.edu/~jmorgan/Lecture_IIIA_hcobordism_Contd.pdf)
  oraz [książką A. Ranickiego](https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf).
- Obejrzano cały rozdział (12 stron, 313–324 PDF) oraz wszystkie
  pięć ilustracji w większej rozdzielczości. Rysunki chirurgii
  i przecięcia na torusie zachowano po kontroli; poprawiony schemat
  przesunięcia obejrzano ponownie. Sprawdzono także odsyłacze do lektur.
- Końcowy skład lokalnym MiKTeX: 324 strony, bez błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji, `Overfull`
  i `Underfull`. Pozostały trzy wcześniejsze ostrzeżenia dotyczące
  zamiany położenia ilustracji `h` na `ht`. Wbudowany kompilator
  nie potwierdził statusu; wynik zweryfikowano lokalnie.
  Zaktualizowano PDF.
- Kontrola zakresu względem `af689aa` potwierdziła identyczność
  źródła poza rozdziałem 18, unikalność etykiet, poprawność odsyłaczy
  i sparowanie środowisk. `git diff --check` przechodzi.
  Ponowne pobranie przed zapisem nie wykazało nowych commitów.

Następna iteracja: ponowna kontrola rozdziału 1 po zmianach autora
pobranych podczas przeglądu późniejszych rozdziałów. Dopiero po niej
pozostaje końcowy audyt całości i lista propozycji rozbudowy do wyboru.

## Ponowny przegląd rozdziału 1 po zmianach autora

Punkt wyjścia: `7222128`. Ponownie sprawdzono fragmenty zmienione
od pierwszego przeglądu (`e144985`), w tym uzupełnienia autora
`0d9857f` i poprawkę relacji równoważności `5b259e6`.

### Matematyka, kolejność i język

- W przykładzie prostej z podwojonym początkiem dopisano dowód
  ciągłości map i ich odwrotności. Sama bijekcja nie wystarcza
  do stwierdzenia, że mapa jest homeomorfizmem.
- Analogicznie uzupełniono konstrukcję map CPⁿ: otwartość dziedzin,
  ilorazowość ograniczenia rzutowania, ciągłość ilorazów współrzędnych
  i odwrotności wstawiającej współrzędną 1. Dodano odsyłacz do
  późniejszego dowodu aksjomatu Hausdorffa i przeliczalności bazy,
  potrzebnych do uznania CPⁿ za rozmaitość.
- W dowodzie niezależności gładkości w punkcie od map ograniczono
  przeciwobraz do otoczenia, na którym wykazano ciągłość. Lokalna
  ciągłość nie uprawnia do uznania pełnego przeciwobrazu za otwarty.
  Przy złożeniu map doprecyzowano kolejność zmniejszania dziedzin.
- Obliczenia macierzy Jacobiego przejścia na RP² zachowano.
  Poprawny rachunek współrzędnych wektora stycznego przeniesiono
  za definicję przestrzeni stycznej i ogólną regułę zmiany współrzędnych.
  Dodano odsyłacze w obu kierunkach i przypomnienie map.
- Identyfikację RPⁿ z ilorazem sfery uzupełniono o zgodność topologii:
  ciągła normalizacja reprezentantów pozwala wykazać ilorazowość
  rzutowania ze sfery, bez zakładania z góry aksjomatu Hausdorffa.
- W RP¹→S¹, [z]↦z², uzasadniono ciągłość mapy indukowanej,
  zwartość dziedziny i zgodność współrzędnych kątowych z atlasem
  afinicznym (pochodne tangensa i cotangensa nie znikają).
- W modelu RP² jako dysku poprawiono zdanie o parach antypodalnych:
  dokładnie jeden punkt w otwartej półsferze mają pary spoza równika.
  Uzasadniono homeomorfizm ilorazu dysku, odwołując się do późniejszego,
  niezależnego dowodu własności Hausdorffa.
- Dla metryk na przestrzeniach rzutowych rozpisano nierówność trójkąta
  z dwiema fazami/znakami i symetrię. Uzupełniono brakujące przejście
  od ciągłości rzutowania ze sfery do ciągłości identyczności między
  pierwotnym ilorazem a przestrzenią metryczną: używa ono normalizacji
  i definicji topologii ilorazowej. Dopiero wtedy stosuje się argument
  zwartej dziedziny i przeciwdziedziny Hausdorffa.
- Poprawiono literówki w przykładzie x↦x³ i usunięto przypadkowy
  znacznik Markdown (trzy grawisy) ze źródła LaTeX.

### Ilustracje i weryfikacja

- Obejrzano wszystkie 42 strony rozdziału (4–45 PDF), a wszystkie
  15 ilustracji także w większej rozdzielczości. Na schemacie RP²
  usunięto pomocnicze średnice, które mogły sugerować sklejanie wnętrza
  dysku, i dodano wyraźny napis, że wnętrze nie podlega utożsamieniom.
  Strzałki w obu modelach doprowadzono bliżej wskazywanych par punktów.
- Symbolicznie sprawdzono wzory CP¹→S² w obu mapach, macierz Jacobiego
  przejścia RP² i jej wyznacznik; potwierdzono również zgodność rysunku
  rzutu stereograficznego ze wzorem i współliniowość zaznaczonych punktów.
- Kontrola zakresu względem `7222128` potwierdziła niezmienność źródła
  poza rozdziałem 1, unikalność etykiet, poprawność odsyłaczy,
  sparowanie środowisk i zachowanie wszystkich 15 ilustracji.
- Końcowy skład lokalnym MiKTeX ma 325 stron. Brak błędów,
  brakujących odsyłaczy, żądań ponownej kompilacji oraz ostrzeżeń
  `Overfull` i `Underfull`; pozostają dwa ostrzeżenia o automatycznej
  zmianie położenia ilustracji z `h` na `ht`. Wbudowany kompilator
  nie potwierdził statusu, więc wynik zweryfikowano lokalnie.
  Poprawioną ilustrację obejrzano ponownie i zaktualizowano PDF.
- Pobranie zmian przed zapisem nie wykazało nowych commitów.
  `git diff --check` przechodzi.

Ponowny przegląd rozdziału 1 zakończony. Pozostaje końcowy audyt
spójności całości oraz lista propozycji rozbudowy do wyboru przez autora.

## Audyt końcowy i propozycje rozbudowy (2026-10-05)

- Pobrano zmiany PortableGit z dysku E; gałąź była aktualna.
- Porównano aktualną treść każdego z 18 rozdziałów z commitem
  kończącym jego przegląd. Wszystkie porównania są zgodne, w tym
  ponownie sprawdzony rozdział 1 po uzupełnieniach autora.
- Zestawiono 140 numerowanych sekcji, 87 numerowanych rysunków
  i końcowy zakres stron każdego rozdziału. Dodatkowe nienumerowane
  diagramy pozostają opisane we wcześniejszych kontrolach wizualnych.
- Sprawdzono znaczenie wszystkich międzyrozdziałowych odsyłaczy naprzód,
  szczególnie zależność dowodu homologii Morse'a od przestawiania
  wartości krytycznych w rozdziale 18. Nie wykryto nowej sprzeczności
  ani zależności kołowej w tych odwołaniach.
- Potwierdzono unikalność 964 etykiet, cele 860 odsyłaczy w źródle,
  sparowanie środowisk oraz cele 1028 wewnętrznych linków PDF.
  Plik PDF w repozytorium jest identyczny z ostatnim zweryfikowanym
  składem (325 stron); treści źródła i PDF w tej iteracji nie zmieniano.
- Dodano `AUDYT_KONCOWY.md` (obecnie scalony z tym dziennikiem): tabelę pokrycia,
  weryfikację zależności, wyniki kontroli i jawne granice zakresu.
- Dodano `PROPOZYCJE_UZUPELNIEN.md` (aktualny stan w [planie](PLAN_DZIALANIA.md)):
  12 ponumerowanych propozycji, informację, co już jest w książce,
  zakres nowych prac i sugerowaną kolejność. Uwzględniono życzenia
  z `do_zrobienia.md`, zachowując sam plik bez zmian.
- Rozdzielono dalszą redakcję i podstawy od pełnych h-/s-kobordyzmów,
  chirurgii, sfer egzotycznych i metod czterowymiarowych. Dla Poincarégo
  wskazano różnicę między kategorią topologiczną i gładką; status
  gładkiego problemu w wymiarze 4 sprawdzono w materiale Clay.
  Proponowanego nowego materiału nie dopisywano do skryptu.

Przegląd istniejących 18 rozdziałów i wymagane przygotowanie listy
dalszych uzupełnień są zakończone. Kolejne rozszerzenia zależą od wyboru autora.

## Kontynuacja po rozbudowie autora — podział źródeł (2026-10-05)

Na nową prośbę użytkownika pobrano zmiany do `19fa283` i porównano je
z `66b220f`. Autor rozbudował książkę do 27 rozdziałów i dodatku;
wersja ma 384 strony. Nowy zakres nie jest objęty historycznym audytem
18 rozdziałów. Dalsza kontrola jest rozpisana w `PLAN_DZIALANIA.md`.

- Potwierdzono obecność sekcji o rozmaitościach z brzegiem w rozdziale 1
  oraz konstrukcji grup wolnych i iloczynu wolnego w rozdziale 5.
  Nie dodawano powtórnych definicji. Zaktualizowano status wszystkich
  wcześniejszych propozycji wobec już dopisanej treści.
- Zgodnie z obecną prośbą użytkownika wydzielono 27 plików rozdziałów,
  preambułę, wstęp, dodatek i indeks — łącznie 31 plików wejściowych
  w `tex/`. Główny plik nadal składa tę samą książkę.
- Użyto `\input`, zachowując kolejność, wszystkie etykiety i istniejące
  polecenia przełamania strony. Pełny tekst po rozwinięciu importów
  jest identyczny z monolitycznym źródłem `19fa283` (po normalizacji
  zakończeń linii). Nie zmieniono w tym kroku treści matematycznej.
- Zmieniono nieaktualną zasadę jednego pliku w `AGENTS.md`; nadrzędna
  jest najnowsza prośba użytkownika o podział. Dodano w README opis
  struktury, kompilacji, zachowania etykiet i współpracy przez Git.
- Uruchomiono pełny `latexmk` z lokalnym MiKTeX przed podziałem i po nim.
  Zadziałał Perl już obecny w PortableGit — bez instalowania programów.
  `makeindex` przyjął 152 wpisy, bez odrzuceń i ostrzeżeń indeksu.
- Porównano wszystkie 384 strony: identyczny tekst, rozmiary,
  linki i obrazy renderowane w 72 dpi. Identyczne są spis treści,
  zakładki, dane indeksu i sam indeks. Wszystkie 31 importów istnieje,
  jest użyte dokładnie raz; nie pozostały osierocone pliki TeX.
- Potwierdzono unikalność 1159 etykiet i cele 1051 odsyłaczy w źródle;
  porównano 1553 linki PDF. Końcowy log nie zgłasza błędów,
  brakujących odsyłaczy ani potrzeby ponownego przebiegu. Zachowuje
  dwa wcześniejsze ostrzeżenia o zmianie `h` na `ht` i jedno `Underfull`;
  nie ma `Overfull`. Te komunikaty nie wynikają z podziału.
- Osobno porównano PDF pobrany od autora ze świeżym składem.
  Strony treści 1–382 są identyczne, lecz na stronach 383–384 stary
  indeks odsyłał o trzy strony za wcześnie (np. rozmaitość z brzegiem
  do s. 11 zamiast 14, grupa wolna do s. 98 zamiast 101).
  Pełny `latexmk` ponownie uruchomił `makeindex` po ustaleniu paginacji.
  Obejrzano obie poprawione strony indeksu i zaktualizowano PDF
  w repozytorium. To naprawa nieaktualnego indeksu, niezależna od podziału.
- Dokument `AUDYT_KONCOWY.md` oznaczono jako historyczny, aby nie
  przypisywać starego przeglądu nowo dopisanym rozdziałom.

Nowe rozdziały będą kontrolowane kolejno. Materiał o Freedmanie
i egzotycznych R⁴ pozostaje poza tym skryptem; istniejącego rozdziału
o sferach Milnora nie usuwano ani nie przenoszono bez potrzeby.

## Rozdział 1 — kontrola nowej sekcji o brzegu i uzupełnień autora

Zakres: zmiany autora od `66b220f`, po podziale źródeł w `9148128`.
Przeczytano nową sekcję o brzegu, dopisany rachunek struktury liniowej
na klasach krzywych oraz pozostałe różnice rozdziału 1.

- Zachowano poprawne definicje, dowód niezależności brzegu od map,
  przykłady dysku i okręgu oraz rozróżnienie naroży.
- Utrwalono domyślną konwencję „bez brzegu, o ile nie zaznaczono inaczej”.
  Wcześniejsze zdanie określało ją tylko do momentu wprowadzenia definicji
  brzegu, co mogło sugerować stosowanie dalszych twierdzeń o zanurzeniach
  i wartościach regularnych do dowolnych rozmaitości z brzegiem.
- W stwierdzeniu o wymiarze brzegu zapisano n≥1, aby teza n−1 nie
  obejmowała przyjętej osobno konwencji dla rozmaitości zerowymiarowych.
- Po konstrukcji przestrzeni stycznej dopisano pełne uzasadnienie modelu
  przy brzegu: kiełki, niezależność pochodnych od przedłużenia,
  reprezentacja każdej derywacji przez n współczynników i odwracalność
  przejść w punkcie brzegu. Wcześniejszą wzmiankę połączono z tym dowodem.
- Uzasadniono identyfikację T_p(∂M) z podprzestrzenią vⁿ=0 oraz fakt,
  że krzywe dwustronne reprezentują właśnie tę podprzestrzeń, nie całe
  T_pM. Przykład minimum ostatniej współrzędnej wyjaśnia brak kierunku
  poprzecznego w modelu krzywych. Podano też związek z derywacjami
  funkcji globalnych przez funkcję odcinającą.
- Dopisane przez autora wzory dodawania klas krzywych i mnożenia
  przez skalar są poprawne; zachowano je wraz z reparametryzacją γ(at).

- Kontrola struktury potwierdziła, że spośród źródeł TeX zmieniono
  wyłącznie rozdział 1. Wszystkie 1160 etykiet jest unikalnych,
  wszystkie 1053 odsyłacze mają cel, środowiska są sparowane,
  zachowano 15 rysunków rozdziału.
- Pełny `latexmk` przebudował dokument i indeks do 385 stron.
  Brak błędów, niezdefiniowanych odsyłaczy, `Overfull` i żądania
  kolejnego przebiegu. Pozostają wcześniejsze dwa `h`→`ht` i jedno
  `Underfull` w rozdziale 23, niezwiązane z tą zmianą.
- Obejrzano sekcję o brzegu (strony 13–15), zmieniony przez autora
  kolorystycznie rzut stereograficzny (21), nowy dowód i jego sąsiedztwo
  (34–36) oraz zaktualizowany indeks (384–385). Układ i odsyłacze są poprawne.
  Zaktualizowano PDF w repozytorium.

Kontrola nowych fragmentów rozdziału 1 zakończona. Następna iteracja:
nowy rozdział 5 z podstawami algebry, w tym grupą wolną i iloczynem wolnym.

## Scalenie dokumentacji projektu (2026-10-05)

Na prośbę użytkownika pozostawiono cztery pliki Markdown w katalogu głównym:
README (obsługa projektu), AGENTS (zasady), PRZEGLAD (historia i dowody kontroli)
oraz PLAN_DZIALANIA (jedyna aktualna kolejka i lista pomysłów).

- Z `AUDYT_KONCOWY.md` przeniesiono poniżej unikalną tabelę pokrycia,
  kontrolę zależności i dane techniczne starej wersji. Nie przenoszono
  powtórzonego opisu ukończenia prac jako statusu obecnej książki.
- Z `PROPOZYCJE_UZUPELNIEN.md` zachowano w planie numerację 1–12,
  stan wdrożenia, niewykonane elementy, granice zakresu i źródła.
- Z `do_zrobienia.md` włączono życzenia dotyczące redakcji rozdziału 1,
  zakończeń rozdziałów, brzegu, grup, h-/s-kobordyzmów, chirurgii,
  Poincarégo i struktur egzotycznych. Pokrywały się z propozycjami;
  nie utworzono kolejnych kopii tych samych zadań.
- Usunięto te trzy scalone pliki; ich pełne historyczne brzmienie zachowuje Git
  (m.in. `aa6c59a`). Poprawiono linki w README i dzienniku.
- Zachowano rozróżnienie torsji Whiteheada i triku Whitneya oraz Smale'a
  i Milnora; literówki w dawnej liście autora nie są nową terminologią.

### Historyczna rozbudowa autora — nie jest bieżącym audytem

Autor w `4233e60` i `b2635d0`, zamkniętych planem `19fa283`, dodał
brzeg, grupy i tensor modułów, nawigację oraz indeks, h-/s-kobordyzmy,
chirurgię (geometrię, przeszkodę Walla, ciąg dokładny), Poincarégo,
sfery Milnora, Cherna–Weila i katalog wyników zewnętrznych.
Algebrę abstrakcyjną wydzielił jako rozdział 5, przesuwając dawny rozdział 5
i kolejne o jeden. Jego plan deklarował zakończony przegląd własnych dodatków,
kontrolę torusów i schematów Walla, chirurgii, Poincarégo oraz Milnora,
skład 384 stron i 152 wpisy indeksu. Wspominał też przejściowe składy
381 stron i brak Perla w MiKTeX. To historia tamtej sesji, nie aktualna
instrukcja kompilacji; działający Perl z PortableGit opisuje README.

W planie autora głębokie wyniki (klasyfikacja powierzchni, geometryczne
lematy Walla, h-kobordyzm, twierdzenie Hirzebrucha) pozostawiono jawnie
zewnętrzne tam, gdzie nie ma pełnego dowodu. Zadań i teorii czterowymiarowej
nie włączono do zakresu. Trzy dodatkowe pomysły geometryczne zachowano
w aktualnym planie. Nasz przegląd nowych dowodów ma własne statusy.

### Archiwalne dane audytu 18 rozdziałów

Poniższe wyniki odnoszą się **wyłącznie do `a36c920`, PDF 325 stron**,
sprawdzonego 5 października 2026 przed rozbudową do 27 rozdziałów.
Numery rozdziałów i stron są historyczne.

### Pokrycie rozdziałów

Poniższa tabela została sprawdzona na aktualnym źródle, spisie treści PDF
i historii Git. Tekst każdego rozdziału jest identyczny z jego treścią
w podanym commicie kończącym odpowiedni przegląd. Późniejsze iteracje
nie nadpisały tych poprawek. Kolumna rysunków liczy numerowane środowiska
`figure`; dodatkowe nienumerowane diagramy również były objęte przeglądem
(np. diagram własności uniwersalnej w rozdziale 3).

| Rozdział | Sekcje | Rysunki | Strony PDF | Commit przeglądu |
|---|---:|---:|---|---|
| 1. Rozmaitości różniczkowe | 11 | 15 | 4–45 | `a36c920` |
| 2. Pola wektorowe, przepływy i pochodna Liego | 7 | 4 | 46–61 | `9bfa3af` |
| 3. Algebra tensorowa i zewnętrzna | 9 | 1 | 62–80 | `02ea77d` |
| 4. Grassmanniany, algebra Clifforda i spinory | 7 | 5 | 81–97 | `831cbcc` |
| 5. Algebra homologiczna: moduły, kompleksy i (ko)homologie | 10 | 1 | 98–114 | `4f017f4` |
| 6. Homotopia, nakrycia i komórkowe modele przestrzeni | 5 | 6 | 115–128 | `21a3ecb` |
| 7. Homologia przestrzeni | 8 | 3 | 129–142 | `3e871f0` |
| 8. Wyższe grupy homotopii i związek z homologią | 7 | 4 | 143–157 | `f7df0ae` |
| 9. Formy różniczkowe, orientacja i kohomologia de Rhama | 10 | 5 | 158–178 | `c4efcb0` |
| 10. Tensor metryczny, długość i miara | 8 | 2 | 179–196 | `3735830` |
| 11. Koneksje i transport równoległy | 6 | 2 | 197–207 | `4c29411` |
| 12. Geodezyjne, odwzorowanie wykładnicze i zupełność | 6 | 9 | 208–222 | `940a346` |
| 13. Krzywizna: od transportu równoległego do tensorów | 9 | 8 | 223–255 | `f03c9d3` |
| 14. Twierdzenie Sarda i transwersalność | 6 | 4 | 256–266 | `bde2d8d` |
| 15. Zanurzenia i otoczenia podrozmaitości | 7 | 4 | 267–281 | `f3d1458` |
| 16. Przecięcia, dualność i klasy charakterystyczne | 10 | 4 | 282–298 | `f3222f9` |
| 17. Teoria Morse'a: punkty krytyczne, uchwyty i przepływ | 7 | 5 | 299–313 | `af689aa` |
| 18. Kobordyzmy i rachunek uchwytów | 7 | 5 | 314–325 | `7222128` |

Razem: **18 rozdziałów, 140 numerowanych sekcji, 87 numerowanych rysunków,
325 stron PDF**. Strony w tabeli odnoszą się do końcowego PDF;
wcześniejsze numery stron w dzienniku opisują stan z dnia danej iteracji.

### Spójność między rozdziałami

- Odsyłacz 2→16 dotyczy przykładu nietrywialności TS² i jest jawnie
  opisany jako użycie klasycznego twierdzenia, nie podstawa konstrukcji
  pól wektorowych w rozdziale 2.
- Odsyłacz 3→5 porównuje już wykonaną faktoryzację przez iloraz
  z ogólnym twierdzeniem o izomorfizmie; konstrukcja tensorów ma własny dowód.
- Własności izometrii 10→11,13 są wyraźnie oddzielone jako zapowiedź
  koneksji i krzywizny. Pozostała część rozdziału 10 nie zależy od tej zapowiedzi.
- Odsyłacze 11→12,13 porównują przykłady z późniejszym wzorem geodezyjnej
  i objaśniają, dlaczego zerowanie symboli Christoffela w punkcie
  nie oznacza płaskości. Wzory koneksji wyprowadzono niezależnie.
- Odsyłacz 12→13 zapowiada drugą wariację i pola Jacobiego po dowodzie
  lokalnej minimalności; nie jest używany w tym dowodzie.
- Zależność 17→18 jest istotna dla identyfikacji homologii Morse'a:
  potrzebne przestawianie wartości krytycznych zachowuje wybrane pole.
  Dowód w 18 używa przepływu i braku połączenia, nie homologii Morse'a.
  Konstrukcja rozkładu i przestawiania uchwytów nie używa wyniku,
  który ma dzięki niej zostać udowodniony.
- Uzupełnienia rozdziału 1 zachowują przyjęte znaczenia mapy,
  struktury różniczkowej i wektora stycznego. Przykład na RP² znajduje
  się obecnie po zdefiniowaniu przestrzeni stycznej. Odwołania w dowodach
  modeli rzutowych prowadzą do niezależnego argumentu metrycznego.

Weryfikacja ta dotyczy sensu odwołań naprzód, a nie tylko istnienia
ich numerów. Szczegółowe konwencje znaków i rachunki są udokumentowane
przy rozdziałach 3–4, 9, 13 i 16–18 w dzienniku.

### Kontrola techniczna końcowego pliku

- 964 etykiety: brak duplikatów. Wszystkie 860 wystąpień odsyłaczy
  `ref`, `eqref`, `pageref` i `autoref` mają istniejący cel.
- Środowiska LaTeX są prawidłowo sparowane w każdym rozdziale.
  W źródle nie ma znaczników TODO/FIXME/TBD ani przypadkowych ogrodzeń Markdown.
- W tekście końcowego PDF nie ma nierozwiązanych odsyłaczy `??`.
  Wszystkie 1028 wewnętrznych linków PDF prowadzi do istniejących stron.
  Sprawdzono także obecność podpisów wszystkich numerowanych rysunków.
- PDF w repozytorium jest identyczny z wynikiem ostatniej kompilacji
  w `build/`. Jej log potwierdza 325 stron, bez błędów, brakujących
  odsyłaczy, żądań ponownego przebiegu oraz `Overfull` i `Underfull`.
  Pozostają dwa ostrzeżenia o automatycznej zmianie położenia rysunku
  z `h` na `ht`. Wbudowany kompilator nie podał potwierdzonego statusu;
  zweryfikowany skład wykonano lokalnym MiKTeX.
- SHA-256 końcowego PDF:
  `12f296ea00243dd915b5ae388288038103f7e60b06c06dbdc1d56f707bbec378`.
- Sprawdzono `git diff --check`. Do obsługi repozytorium używano
  `E:\Programs\Windows\PortableGit\cmd\git.exe`.

Kontrole strukturalne nie zastępują czytania dowodów. Dowody i ilustracje
sprawdzano w poszczególnych iteracjach; końcowa kontrola porównuje ich
zapisane wyniki z aktualnym źródłem i weryfikuje powiązania między nimi.


W tej dawnej wersji pełne h-/s-kobordyzmy, torsja Whiteheada, dalsza
chirurgia i struktury egzotyczne były dopiero propozycjami. Skrypt jawnie
korzystał z twierdzeń Brouwera, o funkcji odwrotnej, triangulacji i pełnego
Cherna–Gaussa–Bonneta. Późniejsza rozbudowa zmienia zakres tekstu, dlatego
nie wolno przenosić tych dawnych deklaracji na obecny stan bez kontroli.

## Rozdział 5 — podstawy algebry po rozbudowie autora (2026-10-05–06)

Zakres: cały nowy rozdział 5 w wersji `aa6c59a`, cztery sekcje i rysunek
grafu słów. Moduły pochodzą częściowo z uprzednio sprawdzonego rozdziału 5;
przeniesienie nie zastępuje kontroli nowych grup, pierścieni i tensorów.

- Uzupełniono brakującą definicję podgrupy i warstwy oraz kryterium równości
  warstw. Sprawdzono aksjomaty ilorazu i krótkie konsekwencje definicji
  homomorfizmu, aby pierwsze użycia nie zakładały niepodanych pojęć.
- W grupie wolnej dopisano, dlaczego stos reprezentuje tę samą klasę słowa;
  dotychczas argument uzasadniał jednoznaczność, pomijając ten krok istnienia.
- W iloczynie wolnym jawnie oznaczono rozłączną sumę alfabetów i odwracalne
  relacje, także dla dwóch kopii tej samej grupy. Odrębność czynników jest
  istotna: identycznie nazwane elementy nie stają się automatycznie równe.
- Naprawiono lukę logiczną: odwracalność dopisywania x nie dowodzi sama
  zgodności z relacją xy. Nowy dowód sprawdza T_y(T_x(u))=T_xy(u), także
  przypadek skasowania końca stosu. Stąd wynik jest stały na klasie,
  postać normalna jednoznaczna, a czynniki osadzają się w iloczynie wolnym.
  Rozpisano też własność uniwersalną używaną w twierdzeniu van Kampena.
- Dodano przykład dwóch grup rzędu dwa: ich iloczyn wolny jest nieskończony
  (różne słowa (ab)^k), podczas gdy iloczyn prosty ma cztery elementy.
- Zastąpiono błędne „zbiliniowa/zbiliniowość” przez „dwuliniowa/dwuliniowość”.
  Doprecyzowano relację modułu spinorów nad nieprzemienną algebrą Clifforda
  do przyjętej w tej części konwencji pierścienia przemiennego.
- Rozpisano izomorfizm tensoru sumy prostej z sumą tensorów i jego odwrotność,
  w tym skończoność nośnika. Uzupełniono rachunek 3R⊕4R=R dla R=Z/6,
  wyjaśniający przykład modułu projektywnego, który nie jest wolny.
- Dla pierścienia nieprzemiennego podano poprawny obiekt wyjściowy:
  wolną grupę abelową na parach oraz relacje addytywności i zbalansowania.
  Sam wybór prawego i lewego modułu nie nadaje tensorowi struktury modułu
  nad tym pierścieniem; zaznaczono tę granicę i odzyskanie wcześniejszej
  konstrukcji w przypadku przemiennym.
- Pozostałe dowody (ilorazy pierścieni i modułów, torsja, własność uniwersalna
  tensoru, (R/I)⊗M, rozszerzenie skalarów i projektywność) sprawdzono,
  zachowując poprawne rachunki. Rysunek przedstawia poprawny fragment grafu
  Cayleya, a nie pełną kulę; podpis już to zaznacza, więc nie zmieniano geometrii.

Dodano dalszą lekturę z dokładnym miejscem: Hatcher, *Algebraic Topology*,
sekcja 1.2, s. 41–42 ([źródło](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf)),
oraz *The Stacks Project*, sekcja 10.12
([tensor nad pierścieniem przemiennym](https://stacks.math.columbia.edu/tag/00CV)).
Pierwsze źródło potwierdza używaną postać normalną i własność uniwersalną;
drugie konstrukcję tensoru. Dowody w skrypcie pozostają rozpisane samodzielnie.

Zinwentaryzowano ponadto różnice `66b220f`→`19fa283` we wcześniej
sprawdzonych rozdziałach. Występują w rozdziałach 2–4 oraz 6–19;
przeniesienie modułów dominuje w rozdziale 6, a w części pozostałych
zmiany ograniczają się do wpisów indeksu. Sama inwentaryzacja nie została
oznaczona jako audyt matematyczny tych rozdziałów.

Kontrole zakończone 6 października 2026:

- Wśród źródeł TeX zmieniono wyłącznie rozdział 5; zachowano cztery
  numerowane sekcje i jeden rysunek, dodano nienumerowaną dalszą lekturę.
  Wszystkie 31 importów istnieje i występuje dokładnie raz; nie ma
  osieroconych źródeł. Środowiska wszystkich części są sparowane.
- Wszystkie 1161 etykiet jest unikalnych; 1053 odsyłacze mają istniejące
  cele. Sprawdzono także wszystkie lokalne linki czterech plików Markdown.
- Pełny `latexmk` wraz z indeksem dał 387 stron i potwierdził aktualność
  wyników. `makeindex` przyjął 152 wpisy bez odrzuceń i ostrzeżeń.
  Nie ma błędów, niezdefiniowanych odsyłaczy, `Overfull` ani żądania
  kolejnego przebiegu. Pozostają wcześniejsze dwa komunikaty `h`→`ht`
  i jedno `Underfull` w rozdziale 23.
- W PDF nie ma `??`; wszystkie 1428 linków wewnętrznych mają cel
  na istniejącej stronie. Kontrola uwzględnia zarówno zwykłe, jak
  i nazwane cele PDF, używane przez hyperref.
- Obejrzano strony 102–110, w tym graf słów, dowód postaci normalnej,
  tensor i dalszą lekturę, oraz obie strony indeksu 386–387.
  Podpisy, wzory i łamanie tekstu są czytelne.
- Zaktualizowano PDF w katalogu głównym; porównano go bajtowo
  z wynikiem kompilacji. `git diff --check` przechodzi.

Kolejna iteracja dotyczy różnic rozdziału 2. Nowe rozdziały 20–27
i dodatek nadal oczekują na nasz audyt; pełny cel pozostaje otwarty.

## Rozdział 2 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w rozdziale 2
oraz ich powiązanie z nowym modelem brzegu w rozdziale 1.
Przed pracą pobrano aktualizacje; gałąź była aktualna i czysta (`23483ad`).

- Autor zastąpił powtórzoną konwencję półprzestrzeni odsyłaczem, dodał
  dwa wpisy indeksu i rozwinął bibliografię. Pozostałe dowody oraz cztery
  ilustracje zachowują treść wcześniejszego audytu.
- Sprawdzono zgodność nowego odsyłacza z uwagą o dwustronnym przepływie,
  dowodem rozszerzania izotopii przy końcach czasu i konstrukcją kołnierza.
  Styczność do brzegu gwarantuje lokalny przepływ zachowujący rozmaitość;
  skierowanie do wnętrza daje czas jednostronny. Założenie bez brzegu
  w głównych twierdzeniach pozostaje jawne.
- Odsyłacz do przestrzeni stycznej prowadzi teraz bezpośrednio do
  `prop:styczna-brzeg-1`, gdzie znajduje się pełny dowód, zamiast
  do wstępnej wzmianki w sekcji o definicji brzegu.
- Dodano przykład X=∂r na [0,∞): pole jest gładkie, lecz krzywa z zera
  musiałaby być r(t)=t i dla t<0 opuszcza półprostą. Wyjaśnia to różnicę
  między pełnym T₀M a T₀∂M i zapobiega myleniu lokalnej dwustronności
  z globalną zupełnością. Nie zmieniono poprawnego argumentu ODE.
- Zweryfikowano nowe źródła bibliograficzne: stronę wydawcy i
  [spis treści Lee udostępniony przez autora](https://sites.math.washington.edu/~lee/Books/ISM/front-matter.pdf)
  oraz [tekst Milnora](https://people.dm.unipi.it/benedett/MILNOR-TDVPOINT.pdf).
  Rozdziały 8–9 Lee wskazano jako źródło pól, przepływów, zachowania przy
  brzegu i pól zależnych od czasu, a 12 jako rozszerzenie do tensorów.
  Przy Milnorze dopisano strony 20–24 (izotopia i przemieszczanie punktów)
  oraz 32–41 (pola i liczba Eulera). Nie przypisano tym ogólnym odsyłaczom
  dokładnej wersji naszego twierdzenia o rozszerzaniu izotopii.

Kontrola: zmieniono wyłącznie źródło rozdziału 2; jego cztery środowiska
rysunków są identyczne z wersją przed tą iteracją. Wszystkie 31 importów,
1161 unikalnych etykiet i 1054 odsyłacze są poprawne; środowiska sparowane,
a lokalne linki dokumentacji istnieją. Pełny `latexmk` zakończył skład
387 stron bez błędów, brakujących referencji ani żądania ponownego przebiegu.
Pozostały dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23;
nie ma nowych ostrzeżeń ani `Overfull`.

Obejrzano strony 50, 55, 58–59, 61, 63 i 65, obejmujące wszystkie rysunki,
nowy przykład, odsyłacz i bibliografię, oraz indeks na stronach 386–387.
Układ jest czytelny. Wszystkie 1429 linków wewnętrznych PDF mają poprawne
cele; nie ma `??`. Zaktualizowano główny PDF, sprawdzono zgodność bajtową
ze składem i `git diff --check`. Następna iteracja: różnice rozdziału 3.

## Rozdział 3 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice `66b220f`→`19fa283` w algebrze tensorowej.
Pobranie zmian przed przeglądem potwierdziło aktualną, czystą gałąź `2035433`.

- Porównano całe źródło z wcześniejszą sprawdzoną wersją. Po pominięciu
  nowych poleceń indeksu, bibliografii i zmiany nazwy rozdziału w jednym
  odsyłaczu tekst jest identyczny. Nie ma pominiętych nowych dowodów.
- Odsyłacz do twierdzenia o izomorfizmie prawidłowo wskazuje obecny
  rozdział 5, twierdzenie 5.3.5. Przeczytano konstrukcję tensoru oraz uwagę
  o faktoryzacji: dowód używa własnego argumentu R⊆ker L, więc późniejsze
  twierdzenie jest porównaniem, a nie ukrytą przesłanką. Nadal jawnie
  rozróżnione są F/R i F/ker L. Nie znaleziono luki wymagającej dopisania.
- Sprawdzono 11 wpisów indeksu: tensor, własność uniwersalną, kontrakcję,
  algebry tensorową, symetryczną i zewnętrzną, symetryzator/antysymetryzator,
  wyznacznik, pole tensorowe, cofnięcie i pochodną Liego. Umieszczono je
  przy odpowiednich definicjach, a numery stron wynikają ze świeżego składu.
- Zweryfikowano [notatki Conrada](https://math.stanford.edu/~conrad/diffgeomPage/handouts/tensor.pdf):
  tytuł, 13 stron i zakres odpowiadają bibliografii. Zachowano odsyłacz
  do Lee, rozdziały 12 i 14, potwierdzone w
  [spisie treści autora](https://sites.math.washington.edu/~lee/Books/ISM/front-matter.pdf).
- Kod rysunku pola równoległoboku i nienumerowanego diagramu własności
  uniwersalnej jest identyczny z poprzednim audytem. Obejrzano je ponownie
  na stronach 66 i 78, a także poprawiony przez autora odsyłacz na 67
  i bibliografię na 84. Oznaczenia, strzałki i rachunek pola 3·2−1·1=5
  są zgodne z tekstem; ilustracje pozostawiono.
- Kontrola struktury potwierdziła 31 importów, 1161 unikalnych etykiet,
  1054 poprawne odsyłacze i sparowanie środowisk. `latexmk` potwierdził
  aktualność pełnego składu z indeksem (387 stron). Główny PDF jest
  bajtowo identyczny ze sprawdzonym wynikiem kompilacji; nie wymagał
  zmiany. Lokalne linki czterech plików Markdown są poprawne.

Nie zmieniano źródeł TeX ani PDF; ta iteracja zapisuje pozytywny wynik
audytu w dzienniku i planie. Następny jest rozdział 4.

## Rozdział 4 — kontrola dodatków po rozbudowie (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w rozdziale
o grassmannianach, algebrze Clifforda i spinorach. Gałąź po pobraniu
aktualizacji pozostała czysta i aktualna (`01cf513`).

- Pełne porównanie źródeł wykazało tylko siedem poleceń indeksu oraz
  zmianę wypełnienia i obrysu dwóch sfer. Po usunięciu tych dokładnie
  wskazanych różnic tekst jest identyczny z wcześniej sprawdzoną wersją.
  Nie ma nowych twierdzeń ani zmienionych dowodów do naprawy.
- Sprawdzono rysunek 4.2 na stronie 88: wybór orientacji płaszczyzny
  odpowiada wyborowi jednostkowej normalnej, a punkty n i −n pozostają
  antypodyczne. Jasnoniebieskie cieniowanie nie zmienia geometrii ani
  nie zasłania punktów, równika czy etykiet.
- Sprawdzono rysunek 4.5 na stronie 98 z opisującym go rachunkiem:
  faza spinora znika po przejściu do prostej zespolonej, a odwzorowanie
  b prowadzi do sfery. Zaznaczony punkt jest czytelny na powierzchni,
  podpis i kolejność strzałek odpowiadają konstrukcji. Rysunek zachowano.
- Obejrzano również pozostałe trzy ilustracje na stronach 86, 92 i 95.
  Ich źródła nie uległy zmianie; diagram wykresu, rozkład iloczynu
  Clifforda i dwukrotne nakrycie Spin(2)→SO(2) zachowują poprawne oznaczenia.
- Siedem wpisów indeksu prowadzi do stron 85, 87, 88, 90, 93, 95 i 98.
  Dwa wystąpienia hasła „Grupa Spin” wskazują początek rozdziału oraz
  właściwą definicję; indeks scala je w jedno hasło z dwiema stronami.
- Potwierdzono strukturę importów, unikalność 1161 etykiet i cele 1054
  odsyłaczy. `latexmk` potwierdził aktualność składu z indeksem, 387 stron.
  Główny PDF jest bajtowo identyczny ze sprawdzonym wynikiem kompilacji.
  Nie zmieniono źródeł matematycznych ani PDF; zapisano wynik w planie
  i dzienniku. `git diff --check` przechodzi.

Następna iteracja: rozdział 6, w szczególności kompletność po przeniesieniu
podstaw modułów i tensoru do osobnego rozdziału 5.

## Rozdział 6 — kompletność po wydzieleniu algebry (2026-10-06)

Zakres: różnice autora `66b220f`→`19fa283` w dawnym rozdziale 5,
obecnie 6. Przed pracą pobrano zmiany; gałąź `d326e06` była aktualna i czysta.

- Sprawdzono przeniesienie sekcji o modułach: wszystkie sześć jej etykiet
  (sekcja, definicje modułu, torsji i homomorfizmów, przykład podstawowy
  oraz twierdzenie o izomorfizmie) zachowano dokładnie raz w rozdziale 5.
  Nie utracono definicji potrzebnych w dowodach homologicznych.
- Porównano całe pozostałe źródło: dziewięć sekcji zachowuje uprzednio
  sprawdzone dowody i przykłady. Różnice poza wstępem dotyczą wpisów
  indeksu i zastąpienia uwagi o tensorze odsyłaczem do rozdziału 5.
- Przy przeniesieniu usunięto z rozdziału 6 jawną konwencję dotyczącą R.
  Przywrócono na początku założenie pierścienia przemiennego z jedynką
  1≠0 oraz R-liniowość odwzorowań, z odsyłaczem do modułów. To potrzebne
  m.in. dla traktowania Hom_R(M,N) jako R-modułu w kompleksie dualnym;
  uwaga o pierścieniach nieprzemiennych na końcu poprzedniego rozdziału
  nie powinna niejawnie zmieniać założeń obecnego.
- Sprawdzono, że usunięty lokalny opis tensoru ma pełny odpowiednik
  w rozdziale 5: konstrukcję, własność uniwersalną, rozszerzenie skalarów,
  tensorowanie odwzorowań oraz zachowanie sum prostych i izomorfizmów.
  Ostatnie dwie własności, uzupełnione podczas audytu rozdziału 5,
  uzasadniają rozkłady w dowodzie zmiany współczynników na Q, R i C.
- Dopisano połączenie dwóch opisów zmiany współczynników:
  C_n⊗Z/m ≅ C_n/mC_n przez c⊗[a]↦ac+mC_n. Odsyłacz prowadzi
  do wcześniej udowodnionego wzoru na tensor ilorazu przez ideał.
  Sprawdzono komutowanie z różniczkami, więc jest to izomorfizm kompleksów.
  Wyjaśniono, że charakterystyka zero jest założeniem późniejszego
  prostszego wzoru na homologię, nie warunkiem istnienia tensoru.
- Przeczytano w powiązaniu dowód redukcji modulo m, przykład nowej klasy
  stopnia 1, konstrukcję kompleksu dualnego i argument zmiany współczynników
  w charakterystyce zero. Ich założenia oraz odsyłacze do przeniesionych
  podstaw są zgodne; nie zmieniano poprawnych rachunków.

Kontrola zakończona: zmieniono wyłącznie źródło rozdziału 6, zachowując
dziewięć sekcji i niezmieniony kod rysunku. Wszystkie 31 importów,
1161 unikalnych etykiet i 1057 odsyłaczy są poprawne; środowiska są
sparowane. Pełny `latexmk` potwierdził aktualny skład 387 stron z indeksem,
bez błędów, brakujących referencji ani żądania kolejnego przebiegu.
Pozostają te same dwa ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23;
nie ma `Overfull`.

Obejrzano strony 111, 114, 116, 122–123 i 125 (wstęp, diagram długiego
ciągu, kompleks dualny, redukcję i tensorowanie współczynników oraz
zakończenie) oraz indeks na stronach 386–387. Układ jest czytelny.
W PDF nie ma `??`, a wszystkie 1432 linki wewnętrzne mają istniejące cele.
Zaktualizowano główny PDF i potwierdzono zgodność bajtową ze składem.
`git diff --check` przechodzi. Następna iteracja: dodatki rozdziału 7.

## Rozdział 7 — połączenie van Kampena z podstawami grup (2026-10-06)

Zakres: wszystkie różnice autora `66b220f`→`19fa283` w dawnym
rozdziale 6, obecnie 7. Pobranie zmian potwierdziło czystą i aktualną
gałąź `83b0896`. Poza dziesięcioma wpisami indeksu jedyna zmiana autora
zastępuje opis iloczynu wolnego odsyłaczem do nowego rozdziału 5.

- Przeczytano cały dowód van Kampena, wybór dróg do punktu bazowego,
  argument siatki dla jądra oraz zastosowania do bukietu okręgów,
  sfer i dołączania komórek. Własność uniwersalna jest potrzebna już
  przy utworzeniu homomorfizmu z iloczynu wolnego; sama definicja
  nie była precyzyjnym wskazaniem przeprowadzonego dowodu tej własności.
- Dodano odsyłacz do `prop:free-product-normal-5` oraz jawne użycie
  własności uniwersalnej w pierwszym zdaniu dowodu. Zdefiniowano symbole
  i_U oraz i_V jako inkluzje przecięcia do składników pokrycia.
  Nie zakłada się iniektywności indukowanych homomorfizmów grup.
- Rozpisano końcowe przejście: relatory leżą w jądrze, więc ich domknięcie
  normalne N także; argument siatki daje inkluzję przeciwną. Odwzorowanie
  gN↦Φ(g) jest dobrze określone, surjektywne i ma trywialne jądro.
  Stąd wynika izomorfizm z tezy bez niejawnego użycia nieudowodnionego
  wcześniej grupowego twierdzenia o izomorfizmie.
- W przykładzie torusa dodano odsyłacz do rachunku prezentacji w rozdziale 5.
  Rozdzielono role obu miejsc: wcześniejszy przykład oblicza grupę z relacji,
  a obecne dołączenie komórki wyjaśnia topologiczne pochodzenie tej relacji.
- Dziesięć wpisów indeksu umieszczono przy właściwych pojęciach. Porównanie
  potwierdziło, że reszta treści autora, w tym kod sześciu rysunków,
  zachowuje wersję wcześniejszego audytu. Poprawki tej iteracji dotyczą
  wyłącznie rozdziału 7.

Kontrola zakończona: 31 importów, 1161 unikalnych etykiet i 1059 odsyłaczy
bez brakujących celów; środowiska i lokalne linki dokumentacji są poprawne.
Pełny `latexmk` złożył 387 stron i indeks (152 wpisy), bez błędów,
niezdefiniowanych referencji, `Overfull` ani żądania kolejnego przebiegu.
Pozostają dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
W PDF nie ma `??`; wszystkie 1434 linki wewnętrzne mają istniejące cele.
Obejrzano strony 126, 127, 129, 132–134, 136–139 oraz indeks 386–387,
w tym w pełnym rozmiarze strony z twierdzeniem i dowodem van Kampena.
Rysunki, tekst dowodu i odsyłacz w przykładzie torusa są czytelne.
Zaktualizowano główny PDF, sprawdzając zgodność ze składem.
Następna iteracja: dodatki rozdziału 8.

## Rozbudowa z 6 października 2026

Na nową prośbę autora plan z `PLAN_DZIALANIA.md` obejmuje w tym samym PDF
przyszłe rozdziały o grupach Liego, teorii Hodge'a--Bochnera oraz wymiarze 4.
Wcześniejszy zapis o osobnym skrypcie dla Freedmana jest historyczny.

- W rozdziałach 2--11 zastąpiono osobne sekcje „Dalsza lektura”
  krótkimi notkami według wzorca rozdziału 18. Zachowano adresy źródeł.
- W rozdziałach 22 i 23 dodano rysunki ruchu Whitneya i pary hiperbolicznej.
  Rozpisano warunki lokalnego ruchu, wpływ przesunięcia uchwytu na formę
  oraz przejście od lagranżjanu do bazy hiperbolicznej nad $\mathbb Z$.
  W rozdziale 19 doprecyzowano, że łuki dysku Whitneya omijają inne
  punkty przecięcia.
- W rozdziale 25 dodano lemat o ściągalności dopełnienia dysku w sferze
  homotopijnej wymiaru 5 i schemat redukcji wielokąta powierzchni.
  Źródło klasyfikacji zmieniono na pełniejszy tekst Putmana, obejmujący
  także powierzchnie nieorientowalne.
- W rozdziale 26 wyprowadzono wzór na $p_1$ wiązek Milnora z dwóch wiązek
  bazowych i rozwinięto wielomian stopnia osiem we wzorze sygnatury.
  Pełna klasyfikacja powierzchni, geometryczny krok Walla, klasyfikacja
  Bardena i twierdzenie Hirzebrucha pozostają jawnie wskazanymi wynikami
  zewnętrznymi.
- Dodatek B zbiera rachunki homologii singularnej i cechy Eulera.
  Dodatku o twierdzeniach Brouwera nie dodano: niezmienniczość obszaru
  nadal jest w skrypcie wynikiem wejściowym, a autor postawił warunek
  posiadania wcześniej wszystkich narzędzi.
- Pełne `latexmk` z Perlem z Git złożyło 391 stron wraz z indeksem
  po połączeniu pięciu nowszych commitów gałęzi zdalnej.
  Końcowy log nie ma niezdefiniowanych odsyłaczy, błędów ani `Overfull`;
  pozostał jeden `Underfull` w rozdziale 23. Obejrzano strony 360 i 364
  z rysunkami, stronę 387 z początkiem dodatku oraz strony 390--391
  indeksu. Zaktualizowano PDF w katalogu głównym.

## Korekta po uwagach autora z 6 października 2026

Poprzednie uznanie całej klasyfikacji powierzchni za wynik zewnętrzny
było zbyt zachowawcze. Krótki dowód Putmana obejmuje tylko przypadek
orientowalny, ale argument przez drzewo rozpinające, graf dualny i cięcie
krzywych daje również przypadek nieorientowalny w niewielkiej objętości.
W rozdziale 25 zastąpiono odsyłacz dowodem: pokazano kryterium
`χ=2`, istnienie krzywej nierozdzielającej, indukcję po charakterystyce
oraz lokalną relację `T²#RP² ≅ #³RP²`, sprawdzoną czterema jawnymi
przekształceniami słowa brzegowego. Jedynym jawnym twierdzeniem
wejściowym o powierzchniach pozostała triangulowalność topologiczna;
skorygowano jej opis w dodatku A i aktualny stan w planie.

W rozdziale 22 dodano przestrzenny przykład chirurgii: od dwóch dysków
na `∂B³`, przez wybór zawęźlonego rdzenia uchwytu, do torusa będącego
brzegiem otoczenia węzła trójlistnego. Rysunek pokazuje etapy, a tekst
oddziela typ abstrakcyjnej powierzchni od jej osadzenia. Dopisano także
powód, dla którego rogata sfera Alexandra wymaga nieskończonej
konstrukcji dzikiego osadzenia i nie jest wynikiem skończonej gładkiej
chirurgii.

W rozdziale 23 wyszczególniono cztery brakujące składniki pełnego
dowodu twierdzenia Walla: chirurgie poniżej środka z normalnym
obramowaniem, geometryczną realizację lagranżjanu nad `Z[π]`,
niezmienniczość wraz z torsją oraz formacje wymiaru nieparzystego.
Nie oznaczono lokalnego rachunku form jako dowodu ogólnego twierdzenia.
Pełny skład `latexmk` utworzył PDF liczący 393 strony. Końcowy log nie ma
niezdefiniowanych odsyłaczy, błędów ani `Overfull`; pozostał jeden
`Underfull` w rozdziale 23. Obejrzano rysunek na stronie 355 oraz dowód
na stronach 375--376. Indeks powstał bez odrzuconych wpisów.

## Rozwinięcie dowodu Walla — 6 października 2026

Na prośbę autora rozbudowano rozdział 23, zachowując jego etykiety.
Nowe stwierdzenie wyprowadza współczynniki przecięć z etykietami
nakrycia uniwersalnego, relację hermitowską i wzory dla
samoprzecięć. Przykład `1−t` pokazuje, dlaczego zerowa zwykła
liczba przecięć nie wystarcza do znalezienia dysku Whitneya.

Dotychczasowy lemat o lagranżjanie nad `Z` zastąpiono rachunkiem
nad `Z[π]`: podano jawne poprawki dualnych wektorów, które zerują
ich parowania i wartości `μ`, oraz warunek prostoty potrzebny dla
`L^s`. Osobno udowodniono, że suma formy z formą przeciwną jest
hiperboliczna. Lemat o pojedynczej chirurgii poniżej środka
rozpisuje ogólne położenie, stabilną normalną ramę i usunięcie
stabilizacji w zakresie `2r<n`. Dwa ciągi dokładne śladu pokazują,
dlaczego chirurgia na prymitywnym wektorze hiperbolicznym usuwa
parę bez wytworzenia niższego jądra.

W przypadku nieparzystym dodano dwa lagranżjany formacji,
elementarny ciąg dokładny, jego związek z dwoma sąsiednimi
jądrami i przykład z cokernelowym `Z/2`. Poprawiono wcześniejsze
nieścisłe zdanie utożsamiające same jądra z formacją.
Źródłami audytu były Wall, *Surgery on Compact Manifolds*,
§§1, 5--6, oraz Ranicki, *An Introduction to Algebraic Surgery*,
§9. Jawne wejścia pozostają w twierdzeniach 1.2, 5.2,
1.4, lemacie 5.7 i w realizacji relacji formacji z §6 Walla.
Dodatek A i plan uaktualniono do tego zakresu.

Po korekcie lewoliniowości odwzorowania przecięcia oraz zapisaniu
hipotez lematu 5.7 pełny skład `latexmk` dał PDF liczący 396 stron.
Log nie wykazuje błędów, niezdefiniowanych odsyłaczy ani `Overfull`;
indeks został utworzony. Obejrzano strony 370--372 z nowym dowodem.

## Scalenie równoległej rozbudowy autora (2026-10-06)

Podczas wysyłania iteracji rozdziału 7 (`b9e863a`) wykryto cztery nowe
commity: `59fd235`, `9d5e5ff`, `dab4c59` i `46fd90c`. Pobrano je
i scalono, zachowując oba ciągi historii. Konflikty dotyczyły planu,
dopisanych wpisów dziennika oraz binarnego PDF. Zachowano oba wpisy
dziennika, uaktualniono status van Kampena i odbudowano PDF z połączonych
źródeł; nie wybrano jednostronnie żadnego z gotowych PDF.

Nowe treści autora w rozdziałach 19, 22, 23, 25, 26 oraz dodatkach
pozostają w kolejce niezależnego audytu. Dodano do niej nowy dodatek B.
Plany dalszej rozbudowy zachowano jako plany autora; znaczniki wykonania
oznaczają obecność materiału, nie pozytywny wynik naszego audytu.
Bieżące iteracje nadal obejmują po jednym rozdziale matematycznym.

Porównanie całych źródeł rozdziałów 2–7 z `b9e863a` potwierdziło,
że nowa rozbudowa zmienia w nich tylko format bibliografii. Zachowano
wszystkie jej słowa, tytuły, zakresy lektur i adresy oraz cały wcześniejszy
tekst matematyczny. Obejrzano nowe zakończenia na stronach 65, 84, 101,
110, 125 i 139, a także dowód van Kampena i przykład torusa (132–133, 138).
Nie wykryto utraty poprawek ani problemów czytelności.

Kontrola integracji: 32 importy, 1187 unikalnych etykiet, 1112 poprawnych
odsyłaczy w źródle, sparowane środowiska i poprawne lokalne linki Markdown.
Względem `46fd90c` jedyną zmienioną treścią TeX jest rozdział 7;
cała pozostała treść autora została zachowana. `latexmk` potwierdza
aktualny skład i kod zakończenia 0: 397 stron, 155 wpisów indeksu,
bez błędów, niezdefiniowanych referencji, `Overfull` ani zaległego przebiegu.
Pozostają dwa ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
Wszystkie 1484 linki wewnętrzne PDF mają cele; brak `??`.
Obejrzano też spis treści i indeks (strony 1–4, 396–397).
Główny PDF zastąpiono sprawdzonym składem i porównano sumy SHA-256.

## Rozdział 8 — indeks i zachowanie treści homologicznej (2026-10-06)

Zakres: wszystkie dodatki autora do `46fd90c` w dawnym rozdziale 7,
obecnie 8. Iterację rozpoczęto na czystym `046a813`, po pobraniu
i scaleniu najnowszych czterech commitów autora.

- Porównano całe źródło z uprzednio sprawdzonym `66b220f`. Po usunięciu
  dokładnie pięciu nowych poleceń indeksu tekst matematyczny jest identyczny.
  Ostatnia zmiana w `59fd235` dotyczy wyłącznie formatu „Dalszej lektury”.
- Zweryfikowano miejsca wpisów: kompleks łańcuchów symplicjalnych,
  homologia singularna, grupy względne i zredukowane, kompleks komórkowy
  oraz stopień odwzorowania sfer. Wszystkie prowadzą do właściwych definicji.
  Przeczytano te definicje z sąsiednimi uzasadnieniami, w tym augmentację
  dla zbioru pustego, zakres skończonych CW, przypadek stopnia zero
  w porównaniu homologii i orientacje we wzorze na brzeg komórkowy.
- Kod wszystkich trzech ilustracji jest niezmieniony. Obejrzano ich skład:
  zorientowany trójkąt (141), singularny sympleks (142) i kompleks torusa
  (151). Kierunki brzegów, oznaczenia obrazu sympleksu i zerowe operatory
  brzegu torusa zgadzają się z tekstem; etykiety są czytelne.
- Bibliografia nadal wskazuje rozdział 2 książki Hatchera. Nowy dodatek B
  stanowi osobny zakres audytu; jego obecność nie zmienia ani nie zastępuje
  definicji rozdziału 8. Nie dodawano ich drugi raz.

Kontrola: 32 importy, 1187 unikalnych etykiet, 1112 rozwiązanych odsyłaczy,
sparowane środowiska i działające lokalne linki dokumentacji. Skład z tej
samej wersji źródeł jest aktualny: 397 stron, 155 wpisów indeksu i 1484
poprawne linki wewnętrzne, bez `??`. Obejrzano strony 140–143, 150–151,
153 oraz indeks 396–397; odsyłacze indeksu wskazują strony definicji.
Zmiany tej iteracji obejmują tylko plan i dziennik; nie ma potrzeby zmieniać
poprawnej treści TeX ani ponownie generować identycznego PDF.
Następna iteracja: dodatki rozdziału 9.

## Rozdział 9 — wpisy indeksu i terminologia odwzorowań (2026-10-06)

Zakres: wszystkie dodatki autora do `46fd90c` w dawnym rozdziale 8,
obecnie 9. Przed pracą pobrano zmiany: `9a783e7` był aktualny i czysty.

- Porównanie całego źródła z `66b220f` przed naszą edycją potwierdziło
  identyczność tekstu matematycznego po pominięciu pięciu nowych poleceń
  indeksu; późniejsza zmiana dotyczy wyłącznie formatu bibliografii.
- Sprawdzono miejsca indeksowania grup homotopii, grup względnych,
  spójności homotopijnej, słabej równoważności i odwzorowania Hurewicza.
  Przeczytano definicje z otoczeniem: rozróżnienie grup i zbiorów
  z wyróżnionym elementem w niskich stopniach, warunek wszystkich punktów
  bazowych, zakres CW i zgodność orientacji w wersji względnej Hurewicza.
- Poprawiono 19 wcześniejszych użyć słowa „mapa” oznaczającego ogólne
  odwzorowanie: m.in. odwzorowania par, charakterystyczne, ilorazowe,
  dołączające i ściskające równik. Dostosowano rodzaj i odmianę przymiotników.
  Zgodnie z konwencją projektu „mapa” pozostaje nazwą lokalnego układu
  współrzędnych; w tych miejscach nie chodziło o takie mapy.
  Zachowano etykietę `def:mapa-hurewicza`, aby nie naruszyć odsyłaczy.
- Cztery ilustracje zachowują swój kod. Sprawdzono dwa kierunki sklejania,
  warunek obrazu brzegu dysku w A, cylinder odwzorowania oraz nakrycie
  bukietu S¹∨S². W ostatnim przykładzie każda podniesiona sfera daje osobny
  generator, a odwzorowanie Hurewicza sumuje współczynniki; rysunek i tekst
  przedstawiają tę samą konstrukcję. Nie wymagały zmiany.

Kontrola: zmieniono wyłącznie źródło rozdziału 9. Wszystkie 32 importy,
1187 unikalnych etykiet i 1112 odsyłaczy są poprawne; środowiska sparowane.
Pełny `latexmk` zakończył się kodem 0: 397 stron, indeks ze 155 wpisami,
bez błędów, niezdefiniowanych referencji, `Overfull` ani zaległego przebiegu.
Pozostają dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
Obejrzano wszystkie strony rozdziału 154–168 i indeks 396–397;
złożenie terminów i etykiet ilustracji jest czytelne. PDF nie zawiera `??`,
a wszystkie 1484 linki wewnętrzne mają istniejące cele.
Zaktualizowano główny PDF i porównano sumy SHA-256 ze składem.
Następna iteracja: dodatki rozdziału 10.

## Rozdział 10 — indeks, ilustracje i zgodność przy brzegu (2026-10-06)

Po pobraniu zmian potwierdzono aktualność i czystość `1481067`.
Porównano cały rozdział z `66b220f`: treść matematyczna i bibliograficzna
jest identyczna po pominięciu siedmiu poleceń indeksu i zmiany formatu
„Dalszej lektury”. Kod wszystkich pięciu ilustracji jest niezmieniony.

Sprawdzono wpisy indeksu przy formach, kontrakcji i pochodnej Liego,
orientacji, orientacji brzegu, całkowaniu oraz kohomologii de Rhama.
Przeczytano definicje i związane uzasadnienia. Konwencje są zgodne
z uzupełnionym rozdziałem 1: gładkość przy brzegu przez lokalne
przedłużenie, pełna przestrzeń styczna i reguła normalnej na zewnątrz.
Uwzględniono także orientację punktów oraz warunek styczności pola do
brzegu przy definicji pochodnej Liego przez dwustronny przepływ.
Wzór Cartana dla pozostałych pól jest osobno opisany przez przedłużenie.

Obejrzano strony 169–171, 173–177, 180, 182, 186, 189 i indeks 396–397.
Rysunki poprawnie pokazują znak formy dwuliniowej, kierunek brzegu dysku,
kasowanie wspólnej krawędzi, okres na przebitej płaszczyźnie i kompleks,
który nie jest rozmaitością. Etykiety są czytelne, a indeks wskazuje
właściwe strony. Zachowano poprawną treść bez dopisywania duplikatów.

Kontrola struktury: 32 importy, 1187 unikalnych etykiet, 1112 poprawnych
odsyłaczy, sparowane środowiska i działające lokalne linki Markdown.
Aktualny sprawdzony PDF ma 397 stron; źródła i PDF tej iteracji pozostają
niezmienione. Zmieniono jedynie plan i dziennik. Następny rozdział: 11.

## Rozdział 11 — metryka i miara, usunięcie powtórzenia indeksu (2026-10-06)

Zakres: dodatki autora do `46fd90c`, na bazie czystego `d39617b`.
Porównanie z `66b220f` potwierdziło niezmieniony tekst matematyczny,
bibliografię i obie ilustracje. Autor dodał dziewięć poleceń indeksu
oraz zmienił format zakończenia. Wpis „Metryka riemannowska” występował
dwukrotnie na tej samej stronie: przy tytule i przy definicji.
Usunięto pierwsze polecenie, pozostawiając odsyłacz przy definicji.

Sprawdzono położenie wszystkich pozostałych wpisów i przeczytano
definicje z uzasadnieniami: dodatniość cofniętej metryki wymaga immersji,
przeniesienie wymaga dyfeomorfizmu, długość riemannowska nie dotyczy
ogólnej metryki lorentzowskiej, a odległość między składowymi może być
nieskończona. Opis gęstości nie wymaga orientacji; miara Hausdorffa ma
jawną normalizację i konwencję dla stopnia zero. Definicja dywergencji
poprawnie skleja się także na rozmaitości nieorientowalnej.

Obejrzano strony 190–191, 194–196, 198–200, 202, 205 i 207. Ilustracje
trzech modeli hiperbolicznych i parametryzowanej powierzchni są czytelne
oraz zgodne z opisem długości wektorów i wyznacznika Grama.
Ponowny skład potwierdził identyczność tekstu wszystkich 397 stron
i zakładek, a także obrazu wszystkich stron rozdziału 11 i indeksu.
Usunięcie podwójnego polecenia nie zmienia drukowanego indeksu, ponieważ
program indeksujący już scalał oba wystąpienia na tej samej stronie.

`latexmk` zakończył się kodem 0: 154 wpisy indeksu przyjęte bez odrzuceń,
brak błędów, niezdefiniowanych referencji i `Overfull`. Pozostają dwa
ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23. Kontrola obejmuje
32 importy, 1187 unikalnych etykiet, 1112 odsyłaczy oraz 1484 działające
linki PDF; brak `??`. Główny PDF zaktualizowano i porównano ze składem.
Następna iteracja: rozdział 12.

## Rozdział 12 — indeks koneksji i transportu (2026-10-06)

Pobranie zmian potwierdziło aktualność czystego `4793c2e`. Całe źródło
porównano z `66b220f`: poza czterema wpisami indeksu treść matematyczna,
bibliografia i oba rysunki są niezmienione. Wpisy wskazują wprowadzenie
do koneksji, jej definicję afiniczną, torsję i zgodność metryczną oraz
pochodną pola wzdłuż krzywej.

Przeczytano indeksowane definicje i powiązane argumenty: lokalność koneksji,
tensorowość torsji, transformację pochodnej wzdłuż krzywej i istnienie
transportu. W szczególności definicja nie zakłada przedłużalności każdego
pola wzdłuż krzywej do pola na rozmaitości; obejmuje postoje i samoprzecięcia.
Istnienie na całym zwartym odcinku jest uzasadnione oszacowaniem liniowego
równania, nie samym lokalnym twierdzeniem ODE.

Obejrzano strony 208–209, 213, 215, 218 i indeks 396–397. Schemat transportu
nie sugeruje metryki na podstawie samego rysunku. Przykład sfery przy
θ=π/3 pokazuje przeciwne wektory po pełnym obiegu, zgodnie z obrotem −π;
oznaczenia i strzałki są czytelne. Wszystkie wpisy indeksu mają właściwe strony.
Kontrola struktury: 32 importy, 1187 etykiet bez powtórzeń, 1112 poprawnych
odsyłaczy, sparowane środowiska i działające lokalne linki dokumentacji.
Źródła i aktualny PDF 397 stron pozostawiono bez zmian; zapisano wynik
w planie i dzienniku. Następna iteracja: rozdział 13.

## Rozdział 13 — geodezyjne, zupełność i indeks (2026-10-06)

Na czystym `5bbd500` porównano cały rozdział z `66b220f`. Jedyne dodatki
to cztery polecenia indeksu; treść, bibliografia i dziewięć ilustracji
są niezmienione. Usunięto podwójny wpis „Geodezyjna” przy tytule:
pozostaje wpis przy definicji na tej samej stronie.

Przeczytano indeksowane definicje geodezyjnej, odwzorowania wykładniczego
i dwóch rodzajów zupełności oraz ich powiązania z konwencjami książki.
Parametr geodezyjnej jest afiniczny; dziedzina exp jest jawnie określona,
a jej otwartość i gwiaździstość uzasadnione. Współrzędne normalne wynikają
z różniczki exp równej identyczności i twierdzenia o funkcji odwrotnej.
Założenie braku brzegu obowiązuje jawnie w całym rozdziale; przykłady
lorentzowskie nie są objęte wnioskami Hopfa–Rinowa.

Obejrzano strony 219, 221–224, 226–227, 229, 231–233 i indeks 396–397.
Wszystkie dziewięć ilustracji jest zgodnych z opisem: lokalne exp,
odcinek euklidesowy, antypody na sferze, modele hiperboliczne, niezupełna
przebita płaszczyzna oraz schematy Schwarzschilda i Kerra. Podpisy ostatnich
rysunków odróżniają rzuty współrzędnych od osadzenia czasoprzestrzeni
i minimalność riemannowską od maksymalności czasu własnego.

Pełny skład zakończył się kodem 0: 397 stron, 153 przyjęte wpisy indeksu,
bez błędów, niezdefiniowanych referencji i `Overfull`. Pozostają dwa
ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23. Tekst wszystkich stron
i zakładki są identyczne z poprzednim PDF; obraz stron rozdziału 13
i indeksu także jest identyczny. Kontrola 32 importów, 1187 etykiet,
1112 odsyłaczy i 1484 linków PDF przeszła; brak `??`.
Główny PDF zaktualizowano i sprawdzono zgodność ze składem.
Następna iteracja: rozdział 14.

## Rozdział 14 — krzywizna i odsyłacze do Cherna–Weila (2026-10-06)

Pobrano aktualizacje; czyste `fce6df0` było aktualne. Porównanie całego
źródła z `66b220f` potwierdziło dokładny zakres zmian autora: dziewięć
poleceń indeksu, jaśniejsze cieniowanie trzech sfer oraz dwa akapity
odsyłające do nowego rozdziału 27. Pozostała matematyka jest niezmieniona.

Sprawdzono indeksowane definicje, zwłaszcza konwencję krzywizny,
niezdegenerowane płaszczyzny w sygnaturze lorentzowskiej, znaki drugiej
formy podstawowej i skrętu narożnika oraz punkty sprzężone wzdłuż
wybranej geodezyjnej. Zmiany barw nie zmieniły współrzędnych, strzałek
ani opisów. Obejrzano wszystkie osiem ilustracji; nowe cieniowanie
na stronach 238, 260 i 263 zachowuje widoczność geometrii i oznaczeń.

Przeczytano wskazane wyniki rozdziału 27 oraz konstrukcję klasy Thoma
w rozdziale 17. Zamiast ogólnej zapowiedzi „pełnego dowodu” rozpisano
zależności: zamkniętość i niezależność od koneksji nie identyfikują jeszcze
klasy Eulera; potrzebne są klasa Thoma, identyfikacja oraz normalizacja
formy kątowej. Dodano trzy precyzyjne odsyłacze. Wyjaśniono rolę Stokesa
i sumy indeksów zer pola. To opis mechanizmu zgodnego z oryginalnym
[dowodem Cherna (1944)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/chern7.pdf).

Ta kontrola powiązania nie zastępuje pełnego audytu rozdziału 27.
W jego jedynym wpisie kolejki zapisano do rozwinięcia model względnej
kohomologii de Rhama i granicę całek wokół zer pola. Dostępny opis
[Cibotaru–Moroianu, Odd Pfaffian forms](https://arxiv.org/abs/1807.00239)
zachowano jako źródło do dalszej kontroli transgresji; timeout adresu PDF
autora nie jest podstawą do usuwania tego źródła.

Kontrola: 32 importy, 1187 unikalnych etykiet, 1115 poprawnych odsyłaczy.
`latexmk` zakończył się kodem 0: 397 stron, 153 wpisy indeksu, bez błędów,
niezdefiniowanych referencji, `Overfull` ani zaległego przebiegu. Pozostają
dwa wcześniejsze ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23.
Obejrzano strony 234, 236–238, 248–250, 252, 254, 259–260, 263, 265–266
i indeks 396–397. Nowe odsyłacze na stronie 265 są czytelne i poprawne.
Wszystkie 1487 linków wewnętrznych PDF mają cele; brak `??`.
Zaktualizowano główny PDF i porównano go ze składem. Następny rozdział: 15.

## Potok Ricciego, kiełki i dalszy dowód Walla (2026-10-06)

Przed edycją pobrano dziewięć commitów współautora do `7fa73f9`.
Do jedynej aktualnej listy w `PLAN_DZIALANIA.md` dodano osobny etap
potoku Ricciego: zależności od krzywizny i analizy, przyszłe miejsce
w jednym PDF, rachunki na sferze i torusie oraz jawne analityczne
wejście do istnienia rozwiązania. Plan rozróżnia konwencję laplasjanu
geometrycznego z rozdziału 14 i laplasjanu Hodge'a.

W rozdziale 1 wszystkie sześć użyć terminu „zarodek” dla *germ*
funkcji zmieniono na „kiełek”, zgodnie z rozdziałem 2. Dodano wpis
indeksu i regułę terminologiczną w `AGENTS.md`; etykiety pozostały
bez zmian. Poprawiono też dawny opis tej konstrukcji w dzienniku.

W rozdziale 23 dodano dowód skończonej redukcji poniżej środka dla
odwzorowania normalnego zamkniętej rozmaitości parzystowymiarowej, czyli
odpowiedniego
przypadku twierdzenia 1.2 Walla. Wykorzystano skończony model CW
z Twierdzenia~`thm:cw-morse-17`, podwójny walec odwzorowań, podniesienie
klasy charakterystycznej komórki w homotopii względnej i dokładną
kontrolę indeksów odwróconych uchwytów. Osobno opisano uchwyt
indeksu jeden, w tym przedłużenie danych normalnych. Niezależny
audyt potwierdził zakres spójności i wskazał brak ram przy wstępnym
łączeniu składowych; brak uzupełniono przed składem.

Podstawą porównania był [Wall, *Surgery on Compact Manifolds*,
§1](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf).
Pozostałe zależności geometryczne są wyliczone w dodatku A.

Pełny skład `latexmk` zakończył się kodem 0: PDF ma 399 stron,
bez błędów, niezdefiniowanych odsyłaczy i `Overfull`.
Indeks zawiera „Kiełek funkcji” na stronie 35. Obejrzano stronę 35,
strony 372--374 z nowym dowodem i obie strony indeksu 398--399;
tekst i odsyłacze są czytelne. Pozostaje wcześniejszy `Underfull`
w rozdziale 23.

## Lemat 5.7 Walla: ciąg, przecięcia i lagranżjan (2026-10-06)

W rozdziale 23 rozwinięto krok niezmienniczości przeszkody przy
normalnym kobordyzmie. Dla pary $(N,M)$ zapisano hipotezy lematu 5.7,
w tym możliwie niespójny brzeg, współczynniki w
$\mathbb Z[\pi_1(Y)]$ i rzeczywistą bazę jądra względnego.
Rozpisano bazowany ciąg
$0\to K_{k+1}(N,M)\to K_k(M)\to K_k(N)\to0$,
konwencję lewego modułu dualnego oraz konkretną mapę dualną
wyrażoną formą przecięcia. Łuki przecięcia dwóch względnych
reprezentantów wyjaśniają znikanie formy na obrazie brzegu;
łuki podwójnych punktów jednego reprezentanta wyjaśniają
znikanie udoskonalenia kwadratowego. Z tego otrzymano prosty
lagranżjan i klasę zerową formy brzegowej.

Niezależny audyt wskazał, że abstrakcyjna dualność nie dowodzi
jeszcze wzoru na mapę dualną. Tekst wymienia więc zgodność
dualności względnej z formą przecięcia jako osobne wejście
geometryczne z dowodu lematu 5.7 Walla. Dla niespójnego brzegu
odwołuje się do nakrycia indukowanego z celu, jak w uwadze 5.2.1.
Pozostawiono jawne użycie twierdzeń 1.3 i 1.4 oraz lematów 2.4,
2.6 i 5.5 Walla; zwłaszcza realizacja obramowanych immersji i
przygotowanie kobordyzmu nie wynikają z samego ciągu dokładnego.
Osobnego rozwinięcia nadal wymaga kryterium $\mu=0$ dla
obramowanego osadzenia środkowej sfery w twierdzeniu 5.2.

Źródło porównania: [C. T. C. Wall, *Surgery on Compact Manifolds*,
§§1–2, 5](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf).

Pełny skład `latexmk` zakończył się kodem 0: 401 stron, indeks
złożony, brak błędów, niezdefiniowanych odsyłaczy i `Overfull`.
Pozostał wcześniejszy `Underfull` w kroku 1 dowodu na stronie 373.
Obejrzano strony 374–377 z nowym rachunkiem i następną sekcją;
wzory, odsyłacze i diagram są czytelne.

## Integracja zmian autora do `308ba4e` i audyt rozdziału 15 (2026-10-06)

Pobrano metodą fast-forward commity `5c9dcd0` i `308ba4e` na czyste
`7fa73f9`. Przeczytano nową regułę terminologiczną w `AGENTS.md`.
Różnica rozdziału 1 obejmuje dokładnie sześć zamian „zarodek” na
„kiełek” oraz hasło indeksu; nie zmienia wzorów, hipotez ani dowodu
konstrukcji przestrzeni stycznej. Sprawdzono zgodność z rozdziałem 2
i brak pozostawionych wystąpień dawnego terminu w źródłach.
Rozbudowy Walla w rozdziale 23 i aktualizacji dodatku A nie uznano
automatycznie za sprawdzone: ich nowe wersje wpisano do jedynej kolejki
audytu. Zachowano plan autora dotyczący dalszych rozdziałów.

Porównanie rozdziału 15 z wcześniej audytowanym `66b220f` potwierdziło,
że treść matematyczna, słowa bibliografii i źródła czterech ilustracji
są identyczne. Zmiany to pięć wpisów indeksu oraz wspólne formatowanie
zakończenia. Przeczytano definicje wskazywane przez hasła: punkt i wartość
krytyczna, miara zero, transwersalność i hesjan w punkcie krytycznym.
Rozróżnienie punktu od wartości, warunek rzędu różniczki i zmiana
współrzędnych hesjanu są poprawne.

Osobno sprawdzono powiązanie z nowymi podstawami brzegu w rozdziale 1:
twierdzenie o przeciwobrazie wymaga transwersalności zarówno na pełnym
`T_pM`, jak i po ograniczeniu do brzegu. Dowód wybiera odwracalny minor
w zmiennych stycznych do brzegu, zachowując współrzędną półprzestrzeni;
otrzymuje właściwy brzeg przeciwobrazu. Przykład `f(x,y)=y` na półpłaszczyźnie
wyjaśnia potrzebę drugiego warunku. W wersji parametrycznej wyklucza się
sumę dwóch zbiorów miary zero. Nie znaleziono tu brakującego założenia
ani powodu do dublowania definicji. Treść rozdziału pozostawiono bez zmian.

Ponowny pełny skład po aktualizacji autora zakończył się kodem 0:
401 stron, 154 wpisy indeksu. Ostateczny przebieg nie ma błędów,
niezdefiniowanych odsyłaczy ani `Overfull`; pozostają dwa wcześniejsze
ostrzeżenia `h`→`ht` i `Underfull` w rozdziale 23. Sprawdzono 32 importy,
1190 unikalnych etykiet, 1123 rozwiązywalne odsyłacze oraz lokalne linki
w czterech głównych plikach Markdown. Wszystkie 1496 linków wewnętrznych
PDF mają poprawne cele; brak `??`.

Obejrzano strony 267–270, 272, 274, 276–277 i indeks 400–401:
cztery ilustracje i oznaczenia pozostają czytelne. Odtworzony skład
ma identyczny tekst i zakładki na wszystkich 401 stronach co PDF autora,
a cały rozdział 15 i indeks są również identyczne pikselowo.
Nie nadpisywano identycznej treści PDF. Następna iteracja: rozdział 16.

## Rozdział 16 — zanurzenia, otoczenia i kołnierze (2026-10-06)

Przed iteracją pobrano stan gałęzi; `445828a` było aktualne. Porównanie
ze sprawdzonym `66b220f`, wykonane przed poniższymi poprawkami, wykazało
sześć nowych poleceń indeksu oraz zmianę formatowania bibliografii.
Pozostała treść i cztery ilustracje były identyczne.

Sprawdzono definicje odwzorowania właściwego, wiązki normalnej,
obramowania, kołnierza i funkcji wyczerpującej. Hasło „Osadzenie” jest
zgodne z konwencją wyjaśnioną w rozdziale 2: oznacza tu zanurzenie
w sensie *embedding*, czyli immersję będącą homeomorfizmem na obraz.
Nie utożsamiono go z samą immersją ani nie wprowadzono nowej definicji.
Sprawdzono ilorazowy model wiązki normalnej, gładkość rzutu przy użyciu
macierzy Grama oraz ograniczenie promienia dla nieortonormalnego
obramowania na zwartej podrozmaitości.

Przeczytano dowód kołnierza wraz z podwojeniem i porównaniem kołnierzy.
Jest zgodny z konstrukcją stycznej przy brzegu: pole ma dodatnią składową
do wnętrza, lokalne przedłużenia dają jednostronne trajektorie, a ich
jednoznaczność zapewnia globalną injektywność. Zależna od punktu
szerokość jest potrzebna dla niezwartych brzegów; stała szerokość wynika
ze zwartości. Wybór szerokości przez podział jedności jest uzasadniony
w tekście. Nie dopisywano drugiego dowodu tego samego twierdzenia.

Poprawiono siedem użyć słowa „mapa” dla ogólnych odwzorowań, w tym
odwzorowań tubularnych i wykładniczych. Zachowano „mapy” oznaczające
układy współrzędnych. „Włączenie włókna” zastąpiono „inkluzją włókna”.
Przy argumentacji o grupach homotopii sfery usunięto nieprecyzyjne
zdanie „ma obraz homotopijny do punktu”: aproksymacja komórkowa daje
homotopię odwzorowania do odwzorowania stałego. To nie jest twierdzenie
o ściągalności jego obrazu jako przestrzeni. Wzory i założenia pozostały
bez zmian; nie dodano etykiet ani odsyłaczy.

Pełny skład `latexmk` zakończył się kodem 0: 401 stron i 154 wpisy indeksu.
Ostateczny log nie zawiera błędów, niezdefiniowanych odsyłaczy ani
`Overfull`. Pozostają dwa wcześniejsze ostrzeżenia `h`→`ht` i jeden
`Underfull` w rozdziale 23. Kontrola struktury: 32 importy, 1190 unikalnych
etykiet, 1123 odsyłacze ze znanymi celami; w PDF 1496 poprawnych linków
wewnętrznych i brak `??`. Obejrzano wszystkie strony rozdziału 278–292
oraz indeks 400–401. Cztery ilustracje (dysk Whitneya, otoczenie tubularne,
kołnierz i pas przepływu) są zgodne z opisami i czytelne; nowe zdania
składają się prawidłowo. Zaktualizowano główny PDF.
Następna iteracja: rozdział 17.

## Rozdział 17 — dualność, terminologia i rozkład kohomologii wiązki (2026-10-06)

Pobrano stan gałęzi; czyste `55d5c06` było aktualne. Porównanie całego
rozdziału z audytowanym `66b220f`, po uwzględnieniu dokładnie dwóch
zmian parametrów cieniowania, wykazało osiem nowych haseł indeksu
i wspólne formatowanie bibliografii. Pozostała treść była identyczna.
Sprawdzono definicje wskazywane przez hasła: iloczyny kubkowy i kapowy,
liczbę przecięcia, system lokalny, klasę charakterystyczną, indeks zera
i chirurgię. Hasło dualności prowadzi do rozdziału zawierającego jej dowód.
Konwencja brzegu iloczynu kapowego zgadza się z [Hatcherem,
*Algebraic Topology*, §3.3, s. 239–240](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
Sprawdzono zgodność kolejności czynników z orientacją przecięcia,
definicję systemu orientacji przy brzegu przez styczną lub kołnierz
oraz rozróżnienie indeksu chirurgii i indeksu uchwytu w jej śladzie.

Ujednolicono nazwę „kochain” (również w tytule sekcji) zgodnie z
`AGENTS.md`. Słowo „mapa” pozostawiono dla układu współrzędnych;
w kontekstach odwzorowań łańcuchowych, dualności, funkcji sklejających
i stopnia użyto „odwzorowania”. Etykiety i wzory tych definicji zachowano.

Przy konstrukcji klas Stiefela–Whitneya ujawniono zbyt skrótowy krok:
sam fakt, że `1,x,…,x^(r−1)` daje bazę we włóknie, nie wyjaśnia jeszcze
izomorfizmu kohomologii całej wiązki. Poprzednie zdanie o poszczególnych
„mapach” mogło też sugerować, że każdy składnik oddzielnie jest
izomorfizmem. Wprowadzono jawny rzut `π:P(E)→M` i łączne odwzorowanie
`Φ` z sumy grup kohomologii bazy z przesuniętymi stopniami.
Rozpisano rachunek względny nad komórką, przesunięcie o jej wymiar,
zgodność z homomorfizmami łączącymi oraz użycie lematu o pięciu
odwzorowaniach. Dla niezwartych baz wyjaśniono produkty po komórkach,
skończoność liczby potęg `x` i zakończenie indukcji po `dim M` krokach.
Jest to rozwinięcie potrzebnego przypadku, bez nowej, powielonej
definicji klas charakterystycznych.

Porównano konstrukcję z [Hatcherem, *Vector Bundles and K-Theory*,
§3.1, s. 78–79](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf)
oraz [twierdzeniem 4D.1 w *Algebraic Topology*, s. 432–433](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
Wskazanie tego twierdzenia dodano również w tekście dowodu.

Kontrola końcowa: `latexmk` zakończył się kodem 0, PDF ma 402 strony,
a indeks 154 wpisy. Usunięto nowe przekroczenie marginesu w zdaniu
o parach szkieletów. Ostateczny log nie ma błędów, niezdefiniowanych
odsyłaczy ani `Overfull`; pozostają dwa wcześniejsze ostrzeżenia
`h`→`ht` i `Underfull` w rozdziale 23. Sprawdzono 32 importy,
1190 unikalnych etykiet, 1123 rozwiązywalne odsyłacze, 1496 poprawnych
linków wewnętrznych PDF oraz brak `??`. Nowy tytuł sekcji z „kochainami”
jest również w spisie treści i zakładkach.

Obejrzano cały rozdział na stronach 293–310 i indeks 401–402.
Rozwinięty argument na stronie 303 mieści się w kolumnie, a nowe
cieniowanie sfer na stronach 301 i 308 zachowuje czytelność równika,
biegunów, trajektorii oraz oznaczeń indeksów. Pozostałe dwa rysunki
przedstawiają poprawnie komórkę dualną i dodatnie przecięcie na torusie.
Ich geometrii nie zmieniano. Zaktualizowano wspólny PDF.
Następna iteracja: rozdział 18.

## Kryterium osadzania Walla 5.2 (2026-10-07)

Przed kontynuacją pobrano i dołączono trzy commity współautora
`445828a`–`ef084df`, bez naruszania roboczych zmian rozdziału 1.
W rozdziale 23 rozwinięto przejście od zaniku $\mu(x)$ do
obramowanego osadzenia środkowej sfery. Rozkład grupy
$Q_{(-1)^k}(\mathbb Z[\pi])$ na orbity $g\leftrightarrow g^{-1}$
wyjaśnia, dlaczego samoprzecięcia można sparować z równymi
etykietami i przeciwnymi znakami. Łuki na dwóch płatach tworzą
zerową w $\pi_1(M)$ pętlę Whitneya. Dla $k\geq3$ transwersalność
i nierówności wymiarowe pozwalają wybrać dysk z wnętrzem
rozłącznym z rdzeniem immersji. Rozpisano zgodność ram na brzegu,
zanik przeszkody w $\pi_1(V_{2k-2,k-1})$ oraz lokalny ruch.

Pełny model produktowego otoczenia dysku i realizacja ruchu
korzystają jawnie z [Milnora, *Lectures on the h-Cobordism
Theorem*, twierdzenie 6.6 i lematy 6.7,
6.13](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf).
Adaptację od dwóch osadzonych podrozmaitości do dwóch płatów
jednej immersji przypisano [Wallowi, §5.2](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf).
Twierdzenie ograniczono do spójnej $M^{2k}$, $k\geq3$, i do
rzeczywistej obramowanej klasy regularnej homotopii. Wyraźnie
odróżniono ten przypadek od rachunku form na nakryciu indukowanym
z innej rozmaitości: uwaga 5.2.1 Walla nie przenosi nań
kryterium osadzenia. Dla wymiaru cztery kryterium nie jest
wystarczające.

Odizolowany pełny skład z aktualnej gałęzi i nowymi plikami
rozdziału 23 oraz dodatku A zakończył się kodem 0. PDF ma
403 strony, indeks zawiera hasło „Trik Whitneya — samoprzecięcia”
na stronie 367; finalny log nie ma błędów, niezdefiniowanych
odsyłaczy ani `Overfull`. Pozostał wcześniejszy `Underfull`
w kroku 1 dowodu rozdziału 23. Obejrzano strony 366–370,
w tym trzy strony nowego kryterium i sąsiedni rysunek; wzory,
odsyłacze i podpisy są czytelne.

## Dołączenie roboczych zmian rozdziału 1 (2026-10-07)

Na prośbę autora dołączono niezapisane rozwinięcie porównania
przestrzeni stycznych $T_p^AM$ i $T_p^BM$. Wykazano, że
$j_\varphi(v)=[U,\varphi,v]$ jest liniową bijekcją: każda klasa
ma reprezentanta w ustalonej mapie, a równość klas w tej mapie
oznacza równość współrzędnych. Z wcześniejszej bijekcji
$\Theta_\varphi$ wynika teraz $\Phi_\varphi=j_\varphi\Theta_\varphi$;
reguła łańcucha dowodzi niezależności od wyboru mapy.

Poprawiono także zdanie o okręgu: brzeg $S^1$ jako rozmaitości
jest pusty, choć brzeg topologiczny $S^1$ jako podzbioru
$\R^2$ jest całym okręgiem. Usunięto zbędną drugą etykietę
definicji rozmaitości z brzegiem i końcową spację. Niezależny
audyt nie znalazł błędu w nowych wzorach.

Pełny skład `latexmk` zakończył się kodem 0: 404 strony,
155 przyjętych wpisów indeksu i brak błędów, niezdefiniowanych
odsyłaczy oraz `Overfull` w finalnym logu. Obejrzano stronę 14
z rozróżnieniem dwóch znaczeń brzegu oraz strony 31–32
z dowodem identyfikacji przestrzeni stycznych; tekst i wzory
są czytelne. Główny PDF skopiowano ze sprawdzonego składu
i potwierdzono identyczny skrót SHA-256.

## Notacja zbiorów skalarnych bez zera (2026-10-07)

Na prośbę autora przyjęto $A_*:=A\setminus\{0\}$ dla
$A\in\{\Z,\Q,\R,\H,\C\}$, gdy mowa o wszystkich elementach
niezerowych. W `AGENTS.md` zapisano rozróżnienie od grupy
jednostek: $\Z^\times=\{-1,1\}$, podczas gdy $\Z_*$ zawiera
wszystkie niezerowe liczby całkowite. Audyt źródeł wykazał
jedno użycie $\R^\times$ w sensie $\R\setminus\{0\}$,
trzy jawne zapisy niezerowych skalarów zespolonych i dwa
niezerowych skalarów rzeczywistych. W rozdziale 1 zastąpiono
je przez $\C_*$ i $\R_*$ po zdefiniowaniu tych oznaczeń
przy pierwszym użyciu. Zapisów $\R^n\setminus\{0\}$
i $\C^{n+1}\setminus\{0\}$ nie zmieniano: dotyczą
przestrzeni wektorowych, a nie samych zbiorów skalarów.

Pełny skład `latexmk` zakończył się kodem 0: 404 strony,
indeks złożony, brak błędów, niezdefiniowanych odsyłaczy
i `Overfull` w finalnym logu. Obejrzano strony 15, 21 i 40:
definicje $\C_*$ i $\R_*$, wzory przestrzeni rzutowych
oraz funkcję przejścia wstęgi Möbiusa są czytelne.

## Uzupełnienie: teoria Hodge'a i intuicja operatorów (2026-10-07)

Dodano osobny rozdział 28 bez zmiany etykiet ani numerów
dotychczasowych rozdziałów. Gwiazdę Hodge'a objaśniono jako
przejście do prostopadłych kierunków z orientacją i skalą
wybraną przez metrykę. Kodyferencjał powiązano z ujemną
dywergencją, a laplasjan Hodge'a z jednoczesnym pomiarem
zamknięcia i współzamknięcia form. Harmoniczny przedstawiciel
klasy ma najmniejszą normę $L^2$; rachunek tej minimalności
umieszczono przy izomorfizmie z kohomologią de Rhama.

Własnymi dowodami objęto wzory dla gwiazdy, sprzężenie
$\delta$ z $\dd$, eliptyczność symbolu, konsekwencje rozkładu,
wzór Weitzenböcka dla $1$-form, zintegrowaną tożsamość
Bochnera i wnioski dla sfery oraz torusa. Istnienie gładkiego
rozwiązania równania $\Delta_Hu=f$ prostopadłego do jądra
zależy od analitycznej teorii eliptycznej; jego dokładne
założenia, status i źródło podano w rozdziale i dodatku A.
Połączono rozkład $2$-form w wymiarze cztery z rzeczywistym
rozszerzeniem całkowitej formy przecięcia; nie utożsamiono
jej milcząco z parowaniem form de Rhama.

Autor równolegle rozwinął liniowość odwzorowania $\Phi$ w
rozdziale 1 i dodał dwa rysunki przy konstrukcji funkcji
odcinającej. Zachowano te zmiany; nie oznaczają one pełnego
ponownego audytu tego rozdziału.
Po obejrzeniu stron 33--34 przesunięto etykiety punktu
$\varphi(p)$ i poziomu $\mu=1$, które zachodziły na
rysunek. Obejrzano także strony 398--402; zakończenie
rozdziału i lektura mieszczą się na ostatniej stronie.

MiKTeX w tym środowisku nie znalazł Perla dla `latexmk`,
więc wykonano pełną sekwencję `pdflatex` i `makeindex`
z `README.md`. Ostatni przebieg zakończył się kodem 0:
410 stron, 160 przyjętych wpisów indeksu, bez błędów,
niezdefiniowanych odsyłaczy i `Overfull`. Pozostał dawny
`Underfull` w rozdziale 23. Wynikowy indeks po ostatnim
przebiegu ma ten sam skrót SHA-256 co indeks użyty w PDF.

## Uzupełnienie: grupy Liego (2026-10-07)

Dodano osobny rozdział 29 po podstawach o rozmaitościach,
przepływach, grupach i nakryciach, zachowując numery oraz
etykiety wcześniejszych rozdziałów. Przykłady
$\mathrm{GL}(n)$, $\mathrm O(n)$, $\mathrm{SO}(n)$,
$T^k$ i $\mathrm{SU}(2)$ mają sprawdzenie gładkości działań.
Dowiedziono identyfikacji algebry Liego z polami
lewostronnie niezmienniczymi, zupełności tych pól,
jednoznaczności podgrup jednoparametrowych,
własności eksponenty i wzoru dla różniczki
działania adjungowanego.

Nakrycie $\mathrm{SU}(2)\to\mathrm{SO}(3)$ otrzymano
przez sprzężenie kwaternionowe. Wyprowadzono wzór
obrotu, surjektywność, jądro $\{\pm1\}$ i lokalne
równomierne pokrycie, a identyfikację z wcześniejszą
konstrukcją $\operatorname{Spin}(3)$ pokazano przez
element objętości algebry Clifforda. Nie korzystano
z pełnego twierdzenia Liego o całkowaniu dowolnej
algebry ani z ogólnej formuły BCH.

Pełny skład `pdflatex` i `makeindex` zakończył się kodem 0:
418 stron, 175 wpisów indeksu, brak błędów, niezdefiniowanych
odsyłaczy oraz `Overfull`. Indeks po ostatnim przebiegu
jest identyczny z użytym w PDF. Obejrzano strony 403--409;
nie ma kolizji wzorów ani końcowej lektury z nagłówkiem
lub stopką. Pozostał wcześniejszy `Underfull` rozdziału 23
oraz niewielki `Underfull` akapitu definicji podgrupy
jednoparametrowej.

## Uzupełnienie: potok Ricciego (2026-10-07)

Dodano osobny rozdział 30 dla gładkich zwartych
rozmaitości bez brzegu. Równanie
$\partial_tg=-2\operatorname{Ric}(g)$ powiązano ze
zmianą długości i obliczono rozwiązania dla metryk
Einsteina, w szczególności kurczącej się sfery
i stacjonarnego płaskiego torusa. Rozpisano zmianę
miary, ściągniętą drugą tożsamość Bianchiego,
wariację skalara oraz
$\partial_t\operatorname{Scal}
=\Delta_g\operatorname{Scal}+2|\operatorname{Ric}|^2$.
Uzgodniono znak laplasjanu z rozdziałem Hodge'a.

W wymiarze dwa wyprowadzono równanie dla krzywizny
Gaussa i, korzystając z wcześniejszego twierdzenia
Gaussa--Bonneta, liniową zmianę całkowitego pola.
Prosta zasada maksimum dotyczy już istniejącego
gładkiego rozwiązania. Dla krótkiego czasu pokazano
rachunek głównego symbolu po poprawce DeTurcka
oraz konstrukcję dyfeomorfizmów cofających metrykę.
Lokalne istnienie i jednoznaczność układu parabolicznego,
także równania ciepła odwzorowań przy zmiennej
metryce dziedziny, pozostają nazwanym wejściem
zewnętrznym opisanym także w dodatku A.

Pełny skład `pdflatex` i `makeindex` dał 424 strony oraz
176 przyjętych wpisów indeksu. Po ponownym przebiegu
nie ma błędów, niezdefiniowanych odsyłaczy ani `Overfull`;
indeks użyty w PDF jest identyczny z ostatnim wynikiem
`makeindex`. Obejrzano strony 410, 412, 414 i 415,
w tym poprawkę DeTurcka oraz końcową „Dalszą lekturę”.
Pozostały wcześniejsze dwa ostrzeżenia `Underfull`
z rozdziałów 23 i 29.

## Uzupełnienie: formy przecięcia i uchwyty w wymiarze cztery (2026-10-07)

Dodano osobny rozdział 31, pierwszy z pięciu zaplanowanych
rozdziałów czterowymiarowych. Wprowadzono kategorię TOP,
PL i DIFF oraz całkowite formy symetryczne. Rozpisano
parzystość, zmianę bazy, przykłady $H$ i $I_{1,1}$,
a dla $E_8$ pełny rachunek wyznacznika i dodatniej
określoności przez dopełnienie Schura. Graf $E_8$
wyjaśnia macierz formy, a diagram obramowanych uchwytów
wiąże przekątną z obramowaniem i wyrazy pozadiagonalne
z liczbami sprzężenia. Udowodniono homologiczny wniosek
o brzegu przy unimodularnej macierzy.

Drugi rysunek pokazuje, dlaczego wnętrze dysku Whitneya
może przecinać powierzchnię w wymiarze cztery. Rachunek
wymiarów opisano tylko jako ograniczenie ogólnej pozycji;
nie podano go jako dowodu niemożliwości usunięcia przecięć.
Po sprawdzeniu skorygowano opis powierzchni Seiferta:
domknięcie rdzenia uchwytu ma ogólnie dodatni rodzaj,
więc nie jest automatycznie sferą. Twierdzenie Freedmana
i niezmiennik Kirby'ego--Siebenmanna pozostawiono dla
osobnego późniejszego rozdziału, zgodnie z planem.

## Domknięcie rozpoczętych szkiców i przegląd (2026-10-07)

Po pobraniu zmian z `origin` sprawdzono rozpoczęte pliki
rozdziałów 31, 32, 33 i 35. Do głównego dokumentu dołączono
rozdział 32 o uchwytach Cassona i rozdział 33 o topologicznej
klasyfikacji Freedmana. Twierdzenie o osadzaniu dysku i
standardowość topologiczna uchwytu Cassona w rozdziale 32
porównano z Freedmanem--Quinnem, twierdzenia 5.2 i 5.2.1,
oraz Freedmanem, twierdzenie 1.1. Sformułowanie klasyfikacji,
warunek dla niezmiennika Kirby'ego--Siebenmanna i wnioski
w rozdziale 33 porównano z Freedmanem--Quinnem, §10.1--10.2.
W obu rozdziałach zaznaczono, które twierdzenia są zewnętrzne;
ich katalog uzupełniono w dodatku A.

Szkic `35-egzotyczne-r4.tex` porównano z lematami 1.1 i 1.2
oraz twierdzeniem 1.3 Gompfa. Poprawiono zapis
`\overline{\C P^2}` i jawnie umieszczono dwie kule we wspólnej
rozmaitości przed połączeniem ich łukiem. Zgodnie z decyzją
autora zachowano kolejność planu: ten plik pozostaje poza
głównym PDF, ponieważ rozdział 34 o Donaldsonie nie istnieje.
Nie nazywamy więc jego przeglądu kontrolą gotowego składu.

W już istniejących rozdziałach usunięto podwójne stwierdzenie
i etykietę `prop:styczna-brzeg-1` oraz naprawiono niedomknięty
nawias we wzorze w rozdziale 1. W rozdziale 26 skorygowano
kierunek izomorfizmu łączącego w ciągu Mayera--Vietorisa
i przywołano rzeczywiste hipotezy $H^3(M)=H^4(M)=0$ zamiast
silniejszego, niezałożonego warunku sfery homotopijnej.
W rozdziale 31 zmieniono „sfery” na „powierzchnie” i
ograniczono geometryczny opis przecięć do kategorii DIFF.
Kontrola kluczowych wzorów w rozdziałach 28--30 nie wykazała
błędu znaków w twierdzeniu Weitzenböcka, nakryciu
$\mathrm{SU}(2)\to\mathrm{SO}(3)$ ani poprawce DeTurcka.
W rozdziale 30 doprecyzowano warunek orientowalności przy
odsyłaczu do laplasjanu Hodge'a i źródła analitycznego.

### Granica sześciu stron dla dowodów wyników wejściowych

Jedynym argumentem redakcyjnym za pozostawieniem poniższych
wyników jako jawnych wejść jest objętość pełnego rozwinięcia
ich założeń i dowodów w stylu tego skryptu: **ponad sześć
stron na każde zagadnienie**. Liczba stron w źródle nie jest
formalnym dolnym ograniczeniem długości każdego możliwego dowodu.

- Dla geometrycznych wejść Walla sam jego rozdział 5 zajmuje
  strony 44--56 (13 stron), rozdział 6 strony 57--73
  (17 stron), a przygotowanie z rozdziałów 1 i 2 dalsze
  9 i 11 stron. Obramowany trik Whitneya potrzebny w tym
  miejscu zajmuje u Milnora §6, strony 67--84 (18 stron).
  Źródła: [Wall, *Surgery on Compact Manifolds*](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
  [Milnor, *Lectures on the h-Cobordism Theorem*, §6](https://www.degruyterbrill.com/document/doi/10.1515/9781400878055-007/html?lang=en).
- Dla sfer Milnora oryginalny dowód konstrukcji i
  rozróżnienia zajmuje drukowane strony 399--405 (7 stron),
  a pełne usunięcie przywołanego tam twierdzenia
  Hirzebrucha wymagałoby jeszcze jego dowodu. Źródło:
  [Milnor, *On Manifolds Homeomorphic to the 7-Sphere*](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf).
- Dla pozostającej w punkcie 2 klasyfikacji
  pięciowymiarowej oryginalna
  [praca Bardena, *Simply Connected Five-Manifolds*](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/barden.pdf)
  obejmuje strony 365--385 (21 stron).
- Dla osadzania dysków i klasyfikacji Freedmana same
  konstrukcje prowadzące do twierdzeń zajmują u
  [Freedmana--Quinna](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf)
  strony 23--88 (66 stron), a oryginalny
  [artykuł Freedmana](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-17/issue-3/The-topology-of-four-dimensional-manifolds/10.4310/jdg/1214437136.full)
  strony 357--453 (97 stron). Uzupełnienie konstrukcji
  geometrycznie dualnych sfer w dowodzie twierdzenia
  o dyskach zajmuje osobną
  [pracę Powella--Ray--Teichnera](https://arxiv.org/abs/2006.05209)
  (25 stron w wydaniu czasopismowym).
- Dla egzotycznych $\R^4$ źródłowa
  [praca Gompfa](https://doi.org/10.4310/jdg/1214439566)
  zajmuje strony 283--300 (18 stron) i zawiera kroki,
  które w szkicu 35 są nazwanymi wejściami.

Końcowy skład pliku głównego przez `latexmk` zakończył się
poprawnie: PDF ma 439 stron, a `makeindex` przyjął 181 wpisów
bez odrzuceń i ostrzeżeń. W dzienniku nie ma błędów,
niezdefiniowanych odsyłaczy ani `Overfull`; pozostały dwa
wcześniejsze ostrzeżenia `Underfull` z rozdziałów 23 i 29.
Obejrzano strony 421, 423, 425, 430 i 439, obejmujące nowe
rysunki, twierdzenie klasyfikacyjne i indeks. Na stronie 423
skrócono nagłówek rysunku dysku Whitneya, aby nie nachodził
na ramkę ani opis po prawej. Szkic rozdziału 35 sprawdzono
tylko w źródle: zgodnie z zachowaną kolejnością planu nie
wchodzi do tego składu.

## Wybrane dowody Walla, Milnora i konsekwencje osadzania dysków (2026-10-07)

Na prośbę autora rozwinięto najważniejsze fragmenty już
rozpoczętych rozdziałów 23, 26 oraz 32--33. W rozdziale 23
oddzielono warunek wymiarowy od ściągalności okręgu
Whitneya. Porównano zastosowanie twierdzenia 6.6 i lematów
6.7, 6.13 Milnora z jego oryginalnym sformułowaniem dla
dwóch osadzonych podrozmaitości. Dla niezmienniczości
przeszkody Walla wypisano hipotezy zaniku potrzebne do
lematów 2.4 i 2.6, fragment ciągu po odejmowaniu uchwytów
z twierdzenia 1.4 oraz macierz obliczającą dwa jądra
formacji z §6. Przykład formacji brzegowej pokazuje, dlaczego
zerowa klasa przeszkody może współistnieć z niezerowym
bieżącym jądrem. Źródła:
[Wall, *Surgery on Compact Manifolds*](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
[Milnor, *Lectures on the h-Cobordism Theorem*, §6](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf).
Konstrukcja produktowego otoczenia dysku, prosta dualność
jąder i geometryczna realizacja ruchów formacji pozostają
jawnie wskazanymi wynikami zewnętrznymi.

W rozdziale 26 rozpisano przeszkodową interpretację klasy
Eulera, dokładny odcinek ciągu Mayera--Vietorisa i rachunek
$H_3(M_{h,j})\cong\Z/|h+j|\Z$ dla $h+j\ne0$.
Doprecyzowano rozszczepienie wiązki stycznej przestrzeni
dysków, addytywność $q$ i sygnatury po sklejeniu wypełnień
oraz zmianę znaku niezmiennika przy zmianie orientacji.
Wynik $\lambda(M_k)\equiv k^2-1\pmod7$ porównano z
[Milnorem, §3](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf).
Wzór Hirzebrucha dla zamkniętych ośmiowymiarowych
rozmaitości pozostaje zewnętrznym wejściem.

W rozdziale 32 rozróżniono algebraiczną i geometryczną
dualność sfer. Stwierdzenie o grupie podstawowej dopełnienia
dysków ma rozpisany argument przez meridiany, z jawnym
użyciem topologicznej transwersalności. Sprawdzono, że
w dawnym dowodzie Freedmana--Quinna konstrukcja
geometrycznie dualnych sfer była niekompletna;
[Powell--Ray--Teichner, Twierdzenie A](https://arxiv.org/abs/2006.05209)
uzupełnia ten krok. Oryginalna numeracja twierdzenia to
5.1A, a używana w skrypcie reformatowana numeracja to 5.2.
Rozdział 33 podaje szczególną postać twierdzenia o osadzaniu
sfer, jego skutek dla grupy podstawowej po chirurgii oraz
łańcuch dalszych zewnętrznych kroków: chirurgię topologiczną,
$s$-kobordyzm, realizację form i rachunek
Kirby'ego--Siebenmanna. Ten łańcuch objaśnia zastosowanie
twierdzenia o dyskach; nie jest przedstawiany jako dowód
całej klasyfikacji Freedmana.

Po zmianach `latexmk` złożył plik główny bez błędów do
442 stron. Nie ma niezdefiniowanych odsyłaczy ani `Overfull`;
indeks przyjął 181 wpisów bez odrzuceń. Pozostały dwa
wcześniejsze ostrzeżenia `Underfull` z rozdziałów 23 i 29.
Obejrzano strony 373, 382--384, 396--397, 428--429, 432--433
oraz 442 (indeks); nowe akapity, wzory, linki i odsyłacze
są czytelne. Przyrost trzech stron jest mniejszy od
wcześniejszej estymaty 15--25 stron, ponieważ większość
rachunków potrzebnych do wybranego zakresu już znajdowała
się w tych rozdziałach.

## Pełny audyt rozdziału 23 (2026-10-07)

Przeczytano cały rozdział 23, w tym definicje form, przykłady
$E_8$ i Arfa, przygotowanie mapy poniżej środka, usuwanie par
hiperbolicznych, lemat o lagranżjanie i rachunek formacji.
Porównano użyte twierdzenia 1.2, 1.4, 5.2, 5.3, 5.7 oraz §6 z
[oryginałem Walla](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf).
Sprawdzono znaki formy hermitowskiej i zmian bazy, wyznacznik
oraz minory przykładu $E_8$, a także odsyłacze do rozdziału 22
i katalogu wyników zewnętrznych.

W definicji formy hermitowskiej dopisano addytywność i jawne
działanie pierścienia na module dualnym lewego modułu. Wzór
$\mu(ax)$ zapisano przez reprezentanta klasy $\mu(x)$ i
wyjaśniono jego niezależność od wyboru reprezentanta. W dodatku A
warunek dla triku Whitneya określono jako ściągalność konkretnego
okręgu w dopełnieniu; nie wymaga on prostej spójności całej
rozmaitości. Skorygowano też opis tego, co rozdział rzeczywiście
wyprowadza, a co pozostaje lematem źródłowym.

Audyt nie zmienia zakresu deklarowanego dowodu: produktowe
otoczenie dysku Whitneya, bazowość i prosta dualność jąder,
przygotowanie kobordyzmu, realizacja formacji oraz obliczenie
grup $L$ pozostają wskazanymi wejściami zewnętrznymi.

Końcowy skład pliku głównego przez `latexmk` zakończył się
poprawnie: PDF ma 442 strony, indeks przyjął 181 wpisów bez
odrzuceń. Nie ma błędów, niezdefiniowanych odsyłaczy ani
`Overfull`; pozostały dwa wcześniejsze ostrzeżenia `Underfull`.
Obejrzano strony 370--371 z poprawionymi definicjami; wzory
i podział stron są czytelne.

## Audyt rozdziałów 22 i 24 (2026-10-08)

W rozdziale 22 sprawdzono kolejno definicję chirurgii,
ślad i uchwyt dualny, oba ciągi homologii względnej,
znak zmiany charakterystyki Eulera, trzy przypadki
rachunku $\pi_1$, dane normalne i warunek ich
przedłużenia, lokalny ruch Whitneya oraz rozszczepienie
formy środkowej. Założenie spójności potrzebne przy
$\pi_1$ obowiązuje w całej sekcji. Rachunki i odsyłacze
do rozdziału 23 są zgodne; nie wymagają zmiany treści.
Obejrzano rysunki i sąsiedni tekst na stronach
361--363, 365--366 i 368--369 aktualnego składu.

W rozdziale 24 porównano definicję normalnych
niezmienników, zbioru struktur i dokładności z
[Wallem, §10, szczególnie lematem 10.6,
stwierdzeniem 10.7 i twierdzeniami 10.5, 10.8](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf).
Doprecyzowano, że $[X,G/O]$ ma strukturę grupy,
ale $\theta_n$ na ogół nie jest homomorfizmem;
strzałka $\theta_{n+1}$ po zawieszeniu jest nim.
Wyjaśniono też, dlaczego prosta równoważność
kobordyzmu nad $X\times I$ daje prostą równoważność
obu inkluzji końców, potrzebną do użycia twierdzenia
o $s$-kobordyzmie. Same wyniki realizacyjne i
bijekcja z $[X,G/O]$ pozostają jawnie zewnętrzne.

Końcowy skład `latexmk` zakończył się poprawnie: 442 strony,
bez błędów, niezdefiniowanych odsyłaczy i `Overfull`.
Indeks zachowuje 181 przyjętych wpisów; pozostały dwa
wcześniejsze ostrzeżenia `Underfull` z innych rozdziałów.
Obejrzano nowe akapity, ciąg i schemat na stronach 387--388;
tekst i etykiety są czytelne.

## Rozdział 18 — punkty krytyczne torusa i terminologia (2026-10-06–08)

Przed pracą pobrano stan gałęzi; czyste `ef084df` było aktualne.
Porównanie z `66b220f` potwierdziło cztery nowe wpisy indeksu,
przebudowę ilustracji torusa i zmianę cieniowania sfery. Pozostała
treść matematyczna oraz słowa i adresy bibliografii były identyczne.
Sprawdzono definicje rozmaitości stabilnej i niestabilnej, pary
Morse'a–Smale'a i kompleksu trajektorii: konwencja dotyczy przepływu
ujemnego gradientu, a skończoność sumy w różniczce odsyła do lematu
o zwartości przestrzeni trajektorii przy różnicy indeksów jeden.

Punkty krytyczne w rysunku autora miały poprawne współrzędne, ale
prowadnice podpisów były umieszczone przez przybliżone przeliczniki
`0.79` i `0.67`. Zastąpiono je współrzędnymi `axis cs` z tej samej osi
PGFPlots, na której rysowana jest powierzchnia i znaczniki. Usunięto
dwie ręcznie dopasowane elipsy obrysu: nie wynikały z projekcji torusa
i mogły przedstawiać inny kontur niż właściwa powierzchnia. Zachowano
jasnoniebieską stylistykę. Podpis wyjaśnia teraz, że znaczniki pokazują
rzuty wszystkich czterech punktów, także zasłoniętych powierzchnią.
Kontrola składu ujawniła przesunięcie prowadnic przy przenoszeniu
współrzędnych poza skalowane otoczenie osi. Wszystkie prowadnice i ich
etykiety umieszczono więc wewnątrz tej samej osi, usunięto zewnętrzne
skalowanie przez osiem i jawnie ustalono granice osi. Zachowano jednakową
skalę przestrzenną, aby nie zniekształcić torusa.

W przykładzie dopisano rozwiązanie równań krytycznych. Dla
`s=cos φ=±1`, `t=sgn(sin θ)=±1`, `L=√(1+ε²)` i `h=r/L` otrzymujemy
`sin θ=t/L`, `cos θ=εst/L` oraz `(x,y,z)=(sR+tεh,0,th)`.
Stąd bezpośrednio wynika `f=εsR+trL`. Dodany odsyłacz do ilustracji
wiąże obliczenie z jej znacznikami. Niezależne obliczenie dla
`R=2`, `r=0.69`, `ε=0.16` potwierdziło przynależność do torusa,
zerowanie obu pochodnych, nieosobliwość hesjanów i kolejno indeksy
`0,1,1,2`. Wartości krytyczne to w przybliżeniu
`−1.018776187`, `−0.378776187`, `0.378776187`, `1.018776187`.
Nie zmieniano poprawnej kolejności podpoziomic: dysk, pierścień,
torus bez dysku, torus.

Ujednolicono „odwzorowanie” w opisach przyczepiania komórek, przejść,
ewaluacji i konstrukcji kompleksu CW. Zachowano „mapę” w sensie
układu współrzędnych Morse'a oraz przy strukturze na przestrzeni
trajektorii. „Mapy wykresów” doprecyzowano jako parametryzacje wykresów.

### Ponowne pobranie zmian współautora — 8 października

Na prośbę użytkownika ponownie sprawdzono GitHuba. Pobrano dziesięć
commitów `f0f8b8a`–`f895347`. Rozdział 18 nie był w nich zmieniany.
Lokalny tekst i wpis dziennika zabezpieczono w osobnym stashu, następnie
przesunięto gałąź metodą fast-forward i przywrócono pracę. Konflikt
w `PRZEGLAD.md` dotyczył dopisania różnych wpisów na końcu pliku:
zachowano pełny dziennik z `f895347` i dopisano lokalny wpis. Nie usuwano
ani nie zastępowano wpisów współautora. Źródło rozdziału 18 połączono
bez konfliktu.

Sprawdzono zmiany zasad redakcyjnych, listę importów oraz nowe statusy
audytów współautora. Aktualny skład ma 33 rozdziały i dwa dodatki.
Szkic `35-egzotyczne-r4.tex` celowo nie jest importowany: zgodnie z planem
czeka na rozdział o Donaldsonie. Uzupełniono tę informację i strukturę
źródeł w `README.md`; odświeżono zakres i kolejkę w `PLAN_DZIALANIA.md`.
Zachowano raporty audytów współautora rozdziałów 22–24, 26 i 31–33,
wyraźnie odróżniając je od własnej kontroli przy scaleniu.

### Kontrola końcowa rozdziału 18

Pełny skład `latexmk` zakończył się poprawnie: 443 strony, bez błędów,
niezdefiniowanych odsyłaczy i `Overfull`. Pozostały dwa wcześniejsze
ostrzeżenia `Underfull` w rozdziałach 23 i 29 oraz dwa automatyczne
rozszerzenia ustawienia pływającego rysunku `h` do `ht`. Indeks przyjął
181 wpisów bez odrzuceń i ostrzeżeń. Kontrola źródeł potwierdziła
38 importów, 1327 unikalnych etykiet i 1285 rozwiązywalnych odsyłaczy;
PDF nie zawiera `??`, a wszystkie 1716 odsyłaczy wewnętrznych prowadzą
do istniejących stron. Obejrzano skład rozdziału na stronach 316–331,
w tym wszystkie pięć ilustracji, i trzy strony indeksu 441–443.
Nowe obliczenia i rysunek torusa są czytelne na stronie 320.

Przed zatwierdzeniem ponownie pobrano zdalną gałąź: nie doszły dalsze
commity współautora. Zaktualizowano główny PDF z tego sprawdzonego
składu. Następna iteracja obejmuje dodatki do rozdziału 19.

## Rozdział 19 — orientacja sklejenia i lokalny ruch Whitneya (2026-10-08)

Rozpoczęto od czystego, wypchniętego `471720b`. Pobranie zdalnej gałęzi
nie wykazało nowych commitów. Porównanie z audytowanym `66b220f`
potwierdziło trzy nowe hasła indeksu i przebudowę jednej z pięciu
ilustracji. Po pominięciu tych elementów i formatowania bibliografii
jedynym nowym fragmentem matematycznym był warunek, że wnętrza łuków
Whitneya omijają pozostałe punkty przecięcia. Sprawdzono zakres
definicji kobordyzmu, rdzenia i współrdzenia oraz pola gradientopodobnego,
zgodność indeksów, konwencję ujemnego gradientu i treść trzech haseł.

W przebudowanym podpisie ilustracji sfera–torus pominięto warunek
orientacji, zachowany w przykładzie. Przywrócono go i doprecyzowano,
że zmienia się brzeg wyjściowy, a wejściowa sfera pozostaje brzegiem
kobordyzmu. Dwa pierścienie przy drugim typie sklejenia dają butelkę
Kleina. Rozwinięto rozpoznanie torusa bez powoływania się na późniejszą
klasyfikację powierzchni: sklejenie opisuje dyfeomorfizm okręgu
zachowujący orientację, którego izotopię do identyczności otrzymujemy
przez interpolację podniesienia do prostej. Podano jawny dyfeomorfizm
ilorazu na `S¹×S¹`; stałość parametru izotopii przy końcach zapewnia
gładkość na szwie.

Usunięto dwie elipsy obrysu torusa, które nie pochodziły z projekcji
powierzchni parametrycznej. Zastosowano jawne granice osi, jednakową
skalę przestrzenną i jasnoniebieską powierzchnię jak w rozdziale 18.
Po obejrzeniu składu odsunięto podpisy obu rozmaitości pod rysunek,
aby podpis torusa nie stykał się z jego dolnym konturem.

Warunek autora o wnętrzach łuków Whitneya jest potrzebny: ruch ma
usunąć wybraną parę, pozostawiając pozostałe przecięcia bez zmian.
Rozwinięto dotychczasowy opis „przesunięcia paska” do modelu
`U×D^(r−1)×D^(s−1)`, gdzie `r=k`, `s=m−k−1`.
Jawna izotopia z funkcją odcinającą zachowuje współrzędne normalne,
więc przecięcia przesuwanej sfery z nieruchomą drugą sferą występują
wyłącznie przy obu współrzędnych normalnych równych zeru. Redukuje to
kontrolę do ruchu dwóch łuków w płaszczyźnie. Wyjaśniono odwracalność,
nośnik, przeniesienie normalnego pogrubienia i wybór rozłącznych
otoczeń. Nadal jawnie zakładamy istnienie osadzonych, czystych,
prawidłowo obramowanych dysków; nie wyprowadzamy go z samej sumy
znaków równej `±1` ani z trywialności wiązki normalnej dysku.
Porównano model z [Milnorem, §6, lemat 6.7 i następujący po nim ruch](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf)
i dodano to źródło do dalszej lektury.

Poprawiono dziewięć użyć „mapy” na „odwzorowanie” w opisie różniczki,
dyfeomorfizmów przedziału, przyczepienia i przejścia przepływem.
Zachowano trzy użycia dotyczące rzeczywistych map Morse'a i modelowych.

Pełna kompilacja zakończyła się poprawnie: 443 strony, bez błędów,
niezdefiniowanych odsyłaczy i `Overfull`. Pozostały dwa wcześniejsze
ostrzeżenia `Underfull` z rozdziałów 23 i 29 oraz dwa rozszerzenia `h`
do `ht`. Indeks nadal ma 181 przyjętych wpisów bez odrzuceń i ostrzeżeń.
Sprawdzono 38 importów, 1327 unikalnych etykiet, 1285 odsyłaczy źródła
i 1716 poprawnych odsyłaczy wewnętrznych PDF; w tekście nie ma `??`.
Obejrzano cały rozdział na stronach 332–343, wszystkie pięć ilustracji
i trzy strony indeksu 441–443. Szczegółowo sprawdzono nowe sklejenie
i ilustrację na stronie 335 oraz rozwinięty ruch na stronach 342–343.
Ponowne pobranie gałęzi przed publikacją nie wykazało zmian współautora.
Główny PDF zastąpiono sprawdzonym składem. Następny etap: rozdział 20.

## Rozbudowa: geometria Kleina, wymiar trzy i geometryzacja (2026-10-08)

Na prośbę autora dodano trzy osobne rozdziały w jednym skrypcie:
29a-geometria-kleina.tex po grupach Liego,
30a-poincare-trzy.tex i 30b-geometrizacja-thurstona.tex
po potoku Ricciego. Kolejność prowadzi od działania grup
do przestrzeni jednorodnych, a następnie od ewolucji metryki
do jej zastosowań w topologii wymiaru trzy. Istniejące etykiety
pozostały zachowane; nowe pliki mają własne etykiety.

Rozdział o geometrii Kleina wyprowadza identyfikację orbity
z $G/G_p$ przy jawnie wskazanym zewnętrznym twierdzeniu
o ilorazie przez domkniętą podgrupę. Przykłady obejmują
przestrzenie euklidesowe i afiniczne, $\mathbb{RP}^n$,
sfery, torusy i dysk Poincarégo. Rozróżniono skuteczne
i nieskuteczne działanie na torusie oraz geometrię projektową
od metryki sferycznej.

Rozdział o Poincarém w wymiarze trzy łączy istniejący potok
Ricciego z analizą szyjek, chirurgią, wygaśnięciem i odtworzeniem
topologii. Twierdzenia Perelmana oraz techniczna kontrola
chirurgii są jawnie oznaczone jako wyniki zewnętrzne,
zgodnie z opracowaniem Morgana--Tiana. Dowód końcowego
wniosku z tych wyników rozpisano, a postać topologiczną
otrzymano przy jawnym użyciu wygładzania Moise'a;
nie przedstawia się go jako samodzielnego pełnego dowodu
twierdzeń Perelmana.

Rozdział o geometryzacji podaje osiem modeli Thurstona,
ich metryki, przykładowe ilorazy i rozróżniki topologiczne.
Twierdzenie po rozkładzie pierwszym i cięciu JSJ
jest jawnym wynikiem zewnętrznym, zgodnym ze źródłami
Thurstona, Scotta oraz Morgana--Tiana. Związek z potokiem
Ricciego jest opisem idei, bez przypisywania skryptowi
dowodu geometryzacji.

Zaktualizowano kolejność importów, mapę skryptu,
katalog wyników zewnętrznych, dokumentację struktury
i aktualną tabelę zakresu. Prefiksy nazw starych plików
odtąd są historyczne, a numerację w PDF wyznacza
kolejność importów. Etap oznacza dodanie treści;
nie jest niezależnym audytem matematycznym nowych rozdziałów.
Wcześniejsze lokalne zmiany audytowe rozdziałów 20, 21 i 25
odłożono przed pobraniem zmian współautora.

Pełny skład z pliku głównego dał 466 stron. Log nie zawiera błędów,
niezdefiniowanych odsyłaczy ani ostrzeżeń `Overfull`; pozostają dwa
wcześniejsze ostrzeżenia `Underfull` w rozdziałach 23 i 29. Indeks
przyjął 210 wpisów bez odrzuceń i ostrzeżeń. Obejrzano strony
415, 420, 428, 434, 437 i 440 z nową treścią; nie ma nowych rysunków.
`latexmk` zgłosił jedynie komunikat środowiska MiKTeX o niesprawdzonych
aktualizacjach, po czym potwierdził aktualność wynikowego PDF.
## Uporządkowanie skryptu i domknięcie wymiaru cztery (2026-10-08)

Przed zmianami pobrano `origin/review/rozdzialy-matematyka`;
gałąź lokalna i zdalna były zgodne. Zachowano robocze dodatki autora:
iloczyny prosty i półprosty oraz iloraz modułów w rozdziale 5,
a także dodatek C o grupach macierzowych. Kontrola porównawcza
wykazała, że przy rozbudowie ilorazu zniknęły definicja podmodułu
i pierwsze twierdzenie o izomorfizmie, używane przez rozdziały 3 i 6.
Przywrócono je bez zmiany etykiet. W dowodzie addytywności rangi
uzasadniono dokładność lokalizacji przez rachunek ułamków,
a powtórzone objaśnienie trywialnego iloczynu półprostego usunięto.

Zgodnie z decyzją autora angielskie `embedding` w źródłach skryptu
nazywa się „zanurzeniem”, a odwzorowanie z samą injektywną
różniczką „immersją”. Zachowano starą etykietę
`prop:osadzenie-Wall-52-22`, aby nie zerwać odsyłaczy.
W miejscu dotyczącym czysto topologicznego sklejenia komórki
opisano wprost homeomorfizm na domknięty obraz.
Definicję grupy Pin umieszczono przy odbiciach w algebrze
Clifforda i wyprowadzono jej dwukrotne nakrycie grupy
ortogonalnej z wcześniej udowodnionego nakrycia Spin.
Sekcja o grafach przed kompleksami CW definiuje drogę,
cykl, drzewo, las, korzeń i liść oraz dowodzi dwóch
elementarnych własności używanych przy drzewach chirurgii
i uchwytów Cassona.

Dodatek C powiązano odsyłaczami z przykładami w rozdziale
o grupach Liego. Tam zachowano obliczenia gładkości
i przykłady, usuwając powtórzone definicje zbiorowe.
Zmieniono zapis zbioru niezerowych skalarów na
$\mathbb K_*$. Sprawdzono źródłowy rachunek ilorazu
modułów i rangę wyłącznie nad dziedziną całkowitości.

Rozdziały uporządkowano w pięciu częściach bez zmiany
istniejących etykiet. Grupy Liego, geometria Kleina,
Chern--Weil i Hodge tworzą blok geometrii globalnej;
chirurgia pozostaje jednym blokiem, a potok Ricciego
prowadzi bezpośrednio do wyników w wymiarze trzy.
Po rozdziałach Freedmana dodano osobny rozdział o
Donaldsonie: równanie ASD i tożsamość energii są
wyprowadzone, natomiast diagonalizacja i analityczne
wejścia przestrzeni moduli są jawnie zewnętrzne.
Istniejący rozdział Gompfa o egzotycznych $\R^4$
włączono po nim do wspólnego PDF; jego trzy głębokie
wejścia są wymienione w dodatku A. Klasyfikacja
Bardena i wzór Hirzebrucha pozostają precyzyjnie
cytowanymi wynikami zewnętrznymi: pełne dowody
przekraczają uzgodnioną granicę długości.

Nie dodano dowodów Borsuka--Ulama, Brouwera i
niezmienniczości obszaru. Rozwinięta w skrypcie
homologia nie zawiera jeszcze potrzebnego rachunku
modulo $2$ dla przestrzeni projektowych, a pełne
przejście lokalne w niezmienniczości obszaru nie jest
przygotowane. Zgodnie z warunkiem autora nie dopisano
tych twierdzeń do dodatku A.

Pełna kompilacja przez `latexmk` i `makeindex` dała 498 stron.
Nie ma błędów, niezdefiniowanych odsyłaczy ani ostrzeżeń
`Overfull`; pozostały dwa wcześniejsze ostrzeżenia `Underfull`
w rozdziałach o grupach Liego i przeszkodzie chirurgicznej.
Indeks przyjął 282 wpisy bez odrzuceń i ostrzeżeń.
Sprawdzono 1437 unikalnych etykiet i brak odsyłaczy
do etykiet nieistniejących. Ekstrakcja tekstu PDF nie wykazała
`??`. Obejrzano strony 100 i 151 z nowymi definicjami,
471--473 i 476 z wymiarem cztery, 486 i 491--494
z dodatkiem C oraz stronę 497 indeksu. Tabela wymiarów
i nowe odsyłacze są czytelne; nie dodano rysunków.

Osobno przeliczono wszystkie rodziny dodatku C: otwarte
$GL$, jądro wyznacznika $SL$, macierze antysymetryczne
dla $O$ i $SO$, antyhermitowskie dla $U$ i $SU$,
bloki symplektyczne nad $\R$ i $\C$ oraz macierze
kwaternionowo antyhermitowskie dla zwartej $Sp(n)$.
Wymiary ilorazów $PGL$, $PSL$, $PU$ i $PSp$
wynikają z wymiarów ich podgrup centralnych;
homomorfizm mnożnika daje dodatkowy parametr $GSp$,
a iloraz przez skalary usuwa go w $PGSp$.
Porównano każdy wynik z tabelą na stronie 493 i
sprawdzono przykłady w małym wymiarze.

## Kolejność rangi i iloczynu tensorowego modułów (2026-10-08)

Autor wskazał błąd kolejności w rozdziale 5: definicja
\(\operatorname{rank}_R M=\dim_K(M\otimes_R K)\) poprzedzała
konstrukcję \(M\otimes_R K\) dla modułów. Pozostawiono dowód wymiaru
przestrzeni ilorazowej przy ilorazie, a definicję rangi,
addytywność i przykład z torsją przeniesiono za definicję iloczynu tensorowego
modułów oraz rozszerzenie skalarów. Zachowano wcześniejsze etykiety.

Dowód addytywności korzystał z zapisu ułamkowego bez uzasadnienia.
Dodano izomorfizm \(M\otimes_R\operatorname{Frac}(R)\cong
(R\setminus\{0\})^{-1}M\) wraz z konstrukcją obu odwzorowań.
Zmieniono też objaśnienie rangi, by nie sugerowało rozkładu
każdego modułu nad dziedziną na część wolną i torsyjną.
Pełny skład `latexmk` zakończył się poprawnie: 499 stron, bez
niezdefiniowanych odsyłaczy, błędów i ostrzeżeń `Overfull`.
Indeks przyjął 282 wpisy bez odrzuceń i ostrzeżeń; dwa
`Underfull` pochodzą z innych rozdziałów. Obejrzano strony
124--126 z rozszerzeniem skalarów, lokalizacją i addytywnością rangi.

## Terminologia iloczynu tensorowego modułów (2026-10-08)

W rozdziale 5 tam, gdzie mowa o konstrukcji $M\otimes_R N$,
użyto pełnej nazwy „iloczyn tensorowy”: dotyczy to własności
uniwersalnej, odwzorowań tensorowych, homomorfizmu z iloczynu
oraz opisu lokalizacji. „Tensor prosty” pozostaje nazwą elementu
postaci $m\otimes n$. Etykiety twierdzeń i odsyłacze zachowano.
Pełny skład ma 499 stron, bez błędów, brakujących odsyłaczy
i ostrzeżeń `Overfull`; indeks przyjął 282 wpisy bez ostrzeżeń.
Obejrzano stronę 123 z poprawionymi nazwami twierdzeń.

## Termin „rozwłóknienie” (2026-10-08)

W rozdziale o geometryzacji cztery użycia „włóknienia”
dotyczyły struktury Seiferta, czyli *fibration*.
Zmieniono je na „rozwłóknienie” i dopisano zasadę do
`AGENTS.md`. „Wiązka” (*fiber bundle*) i „włókno”
(*fiber*) pozostają odrębnymi terminami; etykiety
sekcji i twierdzenia zachowano.
Pełny skład ma 499 stron, bez błędów, brakujących odsyłaczy
i `Overfull`; indeks przyjął 282 wpisy bez ostrzeżeń.
Obejrzano stronę 454 z nowym nagłówkiem i tabelą geometrii.

## Ponowny audyt rozdziału 5 i prośba autora o terminologię (2026-10-09)

Przed pracą pobrano bez konfliktów 12 commitów `b912682`–`386ecb6`
od wspólnego stanu `34e683b`. Autor dodał m.in. geometrię Kleina,
Poincarégo w wymiarze trzy, geometrie Thurstona, Donaldsona oraz
włączył egzotyczne R⁴ i dodatek C. Książka ma teraz 38 rozdziałów
w pięciu częściach i trzy dodatki; prefiks pliku przestał odpowiadać
numerowi w PDF. Deklaracje audytów współautora zachowano jako takie;
ich pobranie nie oznacza niezależnej weryfikacji tych rozdziałów.

Zakres tej iteracji matematycznej: cała aktualna treść rozdziału 5,
z ponownym sprawdzeniem nowych iloczynów grup, ilorazów modułów,
lokalizacji i rangi. Na wyraźną prośbę ze zrzutu dodatkowo wykonano
ograniczone zmiany notacji i terminologii w plikach 03, 21, 23 i 30b.
Nie przypisujemy im statusu pełnego audytu przy tej okazji.

### Zmiany i uzasadnienia

- **Układ §5.1.** Wprowadzono pięć równorzędnych podsekcji: grupy i ilorazy,
  grupy wolne i iloczyn wolny, prezentacje, iloczyn prosty i iloczyn
  półprosty. Rozproszone nagłówki przykładów i jednolinijkowe bloki
  wzorów zastąpiono spójnymi akapitami oraz środowiskami przykładów,
  stwierdzeń i uwag. Zachowano twierdzenia, przykłady, wcześniejsze
  etykiety, indeksowane hasła i rysunek słów; skrócenie składu nie
  wynika z usunięcia omawianych konstrukcji.
- **Uzasadnienia iloczynów grup.** Dopisano rachunek łączności iloczynu
  półprostego, wyjaśniono automorfizm i rozszczepiony ciąg dokładny,
  podano jawny rozkład elementu w rozszczepionym rozszerzeniu.
  Izomorfizm C_m × C_n ≅ C_mn dla względnie pierwszych m,n uzasadniono
  rzędem elementu ([1],[1]); objaśniono cykliczność i rząd.
  Dla grupy diedralnej policzono symetrie, a postać Ax+v izometrii
  euklidesowej wyprowadzono przez polaryzację i bazę ortonormalną.
- **Dziedzina całkowitości i ciało.** Dodano definicje dzielnika zera,
  dziedziny i ciała, własność skracania oraz przykłady Z, Q, K[t]
  i kontrprzykład Z/6Z. To usuwa używanie tych założeń bez wyjaśnienia
  przy randze modułu.
- **Ciało ułamków.** Dodano konstrukcję klas par (a,s), dowód
  przechodniości relacji i niezależności działań od przedstawicieli,
  odwrotności oraz injekcji R → Frac(R). Wyjaśniono Q i K(t), w tym
  formalny charakter ułamków wielomianowych. W rozdziale 5.5 kolejność
  jest teraz następująca: ciało ułamków, lokalizacja, izomorfizm z
  tensorem, ranga i jej addytywność.
- **Lokalizacja i skalary.** Zachowano konstrukcję autora, uzupełniając
  rozróżnienie skalaru a/u ∈ K i wektora m/s ∈ S⁻¹M. Podano działanie
  skalaru także na M ⊗_R K, sprawdzono łączność i wyjaśniono pozostałe
  prawa. Przykład Z/2Z tłumaczy, dlaczego relacja lokalizacji musi mieć
  dodatkowy czynnik t; nie wolno skracać niezerowego skalaru w dowolnym
  module. Przykłady lokalizacji Z i Z ⊕ Z/2Z objaśniają znikanie torsji.
  Ponownie sprawdzono oba odwzorowania izomorfizmu i dokładność ciągu
  użytego w dowodzie addytywności rangi. Źródło porównawcze konstrukcji:
  [Stacks Project, Localization, §10.9](https://stacks.math.columbia.edu/tag/00CM).
- **Założenie skończonego generowania.** W końcowej uwadze o rozkładzie
  modułu nad pierścieniem głównym dodano brakujące ograniczenie do
  modułów skończenie generowanych. Bez niego torsjowolny moduł nie musi
  być wolny (np. Q jako moduł nad Z). Nie dopisywano tu pełnego
  twierdzenia strukturalnego; potrzebę objaśnienia nazwy pierścienia
  głównego odnotowano w rejestrze pojęć do decyzji.
- **Notacja par.** Formalne generatory mają teraz postać [(m,n)]
  w rozdziale 5 oraz [(v,w)] w rozdziale 3. Wyraźnie rozróżniono
  generator modułu wolnego od jego klasy modulo relacje; dotyczy to
  także tensora nad pierścieniem nieprzemiennym.
- **Terminologia.** „Moduł projektywny” zastąpiono „modułem rzutowym”
  w rozdziale 5 i pliku 21; poprawiono też „projektowym” w pliku 23.
  Zachowano etykietę `uwaga:moduly-projektywne`, aby nie zerwać odsyłaczy.
  Siedem wystąpień „trójrozmaitości” w pliku 30b zastąpiono odmienionymi
  formami „rozmaitości trójwymiarowej”. Reguły zapisano w `AGENTS.md`.

### Rejestr pojęć i dokumentacja

Sprawdzono, że definicje geometrii Kleina, geometrii modelowej i rozmaitości
geometrycznej już znajdują się w plikach 29a i 30b, wraz z przykładami.
Nie dodano drugich wersji. Do `PLAN_DZIALANIA.md` wpisano pierwszą partię
potwierdzonych braków objaśnień: monoid, pierścień główny, indeks podgrupy
i własność wirtualna, nilpotentność i rozwiązalność, uśrednianie po
stabilizatorze, ostrzyk oraz wypełnienie Dehna. To lista do decyzji autora,
nie deklaracja ukończenia audytu słownika całej książki.

Uproszczono `PLAN_DZIALANIA.md`: usunięto powtarzające się historyczne
plany napisania już istniejących rozdziałów, zachowano tabelę pokrycia,
warunkowe i odłożone propozycje oraz granice dowodów. Do każdego
numerowanego rozdziału przypisano właściwy plik. Historia szczegółowych
planów jest w Git i wcześniejszych wpisach niniejszego dziennika.
W `README.md` poprawiono nieaktualne oznaczenie pliku 35 jako szkicu poza
składem, dodano plik Donaldsona i dodatek C oraz właściwą ścieżkę Perla
z PortableGit na dysku E. Nadal są tylko cztery pliki dokumentacji.

### Kontrola ukończonego etapu

Pełna kompilacja `latexmk` i indeks zakończyły się poprawnie: **496 stron**,
bez błędów, brakujących lub powtórzonych odsyłaczy i ostrzeżeń `Overfull`.
Pozostały dwa wcześniejsze `Underfull` w innych rozdziałach i dwa
automatyczne rozszerzenia położenia rysunku z `h` do `ht`.
Indeks przyjął 285 wpisów, bez odrzuceń i ostrzeżeń.

Sprawdzono 44 importy, kompletność wszystkich 45 plików źródłowych,
1441 unikalnych etykiet i 1393 wystąpienia odsyłaczy. Wszystkie wcześniejsze
etykiety i źródła rysunków zachowano; poza rozdziałem 5 różnice w LaTeX
ograniczają się dokładnie do wskazanych zamian notacji i terminologii.
W PDF nie ma `??`; 1990 odsyłaczy wewnętrznych prowadzi na istniejące strony.
Obejrzano cały rozdział 5 (strony 109–123), jego rysunek, zmienioną
konstrukcję tensora na stronie 74, terminologię na stronach 387–388 i 403,
rozdział Thurstona na stronach 448–453 oraz indeks 493–496.
Formuły, podpisy i nowe podsekcje są czytelne. Zaktualizowano wspólny PDF.

## Audyt h-kobordyzmu — rozdział 24, plik 20 (2026-10-09)

Baza: `dbfe600`. Przed rozpoczęciem pobrano stan zdalny; nie było nowych
commitów współautora. Przeczytano cały plik `20-h-kobordyzm.tex` i sprawdzono
używane w nim twierdzenia o przestawianiu, przesuwaniu oraz znoszeniu
uchwytów z poprzedniego rozdziału. Ta iteracja zmienia treść jednego
rozdziału; numer 24 w PDF wynika z nowej kolejności książki.

### Naprawy i uzupełnienia

- W wymianie uchwytu indeksu 1 na 3 poprawiono konstrukcję okręgu
  przecinającego wybraną sferę pasa raz. Ominięcie pozostałych sfer
  pasa nie wynika z pozycji ogólnej, bo mają kowymiar 1. Uzasadnia je
  spójność dolnego brzegu z usuniętymi stopami uchwytów i jawny wybór
  drogi poza pozostałymi rurkami.
- Usunięto nieuprawnione przejście od zanurzonego cylindra homotopii
  do izotopii okręgów. W poziomicy po 2-uchwytach nullhomotopię
  poprawiamy względnie do zanurzonego dysku. Jego koncentryczne okręgi
  tworzą izotopię, ponieważ każdy przekrój jest zanurzeniem.
  Wymiar poziomicy co najmniej 5 zapewnia zarówno brak samoprzecięć,
  jak i brak utraty rzędu różniczki.
- Nową parę 2–3 tworzymy przy małym okręgu wewnątrz tego dysku.
  Standardowe obramowanie z modelu narodzin jest transportowane
  przez izotopię; nie zakładamy swobody nadania urodzonemu uchwytowi
  dowolnie skręconego obramowania.
- Przed zniesieniem pary 1–2 wyjaśniono przestawienie nowego
  2-uchwytu poniżej starych: jego sfera przyczepienia pochodzi
  z regularnego przepływu i omija ich sfery pasa, więc nie ma
  zabronionych trajektorii. Przy odwróceniu kobordyzmu dopisano,
  że nowy indeks m−3≥3 nie odtwarza wcześniej usuniętych 1-uchwytów.
- W lemacie o dopełnieniu jawnie zapisano zakres wszystkich indeksów.
  Dla k=2 porównano oba dopełnienia przez retrakcje deformacyjne
  na wspólną część brzegu. Dla k=m−3 opisano odwrócenie górnego
  fragmentu, który zawiera wyłącznie uchwyty indeksu m−2.
  Warunek ten uzasadnia zastosowanie tego samego rachunku od N₊.
- Obramowany trik Whitneya pozostaje wynikiem zewnętrznym.
  Wskazano dokładne założenia używanej wersji Milnora, w tym
  injektywność grup fundamentalnych dopełnienia przy wymiarze
  przesuwanej podrozmaitości 2. Sprawdzono je dla całych rodzin
  sfer; w skrajnym przypadku zamieniono ich role, a następnie użyto
  odwrotnej izotopii. Nie twierdzimy, że trywialność wiązki nad
  dyskiem automatycznie przedłuża zadane obramowanie brzegowe.
  Nieaktualny adres Lücka–Macko zastąpiono źródłem Milnora.
- W opisie ruchu Whitneya doprecyzowano, że nieruchome są końce
  przedłużonych łuków poza usuwanymi przecięciami, a nie same
  punkty przecięcia. Dysk zachowuje standardowe naroża w tych
  punktach. Istniejący schemat jest zgodny z tak opisanym ruchem.
- Przy geometrycznej realizacji operacji kolumnowych uzasadniono
  istnienie obramowanej wstęgi: dopełnienie sfer przyczepienia
  kowymiaru co najmniej 2 jest spójne drogowo, a ramki można uzgodnić
  wzdłuż łuku. Wstęga nie musi omijać sfer pasa; ich przecięcia
  mają zmienić się zgodnie z operacją na kolumnach.
- We wniosku o sferze homotopijnej rozwinięto wycięcie i ciąg
  dokładny pary (Σ,W). Przy orientacjach dysków indukowanych z Σ
  odwzorowanie Z→Z² ma postać a↦(a,a); jego injektywność daje
  H_n(W)=0, a kokernel daje H_{n−1}(W)=Z. Dopiero obrazy dwóch
  klas brzegowych w tym kokernelu są przeciwnymi generatorami.
  Podano bezpośredni odsyłacz do homologicznego kryterium Whiteheada.
- Cztery użycia słowa „mapa” dla odwzorowania zastąpiono poprawną
  terminologią (ostatnie usunięto przy przepisaniu rachunku homologii).
  Pozostałe lematy, redukcję całkowitą macierzy, indukcję usuwania
  uchwytów i rozróżnienie homeomorfizmu od dyfeomorfizmu sprawdzono.

Źródła porównawcze:
[Milnor, *Lectures on the h-Cobordism Theorem*, twierdzenie 6.6,
lematy 6.7 i 6.13 oraz §8](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf),
[Morgan, Lecture III, §4](https://www.math.columbia.edu/~jmorgan/Lecture_III_H-cobordism_Theorem.pdf).
Powyższe uzupełnienia nie zastępują pełnego dowodu zewnętrznego
lematu obramowanego Whitneya; rozdział jawnie odróżnia go od
przeprowadzonych tutaj redukcji.

### Zmiany autora podczas audytu

Kontrola stanu zdalnego przed publikacją wykryła nowe zmiany do `2777149`:
commity `224d680`, `f2b1960`, `2777149` i merge `6e8adaf`.
Odłożono lokalny rozdział i dziennik, wykonano aktualizację fast-forward,
a następnie przywrócono własną pracę bez konfliktów. Autor nie zmienił
rozdziału o h-kobordyzmie. Zachowano jego nowe opisy wiązek i przykład
tautologiczny w pliku 01, rysunek Ricciego, operatory Re/Im i odsyłacze.
Poprawiono jedynie literówkę „Iloczn” w nowym tytule stwierdzenia
w pliku 05; nienumerowane podsekcje i pozostałe zmiany autora zachowano.

Wynik scalenia zastąpił rejestr brakujących pojęć starą tabelą audytu
i dawnymi propozycjami, dublując wcześniejszą część `PLAN_DZIALANIA.md`.
Przywrócono rejestr i zwięzły plan z `dbfe600`, dopisując nowy zakres
kontroli wiązek i Ricciego. Nie usunięto żadnej nowej propozycji
merytorycznej autora; zastąpiony blok był wcześniejszą wersją list.

### Kontrola ukończonego etapu po scaleniu

Pełna kompilacja `latexmk` wraz z indeksem zakończyła się poprawnie:
**503 strony**, bez błędów, brakujących lub powtórzonych odsyłaczy
i ostrzeżeń `Overfull`. Pozostały trzy ostrzeżenia `Underfull`: jedno
w nowym tekście o wiązce tautologicznej i dwa wcześniejsze w innych
rozdziałach, a także dwa automatyczne rozszerzenia położenia rysunku
z `h` do `ht`. Indeks przyjął 294 wpisy bez odrzuceń i ostrzeżeń.

Kontrola źródeł: wszystkie 44 importy, 1446 unikalnych etykiet i 1397
wystąpień odsyłaczy. Wcześniejsze etykiety i trzy ilustracje rozdziału
24 zachowano. Własna różnica w LaTeX względem `2777149` obejmuje
wyłącznie plik 20 i pojedynczą literówkę w pliku 05; zmiany autora
w pozostałych plikach nie zostały nadpisane. PDF nie zawiera `??`,
a wszystkie 1995 odsyłaczy wewnętrznych prowadzą na istniejące strony.

Obejrzano cały rozdział 24 (strony 381–389), wszystkie trzy schematy
i indeks 500–503. Kontrola układu po scaleniu objęła dodatkowo strony
45–47 i 52 z wiązkami autora, stronę 127 z poprawionym tytułem
stwierdzenia oraz stronę 440 z nowym rysunkiem Ricciego. Rysunki
i wzory mieszczą się w składzie, oznaczenia są czytelne.
Kontrola tych stron autora nie zastępuje pełnego audytu ich matematyki;
pozostały zakres zapisano w planie. Wspólny PDF zaktualizowano.

## 11 października 2026 — rozdział 25: torsja i s-kobordyzm

Zakres: pełna lektura pliku `tex/rozdzialy/21-torsja-s-kobordyzm.tex`,
obecnego rozdziału 25 PDF, względem `1ee001a`. Ponowne pobranie zmian
11 października nie wykazało nowych commitów autora. Zgodnie z nową
prośbą dalsza kolejność to rozdziały od 25 wzwyż; stan i rozróżnienie
pełnego audytu od kontroli późniejszych różnic zapisano w planie.

### Poprawki i ich uzasadnienia

- Założono jawnie spójność W. Spójne brzegi same nie wykluczają
  dodatkowej zamkniętej składowej kobordyzmu.
- Poprawiono bazę kompleksu: po jednym podniesieniu rdzenia na uchwyt
  jest bazą nad Z[π], natomiast wszystkie translacje tych podniesień
  dają bazę nad Z. Wskazano prawą translację B·g = g⁻¹B i transport
  orientacji normalnej, także w nieorientowalnym W.
- Zapisano jawnie zmianę macierzy A′ = V⁻¹AU przy zmianach baz e′ = eU,
  f′ = fV. Wiersze mnożymy przez współczynniki z lewej, kolumny z prawej;
  opis prowadzenia pasów uwzględnia wymaganą klasę drogi i kowymiar.
- Zachowano i sprawdzono dowód normalności grupy elementarnej oraz
  abelowości K₁. Rozwinięto rachunek odwrotności jednostki 1−t−t⁻¹
  w Z[C₅]; argument z modułem wyznacznika odróżnia jej klasę od zera.
  Redukcję całkowitą nazwano zgodnie z użyciem algorytmu Euklidesa.
- Niezależność torsji od kontrakcji ma teraz jawny dowód na wolnych
  modułach Cᵢ. Dla dwóch kontrakcji użyto F = ∂s+t∂ = I+N,
  projekcji P = ∂s oraz PN=N, NP=0. Iloczyn czterech elementarnych
  macierzy blokowych daje diag(F,I). Nie trzeba zakładać, że moduły
  brzegów są wolne, ani niejasno stabilizować ich dopełnień rzutowych.
  Równość rang nieparzystej i parzystej sumy wyjaśnia augmentacja.
- Doprecyzowano wolną ścianę w elementarnym zwinięciu i dodano przykład
  trójkąta. Stożek odwzorowania łańcuchowego otrzymał jawny wzór,
  wyjaśnienie acykliczności i przykład identyczności; wskazano wcześniejszą
  wersję kochainową. Charakterystyka prostej homotopii przez torsję
  pozostaje jawnym twierdzeniem zewnętrznym.
- Niezależność od rozkładu oparto na dokładnym porównaniu kompleksów
  Morse'a i triangulacji zgodnych ze strukturą gładką (Milnor, lemat 9.1
  i twierdzenie 9.3). Usunięto nieprecyzyjne odwołanie do teorii Cerfa
  bez podania konkretnego twierdzenia. Rachunki lokalnych ruchów
  zachowano i odróżniono od globalnego twierdzenia porównawczego.
- Usunięto kolistość w użyciu lematu Whitneya: obowiązuje już dla
  rozkładu o indeksach od k do m−2, przed uzyskaniem postaci normalnej.
  Rozpisano izomorfizmy π₁ poziomicy i dopełnień. W kowymiarze dwa
  stosujemy wspólny obszar E i retrakcje na niego, a na górnym krańcu
  dualny rozkład od N₊. Nie utożsamiamy abstrakcyjnych izomorfizmów
  grup z homomorfizmami indukowanymi przez potrzebne inkluzje.
- Sprawdzono hipotezy obramowanego lematu Whitneya dla całych rodzin
  sfer, z zamianą ich ról w skrajnym indeksie. Wynik Milnora o
  obramowaniu, przytoczony dokładnie w rozdziale 24, nadal jest
  wejściem zewnętrznym. Równe etykiety dają ściągalność pętli;
  sama trywialność wiązki nad dyskiem nie daje ruchu Whitneya.
- W redukcji indeksów rozwinięto wybór dysku, izotopię koncentrycznych
  okręgów i transport standardowego obramowania narodzonej pary 2,3.
  Przy wymianie wyższych indeksów używa się równoległego dysku
  D^{j+1}×{v} w nowym brzegu, a nie rdzenia we wnętrzu kobordyzmu.
  Wyjaśniono przestawienie nowego uchwytu przed starymi i zachowanie
  dolnego ograniczenia indeksów podczas redukcji od góry.
- Rozwinięto realizację dowolnej torsji. Początkowe 2-uchwyty mają
  standardowe przyklejenia i obramowania. Bazowe sfery o trywialnej
  wiązce normalnej reprezentują generatory względnej homologii.
  Ocena w₂ jest addytywna i nie zmienia się pod działaniem π₁, więc
  znika na sferach realizujących kolumny macierzy. Funkcje sklejające
  i stabilizacja π₁(SO(q)) uzasadniają, że w₂=0 wystarcza dla normalnej
  wiązki rangi co najmniej trzy nad S². Dopiero wtedy wybieramy
  obramowania i przyczepiamy 3-uchwyty.
- Dla obu brzegów realizacji wyjaśniono przejście przez nakrycia
  uniwersalne i kryterium homologiczne Whiteheada. Dualna macierz
  jest sprzężoną transpozycją A z inwolucją g↦w(g)g⁻¹, więc ma
  odwrotność (A⁻¹)*. Lemat dualności wskazano jako wynik Milnora,
  z uwzględnieniem charakteru orientacji.
- W addytywności torsji rozpisano blok pozadiagonalny kontrakcji,
  zamieniono d na ∂ i uwzględniono klasę [−1] wynikającą z permutacji
  baz według stopni. Znika ona dopiero w odpowiednim ilorazie.
  Doprecyzowano, że klasyfikacja jest względem oznaczonego brzegu
  wejściowego. Sprawdzono argument sklejenia dowodzący jednoznaczności.
- Poprawiono oba schematy: pierwszy pokazuje ściągalność pętli przy
  równych etykietach i odsyła do pełnych założeń; „różnicę etykiet”
  zastępuje iloczyn w grupie. W drugim znikanie [A] jest jawnym
  warunkiem, a nie wnioskiem z samej odwracalności. Usunięto niedziałający
  odsyłacz bibliograficzny i dodano hasła indeksu K₁, grupa Whiteheada
  i torsja Whiteheada. Wszystkie dawne etykiety pozostają zachowane.

Źródła porównawcze:
[Milnor, *Whitehead Torsion*, §§1, 3–4, 7, 9–11](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorwh.pdf),
[Kreck–Lück, *The Novikov Conjecture*, twierdzenie 6.15(1)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/owsem.pdf),
[Khan, *The s/h-Cobordism Theorem*](https://qkhan.pages.iu.edu/research/SLIDES/Lecture02_KHAN.pdf)
oraz obramowany lemat z
[Milnor, *Lectures on the h-Cobordism Theorem*, §6](https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf).

### Kontrola ukończonego etapu

Pełna kompilacja `latexmk` wraz z indeksem zakończyła się poprawnie:
**505 stron**, bez błędów, brakujących lub powtórzonych odsyłaczy
i ostrzeżeń `Overfull`. Pozostały cztery `Underfull`: trzy wcześniejsze
w plikach 01, 29 i 23 oraz jedno łagodne w akapicie o niezależności
torsji w bieżącym rozdziale, obejrzanym na stronie 395. Nie ma kolizji
tekstu ani wyjścia poza kolumnę. Pozostają także dwa wcześniejsze
automatyczne rozszerzenia położenia rysunku z `h` do `ht`.
Indeks przyjął 297 wpisów bez odrzuceń i ostrzeżeń.

Sprawdzono wszystkie 44 importy, 1446 unikalnych etykiet i 1404
wystąpienia odsyłaczy. Własna różnica LaTeX względem `1ee001a`
obejmuje wyłącznie plik rozdziału 25. Zachowano wszystkie jego
wcześniejsze etykiety i oba rysunki, z opisanymi wyżej poprawkami.
PDF nie zawiera `??`; wszystkie 2005 odsyłaczy wewnętrznych
prowadzą na istniejące strony.

Obejrzano skład całego rozdziału, strony 390–401, oraz indeks 502–505.
Oba schematy na stronach 391 i 399 sprawdzono także w powiększeniu;
etykiety są czytelne i zgodne z tekstem. Po doprecyzowaniu źródła
twierdzenia o prostej homotopii powtórzono pełny skład, kontrolę
odsyłaczy oraz ogląd zmienionych stron 394–395. Wspólny PDF
zaktualizowano. Kontrola zdalnej gałęzi przed publikacją ponownie
nie wykazała nowych commitów autora.

## 11 października 2026 — warunki geometrii modelowej i ilorazy

Autor wskazał Definicję 33.1.1 i poprosił o rozwinięcie zwartości,
maksymalności, stabilizatora, dyskretności oraz teorii rozmaitości
ilorazowych. Przed rozpoczęciem pobrano stan zdalny; gałąź przeglądu
była czysta i zgodna z `origin/review/rozdzialy-matematyka` na
`15dc513`. Zmiany umieszczono w rozdziałach 16 i 33, bez powtarzania
definicji działania i przestrzeni $G/H$ już obecnych w rozdziale 16.

W rozdziale o geometrii Kleina dodano znormalizowaną miarę Haara
jako jawny wynik zewnętrzny i pełny rachunek uśredniania iloczynu
skalarnego po zwartym stabilizatorze. Wprowadzono właściwe działanie
i udowodniono równoważność jego właściwości ze zwartością
stabilizatora dla działania przechodniego na $G/H$. Dowód z lokalnymi
przekrojami pokazuje dokładnie, gdzie użyta jest zwartość $H$.
Dla metryki jednorodnej rozpisano jednolity czas istnienia geodezyjnych
i zastosowano wcześniejsze twierdzenie Hopfa–Rinowa. Dla swobodnej
dyskretnej podgrupy wyprowadzono gładką strukturę ilorazu, nakrycie,
metrykę ilorazową, zupełność i identyfikację grupy podstawowej.
Przykłady odróżniają działanie właściwe od samej zwartości
stabilizatorów przy nieprzechodnim działaniu oraz dyskretność od
swobody.

W rozdziale 33 rozdzielono trzy warunki modelu: zwarty stabilizator,
istnienie przynajmniej jednego zwartego ilorazu oraz maksymalność
grupy przekształceń. Wyjaśniono, że konkretna rozmaitość geometryczna
może być niezwarta, ale jej metryka jest zupełna i lokalnie
jednorodna. Dodano przykłady torusa, cylindra $S^1\times\R^2$,
$S^2\times S^1$, $\mathbb{RP}^3$ oraz ilorazu z osobliwym punktem.
Dowód maksymalności grupy euklidesowej sprowadza każdą metrykę
niezmienniczą względem translacji i $\mathrm O(3)$ do stałej
wielokrotności metryki euklidesowej. Odróżniono pojedynczy iloraz
geometryczny od geometryzacji po cięciu, doprecyzowano lewy iloraz
$\Gamma\backslash X$ i wskazano źródła głębokich twierdzeń
Singera, Myersa–Steenroda i Thurstona w wersji Scotta.

Ten etap sprawdza nowe wyjaśnienia i ich połączenie z istniejącymi
odsyłaczami. Pełny niezależny audyt tabeli ośmiu modeli, JSJ
i sformułowania geometryzacji pozostaje zadaniem wymienionym
wyłącznie w `PLAN_DZIALANIA.md`.

### Kontrola składu

Pełny `latexmk` z indeksem zakończył się poprawnie: **509 stron**.
W logu nie ma błędów, brakujących lub powtórzonych odsyłaczy ani
ostrzeżeń `Overfull`. Cztery komunikaty `Underfull` pochodzą z
wcześniejszych akapitów w plikach 01, 29, 21 i 23; nie dotyczą
nowych sekcji. Indeks przyjął 302 wpisy, nie odrzucił żadnego
i nie zgłosił ostrzeżeń. Nowe hasła prowadzą na strony 296, 298,
460 i 461.

Sprawdzono tekst PDF na stronach 292–301 i 459–465 oraz wygląd
stron 299, 461 i 463 w powiększeniu; nagłówki, wzory i odsyłacze
są czytelne i nie kolidują z marginesami. Po stwierdzeniu, że dawna
ścieżka do Perla z README nie istnieje na bieżącym komputerze,
poprawiono ją na działającą ścieżkę instalacji Git. Wspólny PDF
zaktualizowano po tej kontroli.

## 12 października 2026 — orbifoldy i nagłówki sekcji 33.1

Autor zaakceptował uzupełnienie orbifoldów w rozdziałach 16 i 33
oraz polecił zamienić numerowane `\subsection` w sekcji 33.1 na
`\subsection*`. Przed zmianami pobrano aktualny stan gałęzi;
nie było nowych commitów. Trzy nagłówki w 33.1 nie miały etykiet,
więc zachowano istniejące odsyłacze i numerację twierdzeń.

W rozdziale 16 wprowadzono efektywny orbifold gładki przez
zgodne lokalne mapy $B/H$ z grupą skończoną $H$. Rozróżniono
strukturę orbifoldu od przestrzeni podkładowej i wyjaśniono,
że każda rozmaitość jest orbifoldem z trywialnymi grupami
lokalnymi, ale orbifold z punktem stożkowym nie jest rozmaitością
jako orbifold. Przykłady obejmują iloraz dysku przez obroty,
krawędź zwierciadlaną i $\R^3/\{\pm I\}$. Dowód lokalnego modelu
ilorazu przez skutecznie działającą podgrupę dyskretną używa
właściwości działania, skończoności stabilizatora i współrzędnych
wykładniczych. Dla definicji wskazano rozdział 13 notatek Thurstona.

W rozdziale 33 opisano orientowalny orbifold powierzchniowy
z punktami stożkowymi, wyprowadzono wzór na orbifoldową
charakterystykę Eulera przez ważenie komórek oraz obliczono
przykłady o wszystkich trzech znakach. Iloraz torusa przez
inwolucję daje poduszkę $S^2(2,2,2,2)$. Zdefiniowano dobre
orbifoldy i zaznaczono złe przypadki $S^2(p)$ oraz
$S^2(p,q)$ przy $p\ne q$ na podstawie twierdzeń 2.3–2.5
Scotta. Przy lokalnym modelu Seiferta sprawdzono rachunkiem,
że działanie cykliczne jest swobodne na przestrzeni całkowitej,
choć ma punkt stały na dysku bazy. Rozróżniono klasyfikację
geometrii rozmaitości całkowitej od metryki zadanej bazy.

### Kontrola składu

Pełny `latexmk` wraz z indeksem zakończył się poprawnie:
**512 stron**, bez błędów, brakujących lub powtórzonych odsyłaczy
i bez ostrzeżeń `Overfull`. Cztery komunikaty `Underfull`
dotyczą wcześniejszych akapitów w plikach 01, 29, 21 i 23;
pozostały też dwa wcześniejsze komunikaty o zmianie położenia
rysunku z `h` na `ht`. Indeks przyjął 309 wpisów, bez odrzuceń
i ostrzeżeń; nowe hasła orbifoldowe prowadzą na strony 299,
465 i 466.

Sprawdzono tekst nowych fragmentów na stronach 299–300 i 465–467
oraz wygląd stron 299, 465 i 466 w powiększeniu. W spisie treści
i zakładkach PDF nie ma już numerowanych podsekcji 33.1, natomiast
Definicja 33.1.1 zachowała numer. Zaktualizowano wspólny PDF.

## 12 października 2026 — zgodność map orbifoldowych

Na uwagę autora rozpisano skrótowy warunek z Definicji 16.3.7.
Zanurzenie jednej mapy w drugiej określają teraz jawnie injektywny
homomorfizm grup lokalnych i gładkie zanurzenie modeli, spełniające
równanie ekwiwariantności oraz równanie zgodności z rzutami na
przestrzeń podkładową. Zgodność atlasu sformułowano punktowo przez
wspólną mniejszą mapę na każdym przecięciu. Doprecyzowano, że
grupą lokalną punktu w mapie jest stabilizator jego podniesienia,
a grupa całej mapy jest grupą lokalną jej środka.

Na przykładzie $D/C_m$ pokazano oba rodzaje zanurzeń: mapę z grupą
trywialną przy zwykłym punkcie oraz mapę z grupą $C_m$ przy środku.
W dowodzie stwierdzenia o ilorazie $\Gamma\backslash X$ wskazano
konkretną wspólną mapę na przecięciu dwóch modeli, inkluzję i
sprzężenie stabilizatorów oraz oba wymagane warunki. Źródłem
definicji pozostaje rozdział 13 notatek Thurstona wskazany w tekście.

### Kontrola składu

Pełny `latexmk` z indeksem zakończył się poprawnie: **513 stron**.
W logu nie ma błędów, brakujących lub powtórzonych odsyłaczy ani
ostrzeżeń `Overfull`. Cztery komunikaty `Underfull` i dwa o zmianie
położenia rysunku z `h` na `ht` dotyczą wcześniejszych miejsc.
Indeks przyjął 309 wpisów, bez odrzuceń i ostrzeżeń. Sprawdzono tekst
oraz wygląd stron 299–300: definicja, wzory, przykład i dowód są
czytelne, bez kolizji z marginesami. Zaktualizowano wspólny PDF.

## 12 października 2026 — przegląd krótkich rozdziałów o wymiarze cztery

Na prośbę autora przeprowadzono wspólny etap dotyczący rozdziałów 34–38:
sprawdzono luki w przejściach dowodowych, przykłady i rysunki. Przed
pracą `git pull --ff-only` potwierdził zgodność czystej gałęzi
`review/rozdzialy-matematyka` ze stanem zdalnym. Etap obejmuje pięć
rozdziałów o wymiarze cztery, każdy krótszy niż 10 stron w poprzednim
składzie. Głębokie twierdzenia Freedmana, Donaldsona, Gompfa,
Rokhlina i De Michelisa–Freedmana pozostają jawnie cytowanymi wejściami.

W rozdziale 34 skorygowano rysunek Whitneya: czerwony płat przechodzi
przez punkt $q$ leżący we wnętrzu dysku $D$, a etykiety są oddzielone.
W rozdziałach 35–36 odróżniono immersje dysków i sfer z punktami
podwójnymi od topologicznych zanurzeń, zgodnie z terminologią
rozdziału 1. Dla obramowanych immersyjnych sfer w sformułowaniu
twierdzenia o zanurzaniu rozpisano równość
$\lambda(A_i,A_i)=2\mu(A_i)+e(A_i)=0$ przy $\pi_1=1$,
$\mu(A_i)=e(A_i)=0$; wyjaśnia ona użycie wersji z homotopią
regularną u Powella–Raya–Teichnera. Dodano odsyłacz z przykładu
$E_8\oplus E_8$ do późniejszego wniosku Donaldsona.

W rozdziale 37 sprawdzono znak drugiej klasy Cherna dla wiązki
$\mathrm{SU}(2)$ przez rozwinięcie wyznacznika i wynikającą z niego
tożsamość energii ASD. Dodano jawny niepłaski przykład na
euklidesowej $\R^4$, zaznaczając jego nieskończoną energię.
Wniosek o formie $E_8\oplus E_8$ pokazuje krok po kroku, że
$\operatorname{ks}=0$ nie wystarcza do wygładzenia zamkniętej
rozmaitości: parzystość formy przeczy diagonalizacji Donaldsona.
Krótko porównano ten przykład z twierdzeniem Rokhlina, którego
dowód nie jest tu przypisywany rachunkowi energii.

W rozdziale 38 rozpisano przykład śladu zerowo obramowanego splotu
trywialnego, zgodność obramowania dysku plastra z obramowaniem
Seiferta oraz przykład węzła $J$, który jest topologicznie, lecz nie
gładko plastrowalny. Schemat TikZ pokazuje oba zanurzenia użyte w
kroku indukcji Gompfa i położenie zwartego świadka $K_n$.
Na koniec podano precyzyjnie, jako wynik zewnętrzny
De Michelisa–Freedmana, istnienie kontinuum małych egzotycznych
$\R^4$; konstrukcja Gompfa daje duże przykłady, ponieważ każdy
$R_n$ z $n\geq1$ zawiera blok $X$ niezanurzalny w standardowej $\R^4$.
W dodatku A dopisano oba nowe wejścia zewnętrzne, aby katalog zależności
zgadzał się z rozdziałami.

### Kontrola składu

Po zmianach złożono cały dokument poleceniem `latexmk -pdf
-interaction=nonstopmode -halt-on-error -file-line-error
-outdir=build/sklad geometria_i_topologia_rozniczkowa.tex` w odrębnym
drzewie roboczym z tym samym stanem Git i plikami tego etapu. Oddzielny
skład był konieczny, ponieważ podczas pierwszego składu w głównym
drzewie pojawiła się równoległa, niezakończona zmiana rozdziału 1;
nie włączono jej do niniejszego etapu ani do sprawdzonego PDF.
`latexmk` zakończył pracę poprawnie. PDF ma 515 stron, rozdziały
34–38 zajmują odpowiednio 5, 6, 3, 3 i 6 stron, a dodatek A zaczyna
się na stronie 495. W logu nie ma błędów, brakujących odsyłaczy,
powtórzonych etykiet ani przepełnień wierszy. Indeks przyjął
312 wpisów, bez odrzuceń i ostrzeżeń. Pozostały cztery ostrzeżenia
`Underfull \hbox` i dwie automatyczne zmiany położenia rysunków
z `h` na `ht` w innych częściach książki. Obejrzano strony 476,
486–488 i 494: schemat Whitneya, przykłady Donaldsona oraz
schemat indukcji Gompfa są czytelne. Zaktualizowano wspólny PDF.

## 12 października 2026 — odsyłacz w konstrukcji wiązki stycznej

Na prośbę autora w podsekcji „Wiązka styczna” rozdziału 1 usunięto
powtórzony, skrótowy rachunek zmiany bazy derywacji i współrzędnych
wektora. Wcześniejszy wywód z etykietą
`eq:transformacja-derywacji` zawiera już definicje, regułę łańcuchową
i wzór na macierz Jacobiego. W konstrukcji $TM$ wystarczy więc
odsyłacz do tej reguły oraz wynikowy wzór na odwzorowanie przejścia,
potrzebny do sprawdzenia topologii i gładkości wiązki.

Do etapu włączono wcześniejsze niezapisane zmiany rozdziału 1,
ponieważ nowy odsyłacz zależy od dodanej w nich etykiety.
Sprawdzono kierunek macierzy Jacobiego i jednoznaczność obu nowych
etykiet. Długą równość macierzową w tym wywodzie podzielono na
dwa wiersze po stwierdzeniu przepełnienia o 25,36~pt podczas
pierwszej próby składu. Nie przeprowadzono przy tym pełnego
audytu pozostałych nowych części o wiązkach; ich zakres pozostaje
w `PLAN_DZIALANIA.md`.

### Kontrola składu

Pełny `latexmk` z indeksem w odrębnym drzewie roboczym zakończył się
poprawnie: PDF ma 517 stron. Izolacja chroniła wynik przed równoległym
zapisem PDF przez TeXworks w głównym katalogu. W końcowym logu nie ma
błędów, brakujących odsyłaczy, powtórzonych etykiet ani przepełnień.
Indeks przyjął 312 wpisów, bez odrzuceń i ostrzeżeń. Pozostały cztery
komunikaty `Underfull \hbox` i trzy zmiany położenia rysunków z `h`
na `ht`. Obejrzano strony 36, 40 i 54: poprawiony rysunek mapy,
dwuwierszowa równość oraz odsyłacz przy wiązce stycznej są czytelne.
Wspólny PDF zaktualizowano ze sprawdzonego składu.

## 12 października 2026 — lektura, źródła i lematy Gompfa

We wszystkich 38 rozdziałach jest teraz zwarty blok „Dalsza lektura”
o jednakowym nagłówku i składzie. Brakujące bloki dodano w plikach 01,
25, 30b, 32 i 35; w plikach 29a, 30a i 34 zastąpiono odmienne nagłówki.
Dobór lektur odpowiada tematowi konkretnego rozdziału, bez nowych zadań.

W pliku 35 dowiedziono kierunku od gładkich lub lokalnie płaskich dysków
plastra do odpowiedniego zanurzenia śladu. Wyjaśniono rachunek
$x^\perp\cong-E_8\oplus\langle-1\rangle$ w rozmaitości otaczającej
z pracy Gompfa z 1983 roku, wyraźnie odróżniając go od formy zwartego
bloku $X$. Lemat 1.1 z pracy z 1985 roku rozpisano na topologiczny ślad,
przeniesienie atlasu, wygładzenie dopełnienia i ogolenie. Przy lemacie 1.2
wyjaśniono konstrukcję otaczającej rozmaitości o formie hiperbolicznej,
rolę pięciu i sześciu pięter uchwytów Cassona, kontrolę obramowań oraz
zastąpienie topologicznych dysków rdzeniami gładkich uchwytów. Osobno
wskazano twierdzenia Quinna, Cassona, Freedmana i właściwe lematy Gompfa
jako wejścia zewnętrzne; ten opis nie jest pełnym dowodem tych lematów.
Uściślono też, że własna indukcja dowodzi części o skończonych indeksach,
a oryginalne twierdzenie 1.3 obejmuje jeszcze $R_\infty$.

W odsyłaczach zastąpiono strony arXiv `abs` przez adresy `pdf` tej samej
pracy oraz inne strony lądowania bezpośrednimi PDF-ami, gdy potwierdzono
tożsamość publikacji. Dotyczy to m.in. prac Perelmana, Scotta, Thurstona,
Freedmana, Quinna i Powella–Raya–Teichnera. Oryginalne artykuły Gompfa
z 1983 i 1985 roku oraz De Michelisa–Freedmana z 1992 roku nie mają
potwierdzonej wersji arXiv; adresy Project Euclid z końcówką `.pdf`
zwracały w kontroli HTML lub blokadę, więc przy nich pozostawiono DOI.
Strony będące indeksami wielu wykładów i strony interaktywne pozostawiono
bez arbitralnego zastępowania inną pracą.

W podsekcji „Wiązka styczna” usunięto powtórzony skrót o zmianie
współrzędnych i pozostawiono odesłanie do
`eq:transformacja-derywacji` oraz wzór na przejście potrzebny
do konstrukcji wiązki. Niezależnego, niezakończonego akapitu motywacyjnego
w rozdziale 1 nie włączono do tego etapu ani do składanego PDF.

### Kontrola składu

Pełny skład `latexmk` z indeksem wykonano w odrębnym drzewie roboczym,
zawierającym tylko zmiany niniejszego etapu. Wynikowy PDF ma 519 stron;
rozdział 38 zajmuje strony 493–498, czyli nadal sześć stron. Ponowne
uruchomienie `latexmk` potwierdziło, że wszystkie cele są aktualne.
W końcowym logu nie ma błędów, brakujących odsyłaczy, powtórzonych
etykiet ani przepełnień wierszy. Indeks przyjął 312 wpisów, bez
odrzuceń i ostrzeżeń. Pozostały cztery komunikaty `Underfull \hbox`
oraz trzy automatyczne zmiany położenia rysunków z `h` na `ht`.
Obejrzano strony 54 i 63 rozdziału 1 oraz 496 i 498 rozdziału 38:
odsyłacz do transformacji, oba bloki lektury i schemat indukcji są
czytelne. Wspólny PDF zaktualizowano ze sprawdzonego składu.

## 13 października 2026 — holonomia i rozkład de Rhama w rozdziale 14

W `14-krzywizna.tex` po lokalnej charakteryzacji płaskości dodano dwie sekcje.
Pierwsza definiuje pełną i ograniczoną grupę holonomii, dowodzi własności
grupowych, sprzężenia przy zmianie punktu bazowego oraz równoważności
`R=0` z trywialnością holonomii ograniczonej. Przykłady płaskiego torusa,
płaskiej butelki Kleina i okrągłej sfery odróżniają krzywiznę lokalną
od wpływu topologii na transport. Nowy rysunek dwóch dróg pokazuje
operator `P_β^{-1}P_α`; istniejący rysunek małej pętli służy dalej
do powiązania holonomii z krzywizną.

Druga sekcja dowodzi zasady odpowiedniości między polami równoległymi
a niezmiennikami pełnej holonomii. Z niezmienniczej podprzestrzeni
wyprowadza gładkie rozkłady równoległe i, przez lokalne twierdzenie
Frobeniusa oraz zgodność koneksji z metryką, pełny rachunek lokalnej
metryki iloczynowej. Uzasadniono całkowitą geodezyjność i zupełność
liści. Globalne sklejenie liści oraz jednoznaczność rozkładu podano
jako jawne wejście zewnętrzne de Rhama z założeniami zupełności
i jednospójności oraz źródłami de Rhama i Wu. Ambrose–Singer także
jest oznaczony jako wynik zewnętrzny; nie przypisano dowodowi
lokalnemu siły dowodu twierdzenia globalnego. Przykłady `S²×R`,
torusa, butelki i otwartego dysku sprawdzają zakres hipotez.
Drugi nowy rysunek przedstawia lokalną siatkę liści. Odesłanie
do Hodge'a–Bochnera wyjaśnia związek z pierwszą liczbą Bettiego
bez ponownego wprowadzania kohomologii de Rhama z tomu I.

### Kontrola składu

Tom II złożono z pliku głównego `geometria_tom2.tex` przy użyciu `latexmk`;
gotowy PDF ma 177 stron. Obejrzano rysunki 14.3 i 14.4 na stronach
drukowanych 60 i 63, poprawiono położenie etykiet i złożono tom ponownie.
Następnie `buduj_tomy.ps1` ustabilizował odsyłacze i zaktualizował
wszystkie trzy PDF-y: tomy mają odpowiednio 208, 177 i 146 stron.
W końcowych logach brak błędów, nierozwiązanych odsyłaczy i przepełnień
wierszy. Indeksy przyjęły odpowiednio 112, 93 i 111 wpisów, bez
odrzuceń ani ostrzeżeń. W każdym PDF są odsyłacze do obu pozostałych
plików tomów, a nowe odnośniki do prac Ambrose'a--Singera, de Rhama
i Wu znajdują się w tomie II.

## 13 października 2026 — miejsce cięcia i promień injektywności w rozdziale 13

Po twierdzeniu Hopfa--Rinowa w `13-geodezyjne.tex` dodano sekcję
o czasie cięcia geodezyjnej, zbiorze cięcia punktu oraz punktowym
i globalnym promieniu injektywności. Udowodniono, że czasy minimalności
tworzą początkowe przedziały, a ich skończone krańce nadal są osiągane.
Pełny dowód równości promienia injektywności z infimum czasów cięcia
i z odległością do zbioru cięcia używa argumentu o narożniku z pierwszej
wariacji oraz twierdzenia z rozdziału 14 o braku punktu sprzężonego
we wnętrzu geodezyjnej minimalnej; tam druga wariacja jest rozpisana.
Osobny dowód alternatywy w miejscu cięcia rozróżnia drugi minimalny
promień i osobliwość różniczki odwzorowania wykładniczego.

Na sferze promień injektywności wynosi `πR`, a zbiorem cięcia
jest antypoda, do której prowadzą różne półokręgi. Dla płaskiego
torusa `R²/(aZ×bZ)` z metryką ilorazową dowiedziono wzoru na odległość
przez podniesienie dróg, wyznaczono prostokątną komórkę najbliższych
reprezentantów i otrzymano promień `min(a,b)/2`. Jej brzeg daje dwa
okręgi zbioru cięcia; na zwykłym boku są dwie drogi minimalne,
w obrazie narożników cztery, a punktów sprzężonych nie ma.
Dwa nowe rysunki pokazują zapadanie brzegu dysku stycznego sfery
do antypody i sklejenie boków komórki płaskiego torusa.

### Kontrola składu

Tom II złożono przez `latexmk` z pliku głównego; ma 180 stron.
Obejrzano strony 44 i 45 z nowymi rysunkami 13.7 i 13.8;
punkty, promienie i etykiety są czytelne oraz odpowiadają
tekstowi. Następnie `buduj_tomy.ps1` złożył trzy tomy,
ustabilizował odsyłacze i skopiował PDF-y. Tomy mają
odpowiednio 208, 180 i 146 stron. W końcowych logach
nie ma błędów, nierozwiązanych odsyłaczy ani przepełnień
wierszy. Indeksy przyjęły 112, 96 i 111 wpisów,
bez odrzuceń i ostrzeżeń. Każdy PDF zawiera odsyłacze
do dwóch pozostałych tomów.

## 13 października 2026 — audyt nowych wiązek w rozdziale 1

Po wypchnięciu etapu rozdziału 13 sprawdzono, czy rozdział 1 ma
niezintegrowane zmiany lokalne lub na pobranych gałęziach: nie ma.
W aktualnej gałęzi są jednak wcześniejsze dodatki do wiązek
wektorowych i kostycznych, których pełny audyt figurował
w `PLAN_DZIALANIA.md` jako oczekujący. Sprawdzono definicje
wiązki i izomorfizmu, przestrzeń całkowitą wstęgi Möbiusa,
jej funkcje przejścia i nietrywialność, wiązkę tautologiczną
nad `RP¹`, jawny izomorfizm między nimi, konstrukcje
wiązek stycznej i kostycznej, diagramy oraz odsyłacze.

Rachunek transformacji kowektorów i wzór na przejście atlasu
`T*M` są poprawne. Usunięto zbędny drugi zapis różniczki
bez argumentu punktowego. W motywacji ogólnej wiązki
poprawiono lokalny model na `U×R^k` dla rzędu `k`,
a powtórzoną definicję trywializacji zastąpiono odsyłaczem.
W dowodzie nietrywialności wstęgi niezerową sekcję
wiązki trywialnej oznaczono `s_1`, żeby nie mylić jej
z wcześniej zdefiniowaną sekcją zerową `s_0`.
Dopuszczono też długość `2π` otwartego przedziału
reprezentantów łuku `S¹\{[0]}`; taki łuk był używany
w późniejszej trywializacji. Poprawiono dwie literówki.

Dopisano dowód zgodności lokalnych map wstęgi Möbiusa
z topologią ilorazową, jej własności Hausdorffa oraz
drugiego aksjomatu przeliczalności. Przy wiązce
tautologicznej pokazano, że przestrzeń całkowita
jest gładką podrozmaitością produktu, a lokalne
trywializacje są gładkie. Doprecyzowano, że izomorfizm
obu wiązek utożsamia ich różne bazy przez dyfeomorfizm `F`.
Obliczenia przejść znakowych, ich związek z obrotem
o pół kąta oraz dowód nietrywialności pozostały poprawne.

### Kontrola składu

Tom I złożono z pliku głównego `geometria_tom1.tex`; ma 209 stron.
Obejrzano strony PDF 42–46 oraz 52 z transformacją kowektorów,
diagramami wiązek, wstęgą Möbiusa, początkiem opisu wiązki
tautologicznej i wiązką kostyczną; podpisy oraz etykiety są czytelne.
Następnie `buduj_tomy.ps1` złożył wszystkie tomy i indeksy. Tomy
mają 209, 180 i 146 stron, a indeksy przyjęły 112, 96 i 111 wpisów
bez odrzuceń i ostrzeżeń. Końcowe logi nie zawierają błędów,
nierozwiązanych odsyłaczy ani przepełnień wierszy. Każdy PDF
zawiera odsyłacze do dwóch pozostałych tomów.

## 13 października 2026 — powiązanie miejsc cięcia z polami Jacobiego

Na końcu Sekcji 14.9 dopisano odsyłacz do Sekcji 13.6.
Wyjaśniono, że przed czasem cięcia odcinek geodezyjnej
da się przedłużyć do odcinka minimalnego, więc nie może
tam leżeć punkt sprzężony i różniczka odwzorowania
wykładniczego jest odwracalna. W miejscu cięcia może
wystąpić sprzężenie wzdłuż danego promienia lub kilka
geodezyjnych minimalnych, także jednocześnie. Wskazano
związek kresu dolnego czasów cięcia z promieniem
injektywności i porównano antypodę sfery z płaskim torusem.

### Kontrola składu

Tom II złożono z pliku głównego `geometria_tom2.tex`:
180 stron, bez błędów i nierozwiązanych odsyłaczy.
Obejrzano stronę PDF 74 z akapitem oraz rysunkiem
walca; tekst, odsyłacze i etykiety są czytelne.
`buduj_tomy.ps1` złożył trzy tomy i ustabilizował
odsyłacze między nimi. PDF-y mają 209, 180 i 146 stron,
a indeksy przyjęły 112, 96 i 111 wpisów bez odrzuceń
i ostrzeżeń. W końcowych logach nie ma błędów,
nierozwiązanych odsyłaczy ani przepełnień wierszy;
każdy PDF zawiera odsyłacze do dwóch pozostałych tomów.

## 13 października 2026 — porządek w planie dalszej pracy

W `PLAN_DZIALANIA.md` usunięto historyczny opis scalania i ukończonych
próśb z bieżącej kolejki. Poprawiono nieaktualne wskazanie rozdziału 26
jako następnego do audytu, oczekujący rzekomo audyt wiązek w rozdziale 1
oraz instrukcję aktualizowania zbiorczego PDF przy każdej iteracji.
Kolejka wskazuje teraz rozdział 29 jako najbliższy niezweryfikowany.

Na życzenie autora dopisano osobny zakres przyszłej rozbudowy
twierdzenia Walla, sfer Milnora i twierdzeń wymiaru cztery.
Wskazano brakujące kroki względem obecnych dowodów i granicę
między własnym wyprowadzeniem a nazwanym wynikiem zewnętrznym.
Propozycję równań Gaussa–Codazziego usunięto z planu:
autor poprosił o jej objaśnienie wyłącznie w rozmowie.
Poprawiono też dwa drobne nieaktualne lub urwane zdania.
Zmiana dotyczy wyłącznie plików Markdown; źródeł TeX i PDF nie zmieniono.
Kontrolny `buduj_tomy.ps1` zakończył się powodzeniem; logi tomów
nie zawierają błędów, nierozwiązanych odsyłaczy ani przepełnień,
a indeksy przyjęły 112, 96 i 111 wpisów bez odrzuceń i ostrzeżeń.

## 13 października 2026 — pierwszy etap rozbudowy twierdzenia Walla w rozdziale 27

Porównano opis dekoracji przeszkody z §17D książki Walla
*Surgery on Compact Manifolds* oraz rachunek formacji z §9
*An Introduction to Algebraic Surgery* Ranickiego. W
`23-przeszkoda-chirurgiczna.tex` rozpisano sprzężoną zmianę bazy
w dwóch parach hiperbolicznych nad pierścieniem grupowym:
`e'_1=e_1+a e_2` wymusza `f'_2=f_2-\bar a f_1`.
Sprawdzono parowania, udoskonalenie kwadratowe i zerową
torsję Whiteheada obu elementarnych zmian bazy. W ten sposób
geometryczny opis przesunięcia uchwytu uzyskał jawny rachunek
nad `Z[π]`, którego wcześniej brakowało.

Wyjaśniono warunki prostej dualności i prostego lagranżjanu
w dekoracji `s`, zestawiając je ze zwykłą odwracalnością w
dekoracji `h`. Jednostka `u=1-t-t^{-1}` w `Z[C_5]`, której
niezerową klasę Whiteheada udowodniono już w rozdziale 25,
daje konkretną formę o odwracalnej dualności z torsją `2[u]≠0`.
Po zmianie bazy przez `u^{-1}` forma jest hiperboliczna w
opisie `h`; wybrana baza nie spełnia warunku prostej dualności
wersji `s`. Jest to przykład algebraiczny, bez twierdzenia o
realizacji przez zadaną mapę normalną. Doprecyzowano też
hipotezę relatywną na brzegu w obu dekoracjach.

To etap rozbudowy rozdziału 27, a nie dowód pełnego twierdzenia
Walla dla dowolnej grupy podstawowej. Geometryczna realizacja
obramowanych immersji, przygotowanie kobordyzmu i stabilna
relacja formacji nadal używają wskazanych w tekście lematów
Walla i Milnora.

### Kontrola składu

Tom III złożono z `geometria_tom3.tex` przez `latexmk`; nowe
akapity są na stronach PDF 51–53 (numery drukowane 50–52).
Sprawdzono wizualnie te strony: wzory, podpisy i odsyłacze są
czytelne. Następnie `buduj_tomy.ps1` złożył trzy tomy,
ustabilizował odsyłacze i skopiował PDF-y. Mają odpowiednio
209, 180 i 147 stron. Końcowe logi nie zawierają błędów,
brakujących odsyłaczy ani przepełnień wierszy. Indeksy
przyjęły 112, 96 i 111 wpisów bez odrzuceń i ostrzeżeń;
każdy PDF zawiera odsyłacze do obu pozostałych tomów.
W trakcie pracy pojawiły się niezależne lokalne zmiany źródła
rozdziału 1 i PDF tomu I. Pierwszy pełny skład użył ich
aktualnej wersji. PDF-y do tego etapu złożono ponownie
w osobnym katalogu z wersji rozdziału 1 zapisanej w gałęzi
i nowego źródła rozdziału 27. Powtórzony pełny skład również
przeszedł kontrole logów, indeksów i łączy. Niezależne
lokalne zmiany rozdziału 1 nie należą do tego etapu.

## 14 października 2026 — przegląd §1.10 rozdziału 1

Sprawdzono rozbudowany opis funkcji przejścia i szczegółowy dowód
sklejania wiązki. Relacja na sumie rozłącznej jest równoważnością
dzięki warunkowi kocyklu; lokalne trywializacje są dobrze określone,
zgodne na przecięciach i wyznaczają topologię oraz gładki atlas.
Dowód obejmuje ciągłość rzutowania, oddzielanie punktów i drugi
aksjomat przeliczalności, więc uzasadnia wszystkie warunki z definicji
rozmaitości. Sprawdzono także wzory zgodności lokalnych zapisów sekcji,
macierze przejścia dla sumy i wiązki dualnej oraz argument o zerze
każdej ciągłej sekcji wstęgi Möbiusa.
Konwencję funkcji przejścia i konstrukcję z kocyklu porównano
z [notatkami T. S. Mrowki, 18.965, §7](https://math.mit.edu/~mrowka/math965lectnote.pdf#page=12).

Zastąpiono ręczny, niezgodny z numeracją sekcyjną znacznik `(1.1)`
etykietowanym równaniem i odsyłaczami. Doprecyzowano, że macierze
grupy strukturalnej pochodzą z gładkich ram lokalnych, a przykład
ortogonalny wymaga gładkiego iloczynu skalarnego we włóknach.
W warunku gładkości sekcji Möbiusa dodano gładkość funkcji na całym
domkniętym przedziale, obok zgodności jej pochodnych na końcach.
W dowodzie sklejania wniosek o strukturze rozmaitości przeniesiono
za weryfikację aksjomatów topologicznych. Etykiety wektorów na
rysunku przesunięto od obrysów włókien.

### Kontrola składu

Tom I złożono osobno przez `latexmk`, po czym `buduj_tomy.ps1`
złożył wszystkie trzy tomy, ustabilizował odsyłacze między nimi
i skopiował PDF-y. Mają odpowiednio 211, 180 i 147 stron.
Obejrzano strony PDF 52–57 tomu I: wzory, rysunek 1.15,
etykiety wektorów i przykład wstęgi Möbiusa są czytelne.
Końcowe logi nie zawierają błędów, brakujących odsyłaczy ani
przepełnień wierszy. Indeksy przyjęły 112, 96 i 111 wpisów
bez odrzuceń i ostrzeżeń; w każdym PDF są łącza do dwóch
pozostałych tomów. W każdym logu pozostaje ostrzeżenie pdfTeX
o zdublowanym celu `page.1` przy składzie części wstępnej.
## 14 października 2026 — rozpoczęcie pełnych dowodów Walla i Bardena

Autor wyznaczył szerszy etap dla wymiarów co najmniej pięć: celem jest
pełne wyprowadzenie twierdzenia o przeszkodzie chirurgicznej Walla i
klasyfikacji Bardena. Wymiary cztery mają pozostać wykładem informacyjnym.
Zakres i kolejkę zapisano wyłącznie w `PLAN_DZIALANIA.md`.

Pierwsza iteracja w rozdziale 29 dotyczy twierdzenia 2.2 Bardena.
Porównano tekst z [oryginalną pracą Bardena](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/barden.pdf),
zwłaszcza §§3–5. Dodano pełny dowód algebraicznego lematu 4.2:
epimorfizm skończenie generowanych grup abelowych rozdziela jeden
cykliczny czynnik po znalezieniu prymitywnego elementu jądra.
Wypisano dokładny ciąg pary $(V,\partial V)$ i warunek, który musi
spełniać końcowy kobordyzm, aby zrealizować *zadany* izomorfizm
$H_2(P)\to H_2(Q)$. Przykład z $\Z^2\to\Z/2$ ilustruje zmianę bazy.

Lematy geometryczne 3.1, 4.1, 4.3 i 4.4 oraz indukcja z §5 nadal są
zewnętrznymi częściami dowodu; tej iteracji nie oznaczono jako
ukończonego twierdzenia Bardena. Dotychczasowy dowód Walla również
pozostaje niepełny dla dowolnej grupy podstawowej i wymiaru nieparzystego.

### Kontrola składu

Po korekcie kierunku relacji $x-\varphi(x)\in\ker i$ uruchomiono
`buduj_tomy.ps1`. Wszystkie trzy tomy złożyły się, odsyłacze między
tomami ustabilizowały się, a indeksy przyjęły odpowiednio 112, 96
i 111 haseł bez odrzuceń. Sprawdzono tekst wynikowy i wygląd strony 71
tomu III z nowym lematem. Logi nie wskazują brakujących odsyłaczy ani
błędów składu; w tomie I pozostają wcześniejsze ostrzeżenia o zmianie
położenia trzech obiektów pływających. Zaktualizowano PDF-y tomów.

## 14 października 2026 — pełne twierdzenia 2.2 i 2.3 Bardena

Po uwadze autora, że potrzebne jest całe twierdzenie Bardena, rozbudowano
rozdział 29 o oba główne wyniki z [oryginalnej pracy](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/barden.pdf).
Twierdzenie 2.2 realizuje **zadany** izomorfizm $H_2$ zachowujący formę
wiązania i $w_2$; twierdzenie 2.3 podaje kanoniczną listę
$X_j\#M_{k_1}\#\cdots\#M_{k_s}$ i pełność pary $(H_2,\iota)$.

Dowód 2.2 rozpisuje: warunek kobordyzmu z formy wiązania i liczby
$w_2w_3$; chirurgię upraszczającą $\pi_1$ i $H_2$; lematy 4.1–4.4
o reprezentowaniu klas $H_3$, rozdzieleniu generatora, kontrolowanym
powiększaniu $H_2$ i usunięciu względnego $H_3$; następnie indukcję
zachowującą podgrupę różnic $a-\varphi(a)$ i przejście przez
sześciowymiarowy $h$-kobordyzm. W lemacie 4.3 relację meridianu
wyprowadzono z obciętego łańcucha względnego; w lemacie 4.4 użyto
standardowego plumbing dwóch $3$-sfer zamiast zakładać wcześniej
wniosek Poincarégo w wymiarze pięć.

Dowód 2.3 buduje modele przez sklejenie wiązek dysków nad $S^2$,
podaje macierze działań na brzegach i oblicza $H_2$ oraz $w_2$.
Formy wiązania wyznaczono osobno z lematu F Walla–Bardena i
klasyfikacji form z lematu E, nie z samego ciągu Mayera–Vietorisa.
Normalizacja algebraiczna uwzględnia samotny składnik $\Z/2$,
niealternujące pary, mieszany przypadek rzędów $q,2q$, wartości $w_2$
na części wolnej i jednoznaczność czynników niezmienniczych.
Przykłady $M_2/X_1$ i $M_\infty/X_\infty$ pokazują rolę $w_2$.

Jawne wyniki wejściowe obejmują obliczenia grup kobordyzmu Thoma
i Nowikowa, normalną postać Walla, twierdzenia Whiteheada i Haefligera
o reprezentowaniu klas przez sfery, obramowany trik Whitneya Milnora,
realizację automorfizmów brzegów przez Walla z 1964 roku oraz twierdzenie
Smale'a o $h$-kobordyzmie. Ich założeń nie ukryto pod nazwą własnego
dowodu. Niezależny przegląd kroków 2.2–2.3 wykrył i pozwolił poprawić
dwa błędy zmiany bazy: jednoczesne wartości $w_2$ na torsji i części
wolnej oraz utratę ortogonalności przy samotnym generatorze $\Z/2$.
Ponowna kontrola modeli doprecyzowała istnienie sklejenia $X_{-1}$:
identyczność i sprzężenie zespolone na składnikach brzegu składa się
przez lemat 2 Walla. W dowodzie 2.3 rozszczepienie mieszanej pary
rzędów $q,2q$ zapisano przed użyciem bazy z samotnym generatorem $\Z/2$.

Osobno sprawdzono zmiany autora w rozdziale 1. Rozwinięty rachunek
macierzy Jacobiego poprawnie odczytuje współczynniki różniczki przez
działanie na funkcje współrzędnych. W przykładzie niewymiernej prostej
na torusie rachunek różniczki dowodzi immersji, argument z zasadą
szufladkową wytwarza ciąg $q_N\to\infty$ z $\gamma(q_N)\to\gamma(0)$,
a wielokrotności małego przesunięcia dowodzą gęstości obrazu.
Poprawiono przy tym dwa redundantne zwroty „zanurzenie włożone” oraz
„injektywną immersję $d\iota_p$” na „injektywną różniczkę $d\iota_p$”.
Definicje immersji, submersji i zanurzenia zachowują dotychczasowe
znaczenie. W nowym tekście Bardena ujednolicono „osadzone” sfery
i okręgi z projektowym terminem „zanurzone”, bez dodatkowego
odsyłacza do rozdziału 1.

Po poprawkach uruchomiono `buduj_tomy.ps1`: trzy tomy złożyły się
w dwóch przebiegach, bez błędów, przepełnionych wierszy i brakujących
odsyłaczy. Indeksy przyjęły odpowiednio 112, 96 i 111 wpisów,
bez odrzuceń. PDF-y trzech tomów zaktualizowano. Obejrzano strony
57–61 tomu I z nowym przykładem torusa i strony 72–79 tomu III
z dowodami i modelami Bardena; oznaczenia, wzory oraz łamanie stron
są czytelne. Odsyłacze między tomami zostały ustabilizowane
w drugim przebiegu.

## 14 października 2026 — rozszerzenie twierdzenia Walla na $n\geq5$

Porównano rozdziały 27–28 z
[oryginałem Walla](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
zwłaszcza twierdzeniami 5.6, 6.4, 5.8, 6.5 oraz 10.4, 10.5 i 10.8.
Twierdzenie o przeszkodzie dla parzystych $n=2k\geq6$ rozpisano
nad $\Lambda=\Z[\pi]$: preferowana baza jądra, prosta dualność,
stabilizacja formy, dwa ciągi dokładne jednej chirurgii, zanik
torsji Whiteheada przy usunięciu pary oraz lagranżjan na brzegu
przygotowanego kobordyzmu. Wersję nieparzystą $n=2k+1\geq5$
opisano przez $SU/RU$: zdefiniowano podgrupy $TU,UU$, macierz
dwóch lagranżjanów, ruchy $T1$--$T4$, ich realizację geometryczną,
kryterium zerowej klasy i naturalność. Osobno wyjaśniono, czemu
wymiar pięć mieści się w twierdzeniu 6.4, choć twierdzenie
realizacyjne 6.5 zaczyna się od wymiaru siedem.

W rozdziale 28 próg zmieniono na $n\geq5$: przy $n=5$ działanie
$L_6^s$ używa parzystego twierdzenia 5.8 Walla, a gładki
$s$-kobordyzm dotyczy wtedy śladu wymiaru sześć. Rozdzielono
geometryczne twierdzenia realizacyjne od kryterium zaniku
przeszkody. Wersję z dekoracją $h$ pozostawiono osobnym wynikiem
zewnętrznym, ponieważ uwagi §17D Walla o porównaniu dekoracji
nie są pełnym dowodem tej wersji.

Dowód przedstawiony w tekście jest szczegółowym wyprowadzeniem
z jasno wskazanych twierdzeń geometrycznych Walla: 1.2, 1.4,
2.3–2.6, 5.1–5.2, 5.5, 5.7 i 6.1–6.3. Nie wyprowadzono ich
wszystkich od podstaw; dlatego nie oznaczono rozdziału jako
samodzielnie pełnego dowodu. Algebraiczne utożsamienie opisu
przez formacje z $SU/RU$ wskazano osobno za Ranickim.

Niezależny audyt nowego tekstu względem §§5–6 i 10 Walla
potwierdził hipotezy twierdzeń 5.6 i 6.4, zakres $n=5$,
macierze ruchów $T3$–$T4$ oraz rachunek baz i torsji.
Poprawiono dwa znalezione skróty: prosta zmiana bazy
rozkłada się po stabilizacji na macierze elementarne,
jednostki $\pm g$ i permutacje, a źródłem bijekcji
$\mathcal N_{\mathrm{DIFF}}(X)\cong[X,G/O]$ są łącznie
stwierdzenia 10.1–10.2 i lemat 10.6 Walla.

Po tych korektach `buduj_tomy.ps1` złożył wszystkie trzy tomy
w dwóch przebiegach. Logi nie wykazały błędów, przepełnionych
wierszy ani brakujących odsyłaczy. Indeksy przyjęły 112, 96
i 111 wpisów, bez odrzuceń. PDF-y tomów zaktualizowano;
obejrzano wybrane strony 55–69 i 71–73 tomu III, w tym macierze,
ruchy $T1$–$T4$, uwagę o wymiarze pięć oraz rysunek ciągu
chirurgii. Łamanie wzorów i oznaczenia są czytelne.

## 15 października 2026 — derywacje globalne i punktowe w rozdziale 2

Przeredagowano początek §2.1, aby zachować kolejność konstrukcji:
pole $X$ daje operator $D_X(f)(p)=X_p(f)$ o wartościach funkcyjnych,
a ewaluacja dowolnej derywacji globalnej $D$ w punkcie $p$ daje
derywację punktową $v_p(f)=D(f)(p)$, czyli wektor styczny.
Rozdzielono funkcje $X^i$ od liczb $X^i(p)$ i dodano przykład
$D=x^2\,\dd/\dd x$. Uporządkowano też dowód identyfikacji
derywacji globalnych z polami, rozpoczynając od kierunku $X\mapsto D_X$.
Po pytaniu autora dopisano przy definicji pola, że $X_p:=X(p)$ jest
wektorem stycznym w $p$, a $X_p(f)$ jego działaniem na funkcję.
W przykładzie okręgu rozwinięto następnie rachunek zmiany bazy:
reguła łańcuchowa dla $F\circ\varphi^{-1}$ daje
$(\dd\varphi^{-1})_t(\partial_t|_t)
=-r\sin t\,\partial_u|_p+r\cos t\,\partial_v|_p=X_p$.
Wyjaśniono, że zapis parą współczynników ukrywa bazę otaczającej
$\R^2$, a samo $\partial_u|_p$ na ogół nie jest styczne do okręgu.
Po tej zmianie uruchomiono `buduj_tomy.ps1`: trzy tomy i indeksy
złożyły się poprawnie w dwóch przebiegach, a PDF-y tomów
zaktualizowano. Sprawdzono tekst przykładu na stronach 60--61
tomu I; krótki akapit o $\partial_u|_p$ pozostaje w całości
na jednej stronie. Log nie wykazał nowych ostrzeżeń w rozdziale 2.
Uzasadnieniem jest wcześniejsza niejasność typów wyników i kolejności
użycia oznaczeń $D_X$, $D$ oraz $v_p$.

Tom I złożono przez `latexmk` po dodaniu Perla z PortableGit do `PATH`.
Skład zakończył się bez błędów; tekst nowej sekcji sprawdzono w PDF.
W logu pozostały wcześniejsze ostrzeżenia o pudełkach w rozdziale 1,
bez nowych ostrzeżeń dotyczących rozdziału 2.
Po dopisaniu objaśnienia $X_p$ uruchomiono pełny `buduj_tomy.ps1`:
wszystkie trzy tomy przeszły dwa przebiegi, indeksy sprawdzono,
a PDF-y tomów skopiowano do katalogu głównego. W logach nie ma
błędów ani nierozwiązanych odsyłaczy. Nadal występuje wcześniejsze
ostrzeżenie `Overfull \hbox` przy długim wzorze w rozdziale 1,
wiersze 5617--5618; nie dotyczy ono zmiany w rozdziale 2.
Na prośbę autora złożono też dokument zbiorczy przez `latexmk`:
547 stron, indeks 319 wpisów przyjętych i 0 odrzuconych.
Nie było błędów ani brakujących odsyłaczy; PDF zbiorczy skopiowano
z `build/sklad` do katalogu głównego. Pozostały ostrzeżenia
o łamaniu wierszy, w tym wymieniony `Overfull \hbox` z rozdziału 1.

## 16 października 2026 — reguła łańcucha w przykładzie okręgu

W przykładzie 2.1.3 zastąpiono określenie „reguła łańcuchowa” przez
„reguła łańcucha”. Rachunek pokazuje teraz jawnie, że obraz
$\partial_t|_t$ przez różniczkę $\varphi^{-1}$ działa na ograniczenie
$F|_{S_r^1}$ jako pochodna $(F\circ\varphi^{-1})'(t)$. Dopiero z tej
równości działań na funkcje wynika zapis wektora w bazie otaczającej
$\R^2$. Dopisano, że funkcje gładkie na okręgu mają lokalne przedłużenia,
więc porównanie działań wystarcza do równości wektorów stycznych.
Tom I złożono przez `latexmk` i sprawdzono tekst przykładu w PDF.
Następnie `buduj_tomy.ps1` złożył wszystkie trzy tomy w dwóch przebiegach,
sprawdził indeksy i zaktualizował PDF-y. W logu tomu I nie ma błędów
ani nowych ostrzeżeń dotyczących rozdziału 2; pozostały wcześniejsze
ostrzeżenia o łamaniu wierszy w rozdziale 1.

Po uwadze autora dopisano w przykładzie 2.1.3 zastosowanie
$(\dd\varphi)_p$ do równości
$X_p=(\dd\varphi^{-1})_t(\partial_t|_t)$.
Ponieważ różniczki mapy i jej odwrotności składają się do identyczności,
otrzymujemy $(\dd\varphi)_p(X_p)=\partial_t|_t$, a więc współczynnik
pola w mapie kątowej wynosi $X^1(t)=1$.
Ponowny `buduj_tomy.ps1` złożył trzy tomy, sprawdził indeksy i zaktualizował
PDF-y. W tomie I wzór mieści się w przykładzie bez nowych ostrzeżeń składu.

## 16 października 2026 — zmiana mapy dla całego pola

Po prośbie autora dodano przy lokalnym zapisie pola w rozdziale 2 uwagę
o transformacji współczynników $X_\psi^j(p)=\sum_i
(\partial y^j/\partial x^i)(p)X_\varphi^i(p)$ na przecięciu map.
Wynika ona z reguły transformacji bazy wektorów stycznych z rozdziału 1.
Podano także równoważny wzór dla reprezentantów całego pola w obrazach
map, $\widehat X_\psi(G(u))=DG(u)\widehat X_\varphi(u)$, oraz przykład
zmiany współrzędnej $y=2x$.
Pełny `buduj_tomy.ps1` zakończył się poprawnie w dwóch przebiegach,
sprawdził indeksy i zaktualizował PDF-y tomów. Uwaga jest czytelna w tomie I;
nie pojawiły się nowe ostrzeżenia składu w rozdziale 2.
## 16 października 2026 — skrócenie intuicji pochodnej w kierunku pola

W rozdziale 2 zastąpiono cztery powtarzające się podpunkty między opisem
pola a sekcją o nawiasie Liego jednym akapitem. Przykład wiatru i temperatury
łączy teraz znaczenie $X(f)(p)$ z pochodną $f$ wzdłuż krzywej o wektorze
początkowym $X_p$. Zachowano wcześniejsze definicje i etykiety. Tom I
złożono przez `latexmk`; tekst i przejście do nawiasu Liego sprawdzono
w PDF. Pełny `buduj_tomy.ps1` zakończył się po dwóch przebiegach:
odsyłacze między tomami ustabilizowały się, indeksy miały zero odrzuconych
wpisów, a PDF-y tomów zaktualizowano. W tomie I nie ma ostrzeżeń o
brakujących odsyłaczach ani nowych ostrzeżeń w rozdziale 2; pozostały
wcześniejsze ostrzeżenia o łamaniu w rozdziale 1.

## 18 października 2026 — ponowny przegląd całej sekcji o polach i derywacjach

Na prośbę autora ponownie przejrzano całe §2.1 rozdziału 2.
Ułożono podstawowy ciąg pojęć: gładka sekcja $TM$, współczynniki
w mapie i ich transformacja, derywacja globalna, ewaluacja w punkcie
oraz twierdzenie o wzajemnej odpowiedniości pól i derywacji.
Intuicję pochodnej w kierunku pola skrócono i umieszczono przed
definicją derywacji globalnej. Wyjaśniono, że $D_X(f)$ jest funkcją,
natomiast $X_p(f)$ liczbą, oraz że $D$ jest liniowa nad $\R$,
ale zwykle nie nad $C^\infty(M)$ jako operator na funkcjach.

Rozpisano dowód gładkości pola otrzymanego z derywacji $D$:
lokalne współrzędne przedłużono przez funkcję odcinającą,
wyznaczono współczynniki $D(\widetilde x^i)$, sprawdzono ich
gładkość i oba złożenia wzajemnie odwrotnych konstrukcji.
W przykładzie okręgu jawnie wprowadzono inkluzję do $\R^2$,
aby równość w $T_pS_r^1$ odróżnić od zapisu obrazu wektora
w $T_p\R^2$. Radialne przedłużenie funkcji z okręgu uzasadnia
porównywanie działań wektorów na wszystkich funkcjach gładkich.
W uwadze o polu wzdłuż odwzorowania podano lokalny wzór na
współczynniki i przykłady $F(t)=t^2$ oraz $F(t)=t^3$:
zgodność na włóknach jest warunkiem koniecznym, lecz sama nie
gwarantuje gładkiego pola na przeciwdziedzinie.

Podczas kontroli PDF zauważono, że stary blok `minipage` przy rachunku
na okręgu składał tekst poza prawym marginesem; usunięto go i ponownie
obejrzano strony 61–63 tomu I. Rachunki oraz etykiety są czytelne.
`buduj_tomy.ps1` złożył trzy tomy w dwóch przebiegach i zaktualizował
ich PDF-y. Logi nie wykazały błędów ani nierozwiązanych odsyłaczy;
w tomie I nie ma nowych ostrzeżeń dla rozdziału 2. Indeksy przyjęły
odpowiednio 112, 96 i 111 wpisów, wszystkie bez odrzuceń.
Sprawdzono również obecność docelowych nazw pozostałych tomów
w odsyłaczach PDF. Pliku zbiorczego nie składano; jego istniejąca
lokalna modyfikacja została zachowana poza zakresem tej iteracji.

## 18 października 2026 — intuicja podrozmaitości przy definicji

W §1.12 przeniesiono treść końcowego akapitu „Intuicja: rozmaitość
a podrozmaitość” bezpośrednio pod nagłówek sekcji i skrócono ją.
Wyjaśnienie rozróżnia wewnętrzny opis rozmaitości od oglądania
$S\subseteq M$ w przestrzeni otaczającej; przykład okręgu łączy
tę intuicję z wymiarami $1$ i $2$, a ostatnie zdanie prowadzi wprost
do warunku mapy plasterkowej. Usunięto osobny nagłówek i powtórzenia
na końcu sekcji. Definicja oraz twierdzenia pozostały bez zmian.

Pełny `buduj_tomy.ps1` zakończył się po dwóch przebiegach, zaktualizował
PDF-y trzech tomów i sprawdził indeksy bez odrzuconych wpisów.
Na stronie 55 tomu I skontrolowano nowe przejście od akapitu do definicji
i rysunku mapy plasterkowej. Logi nie mają brakujących odsyłaczy ani
nowych ostrzeżeń dotyczących §1.12; pozostało wcześniejsze ostrzeżenie
o szerokim wzorze w rozdziale 1, wiersze 5616–5619, poza zmienioną sekcją.

## 18 października 2026 — skąd bierze się wzór na różniczkę funkcji

Na prośbę autora zachowano istniejące stwierdzenie i jego dowód
w §1.8 „Przestrzeń kostyczna”. W §1.11, zaraz po definicji różniczki
odwzorowania $F\colon M\to N$, dodano twierdzenie wyjaśniające,
dlaczego dla $f\colon M\to\R$ otrzymujemy znany wzór
$df_p=\sum_i(\partial f/\partial x^i)(p)\,dx^i_p$.
Dowód najpierw utożsamia $T_{f(p)}\R$ z $\R$ przez działanie
wektora na standardową współrzędną $t$, potem oblicza wartość
$df_p(v)=v(f)$ na wektorze zapisanym we współrzędnych i korzysta
z dualności $dx^i_p$ do $\partial_{x^i}|_p$. Dodano przykład
$f(u,v)=u^2+uv$, w którym wzór daje konkretną wartość na wektorze.

Pełny `buduj_tomy.ps1` zakończył się poprawnie po dwóch przebiegach.
Sprawdzono stronę 48 tomu I z nowym twierdzeniem, dowodem i przykładem;
wzory mieszczą się w marginesach. Logi nie mają nierozwiązanych
odsyłaczy ani nowych ostrzeżeń przy §1.11. Indeksy tomów przyjęły
112, 96 i 111 wpisów, bez odrzuceń. W PDF-ach znajdują się nazwy
docelowych pozostałych tomów dla odsyłaczy między tomami.
Zaktualizowano PDF-y tomów; lokalnie zmienionego PDF-u zbiorczego
nie włączono do tej iteracji.

## 18 października 2026 — dlaczego w dowodzie wystarcza funkcja $t$

Na pytanie autora doprecyzowano dowód Twierdzenia~1.11.3.
Każdy $w\in T_{f(p)}\R$ ma postać $a\partial_t|_{f(p)}$,
więc dla dowolnej gładkiej $g$ zachodzi
$w(g)=a g'(f(p))$, podczas gdy $w(t)=a$.
Stąd wartość na standardowej współrzędnej $t$ wyznacza działanie
na wszystkich funkcjach $g$. Dopiero po tym wyjaśnieniu użyto
$(df_pv)(t)=v(f)$ i zapisano wynik dla dowolnego $g$.
To usuwa możliwe wrażenie, że definicję różniczki ograniczono
do jednej funkcji testowej.

`buduj_tomy.ps1` złożył trzy tomy w dwóch przebiegach i sprawdził
indeksy bez odrzuconych wpisów. Stronę 48 tomu I obejrzano po składzie:
dopisany krok jest czytelny i nie wprowadza przepełnienia.
Logi nie mają nierozwiązanych odsyłaczy; wcześniejsze ostrzeżenie
o szerokim wzorze w innej części rozdziału 1 pozostało bez zmian.
Zastaną lokalną modyfikację PDF-u tomu I zabezpieczono przed składem;
sprawdzoną wersję dołączono do commitu, a lokalną wersję zachowano
w katalogu roboczym. PDF zbiorczy pozostał poza zakresem zmiany.

## 19 października 2026 — różniczka, Wall, Barden i Milnor

W rozdziale 1 sprawdzono nowe twierdzenie o współrzędnościowym wzorze
na $dF_p$ oraz wynikający z niego wzór na $df_p$. Działanie różniczki
na współrzędne daje kolumny macierzy Jacobiego, a działanie wektora
z $T_{f(p)}\R$ na standardową współrzędną $t$ uzasadnia jego
utożsamienie z liczbą. Dopisano wyjaśnienie użycia lokalnych funkcji
współrzędnych: przedłużamy je funkcją odcinającą, a lokalność derywacji
zapewnia niezależność wyniku. Sprawdzono zgodność z wcześniejszym
wzorem w §1.8 i terminologią immersji, submersji oraz zanurzenia.
W dowodzie twierdzenia o stałym rzędzie przeniesiono zbyt szeroki
wzór do osobnej linii.

W rozdziale 27 dopisano wersję $h$ przeszkody chirurgicznej i fragment
ciągu Rothenberga porównującego $L^s$ i $L^h$, z osobnymi źródłami
dla geometrycznego kryterium zanikania i dla ciągu. Rozpisano rachunek
lokalnej chirurgii na klasie zerowej: suma spójna z $S^k\times S^k$
dodaje preferowaną płaszczyznę hiperboliczną. Geometryczne
sprowadzenie do modelu lokalnego nadal jest dokładnie wskazanym
lematem 5.5 Walla. Porównanie tekstu z §5 i §17D Walla potwierdziło
zakres tych odwołań; nie ogłaszamy przez to całego dowodu Walla
samodzielnym.

Twierdzenia 2.2 i 2.3 Bardena w rozdziale 29 porównano z oryginałem,
zwłaszcza zakres klasyfikacji, dane $H_2$ i $w_2$, lematy 3.1 i
4.1–4.4 oraz modele kanoniczne. Nie znaleziono poprawki wymagającej
zmiany źródła. Jest to kontrola tych twierdzeń, a nie pełny audyt
pozostałej części rozdziału.

W rozdziale 30 skorygowano opis argumentu Milnora dla $p_1$:
lemat 3 oryginału korzysta z addytywności i wiązki Hopfa, a nie
z rachunku przez $\operatorname{Spin}(4)$. Sygnaturę wypełnienia
określono na racjonalnym obrazie homologicznym. Dodano spinowy
niezmiennik Eellsa--Kuipera
$\mu(M)=[(q(B)-4\operatorname{sign}(B))/896]\in\Q/\Z$,
wyprowadzono niezależność od wypełnienia z wzorów Hirzebrucha
i całkowitości indeksu Diraca oraz obliczono
$\mu(M_k)=(k^2-1)/224$. Wartości dla $k=3,5,7$ rozróżniają
trzy sfery także bez wybranej orientacji. Wskazano dokładnie
głębokie twierdzenia użyte z zewnątrz.

Po ostatniej korekcie oznaczenia $\phi$ uruchomiono pełny
`buduj_tomy.ps1`. Dwa przebiegi dały tomy o 212, 181 i 163
stronach. Indeksy przyjęły odpowiednio 112, 96 i 111 haseł,
bez odrzuceń; logi nie wykazały błędów, przepełnień ani
niewyjaśnionych odsyłaczy. Obejrzano strony 49–51 i 56 tomu I
oraz 55–56, 63, 86 i 91–92 tomu III; ostatnią stronę z lematem
o stabilizacji obejrzano ponownie po końcowym składzie.
W plikach PDF potwierdzono docelowe nazwy pozostałych tomów
dla łączy między tomami. Zastaną lokalną wersję PDF-u tomu I
zachowano w `build/preexisting-2026-10-19/`; lokalnie zmieniony
PDF zbiorczy pozostał poza tym commitem.

## 19 października 2026 — pełny audyt rozdziału o sferach Milnora

Przeczytano cały rozdział 30, porównując hipotezy i wzory z pracami
Milnora oraz Eellsa--Kuipera sprawdzonymi w poprzednim etapie.
Skontrolowano klasy sklejania $E_{h,j}$, stopień odwzorowania
$u\mapsto u^{h+j}$, obliczenia $e$ i $p_1$, macierz ciągu
Mayera--Vietorisa, prostą spójność i zastosowanie kryterium
Whiteheada. Rachunki $q(B_k)=4k^2$ i
$\operatorname{sign}(B_k)=1$ dają podane wartości $\lambda$ i $\mu$;
sprawdzono także zmianę znaku obu niezmienników przy odwróceniu
orientacji oraz tabelę dla $k=1,3,5,7$. Nie stwierdzono błędu
w tych wzorach.

Uzupełniono dwa przejścia w dowodach. Przy odwzorowaniu
$M_{h,j}\to S^7$ wskazano wybór orientacji i hipotezę typu CW
potrzebną w kryterium Whiteheada. W dowodzie niezależności
$\lambda$ dualność na brzegu daje
$H_4(M;\Q)=H_3(M;\Q)=0$; dopisano wynikające stąd
rozszczepienie środkowej homologii sklejonego wypełnienia
i ortogonalność form przecięcia. Dzięki temu krok addytywności
sygnatury ma jawne uzasadnienie. Zgodnie z terminologią książki
zastąpiono dwa użycia „mapa” przez „odwzorowanie” i dwa użycia
„fibracja” przez „rozwłóknienie”. Twierdzenie o sygnaturze,
całkowitość indeksu Diraca i wysokowymiarowe twierdzenie
Poincarégo pozostają dokładnie oznaczonymi wynikami zewnętrznymi.

Po poprawkach uruchomiono `buduj_tomy.ps1`: dwa przebiegi złożyły tomy
o 212, 181 i 163 stronach, a indeksy przyjęły odpowiednio 112, 96 i
111 haseł bez odrzuceń. W logach nie ma błędów składu, przepełnień ani
nierozwiązanych odsyłaczy. Obejrzano strony 88, 90 i 91 tomu III,
w tym rysunek 30.1 i dopisane kroki dowodów; skład i etykiety są czytelne.
Sprawdzono także odsyłacze między plikami PDF tomów.

## 19 października 2026 — geometryczny krok lematu 5.5 Walla

Porównano §5, lemat 5.5 oraz §1, twierdzenie 1.1 z
[oryginałem Walla](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf).
Rozdział 27 zawierał rachunek lokalnej chirurgii w dysku, lecz
sprowadzenie do tego modelu dowolnej chirurgii na klasie zerowej
pozostawało cytowanym krokiem geometrycznym. Dopisano osobny lemat:
dopuszczalne obramowane zanurzenie reprezentujące zero w
$\pi_k(\phi)$ ma tę samą klasę regularnej homotopii co model
standardowy na mocy twierdzenia 1.1 Walla. Parametryczne położenie
ogólne zamienia ją w izotopię, ponieważ wymiar potencjalnych
samoprzecięć śladu wynosi $2(k-1)+1-2k=-1$; stabilizacja
$\pi_{k-1}(O(k+1))\to\pi_{k-1}(O)$ kontroluje rzeczywiste
obramowanie. W połączeniu z istniejącym rachunkiem sumy spójnej
otrzymano lemat 5.5 w zakresie używanym w tekście.

Zależność od twierdzenia 1.1, a przez nie od klasyfikacji immersji,
pozostała jawna. Ten etap obejmuje przegląd matematyczny nowego lematu,
jego bezpośredniego zastosowania i zgodności z oryginałem Walla;
nie stanowi pełnego audytu całego rozdziału 27.

Po zmianach `buduj_tomy.ps1` złożył dwa przebiegi trzech tomów
(212, 181 i 163 strony). Indeksy przyjęły 112, 96 i 111 haseł,
bez odrzuceń i ostrzeżeń. W logach nie ma błędów składu,
przepełnień ani nierozwiązanych odsyłaczy. Sprawdzono łącza
między tomami oraz strony PDF 63–64 tomu III, w tym ostateczny
skład nowego lematu i jego zastosowania.

## 19 października 2026 — rozłączne sfery w nieparzystym przypadku Walla

Porównano początek §6 na s.~58
[oryginału Walla](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf)
z krokiem przygotowującym dowód twierdzenia 6.4 w rozdziale 27.
Dopisano lemat wyprowadzający reprezentację skończonej rodziny
generatorów $\pi_{k+1}(f)$ przez parami rozłączne obramowane
zanurzenia $S^k\times D^{k+1}\hookrightarrow\operatorname{int}M$.
Twierdzenie 1.1 Walla dostarcza właściwej klasy regularnej
homotopii z danych normalnych. Jednoczesne położenie ogólne
usuwa przecięcia rdzeni, bo $2k-(2k+1)=-1$. Uzasadniono
także zakres stabilizacji $O(k+1)\to O$: izomorfizm na
$\pi_{k-1}$ wystarcza do trywialności wiązki normalnej,
a surjekcja na $\pi_k$ pozwala dopasować ramę do danych
stabilnych. Dopisano wybór dróg bazowych, zwężenie otoczeń
i homotopię $f$ do odwzorowania stałego na ich sumie.
Twierdzenie 1.1 i identyfikacja jądra z homotopią względną
pozostają jawnymi wejściami zewnętrznymi. Sprawdzono nowy
lemat i jego użycie w dowodzie; pełny audyt rozdziału 27
pozostaje otwarty.

Po dopisaniu lematu `buduj_tomy.ps1` złożył dwa przebiegi tomów
(212, 181 i 164 strony). Indeksy przyjęły 112, 96 i 111 haseł
bez odrzuceń i ostrzeżeń. W logach nie ma błędów składu,
przepełnień ani nierozwiązanych odsyłaczy; łącza między tomami
są obecne. Obejrzano ostateczne strony PDF 69–70 tomu III
z nowym lematem i jego zastosowaniem.

## 19 października 2026 — lokalny rachunek ruchu T1 Walla

Porównano ruch (T1) w §6, s.~61–62
[oryginału Walla](https://www.maths.ed.ac.uk/~v1ranick/books/scm.pdf)
z opisem niezależności od generatorów w rozdziale 27. Dopisano
lemat wyprowadzający efekt dołączenia generatora zerowego.
W rozkładzie $S^{2k+1}=\partial(D^{k+1}\times D^{k+1})$
sfera włóknowa i sfera bazowa brzegu nowej rurki ograniczają dyski
po przeciwnych stronach, więc tworzą dwa komplementarne proste
lagranżjany. Dla $k\geq2$ znikanie homologii sfery
$S^{2k}$ w stopniach $k$ i $k+1$ rozdziela stary oraz nowy
diagram przez ciąg Mayera--Vietorisa. Stąd reprezentant nowej
pary lagranżjanów można wybrać jako $\alpha\oplus\sigma$.
Uściślono wybór dysku usuwanego z lokalnego modelu, orientację
pary oraz dysk ograniczający rdzeń. Ten etap sprawdza nowy
lemat i jego zastosowanie; pełny audyt rozdziału 27
pozostaje otwarty. Konstrukcja ruchu T4 i rachunek śladów
regularnych homotopii pozostają wskazanymi w tekście wynikami
zewnętrznymi.

Po końcowej korekcie `buduj_tomy.ps1` wykonał dwa przebiegi i złożył
tomy o 212, 181 i 165 stronach. Indeksy przyjęły odpowiednio
112, 96 i 111 haseł bez odrzuceń ani ostrzeżeń. W logach nie ma
błędów, przepełnień ani nierozwiązanych odsyłaczy; pozostały cztery
komunikaty o niedopełnionych wierszach poza nowym fragmentem oraz
dwa ostrzeżenia o położeniu rysunków w tomie I. Sprawdzono nazwy
plików w odsyłaczach między tomami i obejrzano strony PDF 70–71
tomu III (drukowane 69–70), zawierające lemat i cały jego dowód.
