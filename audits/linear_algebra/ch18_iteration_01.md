# Algebra liniowa — rozdział 18, audyt I

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/18-rozklad-jordana-chevalleya-i-funkcje-macierzy.tex`  
**Blob po poprawkach:** `5d64b18ee632a71fbebec98f5fa1bd6a92164dd3`  
**Poprzedni etap:** rozdział 17 otrzymał status stabilny po audycie III (`audits/linear_algebra/ch17_iteration_03.md`).

## Kontrola matematyczna całego nowego rozdziału

1. **Rzuty na uogólnione przestrzenie własne.** Dla `m_T=∏(t-λ)^a_λ` poprawnie skonstruowano wielomiany `q_λ=u_λ g_λ` z tożsamości Bézouta. Sprawdzono kongruencje modulo każdy czynnik, niezależność rzutów od wyboru wielomianu, idempotentność, rozdzielność obrazów, komutowanie z `T` i sumę równą identyczności. Nie wymagano iloczynu skalarnego ani ortogonalności tych rzutów.
2. **Jordana–Chevalleya.** Operator `S=Σ λP_λ` jest diagonalizowalny na połączeniu baz uogólnionych przestrzeni własnych, a `N=T-S` jest nilpotentny na każdej z nich; wystarcza maksimum wykładników czynników minimalnego wielomianu. Oba są wielomianami w `T`, więc przemieniają się. Jednoznaczność wyprowadzono z zawierania przestrzeni własnych dowolnej konkurencyjnej części `S'` w uogólnionych przestrzeniach własnych `T` i bezpośredniości obu rozkładów.
3. **Ciała o dodatniej charakterystyce.** Współczynniki `p^[j](λ)` definiowane są przez `p(λ+u)`, bez dzielenia przez `j!`. Dzięki temu rachunek wielomianowy, dwumian Newtona, potęgi operatora i wzór na odwrotność obowiązują nad dowolnym ciałem, przy założeniu rozszczepienia `m_T`.
4. **Potęgi i odwrotność.** Sprawdzono rozdzielenie wyrazów z `j≤min(k,a_λ-1)`, konwencję `0^0=1` w przypadku potęgi zerowej, zgodność `T^0=I`, warunek odwracalności `0∉σ_K(T)` i skończony szereg geometryczny na każdym składniku.
5. **Funkcje analityczne nad `C`.** Definicja `f(T)` opiera się na skończenie wielu pochodnych w wartościach własnych i nie wymaga holomorficzności na całej płaszczyźnie. Multiplikatywność wywiedziono z mnożenia obciętych rozwinięć Taylora na nilpotentnych składnikach. W szczególności `1(T)=I`, `id(T)=T`, `p(T)` zgadza się z podstawieniem wielomianu, a `(1/f)(T)` jest odwrotnością `f(T)`, jeżeli `f` nie ma zer w widmie.
6. **Wykładnicza i ODE.** Dla `V` zespolonej pokazano zbieżność bezwzględną szeregu `e^{zT}`, wzór `e^{zλ}Σ(z^j/j!)N^jP_λ` oraz własność grupową. W przykładzie dla `T=J_3(2)` pochodna `e^{2t}(t²/2,t,1)^T` zgadza się z `Tx(t)` i spełniony jest warunek `x(0)=e_3`.
7. **Przykłady i związek z wcześniejszymi rozdziałami.** Sprawdzono `q_3(t)=(t-1)^2/4` nad `Q`, rzuty `P_1,P_3`, rozkład na `S,N`, a także `J_3(1)^k` nad dowolnym ciałem. Wskazano rozdział 14 dla projekcji ortogonalnych i 16–17 dla przestrzeni własnych oraz postaci Jordana.

## Korekty i walidacja

- Poprawiono język (`Ze wzoru`, a nie `Z wzoru`), sformułowanie o sumie rzutów oraz jawnie dodano konwencję `0^0=1` dla potęgi zerowej w wzorze na `T^k`.
- Dodano plik do `books/pl/linear_algebra.tex`, `catalog/books.json`, kontroli 18 rozdziałów w `.github/workflows/linear-algebra-chapter.yml` oraz README.
- Dodano `tools/test_linear_algebra_chevalley.py`, który sprawdza przypadki `2×2` i `3×3` nad `F_2,F_3` (w tym powtarzające się pierwiastki minimalnego wielomianu), rzuty projekcyjne, nilpotentność `N`, diagonalizowalność `S`, wzory na potęgi i odwrotność oraz wykładniczą `J_3(2)`.
- W kontroli strukturalnej stwierdzono **21 różnych etykiet**, **13 odsyłaczy** do poprawnie zadeklarowanych etykiet i **6 sparowanych środowisk `proof`**. Nie stwierdzono niedozwolonych terminów.
- [GitHub Actions 44937404338](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44937404338) — **success** po poprawkach rozdziału i uruchomieniu nowych testów. Zakończono pomyślnie kontrolę katalogu, regresje Jordana–Chevalleya i funkcji macierzy, dwukrotną kompilację tomu, kontrolę odsyłaczy oraz eksport osobnego PDF rozdziału 18.
- Artefakt `linear-algebra-current-chapter` z tego przebiegu ma **7 stron formatu A4**. Wszystkie zawierają tekst; kontrola PyMuPDF wykazała **0 bloków tekstowych wychodzących poza granice stron**. Siedem stron wyrenderowano i sprawdzono wizualnie; nie wykryto kolizji podpisów i wzorów ani przycięć.

## Decyzja

**Audyt I wykrył poprawki językowe i przypadek brzegowy potęgi zerowej, które zostały poprawione.** Rozdział 18 pozostaje `w audycie`, bez statusu stabilnego. W następnej iteracji należy niezależnie sprawdzić wszystkie wyniki bez dopisywania nowych twierdzeń, potwierdzić aktualny PDF tylko tego rozdziału i zakończenie CI.
