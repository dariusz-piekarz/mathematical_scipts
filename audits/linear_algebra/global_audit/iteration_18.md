# Algebra liniowa — audyt globalny, iteracja 18: indywidualna kontrola LA03–05

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Poprzednio:** [iteracja 17](iteration_17.md).
**Wynik:** **CZYSTY W ZBADANYM ZAKRESIE**, bez matematycznych zmian w zamrożonych źródłach. Indywidualnie przeczytano każde z **42 środowisk dowodowych** w LA03, LA04 i LA05, razem z pełną tezą. **Nie twierdzimy, że ukończono globalną formalizację 382 dowodów.**

## 1. Kontrolowany materiał i identyfikowalność

| Rozdział | Blob SHA źródła | Wiersze | Dowody odczytane | Etykiety | Odsyłacze | Rysunki TikZ |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LA03 — odwzorowania liniowe, jądro i obraz | `7ee828f8438e6030cb7f47685433aa3639220ab7` | 1019 | **17/17** | 42 | 19 | 1 |
| LA04 — macierze i zmiana bazy | `6bc9a3c2de2d09c5f67e9ba032fac387b3bcb36e` | 1221 | **15/15** | 49 | 24 | 1 |
| LA05 — eliminacja Gaussa | `c238cb3232b69fb19d0dfe1062af05a2a0d8ddb8` | 752 | **10/10** | 27 | 16 | 0 |
| **Łącznie** | | **2992** | **42/42** | **118** | **59** | **2** |

[Rejestr 42 indywidualnych kontroli](iteration_18_proof_review_03_05.csv) zawiera etykietę twierdzenia, typ i nazwę, zakres wierszy, SHA źródła, a także oddzielną notatkę o sprawdzonym argumencie. Pola `full_statement_read=TAK`, `full_proof_read=TAK` i `independent_mathematical_review=CZYSTY` odpowiadają rzeczywistemu przeczytaniu całej tezy i dowodu, bez automatycznego utożsamiania tego ze sprawdzeniem w Lean. Kontrola odsyłaczy do wcześniejszych rozdziałów została zestawiona z istniejącym zielonym CI; wszystkie lokalne etykiety są różne. Źródła LA03–05 pozostawiono bez zmian.

## 2. Krokowy audyt argumentów matematycznych

### LA03 — 17 dowodów

- **Liniowość i baza Hamela:** `prop:lin3-kryterium`, `lem:lin3-podstawowe` i `thm:lin3-przedluzenie-z-bazy` poprawnie radzą sobie ze skończonymi nośnikami i pustą bazą. Jednoznaczność odwzorowania na bazie nie wymaga ponownego AC, gdy baza jest już zadana. `cor:lin3-zgodnosc-na-generatorach` i `prop:lin3-generatory-przeciwobrazy` rozważają również pusty zbiór generatorów.
- **Jądro, obraz, rząd i iloraz:** `thm:lin3-jadro-obraz-podprzestrzenie`, `thm:lin3-iniekcja-surjekcja`, `thm:lin3-rzad-nullity`, `thm:lin3-pierwsze-izo` i `prop:lin3-faktoryzacja-iloraz`. Sprawdzono niezależność `T(D)` przy rozszerzaniu bazy jądra do bazy `C\sqcup D`, oddzielenie wymiaru kardynalnego od skończonego, dobrą określoność faktoryzacji i brak niepotrzebnego AC w pierwszym twierdzeniu o izomorfizmie.
- **Izomorfizmy, Hom i projekcje:** `prop:lin3-skladanie`, `thm:lin3-odwrotnosc`, `prop:lin3-izomorfizm-baza`, `cor:lin3-rownymiary`, `thm:lin3-hom-przestrzen`, `prop:lin3-end-algebra` i `thm:lin3-projekcja-suma`. Osobno sprawdzono przypadki wymiaru zero, bazę elementarną `E_{ji}` przestrzeni Hom i równość `V=im P\oplus ker P` dla projekcji idempotentnej.

### LA04 — 15 dowodów

- **Macierze dowolnego skończonego rozmiaru:** `prop:lin4-przestrzen-macierzy`, `prop:lin4-kolumny`, `thm:lin4-wspolrzedne-macierz`, `thm:lin4-hom-mat`, `thm:lin4-macierz-zlozenia` i `thm:lin4-rachunek-macierzy`. Sprawdzono zerowe wymiary `m=0` i `n=0`, zgodność rozmiarów iloczynów, współrzędne bazowe, łączność i kolejność macierzy złożenia.
- **Jądra, rząd i odwracalność:** `thm:lin4-rzad-kolumn`, `cor:lin4-kryteria-kolumn`, `thm:lin4-odwracalnosc-kryteria`, `prop:lin4-iloczyn-odwrotnych`. Wszystkie pięć kryteriów odwracalności używa tego samego skończenie wymiarowego założenia. Osobny przypadek `0\times0` jest poprawny przy konwencji o pustej macierzy jednostkowej.
- **Zmiana baz i układy:** `thm:lin4-zmiana-wspolrzednych`, `thm:lin4-zmiana-macierzy`, `cor:lin4-podobienstwo`, `prop:lin4-transpozycja-dzialania`, `thm:lin4-zbior-rozwiazan`. Krytyczna konwencja to `[v]_B=P_{B\leftarrow B'}[v]_{B'}`; z niej dokładnie wynika `[T]_{C'\leftarrow B'}=Q^{-1}AP`. Kontrola dwóch kierunków odwrotności `P` i wymiarów `Q^{-1}AP` nie wykazała pomyłek.

### LA05 — 10 dowodów

- **Algorytm Gaussa i pivoty:** `prop:lin5-odwracalne-operacje`, `cor:lin5-rownowazne-uklady`, `thm:lin5-gauss`, `thm:lin5-rzad-pivoty` i `cor:lin5-pivoty-odwracalnosc`. Każdy krok jest odwracalnym mnożeniem z lewej strony, algorytm wybiera najwyżej `min(m,n)` pivotów, a liczba wolnych współrzędnych jądra to `n-r`. Sprawdzono puste rozmiary, pusty ciąg operacji i wolne współrzędne.
- **Układy i bazy:** `thm:lin5-zgodnosc`, `thm:lin5-baza-jadra`, `thm:lin5-baza-obrazu`. Kryterium zgodności używa macierzy rozszerzonej; z kolumn swobodnych otrzymuje się bazę jądra; **bazę obrazu tworzą kolumny pierwotnej macierzy**, nie przekształconej RREF.
- **Niezmienniczość RREF:** `thm:lin5-jednoznacznosc-rref` wyznacza kolumny bazowe jako możliwe pierwsze niezerowe współrzędne wektorów przestrzeni wierszy, a następnie wymusza równość poszczególnych wierszy w obu postaciach zredukowanych. Kontrola argumentu z najmniejszym niezerowym indeksem i przypadkiem zerowej przestrzeni wierszy wypadła poprawnie. `thm:lin5-gauss-jordan-odwrotnosc` stosuje `[A|I]\mapsto[PA|P]` i identyfikuje `P=A^{-1}`.

## 3. Rzeczywiście wykonane regresje

Dodano reprodukowalny [skrypt testowy LA03–LA05](../../../tools/test_linear_algebra_la03_la05_exhaustive.py) — jego ścieżka w repozytorium to `tools/test_linear_algebra_la03_la05_exhaustive.py`. Odpowiada lokalnemu plikowi `/mnt/data/la_global18_finite_checks.py` (SHA256 `335cfb7afb6cac79cd4cea5f8945cf38c229f36dfb973b132c30e9e102de4a84`; lokalne wykonanie zakończone kodem 0).

**592 020 / 592 020 PASS; 30 716 przebadanych macierzy.**

- Wszystkie macierze rozmiarów do `3x4` i `4x3` w wybranych przypadkach nad \(\mathbb F_2\), do `3x3` nad \(\mathbb F_3\), także `2x2` nad \(\mathbb F_5\) oraz przypadki rozmiaru zero. Pełen zestaw 18 kombinacji ciała/rozmiaru wypisuje sam skrypt.
- **30 716** razy dla każdej rodziny: niezależność RREF od wyboru pierwszego/ostatniego dopuszczalnego wiersza pivotu, idempotentność eliminacji, zachowanie przestrzeni wierszy i permutacji, wymiar obrazu i jądra z niezależnego wyliczenia wszystkich wektorów, oryginalne kolumny bazowe oraz rząd transpozycji.
- **88 668** sprawdzeń zgodności macierzy rozszerzonej z rzeczywistą przynależnością `b` do obrazu; **78 149** kontroli liczby rozwiązań oraz tyle samo równości zbioru rozwiązań i warstwy jądra.
- **9132** testy wzoru zmiany baz `Q^{-1}AP` w wymiarze 2 nad \(\mathbb F_2\) i \(\mathbb F_3\); dodatkowo kontrola mocy grup \(\operatorname{GL}_2\) oraz 22 przypadków macierzy idempotentnych wraz z rozkładem obraz–jądro.

Test obejmuje **skończone modele**, więc nie stanowi formalnego dowodu ogólnych twierdzeń ani certyfikacji kodu Lean. Nowy skrypt dołączono do `.github/workflows/linear-algebra-chapter.yml` jako obowiązkowy krok i dodano do filtra wyzwalającego workflow.

## 4. LaTeX, rysunki i wcześniejszy CI

- LA03–05: **118** etykiet, **59** odsyłaczy i poprawnie sparowane `\\begin{proof}` / `\\end{proof}` (**42 pary**). Brak powtórzonych etykiet w tych rozdziałach i niepożądanych sformułowań wykrytych w kontroli polskiej terminologii. Nie zmieniano żadnego historycznego identyfikatora `\\label`.
- Przejrzano źródła obu rysunków TikZ: diagram pierwszego twierdzenia o izomorfizmie w LA03 oraz przemienny diagram współrzędnych w LA04. Strzałki i etykiety odpowiadają deklarowanym odwzorowaniom. **W tej iteracji nie wykonano nowej wizualnej inspekcji wyrenderowanego PDF**.
- Wynik **[CI 45061769006](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45061769006)** na commicie `1c7506dc92285d05b2577ec22d32953af84484e7` to `completed/success`, co potwierdza zakończenie CI z iteracji 17, w tym test LA01–02 i budowę książki. Nie jest to weryfikacja nowego testu LA03–05. Dla nowego przebiegu należy oddzielnie sprawdzić krok CI i finalny status.
- Źródła LA03–05 pozostawiono bez zmian. Stabilizacji LA12–32 nie resetowano i nie dodawano materiału opcjonalnego.

## 5. Decyzja i dalszy plan

**Iteracja 18: zakończona, czysta dla wszystkich 42 indywidualnie zbadanych dowodów LA03–05.** Razem z iteracją 17 mamy w nowych per-dowodowych rejestrach **82/382** oznaczonych jako przeczytane i skontrolowane matematycznie. Nie oznacza to, że pozostałe 300 nie były wcześniej audytowane rozdziałowo: mowa o nowym, indywidualnym rejestrze.

**Następny blok:** LA12–13, indywidualne 28 dowodów, ze szczególnym naciskiem na polaryzację w ciele zespolonym, półtoraliniowość, konwencję sprzęgania, twierdzenie Riesza i ortogonalność w przypadku zespolonym. Równolegle kontynuować przeglądy pozostałych rozdziałów w rejestrze, aż cały audyt 382 dowodów będzie domknięty. Dopiero potem **dodatkowy niezależny audyt sceptyczny**.