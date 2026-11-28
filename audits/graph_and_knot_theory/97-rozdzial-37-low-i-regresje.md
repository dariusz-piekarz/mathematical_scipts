# Rozdział 37 — audyt indywidualny 02

2026-11-24. Poprzednie regresje (72662a7): przebieg 45374395899, finite-models 138376597623 i chapter-pdf 138376598033 completed/success; krok exhaustive BFS/DFS/DAG/bridges/catalog success. Pełny audyt źródła 1efec1d: 45374365934 success. Nie oznacza to wizualnej kontroli PDF.

Poprawki 54f7ee09b2b321b672f2b98db86a8abfc9a253c8: wykluczenie rodzica w rekurencji low dla grafu prostego, dowód równoważności definicji i rekurencji, uzasadnienie acykliczności nieskierowanego lasu DFS oraz monotoniczności kolejnych odczytów BFS. Istotny błąd: bez wyłączenia krawędzi rodzica nawet pojedyncza krawędź mogłaby nie zostać uznana za most.

TG37-LOW-01 (7643fecbb0873ed6fb9da7844ce3bc18fb399dc4): niezależna enumeracja potomków i krawędzi niedrzewowych do przodków, porównanie z low obliczanym rekurencyjnie dla wszystkich grafów prostych w istniejącym teście. Wynik nowego przebiegu jeszcze niepotwierdzony. Następnie sprawdzić CI i PDF oraz dowody artykulacji, multigrafów i konstrukcje. Bez nowych rozszerzeń bez akceptacji. Status OTWARTY.
