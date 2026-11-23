# Teoria grafów i węzłów — przepływy, audyt 02: kontrola PDF i odsyłaczy

Data: 2026-11-23. Nie oznaczać jako zakończone przed świeżym przebiegiem CI.

## Przebieg źródłowy

- [GitHub Actions 45144431368](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45144431368): \`finite-models = success\`, \`chapter-pdf = success\`.
- Niezależne regresje sieciowe: 1467 pełnych enumeracji małych sieci skierowanych, 1050 deterministycznych przykładów z pojemnościami całkowitymi (w tym łuki przeciwne i równoległe) oraz 680 przykładów z dokładnymi przepustowościami wymiernymi.
- Dla każdego przypadku sprawdzono trzy algorytmy wobec wyczerpującego minimum po wszystkich przekrojach \`s,t\`, bilanse wierzchołków, ograniczenia pojemności, nasycenie przekroju i odległości resztowe.
- Zapisano PDF fragmentu książki (rozdziały historyczne 00–05 i nowe 37–40), **58 stron**, układ A4. Przeprowadzono niezależny ogląd stron 53–58, zwłaszcza obu rysunków przepływowych i definicji warstw Dinica.
- Brak przepełnień \`Overfull\` w logu.

## Wykryte problemy

1. W drugim rysunku (przepływ o wartości 5) granica przekroju przy \`x=-2.05\` znajdowała się zbyt blisko etykiet pojemności \`2\` i \`3\`. Wprowadzono przesunięcie granicy do \`x=-2.48\`, nadal pomiędzy źródłem \`s\` i pozostałymi wierzchołkami.
2. Pomimo sukcesu kompilacji, log po \`pdflatex\` wykonanym **dwukrotnie** zawierał ostrzeżenie \`LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\`. Dotychczasowy workflow weryfikował tylko ostrzeżenia o bezpośrednio brakujących/powtarzających się odsyłaczach, nie wymagając ich ustabilizowania.
3. Zaktualizowano CI: trzy przebiegi kompilacji i twardy błąd przy ostrzeżeniach o niedookreślonych, powtarzających się lub zmienionych etykietach na ostatnim przebiegu.

## Status i kolejny krok

Oczekuje na świeże CI i sprawdzenie nowego PDF: diagram i jego podpis, brak przepełnień oraz brak ostrzeżeń o zmianach odsyłaczy. Dopiero wtedy można zapisać ostateczny raport stabilizacji rozdziału 40.
