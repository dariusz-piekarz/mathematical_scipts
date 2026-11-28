# Algebra liniowa — rozdział 04: ponowny audyt stabilizacyjny III (drugi czysty)

**Data:** 22 listopada 2026.  
**Plik:** \`chapters/pl/linear_algebra/04-macierze-odwzorowan-liniowych-i-zmiana-bazy.tex\`.
**SHA źródła:** \`6bc9a3c2de2d09c5f67e9ba032fac387b3bcb36e\` — niezmieniony podczas audytów I, II i III.

## Trzecia iteracja: ponowne sprawdzenie dowodów i przykładów

- **Tablice i współrzędne:** własności przestrzeni \(\operatorname{Mat}_{m\times n}(K)\), kolumnowy zapis macierzy odwzorowania, jednoznaczność przedstawienia operatora przez macierz oraz zgodność diagramu współrzędnych są poprawne. Puste bazy \(K^0\) zachowano jawnie w założeniach i dowodach.
- **Składanie:** sprawdzono kolejność działania \(S\) i \(T\), pasowanie rozmiarów \(m\times n\), \(n\times p\) i równość podwójnych sum w dowodzie \(A(Mx)=(AM)x\). Łączność i rozdzielności są uzasadnione rachunkiem wyrazów, w tym skalarem wyciąganym przed sumę.
- **Rząd i odwrotność:** weryfikowano oba zawierania w opisie obrazu przez kolumny, jądro jako warunek \(\sum x_ja_j=0\), ograniczenie rzędu, pięć kryteriów odwracalności, obustronny iloczyn odwrotny i przypadek wymiaru 0.
- **Zmiana bazy:** niezależnie przeprowadzono dwa przekształcenia współrzędnych \([v]_B=P[v]_{B'}\) i \([v]_{B'}=P^{-1}[v]_B\), a następnie \([T(v)]_{C'}=Q^{-1}AP[v]_{B'}\). Potwierdzono konkretny przykład \(P=\bigl(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\bigr)\) i \(P^{-1}AP=\bigl(\begin{smallmatrix}3&1\\-2&0\end{smallmatrix}\bigr)\) z bezpośrednimi obrazami nowych wektorów bazy.
- **Transpozycja i równania:** porównano wyrazy \((AD)^T\) i \(D^TA^T\); przeanalizowano także warunek \(b\in\operatorname{im}A\), rozkład wszystkich rozwiązań \(x_0+\ker A\) i parametryzację przykładowego układu.

## Kontrole integralności

- Źródło **1221 wierszy**, 15 wyników matematycznych z następującymi bezpośrednio 15 pełnymi dowodami, 10 przykładów i 1 diagram TikZ — wszystkie obiekty w tej samej wersji, co podczas audytów I i II.
- W rozdziałach 01–04 **199 różnych etykiet**, bez duplikatów; w 04 wszystkie **24 odsyłacze** wskazują poprawny cel. \`begin/end\` bez błędnego zagnieżdżenia.
- Niezmieniony kod źródłowy zgodny z globalną terminologią. Nie wprowadzono opcjonalnych nowych twierdzeń, które rozszerzałyby zatwierdzony zakres.
- PDF wycięty z poprawnego CI dla tego samego źródła ma **12 stron A4**. Sprawdzono wszystkie strony i diagram, nie wykryto pustych stron, uciętych bloków tekstu ani ostrzeżeń o składzie.
- Test \`tools/test_linear_algebra_ch04.py\` obejmuje dokładne przypadki \(\mathbb F_2,\mathbb F_3\) i przeszedł swój krok w CI [45005857080](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45005857080). Ostateczną konkluzję pełnego workflow należy odczytać po jego zakończeniu.

## Wniosek

**Dwa kolejne czyste audyty II i III przeprowadzono na identycznym SHA treści, bez zmiany rozdziału.** W świetle ponownego sprawdzenia matematycznego, odsyłaczy, testów i wizualnego PDF rozdział 04 uzyskuje status **STABILNY**. Końcowy wynik CI po samych aktualizacjach raportów i statusu należy potwierdzić osobno, bez nazywania niezakończonego workflow wynikiem PASS.
