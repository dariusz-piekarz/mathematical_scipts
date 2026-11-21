# Algebra liniowa — rozdział 20, audyt I (nowy rozdział)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/20-dzielniki-elementarne-i-bloki-pierwotne.tex`
**Stan początkowy:** rozdział 19 stabilny po czterech audytach; nowy rozdział 20 jest **w audycie**.

## Zakres utworzonego tekstu

1. Definicja dzielników elementarnych jako potęg nierozkładalnych wielomianów z czynników niezmienniczych, z krotnościami i normalizacją moniczną.
2. Chińskie twierdzenie o resztach dla pierścienia \`K[t]\`, z pełnym dowodem injektywności, surjektywności i konstrukcją wielomianów idempotentnych modulo czynników.
3. Istnienie i jednoznaczność postaci blokowej przez \`C(p^a)\`; odwrotna rekonstrukcja czynników niezmienniczych przez dopełnianie wykładników zerami z lewej.
4. Wzory na wymiar, wielomian charakterystyczny i minimalny oraz kryterium podobieństwa.
5. Formuły \`D_{p,k}=deg(p) Σ min(k,a)\` i jej różnic, pozwalające z jąder \`p(T)^k\` obliczać dokładne liczby bloków.
6. Jawna zmiana bazy między \`C((t-λ)^a)\` i \`J_a(λ)\`, bez założenia charakterystyki zero.
7. Przykłady: bloki nilpotentne, diagonalna \`diag(1,1,2)\`, bloki \`t²+1\` nad \`R\`, blok nierozkładalny nad \`F2\` i różne bloki o wspólnych \`χ,m\`.

## Kontrole do zamknięcia

- Uruchomić \`tools/test_linear_algebra_elementary.py\`, zwłaszcza odtworzenie czynników niezmienniczych i test wymiarów jąder nad małymi ciałami.
- Zweryfikować GitHub Actions, dwukrotną kompilację książki, odsyłacze i odrębny PDF 20.
- Powtórzyć niezależny audyt matematyczny i językowy aż do uzyskania dwóch kolejnych czystych kontroli.

**Decyzja:** wersja 0.1, rozdział 20 otwarty do audytu II. Nie traktować utworzenia tekstu jako potwierdzenia stabilności.
