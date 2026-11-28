 # Rozdział 37 — audyt indywidualny 01

2026-11-24. Drukowany rozdział 6, po zamknięciu 05. Audyt źródła BFS/DFS, kolejki, lasu, mostów, artykulacji, multigrafów i DAG. Poprawiono zakres zegara do 2n, pętlę BFS, dowód braku nieskierowanego cyklu przez maksimum odległości, jednokrotną inicjalizację tablic oraz liniową konstrukcję porządku topologicznego przez odwrócenie listy wyjść. Źródło: 1efec1dfd0ca43e2fd0ea53d5c9d831170dc1573.

Regresje TG37-CLOCK-01 i TG37-ORDER-01 w tools/tests/test_graph_and_knot_bfs_dfs.py (72662a7d2eb8ef6e769a6ca4bcb39ff8cd260481): pełny zakres różnych czasów oraz liniowy odczyt według czasów wyjścia i sprawdzenie wszystkich łuków DAG. Testy zmodyfikowane, wynik uruchomienia niepotwierdzony. Kontrola PDF i CI pozostają otwarte.

Propozycja po pierwszym audycie: jawny pseudokod iteracyjnego DFS z ramkami stosu i kontrprzykład dla naiwnego stosu wierzchołków; ewentualnie algorytm silnie spójnych składowych tylko po sprawdzeniu pokrycia w pozostałych rozdziałach i akceptacji. Bez samowolnego rozszerzania po tym etapie. Status OTWARTY.
