# Algebra liniowa — rozdział 05: ponowny audyt stabilizacyjny I

**Data:** 22 listopada 2026. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Źródło:** \`chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex\`.
**Blob SHA:** \`f94bdf0b4a35730e858c50cb7fb7288b117facf6\` — bez zmian merytorycznych w tej iteracji.

## Kontrola całego rozdziału: 751 wierszy, 10 dowodów i 4 przykłady

1. **Operacje elementarne:** trzy rodzaje operacji mają jawne odwrotności. Przemnożenie z lewej strony przez macierz elementarną realizuje tę samą operację na wierszach, a produkt tych macierzy pozostaje odwracalny. Konsekwencja dla układu \`PAx=Pb\` obejmuje implikacje w obu kierunkach; jądro jest zachowane, ale obraz podlega działaniu \`P\`, więc nie musi być identyczny.
2. **Algorytm eliminacji:** w kroku \`(r,j)\` wybiera się wyłącznie niezerowy pivot, więc normalizacja i eliminowanie są dopuszczalne nad dowolnym ciałem. Po pominięciu kolumny jej zera pod aktualnym wierszem nie są niszczone przez późniejsze operacje. Po co najwyżej \`n\` kolumnach otrzymuje się postać schodkową, a eliminacja od ostatniego pivotu ku pierwszemu daje postać zredukowaną. Kontrola przypadków \`m=0\`, \`n=0\`, rzędu zero i pełnego nie wykazała luk.
3. **Rząd i jądro:** w macierzy schodkowej zmienne w kolumnach innych niż pivoty mogą być wybierane dowolnie, a pozostałe są jednoznacznie wyznaczane przez podstawianie wstecz. Rzut jądra na współrzędne swobodne jest liniową bijekcją na \`K^{n-r}\`. Stąd poprawny wzór \`rk(A)=r\` na podstawie twierdzenia z LA-04. Kriterium wszystkich pivotów dla iniekcji i \`r=m\` dla surjekcji uwzględnia wymiary zerowe.
4. **Rozwiązalność układów:** przeanalizowano równoważność \`Ax=b\` rozwiązalny, \`b\in im(A)\`, \`rk(A)=rk([A|b])\`, brak sprzecznego wiersza w macierzy schodkowej. Uzasadnienie wzrostu rzędu o jeden po dołączeniu kolumny spoza obrazu jest zgodne z wcześniejszymi wynikami o niezależności; rozwiązania tworzą warstwę \`x_0+ker(A)\`.
5. **Bazy jądra i obrazu:** wektory \`v^(f)\` są dobrze określone przez współrzędną swobodną \`f\` i wzory \`-R_{if}\`, mają jednoznaczne współrzędne swobodne, są niezależne i rozpinają jądro. Dla obrazu wybiera się **kolumny pierwotnej macierzy** o indeksach pivotów, ponieważ eliminacja zmienia podprzestrzeń obrazu poprzez odwracalną macierz z lewej. Dowód przywołuje \`R=PA\` i stosuje \`P^{-1}\`.
6. **Jednoznaczność RREF:** przestrzeń wierszy \`H\` jest niezmiennikiem równoważności wierszowej. Zbiór indeksów pierwszego niezerowego wyrazu niezerowych wektorów \`H\` jest równy zbiorowi pivotów; dopasowanie współrzędnych w kolumnach bazowych ustala jednoznacznie wszystkie wiersze zredukowane. Sprawdzono, że argument działa dla rzędu zero i pustych rozmiarów.
7. **Gauss–Jordan:** z tożsamości \`[PA|P]\` uzyskuje się \`P=A^{-1}\` wtedy i tylko wtedy, gdy lewy blok to \`I_n\`. W przykładzie macierz odwrotna \`[[1,-1],[-1,2]]\` spełnia oba iloczyny z \`A\` i jest zgodna z rozdziałem LA-04.

## Testy i kontrole techniczne

- Dodano trwały regresyjny skrypt \`tools/test_linear_algebra_ch05.py\` i jego uruchamianie w workflow. Niezależna arytmetyka dokładna sprawdziła wszystkie **1553** macierze nad \(\mathbb F_2\) (rozmiary do \`3x3\`) i \(\mathbb F_3\) (do \`2x3\`), wszystkie **12558** pary \`(A,b)\`, jądra, bazę jądra, bazę obrazu z **oryginalnych** kolumn, redukcję przy dwóch odmiennych regułach wyboru pivotu, odwracalność i działania elementarne. **Lokalnie PASS**.
- W rozdziałach 01–05: **226 różnych etykiet**, bez powtórzeń. W rozdziale 05: **16 poprawnie rozwiązanych odsyłaczy**, dziesięć wyników matematycznych z kompletnymi środowiskami \`proof\`, cztery przykłady, brak rysunków wymagających zewnętrznego zasobu i brak naruszeń terminologii. Środowiska LaTeX są prawidłowo zagnieżdżone.
- Z zakończonego sukcesem workflow [45006102819](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006102819) dla tej samej wersji źródła pobrano książkę PDF (315 stron) i wydzielono rozdział 05: **7 stron A4**. Wyrenderowano wszystkie strony, brak pustych stron lub bloków poza stroną; brak \`LaTeX Warning\`, \`Overfull\`, \`Underfull\`, \`Missing character\` i niezdefiniowanych odsyłaczy w logu.
- **Nowy workflow z regresją** [45006576953](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006576953): krok testowy PASS; pełna kompilacja w chwili raportowania jeszcze w toku.

## Wynik
Audyt I **czysty**; nie znaleziono podstaw do korekt w materiale matematycznym. Rozdział pozostaje w procesie ponownej stabilizacji do czasu dwóch kolejnych czystych iteracji i zatwierdzenia CI.
