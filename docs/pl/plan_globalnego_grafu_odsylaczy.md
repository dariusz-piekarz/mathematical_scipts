# Globalny graf odsyłaczy Biblioteki matematycznej

Zakres: wszystkie rozdziały z catalog/books.json, nie tylko aktualnie otwarte tomy.
Praca wyłącznie na istniejącej gałęzi roboczej. Nie zmieniać oryginalnych etykiet ani dowodów dla pozornej spójności.

## Kolejność przeglądu

Priorytet użytkownika: AA (algebra abstrakcyjna), GA (teoria Galois), TOP (topologia algebraiczna), FA (analiza funkcjonalna), LST (logika i teoria mnogości), GT (topologia ogólna), LA (algebra liniowa), ME (teoria miary — ustabilizowana według użytkownika). ALG pozostaje w kolejce kontrolnej po wcześniejszych zmianach. Następnie pozostałe tomy, również nowo dopisane do katalogu.

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

## Aktualizacja priorytetów

Teoria miary (ME, 31 rozdziałów) wchodzi do grupy ustabilizowanych skryptów objętych pełnym audytem odsyłaczy. Pierwsza partia: ME-14, 15, 20, 21, 22, 23, 30 oraz powiązania z CAL-11, 13, 14 i FA-15B. Dalszy przegląd: konstrukcja miary, mierzalność, miary produktowe, Radon--Nikodym, różniczkowanie miar, miara Hausdorffa, geometria i prawdopodobieństwo. Nie zmieniać treści dowodów bez osobnego audytu.

## Audyt kontrolny ME — pierwsze przejście

Sprawdzono ponownie 67 zapisanych par (źródło, kwalifikowana etykieta) z trzech testów regresyjnych: 64 różne pliki, wszystkie 31 rozdziałów ME jako źródła. Każdy z 67 odsyłaczy występuje dokładnie raz w źródle; każda wskazana etykieta dokładnie raz w docelowym pliku. Nie dodano nowych krawędzi ani nie zmieniono dowodów. Globalny audyt indeksu odrzuca teraz nierozwiązane atlasref i błędne przypisanie właściciela etykiety. Pełne uruchomienie CI, indeksu oraz testów przeglądarkowych pozostaje niepotwierdzone; nie oznaczać grafu jako ustabilizowanego bez dowodu wykonania.
