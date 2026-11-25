# Globalny graf odsyłaczy Biblioteki matematycznej

Zakres: wszystkie rozdziały z catalog/books.json, nie tylko aktualnie otwarte tomy.
Praca wyłącznie na istniejącej gałęzi roboczej. Nie zmieniać oryginalnych etykiet ani dowodów dla pozornej spójności.

## Kolejność przeglądu

Priorytet użytkownika: AA (algebra abstrakcyjna), GA (teoria Galois), TOP (topologia algebraiczna), FA (analiza funkcjonalna), LST (logika i teoria mnogości), GT (topologia ogólna), LA (algebra liniowa). ALG pozostaje w kolejce kontrolnej po wcześniejszych zmianach. Następnie pozostałe tomy, również nowo dopisane do katalogu.

Każda iteracja:
1. Przebudować indeks i odczytać raport graph_coverage.json; sprawdzić brakujące rozdziały, ścieżki, kolizje, izolowane węzły i brakujące krawędzie między dziedzinami.
2. Przejrzeć kolejne rozdziały priorytetowego tomu i istniejące odpowiedniki definicji, twierdzeń, dowodów i przykładów w innych tomach.
3. Dodać jawny odsyłacz tematyczny `\atlasref{ID-ROZDZIALU::oryginalna-etykieta}{opis}` przy właściwym fragmencie, zachowując istniejące etykiety. Nie wymuszać połączenia każdej pary dziedzin.
4. Uzupełnić testy regresyjne, wykonać indeksowanie i kontrolę CI; sprawdzić graf na poziomie rozdziału, sekcji i obiektu, także odwrócenie dziedzin. Dopiero po zaliczeniu kontroli przechodzić dalej.
5. Rozróżniać jawne odsyłacze tematyczne od zależności kompilacyjnych i dowodowych. Brak krawędzi nie oznacza braku związku matematycznego.

## Stan początkowy (25 listopada 2026)

- Katalog: 21 tomów, 565 rozdziałów w odczytanej migawce.
- GA-00–GA-09: 14 dodanych odsyłaczy do AA; ALG-00–ALG-10: 38 do AA i TOP.
- LA-01, 02, 03, 10, 19, 20: 10 nowych odsyłaczy do AA-16–18.
- Raport globalny i API /api/graph/coverage: zapisane, CI do potwierdzenia.
- Następny krok po stabilizacji: reszta LA i AA, następnie FA–GT–LST–TOP. W szczególności przegląd odsyłaczy do twierdzenia Zorna, baz Hamela, filtrów, sieci, zupełności, przestrzeni ilorazowych i tensorów.
- Liczby oznaczają wykonane zmiany źródłowe, nie zakończenie audytu całych tomów.
