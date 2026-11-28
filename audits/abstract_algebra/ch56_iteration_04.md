# AA-56 — audyt IV: modele klasyczne, grupy Weyla i niezależność bazy

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob b75d8fac66195d710df141cdae3e3081b137d687, commit 78aad66a51ad2e4399df2621b8dafb81c3fd7f9c.

## Wykonane niezależne kontrole modeli klasycznych
W JavaScript wygenerowano jawne zbiory korzeni w standardowych współrzędnych dla A1–A12, B2–B12, C2–C12, D4–D12. Dla każdego korzenia obliczono współrzędne w bazie prostej niezależnie przez sumy prefiksowe: A/B — sumy prefiksowe, C — ostatnia suma podzielona przez dwa, D — ostatnie dwa współczynniki to połowa sumy wszystkich współrzędnych pomniejszona o ostatnią współrzędną oraz sama połowa sumy. Sprawdzono odtworzenie wektora, całkowitość i jednolity znak, dokładnie połowę dodatnich korzeni, liczebności n(n+1), 2n², 2n², 2n(n-1) oraz wszystkie wpisy macierzy Cartana. Dla każdej uporządkowanej pary korzeni a,b sprawdzono podzielność 2(a,b) przez (a,a) oraz przynależność odbicia do zbioru.
Wyniki: A — 12 układów, 73528 par; B — 11 układów, 242836 par; C — 11 układów, 242836 par; D — 9 układów, 196608 par. Razem 43 układy i 755808/755808 par poprawnych.

## Niezależna enumeracja grup Weyla
Wygenerowano grupy permutacji ze znakami przez iterowane mnożenie przez odbicia proste: sąsiednie transpozycje dla A; dodatkowa zmiana znaku ostatniej współrzędnej dla B/C; dodatkowa transpozycja ostatnich dwóch współrzędnych ze zmianą obu znaków dla D. Klucze to uporządkowane krotki podpisanych indeksów, każda operacja całkowita.
Rzędy A1–A6: 2,6,24,120,720,5040; B/C2–B/C6: 8,48,384,3840,46080; D4–D6: 192,1920,23040. Razem 14 grup (B i C mają identyczne odbicia), 81424 elementy zliczone w tych enumeracjach. Wszystkie rzędy zgodne z (n+1)!, 2^n n!, 2^(n-1)n!. W D każda otrzymana permutacja ma parzystą liczbę zmian znaków. Orbita wektora o parami różnych dodatnich współrzędnych miała w każdym przypadku liczebność grupy; dla A można odjąć średnią, nie zmieniając stabilizatora. To regresja konkretnych przypadków, nie dowód ogólnego twierdzenia o stabilizatorach komór.

## Kontrola dowodów
Sprawdzono wzory na bazę prostą w modelach klasycznych, szczególnie D z j=n i C z ostatnim korzeniem 2e_n. Argument generowania wszystkich zmian znaków, rozkładu półprostego i wierności działania A na hiperpłaszczyźnie jest poprawny. Ponownie prześledzono przechodniość na komorach przez maksymalizację iloczynu z h, przejście do baz przez nierozkładalne korzenie dodatnie oraz niezmienniczość parowań Cartana przy podobieństwie. Nie znaleziono nowej usterki. Bez zmian źródła i zakresu.

## CI
Run 45359728972, job 138326405458: in_progress; ostatni odczyt 50 success, 1 in_progress, 70 pending; krok Run AA-X11 finite-field polynomial factorization and Mobius tests. Brak artefaktu. Nie wykonano oględzin PDF.

## Werdykt
Dwa czyste niezależne audyty po II: 2/2. AA-56 W AUDYCIE TECHNICZNYM do pełnego CI i oględzin aktualnego PDF. AA-57 nieotwarty.
