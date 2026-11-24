# Audyt 163 — drukowany rozdział 17, etap A

Data: 2026-11-24. Poprzedni raport: 162.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: fd38b108c65862578b350ac68931d5f6270d1fa0.
Commit regresji: 215cccf8a4db9b9c419ac589bffaf2575979c00e.

## Audyt matematyczny
- Jawne uzasadnienie, że wszystkie krawędzie wychodzące ze składowej po usunięciu separatora prowadzą do separatora.
- Uzasadnienie zachowania spójności po kontrakcji za pomocą obrazów ścieżek oraz niepustości rodziny trójek minimalizowanej w dowodzie.
- Wybór składowej D bez x,y,z i jawna inkluzja D w C bez w; uwzględniono przypadek jednoelementowej C.
- Nowy przykład grafu kołowego na pięciu wierzchołkach: kontrakcja krawędzi cyklu daje K4, kontrakcja krawędzi łączącej środek z cyklem nie zachowuje trójspójności.
- 22 etykiety zachowane, 58 środowisk poprawnie zagnieżdżonych, 16 różnych celów ref/eqref odnalezionych w rozdziałach 09 i 10. Ponowny odczyt źródła potwierdził zapis.

## Rzeczywiste uruchomienia lokalne (Python, NetworkX 3.6.1)
- GKT-17-SEP-01: PASS graphs=156, separators=335, incidences=2097, descents=444, t_xy=354. Enumeracja separatorów trójelementowych i konfiguracji kroku zejścia; obejmuje też przypadek t=x lub t=y. Blob uruchomionego pliku 8e50d95b82e230af42ebec16e488e2182363facd zgodny z repozytorium.
- GKT-17-TREE-01: PASS assignments=148264, stars=58726, splits=89538; minor_pairs=361, positive=169, negative=192.
- Równoważne implementacje trzech poprzednich regresji uruchomione ponownie: OUTER-01 (3288, 22, 2650), KEMPE-01 (1016, 750, 377), KUR-01 (79471, 15575, 25872, 38024; 156, 2196, 1750, 446). Wyniki zgodne z wcześniejszymi raportami. Nie były to uruchomienia pobranych bezpośrednio plików tych trzech testów.
- Dodatkowo sprawdzono obliczeniowo trójspójność grafu kołowego oraz obie kontrakcje z nowego przykładu.
- Testy skończone, nie formalizacja Lean.

## Bramka
pdflatex i latexmk dostępne. Ponowna próba git ls-remote zakończyła się błędem Could not resolve host: github.com. Pełna kompilacja oraz oględziny PDF niewykonane. Zapytania o statusy i przebiegi dla commitu źródłowego zwróciły puste listy (dostępne zapytanie o workflow ogranicza się do przebiegów PR); brak potwierdzenia CI. Etap A otwarty.
Dalej: kontrola sklejania osadzeń wzdłuż krawędzi i własności ścian, a następnie pełny skład/CI. Nie przechodzić do B przed spełnieniem bramki.
