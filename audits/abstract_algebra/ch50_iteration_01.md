# AA-50 — audyt I: definicje, tożsamości i rozdzielenie zakresów

**Data:** 23 listopada 2026 r.
**Werdykt:** W AUDYCIE — NIE STABILNY.
**Rozdział:** chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex.
**Plan:** docs/pl/zakres_aa50_kovacic_skonczone_grupy.md.

## Sprawdzane zobowiązania matematyczne

1. Postać normalna z''=qz, q∈C(x); wyraźny model obliczeń. Rząd w nieskończoności deg mianownika−deg licznika dla q≠0. Dla q=0 wcześniejszy przypadek wymierny dostarcza rozwiązanie.
2. Klasyfikacja prymitywnych skończonych grup A4,S4,A5 oraz n∈{4,6,12} jest **cytowana** z klasycznej teorii. Nie przedstawiać przykładu A4 jako jej dowodu.
3. Klasyczne konieczne warunki lokalne: skończone bieguny q rzędu 1 lub 2, ord∞ q≥2; dokładna lista E_c dla prostego bieguna {12}; dla podwójnego: {6+(12k/n)√(1+4b_c): k=-n/2,...,n/2}∩Z. E∞ odróżnia ord∞=2 (używa b∞) i ord∞>2 (√(1+4·0)=1). Każdy kandydat jest dokładną liczbą całkowitą; nie zaokrąglać.
4. Konstrukcja S=∏(x−c), θ=(n/12)Σ e_c/(x−c), d=(n/12)(e∞−Σ e_c)≥0 całkowite. Ponieważ q ma tylko bieguny proste lub podwójne, S²q i Sθ są wielomianami. Rekurencja P_{n+1}=0, P_n=−P, P_{i−1}=−SP_i'+((n−i)S'−Sθ)P_i−(n−i)(i+1)S²qP_{i+1}, a P_{−1}=0.
5. Wyprowadzenie równania transportu: A_i=S^iP_i/(n−i)!; F=Σ A_iT^i. Współczynnik T^i w δF wynosi A_i'+(i+1)qA_{i+1}−(i−1)A_{i−1}; RHS to −nA_{i−1}+(nS'/S−θ)A_i. Po przeliczeniu dokładnie rekurencja; warunek przy i=0 to P_{−1}=0. Kontrola współczynnika T^{n+1} daje −nA_n po obu stronach.
6. Odzyskiwanie Riccatiego: jeśli F jest wielomianem niekonstantnym w T i δF=HF, każdy nierozkładalny czynnik f dzieli δf. Dowód przez lokalizację lub porównanie wycen przy f. W charakterystyce 0 f_T(w)≠0 dla algebraicznego pierwiastka w; z różniczkowania f(x,w)=0 wynika w'=q−w². Fakt ten nie wymaga wcześniejszej kontroli bezkwadratowości F.
7. Dodatni wynik P_{−1}=0 daje algebraiczny w i lokalne niezerowe z=exp∫w. Brak wszystkich liouvillowskich rozwiązań z wyniku negatywnego trzeciej gałęzi wynika dopiero gdy wcześniejsze gałęzie również nie dały rozwiązania i uwzględniono **cytowaną** pełną klasyfikację.
8. Dokładny przykład czworościenny: q=−3/(16x²)−2/(9(x−1)²)+3/(16x(x−1)); przy 0,1,∞ rzędy 2, b0=−3/16, b1=b∞=−2/9. Dla n=4, E0={3,6,9}, E1=E∞={4,5,6,7,8}, e0=3, e1=4, e∞=7, d=0, θ=1/x+4/(3(x−1)), S=x(x−1). P=1; jawne P4,...,P0 i P−1=0. Klasyfikacja dokładnego typu monodromii jest osobnym klasycznym wynikiem.

## Testy i dalszy rygor

Dwa niezależne zestawy testów (11 SymPy i 10 Fraction), w tym pełna rekurencja na ułamkach wymiernych i równanie transportowe. Testy są potwierdzeniem modeli i regresją, ale nie dowodzą wyczerpujących list lokalnych. Wymagane: niezależny audyt II; korekty, jeżeli testy lub CI wykryją błędy; rzeczywisty pełny CI; PDF i wszystkie strony nowego rozdziału; audyt III.

**NIE STABILNY. AA-51 nieotwarty.**
