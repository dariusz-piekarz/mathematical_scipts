# Algebra liniowa — rozdział 18, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Tekst:** `chapters/pl/linear_algebra/18-rozklad-jordana-chevalleya-i-funkcje-macierzy.tex`  
**Blob zatwierdzanego rozdziału:** `ef815633cf3a1f795d912c510fbc8575f21e464d`  
**Poprzednie iteracje:** `ch18_iteration_01.md`, `ch18_iteration_02.md`.

## Niezależne sprawdzenie dowodów i przykładów

1. **Wielomianowe rzuty na uogólnione przestrzenie własne.** Wielomiany `f_λ=(t-λ)^a_λ` oraz `g_λ=m_T/f_λ` są względnie pierwsze, więc tożsamość Bézouta daje wielomian `q_λ` z odpowiednimi kongruencjami. Na `W_λ=ker f_λ(T)` działa on jako identyczność, na pozostałych przestrzeniach jako zero. Wynik jest niezależny od wybranego wielomianu; z działania na składnikach wynikają `P_λ²=P_λ`, `P_λP_μ=0`, `sum P_λ=I`, `im P_λ=W_λ` i komutowanie z `T`. Przy `V=0` poprawne są konwencje pustych sum.
2. **Rozkład Jordana–Chevalleya.** Operator `S=sum λP_λ` jest diagonalizowalny, ponieważ ogranicza się do skalara `λ` na każdym `W_λ`. Operator `N=T-S` jest nilpotentny, ponieważ `(T-λI)^a_λ=0` na `W_λ`; jego wykładnik nilpotentności można wziąć jako maksimum skończonej liczby `a_λ`. Oba operatory są wielomianami w `T`, więc przemieniają się. Jednoznaczność wynika z faktu, że dla dowolnego drugiego rozkładu `S'+N'`, każda przestrzeń własna `S'` zawiera się w odpowiedniej uogólnionej przestrzeni własnej `T`; bezpośredniość rozkładu wyznacza `S'` na każdym składniku i wymusza `S'=S`.
3. **Współczynniki wielomianów nad dowolnym ciałem.** Współczynniki `p^[j](λ)` są określone współczynnikowo przez `p(λ+u)`, bez dzielenia przez silnie w dodatniej charakterystyce. Przypadek `p=0` jest zdefiniowany osobno i nie używa stopnia wielomianu zerowego. Formuła `p(T)=sum p^[j](λ) N^jP_λ` jest rachunkiem wielomianowym na nilpotentnych składnikach i obowiązuje dla każdego ciała.
4. **Potęgi i odwrotność.** Wzór dwumianowy i interpretacja jego współczynników w `K` uzasadniają formułę dla `T^k`. Uwzględniono `k=0`, w tym jedyną wartość wielomianu stałego przy zapisie `0^0=1`. Gdy wszystkie wartości własne są niezerowe, skończony szereg geometryczny daje odwrotność `(λI+N)^(-1)` na każdym `W_λ`. Sumowanie po rzutach daje odwrotność globalną.
5. **Rachunek holomorficzny nad `C`.** Wzór `f(T)=sum f^(j)(λ)/j! N^jP_λ` zależy od skończonych dżetów funkcji w wartościach własnych. Przez rozwinięcie Taylora modulo `u^a_λ` wykazano `(fg)(T)=f(T)g(T)`; działania dla funkcji stałej i identycznościowej oraz zgodność z wielomianami mają uzasadnienie. Jeśli `f` nie zeruje się na widmie, funkcja `1/f` jest holomorficzna w pewnym otoczeniu tego skończonego zbioru, więc rzeczywiście `(1/f)(T)=f(T)^(-1)`.
6. **Wykładnicza.** Szereg `sum z^kT^k/k!` jest absolutnie zbieżny w każdej operatorowej normie skończenie wymiarowej; po rozkładzie `T|W_λ=λI+N` zamiana sumowań jest dozwolona, bo liczba potęg `N` jest skończona, a pozostałe szeregi są bezwzględnie zbieżne. Współczynnik `binom(h+j,j)/(h+j)!` jest równy `1/(h!j!)`; otrzymujemy `e^{zλ}sum (z^j/j!)N^jP_λ`. Własność grupowa i odwrotność wynikają z multiplikatywności rachunku funkcji.
7. **Przykłady.** Zweryfikowano wielomian rzutu `q_3=(t-1)^2/4` nad `Q`, przemienność `S,N`, wzór `J_3(1)^k` także w charakterystyce 2 oraz bezpośrednie podstawienie rozwiązania `x(t)=e^{2t}(t²/2,t,1)` do `x'=J_3(2)x`.
8. **Referencje i struktura.** Po korekcie terminologii zachowano wszystkie stabilne etykiety; rozdział ma 21 unikatowych etykiet, 13 odsyłaczy do istniejących miejsc i 6 par środowisk `proof`. Nie wykryto nowych luk matematycznych ani problemów redakcyjnych. Nie dodano twierdzeń ani przykładów.

## Terminologia globalna

- W `AGENTS.md` oraz `docs/pl/standardy_terminologiczne.md` dopisano obowiązkową regułę: wielomian **rozkłada się na czynniki**. Należy jawnie wymieniać ciało, nad którym występuje rozkład na czynniki liniowe.
- Przejrzano **403 kanoniczne rozdziały TeX** i **79 pozostałych plików TeX**. Poza algebrą liniową nie wykryto dodatkowych niepoprawnych sformułowań w odniesieniu do wielomianów. Prawidłowe terminy dotyczące ciągów dokładnych, morfizmów, wiązek i innych konstrukcji pozostawiono nietknięte.
- W algebrze liniowej zmieniono wyłącznie sformułowania w rozdziałach **14, 16, 17 i 18**, bez ingerencji w matematykę ani w nazwy etykiet LaTeX.
- Utworzono `tools/check_polynomial_terminology.py` obejmujący `chapters/pl` oraz `sources/pl`; test podłączono do workflow. Historyczne raporty audytowe traktujemy jako zapisy poprzednich iteracji.

## CI i PDF

- [GitHub Actions 44938888246](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44938888246) — pełna kompilacja z ostateczną korektą tekstu i testami, **success**.
- [GitHub Actions 44939464083](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44939464083) — **success**, w tym nowy globalny test terminologii, testy rachunku funkcji macierzy, dwukrotna kompilacja LaTeX, walidacja odsyłaczy i eksport PDF rozdziału.
- Wygenerowano **8-stronicowy PDF wyłącznie rozdziału 18** z ostatniego przebiegu. Zweryfikowano 8 niepustych stron, 0 bloków poza obszarem strony, kompletność wzorów i wygląd wszystkich stron w zestawieniu renderów.

## Decyzja

**Audyt III — czysty matematycznie.** Jedyną zmianą w stosunku do poprzedniego audytu była globalna korekta językowa, bez zmian w twierdzeniach, dowodach lub przykładach. Kompilacja, testy oraz PDF są poprawne. **Rozdział 18 uznany za stabilny po trzech audytach.** Rozdziały 01–18 stabilne; następny nowy rozdział powinien powstać osobno, bez poszerzania zakresu zatwierdzonego rozdziału.
