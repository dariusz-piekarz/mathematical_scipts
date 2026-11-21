# Algebra liniowa — rozdział 23, audyt I (powstanie i wstępna kontrola)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/23-dyskretne-rownanie-lapunowa-i-stabilnosc-schura.tex`  
**Przed rozpoczęciem:** rozdziały 01–22 stabilne, [CI 44945228873](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945228873) — SUCCESS.  
**Status:** rozdział 23 **w audycie**, nie zatwierdzony.

## Zakres i uzasadnienie kolejności

Rozdział kontynuuje równanie Lapunowa z rozdziału 22, ale dla czasu dyskretnego. Zawiera osobne definicje stabilności Schura i promienia spektralnego, dowód zaniku potęg przez postać Jordana, dyskretne twierdzenie Lapunowa, energię dyskretną z oszacowaniem geometrycznym, kryterium odwracalności operatora Steina bez dodatniej określoności oraz porównanie dokładnego próbkowania z jawną metodą Eulera.

## Audyt matematyczny I

1. **Macierz Schura:** `rho(A)<1` jest równoważne `A^k→0`, a nawet `||A^k||≤Mr^k` dla `rho(A)<r<1`. Dowód używa wzoru dwumianowego dla dowolnego bloku Jordana, również przy `lambda=0`.
2. **Dyskretne równanie Lapunowa:** szereg `P=∑(A*)^k Q A^k` jest bezwzględnie zbieżny z geometrycznego oszacowania potęg; wyraz `k=0` gwarantuje `P≥Q>0`. Przesunięcie indeksu daje `A*PA-P=-Q`.
3. **Jednoznaczność:** różnica rozwiązań w całej przestrzeni macierzy spełnia `D=(A*)^k D A^k`; norma prawej strony dąży do zera. Nie jest potrzebne założenie hermitowskości obu rozwiązań.
4. **Konieczność stabilności:** dla wektora własnego `Av=lambda v` równanie daje `(|lambda|²-1)v*Pv=-v*Qv`; dodatnia określoność wymusza `|lambda|<1`.
5. **Energia:** `E_(k+1)-E_k=-x_k*Qx_k`, ścisły spadek tylko dla `x_k≠0` (uwzględnia przypadek nilpotentny), oraz `E_k≤gamma^k E_0` dzięki porównaniu norm hermitowskich.
6. **Widmo operatora Steina:** zastosowanie Schura, bazy `E_ij` i trójkątności macierzy `X↦T*XT` daje dokładnie iloczyny `conj(lambda_i)lambda_j`. Ich brak równości 1 jest kryterium jednoznaczności dla każdego `Q`, niekoniecznie kryterium stabilności.
7. **Część ciągła/dyskretna:** dokładne próbkowanie `e^{hH}` zachowuje stabilność Hurwitza dla każdego `h>0`; jawna metoda Eulera wymaga `2Re lambda+h|lambda|²<0`. Wektor własny i wyznacznik wyprowadzają pełny zestaw wartości własnych `I+hH`.
8. **Rachunki:** przykład nie-normalny `A=[[1/2,1/2],[0,1/4]]` ma dokładnie `P=[[4/3,8/21],[8/21,32/21]]`. Niezależny rachunek na liczbach wymiernych potwierdza `A^TPA-P=-I` i `det P=832/441`.

## Pierwsza poprawka

W oszacowaniu potęg Jordana zamieniono `1+k^(d-1)` na `(1+k)^(d-1)`, aby wykluczyć niejednoznaczny zapis `0^0` w przypadku `d=1, k=0`. Nie zmieniono tezy lematu.

## Regresje i dalszy plan

Utworzono `tools/test_linear_algebra_discrete_lyapunov.py` dla testów nad `F2,F3` oraz dokładnej arytmetyki wymiernej. Integracja z punktem wejścia, katalogiem i GitHub Actions jest wykonana. Następne kroki: pełne CI, sprawdzenie definicji, języka i odsyłaczy, osobny PDF, kolejne niezależne audyty aż do dwóch kolejnych czystych po ostatniej zmianie.

**Decyzja:** audyt I zawierał poprawkę, nie jest czysty.
