# Topologia ogólna — rozdział 15: audyt 01

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Zakres opracowania

Nowy rozdział: `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`.

Przedstawiono kolejno:
- lokalną skończoność rodzin zbiorów, jej zachowanie przez domknięcia i równość domknięcia lokalnie skończonej sumy z sumą domknięć;
- uszczegółowienia pokryć otwartych i definicję parazwartości (bez niejawnego założenia Hausdorffa);
- definicję nośnika funkcji i podporządkowanego, lokalnie skończonego podziału jedności; dowód, że takie podziały dla dowolnych pokryć implikują parazwartość;
- konstrukcję funkcji odcinających przez lemat Urysohna;
- pełną konstrukcję przeliczalnego, lokalnie skończonego podziału jedności dla regularnej przestrzeni Hausdorffa spełniającej własność Lindelöfa;
- zastosowanie do metryzowalnych przestrzeni spełniających drugi aksjomat przeliczalności oraz lokalnie zwartych, `σ`-zwartych przestrzeni Hausdorffa;
- dwa przykłady: jawne funkcje trójkątne na `R` i dowolna nieprzeliczalna przestrzeń dyskretna.

## Kontrola matematyczna

1. Lokalna skończoność domknięć: otwarte otoczenie nieprzecinające `A_i` nie przecina też `cl(A_i)`. Aby wykazać domkniętość sumy, usuwamy skończenie wiele domknięć ze wskazanego otoczenia.
2. Dla funkcji odcinającej ważne jest potrójne zagnieżdżenie `F⊂W⊂cl(W)⊂V` oraz zastosowanie lematu Urysohna do `F` i `X\setminus W`. W pierwszej wersji źródła skrótowo pomylono rolę `V_n` i `U_n` w wywołaniu lematu; poprawiono ją od razu w commicie `d5a2d250734559cd581a222bf2c0a09e64c1a6b8`.
3. W głównym twierdzeniu `F_n=cl(W_n)⊂V_n⊂cl(V_n)⊂U_n`, skąd powstaje `f_n=1` na `W_n` z nośnikiem w `U_n`. Konstrukcja `φ_n=f_n∏_{j<n}(1-f_j)` jest ciągła i nieujemna.
4. Jeśli `x∈W_N`, to na całym otwartym `W_N` zachodzi `f_N=1`, a więc nośniki `φ_n` dla `n>N` są rozłączne z `W_N`. To dowodzi **lokalnej**, a nie tylko punktowej skończoności.
5. Tożsamość `Σ_{n≤m}φ_n=1-∏_{n≤m}(1-f_n)` i pokrycie przez `W_N` zapewniają sumę równą `1` w każdym punkcie. Test numeryczny sprawdza 3125 pięcioskładnikowych konfiguracji `f_n`.
6. Zastosowania korzystają wyłącznie z twierdzeń poprzednich rozdziałów: metryzowalność daje regularność, drugi aksjomat przeliczalności daje Lindelöfa, zaś lokalna zwartość Hausdorffa daje regularność i `σ`-zwartość implikuje Lindelöfa.
7. Nie przedstawiono ogólnego twierdzenia Stone'a o parazwartości wszystkich przestrzeni metrycznych jako udowodnionego: zostało odnotowane jawnie jako wynik wykraczający poza przeprowadzoną konstrukcję. Nie jest używane w żadnym dowodzie.

## Integracja i regresja

Utworzono `books/pl/general_topology_ch15.tex`, dodano `\input` do książki, wpis w `catalog/books.json` i test `tools/tests/test_general_topology_ch15.py`. Workflow waliduje katalog, uruchamia testy i kompiluje rozdział 15.

Pierwszy przebieg CI zgłosił **regresję testu rozdziału 14**: sztywne `len(chapters)==14`, niepoprawne po dodaniu rozdziału 15. Zmieniono warunek na `len(chapters)>=14`, zachowując sprawdzenie pozycji i etykiet rozdziału 14 (commit `0ee69169f2c2a56205cbb2d06b35190aa52f0b41`).

## Weryfikacja

GitHub Actions dla poprawionej integracji:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45009390372

W chwili rozpoczęcia raportu workflow przechodzi przez etap kompilacji całej książki; wynik końcowy, PDF i log wymagają jeszcze odczytu.

| Warstwa | Status |
| --- | --- |
| Definicje i precyzja kwantyfikatorów | Audyt 01: PASS |
| Dowód lokalnej skończoności i konstrukcja podziału | Audyt 01: PASS po doprecyzowaniu |
| Przykłady i testy tożsamości | Testy zintegrowane |
| Zależności i rozdziały 11–14 | Regresja naprawiona; CI w toku |
| Kompilacja i oględziny PDF | Weryfikacja w toku |
| Stabilność rozdziału | **W AUDYCIE — nie oznaczać jako stabilny** |

Następna iteracja powinna ponownie sprawdzić normalność, wybór pokrycia `W_n`, nośniki oraz rozważyć pełny dowód ogólnego twierdzenia Stone'a.
