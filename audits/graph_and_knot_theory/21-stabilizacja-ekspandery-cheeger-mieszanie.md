# Teoria grafów i węzłów — stabilizacja rozdziału o ekspanderach

Data: 2026-11-23.
Wynik: **STABILNY MODUŁ: rozdział 43, ekspandery i analiza spektralna.**
Werdykt dotyczy rozdziału i jego lokalnej integracji; nie oznacza zakończenia audytów całej książki ani formalizacji w Lean.

## Źródło i raporty

- Rozdział: \`chapters/pl/graph_and_knot_theory/43-ekspandery-widmo-laplasjanu-i-spacery-losowe.tex\`.
- Zatwierdzona matematycznie wersja źródeł: [commit 95e3cbdee2243903b7c13d9f03b69d69d59e42fa](https://github.com/dariusz-piekarz/mathematical_scipts/commit/95e3cbdee2243903b7c13d9f03b69d69d59e42fa).
- Audyty: \`19-ekspandery-audyt-wstepny-cheeger-mieszanie.md\` oraz \`20-ekspandery-niezalezny-audyt-widma-dowodow-i-pdf.md\`.

## Wyniki weryfikacji

[GitHub Actions — testy matematyczne i PDF, przebieg 45152247639](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247639): \`finite-models=success\`, \`chapter-pdf=success\`.

- **33 866** niezależnie wygenerowanych grafów prostych o 2–6 wierzchołkach, spośród których **193** grafy regularne przeanalizowano spektralnie, z enumeracją wszystkich przekrojów;
- **21** dodatkowych modeli grafów pełnych, cykli i przykładu niespójnego;
- dokładne wartości ekspansji i energii, niezależne przybliżenia spektrum metodą Jacobiego, nierówności Cheegera, kryterium spójności, oszacowanie średnicy i mieszania spaceru losowego;
- weryfikacja mieszania z użyciem arytmetyki dokładnej \`fractions.Fraction\`;
- ponownie przeszły wszystkie wcześniej stabilizowane moduły algorytmiczne i probabilistyczne.

## Kontrola dowodów i wizualizacji

- Potwierdzono jawne założenia \`n>=2\`, \`d>=1\`, regularność i wymaganie spójności tam, gdzie to potrzebne.
- Pełny dowód \`lambda_2/2 <= Phi <= sqrt(2lambda_2)\` zawiera argument z poziomicami i pozytywną częścią wektora własnego; stosunek \`h_V\`, \`h_E\`, \`Phi\` jest poprawnie znormalizowany.
- Leniwa macierz przejścia eliminuje przeszkodę okresowości grafów dwudzielnych; czas mieszania opiera się na \`eta_2=1-lambda_2/2\`.
- Przeprowadzono rzeczywistą inspekcję **75-stronicowego PDF**, nowy rozdział znajduje się na stronach PDF 70–75 (druk 66–71).
- Trzy zakończone sukcesem przebiegi LaTeX; końcowy log bez przepełnień i bez ostrzeżeń o niezdefiniowanych lub zmienionych etykietach.
- Rysunek \`C_8\`, cyfry, pogrubione krawędzie granicy, podpisy i wzory nie nachodzą na siebie.

## Testy integracji

- [Mathematical library application checks — 45152247716](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247716): **success**.
- [Polish mathematical terminology — 45152247581](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152247581): **success**.
- Katalog Atlasu oraz główny plik książki zawierają zgodne **44** pliki źródłowe; rozdział 43 jest włączony po 42.

## Zakres werdyktu

Rozdział 43 ma status **STABILNY po audytach 01 i 02**. Numer 43 oznacza identyfikator pliku źródłowego; w kontrolnym składzie fragmentu książki jest to rozdział 12.
Samo wykonanie testów numerycznych nie stanowi formalnego dowodu w Lean, a kontrola 75-stronicowego fragmentu nie zastępuje audytu wszystkich historycznych rozdziałów skryptu.

## Dalsze kroki

Stabilizację podstawowego bloku: BFS/DFS, drogi ważone (A*, CH), MST/DSU, przepływy, Turán/Ramsey, grafy losowe i ekspandery uznano za zakończoną na poziomie **poszczególnych nowo dodanych modułów**. Dalsze prace mogą objąć albo globalną kontrolę spójności całego tomu, albo osobne rozdziały o jawnych konstrukcjach ekspanderów i ich zastosowaniach. Żaden z tych kolejnych etapów nie jest uznany za już wykonany.
