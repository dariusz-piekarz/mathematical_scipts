# Audyt 17 nierozwiązanych odsyłaczy geometrii różniczkowej

Data: 20 listopada 2026 r.  
Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Źródło liczb: CI [#44750813302](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44750813302), `unresolved_reference_triage.json` oraz `reference_provenance_audit.json`.

## Zweryfikowany stan

- 355 zaindeksowanych rozdziałów, 5754 różnych nazw etykiet i 305 nazw mających więcej niż jednego właściciela.
- 17 nierozwiązanych wystąpień, **13 różnych nazw celów**, wszystkie ze statusem `missing`, zero nierozstrzygniętych wystąpień `ambiguous`.
- Wszystkie 17 wystąpień pochodzi z geometrii różniczkowej, gdzie zaimportowano `DG-01`–`DG-20` z docelowych 36 rozdziałów.
- 109 testów Python, `OK (skipped=1)`; GitHub Actions zakończone `success`.
- Nie zmodyfikowano kanonicznych źródeł TeX ani pierwotnych etykiet. **Liczba 305 konfliktowych nazw nie oznacza 305 niejednoznacznych cytowań.**

## Wszystkie 17 wystąpień (lokalizacje w bieżącym indeksie)

| Rozdział:wiersz | Etykieta | Wstępne postępowanie |
|---|---|---|
| DG-05:730 | `app:grupy-algebry-macierzowe` | odszukać załącznik lub inny oryginalny cel, nie wymyślać aliasu |
| DG-11:693 | `prz:thur-dop-nil-kontakt` | sprawdzić niezaimportowany przykład |
| DG-11:1452 | `sec:rownanie-diraca` | sprawdzić późniejszy rozdział |
| DG-12:1271 | `subsec:dirac-koneksja` | sprawdzić późniejszy rozdział |
| DG-14:2232 | `sec:algebra-liego` | sprawdzić oryginalny rozdział/sekcję |
| DG-14:2537 | `cor:bochner-vanishing` | sprawdzić późniejszą część teorii Bochnera |
| DG-14:2541 | `cor:hodge-de-rham` | sprawdzić późniejszą część teorii Hodge'a |
| DG-14:4619 | `ch:chern-weil` | sprawdzić rozdział Cherna–Weila |
| DG-14:4622 | `prop:euler-identification-26` | sprawdzić dowód identyfikacji klasy Eulera |
| DG-14:4624 | `lem:angular-form-26` | sprawdzić lemat normalizacyjny |
| DG-14:4704 | `thm:CGB-boundary-26` | **prawidłowy typ twierdzenia dla omawianej formuły z brzegiem; sprawdzić późniejszy cel** |
| DG-16:1200 | `thm:CGB-boundary-26` | **osobna korekta matematycznego uzasadnienia** |
| DG-16:1879 | `ch:grafy-wezly-cztery` | sprawdzić cel poza DG oraz import międzydziedzinowy |
| DG-17:733 | `prz:hodge-dwie-sfery-18` | sprawdzić późniejszy przykład Hodge'a |
| DG-17:1840 | `ch:chern-weil` | sprawdzić rozdział Cherna–Weila |
| DG-17:1888 | `thm:CGB-boundary-26` | **osobna korekta matematycznego uzasadnienia** |
| DG-17:2182 | `thm:CGB-boundary-26` | **osobna korekta matematycznego uzasadnienia** |

Wiersze `DG-14:4704` i `DG-16:1200` cytują tę samą brakującą etykietę, lecz **nie wymagają identycznej poprawki**.

## Zweryfikowane trzy przypadki użycia CGB dla `TS^2`

**DG-16:1200.** W rozdziale o obramowaniu wiązka normalna przekątnej `S^2\subset S^2\times S^2` jest identyfikowana z `TS^2`; brak trywialności uzasadniono liczbą Eulera `2`, powołując się na `thm:CGB-boundary-26`. Wystarczy twierdzenie Cherna–Gaussa–Bonneta dla **zamkniętej** orientowanej powierzchni (`thm:chern-gauss-bonnet`, obecne w DG-14), albo twierdzenie Poincarégo–Hopfa. Sfera nie ma brzegu; cytowanie wersji brzegowej jest niepotrzebnie nietrafne.

**DG-17:1888.** Przykład `prz:sw-sfera-stabilna-21` stwierdza `TS^2\oplus\varepsilon^1\cong\varepsilon^3`, zatem `w(TS^2)=1`, choć `TS^2` nie jest trywialna. Niezależny dowód nietrywialności podano w `DG-17` w przykładzie o funkcji sklejającej (`sec:clutching-16`): liczba nawinięć ma wartość bezwzględną `2`. Alternatywnie jej całkowita klasa Eulera spełnia `\langle e(TS^2),[S^2]\rangle=\chi(S^2)=2`. Referencja do CGB z brzegiem nie jest właściwym uzasadnieniem.

**DG-17:2182.** Przykład samoprzecięcia przekątnej wyprowadza `I(\Delta,\Delta)=2` przez izomorfizm wiązki normalnej z `TS^2` i jej liczbę Eulera. To również zagadnienie **zamkniętej** sfery i może odsyłać do twierdzenia `thm:chern-gauss-bonnet` i wcześniej udowodnionego wzoru wiążącego samoprzecięcie z klasą Eulera; w samym przykładzie istnieje ponadto niezależne obliczenie homologiczne: `[\Delta]=A+B` oraz `(A+B)^2=2`.

**DG-14:4704**: cytowanie brzegowej wersji CGB występuje przy wzorze `\chi(M^{2m})=(2\pi)^{-m}\int_M\operatorname{Pf}(\Omega)+\int_{\partial M}\mathcal B_g`, gdzie **rzeczywiście** potrzebna jest wersja z brzegiem. Nie zamieniać tego cytowania na wersję zamkniętą.

## Rekomendowana kolejność dalszych zmian

1. Pozostawić `DG-14:4704` nierozwiązane do czasu importu i audytu rozdziału dowodzącego twierdzenia CGB z brzegiem.
2. Po potwierdzeniu zakresu twierdzenia `thm:chern-gauss-bonnet` w `DG-14`, skorygować **tylko trzy** cytowania `DG-16:1200`, `DG-17:1888`, `DG-17:2182` z zachowaniem opisanej argumentacji i kontekstu; zgodnie z aktualną polityką nie wykonano automatycznej edycji źródeł.
3. Zweryfikować wszystkie pozostałe nieodnalezione cele w oryginalnych rozdziałach `21`–`36` oraz źródłach międzydziedzinowych; brak nazwy w bieżącym indeksie nie dowodzi jej braku w pełnym skrypcie.
4. Po audycie brakujących rozdziałów: import bez zmiany `\label`/`\ref`, ponowne indeksowanie, pełne porównanie pochodzenia i rzeczywista kompilacja PDF.

Nie utożsamiać powodzenia testów parsera, API ani przeglądarki z dowodem poprawności matematycznej.

## Wykonane poprawki źródeł — kolejna iteracja, 20.11.2026

Po przeglądzie matematycznym zrealizowano trzy korekty docelowej etykiety, **bez zmiany nazw deklaracji `\\label` i bez zmiany argumentacji dowodów**:

| Plik / źródłowy wiersz przed poprawką | Poprzednia etykieta | Docelowa etykieta | Uzasadnienie |
|---|---|---|---|
| `DG-16:1200` | `thm:CGB-boundary-26` | `thm:chern-gauss-bonnet` | Liczba Eulera `TS^2`, zwarta sfera bez brzegu. |
| `DG-17:1888` | `thm:CGB-boundary-26` | `thm:chern-gauss-bonnet` | `e(TS^2)` i jego wartość `2`, analogicznie. |
| `DG-17:2182` | `thm:CGB-boundary-26` | `thm:chern-gauss-bonnet` | Samoprzecięcie przekątnej sprowadza się do `e(TS^2)`. |

Zachowano `DG-14:4704 -> thm:CGB-boundary-26`, ponieważ omawia **rzeczywistą formułę z brzegiem**. Cel `thm:chern-gauss-bonnet` jest zadeklarowany w `DG-14` i zawiera hipotezę `bez brzegu`. Test zabezpieczający to `application/tests/test_dg_cgb_citations.py`.

**Przewidywana zmiana indeksu** (do potwierdzenia w CI po wszystkich commitach): 17 → 14 nierozwiązanych wystąpień; niezmieniona liczba zaimportowanych rozdziałów `20/36`. Potwierdzoną liczbę należy brać z nowego `reference_provenance_audit.json`, nie z tego oczekiwania. Wiersze w powyższej tabeli odnoszą się do lokalizacji sprzed zmiany; pozostałe wystąpienia odsyłaczy są w tej samej okolicy.

Oryginalne rozdziały `21`–`36` nadal nie są dostępne w `chapters/pl/differential_geometry_and_topology`; do ich audytu i importu potrzebna jest pełna zweryfikowana wersja źródłowa. Nie dopisano fikcyjnych etykiet, uzupełnień ani rozdziałów.

## Retest po poprawkach — potwierdzony

[GitHub Actions #44751913713](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44751913713), commit `7311ffe954203c698242999d865113326eadcfd7`: **success**. Indeks: **14** nierozwiązanych wystąpień (wcześniej 17); `resolved=4397` (wcześniej 4394), `included_resolved=2`, `external_resolved=72`, `ambiguous=0`. Nadal 13 nazw brakujących etykiet, ponieważ `thm:CGB-boundary-26` pozostaje prawidłowo cytowana z `DG-14`. Testy: **112**, `OK (skipped=1)`; Chromium i pozostałe kroki workflow zaliczone. Import DG: nadal `20/36`; brakujące dokładnie `DG-21`–`DG-36`. Raport przed i po zmianach zachowuje dane pochodzenia.
