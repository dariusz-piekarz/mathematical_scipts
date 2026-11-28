# Topologia ogólna — rozdział 16, audyt iteracja 03

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Źródło: `chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex`, SHA `1c2fcb925d62120feaea468400e48842a508a062`.

## Zakres trzeciej, niezależnej kontroli

Ponownie sprawdzono całą aktualną treść, w tym fragmenty zmienione w audycie 02. Nie dodawano nowych twierdzeń ani przykładów, zgodnie z procedurą stabilizacji.

1. **Topologia początkowa.** Zbiory przeciwobrazów otwartych zbiorów tworzą podbazę najmniejszej topologii. Kryterium ciągłości odwzorowania do przestrzeni z topologią początkową jest poprawne również dla pustego zbioru indeksów: topologia początkowa jest wówczas antydyskretna.
2. **Funkcjonalna charakterystyka całkowitej regularności.** Założenie T₁ pozwala oddzielić różne punkty; całkowita regularność daje funkcje oddzielające punkt od zbioru domkniętego. Konstrukcja `1-h` i przeciwobraz `(1/2,1]` są poprawne. W odwrotną stronę skończone przecięcie zbiorów podbazowych `W` zawiera `x` i jest zawarte w `X\setminus F`; dla każdej współrzędnej istnieje ciągła funkcja na odcinku przyjmująca `0` w wartości współrzędnej `x` oraz `1` poza odpowiednim otwartym zbiorem. Maksimum tych funkcji po złożeniu oddziela `x` od `F`. Przypadek `F=∅` został poprawnie rozpatrzony oddzielnie.
3. **Przykład oddzielania punktów.** Funkcja arctan na dyskretnej `R` jest ciągła i różnowartościowa. Indukowana przez nią topologia początkowa odpowiada zwykłej topologii euklidesowej; nie wystarcza samo rozdzielanie punktów przez wybraną rodzinę funkcji.
4. **Istnienie uzwarcenia Hausdorffa.** Konieczność: podprzestrzeń zwartej przestrzeni Hausdorffa jest Tychonoffa. Wystarczalność: wcześniejsze twierdzenie z rozdziału 07 o zanurzeniu w kostkę i domknięciu obrazu. Nie ma odwołań do przyszłego rozdziału 17 w dowodzie.
5. **Jednoznaczność oraz porządek uzwarceń.** Zgodne ciągłe odwzorowanie `K₁→K₂` jest jednoznaczne (gęstość `e₁(X)`, domkniętość przekątnej `K₂`) i surjektywne (zwarty obraz jest domknięty i zawiera gęsty `e₂(X)`). Zwrotność, przechodniość i antysymetria porządku na klasach równoważności wynikają odpowiednio z identyczności, składania i jednoznaczności odwzorowań zgodnych z zanurzeniami. Poprawnie uzasadniono niezależność od reprezentantów.
6. **Dwa uzwarcenia przedziału.** `[0,1]` oraz `S¹` z `e₂(t)=exp(2πit)` są uzwarceniami `(0,1)`. Nie są równoważne, gdyż zgodny homeomorfizm musiałby posłać zarówno `0`, jak i `1` w `1∈S¹`. Jednak funkcja `p(t)=exp(2πit)` jest zgodnym, ciągłym odwzorowaniem surjektywnym, więc określa właściwy kierunek porządku.
7. **Uzwarcenie dyskretnej przestrzeni N i przedłużalność.** `K={0}∪{1/n:n≥1}` jest zwarte, zaś `n↦1/n` jest zanurzeniem z gęstym obrazem. Funkcja `f:N→[0,1]` ma przedłużenie ciągłe do `K` wtedy i tylko wtedy, gdy `f(n)` jest zbieżny. W kierunku wystarczającym z `f(n)→a` i `0<δ<1/N` wynika, że w otoczeniu `[0,δ)∩K` wszystkie punkty różne od `0` odpowiadają `n>N`, zapewniając żądane oszacowanie. To otoczenie jest otwarte we względnej topologii `K`. Przykład funkcji naprzemiennej jest poprawny.
8. **Redakcja i odsyłacze.** Końcowa uwaga poprawnie wskazuje osobno przykład nierównoważnych uzwarceń oraz przykład nieprzedłużalnej funkcji. Nie wykryto nowych luk, błędnych definicji, problemów terminologicznych ani brakujących założeń.

## Sprawdzenie techniczne

Ostatni przebieg GitHub Actions dla treści zmienionej w audycie 02:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45012771143 — `completed/success`. Artefakt `14749659432`: samodzielny PDF rozdziału 16 (4 strony A4) i log. Sprawdzono wszystkie cztery strony w audycie 02 — czytelne wzory, brak kolizji i ucięć. Log bez `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence` i `Fatal error`. W audycie 03 treść TeX **nie uległa zmianie**, więc można wykorzystać ten sam przebieg do weryfikacji technicznej.

## Werdykt

| Kontrola | Wynik |
| --- | --- |
| Matematyka, definicje i dowody | PASS |
| Charakterystyka całkowitej regularności | PASS |
| Istnienie i porządek uzwarceń | PASS |
| Przykłady i przypadki brzegowe | PASS |
| Terminologia i odsyłacze | PASS |
| Testy, pełna książka i samodzielny PDF | PASS |
| Zmiany wymagane w iteracji 03 | **BRAK** |
| Stabilizacja | **STABILNY — audyt 03 zamknięty** |

Następny rozdział 17: szczegółowe uzwarcenia Aleksandrowa i Čecha–Stone’a, z własnościami uniwersalnymi. Nie należy traktować wyniku audytu 03 jako audytu nowych rozdziałów.
