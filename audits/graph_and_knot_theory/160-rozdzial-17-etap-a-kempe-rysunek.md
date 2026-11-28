# Audyt 160 — drukowany rozdział 17, etap A (kontynuacja)

Data: 2026-11-24. Plan 118, poprzedni raport 159.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: be0a0c9fe39a89ac715a2c52afbb6602aa8f082a.
Commit regresji: b49aecf6e6908c412cabadcf400d92c812072d39.

## Zmiany
- Jawne ustalenie osadzenia i permutacji nazw kolorów.
- Pełne uzasadnienie poprawności zamiany kolorów na składowej: krawędzie wewnętrzne, zewnętrzne i przecinające jej granicę.
- Wybór ścieżki prostej i argument rozdzielenia sąsiadów przez krzywą Jordana; jawne zdefiniowanie H24 oraz druga zamiana.
- Zastąpienie rysunku konkretną ścieżką o kolorach 1,3,1,3 i pełną wyróżnioną krzywą Jordana. Wierzchołek v pozostaje niepokolorowany. Poprawiono odstęp od wierzchołka koloru 2 po obejrzeniu pierwszej wersji.
- Zachowano 22 etykiety; sprawdzono zagnieżdżenie 57 środowisk LaTeX. Ponowny odczyt źródła potwierdził poprawki.

## Testy
- GKT-17-KEMPE-01, test_gkt17_kempe.py, Python / NetworkX 3.6.1: rzeczywiste uruchomienie lokalne: PASS planar=1016, swap13=750, swap24=377. Atlas grafów do 7 wierzchołków; wszystkie poprawne kolorowania po usunięciu wierzchołka stopnia pięć z ustaloną permutacją kolorów sąsiadów. Weryfikacja poprawności przedłużenia w obu przypadkach. Test skończony, nie formalizacja Lean.
- GKT-17-OUTER-01: ponownie uruchomiony lokalnie kod równoważny zapisanej regresji: PASS graphs=3288, triangulations=22, potential_drops=2650.
- Rysunek: lokalna kompilacja pdflatex wyodrębnionego TikZ z ustawieniami książki, PDF rzeczywiście wyrenderowany i obejrzany; końcowa wersja bez nakładania wierzchołków, krawędzi i podpisu. Brak ostrzeżeń Overfull/Underfull w logu tego fragmentu. Nie jest to pełny PDF książki.

## Bramka stabilizacji
CI: zapytania o status i workflow commitu źródłowego zwracają puste listy. Pełny PDF: bezpośrednie pobranie repozytorium nadal blokuje DNS, nie przeprowadzono pełnej kompilacji ani oględzin całego rozdziału w książce. Etap A OTWARTY.
Punkt wznowienia: kontrola pozostałych zależności dowodu Kuratowskiego, pełna kompilacja książki i kontrola PDF/CI; dopiero po spełnieniu bramki etap B rozdziału 17.
