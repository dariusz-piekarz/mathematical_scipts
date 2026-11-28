# Audyt 175 — drukowany rozdział 18, etap A (stabilizacja)

Data: 2026-11-25. Kontynuacja raportu 174, bez poszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit korekty: b6f205965c0afa792cb1405c14df7d8e1fdecf49.
Blob po korekcie: b4b3d39301ba2e8f1a70ce8f8f947960b0f07da3.

## Kontrola semantyczna i poprawki
- Uzasadniono lokalnie, dlaczego przy dodatniej rotacji przejście sigma alpha ma ścianę po prawej: przy ruchu do środka dysku prawa strona odpowiada rosnącemu kątowi, przy ruchu na zewnątrz malejącemu. Uwzględniono stopień jeden.
- Ponownie sprawdzono rozcięcie dysków ścian i sklejenie sektorów wokół wierzchołków, także dla pętli, mostów i jednokrawędziowego obchodu; nie stwierdzono nowej sprzeczności w tej konstrukcji.
- Zapisano jawnie odwrócenie cyklu półkrawędzi i trzy przypadki współczynnika dodatniego brzegu: +1, -1, 0, w tym anulowanie dwóch stron tej samej ściany. Wzory dualnej rotacji z audytu 174 pozostają bez zmian.
- Rozwinięto dowód rzędu macierzy incydencji nad R przez bazę różnic wierzchołków, z przypadkiem n=1, oraz wskazano użycie twierdzenia o homologii komórkowej.
- Sprawdzono redukcję całkowitą po drzewie dualnym: operator różnic jest surjektywny nad Z, jego jądro to stałe rodziny, a cykle fundamentalne spoza obu drzew są bazą ilorazu. Brak nowego błędu.
- Ujednolicono terminologię „graf dualny” i „zanurzenie”; wszystkie 14 etykiet zachowano. Ponowny odczyt commitu potwierdził blob i 43 poprawnie zagnieżdżone pary środowisk.

## Regresje wykonane w tej iteracji
Pobrano cztery wersjonowane skrypty JS z gałęzi i wykonano ich kod w izolacie JS, z przechwyceniem console.log i równoważną implementacją wymaganych asercji Node; nie uruchamiano procesu Node.
- GKT18-BRIDGE-01: PASS, 1067 mostów.
- GKT-18-ROT-01: PASS, 7776 rotacji K5 (462 torusowe) oraz 64 rotacje K3,3 (40 torusowych); minimalny rodzaj 1.
- GKT-18-TC-01: PASS, 2546 układów, 2221 spójnych, 4442 rozkłady, 8996 elementów bazy, 12354 relacje.
- GKT-18-ORIENT-01: PASS, 2546 układów, 2221 spójnych, 6177 kontroli znaków. Jest to istniejąca trwała regresja dotycząca doprecyzowanej formuły brzegu. Próby TC i ORIENT pokrywają się.
Kontrole wykonano przed redakcyjną korektą źródła; testy matematyczne nie zostały zmodyfikowane. Nie jest to formalizacja Lean ani dowód geometryczny.

## Bramka
Zapytanie Actions dla commitu korekty nie zwróciło przebiegu w chwili kontroli. Nie wykonano lokalnej kompilacji ani oględzin PDF po tej korekcie. Nie przenosimy wyników CI z wcześniejszego blobu na nowy. Etap A pozostaje otwarty; weryfikacja CI i PDF, następnie osobny audyt kontrolny B. Nie przechodzimy do następnego rozdziału.
