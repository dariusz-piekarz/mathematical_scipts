# Teoria dystrybucji i analiza harmoniczna — migracja (etap 3)

Data: 2026-11-28. Nazwa robocza: distribution_theory. Planowany prefiks Atlasu: DT (do potwierdzenia przy przełączeniu identyfikatorów).

## Zrealizowane
- Samodzielny roboczy master `books/pl/distribution_theory.tex`, korzystający z jednej kopii kanonicznej AF 17–25 (9 jednostek, 211 etykiet). Zachowano oryginalną numerację na etapie przejściowym.
- Cztery zewnętrzne odsyłacze do AF importowane z functional_analysis.aux z prefiksem, bez importowania nieprefiksowanych kolidujących etykiet.
- Rozdział roboczy 26: materiał RRC-08 o mnożnikach L2, normie operatora, rachunku mnożników i transformatach Riesza, dostosowany do unitarnej konwencji AF. Nowe tymczasowe etykiety dt; historyczne etykiety PDE pozostają w źródle do momentu bezpiecznego przełączenia.
- Rozdział roboczy 27: funkcja maksymalna Hardy'ego–Littlewooda, słaby typ (1,1) z ME-24 oraz rozwinięcie silnego typu (p,p) z pełnym dowodem; powiązanie z różniczkowaniem miar ME-25.

## Granice migracji
| Źródło | Zakres docelowy | Co pozostaje |
|---|---|---|
| AF 17–25 | wszystkie rozdziały, z późniejszym rozdzieleniem teorii jąder i nuklearności | AF I–III oraz zależności do przeniesionych twierdzeń |
| RRC 06 | ogólne szeregi Fouriera, twierdzenia zbieżności | Sturm–Liouville, rozdzielenie zmiennych i zastosowania PDE |
| RRC 07 | dystrybucje, pochodne, nośniki, regularizacja, ogólna konstrukcja rozwiązań fundamentalnych | rozwiązania i regularność konkretnych PDE |
| RRC 08 | ogólna transformacja Fouriera, gauss, Plancherel, mnożniki, transformata Riesza, potencjały Bessela, zasada nieoznaczoności | zastosowania do ewolucji i równań eliptycznych |
| RRC 16 | jądra osobliwe, wartość główna, rozkład Calderóna–Zygmunda, interpolacja słabego typu, oszacowania ogólne | lokalna regularność W^{2,p}, zamrażanie współczynników, Schauder |
| ME 23 | splot i analiza harmoniczna na grupach lokalnie zwartych | konstrukcja i jednoznaczność miary Haara |
| ME 24–25 | użycie lematu 5r, operator maksymalny i jego oszacowania | twierdzenia pokryciowe i różniczkowanie miar jako wyniki teorii miary |

Nie przepisywać bez porównania: AF 17,22 mają już odwrócenie i Plancherela, AF 19–21 teorię dystrybucji i splot. AF normalizuje Fouriera przez (2π)^(-d/2), RRC przez 1 w transformacie i (2π)^(-d) w odwrotnej. Przy przenoszeniu splotu, Gaussa, delta, mnożników i potencjałów Bessela sprawdzić każdą stałą.

## Warunki aktywacji i usunięcia źródeł AF
1. Porównać wszystkie twierdzenia i etykiety RRC/ME z AF, przenieść unikatowe dowody, przykłady i rysunki; stare etykiety zachować jako aliasy.
2. Przełączyć katalog books.json, katalog rozdziałów i identyfikatory Atlasu jedną spójną migracją. Nie rejestrować tych samych dziewięciu ścieżek w dwóch książkach: audit_chapter_dependencies odrzuca wielokrotną własność.
3. Zaktualizować parser module_id, preambuły generatora, odsyłacze FA-17…FA-25 i wszystkie jawne atlasref. Zachować ścieżkę zgodności starych ID.
4. Przepisać testy AF zakładające 35 jednostek i workflow z sztywną listą 1–33. Przenieść dedykowane testy 17–25 bez usuwania regresji. Zweryfikować odsyłacze AF do przeniesionych rozdziałów (w szczególności Fourier w AF 33).
5. Kompilacja AF i nowego skryptu, testy Atlasu i audyt braku utraty etykiet. Dopiero potem usunięcie starych źródeł i końcowa renumeracja.

Etap 1 pozostaje celowo poza katalogiem aktywnych książek Atlasu. Nie jest to jeszcze fizyczne przeniesienie ani ukończony audyt matematyczny. Nie uruchomiono dodatkowych automatyzacji. Kompilacja roboczego mastera wymaga wcześniejszej kompilacji AF z tego samego stanu repozytorium.

## Etap 2 — uzupełnienia Fouriera
- Rozdział 28: szeregi Fouriera na okręgu, Bessel, Fejér, Parseval, gęstość wielomianów trygonometrycznych i różniczkowanie szeregów; przejęto ogólną część RRC-06, bez zagadnień Sturma–Liouville'a.
- Rozdział 29: skala Bessela H^s, izometria J^s, równoważność H^m i W^{m,2}, gęstość przestrzeni Schwartza, kryterium delta w H^s. Normalizacja unitarna, odsyłacze do AF 17–22.
- Rozdział 30: nierówność Heisenberga, przypadki równości, przesunięcie środka i wariancje. Uwzględniono współczynniki transformaty unitarnej.
- Numeracja 17–30 pozostaje tymczasowa. Rozdziały RRC nadal niezmienione; stare etykiety zachowane. Przed przełączeniem katalogu trzeba dopiąć kontrolę kompilacji, deduplikację oraz migrację pozostałych tematów.

## Etap 3 — całki osobliwe i interpolacja
- Rozdział 31: rozwiązanie fundamentalne laplasjanu, jądra Hessianu, główna wartość, człon delta i oszacowanie L2.
- Rozdział 32: gęstość testów, aproksymacja jedności, rozkład dyadyczny, ogólne twierdzenie o słabym typie (1,1), szczególny przypadek interpolacji Marcinkiewicza i ograniczoność w Lp dla 1<p<∞ (z dowodem przez sprzężenie), Hessian oraz kontrprzykłady końcowe. Nie udowodniono jeszcze zbieżności głównych wartości p.w. dla ogólnych danych Lp.
- RRC i AF pozostają nietknięte. Kompilacja i przełączenie katalogu nadal do wykonania.
