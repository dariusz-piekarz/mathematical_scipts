# AA-55 — audyt III: niezależna enumeracja drzew i rekurencja charakterów

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 7e6c96ef96bd8f9d6a13b0443e357c738ff6743f, commit 390bae3d002356f1b48ab811f226df4034acc8ab.

## Kontrola klasyfikacji
Wykonano niezależny kod JavaScript z arytmetyką wymierną BigInt. Generacja wszystkich drzew nieizomorficznych rozpoczyna się od jednego wierzchołka, a następnie dołącza nowy liść do każdego wierzchołka każdego drzewa poprzedniego rzędu. Kod kanoniczny to leksykograficznie najmniejsze spośród wszystkich kodowań nawiasowych drzewa ukorzenionego w kolejnych wierzchołkach (poddrzewa sortowane). Każde drzewo ma liść, więc indukcyjnie metoda obejmuje wszystkie typy. Liczby uzyskanych drzew dla rzędów 1–12: 1,1,1,2,3,6,11,23,47,106,235,551; razem 987.

Niezależne kryterium: eliminacja liści w macierzy 2I-A. Początkowo każdy pivot wynosi 2; po usunięciu liścia z pivotem p aktualizujemy pivot sąsiada q do q-1/p. Sprawdzamy, że wszystkie wcześniejsze pivoty są dodatnie, a ostatni jest zero. Kryterium jest równoważne istnieniu dodatniego wektora w jądrze: jeśli taki wektor istnieje, równanie w liściu daje dodatni pivot jako iloraz wartości sąsiada i liścia, a dopełnienie Schura zachowuje dodatnie ograniczenie wektora; odwrotnie, od dodatniej wartości w ostatnim wierzchołku odtwarzamy wartości w liściach przez dzielenie przez dodatnie pivoty. Nie stosowano klasyfikacji ramion przy samym teście.

Wyniki: brak drzew dopuszczalnych dla 1–4; D4 dla 5, D5 dla 6, D6/E6 dla 7, D7/E7 dla 8, D8/E8 dla 9, D9 dla 10, D10 dla 11, D11 dla 12. 11 drzew dopuszczalnych, wszystkie zgodne z klasyfikacją. To skończona regresja, nie zastępuje dowodu ogólnego.

## Kontrola rekurencji
Drugi niezależny kod JavaScript BigInt: dla każdej grupy sprawdzono Ad=2d, nieujemność wszystkich krotności m_k, wymiar d^T m_k=k+1 i współczynnik trywialny, k=0,...,120.
- C_m, m=1,...,80: 9680 przypadków. Porównanie z liczbą j=0,...,k dla których m dzieli k-2j. Grupa trywialna: macierz (2); C2: podwójna krawędź.
- Dic_n, n=2,...,40: 4719 przypadków. Niezależna formuła z uśrednienia charakteru na dwóch warstwach: (N_k+c_k(0))/2, gdzie N_k zlicza j z 2n dzielącym k-2j, a c_k(0)=0 dla k nieparzystego, (-1)^(k/2) w przeciwnym razie. Wynika z diagonalnych elementów a^j i śladu zero elementów a^j J.
- 2T,2O,2I: 363 przypadki, porównanie z szeregiem Hilberta AA-54.
Razem 14762/14762 przypadków zgodnych. Wszystkie sprawdzane wymiary i krotności są dokładnymi liczbami całkowitymi.

Przejrzano argument klasyfikacji w aktualnym źródle po II: przypadki wielokrotnej krawędzi, cyklu, drzewa o dużym stopniu, dwóch rozgałęzień, ścieżki i trzech ramion są wyczerpujące. Równanie centralne oraz argument jednoznaczności dodatniego wektora są poprawne. Nie znaleziono nowej usterki. Nie zmieniono źródła ani zakresu. Propozycja macierzy Cartana pozostaje w raporcie II.

## CI
Run 45356544087, job 138315680615: completed/success, 120 kroków success. Artefakt 14903355925 dostępny; w tej iteracji nie oglądano PDF.

## Werdykt
Pierwszy czysty audyt po korektach II: 1/2. AA-55 W AUDYCIE; kolejny audyt powinien niezależnie sprawdzić argumenty reprezentacyjne, abelianizacje, odsyłacze i skład PDF. AA-56 nieotwarty.
