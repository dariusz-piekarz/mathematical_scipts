# PDE-03 — zamknięcie audytu (iteracja 41, 2026-11-24)

Status: ustabilizowany w zakresie rozdziału i obowiązkowego audytu klasycznego, bez deklaracji formalizacji Lean.
Źródło: chapters/pl/partial_differential_equations/03-rownania-laplace-a-i-poissona.tex, blob 2312e3e42efd784285c58712f17341ed886f5893, ostatnia zmiana cad73a600017460ada11f78e10d0278fd8445ed3.
Rejestr: tests/mathematical/partial_differential_equations/chapter-03/regression.md, blob 09d711b62cb6c28f0c4605472ae3ef67b4bc8c0e.

## Końcowy niezależny przegląd sekcji 3.6–3.10
Ponownie przeczytano wszystkie pięć sekcji i sprawdzono:
- 010–010B: przedłużenie przez zero, zwarty nośnik, dodatni margines Q_R na rozszerzonym iloczynie kul, dominację i harmoniczność poprawki, całkowalność potencjału, zerowanie na brzegu; obie nierówności barierowe i przykład ostrej stałej bez stosowania twierdzenia o zwartym nośniku do stałego wymuszenia.
- 011: skalowanie miary sfery i jądra, współczynniki dwumianowe, norma ważonych współczynników, wspólny promień, bezwzględna zbieżność, zamiana sum i całek, różniczkowanie na mniejszych sześcianach.
- 012–012A: dokładność formy na obszarze jednospójnym jako jawnie przywołane twierdzenie, konstrukcja potencjału, pochodne i równania Cauchy'ego–Riemanna, harmoniczność i jednoznaczność, okres na pierścieniu.
- 013–013B: normalizację Fouriera i całkowanie przez części, sumę szeregu geometrycznego, zbieżność pochodnych kartezjańskich również w zerze, odzyskanie danych brzegowych i nieciągłość odwrotnego odwzorowania T_r.
- 014–015: różnicę między istnieniem, jednoznacznością i stabilnością, kontrprzykład na przekłutej kuli w n≥2, zgodność podsumowania z zakresem twierdzeń i jawnie przywołanymi wynikami.

Nie znaleziono nowych istotnych błędów w tych pięciu sekcjach. Iteracje 39–41 razem stanowią pełny niezależny przegląd 10/10 sekcji po ostatniej korekcie układu; nie są trzema pełnymi audytami całego rozdziału. Pierwszy pełny przebieg matematyczny wykonano w iteracjach 28–36, korektę wizualną w 38, niezależną kontrolę po niej w 39–41. Wszystkie 12 pierwotnych pozycji kolejki mają odpowiadające kryteria i zostały opracowane. Nie stwierdzono otwartych istotnych usterek w audytowanym zakresie. Wyniki przywołane bez dowodu pozostają tak oznaczone.

## Weryfikacja końcowa
W tej iteracji rzeczywiście uruchomiono lokalnie test_laplace_poisson.py po porównaniu git hash-object z repozytorium: ab010d105b9a731d56ad5c7f61be52171270328f. Wynik: Ran 7 tests in 0.017s, OK. Testy są skończonymi kontrolami rachunków, nie formalnymi dowodami. Sprawdzono 47 unikatowych etykiet, 46 odsyłaczy, 30 unikatowych ID i ich kotwice, zagnieżdżenie środowisk oraz występowanie każdego z trzech zewnętrznych celów dokładnie raz w odpowiednich rozdziałach.
Porównano z commitem CI ed7a018fd418ef88f1008da3de02b1f95df3b878 wszystkie 10 plików wejściowych workflow: źródło, rejestr, test, workflow, rozdziały 01 i 19, książkę, manifest, listings i preambułę Atlasu. Wszystkie bloby identyczne. Job 138694173032 (run 45464079233): wszystkie kroki sukces, w tym testy, kompilacja i renderowanie. Nie uruchamiano ponownej kompilacji w tej iteracji. Kontrola wizualna dwóch rysunków po ostatniej poprawce udokumentowana w iteration-39.md (artefakt 14954956784, strony 11 i 20, PDF 21 stron); nie powtarzano oględzin w tej iteracji.
Nie kompilowano całej książki. Nie uruchamiano Lean. Zamknięcie dotyczy audytu rozdziału, a nie formalnej weryfikacji wszystkich twierdzeń ani pozostałych rozdziałów.

Następny rozdział w kolejności manifestu: 04 — Równanie ciepła. Rozpocząć od przeglądu przygotowawczego, nie zmieniać ustabilizowanych rozdziałów bez nowej konkretnej usterki.
