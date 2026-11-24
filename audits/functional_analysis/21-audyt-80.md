# Rozdział 21 — audyt 80 (5/5 podsekcji, etap poprawkowy)

24 listopada 2026. Wyłącznie gałąź biblioteka-matematyczna-iteracja-6.

## Zmiany
Uzupełniono ostatnie dwie podsekcje: dowód gładkości przez ilorazy różnicowe w seminormach o wspólnym zwartym nośniku; jawny zwarty nośnik funkcji G(x,y)=rho(x-y)phi(x); zamianę całkowania i działania dystrybucji przez lemat o iterowanych działaniach z dystrybucją T_1; znak odbicia jądra i identyfikację z operatorem A; istnienie i normalizację aproksymacji jedności; jednolite oszacowanie pochodnych w dowodzie zbieżności silnej, także nad C, i dokładne odwołanie do kryterium ograniczoności. Rozróżniono funkcję wygładzającą i jej dystrybucję regularną. Poprawiono błędne określenie „norma L^1_loc” na topologię i uzasadniono brak zbieżności lokalnie całkowej regularizacji delty. Zamiast nieprecyzyjnego stwierdzenia o kanoniczności splotu podano ścisłą sprzeczność dla rozszerzenia na wszystkie pary zachowującego obie reguły różniczkowania; dla d>1 użyto dystrybucji całkowania po półosi. Commit 5b746b016cae2cbf36d51f1c1c27a31240dcf9d1, blob 8fd9c15b8053e9e77f4a8e36ffcdcc0c1d0a46b5.

## Kontrole
Bieg 45424435143 po audycie 79 zakończył się sukcesem. Dodano szóstą metodę FA21_smoothing_and_strong_convergence_01 w pliku trwałych regresji (ad852c269e667b446f2cb37a0dc7d84eeab542cf). Lokalnie wykonano część arytmetyczną tej metody z dokładnymi ułamkami Python: 1 kontrola normalizacji, 54 równości odbicia, 54 oszacowania błędu, 9 kontroli rozróżnialności znaków — 118/118. Jądro 2z na [0,1] jest niesymetrycznym modelem całkowym, nie gładką funkcją testową; kontroluje znaki i oszacowania, nie stanowi dowodu ogólnego. Kontrola źródła: 19/19 unikatowych etykiet, 22/22 odsyłaczy rozwiązanych w kontekście 17–21, 40/40 fragmentów regresyjnych, poprawne zagnieżdżenie środowisk. Aktualny bieg 45424947906 był queued przy kontroli. Pełny nowy CI i oględziny PDF niepotwierdzone; Lean nie uruchamiano.

## Decyzja
Pierwszy przegląd wszystkich pięciu podsekcji zakończony, stabilizacja 0/3. Audyt 81: pełny przegląd stabilizacyjny I, w tym sprawdzenie spójności założeń i notacji całego rozdziału oraz CI i aktualnego PDF. Bez rozszerzania materiału do zamknięcia rozdziału.
