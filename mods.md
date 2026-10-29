# Uzasadnienia zmian w repozytorium `mathematical_scipts`

## 2026-10-29 — konstrukcje Freedmana w tomie IV

### Problem

Rozdział 34 obliczał $E_8$ dla gładkiego plumbowania z brzegiem,
ale rozdział 36 przechodził od tej macierzy wprost do twierdzenia
o zamkniętych rozmaitościach. Podawał również dwa typy o formie
$[1]$ bez pokazania mechanizmu konstrukcji drugiego typu.
Obramowane uchwyty, dyski Whitneya i wieże Cassona były już
opisane w rozdziałach 34–35.

### Rozwiązanie i wpływ

W `tex/rozdzialy/33-freedman-klasyfikacja.tex` dodano dwa
przykłady z dowodu Freedmana. Pierwszy skleja plumbowanie
$E_8$ z kontraktowalnym topologicznym wypełnieniem brzegu,
a następnie wylicza $\pi_1$, $H_2$, formę i
$\operatorname{ks}=1$. Drugi używa izometrii
$E_8\oplus[-1]\cong8[1]\oplus[-1]$ i zewnętrznego
twierdzenia Freedmana–Quinna o rozkładzie sumy spójnej,
aby otrzymać typ o formie $[1]$ i $\operatorname{ks}=1$.
Dodano też wyjaśnienie, dlaczego rozkład, hipoteza Poincarégo
i porównanie $\operatorname{ks}$ prowadzą do jednoznaczności.
Istniejąca tabela przykładów odsyła do nowych rachunków.
Dodatek A wskazuje osobne wyniki zewnętrzne. W
`PLAN_DZIALANIA.md` poprawiono zakres etapu na konstrukcje
Freedmana, a `PRZEGLAD.md` zapisuje źródła i granicę audytu.

Kompromis: istnienie kontraktowalnego wypełnienia,
topologiczny rozkład sumy spójnej i czterowymiarowa hipoteza
Poincarégo pozostają jawnymi wejściami zewnętrznymi.
Rachunki nie stanowią ich dowodu. Nowy tekst wykorzystuje
istniejący graf $E_8$ i omija powtórzenie opisów uchwytów
oraz wież Cassona.

### Weryfikacja

Niezależna kontrola z oryginalnymi źródłami potwierdziła
znaki macierzy, rachunki van Kampena i Mayera–Vietorisa,
wartość $\operatorname{ks}$ oraz szczególny przypadek
twierdzenia o rozkładzie. Poprawiono odsyłacz do pierwodruku
Freedmana–Quinna: odpowiednikiem §10.5.1 wersji z 2013 r.
jest dowód twierdzenia 10.1 w §10.4 wydania z 1990 r.
Po osobnym przeglądzie zastąpiono nieścisły opis przecinania
się rdzeni odrębnych uchwytów poprawnym opisem sfer zerowych
plumbowanych wiązek. Twierdzenie van Kampena zapisano jako
iloraz iloczynu wolnego, bez zakładania injektywności odwzorowań
grup brzegu. Sprecyzowano rolę twierdzenia Hurewicza.
Pierwszy pełny skład zatrzymał się na zamykającym nawiasie
w opcjonalnym tytule przykładu; tytuł poprawiono przed
ponownym składem.
Przerwany kolejny przebieg pozostawił ucięte pliki pomocnicze
tomów II i IV. Opróżniono sześć wygenerowanych plików
`aux`, `toc` i `out`, a pełny skład uruchomiono ponownie.
Skrypt `buduj_tomy.ps1` zakończył się po dwóch obiegach.
Kontrola czterech PDF-ów dała 216, 182, 104 i 85 stron,
113, 96, 33 i 96 przyjętych wpisów indeksu bez odrzuceń,
po trzy łącza między tomami i zgodne sumy SHA-256 kopii.
W logach nie ma brakujących odsyłaczy, przepełnionych
wierszy ani brakujących znaków. Obejrzano strony 45–48
i 68 tomu IV z nowym tekstem i dodatkiem A; skład jest
czytelny. `git diff --check` przeszedł.

## 2026-10-28 — trzy rachunki chirurgii w tomie III

### Problem

Obliczenie $L_n(\Z)$ w rozdziale 27 nie pokazywało wpływu jednej
nietrywialnej pętli. Rozdział 26 stwierdzał zależność chirurgii od
obramowania, lecz nie porównywał obu możliwości dla okręgu
w $S^4$. Istniejący przykład $C_5$ w rozdziale 27 wskazywał
niezerową torsję Whiteheada bez rachunku grup Tate'a w ciągu
Rothenberga. To trzy uzupełnienia z punktu 1 nowego planu.

### Rozwiązanie i wpływ

- W `tex/rozdzialy/23-przeszkoda-chirurgiczna.tex` obliczono
  $L_n^s(\Z[t,t^{-1}],1)$ przez rozszczepienie Shanesona--Ranickiego.
  Ogólna formuła zachowuje dekorację $h$ w drugim składniku.
  Zapisano tabelę czterookresową, przypadki $n=7,9$ i granicę
  między grupą przeszkód, przeszkodą mapy i jej realizacją.
  Wersję geometryczną Shanesona opisano z hipotezami, a ogólną
  formułę oparto na późniejszej pracy Ranickiego z 1986 r.;
  wcześniejsze twierdzenie z 1973 r. ma sprostowanie.
- W tym samym rozdziale z $\operatorname{Wh}(C_5)\cong\Z$
  i trywialnego działania inwolucji wyliczono grupy Tate'a:
  $\Z/2$ w stopniach parzystych i zero w nieparzystych.
  Podstawienie do ciągu Rothenberga daje injekcję $j_n$
  dla parzystego $n$, surjekcję dla nieparzystego i krótki
  ciąg łączący $\operatorname{coker}j_n$ z $\ker j_{n-1}$.
  Nie przypisuje się tych grup konkretnej mapie normalnej.
- W `tex/rozdzialy/22-chirurgia-geometryczna.tex` porównano dwa
  obramowania standardowego $S^1\subset S^4$. Rozkład brzegu
  $D^2\times D^3$, sklejenie i ciąg Mayera--Vietorisa prowadzą
  do wiązek $S^2$ nad $S^2$ o formach hiperbolicznej i
  nieparzystej. Zewnętrznym wejściem pozostaje identyfikacja
  nietrywialnej wiązki z $\mathbb{CP}^2\#\overline{\mathbb{CP}^2}$.
  Nie użyto wysokowymiarowego kryterium Walla w wymiarze cztery.
- W dodatku A zapisano nowe zależności od Larsona, Wendla,
  Milnora, Shanesona i Ranickiego. `PLAN_DZIALANIA.md` zawiera
  kolejkę, a `PRZEGLAD.md` szczegółowy zakres audytu i źródła.

Kompromis polega na przyjęciu rozszczepienia grup $L$, pełnego
obliczenia $\operatorname{Wh}(C_5)$ i identyfikacji wiązki jako
wyników zewnętrznych. Podane rachunki sprawdzają ich konsekwencje;
nie zastępują dowodów tych twierdzeń ani nie klasyfikują wszystkich
map normalnych lub wszystkich grup $L^s/h(\Z[C_5])$.

### Weryfikacja

Niezależny przegląd potwierdził tabelę grup $L$ z twierdzeniem
13A.8 Walla, generator $\operatorname{Wh}(C_5)$ z przykładem 6.6
Milnora, indeksy ciągu Rothenberga i oba rachunki form przecięcia.
Po przeglądzie doprecyzowano hipotezy Shanesona, homologię wyniku
chirurgii i miejsce przypadku okręgu w dowodzie Larsona.
Pełny `buduj_tomy.ps1` zakończył się kodem 0 po trzech przebiegach.
Tomy I–IV mają 216, 182, 104 i 83 strony, a indeksy przyjęły
113, 96, 33 i 94 wpisy bez odrzuceń. Logi nie wykazały
nieustalonych odsyłaczy, przepełnionych wierszy ani brakujących
znaków. Każdy PDF ma trzy łącza do pozostałych tomów, a kopie
w `build/tomy` mają zgodne sumy SHA-256. Obejrzano fizyczne strony
42–43 i 57–59 tomu III oraz 63–64 tomu IV. `git diff --check`
przeszedł bez błędów.

## 2026-10-28 — most między chirurgią Ricciego a wymiarem cztery

### Problem

Po rozdziałach 31–33 o rozmaitościach wymiaru trzy rozdział 34
przechodził bezpośrednio do form przecięcia. Czytelnik mógł
utożsamić chirurgię potoku Ricciego z operacjami wykonywanymi
za pomocą uchwytów i dysków w wymiarze cztery.

### Rozwiązanie i wpływ

Na początku `tex/rozdzialy/31-freedman-formy-przeciecia.tex` dodano
krótki most. Zestawia on cięcie kontrolowanej szyjki
$S^2\times D^1\to D^3\times S^0$ z wymianą
$S^1\times D^2\to D^2\times S^1$, którą na trójwymiarowym
brzegu powoduje przyczepienie czterowymiarowego uchwytu $2$.
Drugą operację identyfikuje jako wypełnienie Dehna określone
obramowaniem. Następnie wskazuje na przecięcia dysków Whitneya
z powierzchniami w wymiarze cztery i odsyła do hipotez
topologicznego twierdzenia o zanurzaniu dysków.
Po przeglądzie doprecyzowano, że przyczepienie zmienia brzeg
$D^4$, a podpis drugiej strzałki oznacza operację na tym brzegu;
nie opisuje całego brzegu samego uchwytu.

To porównanie ułatwia przejście między częściami książki i
oddziela formalną wymianę brzegu od głębokiego twierdzenia
Freedmana--Quinna. Kompromis: jest to krótka mapa pojęć,
bez dowodzenia twierdzeń Perelmana ani o zanurzaniu dysków.
Nie zmieniono konfiguracji składu ani zależności projektu.
Zaktualizowano `PLAN_DZIALANIA.md` i `PRZEGLAD.md`, aby zamknąć
czwarty punkt planu tomu IV i zapisać matematyczny zakres zmiany.

### Weryfikacja

Podgląd tomu IV złożył się poprawnie do 83 stron. Obejrzano
fizyczną stronę 31: formuła, tekst i odsyłacze są czytelne.
Po doprecyzowaniu opisu brzegu ponownie wykonano pełny
`buduj_tomy.ps1`. Oba uruchomienia zakończyły się kodem 0
po dwóch przebiegach. Ponownie obejrzano fizyczną stronę 31.
Tomy I–IV mają
216, 182, 102 i 83 strony; indeksy przyjęły 113, 96, 30 i 94
wpisy bez odrzuceń. Kontrola logów nie wykazała nieustalonych
odsyłaczy, przepełnionych wierszy ani brakujących znaków.
Każdy tom ma trzy łącza do pozostałych tomów, a kopie PDF mają
zgodne sumy SHA-256. `git diff --check` przeszedł.

## 2026-10-28 — mechanizm małych i dużych egzotycznych $\R^4$

### Problem

Rozdział 38 szczegółowo przedstawiał indukcję dużych struktur Gompfa,
ale twierdzenie o kontinuum małych struktur De Michelisa--Freedmana
było podane tylko jako wynik zewnętrzny. Bez wyjaśnienia wspólnego
rdzenia i rodziny radialnej czytelnik mógł odnieść błędne wrażenie,
że obie konstrukcje rozróżnia ten sam zakaz zanurzenia zwartego bloku.

### Rozwiązanie i wpływ

W `tex/rozdzialy/35-egzotyczne-r4.tex` dopisano opis obszaru typu
*ribbon* otwartego w standardowej $\R^4$, wspólnej zwartej gładkiej
podrozmaitości $K$ i zagnieżdżonych obszarów dla parametrów ze
zbioru Cantora. Tekst odróżnia topologiczną funkcję promienia od
gładkiej sfery poziomu. Wyjaśnia, że argument z niezmiennikiem
cechowania $|\Phi(B)|\ne|\Phi(Q)|$ dotyczy dyfeomorfizmu zgodnego
na $K$ do izotopii; analiza końców okresowych i przeliczalność
klas zanurzeń $K$ prowadzą do kontinuum nieoznaczonych typów.
Nie przypisuje każdemu parametrowi osobnego typu.

Nowy diagram TikZ porównuje tę drogę z indukcją Gompfa.
Duże $R_n$ zawierają zwarty $X$, którego nie można zanurzyć
z zachowaniem orientacji w standardowej $\R^4$; świadek
$K_n=X\sqcup M_{L_n}$ odróżnia kolejne etapy. Małe obszary
już zanurzają się w standardowej $\R^4$, więc ich rdzeń $K$
pełni inną rolę. W podpisie zachowano hipotezę ogolenia
$R_{n-1}$ i ograniczenie orientacyjne po stronie Gompfa.
Źródłami są [De Michelis--Freedman, §3–4](https://doi.org/10.4310/jdg/1214447810)
oraz [Gompf, lematy 1.1–1.2](https://doi.org/10.4310/jdg/1214439566).

Kompromis: diagram przedstawia zależności, a nie geometryczny
model dzikiego końca. Głęboka analiza uchwytów Cassona i końców
okresowych pozostaje cytowanym wynikiem zewnętrznym.
Nie zmieniono konfiguracji LaTeX ani nie dodano zależności.

### Weryfikacja

Porównano hipotezy i dwa etapy rozróżnienia typów z oryginalnymi
pracami. Doraźny skład tomu IV zakończył się kodem 0. Po
przeniesieniu diagramu obejrzano fizyczne strony 59–60;
po ostatnim doprecyzowaniu etykiety obejrzano je ponownie
w końcowym PDF. Diagram, podpis i tekst mieszczą się w łamie.
Pełny `buduj_tomy.ps1` przeszedł po dwóch przebiegach.
Tomy I–IV mają 216, 182, 102 i 83 strony, a indeksy przyjęły
113, 96, 30 i 94 wpisy bez odrzuceń. Kontrola logów nie wykazała
nieustalonych odsyłaczy, przepełnionych wierszy ani brakujących
znaków. Każdy PDF ma trzy łącza do pozostałych tomów i kopię
o zgodnej sumie SHA-256. `git diff --check` przeszedł.

## 2026-10-28 — skończona energia instantonu i wejścia do twierdzenia Donaldsona

### Problem

Rozdział 37 podawał lokalne rozwiązanie równania antysamodualności
o nieskończonej energii, ale brakowało obliczalnego przykładu
instantonu na zwartej czterowymiarowej rozmaitości z niezerową
liczbą Cherna. Opis dowodu diagonalizacji wymieniał narzędzia
analityczne bez pokazania ich osobnych ról. Ponadto tekst
przypisywał samemu rachunkowi sygnatury równość liczby punktów
redukowalnych z $b_2(X)$, chociaż bez uwzględnienia orientacji
składowych brzegu daje on jedynie nierówność.

### Rozwiązanie i wpływ

W `tex/rozdzialy/34-donaldson.tex` dodano przykład BPST dla
$A_\lambda=\operatorname{Im}(\bar q\,\mathrm dq)/(|q|^2+\lambda^2)$
w orientacji zgodnej z wcześniejszą konwencją rozdziału.
Jawny rachunek krzywizny pokazuje $F_A^+=0$,
$|F_A|^2=48\lambda^4/(r^2+\lambda^2)^4$ i energię $8\pi^2$.
Druga lokalna trywializacja po zmianie cechowania przez
odwrotność mapy $q/|q|$
pokazuje gładkie przedłużenie na $S^4$; to pozwala wywnioskować
$c_2(E)[S^4]=1$ z istniejącej tożsamości energii. Zapis
odsyła do [oryginalnej pracy BPST](https://strings.itp.ac.ru/Papers/belavin1975.pdf).

W części o diagonalizacji dopisano operator
$d_A^*\oplus d_A^+$, jego indeks
$8k-3(1-b_1+b_2^+)$ i wynikający stąd oczekiwany wymiar $5$
dla przypadku jednospójnego, ujemnie określonego i $k=1$.
Tabela oddziela rolę cechowania i transwersalności,
punktów redukowalnych z linkiem $\mathbb CP^2$,
koncentracji krzywizny oraz kołnierza małych instantonów.
Odsyłacze prowadzą do prac Atiyaha--Hitchina--Singera,
Donaldsona, Uhlenbeck i Taubesa. Tekst precyzuje, że słaba
zwartość Uhlenbeck przy ograniczeniu $L^p$, $p>2$,
nie wyklucza koncentracji przy krytycznym ograniczeniu energii
$L^2$, a opis kołnierza korzysta również z konstrukcji Taubesa
i analizy Donaldsona.

Poprawiono przejście do algebraicznego zakończenia dowodu:
rachunek sygnatury daje $n(Q_X)\geq b_2(X)$, natomiast
ortogonalność różnych klas o kwadracie $-1$ daje
$n(Q_X)\leq b_2(X)$. Dopiero obie nierówności dają równość
i pełną rangę układu. Wniosek o diagonalizacji pozostaje
bez zmian.

Kompromis: przykład zawiera dłuższy rachunek i drugą kartę,
a tabela syntetyzuje głębokie wyniki, których dowody nadal
pozostają zewnętrzne. Nie dodano pakietów LaTeX ani nie
zmieniono konfiguracji składu.

### Weryfikacja

Porównano formułę BPST, znak antysamodualności i indeks z pracami
źródłowymi; sprawdzono bezpośrednio normę krzywizny, całkę radialną
i zgodność lokalnych form po zmianie cechowania. Doraźny skład
tomu IV zakończył się kodem 0. Obejrzano fizyczne strony 50--52:
przykład BPST i tabela mieszczą się w łamie, a wzory i podpisy
są czytelne. Pełny skład `buduj_tomy.ps1` przeszedł po dwóch
przebiegach. Tomy I--IV mają 216, 182, 102 i 82 strony;
indeksy przyjęły odpowiednio 113, 96, 30 i 94 wpisy bez
odrzuceń. Kontrola logów nie wykazała niezdefiniowanych
odwołań, przepełnionych wierszy ani brakujących znaków.
Każdy PDF ma na stronie tytułowej trzy łącza do pozostałych
tomów i kopię o zgodnej sumie SHA-256. `git diff --check`
zakończył się kodem 0.

## 2026-10-28 — droga do klasyfikacji TOP w tomie IV

### Problem

Rozdział 34 wyprowadzał macierz obramowanego splotu bez rysunku,
na którym można jednocześnie odczytać wpis diagonalny i liczbę
sprzężenia. Rozdział 36 omawiał przykłady $H$, $[1]$, $E_8$ i
$2E_8$ oraz łańcuch wyników prowadzących do klasyfikacji, lecz
porównanie typów TOP/DIFF i roli dysków oraz sfer wymagało
zestawiania kilku akapitów.

### Rozwiązanie i wpływ

W `tex/rozdzialy/31-freedman-formy-przeciecia.tex` dodano
oryginalny diagram TikZ splotu Hopfa z obramowaniami $(0,0)$
oraz niewęzła z obramowaniem $+1$. Strzałki orientacji i dwa
przejścia nad/pod dają dwa dodatnie skrzyżowania, więc
$\operatorname{lk}=1$ i macierz $H$; pojedyncza liczba obramowania
daje macierz $[1]$. Rysunek odsyła do istniejącego grafu $E_8$
bez powielania jego rachunku.

W `tex/rozdzialy/33-freedman-klasyfikacja.tex` dodano schemat
danych immersyjnych, wież Cassona, lokalnie płaskich dysków
i sfer, chirurgii TOP, kontroli $\pi_1$, topologicznego
$s$-kobordyzmu i klasyfikacji przez $(Q,\operatorname{ks})$.
Tekst i podpis rozdzielają dualność algebraiczną jako hipotezę
od dualności geometrycznej jako wniosku. Wymagania dotyczące
zaniku przeszkód i pozostałych hipotez są jawne; schemat nie
zastępuje twierdzeń Freedmana--Quinna ani
Powella--Raya--Teichnera. Realizacja form i rachunek
$\operatorname{ks}$ są wskazane jako dalsze, osobne wejścia.

Tabela w tym samym rozdziale rozdziela dwa typy TOP dla $[1]$
według $\operatorname{ks}=0,1$ oraz zestawia parzystość,
sygnaturę, $\operatorname{ks}$ i istnienie wygładzenia dla
wszystkich czterech form. W szczególności $2E_8$ ma
$\operatorname{ks}=0$, lecz nie jest wygładzalna przez
twierdzenie Donaldsona. „DIFF: tak” oznacza istnienie
struktury gładkiej, bez tezy o jej jednoznaczności.
Zakres klasyfikacji i wzór dla form parzystych porównano z
[Freedmanem--Quinnem, §10.1 i §10.2.2](https://archive.mpim-bonn.mpg.de/4789/2/FreedmanQuinn-TopologyOf4Manifolds-Reformatted2013.pdf).

Kompromis: rozdział 36 zawiera teraz syntetyczną tabelę po
opisanych już przykładach, a schemat pokazuje zależność wyników,
nie dowód klasyfikacji. Nie zmieniono kodu rozdziału 35,
istniejącego drzewa Cassona, rachunku $E_8$ ani konfiguracji
pakietów LaTeX.

### Weryfikacja

Sprawdzono znaki obu skrzyżowań splotu Hopfa, wartości pięciu
wierszy tabeli względem klasyfikacji Freedmana--Quinna i rolę
sfer dualnych w schemacie. Doraźny skład tomu IV przez
`latexmk` zakończył się kodem 0 i dał 81 stron. Obejrzano
fizyczne strony 35, 46 i 47: rysunki i tabela mieszczą się
w łamie, etykiety i podpisy są czytelne. Po powiększeniu tabeli
sprawdzono ponownie stronę 47 końcowego PDF. Pełny skład
`buduj_tomy.ps1` przeszedł po dwóch przebiegach: tomy I--IV
mają 216, 182, 102 i 81 stron, a indeksy przyjęły 113, 96,
30 i 93 wpisy bez odrzuceń. Kontrola logów, trzech łączy do
pozostałych tomów w każdym PDF oraz zgodności SHA-256 kopii
PDF zakończyła się kodem 0. `git diff --check` nie wykazał
błędów białych znaków.

## 2026-10-28 — przeplecenie dwóch uchwytów sfery

### Problem

Autor poprosił o przestrzenny przykład, w którym dwa rozłączne
uchwyty na sferze zostają przecięte, przeplecione i ponownie
sklejone. Doprecyzował, że każda rurka ma wrócić do swoich
pierwotnych końców. Bez tego warunku rysunek mógłby przedstawiać
inną operację na parowaniu czterech obrzeży.

### Rozwiązanie i wpływ

W rozdziale 26 dodano przykład i trójstanowy rysunek TikZ:
sfera z dwoma uchwytami, cztery otwarte obrzeża po dwóch
cięciach oraz dwa przeplecione uchwyty po sklejeniu.
Rurki tworzą czysty warkocz $\sigma_1^2$ z dwoma
skrzyżowaniami rzutu, zaznaczonymi białymi maskami
i kolejnością głębokości. Pary $A_-/A_+$ oraz $B_-/B_+$
pozostają te same. Tekst liczy $\chi=-2$ na sferze z
czterema otworami; dwie wklejane pobocznice mają $\chi=0$,
więc wynik nadal jest powierzchnią rodzaju dwa.

Rysunek ma charakter przestrzennego schematu opartego na
cieniowaniu i szerokich, warstwowych kreskach TikZ. Oznacza
położenie wyróżnionych uchwytów, ale nie ustala klasy
izotopii nieoznaczonej powierzchni. To ograniczenie
sprawdzono wobec przykładu niezawęźlonego ciała uchwytowego
z przeplecionymi rdzeniami w pracy
[Benedettiego, Frigeria i Ghilioniego, *The topology of Helmholtz
domains*, przykład 6.16](https://people.dm.unipi.it/benedett/Expositiones_online.pdf).
Nie dodano nowych pakietów ani zewnętrznych plików graficznych.
Po podglądzie ustawiono dla nowego rysunku `[H]`, aby stał
bezpośrednio po przykładzie, przed dwiema dalszymi uwagami.
Kosztem jest mniejsza swoboda łamania: tekst przykładu
kończy się na jednej stronie, a rysunek otwiera następną.

### Weryfikacja

Sprawdzono rachunek charakterystyki Eulera oraz zachowanie
par końców w modelu dwóch skrzyżowań. Pełny skład czterech
tomów zakończył się kodem 0; PDF-y mają 216, 182, 102 i 80
stron. Indeksy przyjęły 113, 96, 30 i 93 wpisy bez odrzuceń.
Kontrola logów, trzech łączy między tomami na każdej stronie
tytułowej i sum SHA-256 kopii PDF przeszła bez błędów.
Obejrzano fizyczne strony 39–40 tomu III: tekst przykładu
stoi przed rysunkiem 26.4, a rysunek mieści się w łamie;
etykiety, obrzeża i przejścia nad/pod są czytelne.

## 2026-10-28 — dwa wizualne kroki chirurgii powierzchni

### Problem

Obecne rysunki pokazywały lokalną wymianę dwóch dysków na pierścień
oraz przejście od jednej sfery do torusa. Brakowało obrazu dwóch
sfer połączonych kolejno dwiema rurkami. Sam skrót
$S^2\sqcup S^2\to T^2$ mógł sugerować, że pierwszy uchwyt
od razu tworzy rodzaj jeden.

### Rozwiązanie i wpływ

W rozdziale 26 (`tex/rozdzialy/22-chirurgia-geometryczna.tex`)
dodano przykład i schemat $S^2\sqcup S^2\to S^2\to T^2$.
Pierwszy $1$-uchwyt trójwymiarowego śladu łączy składowe,
drugi dołącza rurkę do dwóch miejsc już połączonej powierzchni.
Na brzegu każdy krok jest chirurgią typu $(0,2)$: wycina
$S^0\times D^2$ i wkleja $D^1\times S^1$.
Schemat pokazuje miejsca wycinania złotymi polami,
a podpisy pod bryłami podają liczby składowych i charakterystyki
Eulera: $(2,4)\to(1,2)\to(1,0)$.
Drugi krok jest także samodzielnym wariantem jednej sfery;
tekst odsyła do istniejącego rysunku tego wariantu.
Dodano warunek sklejenia zachowującego orientowalność,
ponieważ inne sklejenie daje butelkę Kleina.

Kompromis: zamiast powielać istniejący rysunek $S^2\to T^2$,
nowy schemat przedstawia uproszczone bryły z dwiema rurkami.
Ich podpisy dotyczą brzegów po wygładzeniu naroży.
Po podglądzie zwiększono skalę schematu, aby wyraźnie pokazać
dyski i prześwit między rurkami. Wcześniejszy rysunek lokalnej
wymiany dysków na pierścień przypięto do miejsca w tekście
specyfikatorem `[H]` z używanego już pakietu `float`: w pierwszym
składzie wpływał między części nowego przykładu i rozcinał zdanie
na granicy stron. Kosztem mniejszej swobody łamania rysunek
pozostaje przed przykładem, do którego wprowadza.
Źródłem pojęcia i kontroli orientowalności jest
[A. H. Wallace, *Modifications and Cobounding Manifolds*,
§§1 i 3](https://doi.org/10.4153/CJM-1960-045-7);
rysunek opracowano samodzielnie. Rozdział zachowuje własną
konwencję typu $(0,2)$ i jawnie odróżnia ją od Wallace'owskiego
oznaczenia $(0,1)$.

### Weryfikacja

Przeliczono $\chi(M')=\chi(M)-2$ z sumy po dwóch dyskach
i pierścieniu oraz porównano liczbę składowych i orientowalność
z opisem Wallace'a. Wyniki składu i oględzin strony zapisano
w `PRZEGLAD.md` oraz polecenia w `manual.md`.

## 2026-10-28 — mapa hipotez chirurgii w tomie III

### Problem

Po rozpisaniu ciągu chirurgii i śledzonego przykładu czytelnik musiał
zbierać z kilku rozdziałów hipotezy kategorii, wymiaru, grupy
podstawowej, brzegu i dekoracji. Szczególnie łatwo było utożsamić
pięciowymiarowe kryterium Walla z twierdzeniem realizacyjnym dla
nieparzystej grupy $L$ albo zastosować $s$-kobordyzm do śladu,
który jeszcze nie jest prostym $h$-kobordyzmem.

### Rozwiązanie i wpływ

W `tex/rozdzialy/24-ciag-chirurgii.tex` dodano jedną sekcję z tabelą
hipotez. Zestawia ona DIFF z osobnym odpowiednikiem TOP,
$n$-wymiarowy cel ze śladem wymiaru $n+1$, dowolną grupę
$\pi_1(X)$ i charakter orientacji, warunek ustalonego brzegu oraz
dekoracje $s/h$. Osobny akapit objaśnia $n=5$: kryterium leży
w $L_5^s$, działanie realizuje parzysta grupa $L_6^s$ i twierdzenie
5.8 Walla, a końcowy $s$-kobordyzm jest sześciowymiarowy.
Zaznaczono, że twierdzenie Smale'a o $h$-kobordyzmie wymaga
jednospójności, podczas gdy ogólne twierdzenie o $s$-kobordyzmie
kontroluje torsję. Wersja TOP i związek dekoracji pozostają
jawnymi wynikami zewnętrznymi.

`PLAN_DZIALANIA.md` oznacza ostatni etap tomu III jako ukończony
i wskazuje pierwszy punkt tomu IV. `PRZEGLAD.md` rejestruje dokładny
zakres porównania ze źródłami. `manual.md` podaje polecenia budowania
i kontroli wykonane w tym etapie.

Kompromis: rozdział 28 jest dłuższy o syntetyczną tabelę, lecz nie
powiela dowodów Walla ani nie deklaruje dowodu odpowiednika TOP.

### Weryfikacja

Zakres twierdzeń porównano z
[Wallem, §§5–6 i 10](https://webhomes.maths.ed.ac.uk/~v1ranick/books/scm.pdf),
[Ranickim, §18](https://webhomes.maths.ed.ac.uk/~v1ranick/homology/topman.pdf)
oraz [Crowleyem–Macko, §2.2](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/crowmac.pdf).
Sprawdzono zwłaszcza, że ustalony brzeg dopuszcza $n=5$ i nie
wymaga izomorfizmu $\pi_1$ jego składowych z $\pi_1(X)$.
Po końcowej korekcie pełny skład czterech tomów zakończył się
po dwóch przebiegach. PDF-y I–IV mają 216, 182, 100 i 80 stron;
indeksy przyjęły 113, 96, 29 i 93 wpisy bez odrzuceń.
W logach nie ma niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Sprawdzono łącza na stronach tytułowych,
odsyłacz z mapy do tomu IV i zgodność kopii PDF według SHA-256.
Obejrzano fizyczne strony 78–80 tomu III: tabela mieści się
w polu strony, a przykład 28.6.2 zaczyna się od góry strony 80.
`git diff --check` nie wykazał błędów białych znaków.

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
