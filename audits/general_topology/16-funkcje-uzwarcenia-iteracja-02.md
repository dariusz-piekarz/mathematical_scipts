# Topologia ogólna — rozdział 16, audyt 02

Data: 2026-11-22. Źródło: `chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex`.

## Audyt matematyczny

1. **Topologia początkowa**: przeciwobrazy otwartych zbiorów tworzą podbazę najmniejszej topologii, a kryterium ciągłości wynika z przeciwobrazów tej podbazy. Przypadek pustej rodziny indeksów jest spójny.
2. **Charakterystyka całkowitej regularności**: przeanalizowano każdy kierunek implikacji, w tym aksjomat T₁ użyty do rozdzielania punktów, funkcję `1-h`, skończone przecięcie zbiorów podbazowych i maksimum funkcji odcinających. Przypadek `F=∅` jest poprawny.
3. **Przykład z funkcją arctan** na `R` dyskretnej: oddzielanie punktów przez jedną funkcję nie wymusza odtworzenia topologii dyskretnej; topologia początkowa jest euklidesowa.
4. **Istnienie uzwarcenia Hausdorffa**: konieczność opiera się na całkowitej regularności zwartych przestrzeni Hausdorffa i dziedziczeniu własności; wystarczalność na konstrukcji kostkowej, udowodnionej w rozdziale 7.
5. **Jednoznaczność zgodnego odwzorowania**: ciągłe odwzorowania do przestrzeni Hausdorffa zgodne na gęstym zbiorze są równe dzięki domkniętości przekątnej.
6. **Porządek uzwarceń**: ciągły zgodny czynnik `p:K₁→K₂` ma zwarty, więc domknięty obraz zawierający gęsty `e₂(X)`; stąd jest surjektywny. Dwa zgodne czynniki w przeciwnych kierunkach składają się do identyczności na gęstych zbiorach, więc uzwarcenia są równoważne. Porządek jest dobrze określony na klasach.
7. **Przedział i okrąg**: obie konstrukcje są uzwarceniami `(0,1)`; ciągłość wyklucza zgodny homeomorfizm, bo musiałby skleić końce. Istnieje jednak zgodne odwzorowanie `[0,1]→S¹`.
8. **Uzwarcenie dyskretnej N**: `K={0}∪{1/n}` jest zwarte, obraz `e(N)` gęsty; ograniczona funkcja `f:N→[0,1]` ma ciągłe przedłużenie do `K` wtedy i tylko wtedy, gdy `f(n)` jest zbieżny. Doprecyzowano konstrukcję otoczenia `[0,δ)∩K` przy `0<δ<1/N`, żeby z wybranej granicy wynikała ciągłość w `0`.
9. **Redakcja**: poprawiono końcowe odesłanie „przykład powyżej”, ponieważ przykład przedziału i okręgu dowodzi niejednoznaczności uzwarcenia, a przykład N — ograniczeń przedłużania funkcji. Zmiana źródła w commicie `e9763ba46f76d2fe6232684128dbf844a5fe0e58`.

## Kontrola techniczna

Poprzednia wersja źródła przeszła GitHub Actions `45012354172` (`success`), pełną kompilację i czterostronicowy PDF bez usterek. Po aktualnej korekcie należy sprawdzić nowy przebieg CI i skład PDF; nie należy przenosić poprzedniego sukcesu bez weryfikacji.

| Warstwa | Status |
| --- | --- |
| Poprawność matematyczna i zależności | PASS |
| Przykłady i przypadki brzegowe | PASS po doprecyzowaniu |
| Język i jednoznaczność referencji | Poprawiono |
| Nowy CI, PDF i log LaTeX | Weryfikacja |
| Status | W AUDYCIE — do końcowej walidacji |

Zgodnie z procedurą kolejne audyty mają weryfikować obecny materiał, bez nieuzasadnionego dopisywania nowych twierdzeń.
