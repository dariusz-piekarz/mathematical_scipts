# Audyt 171 — drukowany rozdział 18, etap A

2026-11-24. Plan 118; raport 170 zamyka rozdział 17. Kolejność potwierdzona w catalog/books.json.

Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.

- Poprawiono identyfikację ścian w konstrukcji wstęgowej: nie są jedynie wnętrzami doklejonych dysków.
- Zastąpiono nieuzasadniony argument o mostach dowodem przez zamknięty spacer i dwa boki krawędzi.
- Jawnie ustalono orientacje krawędzi oraz oznaczenie zbioru ścian.
- Commit źródłowy e0d1ced004cbbcfe2c633a091a33c767e97c0ce7; blob 4a8c0d4b8dee99f7f72a1df3aae08a29ab057a9e.
- GKT18-BRIDGE-01: niezależna enumeracja spójnych grafów prostych etykietowanych na 2–5 wierzchołkach, jeden ustalony układ rotacji na graf; 1067 przypadków mostów zaliczonych w wykonaniu JavaScript. Trwały odpowiednik testu zapisano w test_gkt18_bridge_faces.js, commit 3563b9f6d63ab813725458b3dd9ebd44a014a791. Nie potwierdzono jeszcze wykonania zapisanego pliku w CI.

CI i rzeczywisty PDF niezweryfikowane. Etap A otwarty. Wznowienie: audyt konstrukcji dualnej i homologii całkowitej, ocena uzupełnienia o drzewa pierwotne i dualne na powierzchniach, uruchomienie trwałych regresji oraz kontrola CI i PDF. Nie przechodzić do B przed stabilizacją.
