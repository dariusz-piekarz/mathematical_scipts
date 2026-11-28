# Algebra liniowa — rozdział 05, audyt 2

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex`

## Usterka składu i korekta

Z pierwszego przebiegu CI po utworzeniu rozdziału: [44908413216](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44908413216) — wszystkie zadania kompilacji i statycznej walidacji zaliczone, jednak końcowy log ujawnił **Overfull \\hbox (19.6003 pt) przy wierszu 478** nowego rozdziału. Problem dotyczył długiego wzoru definiującego wektory bazowe jądra w Twierdzeniu `thm:lin5-baza-jadra`, a nie błędu matematycznego. Rozdzielono równania definicyjne na trzy wiersze wewnątrz `aligned`, zachowując warunki dla wszystkich pivotów i wszystkich swobodnych indeksów. Konieczna jest powtórna kompilacja po poprawce.

## Niezależne wyczerpujące testy nad F_2

Przeprowadzono osobną implementacją wyczerpujące sprawdzenie wszystkich **689 macierzy** rozmiaru `m × n`, gdzie `0 ≤ m,n ≤ 3`, oraz wszystkich **5054 układów** `Ax=b` nad `F_2`. Kontrolowano liczbę pivotów i rząd (przez moc obrazu), liczbę rozwiązań jednorodnych, bazę jądra z postaci zredukowanej, bazę obrazu z oryginalnych kolumn bazowych, zgodność układu z kryterium rzędu macierzy rozszerzonej oraz wykrywanie sprzecznych wierszy. **Wynik: 0 rozbieżności.** Testy wspierają kontrolę, ale nie zastępują ogólnych dowodów.

## Integralność

Po utworzeniu rozdziału 05 kontrola wszystkich pięciu rozdziałów wykazała **226 unikalnych etykiet, 102 odsyłacze z istniejącymi celami**, brak błędów zagnieżdżenia środowisk i brak naruszeń wymagań terminologicznych. Po zmianie wzoru liczba i nazwy etykiet są niezmienione. Workflow `validate-cli` dla pierwszego commitu zakończył się sukcesem. Rozdział 05 pozostaje otwarty: potrzebne są kontrola końcowego logu po korekcie oraz kolejny audyt stabilizacyjny.
