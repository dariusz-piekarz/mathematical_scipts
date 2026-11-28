# AA-52 — audyt III: nakrycie i półniezmienniki

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Niezależne obliczenia
W lokalnym Python/SymPy odtworzono domknięcie trzech zbiorów generatorów kwaternionowych w dokładnych ciałach QQ(sqrt(2)) oraz QQ(sqrt(5)), otrzymując 24, 48, 120 elementów. Dla czterech kwaternionów h, r, u, i i trzech macierzy bazowych przestrzeni hermitowskiej sprawdzono tożsamość sprzężenia przez M(q) z obrotem PR_q P^T, gdzie P zamienia pierwszą i trzecią współrzędną. Wynik 12/12 PASS; sprawdzono również unitarność czterech macierzy M(q). Proces zakończył się kodem 0. W dodatkowym rachunku zliczono ślady reprezentacji naturalnej i zastosowano rekurencję charakterów Sym^d: chi_0=1, chi_1=t, chi_d=t chi_(d-1)-chi_(d-2). Uśrednienie po grupie dało dla d=0,...,12 listy 2T: [1,0,0,0,0,0,1,0,1,0,0,0,2]; 2O: [1,0,0,0,0,0,0,0,1,0,0,0,1]; 2I: [1,0,0,0,0,0,0,0,0,0,0,0,1]. W tym rachunku wynik przekonwertowano na int; jest on dodatkową diagnostyką, nie nowym twierdzeniem w rozdziale ani trwałą regresją. Nie przypisuje się temu wykonaniu weryfikacji całego CI.

## Poprawka matematyczna
Dopisano jawny wzór -i M(bi+cj+dk) i rzeczywistą zmianę współrzędnych (b,c,d)->(d,c,b). Pokazano, że -P ma wyznacznik +1, a jego podniesienie przez pi sprzęga modele w SU(2). Wzmocniono argument orbitowy: każdy niezerowy jednorodny półniezmiennik dodatniego stopnia d ma niepusty niezmienniczy zbiór zer rzutowych o liczności <=d (rozkład liniowy, również pierwiastek w nieskończoności). Stąd najmniejszy dodatni stopień półniezmiennika równa się najmniejszej liczności orbity. Dla 2T,2O,2I: 4,6,12. Nie utożsamiono półniezmienników z niezmiennikami ani nie rozszerzono zakresu na pełne tablice charakterów. Commit 52acf372ac64229c8f13fc20b6f62c88377c5b95, blob a151f25b5b4e083cf39621c34fb0bca6af3948fc.

## CI i status
Run 45304522955, job 138144964119, źródło audytu II (528d401474de0d29bf621d006ab713939c7b032a), w chwili kontroli in_progress: 7 success, 1 in_progress, 105 pending. Terminologia tego commita przeszła (45304523082). Nie ma podstaw do przypisania sukcesu aktualnemu źródłu audytu III. PDF po poprawce nie został obejrzany. AA-52 W AUDYCIE; AA-53 nieotwarty. Następny krok: CI aktualnego źródła, niezależna kontrola dowodu oraz wizualna kontrola PDF.
