# Audyt 232 — drukowany rozdział 25, etap A: warkocze, Schubert, węzły torusowe

Data: 2026-11-25. Kontynuacja 231.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex.
Blob wejściowy 9923272820507d4e46fdc9570aa62c0534499f94.

## Poprawki
Odczytano wszystkie końcowe sekcje rozdziału. Doprecyzowano standardowe domknięcie warkocza i wykazano zależność liczby składowych od cykli permutacji. Uzupełniono brakujące odcinki domknięć na rysunku trójlistnika i splotu Hopfa. Suma spójna zdefiniowana przez standardowe sklejenie sfer brzegowych zamiast dowolnych łuków; jawnie wskazano przyjmowany lemat o niezależności konstrukcji. Uzasadniono blokową postać macierzy Seiferta sumy spójnej. W dowodzie addytywności rodzaju zastąpiono nieuzasadnioną izotopię dysków operacją wymiany dysku z zachowaniem rodzaju i brzegu, bez założenia pustego wnętrza kuli. Wyprowadzono wielomian Alexandera węzła torusowego przez rachunek Foxa z niejednakowymi obrazami generatorów, jądro operatora brzegowego, podzielność w pierścieniu Laurenta, stopień i wyraz stały ilorazu. Rozpisano prezentację modułu z monodromii, poprawiono terminologię współczynników skrajnych. Twierdzenia Alexandra, Markowa, Artina, Schuberta i rozwłóknienie Milnora pozostają wynikami z literatury lub przedstawionymi zarysami, nie pełnymi własnymi dowodami.
Commit ce010c15e9429f48e77331bb199375944ea15a01; blob 08aa394e69c5136c3f0d1203329b9bff6aa48b99.

## Testy i struktura
GKT-25-TORUS-FOX-01: rzeczywiście wykonano samodzielny test Python z arytmetyką całkowitą, 216 uporządkowanych względnie pierwszych par p,q z zakresu 2–20. PASS: dzielenie bez reszty, obie współrzędne operatora Foxa, stopień, skrajne współczynniki, symetria i wartość w 1. Test trwale dodano do tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py, commit 8f5159ac558cb3d00ea695a972dbb7c3d80f3dbd, blob 36d6995405463a2dbbd82d890fe3c0e1d2386636. Ponowny odczyt potwierdził wywołanie w __main__. Test skończony, nie dowód ogólny ani formalizacja Lean.
Kontrola bieżącego rozdziału: 170 poprawnie zagnieżdżonych par środowisk, 21 unikatowych etykiet, 8 odsyłaczy, wszystkie cele istnieją w tym samym rozdziale.

## Bramki
Poprzedni run 45596077674: full-book-pdf completed/success, structural-audit queued. Nowy run 45596400156 dla 8f5159ac queued przy odczycie. Nie wykonano nowych oględzin PDF ani całego zintegrowanego pliku testowego lokalnie.
Zakończono pierwsze przejście merytoryczne A, ale nie stabilizację. Kolejne bramki w wymaganej kolejności: końcowa kontrola strukturalna całego tomu; końcowy CI dla stabilizowanej wersji; końcowa kontrola wizualna PDF; niezależny audyt kontrolny; pełna stabilizacja wyłącznie po spełnieniu wszystkich kryteriów. Ewentualny błąd oznacza poprawkę i ponowienie odpowiednich kontroli, nie rozszerzenie materiału. Postęp 24/44.
