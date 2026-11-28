# GT — audyt kontrolny 319

GT01: ponownie prześledzono dowód kryterium Erdősa–Gallaia (maksymalizacja częściowej realizacji, kroki A–C, parzystość niedoboru, przypadek wspólnych końców w kroku C). Rozpisano porównanie liczności i wykluczenie niedozwolonych końców w kroku B. Commit 0504006bfa8f51314d9a1d0a046f2ea3af568663.
GT04: sprawdzono dowody obu wersji Mengera, usuwanie przeciwnych przepływów, konstrukcję rozcięcia wierzchołków i oba kierunki porównania separatora z przekrojem. Doprecyzowano, dlaczego rozkład na jednostkowe ścieżki działa również przy pojemnościach większych od 1; poprawiono błąd językowy. Commit 1ae92379cd29a0c6fc61648d88013a08e448ed02.
GT05: ponownie sprawdzono indukcję Halla, deficyt i dowód Königa przez ścieżki naprzemienne, również przypadki pustych części; w sprawdzonych dowodach bez nowych luk.
GT06: sprawdzono rząd i całkowitą bazę homologii, ortogonalność modulo dwa, dowód całkowitej unimodularności i całkowitości punktów ekstremalnych. Dodano jawny izomorfizm kompleksów przy zmianie orientacji (3b8715822597c12820bef7efb4818eb019c19ebd) oraz kontrprzykład C4 przeciw myleniu ortogonalności nad F2 z sumą prostą (3c8591f5f6962efd07c8c0ed82cd1d9d6a40d3c4).

Kontrola: 637/637 niemalejąco ograniczonych (uporządkowanych nierosnąco) ciągów stopni dla 1<=n<=6, porównanie nierówności Erdősa–Gallaia z enumeracją wszystkich grafów prostych na ustalonym zbiorze. 3/3 cele nowych odsyłaczy występują dokładnie raz w sprawdzonych plikach. Zagnieżdżenie środowisk LaTeX poprawne w trzech zmienionych rozdziałach, ponowny odczyt potwierdził zapis. Test skończony nie zastępuje dowodu.

CI pełne 45984230178, algorytmy 45984230317, aplikacja 45984230304, terminologia 45984230170 w kolejce podczas odczytu. PDF niezweryfikowany wizualnie. Następny krok: GT07–10, pokrycia grafów, operator Laplace'a, Kirchhoff i szczegółowy dowód Kuratowskiego. Kontrola nie obejmowała wszystkich twierdzeń GT01–06; odbiór całości pozostaje otwarty.
