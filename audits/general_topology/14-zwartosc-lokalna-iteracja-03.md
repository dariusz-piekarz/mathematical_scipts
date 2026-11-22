# Topologia ogólna — rozdział 14: audyt iteracja 03

Data: 2026-11-22. Źródło: `chapters/pl/general_topology/14-zwartosc-lokalna.tex`; SHA bloba `24ca61f0e19fe6674719fc76e53073aa82cc755c`.

## Cel i wynik niezależnej kontroli

Przeprowadzono **trzeci niezależny audyt** całej aktualnej treści po poprawieniu kontrprzykładu z `Q` w iteracji 02. W tej iteracji **nie stwierdzono nowych błędów matematycznych ani potrzeby korekty źródła**. Przeanalizowano ponownie:

1. Definicję lokalnej zwartości i lemat o otoczeniu ze zwartym domknięciem. Wykorzystane fakty: zwarta podprzestrzeń Hausdorffa jest normalna (rozdz. 7), możliwość zwężania otoczeń w regularnej podprzestrzeni (rozdz. 5), zwartość i domkniętość `K` w `X`. Każdy krok jest uzasadniony.
2. Wersję lokalnie zwartą twierdzenia Baire'a: dla otwartych gęstych `G_n` tworzy się niepuste zstępujące zwarte domknięcia `K_n`; końcowa część jest poprawnym zastosowaniem własności skończonych przecięć w `K_1`. Nie zachodzi zależność od materiału rozdziału 15 lub późniejszych.
3. Otwarta i domknięta podprzestrzeń: odpowiednio zwarty zbiór leżący wewnątrz `U` oraz `K∩F` zwarty z niepustym względnym wnętrzem przy danym punkcie.
4. Skończone oraz dowolne iloczyny: w konieczności niepuste czynniki zapewniają możliwość wyboru punktu produktu; podstawowy cylinder `B⊂K` ma poza skończonym zbiorem indeksów pełne rzutowania, a ciągłe obrazy `K` są zwarte. Dla poszczególnych współrzędnych rzutowanie `B` zawiera otwarte otoczenie, więc czynniki są lokalnie zwarte. Wystarczalność wynika z twierdzenia Tychonoffa i skończonych iloczynów. Przypadek pustego zbioru indeksów uwzględnia jednopunktowy iloczyn.
5. Twierdzenie o wyczerpaniu: `σ`-zwartość pozwala rekurencyjnie objąć `K_n∪C_(n+1)` wnętrzem nowego zwartego `K_(n+1)`. Odwrotnie, rosnące otwarte pokrycie każdego zwartego `C` ma skończone podpokrycie, z którego wynika zawieranie `C` w jednym `K_N`. Implikacja przeliczalności w nieskończoności do `σ`-zwartości korzysta ze zwartości singletonów.
6. Drugi aksjomat przeliczalności: z własności Lindelöfa i otwartego pokrycia otoczeniami o zwartych domknięciach powstaje przeliczalne pokrycie zwartymi podzbiorami.
7. Kontrprzykład z `Q`: zastąpienie `(K_n)` przez `L_n=∪_{j≤n}K_j` zachowuje zwartość i współkońcowość. Każdy `L_n` ma puste wnętrze w `Q`; `q_n∈(q-1/n,q+1/n)∩Q\setminus L_n` jest wykonalny. Zwarty zbiór `C={q}∪{q_n}` nie mieści się w żadnym `L_n`, a tym samym w żadnym `K_n`: argument jest poprawny. Sprawdzono osobno, że zwarty `K⊂Q` musi mieć puste wnętrze.
8. Kontrprzykład nieprzeliczalnej przestrzeni dyskretnej oraz wyczerpanie `R` przedziałami: obliczenia i hipotezy poprawne.

## Struktura i walidacja

- Rozdział 11 nie definiuje ani nie używa lokalnej zwartości; wszystkie cztery przeniesione etykiety są obecne w rozdziale 14. Sprawdzono test regresyjny `tools/tests/test_general_topology_ch14.py`.
- Odsyłacze lokalne i odsyłacze w katalogu nie wymagają zmian. Terminologia `przeliczalność w nieskończoności`, `uzwarcenie`, `spełnia drugi aksjomat przeliczalności` jest zgodna z regułami projektu.
- CI dla dokładnie tej samej treści źródła po poprawce z iteracji 02: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008598489 — `completed/success`. Odpowiedni artefakt `14748314830` zawiera czterostronicowy samodzielny PDF; wszystkie strony i log zostały skontrolowane podczas audytu 02, bez ostrzeżeń i usterek graficznych.
- Potwierdzono dodatkowo zielony przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45008638942 dla niezmienionego źródła.

## Tabela statusów

| Kontrola | Wynik |
| --- | --- |
| Matematyka i wszystkie dowody | PASS |
| Naprawiony dowód dla `Q` | PASS |
| Kryterium dowolnych iloczynów | PASS |
| Wyczerpania zwarte i przeliczalność w nieskończoności | PASS |
| Przykłady, założenia i odsyłacze | PASS |
| CI oraz czterostronicowy PDF dla aktualnego źródła | PASS |
| Nowe poprawki wymagane w iteracji 03 | **BRAK** |
| Decyzja | **ROZDZIAŁ 14 STABILNY — audyt zamknięty** |

Rozdział 14 może stanowić podstawę opracowania rozdziału 15; kolejność zależności jest zachowana.
