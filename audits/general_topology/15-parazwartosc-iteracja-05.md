# Topologia ogólna — rozdział 15: reaudyt 05 (Nagata–Smirnow)

Data: 2026-11-22; gałąź `biblioteka-matematyczna-iteracja-6`.

## Zmiany zakresu

Ponownie otwarto wcześniej stabilny rozdział 15 i dopisano pełne twierdzenie Nagaty–Smirnowa o metryzowalności przestrzeni regularnych T₁ z bazą będącą przeliczalną sumą rodzin lokalnie skończonych. Dodano definicję tej bazy, oba kierunki dowodu i porównanie z twierdzeniem Urysohna z rozdziału 10. Zachowano wszystkie wcześniejsze dowody, w tym twierdzenie Stone'a. Źródło: `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`. Główna etykieta: `thm:topog-parazwartosc-nagata-smirnow`.

## Reaudyt matematyczny

1. **Konieczność.** Dla metryki `d` pokrycia kulami promienia `2^{-n}` mają otwarte lokalnie skończone uszczegółowienia `V_n` na mocy udowodnionego wcześniej twierdzenia Stone'a. Ich przeliczalna suma stanowi bazę: dla `x∈O` i kuli `B(x,ε)⊂O`, wybieramy `n` z `2·2^{-n}<ε`. Jeśli `x∈V⊂B(y,2^{-n})`, to dla `z∈V` zachodzi `d(x,z)<2·2^{-n}<ε`. Podano wszystkie kwantyfikatory.
2. **Normalność w wystarczalności.** Dla rozłącznych domkniętych `A,C` oraz każdej lokalnie skończonej warstwy bazy bierzemy sumy `P_n` i `Q_n` elementów, których domknięcia omijają odpowiednio `C` i `A`. Domknięcia sum są sumami domknięć, ponieważ warstwy są lokalnie skończone (wynik wykazany na początku rozdziału 15). Z regularności i bazy wynika, że `P_n` pokrywają `A` oraz `Q_n` pokrywają `C`. Otwarte zbiory `P=⋃_n(P_n\setminus⋃_{j≤n}cl Q_j)` i `Q=⋃_n(Q_n\setminus⋃_{j≤n}cl P_j)` zawierają `A,C`, a ich rozłączność wynika przez porównanie indeksów.
3. **Każdy zbiór otwarty jest zbiorem dodatniości funkcji.** Dla `G` otwartego konstrukcja `F_n(G)` jako sumy domknięć odpowiednich elementów `B_n` daje `F_n(G)` domknięty i zawarty w `G`; regularność zapewnia `G=⋃_n F_n(G)`. Normalność i lemat Urysohna dostarczają `g_n=1` na `F_n(G)`, `g_n=0` poza `G`; ciągły szereg `∑2^{-n}g_n` jest dodatni dokładnie na `G`.
4. **Zanurzenie do przestrzeni metrycznej.** Dla każdego `(n,B)` wybrano funkcję `f_{n,B}` dodatnią dokładnie na `B` i ograniczoną przez `2^{-n}`. Obraz `F(X)` leży w `ℓ∞(J)`, także gdy `J` jest nieprzeliczalny. Ciągłość względem normy supremum wynika z kontroli wszystkich późnych poziomów jedną wagą oraz skończenie wielu współrzędnych wcześniejszych poziomów w małym otoczeniu (lokalna skończoność `B_n`). Rozdzielanie punktów zapewnia `T₁` i własność bazy; ciągłość odwrotności wynika z dodatniości wybranej współrzędnej `f_{n,B}` na `B⊂G`.
5. **Przestrzeń pusta.** Rozważono osobno; w pozostałym dowodzie zbiór indeksów bazy jest niepusty. Wniosek `d(x,y)=sup_{(n,B)∈J}|f_{n,B}(x)-f_{n,B}(y)|` jest rzeczywistą metryką zgodną z topologią.
6. **Porównanie z Urysohnem.** Baza przeliczalna jest przeliczalną sumą rodzin jednoelementowych, lecz baza singletonów w nieprzeliczalnej przestrzeni dyskretnej jest lokalnie skończona i nie jest przeliczalna. Nie należy mylić tych pojęć.

## Weryfikacja testowa

Rozszerzono `tools/tests/test_general_topology_ch15.py` o kontrolę nowych etykiet i krytycznych elementów dowodu (normalność, `F_n(G)`, wagi `2^{-n}`, `ℓ∞(J)`, norma supremum). Wcześniejsze testy konstrukcji Stone'a i tożsamości teleskopowej zachowano. W toku audytu poprawiono zapisy ukośników w asercjach testowych (źródło zawiera pojedyncze ukośniki LaTeX). Testy nie są formalnym dowodem twierdzenia; niezależna kontrola dowodu jest wymagana.

## Stan techniczny

Końcowy workflow GitHub Actions dla komitu testów i źródła: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011132217 — **completed/success**, bez nieudanych kroków. Artefakt `14749962442` dostarczył samodzielny PDF rozdziału 15 (6 stron A4) i logi. Sprawdzono w logu brak `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence` i `Fatal error`. Wyrenderowano i obejrzano strony 4–6, ze szczególną kontrolą dowodu Nagaty–Smirnowa na stronach 5–6 — brak ucięć lub kolizji. Wcześniejsze testy Stone'a i podziałów jedności pozostają zielone.

| Kryterium | Status |
| --- | --- |
| Dwie implikacje twierdzenia Nagaty–Smirnowa | PASS — kontrola dowodu |
| Normalność, funkcje dodatnie, zanurzenie do ℓ∞ | PASS — kontrola dowodu |
| Zależności od Stone'a/Urysohna | PASS |
| Reorganizacja i testy | Wdrożone |
| Kompilacja CI / wizualizacja PDF | **PASS — run 45011132217, PDF 6 stron** |
| Rozdział 15 | **OTWARTY — audyt 05 zakończony; nowy dowód wymaga niezależnego audytu 06** |
