# Topologia ogólna — rozdział 21, audyt 03 (pierwsza czysta kontrola nowego bloba)

**Data:** 2026-11-22. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/general_topology/21-topologie-na-rodzinach-podzbiorow.tex.
**Niezmieniony blob:** a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b.
**Wynik:** CZYSTY, **1/2** audytów stabilizacyjnych od ostatniej poprawki.

## Audyt matematyczny — niezależna rekonstrukcja

1. Vietoris jest topologią wyznaczoną podbazą trafienia U^- i zawierania U^+. Baza kształtu \langle U_1,...,U_m\rangle uwzględnia wszystkie skończone przecięcia; gdy warunki dolne są puste, działa \langle V\rangle. Nie korzysta z Hausdorffa.
2. Zanurzenie singletonów j:X→K(X) jest homeomorfizmem na obraz z uwagi na j^{-1}(U^-)=j^{-1}(U^+)=U. Domkniętość obrazu w Hausdorffie otrzymuje się z dwóch rozłącznych warunków trafienia otoczeń różnych punktów.
3. Hausdorff K(X) w topologii Vietorisa wynika z oddzielenia punktu x∈A\B od całego zwartego B przez skończoną rodzinę rozłącznych par otwartych otoczeń.
4. Ciągły obraz zbioru zwartego przez f jest zwarty. Równości przeciwobrazów podbazowych dla K(f) nie wymagają dodatkowych aksjomatów oddzielania.
5. Metryka Hausdorffa: odległość od niepustego zwartego B ma zerowy zbiór dokładnie B, a nierówności typu d(a,C)≤d(a,B)+sup_{b∈B}d(b,C) dają trójkąt.
6. Metr yzacja Vietorisa: dla zwartych K⊂U odległość K od zamkniętego X\U ma dodatnie minimum. Skończone pokrycie K kulami promienia r/3 oraz otwarte r/2-sąsiedztwo K budują otoczenie Vietorisa wewnątrz kuli d_H(K,r).
7. Zupełność: jednostajny limit funkcji odległości f_j=d(.,K_{n_j}) ma niepusty domknięty zbiór zerowy K. Dwa jednostajne oszacowania (budowa łańcuchów z K_{n_j} do K oraz granica f_j na K) dają asymptotyczną bliskość. Zwarta K wynika dopiero z całkowitej ograniczoności i zupełności. Następnie oryginalny ciąg Cauchy'ego zbiega.
8. Zwartość K(X) dla zwartej metrycznej X: skończone podzbiory skończonej sieci S aproksymują wszystkie niepuste zwarte K. Dla zwartej Hausdorffa X dowód ultrafiltrowy działa bez metryki.
9. Zwartość Fella na wszystkich domkniętych F⊂X (również pustym) jest poprawnie wywiedziona z kryterium podbazowego Aleksandra i własności skończonych przecięć we wszystkich zwartych C_j. To twierdzenie nie wymaga Hausdorffa X.
10. Lokalna zwartość Hausdorffa X zapewnia Hausdorffa F(X): otwarte W i zwarte C=cl W zawarte w X\G wyznaczają rozłączne otoczenia.
11. Równość Vietorisa i Fella dla zwartej Hausdorffa X wynika z przejścia do dopełnień. Dla R sekwencja {0,n}→{0} w Fellu, ale d_H=n; kontrprzykład kompletny.

## Statyka i rzeczywista walidacja

- 724 wiersze, 31 różnych etykiet, 9 odsyłaczy: wszystkie mają cele w rozdziałach 07, 14, 18, 21. Brak niezrównoważonych środowisk, \mathscr, podwójnych indeksów dolnych i zabronionych zwrotów polskich.
- Rzeczywisty [workflow 45042413561](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042413561) ukończył się wynikiem success na commicie 9f02772e1222575964f13b98dd6910d7a71163c3, zawierającym identyczny blob a8e0c4db...
- Przeszły testy modeli rozdziału 21, kompilacja całej książki, osobnego rozdziału 21, kontrola PDF i logów. Artefakt general-topology-ch01-ch21, ID 14761939222.
- Rzeczywisty 7-stronicowy PDF rozdziału 21 wyrenderowano; sprawdzono strony 1–7 w montażu oraz osobno 3, 5, 6. Nie widać nakładek, obciętych etykiet figury ani brakujących wzorów. Log nie zawiera Overfull, Underfull, Missing character, LaTeX Warning ani nieokreślonych odsyłaczy.

**Status rozdziału 21: 1/2, bez zmian w źródle.**
