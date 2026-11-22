# Topologia ogólna — rozdział 23, audyt 06 (nadmiarowy, czysty 3/2)

**Data:** 2026-11-22.
**Weryfikowany blob (bez zmian od audytów 04 i 05):**
`9dc1ed4784d929b405d00a3216865418f240a37c`.
**Wynik:** CZYSTY 3/2 — wymagane dwa czyste audyty
i jeden dodatkowy zakończone.

## Próby obalenia wyników przypadkami granicznymi

1. X=∅: wymiar -1 w definicjach; przypadki
   „dla każdego pokrycia” i „dla każdego punktu”
   nie służą do sztucznego przypisania wymiaru 0
   pustej przestrzeni.
2. X z jednym punktem: baza clopen i rząd 1;
   wymiar dokładnie 0, a twierdzenie o
   dodatnim wymiarze spójnego X wymaga >=2 punktów.
3. Pokrycie zawierające U_i=∅:
   nie jest to wierzchołek nerwu;
   współrzędna barycentryczna tego indeksu
   jest równa 0. Przypadek U_i=X
   ma osobne poprawne określenie psi_i=1,
   dzięki czemu nie używa odległości do ∅.
4. Rodzina indeksów iloczynu pusta:
   iloczyn zwartych przestrzeni wymiaru 0
   jest singletonem. Nie mylono go
   z pustą przestrzenią.
5. K zwarty, ale pusty, w twierdzeniu o wymiarze
   euklidesowym: obsłużony oddzielnie;
   lemat liczby Lebesgue'a używany jedynie
   dla K niepustego.
6. Sześcian n=1: pokrycie przeciwległych ścian
   redukuje się do dwóch otwartych przedziałów,
   a lemat Poincarégo–Mirandy odpowiada
   własności Darboux. Dowód ogólny działa
   również przy n=1.
7. Wybór wektorów ortantowych przy n=1:
   do odrzucanych podprzestrzeni
   należy rozpiętość rodziny pustej, czyli {0};
   ortant ma niepuste wnętrze,
   więc wybrany wektor jest niezerowy.
   Przy m>n wybieramy ogólne położenie
   wszystkich podrodzin długości <=n.
8. Wymiar zbioru Cantora i wymiar Hausdorffa
   to różne pojęcia: tekst odwołuje się do
   clopen bazy, a nie do miary Hausdorffa.
9. Ciągły obraz Cantora na [0,1] może zwiększyć
   wymiar pokryciowy: konstrukcja nie
   jest zanurzeniem, więc nie przeczy
   niezmienniczości przy homeomorfizmach.
10. Wykorzystanie Brouwera:
    przywołany wynik jest już udowodniony
    w AT-19 dla domkniętej kuli D^n,
    a przejście do kostki ma
    jawny, poprawny homeomorfizm radialny.
    Nie wstawiono ponownie pełnego
    dowodu twierdzenia Brouwera.

## Kontrola niezależna wydania

W pliku źródłowym nadal 40 etykiet,
23 odsyłacze i niezmieniony identyfikator bloba.
Wynik zakończonego CI 45051754287 to PASS.
Rzeczywisty PDF rozdziału: 9 stron A4,
wszystkie obejrzane w audycie 04,
a strona ostatnia sprawdzona osobno
po usunięciu osieroconego podsumowania.
Oględziny obejmują również
rysunek rodziny przedziałów na stronie 5;
nie występują nakładające się podpisy.
Kontrola logów kompilacji dla rozdziału
i całej książki: brak Overfull/Underfull,
brak Missing character i brak ostrzeżeń LaTeX.
Wyniki testów regresyjnych rozdziałów 01–23
i globalnej struktury: sukces.

**Rozdział 23 stabilny matematycznie i wydawniczo.
Gotowy do zmiany oznaczenia na 01–23 stabilne,
pod warunkiem wykonania dodatkowego CI
po samej aktualizacji tytułu i testów wersji.**
