# Algebra liniowa — rozdział 16, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/linear_algebra/16-podprzestrzenie-niezmiennicze-i-wielomian-minimalny.tex`  
**Niezmieniony blob rozdziału od audytu II:** `1874f4774a038e32ccc53dec543ce1c2c8b39a28`  
**Poprzednie audyty:** `ch16_iteration_01.md`, `ch16_iteration_02.md`.

## Ponowna niezależna kontrola

1. **Założenia i przypadki brzegowe.** Rozdział obowiązuje nad dowolnym ciałem; we wszystkich wynikach skończoność wymiaru jest jawna lub wynika z globalnego założenia. Poprawnie rozpatrzono `V={0}`, `W=0`, `W=V`, `v=0`, `d=1`, `r=1,2`, charakterystykę 2, puste sumy i iloczyny.
2. **Niezmienniczość i operator na ilorazie.** Dobrze określono `bar T(v+W)`; blokowa postać `[[A,B],[0,C]]` poprawnie identyfikuje wielomian charakterystyczny ograniczenia i ilorazu. Kontrprzykład do niezmienniczego dopełnienia nie zakłada błędnie, że każda podprzestrzeń ma takie dopełnienie.
3. **Przestrzenie cykliczne.** Dowód minimalnego `d` wykorzystuje liniową zależność `n+1` wektorów; po pierwszej relacji wszystkie dalsze potęgi należą do wcześniej wygenerowanej podprzestrzeni. Wielomian `m_{T,v}` ma stopień `d`, a dzielenie z resztą daje dokładnie `m_{T,v}|p`. Macierz towarzysząca została zdefiniowana współrzędnymi, również dla `d=1,2`, i zweryfikowana w testach.
4. **Wielomian minimalny operatora.** Istnienie i jednoznaczność udowodniono bez założenia algebraicznego domknięcia `K`. Równość `m_T=lcm(m_{T,v_i})` wykorzystuje osobno fakt, że `p(T)` zeruje każdy element bazy wtedy i tylko wtedy, gdy jest operatorem zerowym.
5. **Twierdzenie Cayleya–Hamiltona.** Tożsamość macierzy dołączonej nad `K[t]`, porównanie współczynników i prawidłowe mnożenie przez potęgi `A` z lewej dają `χ_T(T)=0`, bez niedozwolonego podstawienia macierzy do `adj(tI-A)`. Wynik `m_T|χ_T` nie zależy od rozszczepienia wielomianu.
6. **Pierwotny rozkład.** Lemat Bézouta działa także przy stałych wielomianach. W dowodzie rozkładu na jądra wielomianów `p_j(T)^{a_j}` przypadki `r=1`, `r=2` i `r>=3` są rozdzielone. Każdy kolejny krok odbywa się na podprzestrzeni niezmienniczej, na której odpowiedni iloczyn wielomianów zeruje ograniczenie.
7. **Uogólnione przestrzenie własne.** Kierunki lewa/prawa odwrotność `u(T)` względem `T-λI` są odróżnione i uzasadnione przemiennością wielomianów w `T`. Rozkład `V=ker((T-λI)^a)⊕ker g(T)` dowodzi stabilizacji jąder. Z rozkładu pierwotnego wynika dokładnie rozkład na uogólnione przestrzenie własne przy rozszczepieniu.
8. **Diagonalizowalność.** Kryterium przez `m_T` wymaga różnych **liniowych** czynników nad danym ciałem. Kontrprzykład obrotu nad `R` poprawnie oddziela brak powtórzeń irreducybilnych od rozszczepienia nad `K`.
9. **Język, odsyłacze i typografia.** Sprawdzono rozdział zawierający 5 definicji, 6 twierdzeń, 1 lemat, 3 stwierdzenia, 2 wnioski, 5 przykładów, 1 uwagę i 12 dowodów. Ma 30 różnych etykiet i 17 odsyłaczy; nie wykryto niezamkniętych środowisk, kolizji etykiet, angielskiego rzeczownika „dual” ani błędów terminologicznych.
10. **PDF.** Zweryfikowano artefakt rozdziału 16 z przebiegu 44934636481. Osiem stron zostało wyrenderowanych, wszystkie zawierają tekst, żaden blok nie wychodzi poza obszar strony, a w przeglądzie wizualnym nie stwierdzono kolizji. Porównanie z PDF audytu I pokazuje zmiany na pięciu stronach bez zmian w całkowitej liczbie stron.

## CI i testy

- [Przebieg 44934636481](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934636481): sukces dla skorygowanego tekstu, w tym pełny LaTeX, kontrola odsyłaczy, testy macierzy i eksport PDF.
- [Przebieg 44934853492](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934853492): sukces również po wzmocnieniu testów uogólnionych przestrzeni własnych przy powtarzających się wartościach własnych.
- Regresja 3×3 obejmuje 512 macierzy nad `F_2`, 500 deterministycznie wybranych macierzy nad `F_3` oraz 53 macierze towarzyszące stopni 1–3. Nie znaleziono błędów.

## Decyzja

**Audyt III: czysty, bez potrzeby kolejnych zmian rozdziału.** Matematyka, redakcja, testy i PDF są stabilne. Rozdział 16 uznany za **stabilny po trzech audytach** i może być traktowany jako zamknięty na obecnym etapie. Po rozdziałach 01–16 kolejnym etapem jest rozdział 17; nowe twierdzenia dodawać tylko do nowego rozdziału, a nie do ustabilizowanego rozdziału 16.
