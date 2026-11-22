# Topologia ogólna — globalny audyt 02, blok 01–06

**Data:** 2026-11-22. **Zakres:** rozdziały 01–06, niezależna
próbka szczegółowego audytu matematycznego i zależności.
**Wynik:** brak wykrytych błędów w przejrzanych twierdzeniach;
audyt wszystkich dowodów tych rozdziałów pozostaje otwarty.
Nie nadawać całemu blokowi statusu pełnej kontroli dowód po dowodzie.

## Kontrola semantyczna wybranych wyników

- **01 — konstrukcja topologii z podbazy**
  (`thm:topog-podbaza-konstrukcja`):
  rodzina przecięć skończonych, z przecięciem pustym
  równym X, spełnia aksjomaty bazy; minimalność
  względem wszystkich topologii zawierających
  podbazę poprawnie wyprowadzono ze stabilności
  zbiorów otwartych na sumy dowolne i przecięcia skończone.
  Przypadek podbazy pustej daje topologię antydyskretną.
- **02 — zbiór pochodny**:
  \(\overline A=A\cup A'\) udowodniono
  dla dowolnej przestrzeni topologicznej, bez założenia T1;
  także \((A\cup B)'=A'\cup B'\) nie wymaga oddzielania.
  W dowodzie domkniętości A' użycie
  otwartości X\{x} jest poprawne i jawnie wymaga T1;
  kontrprzykład dwupunktowej przestrzeni
  antydyskretnej pokazuje konieczność ostrożności.
- **03 — sklejanie funkcji ciągłych**:
  na pokryciu otwartym ciągłość jest lokalna,
  a na skończonym pokryciu domkniętym
  kryterium przeciwobrazów domkniętych dowodzi
  ciągłości globalnej. Kontrprzykład rodziny
  singletonów pokazuje, że nie można zastąpić
  pokrycia skończonego dowolnym domkniętym.
- **04 — topologia ilorazowa**:
  sprawdzono rozróżnienie topologii końcowej
  i początkowej, odtwarzanie topologii
  ilorazowej przez przeciwobrazy,
  własność uniwersalną odwzorowań stałych na włóknach
  oraz poprawność warunku, że ciągła otwarta
  lub domknięta surjekcja jest ilorazowa.
- **05 — lemat Urysohna**:
  konstrukcja przez wymierne liczby dwójkowe
  \(r\mapsto U_r\) ma właściwą relację
  \(\overline{U_r}\subset U_s\) dla \(r<s\).
  Otwartość obu stron warunków \(f<a\) i \(f>a\)
  zapewnia ciągłość. Twierdzenie Tietzego:
  pierwszy krok zmniejsza błąd do 2M/3,
  szereg poprawek jest jednostajnie zbieżny,
  a dla funkcji nieograniczonej przeskalowanie
  przez \(t/(1+|t|)\) i odcięcie zbioru, gdzie
  ograniczone przedłużenie ma wartość ±1,
  pozwala zastosować odwrotność funkcji.
  Żadna z tych argumentacji nie wymaga T1
  poza normalnością w podanej w rozdziale konwencji.
- **06 — sieci, podsieci i filtry**:
  konstrukcja skierowanego zbioru
  \(E=\{(d,U):x_d\in U\}\) dla punktu
  skupienia sieci daje faktyczną podsieć zbieżną.
  W równoważności filtrów i sieci
  indeksy \((F,a)\), \(F\in\mathcal F,a\in F\)
  tworzą skierowaną rodzinę przez przecięcia F∩G.
  To, że zbieżność sieci wymusza F⊂U
  dla pewnego F z filtru, jest wykazane
  poprzez wszystkie indeksy (F,b) z b∈F,
  a nie sam jeden punkt a.

## Spójność i brak powtórzeń

01 definiuje bazy/podbazy i generowanie topologii;
02 wykorzystuje te aksjomaty do operacji na zbiorach;
03 bada ciągłość; 04 konstrukcje (iloczyn, suma rozłączna,
iloraz); 05 aksjomaty oddzielania i przedłużanie funkcji;
06 uogólnia zbieżność ciągów do sieci i filtrów.
W tym przekroju zakresy są logicznie rozdzielone.
Rzeczywiste porównanie całego materiału z
osobnymi skryptami wciąż wymaga kolejnych audytów.

## Wynik i ograniczenie

W przytoczonych dowodach nie znaleziono błędów matematycznych;
regresje strukturalne pełnej książki przechodzą.
Raport nie obejmuje kompletnego samodzielnego
odtworzenia wszystkich 77 dowodów w blokach 01–06,
ani wizualnej inspekcji każdego rysunku.
Nie podnosi statusu całego globalnego audytu do
„stabilny”. Następne bloki do sprawdzenia:
07–11, 12–17, 18–22 oraz porównanie między skryptami.
