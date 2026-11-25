# Audyt 257 — rozdział 26 (TG19), kontrola C

Data: 2026-11-25. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Weryfikacja wersji po audycie 256

- Commit `e90a5b879f4c602e82b15d7a5498fc5cb01fb173`: pełny audyt tomu [45633311054](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45633311054) i audyt algorytmiczny [45633311008](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45633311008) zakończone sukcesem; sprawdzono poszczególne kroki.
- Artefakt 15032675741 zawiera PDF całego tomu: 363 strony A4; plik ostrzeżeń pusty. Obejrzano render stron fizycznych 235–241 (drukowanych 225–231), w tym zapis bibliograficzny poprawiony w audycie 256.
- Porównanie z `c6c7bafa820882d027f410eb798538f0cdc1d8f4`: brak późniejszych zmian w źródłach grafów i w odpowiadających workflow (jedynie raport audytu).

## Usterka wykryta podczas kontroli wizualnej C

Na stronie drukowanej 226 rysunek czarnego grafu Taita podpisany C_3 miał tylko dwie widoczne krawędzie; brakowało krawędzi zamykającej cykl. Powiększenie renderu potwierdziło usterkę. Poprzednia kontrola jej nie wykryła. Zastąpiono ścieżkę `(a)--(b)--(c)--cycle` trzema niezależnymi poleceniami TikZ rysującymi krawędzie a–b, b–c, c–a. Treść matematyczna i pozostałe elementy rysunku bez zmian.

Commit poprawki: `c7f869ae38d30ab8f298e2847f754d16c3fcc4c5`. Lokalna kompilacja odizolowanego poprawionego rysunku z oryginalnymi stylami i kodowaniem T1 zakończona sukcesem; oględziny renderu potwierdziły wszystkie trzy krawędzie trójkąta i trzy krawędzie równoległe grafu dualnego. Nie jest to jeszcze kontrola całego PDF po poprawce.

## Status

Nowy pełny CI [45634029595](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45634029595) oraz CI algorytmiczny [45634029795](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45634029795) były w toku w chwili sprawdzania. Kontrola C pozostaje otwarta do potwierdzenia obu CI i oględzin nowego PDF. Nie przechodzimy jeszcze do rozdziału 27.
