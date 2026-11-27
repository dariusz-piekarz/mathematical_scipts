# AM II 18 — Twierdzenie o funkcji odwrotnej

Data: 27.11.2026. Gałąź: biblioteka-matematyczna-iteracja-6.

## Trzeci audyt szczegółowy

Commit 795b033ada9b0090cbca8f6268c4c3d7273e5a81, blob 979ce760caa3040d2d0026bf7421553bf94b331c. Sześć poprawek: jednoznaczne odwołanie do kontrakcji, jawne działanie operatora odwrotnego przy drugiej pochodnej, rozwinięcie Taylora, rachunek pochodnych arctan i wyznacznika, oba kierunki monotoniczności oraz uzasadnienie gładkości odwrotności w przestrzeni Hilberta. Zachowano wszystkie 15 etykiet. Ponowny odczyt: 13/13 różnych wewnętrznych celów odsyłaczy w AM II oraz 3/3 celów FA-15 potwierdzone w źródłach. Stos środowisk LaTeX bez błędów. Stabilizacja 0/2 po zmianach; następne dwa pełne audyty bez usterek i niezależny audyt kontrolny.

## Plotly

Sprawdzono rzeczywiste pliki application/frontend/plots/am2-figures.js, viewer.js oraz application/frontend/preview.js. Dwanaście identyfikatorów figur ma odpowiadające wpisy w ATLAS_AM2_PLOTS, w tym AM2-18 -> am2_18_inverse.html. W definicji figury 18 są dwie powierzchnie v+u² i v-u² w oddzielnych scenach, zgodne z listingiem rozdziału. Podgląd tworzy adres viewer.html z identyfikatorem, a viewer.js wywołuje Plotly.newPlot z zarejestrowaną definicją. Jest to kontrola źródła, nie test renderowania w przeglądarce.

## Odbiór techniczny

Przebiegi dla commitu 795b033: AM II 46036866457 i 46036854360, AM I 46036866532, terminologia 46036854373, aplikacja 46036854439 — queued w chwili kontroli. Nie wykonano lokalnej kompilacji PDF ani testu przeglądarkowego. Odbiór pozostaje otwarty.
