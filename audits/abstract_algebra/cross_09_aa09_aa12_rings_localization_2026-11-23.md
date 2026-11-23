# AA-X09 — przekrojowy audyt AA-09–AA-12: pierścienie, podzielność, wielomiany i lokalizacja

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD przed audytem i ponownie przed zapisem:** `39681861afb3ccd5d609702eb65612941d1ea8d9`.

## Zakres
Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, `catalog/books.json`, plik główny książki i źródła AA-09–AA-12. Sprawdzono wcześniejszy raport przekrojowy X08. Katalog zawiera AA-01–AA-42; nie stanowi to niezależnego dowodu nieistnienia nieujętego w katalogu AA-43. Zakres X09 jest odmienny od X08 (AA-01–04) i wcześniejszych kontroli przekrojowych reprezentacji, teorii Galois oraz wyróżników.

## Sprawdzenie strukturalne
Źródła AA-09–AA-12 mają odpowiednio 41, 26, 37, 36 deklaracji `\\label` (razem **140**) oraz 1, 1, 18, 7 użyć `\\ref`/`\\eqref`/`\\cref`/`\\autoref` (razem **27**). Wśród 140 etykiet nie znaleziono duplikatów, a wszystkie 27 użyć ma cel w obrębie tych czterech rozdziałów. Kontrola ma charakter statyczny, obejmuje wymienione polecenia i nie zastępuje analizy wszystkich makr oraz pełnego buildu. W czterech źródłach nie wykryto wyszukiwanych form `rozszczep...`, `tensorowan...`, `unia zbior...`, `relacja liniowa` (kontrola tekstowa, niepełna ocena językowa).

## Sprawdzenie matematyczne
Przejrzano wybrane zależności: definicja ideału pierwszego i ilorazu (AA-09) -> pierwszość elementu w dziedzinie ideałów głównych (AA-10) -> lemat Gaussa i kryteria nierozkładalności (AA-11); konstrukcja ciała ułamków (AA-11) -> lokalizacja i ciało reszt lokalizacji (AA-12). Nie wykryto sprzeczności w kontrolowanych fragmentach, ale **nie wykonano kompletnego niezależnego sprawdzenia wszystkich dowodów**.

Niezależnie uruchomiono pięć asercji Pythona:
1. Nilpotenty w `Z/12Z` to dokładnie klasy 0 i 6 (AA-12).
2. Pierwiastki `x²−1` w `Z/8Z` to 1, 3, 5, 7 (AA-11).
3. Nasycenie `(6)` po odwróceniu 2 w `Z` odpowiada `(3)` na reprezentatywnym przedziale −36…36 (AA-12).
4. `sqrt((12))=(6)` sprawdzone dla całkowitych z przedziału −36…36 i potęg do 7 (AA-12).
5. `gcd(252,198)=18=4·252−5·198` (AA-10).
**Wynik: 5/5 PASS** dla tych asercji; nie są dowodami ogólnych twierdzeń.

Przykład AA-12 wykazujący nieprzechodniość naiwnej relacji iloczynów krzyżowych w `Z/6Z` sprawdzono bezpośrednio: `(0,1)~(0,2)`, `(0,2)~(3,1)`, ale `(0,1)!~(3,1)`; mnożnik 2 zeruje różnicę 3. Przykład jest poprawny.

## Kompilacja, PDF, CI i ograniczenia
Repozytorium nie jest dostępne przez lokalny Git (DNS: `Could not resolve host: github.com`); odczyt źródeł odbył się przez konektor GitHub. **Nie wykonano kompilacji LaTeX, inspekcji PDF ani uruchomienia/potwierdzenia CI**. Nie wprowadzano poprawek do zatwierdzonych rozdziałów i nie resetowano ich liczników czystych audytów. Nie proponuje się nowych twierdzeń. Brak wykrytych błędów w wybranych kontrolach nie oznacza stabilności całych AA-09–AA-12.

## Następny krok
Ponownie odczytać HEAD, ustalić czy AA-43 istnieje w pełnym drzewie źródeł (nie tylko katalogu); w jego braku przeprowadzić kolejny **odmienny** audyt przekrojowy, preferencyjnie AA-13–AA-16. Gdy będzie dostępny pełny checkout, wykonać kompilację i wizualną inspekcję PDF oraz weryfikację CI.
