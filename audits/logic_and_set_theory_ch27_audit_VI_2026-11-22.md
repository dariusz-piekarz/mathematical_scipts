# Logika matematyczna i teoria mnogości — rozdział 27, audyt VI (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex`  
**Zakres:** tylko rozdział 27, bez dodawania nowego materiału i bez modyfikacji tekstu w audycie VI.

## Ponowna pełna kontrola matematyczna

1. **Porównywanie mocy:** zweryfikowano definicje równoliczności, porządku mocy przez iniekcje, nierówności ostrej i skończonego przypadku właściwej inkluzji.
2. **Cantor–Bernstein w ZF:** sprawdzono rekurencję `A_{n+1}=g[f[A_n]]` za pomocą całkowitej funkcji na `P(A)`, istnienie sumy `C`, dokładną równość `C=A₀∪g[f[C]]` oraz rozdział obu części zbudowanej bijekcji. Sprawdzono iniektywność i surjektywność także dla zbiorów pustych.
3. **Operacje kardynalne:** potwierdzono istnienie zbiorów funkcji `B^A` w ZF przez separację w `P(A×B)`, niezależność operacji od reprezentantów (w tym składanie bijekcji `β∘h∘α⁻¹`), wszystkie cztery podstawowe prawa, kurrowanie funkcji i przypadki `0^0=1`, `0^1=0`.
4. **Parowanie Cantora:** skontrolowano indukcję `2t_s=s(s+1)`, związek `t_{s+1}=t_s+s+1`, rozłączność, brak luk i nieograniczoność przedziałów numeracyjnych; ręczne odwrócenie `π(2,1)=7`; poprawność wyróżnionej przekątnej `m+n=3` na rysunku.
5. **Podzbiory liczb naturalnych:** sprawdzono konstrukcję enumeracji przez minima i rekurencję na `P(D)` z odpowiednią totalizacją funkcji przejścia; odwołania do dobrego porządku `ω` i rekurencji z rozdziału 25.
6. **Moc kontinuum:** zweryfikowano dodatnią różnicę w kodowaniu trójkowym `S↦∑_{n∈S}2/3^{n+1}`, gęstość `Q` wykorzystaną w przekrojach `D_x`, kanoniczny zredukowany ułamek `a/b`, iniekcję `γ:Z→ω` i `j:Q→ω`, a następnie zastosowanie Cantora–Bernsteina.
7. **Diagonalizacja nieprzeliczalności `R`:** sprawdzono jednoznaczność każdego `S_n`, wykres funkcji `n↦S_n` przez zastępowanie, separację dla zbioru `D={n∈ω:n∉S_n}` oraz właściwą sprzeczność `k∈D ⇔ k∉D`; brak ukrytej aplikacji AC.
8. **Jawne bijekcje:** skontrolowano ograniczenia wartości `F:R→(0,1)`, istnienie odwrotności i obie tożsamości złożenia, przesuwanie ciągu `1/2,1/3,…` w funkcji `H:(0,1)→(0,1]` oraz poprawność jej odwrotności `K`. Wyraźnie rozróżniono równość mocy od długości przedziałów.
9. **Porównywalność a AC:** sprawdzono obie implikacje w ZF, korzystając z wcześniej skonstruowanego zbioru Hartogsa i porównania dobrych porządków; dowód nie odwołuje się do wyników przyszłego rozdziału 28.

**Werdykt audytu matematycznego VI:** nie wykryto nowych błędów, nieuzasadnionych wzorów ani nieprecyzyjnych warunków wymagających kolejnej poprawki.

## Inwentarz, testy i kompilacja

- **4 definicje, 11 twierdzeń, 2 wnioski, 5 przykładów, 6 uwag, 13 dowodów, 1 rysunek.**
- **24 unikatowe etykiety; 16 odsyłaczy.** Jedynym świadomym odsyłaczem przyszłym jest `ch:ordinals` do niewłączonego jeszcze rozdziału 28; występuje dwukrotnie, pozostaje jawnie dozwolony w CI. Pozostałe odsyłacze rozwiązywane poprawnie.
- Rozszerzone regresje `tools/tests/test_logic_and_set_theory_ch27.py`: **PASS**.
- GitHub Actions [45006805145](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006805145): **SUCCESS**. Identyczny SHA źródła rozdziału na gałęzi i w zakończonym przebiegu CI.
- Pełny skrypt: **213 stron**; PDF samego rozdziału 27: **9 stron** (strony pełnego PDF 205–213). Wszystkie dziewięć stron wyrenderowano i przejrzano wizualnie, w tym rysunek i jego podpis; bez nachodzenia napisów, uciętych wzorów i przekroczeń marginesów.
- Log kompilatora: **0** przepełnień `Overfull \hbox`; **1** niewielkie ostrzeżenie `Underfull \hbox` bez wpływu na czytelność; **2** oczekiwane wystąpienia niezdefiniowanego odsyłacza `ch:ordinals`, bez innych brakujących referencji.

## Werdykt końcowy

**ROZDZIAŁ 27 — STABILNY po audycie VI.**

Audyty I–V przyniosły konkretne poprawki matematyczne i redakcyjne; audyt VI był ponowną niezależną iteracją bez korekt źródła, z zielonym CI i kontrolą wizualną. Nie rozpoczęto prac nad rozdziałem 28.
