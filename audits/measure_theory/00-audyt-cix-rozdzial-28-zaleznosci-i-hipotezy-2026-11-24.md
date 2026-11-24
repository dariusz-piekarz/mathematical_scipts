# Audyt CIX (109) — zależności, hipotezy i dowody wykresu
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 059d5a5b69e6f4e612686a2654149a9e8147e980, blob 28034caf65c2721e46f320a978609f38b672ae3e. Commit źródłowy cd628415d3a9bbc56b11dae97ef7af0f475bba0e, blob aa60f0af2f22ae958372ec832120de11d82323c9.

## Kontrola matematyczna
Dziesięć celowanych zmian, 28 etykiet zachowanych w tej samej kolejności.
- Uzasadniono dodatnią półokreśloność macierzy Grama, jej jądro, kryterium rangi, przypadek kwadratowy oraz analogiczne własności jakobianu normalnego.
- Doprecyzowano kwantyfikację punktu y w definicji krotności.
- W lemacie o wykresie rozpisano całkową resztę i wybór malejącego błędu z ciągłości Dh.
- W twierdzeniu o wykresie sprawdzono dokładne sformułowania twierdzeń w rozdziałach 18 i 25. Zamiast ogólnego odwołania do różniczkowania miary na R^k dla miary określonej na V zastosowano lokalne różniczkowanie całek: gęstość lokalnie całkowalna, ograniczenia do kul z domknięciem w V i przedłużenie przez zero. Rozpisano przejście od równości miar do całek funkcji charakterystycznych, prostych, nieujemnych, rzeczywistych i zespolonych.
- W przykładzie okręgu obliczono wszystkie krotności, także wyjątkowy punkt, i długość okręgu przez zastosowanie już udowodnionego wzoru do różnowartościowej parametryzacji.
- Uzupełniono wymiary i konstrukcję blokową w lemacie liniowo-algebraicznym oraz pełne hipotezy twierdzenia o gęstości miary obrazowej. Wskazano dokładną etykietę twierdzenia Radona–Nikodyma dla miar sigma-skończonych.
- Łańcuch dowodowy: kalibracja i nierówność Lipschitza (26), Radon i różniczkowanie (20,25), wykres, immersja, submersja, Rademacher i Whitney, niezależne oszacowania krytyczne, wzory Lipschitzowskie, wersja rozmaitościowa. Nie znaleziono błędnego koła w tym łańcuchu. Kontrola nie jest formalnym dowodem poprawności wszystkich twierdzeń.

## CI
Przebieg 45351151128 (wersja CVIII, 9b41bb602aee7f73222b1584f9b9424b2aba276d): testy, PDF i publikacja statusów zakończone sukcesem; artefakt 14899973359 dostępny. Nie pobierano go w tej iteracji, nie deklaruje się nowych oględzin. Wersja CIX wymaga ponownego CI i kontroli PDF.
## Otwarte
Niezależny audyt pozostałych szczegółów Rademachera, Whitneya, włókien krytycznych i wersji na rozmaitościach; ponowna kontrola terminologii, kompilacji i PDF. Rozdział 28 nadal otwarty, stan 27/31. Nie przechodzić do 29. Bez rozszerzania zakresu.
