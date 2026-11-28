# Audyt 212 — drukowany rozdział 23, stabilizacja A: ogniwa i topologia ilorazu

Data: 2026-11-25. Kontynuacja 211 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/16-od-triangulacji-do-topologii-i-geometrii-rozmaitosci.tex.
Blob wejściowy b5d0b9c783dde066355ab85dde1eb038bf26c84e.
Korekta bcc60444c9a4e014d0a005870790ada86c09e99a, blob 3c9c08a9577bfbf20f7d2e173d5d9a8684a38c2f.

## Poprawki i kontrola
- GKT-23-LINK-02: w szczególnym modelu pełnego parowania boków i relacji generowanej wyłącznie przez sklejenia ogniwo każdej klasy wierzchołków jest automatycznie spójne. Każde naroże daje odcinek; ciąg identyfikacji naroży daje ciąg odcinków mających wspólne końce. Stopień dwa (z krotnościami) i spójność dają okrąg. Wzmocniono wypowiedź stwierdzenia, zachowując jej zakres. Wyjaśniono, że dodatkowe identyfikacje wierzchołków mogą dać niespójne ogniwo; dotychczasowy argument lokalnej homologii pozostawiono w tym kontekście.
- GKT-23-QUOTIENT-02: poprawiono zapis przekątnej (to {(x,x):x in X}, nie cały X x X). Wykazano otwartość i nasycenie sumy sektorów, opis parametru r=1-t_v, stożkowe współrzędne, zwartość i homeomorfizm domkniętych sektorów po sklejeniu, a następnie otwarte otoczenie stożkowe. Doprecyzowano krotności pętli grafu dualnego i odsyłacz do wcześniejszego rozdziału.
- GKT-23-HODGE-02: ustalono zwykły, nieuzupełniony kompleks i zerowe przestrzenie poza zakresem wymiarów; jawna definicja kohomologii oraz uzasadnienie dobrego określenia i liniowości mapy z kołańcuchów harmonicznych. Terminologia dodatnio określonych iloczynów skalarnych.
- Zachowano pięć etykiet i 13 poprawnie zagnieżdżonych par środowisk. Pierwszy zapis napotkał konflikt 409 równoczesnych zmian gałęzi; ponownie pobrano źródło i potwierdzono identyczny blob, następnie zapisano poprawki. Nie nadpisywano innych plików.

## Regresje
GKT-23-GLUE-01 PASS: 120 modeli, 222 ogniwa, 48 modeli z trzema równoległymi krawędziami.
GKT-23-HODGE-01 PASS: 196 zestawów Grama, 196 kontroli jądra cyklu, 196 odwracalnych laplasjanów pełnego trójkąta.
Nowy GKT-23-LINK-COMPONENTS-01, test_gkt23_link_components.js, commit 10ee441e6c16089747f5c9df0fd0047381dd4fdf. PASS: 480 deterministycznych prób pełnych parowań dla 2,4,6,8,12,20 trójkątów, 1836 ogniw, 1003 wystąpienia sklejeń boków tego samego trójkąta, 116 modeli z niespójnym grafem dualnym, 399 kontroli dodatkowego utożsamienia dwóch klas wierzchołków dającego ogniwo z dwóch okręgów. Sprawdzono stopień dwa, spójność ogniw i to, że klasy wierzchołków nie przecinają różnych składowych grafu dualnego. Próby nie są enumeracją klas izomorfizmu. Wszystkie trzy skrypty wykonano po odczycie z repozytorium w izolacie JS, nowy także przed zapisem. Nie potwierdzono wykonania w procesie Node ani integracji z CI; nie Lean.

## CI i PDF
Dla ad6fca17 terminologia 45585802574, algorytmy 45585802955, pełny audyt 45585802480 SUCCESS, aplikacja 45585802773 w toku przy pierwszej kontroli. Dla bcc60444: algorytmy 45586255911 i terminologia 45586255959 queued, aplikacja 45586255904 i pełny audyt 45586255906 w toku. Nie przeniesiono PASS ze starszego SHA. Nie oglądano PDF najnowszej wersji.
Etap A otwarty. Następny audyt 213: kontrola uzupełnionych dowodów, odsyłaczy, CI i rzeczywiste oględziny PDF. Bez niezatwierdzonych rozszerzeń. Postęp 22/44.
