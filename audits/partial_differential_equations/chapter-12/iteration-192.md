# RRC 12 — iteracja 192, pierwsza lektura 041–054

Źródło przed 0e4ed3daf86a78c8bcf8bb2bc861e910b42707e0, po 4e3f715e61f85a7f3773169391ff980d1d551661. Commity 2cac3fd064e0fec5a58f66f01c46f6705af1eea1 i e04ea2f6780cb2579e17f65016b1a71dc4f37f36. Pełny odczyt sekcji o półgrupie cieplnej i Duhamelu.

| ID | Kotwica | Wynik pierwszej lektury |
|---|---|---|
| PDE-12-041 | sec:pde12-heat | Definicja półgrupy i liniowość generatora — uzupełniono. |
| PDE-12-042 | thm:pde12-heat | Zbieżność szeregu, liniowość, dokładna norma i własność półgrupy — uzupełniono. |
| PDE-12-043 | thm:pde12-heat | Zbieżność zmajoryzowana i obustronna ciągłość silna — uzupełniono. |
| PDE-12-044 | thm:pde12-heat | Indukcyjna charakterystyka dziedzin potęg A — pełny dowód. |
| PDE-12-045 | thm:pde12-heat | Maksimum x^m exp(-tx), oszacowanie wygładzające i zakres m — uzupełniono. |
| PDE-12-046 | thm:pde12-heat | Obie inkluzje dziedziny generatora, jawna sumowalna majoranta — uzupełniono. |
| PDE-12-047 | thm:pde12-heat | Komutacja A i S(t), ciągłość grafowa, obie pochodne i regularność dla t>0 — uzupełniono. |
| PDE-12-048 | thm:pde12-heat | Jednoznaczność rozwiązania jednorodnego przez skalarne równania modalne — dodano. |
| PDE-12-049 | thm:pde12-duhamel | Wspólna ciągłość, całkowalność Bochnera, oszacowanie i ciągłość rozwiązania łagodnego — uzupełniono. |
| PDE-12-050 | thm:pde12-duhamel | Różniczkowanie po zmianie zmiennej, obie strony i końce przedziału, ciągłość F' — uzupełniono. |
| PDE-12-051 | thm:pde12-duhamel | Całkowanie w normie grafowej na odciętym przedziale, przenoszenie A pod całkę — pełne uzasadnienie. |
| PDE-12-052 | thm:pde12-duhamel | Reguła iloczynu, całkowanie przez części, granica przez domkniętość A, ciągłość grafowa także w zerze — uzupełniono. |
| PDE-12-053 | thm:pde12-duhamel | Zgodność klasycznego i łagodnego rozwiązania przez równania modalne; rozróżnienie hipotez o f — uzupełniono. |
| PDE-12-054 | sec:pde12-heat | Wygładzanie przestrzenne we wnętrzu dla równania jednorodnego przez iterację regularności eliptycznej, bez obietnicy gładkości przy brzegu lub dla dowolnego f — uzupełniono. |

15 zmian blokowych plus korekta składni i miar całkowania. Zachowano 33 etykiety w tej samej kolejności, 36/36 odsyłaczy (25 różnych celów) rozwiązanych w rozdziałach 06,08,09,10,11,12,15; brak duplikatów etykiet w sprawdzonych plikach; stos środowisk poprawny. Sprawdzono źródło AF 15B (kryterium całkowalności Bochnera) i twierdzenie o bootstrapie z RRC 15. Dodatkowo 20 skończonych kontroli oszacowania wygładzającego dla różnych m,t i 16 kontroli tożsamości F'+lambda F=t dla prawej strony f(t)=t w pojedynczym modzie (wszystkie 36 zaliczone, nie są dowodem twierdzeń). Pierwsza lektura 54 kryteria łącznie z iteracjami 189–191. Nie uruchamiano dedykowanych testów repozytorium, CI, kompilacji PDF ani Lean. Następna iteracja: równanie falowe, zachowanie energii i przepływ Schrödingera. Końcowa liczba kryteriów jeszcze nieustalona.
