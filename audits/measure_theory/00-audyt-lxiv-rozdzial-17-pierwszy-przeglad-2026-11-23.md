# Audyt LXIV (64) — rozdział 17: pierwszy szczegółowy przegląd i bramka regresji

Data: 2026-11-23. Repozytorium: `dariusz-piekarz/mathematical_scipts`. Istniejąca gałąź: `biblioteka-matematyczna-iteracja-6`.

**Punkt startowy:** rozdział 16 zamknięty w audycie LXIII (63), po rzeczywistym przebiegu [GitHub Actions 45253108348](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45253108348). W bieżącej iteracji audytowano wyłącznie rozdział 17; nie zaczęto kontroli rozdziału 18.

## Kontrola treści i zależności

Plik: `chapters/pl/measure_theory/17-bezwzgledna-ciaglosc-osobliwosc-i-rozklad-lebesguea-miar.tex`, **nowy blob: `e8c27586b79374f799533adf99e39b90725ddc25`**.

Przeczytano całość rozdziału (bezwzględna ciągłość, równoważność miar, osobliwość, kryterium epsilon–delta, niezależny od Radona–Nikodyma dowód rozkładu Lebesgue'a dla miar skończonych, uogólnienie sigma-skończone, rozkład miary zespolonej, miara Cantora oraz rozkład atomowy i bezatomowy). Kluczowe punkty kontroli:
- w konstrukcji rozkładu skończonych miar poprzez Hahn dla `nu - 2^k mu` próg dodatni daje `mu(P_k) <= 2^{-k} nu(X)`, więc `S = limsup P_k` ma `mu(S)=0`; z nierówności na `N_k` wynika `nu(E\S)=0` dla każdego zbioru `mu`-zerowego. Nie zakłada się tu istnienia gęstości;
- epsilon–delta wykorzystuje skończoność `nu`, nie wymaga skończoności `mu`. Przykład przyjmujący tylko wartości 0 i nieskończoność pokazuje konieczność hipotezy;
- gluing dla miar sigma-skończonych opiera się na przeliczalnym, rozłącznym podziale przez wspólne zbiory skończone w obu miarach;
- rozróżniono atomowe i osobliwe bezatomowe części miary na prostej.

**Dwie uzupełnione luki ekspozycyjne**, commit `d7e3685369f1516be3c00fd2ce4debef411bbec4`:
1. Dowiedziono obu implikacji dla równoważności `dnu=x dλ` i `dmu=dλ` na (0,1), jawnie używając zbiorów `E_n = E ∩ {x>=1/n}` i przejścia do sumy przeliczalnej.
2. W przykładzie miary Cantora każdy przedział podstawowy poziomu `n` skojarzono z prefiksem cyfr dwójkowych; pokazano dokładną miarę `2^{-n}` przez przeciwobraz przedziału dwójkowego tej długości (nie licząc przeliczalnych końców). Stąd brak atomów, przy skupieniu miary na zbiorze Cantora miary Lebesgue'a zero.

**Kontrola źródła:** 14/14 unikalnych etykiet, 9 odwołań, 30/30 par środowisk prawidłowo zagnieżdżonych, brak zakazanych oznaczeń funkcji charakterystycznych. W zależnościach między rozdziałami 16, 17, 18 każda z 9 referencji znajduje deklarację (4 różne etykiety zewnętrzne: trzy z rozdziału 16 i jedna przyszła z 18). Ta statyczna kontrola nie stanowi kompilacji ani formalnego dowodu matematycznego.

## Trwałe testy i kompilacja CI

Utworzono `tools/tests/test_measure_theory_ch17.py`, **8 przypadków unittest**, commit `d32c997bf32b9e9684a30c1b3c9582dc0058824a`, blob `1fd1971e1caaa223f07bb4e4ac2a197e2c6ca91c`:
- miary równoważne i kryterium epsilon–delta na przestrzeniach atomowych;
- progi Hahna `nu-2^k mu` oraz rozkład Lebesgue'a na skończonych modelach;
- jednoznaczność podziału na część osobliwą i bezwzględnie ciągłą;
- sklejanie lokalnych rozkładów na rozłącznych częściach;
- złożone miary i wariacja całkowita;
- prefiksy dwójkowe i trójkowe w konstrukcji miary Cantora;
- jawny przykład mieszanej części gęstościowej i atomowej;
- kompletność odsyłaczy 16–18, zagnieżdżenie TeX i brak kołowego użycia Radona–Nikodyma.

Utworzono oddzielny workflow `.github/workflows/measure-theory-ch17.yml`, commit `a65aa304ec7403bd9ee5e965b6b8f47dd4ffe974`, blob `30f7646af9814b46f860d5912c0faa3803a684ee`. Dwa niezależne joby: 8 nowych testów + 4 testy integralności całego tomu oraz budowa 31-rozdziałowej książki i osobnego PDF rozdziału 17. Osobny PDF importuje tylko naprawdę potrzebne etykiety z AUX całej książki przez `xr-hyper`, w tym odwołanie naprzód do rozdziału 18; własne etykiety są wykluczane, numer rozdziału zachowany. Dodatkowe zadanie publikuje osobne statusy `measure-theory/ch17-regressions` i `measure-theory/ch17-pdf`, przy odnotowaniu `run_id`.

## Werdykt i otwarte warunki

Pierwszy przegląd matematyczny rozdziału 17: zakończony, poprawki wykonane.
Nowe testy i workflow: zapisane w tej samej gałęzi.
**CI niezweryfikowane w chwili zamykania audytu:** zapytania o klasyczne statusy na commicie `a65aa304ec7403bd9ee5e965b6b8f47dd4ffe974` zwracały pustą listę. Nie oznacza to sukcesu ani porażki.
**Rozdział 17: W STABILIZACJI.** Do zamknięcia potrzebne są rzeczywiste wyniki 8+4 testów, oba PDF-y, logi bez nierozwiązanych odsyłaczy, niezależny przegląd matematyczny oraz oględziny stron (zwłaszcza przykładu Cantora i końcowej strony). Nie przechodzić do rozdziału 18 przed zamknięciem 17.
