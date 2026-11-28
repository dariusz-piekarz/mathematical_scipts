# Topologia ogólna — rozdział 23, audyt 02 (pierwszy czysty)

**Data:** 2026-11-22.
**Źródło:** chapters/pl/general_topology/23-wymiar-topologiczny.tex.
**Nie­zmieniony blob:** c666640268a1a14b813b4e0a1e7744e342cf9fe8.
**Stan:** matematyczno-redakcyjny audyt czysty, **1/2**.
**CI/PDF:** odrębne wymagania; nowe testy przeszły, finalne
potwierdzenie plików PDF jeszcze nie było dostępne w chwili wpisu.

## Kontrola twierdzeń podstawowych

1. Każde pokrycie rozpatrywane jest jako indeksowane;
   rząd uwzględnia wielokrotne wystąpienia tego samego zbioru.
   Definicja wymiaru dotyczy wyłącznie zwartych przestrzeni
   Hausdorffa i nie uzurpuje sobie twierdzeń dla ogólnych X.
2. Dla homeomorfizmu h przeciwobrazy i obrazy rozdrobnienia
   zachowują rząd; zachodzi dim X=dim Y, łącznie z ∅ i ∞.
3. W lemacie o zamkniętym zmniejszeniu skończonego pokrycia
   normalność zwartego Hausdorffa X dostarcza zwężeń V_x
   o domknięciu w U_i; zwartość daje skończoną liczbę
   domknięć. Jeżeli X jest pusta, wybór k=0 daje F_i=∅.
4. Dla F domkniętego w X dodanie X\F do skończonego
   pokrycia i ograniczenie rozdrobnienia do F
   zachowuje rząd i zapewnia dim F<=dim X.
5. W charakterystyce dim X=0 warunek T1 pozwala
   użyć pokrycia U, X\{x}; rozdrobnienie rzędu 1
   wyodrębnia clopen otoczenie x zawarte w U.
   Dla clopen bazy skończone clopen podpokrycie
   i różnice zbiorów dają rozłączne rozdrobnienie.
6. Iloczyn dowolnej rodziny zwartych Hausdorffa
   przestrzeni wymiaru zero jest zwarty na mocy
   Tychonoffa, ma bazę clopen cylindrów,
   a więc dim=0; dla I=∅ iloczyn jest punktem.
7. Cantor: pierwsza różniąca się ternarna cyfra 0/2
   daje odległość co najmniej 3^{-m};
   homeomorfizm z \{0,1\}^N jest ciągły
   i różnowartościowy; otrzymujemy dim C=0.
8. Dla zwartej spójnej Hausdorffa X o >=2 punktach
   pokrycie X\{a},X\{b} wyklucza clopen rozdrobnienie,
   więc dim X>=1.

## Wymiary indukcyjne i przykłady

9. Warunek ind<=0 oznacza lokalną bazę clopen,
   a Ind<=0 oznacza możliwość wyboru clopen
   otoczeń całych domkniętych F wewnątrz U.
   Dla zwartego F wystarcza skończona suma
   clopen zbiorów z bazy. Obie implikacje
   prowadzą do dim=ind=Ind=0 (w odniesieniu do
   niepustych X); dla ∅ przyjęto wymiar -1.
10. W lemacie Lebesgue'a pokrycie kulami
    B(x,epsilon_x), których podwojone kule
    leżą w U_i, daje minimum delta.
    Każdy zbiór średnicy <delta jest w U_i.
11. Przedziały (kh-h,kh+h) mają rząd <=2
    na prostej, średnicę <delta i tylko
    skończenie wiele z nich przecina zwarte K.
    Stąd dim K<=1; dla nietrywialnego
    odcinka dolne oszacowanie daje dim=1.

## Nerw, triangulacja i pełny wymiar sześcianu

12. Po korekcie z audytu 01 wierzchołkami nerwu
    są wyłącznie indeksy niepustych U_i.
    Gdy U_i=X użyto psi_i=1,
    a dla innych U_i psi_i=d(x,X\U_i).
    Funkcje barycentryczne są nieujemne,
    ciągłe, o sumie 1, a ich dodatnie
    indeksy tworzą sympleks nerwu.
13. Triangulacja sześcianów siatki Freudenthala
    jest zgodna na wspólnych ścianach;
    lokalnie skończone otwarte gwiazdy
    mają rząd <=n+1, średnicę <=2h sqrt(n).
    Zwartość K i liczba Lebesgue'a
    wyznaczają skończone rozdrobnienie o takim rzędzie.
14. Własność Poincarégo--Mirandy wyprowadzono
    z twierdzenia Brouwera dla D^n:
    jawny homeomorfizm radialny
    [-1,1]^n -> D^n ma odwrócenie
    v -> (||v||_2/||v||_∞)v dla v!=0,
    oba odwzorowania są ciągłe również w zerze.
    Punkty stałe projekcji P_Q(x-f(x))
    nie mogą należeć do ścian x_i=0 lub x_i=1
    na mocy warunków znaku; we wnętrzu
    są zerami f.
15. Lemat o wektorach w ortantach wybiera
    kolejny wektor poza skończoną sumą
    właściwych podprzestrzeni rozpiętych
    przez co najwyżej n-1 wcześniejszych.
    Zapewnia to niezależność każdej rodziny <=n.
16. Przypuszczenie dim[0,1]^n<=n-1
    daje rozdrobnienie rzędu <=n
    pokrycia przez 2^n zbiorów U_σ.
    Wybierając wektory w ortantach według U_σ
    i ciągłe współczynniki barycentryczne,
    otrzymujemy f(x) bez zera,
    bo ma najwyżej n dodatnich współczynników
    przy liniowo niezależnych wektorach.
    Na przeciwległych ścianach każda współrzędna
    f_i ma ścisłe przeciwne znaki,
    co przeczy lematowi Poincarégo--Mirandy.
    Stąd dim[0,1]^n=n.
17. Nie twierdzimy ogólnej równości
    dim=ind=Ind w wymiarze >0 bez dowodu;
    źródło twierdzenia Brouwera jest wskazane
    w już istniejącej topologii algebraicznej AT-19.

## Kontrola redakcyjna i integracja

Źródło: 1135 wierszy, 40 różnych etykiet,
23 odsyłacze, z czego dwa do
już istniejących twierdzeń rozdziału 07
(Tychonoff i normalność zwartych Hausdorffa).
Sprawdzone środowiska twierdzeń, definicji,
dowodów, wyliczeń i rysunku są zrównoważone.
Nie znaleziono niedozwolonej terminologii
ani niejawnych założeń domkniętości/pustości.
Żadnego źródła rozdziałów 01–22 nie zmieniono.

**Wynik: CZYSTY 1/2**, bez zmian źródła w audycie 02.
Wymagana dalsza niezależna czysta kontrola
tego samego bloba oraz audyt dodatkowy
i zielony CI z realnym przeglądem PDF.


## Aktualizacja po inspekcji PDF

Po audycie 02 pobrano rzeczywisty PDF z zielonego
[CI 45051084818](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45051084818)
(artefakt general-topology-ch01-ch23, ID 14765586288).
Wyrenderowano wszystkie 10 stron A4 i obejrzano je.
Wzory i rysunek nie zachodziły na siebie, lecz
zidentyfikowano problem redakcyjny:
ostatnia, dziesiąta strona zawierała wyłącznie
krótkie podsumowanie i była niemal pusta.
Skrócono podsumowanie bez zmiany wyników matematycznych
w commicie 16672f16602b27fc08ba96a201c76c001fcf24a8
(nowy blob źródła: ef9c42ad0b4a423bf85f4cb80939ee9c46b3da96).

**Niniejszy audyt pozostaje czystą kontrolą matematyki
poprzedniego bloba, ale po tej zmianie nie zalicza się
do dwóch czystych audytów najnowszego źródła.**
Aktualny licznik: **0/2**. Konieczne ponowne CI i rendering.
