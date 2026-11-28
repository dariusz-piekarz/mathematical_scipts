# Audyt 167 — drukowany rozdział 17, etap A (kontynuacja)

2026-11-24. Plan 118, poprzedni raport 166.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 311f777945af4022742d4fb85db2856651446431.
Blob: 592e56045757749df58cb7fadfc3ee51fbe984f3.

## Zmiany
- Dziewięć punktowych korekt: jednoznaczne określenie grafów G,H w definicji podgrafu topologicznego, dopuszczenie pustego ciągu podziałów oraz izomorfizmu; uzasadnienie cofnięcia podziału.
- Definicja minora przez izomorfizm, usuwanie wierzchołka z incydentnymi krawędziami, kontrakcje wyłącznie krawędzi o różnych końcach, dopuszczenie pustego ciągu operacji, rozróżnienie grafów pośrednich i uproszczonego grafu G/xy.
- Doprecyzowanie dowodu zachowania planarności przy kontrakcji i jego zależności od regularnego otoczenia.
- W dowodzie pięciokolorowalności: dowolny wolny kolor, ustalenie osadzenia przed numeracją sąsiadów, jawna sprzeczność między rozłącznością podgrafów i przecięciem ich obrazów.
- Zachowano 22 etykiety i poprawne zagnieżdżenie 57 par środowisk; 35 wystąpień odsyłaczy ma odpowiadające etykiety w bieżącym lub poprzednim rozdziale. Ponowny odczyt źródła potwierdził zmiany.
- Bez nowego testu: wykorzystano komplet ośmiu istniejących regresji dla zmienianych definicji i dowodów.

## Rzeczywiście ponowione regresje (8/8)
Python 3 / NetworkX 3.6.1, lokalne pliki o git hash-object identycznym z blobem na gałęzi:
- test_gkt17_kempe.py, d497c7b896d58892865146b343d502e53faf2baf: PASS planar=1016, swap13=750, swap24=377.
- test_gkt17_outerplanar.py, adc59d4ba9a10116cd48747424de9c9021446879: PASS graphs=3288, triangulations=22, potential_drops=2650.
- test_gkt17_kuratowski.py, 55974646d55f3dd1a38a1df0755a5478fe84047f: PASS cyclic=79471, three_connected=156, edges=2196, contractible=1750, noncontractible=446.
- test_gkt17_outer_criteria.py, 12e7ca27476b6a337e2f84a635f505eed97dbc65: PASS graphs=209, outer=123, connected_n_ge_3=66, equality=6, extra_edge_checks=453.

JavaScript: odczytano aktualne bloby z gałęzi i wykonano ich funkcje run bez modyfikacji treści funkcji (zastąpiono wyłącznie wywołanie console.log przez return):
- test_gkt17_contraction_descent.js, 37ce9db13ea0d9c9e0fe4700079972f7d8ca9167: PASS graphs=3902, edges=48996, descents=15449, outside=0.
- test_gkt17_tree_terminals.js, e9406f52e7811135dd82f8b6fbe3cb9b896e9fbd: PASS trees=1442, cases=249963.
- test_gkt17_minor_subdivision.js, 9caf5bb112b1326dffa03442bd557cc3e3ab9dd0: PASS models=3372, k5=751, k33=2621.
- test_gkt17_face_boundaries.js, 1342529891d88d64161063f9438d0d7e770b56f7: PASS graphs=770, rotations=27959, planeEmbeddings=2397, biconnectedEmbeddings=700, bridgeChecks=13989.

Testy skończone, nie formalizacja Lean. Nie sumujemy liczebności nakładających się prób.

## Stabilizacja
CI: zapytania o status i przebiegi dla ostatniego commitu zwracają puste listy; zapytanie o przebiegi ograniczone do PR nie wyklucza innych uruchomień. Lokalny pdflatex i node dostępne, rzeczywisty git ls-remote zakończył się błędem Could not resolve host: github.com. Odczyt pojedynczych plików przez konektor działa, ale brak automatycznego przekazania kompletnego drzewa źródeł do lokalnej kompilacji. Nie zbudowano pełnego PDF ani nie sprawdzono jego wyglądu. Etap A OTWARTY.
Wznowienie: priorytet pełny skład książki i oględziny stron rozdziału, kontrola CI; jeśli konieczne, przygotowanie lokalnej kompilacji wycinka z rzeczywistą preambułą, jawnie odróżnionej od pełnej kompilacji. Dopiero po spełnieniu bramki etap B tego samego rozdziału.
