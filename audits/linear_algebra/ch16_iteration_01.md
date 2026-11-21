# Algebra liniowa — rozdział 16, audyt I (nowy rozdział)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/16-podprzestrzenie-niezmiennicze-i-wielomian-minimalny.tex`  
**Ostatnio sprawdzony blob:** `e84aa39318ece4cd5bcf92be547767e1aaad0fa5`  
**Poprzedni etap:** audyt V rozdziału 14 (`audits/linear_algebra/ch14_iteration_05.md`).

## Zakres i weryfikacja matematyczna

1. **Podprzestrzenie niezmiennicze.** Poprawnie rozróżniono `T(W) ⊆ W` od `T(W)=W`; weryfikacja jąder, obrazów wielomianów i działań na podprzestrzeniach wykorzystuje komutowanie `p(T)` z `T`. Operator ilorazowy jest dobrze określony. Blokowy wzór `chi_T=chi_{T|W}chi_{bar T}` jest poprawny także przy `W=0` i `W=V`; przykład bloku Jordana dowodzi braku niezmienniczego dopełnienia.
2. **Przestrzenie cykliczne.** Minimalność `K(T,v)`, stabilizacja potęg oraz wyprowadzenie minimalnego monicznego `m_{T,v}` opierają się na liniowej niezależności wektorów `v,...,T^{d-1}v`. Poprawiono interpretację rozpiętości pustej rodziny przy `v=0` i macierz towarzyszącą przy `d=1`.
3. **Wielomian minimalny operatora.** Istnienie udowodniono z `dim End(V)=n^2`, jednoznaczność i podzielność z algorytmu dzielenia przez moniczny wielomian, a wzór jako moniczna najmniejsza wspólna wielokrotność wielomianów minimalnych wektorów bazowych — z ich definicji. Przypadek `V=0` ma `m_T=1`.
4. **Cayley--Hamilton.** Pełny dowód przez macierz dołączoną nad przemiennym `K[t]` i porównanie współczynników unika niepoprawnego podstawiania macierzy do tożsamości wielomianowej nad pierścieniem macierzy. Doprecyzowano, dlaczego tożsamość z rozdziału 6 obowiązuje nad `K[t]`. Wynik `m_T|chi_T` i zgodność pierwiastków w `K` są uzasadnione.
5. **Rozkład pierwotny.** Lemat Bézouta dla `p(T)q(T)=0` jest poprawny. W pierwotnym szkicu wykryto skrót indukcyjny: ograniczenie operatora do jądra iloczynu czynników nie musi mieć dokładnie tego iloczynu jako wielomianu minimalnego. Naprawiono dowód przez kolejne stosowanie dwuczynnikowego lematu do operatora na coraz mniejszej podprzestrzeni, przy zachowaniu założenia o zerowaniu przez odpowiedni iloczyn.
6. **Uogólnione przestrzenie własne.** Stabilizację jąder `ker((T-lambda I)^k)` wyprowadzono z rozkładu Bézouta dla `(t-lambda)^a` i `g` oraz odwracalności `T-lambda I` na `ker g(T)`. W definicji pozostawiono wyłącznie właściwy opis przestrzeni, a własność stabilizacji udowodniono osobno.
7. **Kryterium diagonalizowalności.** Równoważność `T` diagonalizowalny nad `K` oraz `m_T` będący iloczynem różnych czynników liniowych `nad K` poprawnie uwzględnia konieczność rozszczepienia wielomianu; rzeczywista macierz obrotu dostarcza kontrprzykładu do słabszego warunku braku powtórzonych czynników nierozkładalnych.

## Integracja i testy

- Rozdział 16 dodano do `books/pl/linear_algebra.tex`, `catalog/books.json` i do jawnego wykazu 16 plików w `.github/workflows/linear-algebra-chapter.yml`.
- Dodano `tools/test_linear_algebra_invariant.py` do CI. Test wyczerpująco obejmuje wszystkie macierze `2x2` nad `F_2` i `F_3`: tożsamość Cayleya--Hamiltona, podzielność wielomianu charakterystycznego przez minimalny, kryterium diagonalizacji, niezmienniczość prostych własnych i wektory cykliczne.
- W pierwszej kontroli stwierdzono **30 unikatowych etykiet, 17 odsyłaczy i 12 prawidłowo zamkniętych dowodów**. Zweryfikowano niesprzeczność nazw i poprawne odwołania do wcześniejszych rozdziałów.
- Wstępny workflow po integracji oraz dołączeniu testów [GitHub Actions 44933803169](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44933803169) zakończył się sukcesem: testy, kompilacja pełnego tomu i eksport osobnego PDF. Ostateczny przebieg zawierający ostatnie doprecyzowanie o macierzy dołączonej: [44934049446](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934049446); status tego przebiegu wymaga osobnej kontroli po ukończeniu.
- Wstępny 8-stronicowy PDF rozdziału 16 poddano oględzinom stron i kontroli współrzędnych tekstu. Nie stwierdzono przycięcia tekstu ani kolizji; ostateczna wersja PDF wymaga ponownego oglądu po ostatniej poprawce.

## Decyzja

**Audyt I — wykrył i usunął kilka luk/precyzowań, dlatego rozdział 16 ma status „w audycie”, nie „stabilny”.** W następnej iteracji należy ponownie przejść cały rozdział niezależnie, w szczególności dowody minimalności i rozkładu pierwotnego, a następnie skontrolować najnowszy PDF i CI. Rozdziały 1–15 pozostają stabilne.
