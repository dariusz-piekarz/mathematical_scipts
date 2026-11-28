# AM II 18 — Twierdzenie o funkcji odwrotnej

Data: 27.11.2026. Gałąź: biblioteka-matematyczna-iteracja-6.

## Trzeci audyt szczegółowy

Commit 795b033ada9b0090cbca8f6268c4c3d7273e5a81, blob 979ce760caa3040d2d0026bf7421553bf94b331c. Sześć poprawek: jednoznaczne odwołanie do kontrakcji, jawne działanie operatora odwrotnego przy drugiej pochodnej, rozwinięcie Taylora, rachunek pochodnych arctan i wyznacznika, oba kierunki monotoniczności oraz uzasadnienie gładkości odwrotności w przestrzeni Hilberta. Zachowano wszystkie 15 etykiet. Ponowny odczyt: 13/13 różnych wewnętrznych celów odsyłaczy w AM II oraz 3/3 celów FA-15 potwierdzone w źródłach. Stos środowisk LaTeX bez błędów. Stabilizacja 0/2 po zmianach; następne dwa pełne audyty bez usterek i niezależny audyt kontrolny.

## Plotly

Sprawdzono rzeczywiste pliki application/frontend/plots/am2-figures.js, viewer.js oraz application/frontend/preview.js. Dwanaście identyfikatorów figur ma odpowiadające wpisy w ATLAS_AM2_PLOTS, w tym AM2-18 -> am2_18_inverse.html. W definicji figury 18 są dwie powierzchnie v+u² i v-u² w oddzielnych scenach, zgodne z listingiem rozdziału. Podgląd tworzy adres viewer.html z identyfikatorem, a viewer.js wywołuje Plotly.newPlot z zarejestrowaną definicją. Jest to kontrola źródła, nie test renderowania w przeglądarce.

## Odbiór techniczny

Przebiegi dla commitu 795b033: AM II 46036866457 i 46036854360, AM I 46036866532, terminologia 46036854373, aplikacja 46036854439 — queued w chwili kontroli. Nie wykonano lokalnej kompilacji PDF ani testu przeglądarkowego. Odbiór pozostaje otwarty.

## Audyt stabilizacyjny I — 27.11.2026

Ponowny pełny odczyt źródła, blob 979ce760caa3040d2d0026bf7421553bf94b331c. Bez nowych usterek wymagających zmian.

- Lokalna odwracalność: sprawdzono zgodność hipotez z FA-15, typy operatorów, oszacowania na kuli domkniętej, warunek kontrakcji, przynależność punktu stałego do wnętrza, otwartość obrazu, sklejanie odwrotności, normę pochodnej i przypadek przestrzeni zerowej.
- Pochodne: sprawdzono obie kompozycje dające identyczność, kolejność czynników w drugiej pochodnej, normę dwuliniową, kryterium wyznacznika i rozwinięcie Taylora przykładu wielomianowego.
- Przykłady: sprawdzono oba złożenia ścinania parabolicznego i obraz brzegu kwadratu, periodyczność odwzorowania wykładniczo-biegunowego, dziedzinę gałęzi arctan i wszystkie elementy Jacobiego, iloraz różnicowy pierwiastka sześciennego, znaki pochodnych w kontrprzykładzie oraz dowód monotoniczności, rachunek Frécheta i promienie kul w przykładzie Hilberta.
- Odczytano pełne deklaracje sześciu przywołanych wyników AM II: ma2:thm:finite, ma2:thm:inverse-perturbation, ma2:thm:frechet-chain, ma2:thm:mean-value-inequality, ma2:prop:second-chain, ma2:thm:taylor-peano; zastosowania zgodne z hipotezami.
- Rozdział występuje dokładnie raz w books/pl/mathematical_analysis_ii.tex i catalog/books.json. Definicja dwóch powierzchni oraz powiązanie AM2-18 w preview.js nadal obecne. Geometria TikZ zgodna z obrazem kwadratu; bez kontroli składu PDF.

Stabilizacja merytoryczna 1/2. Pięć przebiegów CI wymienionych powyżej nadal queued w chwili odczytu. Nie deklaruje się odbioru technicznego ani wykonania testu renderowania.

## Audyt stabilizacyjny II — 27.11.2026

Ponowny przegląd wszystkich czterech sekcji niezmienionego źródła (blob 979ce760caa3040d2d0026bf7421553bf94b331c). Kontrola niezależnie od poprzedniego raportu: w oszacowaniu przyrostów sprawdzono znak obu nierówności i przypadek x=z, ostrą nierówność dla V_r i domkniętą kulę, działanie A i A^{-1} pomiędzy różnymi przestrzeniami, odwracalność I_E+(A^{-1}Df(x)-I_E), stałą Lipschitza i normę odwrotnej pochodnej. W przestrzeni zerowej wykluczono dzielenie przez normę zerową. W części o drugiej pochodnej zweryfikowano dziedziny wszystkich operatorów, znak oraz czynnik 1/2 w rozwinięciu Taylora. Kryterium euklidesowe i obie kompozycje w przykładach są poprawne. W kontrprzykładzie monotoniczności sprawdzono przypadki x<y<a, a<x<y, x<=a<=y oraz ciągi o pochodnych -1 i 3. W przykładzie Hilberta sprawdzono oszacowanie na brzegu kuli, 2r||v||=1/2, promień obrazu r/2, normę identyczności dla H != {0} i niezerowy punkt o obrazie 0. Nie stwierdzono nowych usterek wymagających zmian.

Kontrola strukturalna ponowiona: 15 unikalnych etykiet, 4 sekcje, poprawny stos środowisk. Odczytano dodatkowo viewer.html, trasę /api/plotly/bundle.js w backendzie i rzeczywisty test browser_reader_preview.py (wiersze 142–158): test obejmuje leniwe otwieranie, sandbox, data-ready, obecność kontenera WebGL, zamykanie i brak figury dla niewłaściwego rozdziału. Sam test nie został w tej iteracji uruchomiony; potwierdzono wyłącznie obecność i zakres testu w repozytorium.

Stabilizacja merytoryczna 2/2; wymagany audyt kontrolny. CI dla 795b033 nadal queued przy ostatnim odczycie; brak potwierdzenia aktualnego PDF i renderowania interaktywnego.

## Audyt kontrolny — 27.11.2026

Odczytano ponownie pełny rozdział, blob 979ce760caa3040d2d0026bf7421553bf94b331c. Zweryfikowano niezależnie od historii zmian: definicję dyfeomorfizmu, twierdzenie i oszacowania lokalne (w tym otwartość obrazu, istnienie i jednoznaczność punktu stałego), konieczność odwracalności pochodnej, wzór na drugą pochodną i jej normę, kryterium Jacobiego, przykład Taylora, obraz siatki przy ścinaniu, sklejanie odwrotności, przykład wykładniczo-biegunowy i jego gałąź odwrotną, pierwiastek sześcienny, kontrprzykład z nieciągłą pochodną i przykład Hilberta. Nie znaleziono nowych błędów merytorycznych ani luk wymagających zmiany źródła.

Automatyczna kontrola tekstowa na rzeczywiście pobranych plikach AM II 01, 07, 13–16, 18 i FA-15: każdy z 13 wewnętrznych oraz 3 zewnętrznych różnych celów odsyłaczy występuje dokładnie raz w sprawdzonych źródłach. 15 etykiet rozdziału, poprawne zagnieżdżenie środowisk, pojedynczy wpis w książce i katalogu. Nie zmieniano źródła ani definicji Plotly.

Stabilizacja merytoryczna 2/2 + audyt kontrolny: zaliczone. Odbiór techniczny pozostaje otwarty: pięć przebiegów dla 795b033 nadal queued przy ostatnim odczycie, brak aktualnego artefaktu PDF i wyniku testu przeglądarkowego. Nie jest to pełny odbiór rozdziału. Kolejny etap merytoryczny: AM II 19, twierdzenie o funkcji uwikłanej, z wykorzystaniem FA-15 i AM II 18 oraz repozytoryjną wizualizacją Plotly 3D.
