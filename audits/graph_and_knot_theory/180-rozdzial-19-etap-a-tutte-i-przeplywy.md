# Audyt 180 — drukowany rozdział 19, etap A

Data: 2026-11-25. Po zamknięciu rozdziału 18 w audycie 179.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Blob wejściowy bd8f248bd86b0df6c84da54e02055ad06dd07402.
Korekty 8ddebd8b895b87cd4b7db98826f665db5165ddb8, d24c1110e8ab68158020559bcc6f5ecc23f0dccd; końcowy blob e38269251fa906ac3bde55f733a354a6bbc0091c.

## Ustalenia i poprawki
- Nie przedstawiamy rekurencji usuwania i kontrakcji jako bezwarunkowo efektywnej: może rozgałęziać się wykładniczo.
- Rozwinięto dowód wymiaru przestrzeni cykli nad F2 dla multigrafów, w tym pętli i grafu zerowego; wcześniejsze twierdzenie o rzędzie dotyczy grafów prostych nad R, więc nie wystarczało samo jego przywołanie.
- Wyprowadzono wykładniki w rekurencji dla mostu, obliczenia C2 i Cn oraz theta, specjalizację (1,1) dla grafów niespójnych i pustego, przypadek q=1 w przykładzie chromatycznym. Doprecyzowano definicję macierzy incydencji dla przepływów.
- Zastąpiono skrótowe uzasadnienie dualności usuwania i kontrakcji bezpośrednim dowodem przez A i dopełniający zbiór krawędzi dualnych. Wykorzystano wzór Eulera dla grafu niespójnego, zachowanie izolowanych wierzchołków oraz lokalne łączenie ścian. Wykładniki w obu sumach zamieniają się miejscami. Obejmuje graf z jednym wierzchołkiem bez krawędzi.
- Zastąpiono skrótowy argument rozkładu zamkniętych spacerów dualnych dowodem surjektywności D=-d2 poprzez dopełniające drzewa rozpinające. Różnica przepływów jest wsparta na drzewie i znika przez usuwanie liści. Działa nad Z/qZ bez dzielenia, także gdy q jest złożone. Każdy przepływ ma q przeciwobrazów; warunek niezerowości odpowiada poprawnemu kolorowaniu.
- Uściślono, że dualny trójkąt dotyczy sferycznego zanurzenia theta. Zachowano wszystkie 12 etykiet i 32 poprawnie zagnieżdżone pary środowisk.

## Trwały test automatyczny
GKT-19-DUAL-01, audits/graph_and_knot_theory/test_gkt19_dual_flows.js, commit be5bb44433307b419b69f8f3a1f5773bd914b4a6.
Wykonano dwukrotnie, drugi raz po odczycie zapisanego pliku i finalnego źródła, w izolacie JS. PASS: 747 układów (w tym pusty model), 453 spójne sferyczne, 3533 pary dopełniających podzbiorów, 1812 porównań liczby kolorowań z przepływami, w tym 906 dla q=4,6; pętle, mosty i krawędzie równoległe objęte próbami. Sprawdzono również współczynniki w bazie przesuniętej (x-1,y-1). Test modeli skończonych, nie formalizacja Lean i nie dowód geometryczny.

## Propozycje (nie wprowadzono)
Możliwa wartościowa specjalizacja: jawny wielomian przepływów dla dowolnego grafu przez zasadę włączeń i wyłączeń oraz T_G(0,1-q), z osobnym dowodem dla złożonego q; uzupełniłaby obecne powiązanie ograniczone do sferycznej dualności kolorowań. Wymaga akceptacji użytkownika zgodnie z AGENTS.md.

## Bramka
CI dla pierwszej korekty: terminologia 45568589218 SUCCESS, pełny audyt 45568589220, algorytmy 45568589249, aplikacja 45568589240 w toku w chwili zapytania. Dla końcowego commitu zapytanie jeszcze nie zwróciło przebiegu. Nie przeprowadzono lokalnej kompilacji ani oględzin PDF. Etap A otwarty. Następnie: ponowna szczegółowa kontrola całej rekurencji, specjalizacji i dowodów dualności, CI i PDF; bez samowolnego rozszerzania materiału.
