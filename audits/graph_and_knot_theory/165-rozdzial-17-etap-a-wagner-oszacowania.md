# Audyt 165 — drukowany rozdział 17, etap A

Data: 2026-11-24. Poprzedni raport: 164.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 5467adfb381183eb3a9cf0d92895bd0d234ef5cf.
Commit regresji: 00042bb3f1245692af514191367493724775b6c3.

## Zmiany
- Wagner: jawna konstrukcja minora z subdywizji, bez utożsamiania wierzchołków rozgałęzienia.
- Kryterium stożka: uzasadnienie, dlaczego wybrana ściana staje się nieograniczoną i zachowuje wszystkie wierzchołki na brzegu.
- Triangulacja grafu zewnętrznie planarnego: rozwinięcie argumentu o przecinaniu się łuków z naprzemiennymi końcami.
- Lemat o małym stopniu: rozróżnienie liczby krawędzi grafu pierwotnego i uzupełnionego do spójnego.
- Zachowano 22 etykiety i 58 par poprawnie zagnieżdżonych środowisk; 16 różnych celów odsyłaczy znaleziono w rozdziałach 09–10.

## Rzeczywiste uruchomienia lokalne (Python / NetworkX 3.6.1)
Nowy test GKT-17-WAGNER-01: PASS atlas=209, planar=194, outer=123, planar_bound=190, bipartite_bound=57, outer_bound=121, equality=6. Niezależna enumeracja operacji minorowych i porównanie z testem planarności oraz stożka; sprawdzono ograniczenia także dla grafów niespójnych. Hash git uruchomionego pliku bbf69d196f167abb20c4c8b4a8135fce779d49d8 zgodny z repozytorium.
Ponownie uruchomiono trzy zapisane pliki o identycznych hashach z repozytorium:
- TREE-01: PASS 148264 przypisań, 361 par minorowych.
- SEP-01: PASS 335 separatorów, 2097 incydencji, 444 zejścia.
- FACE-01: PASS 2172 obchodów, 3721 sklejeń w wierzchołku, 6400 sklejeń wzdłuż krawędzi.
Ponownie uruchomiono lokalny skrypt recheck.py (hash cdae3b82b35e1c38553a132b1d503f8ae62f7862), równoważne implementacje OUTER-01 (3288,22,2650), KEMPE-01 (1016,750,377), KUR-01 (79471,15575,25872,38024;156,2196,1750,446) i przykład koła. Nie są to uruchomienia identycznych plików tych trzech testów. Wszystkie wyniki zgodne z wcześniejszymi raportami.
Testy skończone, nie formalizacja Lean.

## Bramka
pdflatex i latexmk dostępne, jednak rzeczywista próba git ls-remote zakończyła się błędem Could not resolve host: github.com. CI: puste listy statusów i dostępnych przebiegów PR. Pełny skład i oględziny PDF niewykonane. Etap A pozostaje OTWARTY.
Dalej: kontrola całościowa źródła po poprawkach, uruchomienie dokładnych wersji pozostałych trzech plików testów, próba składu z plików pobranych przez konektor (jeśli możliwe). Nie zamykać A bez wymaganej bramki.
