# RRC 12 — iteracja 190, pierwsza lektura 013–026

Źródło przed f9fc2266096a37bbd73d0c2e0f1dc48b443c9e00, po 26970b097e7ceee35519919ebc0a7d7b13b59b2b, commit 2ee8f6e5b5981bf698d3a05e6ad0b3b81c21c433. Odczytano pełne sekcje twierdzeń spektralnych, dziedziny formy i min–max; sprawdzono odwołanie do bazy sinusowej w rozdziale 06.

| ID | Kotwica | Wynik pierwszej lektury |
|---|---|---|
| PDE-12-013 | thm:pde12-compact-spectral | Przypadek K=0, układ pusty, skończony wymiar — uzupełniono. |
| PDE-12-014 | thm:pde12-compact-spectral | Cauchy–Schwarz dla dodatniej formy, także z zerową wartością na przekątnej, i równość normy z supremum — uzupełniono. |
| PDE-12-015 | thm:pde12-compact-spectral | Słaby podciąg, również w zespolonej przestrzeni, silna zbieżność po zastosowaniu K i granica ilorazu Rayleigha — uzupełniono. |
| PDE-12-016 | thm:pde12-compact-spectral | Różniczkowanie ilorazu dla t rzeczywistego, test iy, wektor własny — uzupełniono. |
| PDE-12-017 | thm:pde12-compact-spectral | Iteracja na niezmienniczych dopełnieniach, monotoniczność i zanik wartości własnych — uzupełniono. |
| PDE-12-018 | thm:pde12-compact-spectral | Obie inkluzje dla jądra i dopełnienia, pełne rozwinięcie oraz krotności — uzupełniono. |
| PDE-12-019 | thm:pde12-compact-general-spectral | K² dodatni i zwarty, równość jąder, niezmienniczość przestrzeni własnych i diagonalizacja — uzupełniono. |
| PDE-12-020 | cor:pde12-eigen | Nieskończony wymiar L², przynależność funkcji własnych do D(A), dodatniość, krotności i granica — uzupełniono. |
| PDE-12-021 | thm:pde12-formdomain | Baza ortonormalna V, zupełność, Parseval i obie implikacje sumowalności z wagą lambda — uzupełniono. |
| PDE-12-022 | thm:pde12-formdomain | Dziedzina operatora: waga lambda², przejście do V, równanie dla testów i gęstość — uzupełniono. |
| PDE-12-023 | thm:pde12-minmax | Istnienie maksimum na zwartej sferze, górna i dolna nierówność oraz osiąganie minimum — uzupełniono. |
| PDE-12-024 | cor:pde12-first | Ostrość stałej Poincarégo, przypadek zerowy — uzupełniono. |
| PDE-12-025 | cor:pde12-first | Przedłużenie przez zero przez gęstość testów, izometria i monotoniczność wartości własnych — uzupełniono. |
| PDE-12-026 | sec:pde12-minmax | Normalizacja, równania własne oraz zupełność bazy na prostokącie przez Fubiniego i bazy sinusowe — uzupełniono. |

19 zmian tekstowych, zachowano 33 etykiety w tej samej kolejności. 31 wystąpień odsyłaczy (21 różnych), wszystkie rozwiązane w 06,09,10,11,12,15; brak duplikatów etykiet w sprawdzanych plikach; stos środowisk poprawny. Pierwsza lektura: 26 kryteriów łącznie z iteracją 189. Nie wykonano testów wykonywalnych, CI, kompilacji PDF ani Lean. Następny etap: widmo, rezolwenta i alternatywa Fredholma. Liczba końcowa kryteriów jeszcze nieustalona.
