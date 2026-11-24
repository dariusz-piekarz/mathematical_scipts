# AA-53 — audyt IV: operator Reynoldsa i skończona generowalność

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 5675bf04c336a76e6424eeca337f24b5f211aeb5, bez zmian.

## Kontrola matematyczna
Sprawdzono lewostronne działanie przez podstawienie odwrotności, permutowanie składników sumy przez lewostronne mnożenie, tożsamość rzutu na niezmienniki oraz jego liniowość względem pierścienia niezmienników. Skończony zbiór generatorów ideału dodatnich jednorodnych niezmienników można wybrać spośród pierwotnych jednorodnych generatorów przez noetherowskość; projekcja na jednorodną część stopnia d daje współczynniki stopni d-deg f_i. Uśrednienie zachowuje te stopnie i zapewnia niezmienniczość współczynników, więc indukcja silna jest poprawna. Przypadek I=0 oraz zerowymiarowa przestrzeń V są objęte dowodem. We wzorze Moliena ślad rzutu to wymiar obrazu, a zamiana g na g^-1 jest dozwolona dopiero po sumowaniu po grupie. Nie znaleziono nowych luk ani potrzeby zmian redakcyjnych.

## Wykonana niezależna kontrola
Uruchomiono JavaScript z dokładną arytmetyką BigInt i rzadkimi wielomianami o całkowitych współczynnikach dla działania C3 i S3 przez permutacje trzech zmiennych. Użyto sumy P=|G|R zamiast dzielenia. Dla wszystkich monomów trzech zmiennych stopni 0–15 (816 na grupę) obliczono P bezpośrednio ze wszystkich permutacji. Zweryfikowano P²=|G|P (1632 przypadki), gP=P dla każdego g (7344 przypadki), P(af)=aP(f) dla każdego z trzech elementarnych wielomianów symetrycznych a (4896 przypadków). W każdym stopniu dla każdej grupy porównano ślad P z |G| razy liczbą orbit monomów (32 przypadki). Wszystkie asercje przeszły. Wymienione liczby obejmują łącznie 13904 asercje; test nie zastępuje dowodu ogólnego. Nie rozszerzano zakresu rozdziału.

## CI
Run 45348236656, head 3d9d4373b9a1c3e369394912a6dbdf27c752ee7d, job 138287946248: status in_progress, conclusion brak, kroki {"success":7,"in_progress":1,"pending":107}. PDF aktualnej wersji pozostaje niezweryfikowany.

## Werdykt
Drugi czysty przegląd matematyczny po II (2/2); źródło bez zmian. AA-53 W AUDYCIE do potwierdzenia właściwego CI i obejrzenia wszystkich stron PDF. AA-54 nieotwarty.
