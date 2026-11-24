# Audyt 161 — drukowany rozdział 17, etap A (kontynuacja)

Data: 2026-11-24. Plan 118, poprzedni raport 160.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 1057e0c87550117460aefde2379848e9df6df600.
Commit regresji: 1346f8e973adf890e316772625300a4d8caf6c62.

## Zmiany i kontrola
- Uściślono minimalność po kontrakcji, przynależność wnętrz usuniętych krawędzi do ściany i ich końców do cyklu brzegowego oraz dowód minimalnego stopnia.
- W kroku 4 uzasadniono podział dysku przez łuki i konstrukcję nowych krawędzi bez przecięć, także gdy k=2.
- W kroku 5 skonstruowano jawnie trzy rozłączne ścieżki cyklu; poprawiono przypisanie wniosku o subdywizji do G, a nie modelu minora.
- Ujednolicono pisownię Schoenfliesa z poprzednim rozdziałem.
- Zachowano 22 etykiety, sprawdzono zagnieżdżenie 57 środowisk. Wszystkie 14 różnych celów ref/eqref znaleziono w rozdziałach 09 i 10. Ponowny odczyt źródła i testu potwierdził zapis, także po konflikcie zapisu raportu z równoległym commitem analizy matematycznej.

## Regresje rzeczywiście uruchomione lokalnie
GKT-17-KUR-01 — test_gkt17_kuratowski.py (Python, NetworkX 3.6.1):
- PASS cyclic=79471, insertion=15575, common=25872, alternating=38024. Pary zbiorów X,Y o liczności co najmniej dwa na cyklach długości 3–8; sprawdzono alternatywę wstawienia, trzech wspólnych sąsiadów lub naprzemiennej czwórki.
- PASS three_connected=156, edges=2196, contractible=1750, noncontractible=446. Atlas grafów do siedmiu wierzchołków; sprawdzono równoważność kontraktowalności z brakiem separatora trójwierzchołkowego zawierającego końce krawędzi i istnienie krawędzi kontraktowalnej.
- Ponownie uruchomiono równoważne implementacje wcześniejszych regresji: OUTER-01 (3288 grafów, 22 triangulacje, 2650 spadków potencjału), KEMPE-01 (1016 grafów planarnych, 750 zamian 1–3, 377 zamian 2–4). Wyniki zgodne z raportami 159–160.
- Testy skończone, nie formalizacja Lean ani zastępstwo dowodu.

## Bramka stabilizacji
Statusy i przebiegi CI commitu źródłowego: puste listy, sukces niepotwierdzony. pdflatex i latexmk dostępne, ale git ls-remote nadal zwraca Could not resolve host: github.com. Nie wykonano nowej kompilacji rozdziału ani książki, nie obejrzano całego PDF. Etap A OTWARTY.
Punkt wznowienia: niezależna kontrola lematu o modelach minorów i etykietach drzewa oraz pełny skład i CI. Nie przechodzić do B przed spełnieniem bramki.
