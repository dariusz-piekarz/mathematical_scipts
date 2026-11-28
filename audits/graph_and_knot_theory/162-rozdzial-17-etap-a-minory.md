# Audyt 162 — drukowany rozdział 17, etap A

Data: 2026-11-24. Kontynuacja kontroli dowodu Kuratowskiego.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: fb3fe1156c3a16721ecd0c4906dec13537b2f97d.
Commit testu: 82e9409a7e37e61aa9041808441dac15bb4011a7.

## Audyt matematyczny
- Jawnie usuwamy krawędzie między zbiorami odpowiadającymi nieprzylegającym wierzchołkom H. Model nie jest modelem podgrafu indukowanego.
- Dowód równoważności modelu i minora: trzy niezmienniki, w tym niepustość i parami rozłączność zbiorów pierwotnych wierzchołków.
- Lemat o etykietach drzewa: jawne liczenie wielokrotnych etykiet na wspólnym wierzchołku, dowód jedyności krawędzi łączącej składową T-z z z, uzasadnienie ograniczenia liczby etykiet w składowej.
- Przejście od modelu K5 do K3,3: jawny odsyłacz do równoważności modelu i minora oraz użycie wcześniejszego przypadku lematu, a nie twierdzenia Kuratowskiego.
- Zachowano 22 etykiety, poprawne zagnieżdżenie 57 środowisk; ponowny odczyt źródła potwierdził zapis. Zachowano zastany blob źródłowy 592e56045757749df58cb7fadfc3ee51fbe984f3 jako podstawę edycji.

## Regresja GKT-17-TREE-01
Plik: test_gkt17_tree_minors.py. Rzeczywiste uruchomienie lokalne Python / NetworkX 3.6.1:
- PASS assignments=148264, stars=58726, splits=89538. Wszystkie przypisania trzech lub czterech różnych etykiet do wierzchołków wszystkich nieizomorficznych drzew o 1–8 wierzchołkach, z dopuszczeniem powtórzeń wierzchołków.
- PASS minor_pairs=361, positive=169, negative=192. Porównanie niezależnego przeszukiwania operacji usuwania i kontrakcji z enumeracją zbiorów rozgałęzienia dla par grafów prostych do czterech wierzchołków.
- Git hash-object lokalnie uruchomionego pliku: 7e2e6423cb6df21146c15cfea637e92ee575205c, zgodny z blobem repozytorium.
- Test skończony, nie formalizacja Lean. Poprzednich regresji nie uruchomiono ponownie w tej iteracji.

## Bramka
pdflatex dostępny; git ls-remote rzeczywiście zakończył się błędem Could not resolve host: github.com. Pełna kompilacja i oględziny PDF niewykonane. Statusy CI i dostępna lista przebiegów dla commitu źródłowego puste. Etap A otwarty. Dalej: kontrola lematu o kontrakcji i separatorach, ponowne uruchomienie kompletu regresji oraz próba pełnego składu. Nie zamykać A bez spełnienia bramki.
