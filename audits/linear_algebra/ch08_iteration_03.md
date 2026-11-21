# Algebra liniowa — rozdział 08, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/08-odwzorowania-wieloliniowe.tex`  
**SHA zweryfikowanej treści:** `75855375e2e2cddaef81fd1ad384b307c79287b8`

## Cel

Po redakcyjnej korekcie odsyłacza w audycie II ponownie zweryfikowano istniejący tekst rozdziału 08, bez dodawania materiału i bez zmieniania założeń twierdzeń.

## Wyniki sprawdzenia

1. **Definicje i założenia:** wieloliniowość jest określona dla dowolnego ciała, w tym przypadków charakterystyki `2`; formy skalarne mają wartości w `K`, a wartości wektorowe w `W`; twierdzenia wymiarowe jawnie wymagają skończonego wymiaru; wyróżniono `k=0` i zerowe wymiary.
2. **Konstrukcja ze współczynników:** istnienie i jednoznaczność zostały udowodnione oddzielnie; każdy wektor ma jednoznaczne współrzędne w bazie, a rozszerzenie formy na dowolne argumenty wynika z liniowości w każdym z nich.
3. **Formy dwuliniowe:** wzór `b(v,w)=x^T A y`, transformacja `A_C=P^T A_B P`, lewy radykał `ker A^T`, prawy radykał `ker A` i kryterium niezdegenerowania są poprawne i zgodne z poprzednimi rozdziałami.
4. **Formy symetryczne:** wymiar `binom(n+k−1,k)` otrzymano przez liczenie niemalejących krotek indeksów bazowych, niezależnie od dzielenia przez `k!`. Dowód obowiązuje także przy dodatniej charakterystyce ciała.
5. **Formy naprzemienne:** `binom(n,k)` niezależnych wartości na rosnących krotkach bazowych, z niezależną bazą determinantową; argumenty obejmują przypadki `k>n` i `n=0`. Nie utożsamiono niepoprawnie antysymetrii z naprzemiennością w charakterystyce `2`.
6. **Operatory:** nieznormalizowana symetryzacja ma obraz symetryczny, a alternowanie ma obraz naprzemienny; ostatni wniosek uzyskano przez parowanie składników o przeciwnych znakach również w charakterystyce `2`. Rzutowania przez dzielenie przez `k!` wprowadzono wyłącznie wtedy, gdy `k!1_K ≠0_K`.
7. **Polaryzacja:** suma po wszystkich podzbiorach usuwa krotki niewykorzystujące każdego indeksu, pozostawiając dokładnie `k!` równych składników. Rozróżniono samą tożsamość od rekonstrukcji przez dzielenie.

**Wynik matematyczny:** nie wykryto kolejnego błędu, nieprecyzyjnego kwantyfikatora ani istotnej luki dowodowej. Plik rozdziału pozostawiono bez zmian.

## Niezależne testy i spójność

Powtórnie przejrzano wyniki testów z audytu II: 12 konfiguracji wymiarów form nad `F_2` i `F_3`, 60 073 sprawdzenia polaryzacji oraz 8000 konfiguracji prawa zmiany bazy form dwuliniowych; brak rozbieżności. Statyczna kontrola ośmiu rozdziałów wykazała **346 niepowtarzających się etykiet oraz 140 poprawnych odsyłaczy**, bez błędów zagnieżdżenia środowisk, niedozwolonych wyrażeń i brakujących importów. Pierwszy pełny CI dla rozdziału 08 zakończył się sukcesem (PDF 85 stron, końcowy log bez ostrzeżeń; walidacja CLI i testy aplikacji również `success`). CI dla poprawionej redakcyjnie wersji i późniejszego commitu raportowego należy sprawdzić oddzielnie; nie wolno uznać samego zapisu raportu za wynik kompilacji.

## Decyzja

**Rozdział 08 stabilny i zamknięty po trzecim, czystym audycie matematycznym.** Zmiana tego commitu ogranicza się do raportu i komentarza w pliku głównym. Rozdziały 01–08 pozostają w ustalonej kolejności; następny w planie jest rozdział 09 poświęcony iloczynom tensorowym.
