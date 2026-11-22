# Algebra liniowa — rozdział 04: ponowny audyt stabilizacyjny I (czysty)

**Data:** 22 listopada 2026. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Plik:** \`chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex\`.
**SHA treści:** \`6bc9a3c2de2d09c5f67e9ba032fac387b3bcb36e\`. Plik pozostawiono bez zmian.

## Kontrola matematyczna, rozdział po rozdziale

Odczytano **1221 wierszy**, w tym **15 dowodów** i **10 przykładów**. Skontrolowano:
1. **Macierze \(\operatorname{Mat}_{m\times n}(K)\)** — definicję jako rodzinę indeksowaną parami, rozmiary \(0\times n\), \(m\times0\), bazę \(E_{ij}\), liniową niezależność i wymiar \(mn\). Macierze z pustymi zbiorami indeksów zachowują rozmiary; istnieje dokładnie jedna taka macierz dla każdego danego rozmiaru.
2. **Kolumny i macierz odwzorowania** — rachunek \(Ax=\sum_jx_jAe_j\); podstawienie obrazów wektorów bazowych do \([T(v)]_C=[T]_{C\leftarrow B}[v]_B\) i jednoznaczność kolumn. Weryfikowano również przypadki \(m=0\), \(n=0\) oraz diagram współrzędnych.
3. **Składanie i iloczyn** — zgodność konwencji \([T\circ S]=[T][S]\), dokładny rachunek \(A(Mx)=(AM)x\); łączność po przestawieniu dwóch sum skończonych, obie rozdzielności i mnożenie przez skalar, macierze jednostkowe i jawny kontrprzykład przemienności.
4. **Jądro, obraz i rząd** — opis jądra jako wszystkich zależności kolumn, obrazu jako przestrzeni przez nie rozpiętej; oszacowanie \(0\leq\operatorname{rk}A\leq\min(m,n)\), wzór \(n=\dim\ker A+\operatorname{rk}A\) oraz sprawdzenie prostokątnego przykładu.
5. **Odwracalność** — równoważność 5 kryteriów, związek z liniową odwrotnością, jednoznaczność \(A^{-1}\), obustronny rachunek \(AB=BA=I_2\) oraz oba iloczyny w tożsamości \((AB)^{-1}=B^{-1}A^{-1}\). Przypadek \(n=0\) jest jawny.
6. **Zmiana bazy** — orientację macierzy \(P_{B\leftarrow B'}\), oba kierunki \(QP=PQ=I_n\), wzór \([T]_{C'\leftarrow B'}=Q^{-1}[T]_{C\leftarrow B}P\), a dla endomorfizmu \(P^{-1}AP\). Przeliczono przykłady w \(\mathbb R^2\) z kolumnami \((3,-2)^T,(1,0)^T\).
7. **Transpozycja i układy** — definicję i rozmiary transpozycji, \((AD)^T=D^TA^T\), w tym puste indeksy; rozwiązalność \(Ax=b\iff b\in\operatorname{im}A\) i zbiór rozwiązań \(x_0+\ker A\), przykład z dwoma parametrami \(\alpha,\beta\) i jednym wolnym \(t\).

Nie wykryto brakujących założeń, nieuzasadnionego istotnego wzoru ani rachunku z błędną kolejnością czynników. Pozostawiono historyczne etykiety i zaakceptowany zakres materiału.

## Przegląd techniczny i wizualny
- Rozdziały 01–04: **199 unikatowych etykiet**, bez powtórzeń; rozdział 04: **24 odsyłacze**, wszystkie prowadzą do istniejących etykiet w rozdziałach 01–04. Zagnieżdżenie środowisk poprawne (103 otwarcia i zamknięcia).
- W treści matematycznej nie znaleziono niedozwolonych wyrażeń („unia”, „injektywność”, „tensorowanie”, „relacja liniowa”, „sekwencja” itp.). Rysunek TikZ nie wymaga zewnętrznych plików.
- Z artefaktu zakończonego sukcesem CI \`45005500264\` pobrano pełną książkę (315 stron) i wyodrębniono rozdział 04: **12 stron A4**, niezmieniony SHA źródła. Wyrenderowano wszystkie 12 stron do kontaktowego arkusza i obejrzano diagram macierzy odwzorowania. Nie ma pustych stron, bloków poza stroną, ostrzeżeń \`Overfull\`/\`Underfull\`, brakujących znaków ani nierozwiązanych odsyłaczy.
- Porównano standard szczegółowości dowodów z rozdziałem 01 geometrii różniczkowej, bez dodawania opcjonalnych nowych twierdzeń.

## Testy regresyjne i CI
Dodano \`tools/test_linear_algebra_ch04.py\` oraz krok \`Verify matrix algebra, base changes and zero dimensions\` do Actions. Testy obejmują dokładne arytmetyczne kontrole macierzy prostokątnych i zerowych rozmiarów nad \(\mathbb F_2\) i \(\mathbb F_3\), równości jądra i obrazu, warstwy rozwiązań \(Ax=b\), obustronną odwracalność, łączność i transpozycję iloczynu oraz poprawność wzoru \(Q^{-1}AP\) przy niezależnych bazach dziedziny i przeciwdziedziny. **Status nowego CI należy odczytać po zakończeniu — nie jest automatycznie uznany za PASS przez sam zapis skryptu.**

**Wniosek:** audyt stabilizacyjny I czysty na źródle \`6bc9a3c...\`. Do zamknięcia konieczne są jeszcze niezależne czyste audyty na tym samym źródle i ostateczny wynik CI.
