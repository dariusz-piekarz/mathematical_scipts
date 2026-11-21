# Algebra liniowa — rozdział 22, audyt I

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Założenia:** rozdziały 01–21 stabilne; rozdział 22 w audycie.

## Zakres i pierwszy przegląd

1. `S_{A,B}(X)=AX-XB` i identyfikacja jądra z przestrzenią homomorfizmów modułów `W_B -> V_A`.
2. Wymiar przestrzeni rozwiązań jednorodnych przez sumę `deg gcd(f_i,g_j)`. Warunek zaniku jądra jest równoważny `gcd(chi_A,chi_B)=1`.
3. Równoważność odwracalności operatora Sylvestera i jednoznacznej rozwiązywalności dla wszystkich macierzy prawej strony.
4. Tożsamość teleskopowa `A^kX-XB^k` i jawna formuła rozwiązania wykorzystująca `chi_A` i odwracalność `chi_A(B)`.
5. Bloki Jordana o różnych wartościach własnych: skończony wzór geometryczny; przy wspólnej wartości własnej liczba parametrów wynosi `min(a,b)`.
6. Nad `C`: twierdzenie Lapunowa o stabilności spektralnej, zbieżności całki `int e^{tA*}Qe^{tA}dt`, dodatniej określoności rozwiązania i implikacji odwrotnej.
7. Przykłady: wspólne widmo i brak jednoznaczności, macierz trójkątna, równanie skalarne, stabilna macierz niediagonalna i macierz niestabilna.

## Weryfikacje wymagane przed stabilizacją

- Uruchomić `tools/test_linear_algebra_sylvester.py` porównujący jądro `AX-XB` z czynnikami Smitha nad `F2,F3`, oraz dokładny rachunek macierzy Lapunowa.
- Zbadać wszystkie symbole/założenia, szczególnie wzór wykonawczy i zbieżność całki.
- Sprawdzić odsyłacze, kompilację CI, ostrzeżenia składu i samodzielny PDF.

**Status:** audyt I, rozdział nie jest jeszcze stabilny.
