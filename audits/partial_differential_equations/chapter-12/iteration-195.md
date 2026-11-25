# RRC 12 — iteracja 195, druga lektura 013–026

Ponownie odczytano pełne sekcje o rozkładzie spektralnym i zasadzie min–max. Źródło przed 07303ce043dcd0e8e0fb23df97e40c8f5d817783, po f3ef0340fadd2c0e54083943faa6d4ca36c56f88, commit df76d69c4fa2687b6648974d6711fc009e50d40e.

| Kryterium | Wynik drugiej lektury |
|---|---|
| PDE-12-013 | Przypadki zerowe, skończone i nieskończone — poprawne. |
| PDE-12-014 | Usunięto przedwczesne stwierdzenie równości normy z supremum; jawny wybór wektora normującego, poprawna nierówność dla formy półokreślonej. |
| PDE-12-015 | Poprawiono zapis oszacowania granicy zespolonej przez moduł; wyjaśniono testy y i iy. Argument zwartości i osiągania maksimum poprawny. |
| PDE-12-016 | Rozpisano znak części urojonej i ortogonalność Kx-mx do całej przestrzeni. |
| PDE-12-017 | Uzasadniono niezmienniczość kolejnych dopełnień i własności ograniczeń oraz dolne oszacowanie odległości obrazów wektorów własnych. |
| PDE-12-018 | Obie inkluzje jądra poprawne, rozpisano rzut równania na jądro i porównanie współczynników. |
| PDE-12-019 | Zastąpiono odwołanie do diagonalizacji skończeniewymiarowej jawnym rozkładem na części dodatnią i ujemną za pomocą inwolucji; wykazano krotności i zanik modułów wartości własnych. |
| PDE-12-020 | Dodano dokładne odwołanie do dodatniego twierdzenia spektralnego i nierówności Poincarégo; przejście od B do A i krotności poprawne. |
| PDE-12-021 | Jawna normalizacja bazy w V i definicja mu_j; poprawiono niejednoznaczny zapis c_j dla v; dodano polaryzowaną tożsamość energii. |
| PDE-12-022 | Obie implikacje charakterystyki D(A), waga lambda² i przejście do granicy przez gęstość poprawne. |
| PDE-12-023 | Doprecyzowano odwzorowanie liniowe i wymiar jego jądra, również k=1. Istnienie maksimum i obie nierówności poprawne. |
| PDE-12-024 | Najlepsza stała Poincarégo i osiąganie równości poprawne. |
| PDE-12-025 | Przedłużenie przez zero i monotoniczność poprawne. |
| PDE-12-026 | Uzasadniono brak dodatkowych wartości własnych na odcinku, rozpisano normalizację na prostokącie i przykładowe krotności na kwadracie. |

18 zmian blokowych. Zachowano kolejność 33 etykiet; wszystkie 40 wystąpień odsyłaczy (26 różnych celów) rozwiązane w rozdziałach 05,06,08,09,10,11,12,15. Nie wykryto duplikatów etykiet w tych plikach, stos środowisk poprawny. Ponownie odczytano tezy lematu o słabej zwartości, nierówności Poincarégo i twierdzenia o bazie sinusowej. Dodatkowe kontrole skończone: 48 obliczeń ortogonalności i normalizacji sinusów metodą punktu środkowego (512 węzłów) oraz sprawdzenie pierwszych trzech wartości na kwadracie (2,5,5 w jednostkach pi²/L²); 49/49 PASS. Nie są to dowody twierdzeń.

Pierwsza lektura 68/68, druga 26/68. Nie przeprowadzono kompilacji, dedykowanego CI, kontroli wizualnej PDF ani Lean. Następnie druga lektura 027–040: widmo, rezolwenta, Fredholm i kontrprzykład na R^d.
