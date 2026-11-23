# AA-47 — audyt II: niezależna kontrola argumentów matematycznych

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex`.
**Status:** kontrola merytoryczna wykonana częściowo; **NIE STABILNY**. Nie poświadczono CI, PDF ani kompilacji.

## Kontrola niezależna

1. Rozkład funkcji wymiernej: pochodna składnika `-b(x-a)^{1-k}/(k-1)` jest `b(x-a)^{-k}`. Kryterium zerowych residuów dla wymiernej funkcji pierwotnej jest poprawne.
2. Rothstein–Trager: dla unormowanego bezkwadratowego `B`, `Res_x(B,A-zB')=∏(A(a)-zB'(a))`; odtworzenie przez `gcd(B,A-cB')` jest poprawne dla właściwego `A/B`.
3. Równanie `r'+hr=s`: przy wielomianowym `h` pochodna części głównej bieguna rzędu `j` ma rząd `j+1`, więc rekurencja od najwyższej potęgi ujemnej jest trójkątna. Kontrola współczynnika `(x-a)^{-1}` jest konieczna.
4. Wielomianowe `P'+hP=S`: dla `deg h=d≥1` i `P≠0` stopień wynosi `deg P+d`; dla stałego `h=c≠0` skończona suma `Σ(-1)^k S^(k)/c^(k+1)` spełnia równanie.
5. Riccati: bieguny wymiernego rozwiązania przy wielomianowym `q` są proste i mają residuum 1. Po podstawieniu `r=ω+P'/P` równanie liniowe dla `P` ma właściwy znak.
6. Dla `deg q=2d≥2` dwa wybory znaku współczynnika wiodącego `ω` i porównanie współczynnika przy `x^{d-1}` dają `n=[x^{d-1}](q-ω²-ω')/(2a_d)`. Warunek `n∈Z_{≥0}` jest konieczny.
7. Przykłady: `r=x` daje `q=x²+1`; `r=x+1/x` daje `q=x²+3`; `r=√x-1/(4x)` daje `q=x+5/(16x²)`. Ostatni przykład prawidłowo odróżnia gałąź wymierną od algebraicznej.
8. Redukcja `y=gz`, `g'/g=-a/2`, daje `q=a'/2+a²/4-b`; równanie Airy'ego nie jest błędnie rozstrzygane samą gałęzią wymierną.

**Zakres:** sprawdzono osiem grup argumentów matematycznych, nie jest to pełne policzenie wszystkich dowodów i przykładów ani niezależne wykonanie testów regresyjnych.

## Pozostałe bramki

- Uruchomić oba niezależne zestawy testów regresyjnych dla AA-47 i podać ich rzeczywiste wyniki.
- Zweryfikować katalog 47 rozdziałów, etykiety i odsyłacze.
- Uruchomić kompilację LaTeX, sprawdzić log oraz wszystkie nowe strony PDF.
- Potwierdzić zakończony zielony GitHub Actions dla konkretnego commita.
- Wykonać końcowy niezależny audyt stabilizacyjny.

**Werdykt:** nie wykryto błędu w ośmiu sprawdzonych grupach argumentów; brak podstaw do uznania AA-47 za stabilny. Brak zmian źródła i testów, ponieważ w sprawdzonym zakresie nie ustalono usterki wymagającej poprawki. Historycznych statusów AA-01–AA-46 nie zmieniano.
