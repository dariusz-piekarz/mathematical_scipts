# Audyt 194 — drukowany rozdział 20, zamknięcie etapu A

Data: 2026-11-25. Kontynuacja 193 bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex.
Commit źródłowy 0991cb332182507dee3db82b357f048324b44969, blob 52e28adc146a90688df02e04f1b225efcde82c59 potwierdzony na aktualnej gałęzi. Bez zmian źródła.

## CI i PDF
Dla wskazanego SHA: pełny audyt 45572737213, algorytmy 45572737294, terminologia 45572737114, aplikacja 45572737085 — wszystkie SUCCESS.
Pobrano rzeczywisty artefakt 15002223248, rozpakowano i sprawdzono PDF (343 strony, plik ostrzeżeń 0 bajtów). Rozdział 20 obejmuje strony PDF 172–178 (druk 162–168), rozdział 21 zaczyna się na PDF 179. Jedna adnotacja odsyłacza. Wyrenderowano wszystkie siedem stron w skali 1.6, obejrzano dwa arkusze kontaktowe i pełną stronę 175. Oznaczenia a,b,c,d oraz podpis zewnętrznej ściany czworościanu są czytelne i bez kolizji; na rysunku ruchu 2->2 wszystkie wierzchołki mają oznaczenia. Preferowany podział przed stwierdzeniem o subdywizji nie wymusił przeniesienia stwierdzenia: jest ono w całości na stronie 177, dowód zaczyna się na 178. Wypowiedź kryterium ogniwa przechodzi ze strony 173 na 174; ostatnia strona częściowo zapełniona. Pozostawiono te dopuszczalne podziały, nie wprowadzając kolejnego cyklu kosmetycznych zmian. Nie zauważono obcięć ani kolizji.

## Zależności
Domknięto rozpoczęte w 191–193 przeszukanie wszystkich dalszych plików źródłowych 14–43 (30 plików), sprawdzając 23–43 w trzech grupach po siedem plików. Nie znaleziono zależności od konwencji pustego sympleksu w ogniwie. Trafienia w 25 i 35 to operatorname{lk} oznaczające liczbę zaczepienia, nie ogniwo symplicjalne. W źródle 16 występuje zgodna geometryczna interpretacja ogniwa. Jest to celowane przeszukanie tekstowe, nie pełny audyt późniejszych rozdziałów. Nie zmieniano innych źródeł.

## Regresje
GKT-20-LINK-MOVES-01 PASS: 1044 przypadki, 17 spełniających warunek spójnej powierzchni, 92 ruchy 1->3, 42 dopuszczalne i 96 zablokowanych 2->2, 24 zablokowane 3->1, 138 podziałów krawędzi, 1 przypadek niespójnego ogniwa.
GKT-20-CHAIN-01 PASS: 873 uporządkowania, 873 kontrole brzegu brzegu, 4166 transpozycji, 2197 trójek całkowitych, 503 trójki nad czterema ciałami.
Oba skrypty pobrano i ponownie wykonano w izolacie JS. Nie formalizacja Lean; nie potwierdzono wykonania w procesie Node ani wywołania przez CI.
7 etykiet i 48 poprawnie zagnieżdżonych par środowisk. Brak nowych zidentyfikowanych istotnych usterek w zakresie audytu A.

## Decyzja
Etap A zamknięty dla wskazanego blobu. Następny audyt 195: niezależna kontrola B, bez rozszerzania zakresu. Rozdział 20 jeszcze niezamknięty. Postęp całego tomu 19/44. Proponowanego kryterium powierzchni z brzegiem i orientowalności nie dodano bez akceptacji użytkownika.
