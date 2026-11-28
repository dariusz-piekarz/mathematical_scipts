# AA-68 — audyt II: charaktery formalne, etap D otwarty

24 listopada 2026 r. Źródło 3189372249d8768dc9ea731fa3518d8e8cb35800, bez zmian matematycznych. Kontynuacja ch68_iteration_01.md, bez otwierania AA-69.

## Niezależna kontrola
1. Działania na charakterach: bazy wagowe czynników rzeczywiście dają bazę tensorową, a porównanie składowych względem wszystkich t identyfikuje właściwe przestrzenie wagowe; w przestrzeni sprzężonej znak jest ujemny, przedłużenie funkcjonału przez zero jest poprawne. Odbicia zachowują kratę, a augmentacja jest homomorfizmem.
2. Trójkątność: iloraz modułu Verma nie tworzy nowych wag, zachowuje jednowymiarową najwyższą składową i ma skończony wymiar na mocy AA-67.
3. Baza niezmienników: odwracalna całkowita macierz Cartana daje wymierne wysokości, niezależnie od ciała K. Każde maksimum wysokości jest dominujące, także przy remisie i układzie redukowalnym. Odejmowanie charakteru nie tworzy nowych wag na maksymalnej wysokości; para (maksymalna wysokość, liczba wag na niej) maleje leksykograficznie, a możliwych nieujemnych wysokości nie większych niż początkowa jest skończenie wiele. Argument obejmuje ujemne współczynniki całkowite i element zerowy. Niezależność wynika z wybrania maksymalnej wysokości w skończonej kombinacji. Nie użyto wzoru Weyla.
4. Charaktery wyznaczają moduły: pełna redukowalność i klasyfikacja AA-66–67 dają skończone sumy prostych składników; niezależność charakterów zapewnia równość krotności. W przypadku zerowym suma jest pusta.
5. Przykład sl2: dla k≤a oba współczynniki wynoszą min(b,k)+1; dla k>a oba wynoszą a+b−k+1, z warunkami 0≤k≤a+b i właściwej parzystości. Zamiana czynników jest izomorfizmem modułów. Przypadki a=0, b=0 są objęte wzorem.
Nie wykryto błędnej tezy ani istotnego przeskoku. Bez rozszerzania zakresu rozdziału. Źródło zawiera 7 etykiet i 12 różnych celów odsyłaczy.

## Wykonane regresje
Pobrano i wykonano istniejące skrypty JS:
- AA-68-CH-01, blob c6d56326ae652d79135454b97303127609daffb0: PASS, 441 iloczynów, 9261 współczynników, 31 kombinacji wirtualnych.
- AA-68-CH-02, blob 9244f5c58c76d31b921496ccf0805818ce8e5c97: PASS, 22 modele, 121 iloczynów, 25586 odbić, 12793 wagi.
Nowa trwała regresja AA-68-CH-03, źródło aa:tw:lie-character-basis, dodana do istniejącego skryptu test_abstract_algebra_ch68_independent.js, commit 2a5bba1c82efdd61c4810373bcd1a2752f7903a0, blob 8c75f72d98d3a32980a8459b37c25013d9c20c9b. Modele A1×A1, dokładne BigInt, podpisane kombinacje sum orbit. Sprawdza dominację wszystkich maksimów, ścisły spadek pary miar, niezmienniczość każdej reszty, rekonstrukcję i niezależny wzór różnic skończonych na współczynniki bazy. Wykonano rozszerzony skrypt: CH-02 i CH-03 PASS; CH-03: 108 przypadków, 1730 kroków, 1226 kroków z remisem, 830 z półcałkowitą wysokością, 832 z ujemnym współczynnikiem, jeden element zerowy. To regresje skończonych modeli, nie formalizacja Lean.

## CI
Run 45466578862, job 138702959439, failure na Validate chapter dependencies: niespójność katalogu mathematical_analysis_i i niezarejestrowany rozdział 15 tego skryptu, nie błąd AA-68. Nie ingerowano w równoległy skrypt. Run 45466587281, job 138702994118, na 8f8ae568f9dfc907035220ce8fe1c23cf1077387, przeszedł bramkę zależności i pozostawał w toku na Run repository tool tests (7 success, 138 pending). Nie potwierdzono pełnego CI po nowej regresji ani PDF; nie deklarować stabilności. Kolejna iteracja: potwierdzić pełne CI, log i wszystkie strony PDF AA-68, w razie potrzeby skorygować usterki; dopiero po zamknięciu D/P AA-69.
