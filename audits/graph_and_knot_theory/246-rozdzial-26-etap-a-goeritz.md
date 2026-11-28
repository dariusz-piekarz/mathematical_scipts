# Audyt 246 — rozdział drukowany 26, etap A (otwarty)

Data: 2026-11-25. Odczytano plan 118, raporty 244–245, catalog/books.json oraz pełne źródło pliku 19-grafy-taita-wielomian-tutte-a-i-macierze-goeritza.tex. Raport 245 zamyka rozdział 25; kolejność katalogowa potwierdza rozdział 26.

Poprawiono dwa błędy: pętle nie wnoszą wkładu do przekątnej podpisanego laplasjanu; jednakowe znaki krawędzi są wystarczające, ale nie konieczne dla równości modułu sumy ważonej i liczby drzew. Dodano dokładne kryterium i dowód przez liczby dodatnich i ujemnych iloczynów oraz kontrprzykład drzewa z mieszanymi wagami. Commit 747a1825add5cf9d211f78cdbae86152a4db5d3a.

GKT-26-SIGNED-TREES-01: trwały test test_gkt26_signed_trees.js, commit 37089ab281b672f13e48faee1d0de9b6f88c3deb. Wykonano równoważną kontrolę JS w pamięci: 729 konfiguracji wag -1,0,1 (zero oznacza brak krawędzi), trzy minory każdej macierzy, 2187 przypadków PASS. Porównano bezpośredni wyznacznik z enumeracją drzew oraz kryterium równości. Nie uruchomiono zapisanego pliku w Node ani nie potwierdzono jego integracji z CI. Nie jest to formalizacja Lean.

CI/PDF nowych commitów niezweryfikowane. Etap A pozostaje otwarty. Następny punkt: szczegółowy dowód kolorowania i dualności, lokalna zgodność wygładzeń w diagramie alternującym, konwencje Goeritza i odsyłacze, integracja regresji, CI i oględziny PDF. Postęp 25/44 według konwencji raportu 245. Nie zmieniano aplikacji ani innych gałęzi.
