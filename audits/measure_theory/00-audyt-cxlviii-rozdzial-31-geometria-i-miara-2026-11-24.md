# Audyt CXLVIII (148) — geometria i teoria miary
Data 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.

## Korekty
Commit dc33d2d4cb8ae988c43db954c78c644951e248b3; blob ea84b20cefbb5b7610c07572da07df6a075a6ebb; 1470 → 1594 wiersze; 30 etykiet bez zmian.
- Formy kontaktowe: lokalny charakter i niezmienniczość wspólnego jądra, rozpisanie reguły transformacji; hipotezy i globalność rzutowania przekroju holonomicznego.
- Symbol główny: działanie na różnicach dżetów, transformacja kowektora, konwencja bez czynnika urojonego.
- Euler–Lagrange: zwarty nośnik, majoranta ilorazów różnicowych, całkowanie przez części i uzasadnienie równania punktowego.
- Rademacher: jawna mierzalna macierz kandydująca, borelowski zbiór zbieżności, odsyłacz do rozdziału 28.
- Sobolew: uzasadnienie inkluzji lokalnych przestrzeni; zachowano jawne przyjęcie twierdzenia o przybliżonej różniczkowalności. BV: lokalna skończoność, gęstość części absolutnie ciągłej i orientacja, rozpisane obliczenie pochodnej charakterystycznej półprzestrzeni.
- Wzory pola i koobszaru: otwarta dziedzina, lokalizacja za pomocą rozłącznych fragmentów i przedłużeń Lipschitzowskich, mierzalność włókien i krotności, normalizacja oraz przypadek braku różniczki. Zweryfikowano etykiety twierdzeń w rozdziałach 28–29.
- Uściślono wprowadzenie o zakresie twierdzenia Whitneya–Luzina. Bez rozszerzenia tematycznego.

## Regresje
MT31-012–014: commit 2ced03e70d2145c7108a964d77c881683c785550; 14 trwałych testów. Kontrole modeli JS: 4096 transformacji form kontaktowych, 343 symboli głównych, 343 tożsamości skoku BV, 81 rozłącznych podziałów włókna i 11 warunków źródłowych. Wszystkie zaliczone. Testów Python lokalnie nie uruchomiono. Poprzednie CI: []. Aktualne CI: []. Nie przeprowadzono nowych oględzin PDF.

## Następny krok
Niezależny przegląd domykający: hipotezy, terminologia, definicje i dowody, w tym kontrola wcześniejszych zmian; CI i wszystkie strony PDF. Zamknięcie tylko po spełnieniu bramek. Stan 30/31.
