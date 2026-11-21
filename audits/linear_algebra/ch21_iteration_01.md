# Algebra liniowa — rozdział 21, audyt I

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/linear_algebra/21-komutant-operatora-i-centralizatory-macierzy.tex`.  
**Wcześniejsze rozdziały:** 01–20 stabilne; nowy rozdział 21 **w audycie**.

## Cel i weryfikacja zakresu

Rozdział bada komutant \(\mathcal C(T)\) i jego odwracalne elementy. Nie powiela dowodów postaci Frobeniusa, Jordana ani bloków pierwotnych. Wcześniejsze planowane zagadnienia wieloliniowe są już obecne w rozdziałach 08–11.

## Audyt matematyczny I

1. **Algebra komutanta.** Sprawdzono zamknięcie na liniowe kombinacje, iloczyny, jedynkę, wielomiany w \(T\), odwrotności elementów odwracalnych i zmianę bazy.
2. **Moduł operatora.** Związek \(ST=TS\) z \(K[t]\)-liniowością wykorzystuje Definicję \(V_T\) z rozdziału 19.
3. **Hom modułów cyklicznych.** Każdy homomorfizm wyznacza obraz \([1]\), który spełnia \(fy=0\pmod g\). Dla \(d=\gcd(f,g)\) i \(g=dg_0\) rozwiązania mają postać \([g_0h]_g\), \(h\pmod d\). Zweryfikowano dwie inkluzje i przypadek \(d=1\).
4. **Operator cykliczny.** Komutant jest \(K[T]\), a wielomian operatora jest odwracalny dokładnie dla względnej pierwszości z \(m_T\). Wymiar komutanta to \(n\).
5. **Wymiar z czynników niezmienniczych.** Rozkład przestrzeni homomorfizmów między sumami modułów daje \(\sum_{i,j}\deg\gcd(f_i,f_j)\). Łańcuch podzielności przekształca go w \(\sum_i(2(r-i)+1)\deg f_i\).
6. **Oszacowania.** \(n\le\dim\mathcal C(T)\le n^2\). Zbadano warunki równości: odpowiednio operator cykliczny i skalarny. Uwzględniono przypadek \(n=1\).
7. **Wzór z dzielników elementarnych.** Dla różnych \(p,q\) Hom zanika; dla tego samego \(p\) wymiar to \(\deg p\cdot\min(a,b)\). Tożsamość licznikowa \(\min(a,b)=\sum_k1_{a\ge k}1_{b\ge k}\) daje sumę kwadratów filtracji i przepis na różnice jąder.
8. **Skończone centralizatory.** Dla cyklicznego operatora nad \(\mathbb F_q\) liczba jednostek wynika z CRT i wykluczenia klas podzielnych przez nierozkładalne czynniki; testowane wartości: \(12\) dla \(C((t^2+t+1)^2)\) nad \(\mathbb F_2\) i \(108\) dla \(J_2(0)\oplus J_1(0)\) nad \(\mathbb F_3\).
9. **Przykłady.** Ujęto blok Jordana, diagonalną o powtórzonych wartościach, obrót rzeczywisty, nilpotentną sumę bloków oraz różne komutanty przy takich samych \(\chi,m\).

## Kryteria stabilności

- Uruchomić niezależny test \(`tools/test_linear_algebra_commutants.py`\) wraz z dotychczasowymi regresjami.
- Sprawdzić kompatybilność katalogu, importów, makr, etykiet, odsyłaczy i zasad terminologii.
- Zbudować pełny PDF, wyeksportować tylko rozdział 21 i zbadać jego strony.
- Powtórzyć niezależne audyty do co najmniej dwóch kolejnych czystych kontroli po ostatniej korekcie.

**Status:** I audyt wstępny; rozdział nie jest jeszcze stabilny.
