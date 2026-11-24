# AA-51 — audyt II: niezależna identyfikacja grup i integracja

Data: 24 listopada 2026 r.; gałąź biblioteka-matematyczna-iteracja-6.

## Pierwsze wykonanie CI
Run 45294695431, job 138112007684, head 77be1a02d035fef3abb9263f8a6c42e2bff8e419: failure w kroku Run repository tool tests. Z logu: 4556 testów, 12 failures; wszystkie dotyczą asercji liczby plików rozdziałów 51 != 50 w dwunastu starych testach przekrojowych AA. Oba nowe moduły w tym samym odkrywaniu testów: 4/4 i 3/3 PASS (w tym dokładna macierz obrotu dwudziestościanu). Dedykowane kroki AA-51, AA-GLOBAL i kompilacja zostały pominięte po błędzie. Poprawiono wyłącznie oczekiwaną liczbę 50 na 51 w zgłoszonych dwunastu asercjach, nie osłabiając sprawdzeń ani nie zmieniając historycznych raportów. Nie deklaruje się jeszcze wyniku nowego CI.

## Audyt dowodów
1. Doprecyzowano skończoność i niezmienniczość zbioru wyjątkowego, wybór reprezentantów oraz definicję m_i.
2. Dla S4 uzupełniono rozłączność par punktów stałych różnych podgrup Sylowa rzędu 3. Argument jądra: jego rząd dzieli 6; 3 nie dzieli rzędu z normalności, a rząd 2 wymusza centralną inwolucję ustalającą osiem punktów, sprzecznie z dwoma punktami stałymi.
3. Dla A5 dopisano identyfikację grupy rzędu 4 z C2 x C2. Liczba 15 inwolucji i centralizatory rzędu 4 wyznaczają pięć rozłącznych (poza jedynką) podgrup Sylowa rzędu 4. Normalne jądro działania ma rząd dzielący 12, niepodzielny przez 2 ani 3 na podstawie zliczenia elementów. Wniosek o A5 pozostaje poprawny.
4. Zastąpiono geometryczny argument o regularnym pięciokącie ścisłą konstrukcją macierzową R=C B^{-1}, z identycznymi macierzami Grama. Dowód pokazuje Rw_i=w_{i+1} przez porównanie iloczynów skalarnych z bazą, R^5=I i det R=1. Jest to samodzielny dowód istnienia obrotu rzędu 5, zgodny z niezależnym testem geometrycznym.
5. Parametry 4,6,12 pozostają długościami minimalnych orbit; nie dowodzą samodzielnie lokalnych list Kovacica.

## Werdykt
AA-51 W AUDYCIE do potwierdzenia pełnych regresji i kontroli PDF po poprawkach. AA-52 nieotwarty.
