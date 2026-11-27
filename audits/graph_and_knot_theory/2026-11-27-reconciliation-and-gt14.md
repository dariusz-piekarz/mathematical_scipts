# Uzgodnienie audytów GT — 2026-11-27

Skrypt books/pl/graph_and_knot_theory.tex zawiera 42 wejścia: wstęp GT00 oraz 41 rozdziałów merytorycznych GT01–34 i GT37–43. GT35–36 nie są włączone.

Wcześniejsze raporty konwersacyjne z 27 listopada deklarują zakończenie 41/41 audytów szczegółowych, w tym 334–337 dla GT14–34 oraz poprawki GT24/32/33 w audycie 340 i czysty przebieg 341. Nie odzyskano kompletnych raportów ani SHA tych przebiegów, zatem nie jest to niezależny certyfikat wersji źródeł.

Porównanie GitHub od d7e2f71806f39514ea2f3ba6590c5ae2ed0e6725 do gałęzi w chwili odczytu: 92 commity naprzód, 53 pliki zmienione, w katalogu rozdziałów GT tylko GT12, GT13 i GT14. Porównanie nie potwierdza stanu sprzed punktu odniesienia.

| Rozdział | Blob | Ostatni wynik |
|---|---|---|
| GT12 | cdbb8ec13b91e5f5bf8cac37ba4fb5c782f06f7c | Kontrolny merytoryczny bez zmian; 760 multigrafów w teście zgodności definicji i dwóch kolejności rekurencji |
| GT13 | b090cb8f7d2485d47e8eee7774ec5194ac02832e | Kontrolny w sprawdzonym zakresie bez zmian; poprzednio 702 ruchy Pachnera bez naruszenia inwariantów |
| GT14 | 0718c6837140a6389f75ecccfab64072c653fa5e | Drugi audyt: sprawdzono dowód wzoru dla powierzchni nieorientowalnych, klasyfikację pasa siodłowego, liczenie stopni i charakterystykę Eulera; brak nowych usterek w sprawdzonym zakresie; 8/8 celów odsyłaczy, poprawne zagnieżdżenie środowisk, 769 wierszy |

Następnie: niezależny audyt kontrolny zmienionych fragmentów GT14, audyt przekrojowy zależności, terminologii i notacji, pełna kompilacja PDF, odbiór wizualny rysunków i CI. Nie powtarzać automatycznie GT15–34 tylko ze względu na kolejność numeracji. Kontrolować konkretne rozbieżności lub późniejsze zmiany.

Nie przeprowadzono kompilacji PDF, kontroli wizualnej ani pełnego CI w tym przebiegu. Nie certyfikowano wcześniejszych raportów bez identyfikatorów wersji.

## Audyt kontrolny GT14 i pierwsza kontrola przekrojowa

GT14, blob 0718c6837140a6389f75ecccfab64072c653fa5e: ponownie sprawdzono dowód wzoru dla powierzchni nieorientowalnych oraz rachunek homologii szkieletu. Brak nowych usterek w tych fragmentach; źródło bez zmian.

Pobrano wszystkie 42 pliki rozdziałów z listy wejść książki (blob listy fa90ea1b3c9fc9ab09061ca77448a5d1b735bc4d), łącznie 40179 wierszy. Sprawdzenie zagnieżdżenia środowisk LaTeX po usunięciu komentarzy: 42/42 pliki bez błędów. W czterech partiach wyodrębniono etykiety oraz cele ref, eqref, pageref, autoref, cref i Cref; przy przeglądzie zestawień nie zauważono brakujących celów ani powtórzonych etykiet. Nie wykonano jeszcze jednego maszynowego porównania wszystkich partii: zbiorcze wywołanie przekroczyło limit liczby operacji konektora. To ograniczenie nie dotyczy kontroli zagnieżdżenia, wykonanej dla każdego pliku.

Dalsze prace: mechaniczna kontrola globalnej unikatowości i rozwiązywalności odsyłaczy, terminologia, notacja, PDF i odbiór wizualny oraz CI. Bez powtarzania audytów szczegółowych wyłącznie na podstawie numeru rozdziału.
