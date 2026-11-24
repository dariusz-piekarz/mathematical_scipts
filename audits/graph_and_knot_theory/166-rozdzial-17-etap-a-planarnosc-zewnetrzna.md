# Audyt 166 — drukowany rozdział 17, etap A (kontynuacja)

2026-11-24. Plan 118, poprzedni raport 165.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: 1aea6e77b1d2127401a473a12262052942090f2d.
Commit regresji: dfd37983f13f2c7e8a1a029549aed6c85874139f.

## Zmiany
- Dwanaście punktowych zmian: jawne przypadki grafu bez wierzchołków i składowych jednoelementowych, dziedziczenie osadzenia przez składowe, sklejanie rozszerzeń, wybór punktu w nieskończoności.
- W kryterium zakazanych minorów uzasadniono zachowanie spójności zbiorów rozgałęzienia i świadków krawędzi po usunięciu wierzchołka p.
- Wzmocniono twierdzenie o liczbie krawędzi: dla spójnego grafu o n>=3 równość m=2n-3 odpowiada triangulacji dysku z wszystkimi wierzchołkami na brzegu; dowód obu kierunków i maksymalności uzupełnienia.
- Dodano jawny odsyłacz do lematu o brzegach ścian, ograniczenie definicji liczby chromatycznej do grafów skończonych, uzasadnienie dziedziczenia zewnętrznej planarności przez G-v.
- Zachowano 22 etykiety i 57 poprawnie zagnieżdżonych par środowisk. Wszystkie 34 wystąpienia odsyłaczy rozstrzygnięto w bieżącym i poprzednim rozdziale.

## Regresje
- GKT-17-OUTER-02: test_gkt17_outer_criteria.py. Rzeczywiste wykonanie Python/NetworkX 3.6.1: PASS graphs=209, outer=123, connected_n_ge_3=66, equality=6, extra_edge_checks=453. Trzy niezależne metody: permutacje porządku kołowego i test przecięć cięciw, planarna stożkowa nadbudowa, rekurencyjne kontrakcje do zakazanych minorów (test nieindukowanego podgrafu). Dodatkowo test zachłannego kolorowania i maksymalności przez dodanie każdej brakującej krawędzi. Lokalny git hash-object jest identyczny z blobem zapisanego testu: 12e7ca27476b6a337e2f84a635f505eed97dbc65.
- Ponowne wykonanie równoważnych lokalnych implementacji OUTER-01: PASS 3288 grafów, 22 triangulacje, 2650 spadków potencjału; KEMPE-01: PASS 1016 grafów, 750 i 377 zamian. Nie uruchamiano pozostałych starszych regresji.
- Testy skończone, nie formalizacja Lean i nie zastępują dowodów.

## Stabilizacja
CI: puste listy statusów i workflow dla commitu źródłowego. Lokalny pdflatex dostępny; rzeczywista próba git ls-remote zwróciła Could not resolve host: github.com. Pełnej kompilacji i PDF nie zweryfikowano. Etap A OTWARTY.
Wznowienie: sprawdzić terminologię i pozostałe drobne niejasności w całym rozdziale, ponowić resztę regresji, następnie pełna kompilacja i CI/PDF. Dopiero po spełnieniu bramki niezależny etap B.
