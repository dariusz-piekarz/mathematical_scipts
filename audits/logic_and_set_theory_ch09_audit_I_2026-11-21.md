# Logika matematyczna i teoria mnogości — rozdział 09, audyt I

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** istniejący rozdział `09-formal-languages-terms-and-formulas.tex` z Biblioteki matematycznej (530 wierszy, 24 599 znaków).  
**Zasada:** sprawdzenie aktualnego materiału, bez dodawania nowych twierdzeń, lematów ani przykładów.

## Zakres i wynik

Sprawdzono **2 twierdzenia, 5 lematów, 1 stwierdzenie, 8 dowodów, 7 definicji, 13 przykładów, 3 uwagi i 1 rysunek**. Kontrola obejmuje kompletność założeń i kwantyfikatorów, rozróżnienie składni i semantyki, gramatykę termów i formuł, unikatowość parsowania, free monoid, zmienne wolne, indukcję strukturalną, podstawianie i przechwytywanie zmiennych.

Nie stwierdzono fałszywego twierdzenia wymagającego zmiany tezy lub nowego dowodu. Wprowadzono następujące korekty **istniejących** sformułowań:

1. Jawnie odróżniono formułę zapisaną według ścisłej gramatyki od jej zapisu z nadmiarowymi nawiasami grupującymi. Przykłady typu `∀v₀ (v₀=v₀)` posługują się konwencją czytelnego zapisu, a nie dodatkową regułą konstrukcji; jednoznaczne parsowanie dotyczy zapisu ścisłego.
2. Uzupełniono jawne wskazanie alfabetu `Σ` w stwierdzeniu o łączności konkatenacji.
3. W lemacie o jednoznaczności odczytywania termów i lemacie o budowie formuły jawnie wskazano ustaloną sygnaturę `L`.
4. W lemacie o zbiorze zmiennych termu po podstawieniu i lemacie o wolnych zmiennych formuły po podstawieniu doprecyzowano dziedzinę termów, formuł i zmiennej oraz warunek dopuszczalności.

Nie zmieniano liczby wyników ani żadnego dotychczasowego `\\label`; zachowano **19 etykiet** i 5 odsyłaczy rozdziału.

## Matematyczne przypadki graniczne

- **Pusty alfabet**: jedynym słowem jest `ε`; przedłużenie pustej funkcji `Σ→M` do homomorfizmu monoidów jest jednoznaczne.
- **Zagnieżdżone termy**: poprawne rozdzielenie argumentów na poziomie zewnętrznych nawiasów niezależnie od przecinków wewnętrznych.
- **Kwantyfikator zasłaniający**: `(Qx φ)[x:=t]=Qx φ` nawet przy `x∈FV(φ)`, bo wystąpienia stają się związane.
- **Przechwycenie zmiennych**: `∀y(x=y)` i podstawienie `x:=y` nie są dopuszczalne; poprawne przemianowanie związanej zmiennej usuwa przeszkodę.
- **Formuły bez wolnego `x`**: podstawienie za `x` pozostaje bez zmian bez względu na wolne zmienne termu.
- **Wolny monoid**: konstrukcja funkcji z liter przez konkatenację i homomorfizm do monoidu, również nieprzemiennego, nie wymaga aksjomatu wyboru.
- **Indukcja strukturalna**: minimalność zbiorów generowanych przez gramatykę wyklucza brakujące podstawowe przypadki.

## Testy niezależne i integralność

W niezależnej, ograniczonej enumeracji sprawdzono **1838 skonstruowanych formuł** i **44 112** kombinacji formuła–zmienna–term; **37 612** podstawień dopuszczalnych i **6500** niedopuszczalnych. W dopuszczalnych przypadkach sprawdzono wzór na zbiór zmiennych wolnych, a także brak zmian przy nieobecności wolnego wystąpienia oraz zasłanianie przez kwantyfikator. Nie uzyskano kontrprzykładu. Nowy test regresyjny znajduje się w `tools/tests/test_logic_and_set_theory_ch09.py`.

Zweryfikowano istniejący diagram składniowy na stronie PDF 90 książki iteracji 79: brak widocznej kolizji etykiet i obcięć. Nadal należy potwierdzić układ po imporcie, poprzez aktualną kompilację CI.

Po imporcie rozdziałów 01–09 oczekiwana struktura: **269 unikatowych etykiet, 96 odsyłaczy** oraz tylko dwa oczekiwane odsyłacze do późniejszych rozdziałów: `ch:semantics-fol`, `ch:zf-axioms`. Te liczby podlegają weryfikacji dedykowanemu workflow. Żaden test skończonych formuł nie zastępuje ogólnego dowodu matematycznego.

## Status

**Audyt I zakończony z poprawkami formalnymi.** Rozdział 09 należy poddać audytowi II, ponieważ zmieniono jego źródło. Nie przechodzić do rozdziału 10 przed niezależną czystą iteracją oraz zielonym CI.
