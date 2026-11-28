# RRC 18 — iteracja 306: Li–Yau, pierwsza wartość własna, Neumann

Commit źródła: 71343c21f5c4d6369a6d72b18f060edd686424ce.

- W zasadzie wypełniania najniższych częstotliwości rozpatrzono nieskończony moment, rozpisano całkowanie radialne i warunek równości.
- W dowodzie Li–Yau uzasadniono przedłużenie zerowe w H^1 oraz całkowalność L^1, tożsamość transformaty słabej pochodnej przez aproksymację, energię funkcji własnej i zastosowanie nierówności Bessela w zespolonej przestrzeni. Poprawiono znak wykładnika w funkcji testowej przy konwencji iloczynu skalarnego liniowego w pierwszym argumencie.
- W dowodzie prostoty pierwszej wartości własnej usunięto zbędne założenie C^{1,1} brzegu. Uzasadniono dodatniość wartości własnej przez Poincarégo na kostce, przynależność modułu do H_0^1 przez słabą zbieżność aproksymacji, równanie Eulera–Lagrange'a minimalizatora. Gładkość i ścisłą dodatniość wykazano przez harmoniczne podniesienie f(x)cosh(sqrt(lambda_1)t), lemat Weyla w wymiarze d+1 i mocną zasadę maksimum. Dowód działa także w d=1.
- W przypadku Neumanna rozpisano przesunięcie formy, zastosowanie zwartości, identyfikację jądra oraz osiąganie minimum dla średniej zero i jego dodatniość.

Kontrola źródła: 1031 wierszy (wcześniej 930), 42 zachowane unikatowe etykiety, 45 wystąpień odsyłaczy, dziewięć różnych zewnętrznych celów; siedem celów w rozdziałach 7, 9, 10, 14 potwierdzono w źródłach w tym samym commicie (pozostałe dwa to wcześniejsze chap:pde12 i chap:pde20). Brak niezgodności begin/end. Brak dedykowanego workflow rozdziału 18; przebiegi terminologii, aplikacji i rozdziałów 13–16 w kolejce. Kompilacja rozdziału 18 niepotwierdzona.

Pierwsza lektura szczegółowa objęła sekcje 18.1–18.7. Następny etap: ślad półgrupy cieplnej, przejście abelowe, perturbacje widma i wzór Hellmanna–Feynmana, następnie pełne audyty stabilizacyjne i dedykowana kompilacja.
