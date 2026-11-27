# GT — audyt szczegółowy 330

GT01: sprawdzono dowody rachunku dopełnienia, potęg macierzy sąsiedztwa, wzoru na liczbę trójkątów, usuwania zamkniętych fragmentów spaceru, metryki grafowej, lematu o nieparzystym spacerze i kryterium dwudzielności. Nie wykryto nowych luk w tych fragmentach.

GT02: sprawdzono charakteryzacje drzewa i lasu rozpinającego, BFS i jednoznaczność rodzica, kryterium mostu, dualność fundamentalną, współrzędne przestrzeni cykli i zmianę liczby cyklomatycznej. Ujednolicono 17 wystąpień funkcji charakterystycznych na chi, doprecyzowano że chi_C oznacza funkcję zbioru krawędzi cyklu. Commity dac4434cd2b589f484ef00a2d64084854702463c i 88c8c09489afb2acdc68df36bf6658df7ace57d2; końcowy blob ab7fd76672d38ececa2b5e843d09775f7e24fd42.

GT03: sprawdzono dowody nieskierowanego obiegu Eulera i wplatania obiegów Hierholzera, skierowanego obiegu i otwartego szlaku oraz orientacji eulerowskiej. Doprecyzowano że słaba spójność nośnika wraz z równowagą stopni wymusza silną spójność nośnika, i wyjaśniono liniową złożoność skierowanej wersji Hierholzera, z uwzględnieniem pętli i krotności łuków. Commit 34dc8b083d8f1472fb4f219cdf6863165b1372e0, blob 9e233172de95e6f288a61fce913adde0af11d98f.

Walidacja: enumeracja 19764 niepustych skierowanych multigrafów na 1..3 wierzchołkach z każdą krotnością łuku od 0 do 2, w tym 1110 spełniających warunki zamkniętego obiegu. Niezależny wariant stosowy Hierholzera dał 1110/1110 poprawnych zamkniętych szlaków z dokładną krotnością każdego łuku. Nie jest to test wydajności implementacji listowej ani dowód konieczności warunków. Etykieta thm:tg-euler-directed-circuit unikatowa, środowiska zmienionych źródeł poprawnie zagnieżdżone, oba końcowe bloby potwierdzone. Konflikt zapisu rozwiązano po odświeżeniu źródła. Nie uruchomiono pełnej suity ani kompilacji.

CI: pełne 45989056077, algorytmy 45989055886, aplikacja 45989055876, terminologia 45989056112 — queued przy odczycie. Brak odbioru PDF. Następny etap: GT04–06, szczegółowa kontrola dowodów nieobjętych dotychczasową kontrolą, w tym twierdzenia Berge'a, Diraca i Ore'a oraz całkowitej unimodularności.
