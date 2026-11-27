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
