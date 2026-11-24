# AA-56 — audyt III: niezależna enumeracja ważonych drzew i układów ADE

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob b75d8fac66195d710df141cdae3e3081b137d687, commit 78aad66a51ad2e4399df2621b8dafb81c3fd7f9c.

## Wykonana enumeracja ważonych drzew
Kod JavaScript z BigInt generował drzewa przez dołączanie liścia z każdą z trzech wag kwadratowych 1,2,3 do każdego wierzchołka. Klucz izomorfizmu to minimum leksykograficzne kodów nawiasowych dla wszystkich ukorzenień; kody poddrzew sortowane wraz z wagą krawędzi. Indukcja po usunięciu liścia daje kompletność. Dodatnia określoność symetrycznej macierzy 2I-P jest badana niezależnie od klasyfikacji: eliminujemy liść o pivocie p, aktualizując pivot sąsiada q do q-w/p, gdzie w jest kwadratem wagi krawędzi. Warunkiem jest dodatniość wszystkich pivotów, także ostatniego (dopełnienia Schura). Wszystkie obliczenia wymierne dokładne. Liczba nieizomorficznych ważonych drzew kolejno dla 1–8: 1,3,6,28,114,606,3298,19614; razem 23670. Dopuszczalne typy: A1; A2,BC2,G2; A3,BC3; A4,BC4,D4,F4; A5,BC5,D5; A6,BC6,D6,E6; A7,BC7,D7,E7; A8,BC8,D8,E8. Zgodność pełna. BC oznacza drzewo bez orientacji, zatem B i C nie są tu odróżniane. To regresja skończona, nie dowód ogólny.

## Wykonana niezależna kontrola realizacji ADE
Współrzędne całkowite w bazie prostej, macierz Grama C z przekątną 2 i wpisami -1 przy krawędziach. Wygenerowano orbity wszystkich wektorów standardowych pod odbiciami prostymi s_i(x)=x-(e_i^T C x)e_i, iterując do osiągnięcia domknięcia. Każdy wygenerowany korzeń ma normę kwadratową 2, przeciwieństwo w zbiorze, współrzędne jednolitego znaku. Dla każdej uporządkowanej pary a,b sprawdzono, że b-(a^T C b)a należy do zbioru. A1–A12: n(n+1) korzeni; D4–D12: 2n(n-1) korzeni; E6,E7,E8: 72,126,240 korzeni, odpowiednio 36,63,120 dodatnich. Wszystkie 24 układy i 348796 par zgodne. Iloczyny skalarne są całkowite. Sprawdzian orbit jest niezależny od argumentu realizacji przez wszystkie wektory normy 2; nie twierdzimy, że sam test wyczerpuje wszystkie wektory normy 2 bez dowodu.

## Kontrola dowodów
Argument zakazanych podgrafów w klasyfikacji skończonej, eliminacja krawędzi wielokrotnych, warunki Schura i realizacja jednokrawędziowa z kraty są poprawne w sprawdzanym zakresie. Nie znaleziono nowej usterki. Bez zmian źródła ani zakresu.

## CI
Run 45359728972, job 138326405458, in_progress/brak, kroki {"success":7,"in_progress":1,"pending":113}. Nie wykonano oględzin PDF w tej iteracji.

## Werdykt
Pierwszy czysty niezależny audyt po II: 1/2. AA-56 W AUDYCIE. Kolejna iteracja: kontrola modeli klasycznych, niezależności bazy i grup Weyla oraz CI i PDF. AA-57 nieotwarty.
