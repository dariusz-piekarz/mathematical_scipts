# PDE-03 — iteracja stabilizacyjna 39 (2026-11-24)

Aktualne źródło: blob 2312e3e42efd784285c58712f17341ed886f5893. Rejestr 30 kryteriów: blob 09d711b62cb6c28f0c4605472ae3ef67b4bc8c0e. Źródło identyczne z wersją w przebiegu 45464079233 (commit ed7a018fd418ef88f1008da3de02b1f95df3b878).

## Dowody
Niezależnie ponownie przeczytano pełne sekcje 3.1–3.2: definicje, skalowanie sfery, pochodną średniej, Gaussa, granicę w zerze, całkowanie radialne; odwrotność z resztą Taylora, oba współczynniki i momenty sfery; radialny splot z dokładną równością i alternatywę nieradialną; zasadę maksimum lokalnego i globalnego, zasadę identyczności, gradient oraz Liouville'a. W szczególności sprawdzono zawieranie domkniętych kul w obszarze, dominację, warunki przejścia do granicy i brak uzależnienia podstawowego dowodu dla funkcji ciągłych od reprezentacji Poissona. Nie znaleziono nowego istotnego błędu w tych dwóch sekcjach. Nie jest to powtórny pełny audyt pozostałych ośmiu sekcji.

## CI i rysunki
Przebiegi 45464035707 i 45464079233 zakończone sukcesem. W drugim przebiegu job 138694173032 wszystkie kroki zakończone sukcesem, w tym 7 testów, kontrola struktury, kompilacja i renderowanie. Artefakt 14954956784 (6258194 bajtów) pobrano i rozpakowano. PDF A4, 21 stron, 21 obrazów PNG. Otworzono w pełnej rozdzielczości strony 11 i 20: inwersja z podpisem na stronie 11, wykres Fouriera wraz z podpisem na stronie 20; legenda poza krzywymi, bez kolizji. Kryteria wizualne 016–017 spełnione dla tego konkretnego blobu. Nie powtarzano wizualnego przeglądu pozostałych 19 stron w tej iteracji.

Źródło matematyczne i kryteria bez zmian. Pierwszy czysty przebieg stabilizacyjny w zakresie sekcji 3.1–3.2 i obu rysunków po poprawce. Cały rozdział pozostaje otwarty; przed zamknięciem potrzebny ponowny przegląd sekcji 3.3–3.10 oraz potwierdzenie braku nowych problemów. Nie kompilowano całej książki, nie uruchamiano Lean.
