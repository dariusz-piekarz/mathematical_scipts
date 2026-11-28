# Audyt 186 — drukowany rozdział 19, niezależny etap B

Data: 2026-11-25. Po zamknięciu A w audycie 185.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Blob wejściowy 2472339133f7c28a618e3fd47dbbc1ba46658755.
Korekta bdd1587f6b5465ce720ccd8f2bb2ed89a96f7e96, blob 1902a533a76e3e5d1110908ba74789303e064dde.

## Niezależny przegląd
- GKT-19-B-FOREST-01 (kontrola semantyczna): jawnie rozróżniono wystąpienia krawędzi oraz cykle długości 1 i 2. Twierdzenie thm:tg-las-rozpinajacy dotyczy grafów prostych; teraz las multigrafu konstruowany przez usunięcie pętli, sklejenie krawędzi równoległych w graf prosty i wybór reprezentantów krawędzi lasu. Sprawdzić zachowanie składowych, rozróżnialność kopii, n=0 i brak cykli. Wykazano zgodność z definicjami z rozdziału źródłowego 02.
- GKT-19-B-REC-01: dopisano argument zachowania składowych przy kontrakcji krawędzi już należącej do podgrafu oraz rozłączności końców mostu w każdym podzbiorze bez niego. Sprawdzono wszystkie trzy rekurencje, w tym brak ujemnych wykładników i liczenie kopii pętli.
- GKT-19-B-CHROM-01 (semantyczna): dodano jednoznaczność wielomianu chromatycznego jako wielomianu zgodnego z liczbą kolorowań dla wszystkich dodatnich całkowitych q; różnica ma nieskończenie wiele pierwiastków. Sprawdzono rachunek znaku i graf zerowy.
- GKT-19-B-CELL-01 (semantyczna): oba twierdzenia dualności wymagają komórkowości. Dla spójnego zanurzenia w sferze wynika ona z argumentu o regularnym otoczeniu w thm:tg-euler-plane (rozdział źródłowy 09): spójne otoczenie ma dopełnienie złożone z dysków; każdy dysk z półotwartym kołnierzem jest otwartym dyskiem. Dodano ten argument i odsyłacz do konstrukcji dualnej w rozdziale 18. Sprawdzić również przypadek jednego wierzchołka.
- Doprecyzowano całkowitość q oraz bijekcję zbioru kolorów z Z/qZ w dowodzie przepływów. Sprawdzono konwencję znaku D=-d2 i zastosowanie drzewa dualnego z rozdziału 18. Nie dzielimy przez elementy pierścienia. Nie zmieniono wyniku twierdzenia.
- Ponownie przejrzano przykłady, specjalizacje, ważony Kirchhoff, dowód przez dopełniające zbiory i przepływy. Nie dodano proponowanego ogólnego wielomianu przepływów ani nowego zakresu.
- Zachowano 12 etykiet i 32 poprawnie zagnieżdżone pary środowisk.

## Regresje
Cztery zapisane skrypty pobrano i wykonano po korekcie w izolacie JS:
REC-01 PASS (3528 grafów, 15855 rekurencji, 14112 porównań kolorowań);
DUAL-01 PASS (453 sferyczne układy, 3533 par podzbiorów, 1812 porównań);
KIRCH-01 PASS (3532 dokładne minory);
LIFT-01 PASS (8791 kolumn, 216466 rekonstrukcji, 178826 dla złożonych q).
Próby skończone częściowo pokrywające się, nie formalizacja Lean. Kryteria semantyczne zapisane powyżej nie są testami automatycznymi; testów nie uruchamiano w procesie Node.

## Bramka
Dla nowego SHA przy kontroli: algorytmy 45570370580, pełny audyt 45570370695, terminologia 45570370783, aplikacja 45570370627 — w toku. Nie oglądano nowego PDF. Etap B otwarty do ponownej stabilizacji i kontroli układu stron. Nie przechodzimy do rozdziału 20.
