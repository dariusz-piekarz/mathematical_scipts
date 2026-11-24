# Audyt 168 — drukowany rozdział 17, zakończenie etapu A

Data: 2026-11-24. Plan 118. Uwzględniono równoległe raporty 166 i 167, nie zmieniano ich.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Aktualny blob: cb06ea9d5c73fc5b1b9e0d3d3517a10b573f5d89, zgodny z commitem kompilacji 5467adfb381183eb3a9cf0d92895bd0d234ef5cf.
W tej iteracji nie zmieniano tekstu rozdziału; zamknięcie brakującej bramki.

## Rzeczywiste regresje: 12/12
Osiem lokalnych plików Python uruchomiono z NetworkX 3.6.1. Dla każdego git hash-object był identyczny z aktualnym blobem repozytorium:
- OUTER-01 adc59d4ba9a10116cd48747424de9c9021446879: PASS graphs=3288, triangulations=22, potential_drops=2650.
- KEMPE-01 d497c7b896d58892865146b343d502e53faf2baf: PASS planar=1016, swap13=750, swap24=377.
- KUR-01 55974646d55f3dd1a38a1df0755a5478fe84047f: PASS cyclic=79471, insertion=15575, common=25872, alternating=38024; three_connected=156, edges=2196, contractible=1750, noncontractible=446.
- TREE-01 7e2e6423cb6df21146c15cfea637e92ee575205c: PASS assignments=148264, stars=58726, splits=89538; minor_pairs=361, positive=169, negative=192.
- SEP-01 8e50d95b82e230af42ebec16e488e2182363facd: PASS graphs=156, separators=335, incidences=2097, descents=444, t_xy=354.
- FACE-01 9b1bb85463efe7875978df670e9d81263d433634: PASS biconnected=351, faces=2172, darts=7704, vertex_glues=3721, edge_glues=6400.
- WAGNER-01 bbf69d196f167abb20c4c8b4a8135fce779d49d8: PASS atlas=209, planar=194, outer=123, planar_bound=190, bipartite_bound=57, outer_bound=121, equality=6.
- OUTER-02 12e7ca27476b6a337e2f84a635f505eed97dbc65: PASS graphs=209, outer=123, connected_n_ge_3=66, equality=6, extra_edge_checks=453.

Cztery aktualne pliki JavaScript pobrano z repozytorium i wykonano w środowisku JS bez zmiany funkcji testowych; jedynie końcowe console.log zastąpiono przez return run():
- contraction_descent 37ce9db13ea0d9c9e0fe4700079972f7d8ca9167: PASS graphs=3902, edges=48996, descents=15449, outside=0.
- face_boundaries 1342529891d88d64161063f9438d0d7e770b56f7: PASS graphs=770, rotations=27959, planeEmbeddings=2397, biconnectedEmbeddings=700, bridgeChecks=13989.
- minor_subdivision 9caf5bb112b1326dffa03442bd557cc3e3ab9dd0: PASS models=3372, k5=751, k33=2621.
- tree_terminals e9406f52e7811135dd82f8b6fbe3cb9b896e9fbd: PASS trees=1442, cases=249963.

Nie sumowano nakładających się prób. Testy skończone, nie formalizacja Lean.

## CI i rzeczywisty PDF
Pobrano listę rzeczywistych przebiegów push przez GitHub API (wcześniejsze zapytanie ograniczone do PR nie znajdowało tych przebiegów).
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45483300188 : SUCCESS, structural-audit i full-book-pdf SUCCESS, w tym trzy kompilacje rzeczywistej książki.
- https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45483300063 : SUCCESS, dodatkowy audyt algorytmiczny.
- Artefakt 14963446684 graph-and-knot-complete-book-audit (ZIP 2807147 B) rzeczywiście pobrano przez konektor, rozpakowano i sprawdzono PDF 335 stron, 2448195 B. Plik graph_and_knot_full_warnings.txt ma 0 bajtów.
- Porównano bloby pliku głównego książki, poprzedniego rozdziału 09 oraz rozdziału 10 na commicie CI i na aktualnej gałęzi: wszystkie trzy identyczne. Nie jest to deklaracja identyczności całego HEAD z commitem CI.
- Wydzielono rozdział 17 (strony fizyczne PDF 142–155, drukowane 132–145). Wyrenderowano i obejrzano wszystkie 14 stron w czterech arkuszach; brak zauważonych kolizji, ucięć i problemów z rysunkiem Kempego. 22 etykiety i 58 par środowisk poprawnie zagnieżdżonych, sprawdzone ponownie.
- Lokalny git ls-remote nadal blokuje DNS, ale nie blokuje już weryfikacji: kompilacja odbyła się w CI, artefakt jest rzeczywisty.

## Decyzja
Etap A rozdziału 17 zamknięty dla wskazanego blobu. Wszystkie wymagane bramki tej iteracji potwierdzone; nie znaleziono otwartego istotnego błędu w dotychczasowych kontrolach. Kolejny krok: niezależny etap B tego samego rozdziału, bez rozszerzania zakresu, z ponowną kontrolą matematyczną, regresjami i PDF. Rozdział jako całość nie jest jeszcze zamknięty. Jeśli źródło zostanie zmienione, ponownie zweryfikować kompilację dla nowego blobu.
