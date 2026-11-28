# GT — audyt kontrolny 318

Punkt odniesienia: 4605e323f4ec3d0d7bc2dc63df7298d8df1d2052 (ustalony commit, odczyt 42 plików w trzech partiach po 14, zgodność każdego SHA z listą katalogu).

| Zakres | Etykiety | Wystąpienia odsyłaczy | Środowiska proof | Środowiska tikzpicture |
|---|---:|---:|---:|---:|
| 00–13 | 182 | 142 | 139 | 46 |
| 14–27 | 203 | 212 | 143 | 33 |
| 28–34, 37–43 | 353 | 251 | 163 | 24 |
| Razem | 738 | 605 | 445 | 103 |

Wszystkie 42 pliki obecne dokładnie raz w pliku książki, brak plików osieroconych i nieznanych wejść. Kolejność 00–05,37–43,06–34 zachowana. W każdej partii brak powtórzonych etykiet i błędów zagnieżdżenia środowisk w prostym skanerze po odrzuceniu komentarzy. Porównanie list etykiet i 49 zewnętrznych względem partii celów odsyłaczy nie ujawniło brakującego celu ani kolizji między partiami. Skan nie zastępuje parsera TeX ani testu test_graph_and_knot_global.py --strict. Liczba środowisk proof nie stanowi miary kompletności dowodów.

Ponowna kontrola merytoryczna wybranych dowodów: GT01 Havel–Hakimi (zamiana czterech różnych wierzchołków, zachowanie stopni i argument maksymalności); GT02 rozkład parzystego podgrafu na cykle, baza cykli fundamentalnych (indukcja, niezależność, eliminacja krawędzi pozadrzewowych); GT03 Robbins (drzewo DFS, własność przodków, krawędź wychodząca z poddrzewa, ścisły spadek głębokości). W tych dowodach nie wykryto nowej luki. To kontrola wybranych dowodów, a nie odbiór wszystkich twierdzeń GT01–03. Źródeł rozdziałów nie zmieniano.

CI źródłowego commitu GT 57fd33576dd76f9f612a2e3afcb69d88af46c1d7: pełny audyt 45982638459, algorytmy 45982638663, aplikacja 45982638608 — queued podczas odczytu. Workflow pełny przewiduje potrójną kompilację i odrzucenie ostrzeżeń; brak dowodu jej wykonania. Nie przeprowadzono kontroli wizualnej PDF.

Następny krok: dalszy audyt szczegółowości dowodów od GT01 (Erdős–Gallai) i GT04–06, a następnie kontrola pozostałych bloków; odbiór CI i PDF osobno. Nie zamykać stabilizacji.
