# Algebra liniowa — rozdział 05, audyt 4 (ponowna kontrola niezależna)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex`  
**SHA bloba skontrolowanej treści:** `f94bdf0b4a35730e858c50cb7fb7288b117facf6`

## Zakres i rezultat audytu

Przeprowadzono nową iterację kontroli aktualnego rozdziału 05, bez dodawania nowych tematów, definicji, lematów ani twierdzeń. Oceniono kompletność założeń, poprawność matematyczną istniejących wyników, poprawność rachunków, spójność terminologii, odniesienia do poprzednich rozdziałów, przypadki brzegowe oraz algorytmiczną konstruktywność dowodów.

1. **Operacje elementarne:** każda z trzech operacji jest odwracalna, a pomnożenie z lewej strony przez odpowiednią macierz elementarną odtwarza przekształcenie na wierszach. Dla układu `Ax=b` te same operacje należy zastosować jednocześnie do `A` i `b`; nie wolno wnioskować, że wierszowo równoważne macierze mają identyczny obraz w `K^m`.
2. **Algorytm Gaussa:** przy poszukiwaniu niezerowego pivotu dzielenie jest legalne w dowolnym ciele; przeszukiwanie kolumn i zwiększanie numeru wiersza dowodzą zakończenia. Eliminacja wsteczna zachowuje wcześniej uzyskane zera w kolumnach bazowych.
3. **Rząd i zmienne swobodne:** podstawianie wstecz wyznacza bijekcję między jądrem a przestrzenią parametrów wymiaru `n-r`; wykorzystano poprawnie wzór wymiarowy z poprzedniego rozdziału.
4. **Kryterium zgodności:** dodanie prawej strony `b` jako kolumny zwiększa rząd o jeden dokładnie wtedy, gdy `b` nie należy do obrazu. Sprzeczny wiersz `(0,...,0 | beta)` z `beta != 0` wykrywa niezgodność; dowód obejmuje także `m=0` i `n=0`.
5. **Bazy jądra i obrazu:** w konstrukcji wektorów jądra każdej zmiennej swobodnej odpowiada dokładnie jeden wektor. Dla obrazu należy wybrać kolumny bazowe **pierwotnej macierzy**, nie jej postaci zredukowanej; dowód z mnożeniem przez odwracalną macierz `P` jest prawidłowy.
6. **Jednoznaczność postaci zredukowanej:** wykazane pozycje pierwszego niezerowego wyrazu niezerowych wektorów przestrzeni wierszy są niezmiennikiem tej przestrzeni. Porównanie współrzędnych w kolumnach bazowych jednoznacznie ustala każdy niezerowy wiersz, także w przypadku przestrzeni wierszy `{0}`.
7. **Metoda Gaussa–Jordana:** po obustronnej redukcji bloków macierzy rozszerzonej `[A|I_n]` lewy blok `I_n` oznacza, że prawy blok jest `A^{-1}`. Uwzględniono rozmiar `0×0`.
8. **Przykłady:** skontrolowano postać schodkową i zredukowaną macierzy `3×4`, jej rząd `2`, bazę jądra i obrazu, rozwiązalność dla `b=(3,7,4)`, sprzeczność dla `b'=(3,7,5)` i mnożenie macierzy przez obliczoną odwrotność `2×2`.

**Wynik:** w aktualnej treści rozdziału 05 **nie wykryto błędu merytorycznego ani istotnej luki dowodowej**. Rozdział pozostaje bez zmian; nie ma potrzeby jego ponownego otwierania w tym cyklu.

## Niezależna kontrola obliczeniowa

W nowej iteracji testów napisano oddzielne procedury redukcji wierszowej oraz enumeracji wszystkich wektorów. Obejmują one wszystkie rozmiary `0≤m,n≤3`, z pustymi macierzami włącznie:

| Test | Liczba | Wynik |
| --- | ---: | --- |
| Wszystkie macierze nad `F_2` | 689 | 0 rozbieżności |
| Wszystkie układy `Ax=b` nad `F_2` | 5054 | 0 rozbieżności |
| Wszystkie macierze nad `F_3` | 21304 | 0 rozbieżności |
| Wszystkie permutacje wierszy badanych macierzy nad `F_2` | 3699 | 0 rozbieżności |

Dla każdej macierzy porównano liczbę pivotów z mocą obrazu `q^rank`, rozmiar jądra z `q^(n-rank)`, dokładny zbiór rozpięty przez konstruowaną bazę jądra z enumerowanym jądrem oraz zbiór rozpięty przez wybrane kolumny pierwotnej macierzy z enumerowanym obrazem. Nad `F_2` każdy układ `Ax=b` oceniono niezależnie trzema metodami: przez enumerację rozwiązań, porównanie rzędów oraz obecność sprzecznego wiersza po redukcji. Dodatkowo dla wszystkich **21993** macierzy nad `F_2` i `F_3` porównano wynik redukcji z wyborem pierwszego oraz ostatniego dostępnego pivotu; obie procedury dały identyczną postać schodkową zredukowaną. Testy skończone nie zastępują dowodów ogólnych.

## Spójność i narzędzia

Z aktualnej gałęzi pobrano ponownie wszystkie pięć rozdziałów. Wynik: **226 etykiet, wszystkie unikalne; 102 odsyłacze z istniejącymi celami; brak błędnie zagnieżdżonych lub niedomkniętych środowisk; brak wykrytych niedozwolonych form terminologicznych**. Kolejność rozdziałów w `catalog/books.json` odpowiada dokładnie importom w `books/pl/linear_algebra.tex`. Nie naruszono obowiązującej zasady „suma zbiorów” ani „warunek niezależności liniowej”.

Poprzedni CI dla identycznej treści rozdziału: [44908793211](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44908793211) — **success**, w tym podwójna kompilacja PDF i ścisła kontrola ostrzeżeń w końcowym logu. Niniejszy audyt dodaje tylko raport i konfiguracyjny wyzwalacz CI dla przyszłych raportów audytowych. Wynik nowego CI po tej zmianie należy sprawdzić osobno.

**Decyzja:** rozdział 05 pozostaje **zamknięty i stabilny** po czwartej iteracji kontrolnej.
