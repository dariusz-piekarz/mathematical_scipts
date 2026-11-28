# AA-57 — audyt V: reprezentacje dołączone, ilorazy i przypadki brzegowe

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob a64577b1841a14ea92d6ed08de7db6248684be76, commit 8b9b02e4c3eaa41ac8e6096a4df421ba21de6b3d.

## Wykonana niezależna kontrola reprezentacji i ilorazów
Kod JavaScript konstruował stałe struktury C_ijk, macierze ad(e_i) oraz macierze działania indukowanego na ilorazie przez centrum. Wymiar centrum i algebry pochodnej obliczono przez dokładną eliminację całkowitą BigInt z redukcją przez NWD. Sprawdzono równanie [ad(e_i),ad(e_j)]=ad([e_i,e_j]) i analogiczne równanie dla reprezentacji ilorazowej dla wszystkich uporządkowanych par wektorów bazowych. Wyniki (wymiar, centrum, pochodna, iloraz przez centrum): zerowa (0,0,0,0), abelowa 1 (1,1,0,0), abelowa 4 (4,4,0,0), aff(1) (2,0,1,2), Heisenberga (3,1,1,2), sl2 (3,0,3,3), sl2+K (4,1,3,3), filiform n=4,...,10 (n,1,n-2,n-1). Łącznie 14 instancji i 835/835 kontroli tożsamości reprezentacji; dla ilorazów zerowych warunek jest pusty. Rangi reprezentacji dołączonych to n-dim Z. Nie są to nowe twierdzenia w rozdziale.

## Kontrola matematyczna i redakcyjna
Ponownie sprawdzono definicje alternującego nawiasu, w tym charakterystykę 2, ideału, ilorazu i homomorfizmu. Zmiana reprezentantów w ilorazie daje trzy składniki w ideale; w reprezentacji ilorazowej wystarczy niezmienniczość podmodułu. Sprawdzono przypadki zerowego wymiaru flag i algebry, n=1 algebr trójkątnych, sl1, so1 i sp2 oraz rozróżnienie nilpotentności operatorów od nilpotentności algebry Liego. Sprawdzono ponownie hipotezy twierdzeń Engela i Liego oraz zastosowanie do algebry pochodnej. Nie znaleziono nowej usterki w badanym zakresie. Wszystkie 13 wystąpień odsyłaczy do 11 różnych celów jednoznaczne w AA-56–57, środowiska LaTeX zrównoważone. Bez zmian źródła. Propozycja jawnych derywacji Heisenberga i sl2 pozostaje poza obecnym zakresem.

## CI
Run 45363665637, job 138339753759, ostatni odczyt in_progress: 100 success, 1 in_progress, 22 pending, 0 failure. Brak artefaktu, nie wykonano oględzin PDF.

## Werdykt
Dwa czyste audyty po III: 2/2. AA-57 W AUDYCIE TECHNICZNYM do pełnego CI i oględzin PDF dla aktualnego blobu. AA-58 nieotwarty.
