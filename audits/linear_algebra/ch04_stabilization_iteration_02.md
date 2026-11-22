# Algebra liniowa — rozdział 04: ponowny audyt stabilizacyjny II (czysty)

**Data:** 22 listopada 2026. **Źródło:** \`chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex\`.  
**SHA źródła przed i po audycie:** \`6bc9a3c2de2d09c5f67e9ba032fac387b3bcb36e\`, identyczny jak podczas audytu I.

## Druga niezależna lektura: założenia, implikacje i przypadki brzegowe

1. **Puste rozmiary:** \(\operatorname{Mat}_{m\times n}\) dla \(m=0\) lub \(n=0\) ma jeden element, ale pary wymiarów pozostają częścią typu obiektu; baza \(E_{ij}\) jest pusta, \(\dim=mn=0\), iloczyny z pustym indeksem sumowania pozostają zgodne. Wyjątkowy przypadek \(\operatorname{Mat}_{0\times0}\) zachowuje identyczność i odwracalność \(I_0\).
2. **Identyfikacja Hom–Mat:** w twierdzeniu o macierzy odwzorowania obie strony wzoru \([T(v)]_C=A[v]_B\) są kolumnami w \(K^m\). Dowód jedyności przez podstawienie \(v=b_j\) jest poprawny dla \(n>0\), a przy \(n=0\) jedyność wynika z jedynej macierzy i jedynego odwzorowania. Izomorfizm Hom–Mat wykorzystuje dwustronnie dokładnie te fakty.
3. **Kolejność mnożenia:** w \([T\circ S]_{C\leftarrow D}=[T]_{C\leftarrow B}[S]_{B\leftarrow D}\) wymiary iloczynu są \(m\times p\). Obie strony wyznaczają te same współrzędne; łączność opiera się na równości dwóch skończonych podwójnych sum. Rozdzielności i skalary mają jawne wzory współrzędnych, bez ukrytych przeskoków.
4. **Rząd i odwrotność:** \(\operatorname{im}A=\operatorname{span}\{a_1,\ldots,a_n\}\), \(\ker A=\{x:\sum_jx_ja_j=0\}\), \(n=\dim\ker A+\operatorname{rk}A\) dają właściwe kryteria niezależności i rozpinania. W twierdzeniu o odwracalności rozdzielono bijektywność, niezerowe jądro, surjektywność i istnienie macierzy odwrotnej, włącznie z \(n=0\).
5. **Zmiana baz:** baza po prawej jest bazą dziedziny, a lewa przeciwdziedziny. Matryca \(P_{B\leftarrow B'}\) bierze kolumny nowej bazy wyrażone w starej, stąd \([v]_B=P[v]_{B'}\); analogicznie \(Q=P_{C\leftarrow C'}\). Wobec tego \(Q^{-1}AP\), nie \(QAP^{-1}\). Dokładny rachunek przykładu \(P^{-1}AP=\bigl(\begin{smallmatrix}3&1\\-2&0\end{smallmatrix}\bigr)\) zgadza się z bezpośrednimi obrazami bazowymi.
6. **Transpozycja i układ liniowy:** kolejność w \((AD)^{\mathsf T}=D^{\mathsf T}A^{\mathsf T}\) uzasadnia porównanie \((k,i)\) wyrazów, a opis wszystkich rozwiązań \(x_0+\ker A\) wynika z równości \(A(x-x_0)=0\) także dla pustego zbioru zmiennych.

## Redakcja, odsyłacze, skład
- Ponownie sprawdzono **1221 wierszy, 15 dowodów, 10 przykładów**. Każde z 15 twierdzeń/stwierdzeń/wniosków ma bezpośrednio następujący dowód.
- **199 unikalnych etykiet** w rozdziałach 01–04, **24 odsyłacze** w rozdziale 04 bez brakujących celów. Stos otwartych środowisk po analizie LaTeX jest pusty, bez niezgodności \`begin/end\`.
- Nie wykryto uchybień terminologicznych ani potrzeby dodawania nowego twierdzenia.
- Kontrolowany PDF ma **12 stron A4**, nie zawiera pustych stron, tekstu poza formatem ani \`Overfull\`/\`Underfull\`; diagram współrzędnych widoczny i czytelny.
- Trwały test \`tools/test_linear_algebra_ch04.py\` przeszedł krok \`Verify matrix algebra, base changes and zero dimensions\` w workflow [45005857080](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45005857080). Wynik pełnego workflow należy potwierdzić po zakończeniu kompilacji.

**Wynik:** audyt II czysty, bez zmian w źródle. Jest to pierwszy z dwóch kolejnych czystych przebiegów kontrolnych po audycie I; do ostatecznej stabilizacji pozostaje audyt III i końcowy CI.
