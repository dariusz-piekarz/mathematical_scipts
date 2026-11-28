# Audyt 164 — drukowany rozdział 17, etap A

Data: 2026-11-24. Poprzedni raport: 163.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 75e11545ca174d1b77c590801a1debdccb8220b2.
Commit regresji: 7a9f43ac176517319f2b33d64186ee2190615e5f.

## Audyt matematyczny
- Uściślono konstrukcję dysku pomocniczego przy krawędzi, także przy moście, oraz zgodność homeomorfizmów na całej wspólnej średnicy.
- Uzasadniono różność sektorów odpowiadających powtórzonym wystąpieniom wierzchołka w obchodzie.
- Jawnie wykorzystano zwartość łączącego łuku do wyboru małego otoczenia wierzchołka, w którym krzywa Jordana składa się z dwóch promieni; uzasadniono przynależność końców krawędzi do przeciwnych składowych dopełnienia.
- Rozpisano oba przypadki ewentualnej części grafu wewnątrz dysku ograniczonego cyklem: obecność wierzchołka i obecność wnętrza cięciwy.
- Poprawiono język; zachowano zakres rozdziału, 22 etykiety i poprawne zagnieżdżenie 58 środowisk. Wszystkie 16 różnych celów ref/eqref znaleziono w rozdziałach 09–10. Ponowny odczyt źródła potwierdził blob f89237095b109d31f0f2f5ca3f1e4cf062684882.

## GKT-17-FACE-01
Plik test_gkt17_gluing_faces.py, rzeczywiste uruchomienie Python / NetworkX 3.6.1:
PASS biconnected=351, faces=2172, darts=7704, vertex_glues=3721, edge_glues=6400.
Sprawdzono prostotę obchodów i wzór Eulera dla osadzeń zwracanych przez NetworkX grafów dwuspójnych z atlasu do siedmiu wierzchołków. Sprawdzono też sklejenia wszystkich par grafów atlasu o 1–4 wierzchołkach przy wszystkich wyborach punktów sklejenia (wzdłuż krawędzi także po usunięciu krawędzi pomocniczej). Hash git lokalnie uruchomionego pliku 9b1bb85463efe7875978df670e9d81263d433634 jest identyczny z blobem pobranym po zapisie. To testy skończone; nie dowodzą twierdzeń topologicznych ani nie obejmują wszystkich osadzeń. Poprzednie regresje nie były ponownie uruchamiane w tej iteracji.

## Bramka
pdflatex i latexmk są dostępne. Próba git ls-remote rzeczywiście zakończyła się błędem DNS Could not resolve host: github.com. Brak pełnej kompilacji i oględzin PDF. Zapytanie o łączny status commitu źródłowego zwróciło pustą listę, nie potwierdzono CI. Etap A otwarty.
Punkt wznowienia: kontrola wszystkich pozostałych twierdzeń rozdziału (Wagner, oszacowania planarności i zewnętrznej planarności), uruchomienie pełnego zestawu regresji i uzyskanie pełnego składu/CI. Bez spełnienia bramki nie przechodzić do etapu B.
