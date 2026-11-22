# Topologia ogólna — rozdział 25, audyt 02 (pierwszy czysty)

**Data:** 2026-11-22.
**Niezmieniony blob:** `7b772123870296af95d3ce951ccddb65685af7aa`.
**Wynik:** CZYSTY 1/2, bez zmian źródła rozdziału.
**GitHub CI:** [45056802863](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45056802863)
— completed/success, artefakt 14767733188.

## Niezależna weryfikacja 14 dowodów

**1. Obrazy i produkty continuów.** Obraz ciągły jest niepusty,
zwarty i spójny; cecha Hausdorffa pochodzi od przestrzeni
docelowej, a nie jest wnioskowana z ciągłości. Produkt
zwartego Hausdorffa jest zwarty (Tychonoff) i spójny
(wcześniejsze twierdzenie z rozdziału 08), przy jawnym
użyciu aksjomatu wyboru.

**2. Przecięcie zstępujące.** Niepustość
przecięcia niepustych zstępujących kompaktów
wynika z własności skończonych przecięć.
Rozdzielenie przecięcia przez U,V
powodowałoby, że jakiś K_N musi leżeć w U∪V;
istnienie takiego N jest wykazane przez
zwartość, a nie założone. Daje to sprzeczność.

**3. Przecięcie łańcucha.** Dla dowolnego
łańcucha podcontinuów niepustość wynika
z FIP; spójność uzyskuje się przez
skończone podpokrycie otwartymi
X\C oraz U∪V. Liniowy porządek inkluzji
zapewnia, że przecięcie skończonej
podrodziny jest jednym z jej elementów.

**4. Kryterium nierozkładalności.**
Jeżeli X=A∪B, gdzie A,B są właściwymi
podcontinuami, niepusty otwarty zbiór
X\B zawiera się w A. Wymóg pustego wnętrza
wszystkich właściwych podcontinuów
wyklucza taki rozkład. Nie zadeklarowano
nieudowodnionej odwrotnej implikacji.

**5. Istnienie continuum nieprzywiedlnego.**
Rodzina podcontinuów zawierających a,b
jest niepusta. Porządek odwrotny
do inkluzji i lemat o przecięciu
łańcucha spełniają hipotezy
lematu Kuratowskiego–Zorna.
Dla a=b wśród podcontinuów
jest singleton, a dowód nadal działa.

**6. Granice odwrotne.**
Granica jest zamknięta w zwartym
Hausdorffa produkcie, bo warunki
f_n(x_{n+1})=x_n są przeciwobrazami
domkniętych przekątnych. Surjektywność
projekcji p_n wynika z kolejnego
wyboru przeciwobrazów dla kolejnych map,
a współrzędne wcześniejsze wyznaczamy
przez składanie map wiążących.
Gdyby cała granica nie była spójna,
zamknięte rozłączne A,B
wyznaczałyby zstępujące
niepuste zbiory par (a,b)∈A×B
o takich samych pierwszych n współrzędnych.
Zwartość dałaby a=b; stąd
na którymś poziomie projekcje A,B
są rozłączne i rozdzielają spójne X_n:
sprzeczność. W przypadku metrycznym
użyto zgodnej metryki produktu.

**7. Surjektywność granic przedziałowych.**
Ograniczenie X_n=[0,1] spełnia
hipotezy poprzedniego twierdzenia;
nie wymaga nowego argumentu.

**8. Pełne gałęzie odwzorowania namiotowego.**
T^r ma dokładnie 2^r gałęzi
afinicznych, każda o pełnym obrazie [0,1].
Indukcja dzieli każdą wcześniejszą
gałąź na dwie równe podgałęzie,
dając poprawny indeks j=0,...,2^r-1.

**9. Nierozkładalność Knastera.**
Niepuste wnętrze właściwego
podcontinuum C dawałoby cylinder
p_k^-1(U)⊂C. Na poziomie m≥k+2
projekcja p_m(C) jest przedziałem
zawierającym punkty pierwszej
i ostatniej pełnej gałęzi T^{m-k},
więc zawiera [1/4,3/4].
Dla dowolnego j dobieramy m≥j+2
i otrzymujemy p_j(C)=I, gdyż
T²([1/4,3/4])=I.
Pełność wszystkich rzutów
zamkniętego C oznacza C=X:
dowolne otoczenie w X zawiera
cylinder o pewnym poziomie.
To przeczy właściwości C.
Ponieważ właściwe podcontinua
mają puste wnętrze,
nierozkładalność jest dowiedziona.

**10. Solenoid jako continuum i grupa.**
Wszystkie mapy z↦z² są
ciągłymi surjekcjami okręgu na siebie.
Warunki z_{n+1}²=z_n są stabilne
przy mnożeniu i odwracaniu współrzędnych,
co daje zwartą przemienną grupę
topologiczną Hausdorffa.

**11. Lokalny model solenoidu.**
Dla łuku U otrzymanego z przedziału
J o długości <1 jednoznaczny
parametr t0∈J rozróżnia początek.
Na każdym poziomie dokładnie
dwa pierwiastki kwadratowe z_n
odpowiadają epsilon_{n+1}=0 lub 1.
Dzięki lokalnym ciągłym
wyborom gałęzi inverse jest
ciągła w topologii produktowej.
Otrzymujemy homeomorfizm
p0^-1(U)≅J×{0,1}^N.

**12. Brak lokalnej spójności solenoidu.**
Każdy spójny podzbiór
J×{0,1}^N ma rzut na Cantor
jednopunktowy. Żaden taki
pionowy przekrój nie zawiera
niepustego otwartego podzbioru
produktu, gdyż przestrzeń Cantora
nie ma punktów izolowanych.
Żadne otwarte otoczenie solenoidu
nie może być spójne w opisanej
lokalnej karcie.

**13. Spójny skończony graf.**
Realizacja jest zwartą Hausdorffa
przestrzenią metryzowalną
metryką długości najkrótszej drogi,
a małe gwiazdy wierzchołków i
przedziały krawędziowe tworzą
lokalnie spójną bazę. Dla każdej
krawędzi konstruujemy zamknięty
spacer od wspólnego wierzchołka,
który ją pokonuje i wraca.
Skończenie wiele spacerów
można skleić w ciągłą surjekcję
z [0,1] na graf.

**14. Surjekcje Peana na sześciany.**
Kodowanie Cantora przez ciągi
zero-jedynkowe jest homeomorfizmem.
Rozdzielanie cyfr na n podciągów
daje ciągłą surjekcję Cantora
na [0,1]^n; ciągłość współrzędnych
wynika z jednostajnie małych
ogonów szeregu. Twierdzenie Tietzego
z rozdziału 05 przedłuża każdą
współrzędną do funkcji na całym
[0,1] o wartościach nadal w [0,1].
Wektor tych funkcji jest ciągłą
surjekcją, ponieważ jego obraz
zawiera cały obraz Cantora.

## Kontrola składu i zależności

Źródło posiada 35 różnych etykiet,
15 odsyłaczy (5 do istniejących wyników
w rozdziałach 05, 08, 23) i 14
zrównoważonych środowisk proof.
Pary środowisk twierdzeń,
definicji, przykładów i rysunku
są poprawnie zamknięte.
Brak zakazanych sformułowań terminologicznych.

Zakończony CI 45056802863 (ten sam
blob rozdziału) zbudował
osobny **8-stronicowy PDF** i
pełną książkę **183 strony**.
Pobrano artefakt 14767733188,
wyrenderowano wszystkich osiem
stron i obejrzano ich zestawienie,
a strony 6 (rysunek namiotu)
i 8 (dowód Peana, podsumowanie)
dodatkowo w powiększeniu.
Wykres nie ma nakładających się napisów;
strona końcowa jest wypełniona
dowodem i podsumowaniem.
W logu pełnej książki i samodzielnego
PDF brak Overfull/Underfull,
Missing character, LaTeX Warning,
Undefined control sequence i Fatal error.

**Status: CZYSTY 1/2.** Rozdział
ma jeszcze przejść drugi niezależny
czysty audyt i jeden nadmiarowy
na dokładnie tym samym blobie.
