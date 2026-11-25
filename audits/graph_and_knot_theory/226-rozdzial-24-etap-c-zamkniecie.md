# Audyt 226 — drukowany rozdział 24, zamknięcie etapu C

Data: 2026-11-25. Kontynuacja 225, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex, blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830.

## Końcowa kontrola semantyczna
Ponownie odczytano cały rozdział. Sprawdzono symetrię zbioru generatorów i argument redukcji słowa, stabilizatory i działanie bez inwersji, bijekcję gwiazd i nakrycia w słabej topologii CW, zwartość obrazów pętli i homotopii, drzewo rozpinające z lematu Zorna, izomorfizm przez końce podniesień, prezentację grafu grup, dwa kołnierze cylindra i kierunek sprzężenia w HNN, zmianę ścieżek bazowych, dobór reprezentantów i monomorfizmy, dobrze określone końce klas bocznych i wzór na stopnie (obie orientacje pętli). Przykłady grup wolnych, torusa, C2*C3 i BS(1,2) zgodne z tezami. Nie stwierdzono nowych istotnych błędów ani luk w przeprowadzonych dowodach. Fundamentalne twierdzenie Bassa–Serre'a, w szczególności acykliczność ogólnego modelu klas bocznych, pozostaje jawnie przyjętym wynikiem literaturowym, nie dowodem własnym.

## Regresja i integralność
W procesie Python ponownie wykonano samodzielną kopię modelu GKT-24-BS12-PY-01 z dokładnymi ułamkami: 6534 reprezentantów, 594 odwrócenia, 26730 translacji, 4602 incydencje, 1534 wierzchołki, 1533 krawędzie. PASS, 38460 iteracji kontrolnych. To test skończonego modelu, nie formalizacja Lean. Zintegrowaną wersję potwierdza rzeczywisty log z audytu 224.
Porównano listy nazw i blobów wszystkich 44 plików rozdziałów na gałęzi roboczej z SHA fcce40f7b25b4aa8db9b7f75974a2986330d33dc: identyczne. Także plik główny (9298d7d95e1787db19382449018320ac3cb91a79), globalny workflow (fc58c9936b5387e821085146173b936def36b167) i plik testu Hodge/Bass–Serre (b01851e33633381568d88ecd3d41660022a31a44) są identyczne.
Run 45591196612 dla fcce40f7 potwierdzony jako completed/success. Kontrola PDF z 225 pozostaje aktualna dla niezmienionego tomu: 354 strony, zero ostrzeżeń, siedem stron rozdziału obejrzanych. Nie kompilowano ani nie oglądano PDF ponownie w tej iteracji; nie twierdzi się, że cały aktualny HEAD przeszedł nowy CI.

## Decyzja
Etapy A, B i C zamknięte. Rozdział 24 ustabilizowany w przyjętym zakresie. Brak zmian źródła. Postęp 24/44.
Następny audyt 227: drukowany rozdział 25, etap A, źródło chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex. Pierwsza kontrola matematyczna, językowa, szczegółowości dowodów, odsyłaczy, przykładów, rysunków i istniejących regresji; ewentualne rozszerzenia wyłącznie w pierwszym etapie.
