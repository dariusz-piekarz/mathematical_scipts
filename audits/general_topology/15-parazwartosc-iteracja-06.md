# Topologia ogólna — rozdział 15: reaudyt 06 (niezależna kontrola Nagaty–Smirnowa)

Data: 2026-11-22. Audyt bez zmian w źródle po iteracji 05.
Plik: `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex` (SHA `82e0fb5be75489017c8ea1844c698c87ce580901`).

## Weryfikacja wszystkich założeń i dowodu

1. **Pusta przestrzeń.** Wyłączona jawnie. Metryzowalność jest trywialna; pusta rodzina stanowi bazę i przeliczalną sumę lokalnie skończonych rodzin.
2. **Konieczność.** Twierdzenie Stone'a zastosowane do pokryć kulami `B_d(x,2^{-n})`. Dla `x∈O` wybór `n` z `2^{1-n}<ε` i `x∈V⊂B_d(y,2^{-n})` implikuje `V⊂B_d(x,ε)⊂O`. Rodziny uszczegółowienia nie muszą być przeliczalne.
3. **Normalność w wystarczalności.** Rodziny `P_n` (otwarte zbiory bazy z domknięciem rozłącznym z `C`) i `Q_n` analogiczne dla `A` są pokryciami odpowiednich zbiorów domkniętych dzięki regularności. Lokalna skończoność pozwala przejść od domknięcia sumy do sumy domknięć, co uzasadnia `cl P_n∩C=∅` i `cl Q_n∩A=∅`. Dla `x∈P∩Q` wybór indeksów `n,m` prowadzi do sprzeczności bez względu na relację porządku `m≤n` lub `n≤m`. Skończone odejmowane sumy są domknięte, więc uzyskane rozdzielające otoczenia są otwarte.
4. **Funkcje dodatnie dokładnie na danym otwartym `G`.** Rodzina elementów `B∈B_n` z `cl B⊂G` pozostaje lokalnie skończona, więc `F_n(G)=⋃cl B` jest domknięty. Regularność i własność bazy gwarantują `G=⋃F_n(G)`. Normalność i lemat Urysohna dają `g_n=1` na `F_n(G)`, `g_n=0` na `X\setminus G`. Szereg wag `2^{-n}` zbiega jednostajnie, a jego suma jest dodatnia w każdym punkcie `G` i zerowa poza `G`.
5. **Metryzowalność przez `ℓ∞(J)`.** Wszystkie współrzędne `f_{n,B}=2^{-n}g_B` są ograniczone. Dla zadanego `ε` późne poziomy `n≥N` mają wahanie nie większe od `2^{-N}<ε/2`. Dla skończenie wielu wcześniejszych poziomów lokalna skończoność `B_n` ogranicza liczbę aktywnych współrzędnych na otoczeniu punktu, po czym można jednocześnie zapewnić małe różnice wszystkich pozostałych. Otrzymano ciągłość w **normie supremum**, nie tylko w topologii produktu.
6. **Iniektywność i odwrotność.** Aksjomat T₁ oraz baza zapewniają dla `x≠y` zbiór bazowy `B` zawierający `x`, nie `y`, więc różni się jedna współrzędna. Dla `x∈G` wybrana współrzędna dodatnia dokładnie na `B⊂G` zapewnia, że odpowiednia kula w `ℓ∞(J)` o promieniu `f_{n,B}(x)/2` ma przeciwobraz zawarty w `G`. Zatem `F` jest zanurzeniem topologicznym, a pullback normy definiuje zgodną metrykę.
7. **Porównanie z Urysohnem.** Nieprzeliczalna przestrzeń dyskretna jest poprawnym przykładem bazy lokalnie skończonej bez drugiego aksjomatu przeliczalności; sama baza jest rodziną singletonów. To nie przeczy kryterium Urysohna, lecz wskazuje jego silniejsze założenie.
8. **Regresja starych wyników.** Twierdzenie Stone'a, podziały jedności dla regularnych przestrzeni Lindelöfa, nośniki funkcji i przykład na prostej pozostają w niezmienionej, wcześniej zweryfikowanej postaci.

## Testy, odsyłacze i skład

- Workflow https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011132217: `completed/success`, bez błędów testów i logów.
- Artefakt `14749962442` zawiera 6-stronicowy PDF samodzielnego rozdziału 15. Sprawdzono układ tezy, normalności, konstrukcji funkcji dodatnich i metryki na stronach 5–6. Brak przepełnień i ostrzeżeń.
- Rozdział 10 zawiera kryterium Urysohna; rozdział 15 zawiera definicję lokalnej skończoności i pełne twierdzenie Stone'a. Brak odwołania do wyników późniejszych rozdziałów.
- Nie znaleziono duplikatów etykiet ani nowych nieuzasadnionych przejść.

## Werdykt

| Obszar | Wynik |
| --- | --- |
| Dwie implikacje Nagaty–Smirnowa | PASS |
| Normalność i funkcje ciągłe | PASS |
| Ciągłość w normie supremum i metryka | PASS |
| Niezmienione wcześniejsze twierdzenia rozdziału 15 | PASS |
| Testy, pełna książka i PDF | PASS |
| Zmiany wymagane w iteracji 06 | **BRAK** |
| Status | **STABILNY — audyt 06 zamknięty** |

Przeniesienie statusu z „otwarty” na „stabilny” jest uzasadnione czystym niezależnym audytem po istotnym rozszerzeniu rozdziału.
