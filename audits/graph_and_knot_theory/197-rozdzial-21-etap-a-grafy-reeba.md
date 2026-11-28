# Audyt 197 — drukowany rozdział 21, pierwszy etap A

Data: 2026-11-25. Rozdział 20 zamknięty w 196.
Źródło: chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex.
Blob wejściowy c56007887df8a03de3821186be4f89f6bffe2ffc.
Korekta d2e2224f7679c2eb55fe64e5bad9d9111f68757e, blob dcb909fe03e7d7236b4d2789076b572407526df7.

## Usterki i poprawki
- GKT-21-REG-01: jawne uzasadnienie istnienia przepływu na całym regularnym pasie przez funkcję odcięcia i zupełność pola na zwartej rozmaitości; wskazano warunek a<b i niepustość dolnego poziomu.
- GKT-21-BAND-01: pas jest zwartą powierzchnią z brzegiem; zastosowano jawnie klasyczne twierdzenie o uchwytach (Matsumoto, An Introduction to Morse Theory, 2002), sprawdzono założenia, rozpisano rachunek chi=-1 przez addytywność, uzasadniono spotkanie obu poziomów i rozróżniono b od liczby składowych brzegu r. Nie twierdzimy, że podano pełny dowód klasycznego twierdzenia o uchwytach.
- GKT-21-FIBER-01: usunięto lukę między typem topologicznym pasa i jego ilorazem Reeba. Regularna składowa poziomu krytycznego jest okręgiem, przesuwanym przez przepływ do obu końców pasa; otrzymany cylinder jest otwarty i domknięty w pasie, nie zawiera p. W składowej W zawierającej p krytyczne włókno jest zatem spójne. Konstrukcja ciągłej mapy do gwiazdy z ramionami parametryzowanymi wysokością, ciągłość przy c i identyfikacja włókien dają homeomorfizm ilorazu.
- GKT-21-GLUE-01: skończoność zbioru krytycznego przez zwartość i domkniętość zbioru zer różniczki; sklejanie lokalnych grafów na regularnych poziomach, ciągła mapa z M i homeomorfizm ilorazu przez zwartość/Hausdorff. Wnętrza krawędzi mogą obejmować regularne składowe poziomów krytycznych innych składowych; dopuszczono krawędzie równoległe.
- Definicje: gładkość funkcji Morse'a, nieosobliwość hesjanu, indeks niezależny od mapy przez kongruencję, własność uniwersalna ilorazu. Poprawiono zbiór podpoziomowy.
- Rysunek siodła: dodano brakujące trzecie ramię po obu stronach, poprawiono podpis orientacji wysokości. Oględziny PDF pozostają konieczne.
7 etykiet bez zmian, 29 poprawnie zagnieżdżonych par środowisk.
Do dalszej stabilizacji: jawne modele funkcji wysokości na torusie i funkcji na RP2, uzasadnienie zmiany liczby składowych przy siodle i rachunku Eulera całej powierzchni, sprawdzenie topologii ilorazu na regularnych cylindrach, terminologia i skład. Nie uznajemy całego etapu A za zakończony.

## Regresja
GKT-21-REEB-01, test_gkt21_reeb.js, commit 8f1f25edc95efa2ac74389fcd9a3a511be8262be.
PASS: 460 sekwencji do 8 zdarzeń (narodziny, rozdzielenie, połączenie, zanik) kończących się pustym poziomem, ustalony wybór aktywnych ramion FIFO; 161 modeli spójnych, 150 cykli łącznie w modelach spójnych, 182 modele z krawędziami równoległymi, 3572 zdarzenia, 2994 podziały krawędzi. Stopnie 1/3, liczba cykli przez union-find, wzór beta1=k-chi/2 i niezmienniczość przy podziale. Nie jest to enumeracja wszystkich grafów Reeba ani dowód ich realizowalności. Wykonano przed zapisem i po odczycie z repozytorium w izolacie JS, nie w procesie Node; nie potwierdzono wywołania przez CI. Przy pierwszym zapisie testu wystąpił konflikt gałęzi z równoległym raportem PDE, po sprawdzeniu niezmienionego blobu rozdziału ponowiono zapis skutecznie. Nie zmieniano plików PDE.

## Propozycje po pierwszym audycie
Opcjonalnie: jawne odwzorowanie ilorazowe dla wysokości torusa z oznaczeniem poziomów krytycznych oraz rozróżnienie grafu Reeba, grafu konturowego i drzewa konturowego w analizie danych. Propozycja niezatwierdzona, nie rozszerzać samodzielnie zakresu podczas stabilizacji; poprawki istniejących przykładów są częścią audytu.

## Bramka
Dla d2e2224: terminologia 45574398809 SUCCESS, algorytmy 45574398634, aplikacja 45574398914, pełny audyt 45574398923 w toku. Nie oglądano nowego PDF. Etap A otwarty. Następny audyt 198: stabilizacja istniejących dowodów, przykładów, regresji i kontrola CI/PDF.
