# Algebra liniowa — rozdział 08, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/08-odwzorowania-wieloliniowe.tex`  
**Sprawdzona wersja wejściowa:** `25cf3d2212b4917b57aa38c0a58a92b6b4729f32`

## Ponowna kontrola dowodów

Skontrolowano niezależnie wszystkie sekcje rozdziału: definicję wieloliniowości, liniowość w poszczególnych argumentach, konstrukcję z wartości na bazach, obliczanie wymiarów, prawo zmiany współczynników przy zmianie baz, formy dwuliniowe, kongruencję i radykały, symetrię i naprzemienność w dowolnej charakterystyce, bazę form naprzemiennych, operatory symetryzacji i alternowania oraz wzór polaryzacyjny.

- Wymiary `m ∏ n_r`, `binom(n+k−1,k)` i `binom(n,k)` wynikają z jawnego zliczenia niezależnych wartości na krotkach wektorów bazowych; żadne twierdzenie nie używa niejawnego dzielenia przez `k!`.
- Prawo przekształcania macierzy formy `A_C=P^T A_B P` jest zgodne z konwencją zmiany bazy poprzednich rozdziałów; radykały odpowiadają `ker A^T` oraz `ker A`.
- Antysymetria i naprzemienność są poprawnie rozróżnione dla `char K=2`; dowód alternowania wykorzystuje bezpieczne parowanie składników.
- W polaryzacji udowodniono kasowanie wyrazów ze zbiorami indeksów mniejszymi od `{1,...,k}` oraz właściwy współczynnik `k!`. Obowiązywanie tożsamości nie jest uzależnione od jego odwracalności; tylko odtwarzanie formy wymaga `k!1_K !=0_K`.
- Uwzględniono zerowe przestrzenie, `k=0`, `k>n` i formy o wartościach wektorowych.

## Niezależne testy

- Dla `p=2,3`, `n=1,2,3`, `k=2,3`: **12 konfiguracji**. Obliczono rzędy układów warunków liniowych i potwierdzono oba wzory wymiarowe, zero rozbieżności.
- Wzór polaryzacyjny form trójliniowych nad `F_2^2` (1024 przypadki) oraz nad `F_3^2` (59049 przypadków): **60073 kontrole**, zero rozbieżności.
- Prawo kongruencji dla form dwuliniowych: **8000 testów** dla czterech ciał `F_2,F_3,F_5,F_7`, wymiarów `1...4`, losowych odwracalnych zmian baz i różnych wektorów: zero rozbieżności.
- Kontrola statyczna rozdziałów 01–08: **346 unikalnych etykiet i 140 odsyłaczy**, wszystkie rozwiązywane; brak błędów zagnieżdżania środowisk i niedozwolonej terminologii.
- Początkowe GitHub CI dla rozdziału 08: [kompilacja](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44911689642), [CLI](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44911689614) oraz [testy aplikacji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44911689637) zakończyły się sukcesem. Książka ma 85 stron, końcowy log kompilacji bez ostrzeżeń.

## Korekta

W dowodzie o wymiarze przestrzeni wieloliniowych poprawiono określenie odsyłacza z `Wynik` na `Twierdzenie`. Jest to wyłącznie korekta redakcyjna, bez zmiany matematyki.

**Status:** nie wykryto istotnych błędów; rozdział 08 nadal otwarty do czystej kontroli po korekcie redakcyjnej i nowej walidacji CI.
