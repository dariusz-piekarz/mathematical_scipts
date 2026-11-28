# Algebra liniowa — rozdział 01, audyt stabilizacyjny I

**Data:** 22 listopada 2026.  
**Źródło:** `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`; wersja wejściowa blob `2ac33abc4cf87d5085e81ff14c746ce6c11a20c7`.  
**Zakres:** cały rozdział (1716 wierszy przed korektą), bez dodawania nowych twierdzeń.

## Kontrola matematyczna
- Sprawdzono pełny tekst i założenia 24 dowodów: kryterium podprzestrzeni, przecięcia i sumy mnogościowe, rozpinanie i niezależność, wymianę Steinitza, równość długości baz skończonych, dołączanie wektorów, charakteryzację skończonej wymiarowości, wymiar podprzestrzeni, współrzędne, lemat o łańcuchu i dwie konstrukcje przez lemat Zorna.
- Zweryfikowano przypadki skrajne: `K^0`, `V={0}`, puste zbiory indeksów, podprzestrzeń zerową, ciała skończone i charakterystykę dwa, rodziny indeksowane z powtórzeniami i skończony nośnik.
- Przeczytano 21 przykładów oraz kontrprzykłady nad `F_2`. Odsyłacze `\\ref` rozdziału rozwiązują się w jego 69 etykietach; nie stwierdzono duplikatów.
- Porównano sposób rozpisania argumentów z faktycznie odczytanym `chapters/pl/differential_geometry_and_topology/01-rozmaitosci-rozniczkowe.tex` (rozdział wzorcowy DG-01), nie tylko z deklaracją standardu.
- Nie znaleziono błędu w twierdzeniach, w dowodzie lematu Steinitza ani w dwóch argumentach Zorna.

## Korekta nieuzasadnionego kroku
W Przykładzie `prz:lin-ciagi` stwierdzono, że `K^{(N_0)}` jest podprzestrzenią, omawiając tylko dodawanie ciągów. Uzupełniono brakujące sprawdzenie: ciąg zerowy ma pusty nośnik, a dla dowolnych `a,b∈K`, `x,y∈K^{(N_0)}` zachodzi `supp(ax+by)⊂supp(x)∪supp(y)`, więc wynik ma skończony nośnik. Jest to potrzebne jawne uzasadnienie pełnego kryterium podprzestrzeni, nie nowe twierdzenie.

## Niezależne testy
- Dokładna enumeracja podprzestrzeni `F_p^2`, `p=2,3,5`, i weryfikacja `U∪W` jest podprzestrzenią wtedy i tylko wtedy, gdy `U⊆W` lub `W⊆U`: **125 par — PASS**.
- Losowe kombinacje ciągów o skończonym nośniku nad `F_2,F_3,F_5,F_7`: **12 000 przypadków — PASS**.
- Dokładna enumeracja kryteriów niezależności i rozpinania rodzin nad `F_2,F_3` w wymiarach do 3: **323 rodziny — PASS**.
- Kompletny PDF wczorajszej wersji z CI `45000765561` miał **315 stron**, brak ostrzeżeń/Overfull/Underfull w końcowym logu; rozdział 01 zajmuje strony PDF **6–21 (16 stron)**. Wyrenderowano i skontrolowano montaż wszystkich 16 stron starej wersji. Oba rysunki znajdują się we właściwych sekcjach, bez widocznego konfliktu układu.

## Decyzja
**Audyt I: wykryto i poprawiono jedną lukę w uzasadnieniu. Nie jest czysty.**
Po zapisie wymagane ponowne pełne CI dla zmienionego źródła, samodzielny PDF nowej wersji, oględziny obu rysunków, a następnie co najmniej dwa kolejne niezależne czyste audyty `iteration_02.md` i `iteration_03.md` na niezmienionym źródle.
